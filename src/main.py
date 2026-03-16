import sys
from dotenv import load_dotenv

load_dotenv()

from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
)
import questionary

from service.data_extractor_factory import data_extractor_factory
from service.memorandum_factory import memorandum_factory
from service.ia_service import ia_service

console = Console()


def builder_orchestrator(target_folder_name: str) -> None:
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:

        task = progress.add_task(f"[cyan]Processing '{target_folder_name}'...", total=3)

        progress.update(
            task, description=f"[cyan]generating context for AI {target_folder_name}..."
        )
        memo_data = data_extractor_factory.data_builder(target_folder_name)
        progress.advance(task)

        progress.update(task, description="[yellow]Generating information with AI...")
        ia_response = ia_service.data_memo_generator(memo_data)

        if not ia_response.get("state"):
            console.print(
                f"\n[red]Error: The AI ​​service failed. Check API key, limits, or service status.[/red]"
            )
            return
        progress.advance(task)

        progress.update(task, description="[green]Creating document...")
        output_path = memorandum_factory.generate_memo(ia_response)
        progress.advance(task)

    if output_path:
        console.print(f"\n[bold green]Successfully generated in:[/bold green] [white]{output_path}[/white]")
        console.print("[bold blue]Consumption details:[/bold blue]")
        console.print(f"  [dim]>[/dim] Entry tokens: [yellow]{ia_response.get('input_tokens')}[/yellow]")
        console.print(f"  [dim]>[/dim] Output tokens:  [yellow]{ia_response.get('output_tokens')}[/yellow]")
        console.print(f"  [dim]>[/dim] Estimated cost:    [green]{ia_response.get('estimated_cost')}USD[/green]")
    else:
        console.print("\n[bold red]Something went wrong. Outpath failed. Empty.[/bold red]")


def generate_all() -> None:

    deals_data = data_extractor_factory.scan_available_deals_data()

    if not deals_data:
        console.print("[bold red]There are no folders in the input folder. Closing script.[/bold red]")
        
        sys.exit(0)

    folder_names = [deal[0] for deal in deals_data]

    for folder in folder_names:
        builder_orchestrator(folder)

    console.print("\n[bold green]Mass generation complete![/bold green]")


def main_menu() -> None:

    while True:
        console.print("\n")

        opcion = questionary.select(
            "Main menu.",
            choices=[
                "1. Generate a specific memorandum",
                "2. Generate all available memos",
                "3. Exit",
            ],
        ).ask()

        if opcion is None or opcion.startswith("3"):
            break

        if opcion.startswith("1"):

            deals_data = data_extractor_factory.scan_available_deals_data()

            if not deals_data:
                console.print("[bold red]There are no folders in the input folder. Closing script.[/bold red]")
                
                sys.exit(0)

            folder_names = [deal[0] for deal in deals_data]

            chosen_project_folder = questionary.select("Choose the project you want to process:", choices=folder_names).ask()

            if chosen_project_folder:
                builder_orchestrator(chosen_project_folder)

        elif opcion.startswith("2"):
            generate_all()


if __name__ == "__main__":
    main_menu()
