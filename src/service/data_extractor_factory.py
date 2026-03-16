from pathlib import Path
from utils.json_data_extractor_util import json_data_extractor
from utils.pdf_data_extractor_util import pdf_data_extractor
from utils.excel_data_extractor_util import excel_data_extractor

class DataExtractorFactory:

    def __init__(self, root_folder: str = "input"):

        self.root = Path(root_folder)

    def scan_available_deals_data(self) -> list:

        if not self.root.exists():
            self.root.mkdir(parents=True, exist_ok=True)
            print(f"NOTICE: The '{self.root}' folder is empty.")
            return []

        if not any(self.root.iterdir()):
            print(f"NOTICE: The '{self.root}' folder is empty.")
            return []

        grouped_files = []

        for item in self.root.iterdir():

            if item.is_dir():
                folder_name = item.name

                files_in_folder = [
                    str(f.resolve()) for f in item.rglob("*") if f.is_file()
                ]

                grouped_files.append([folder_name, files_in_folder])

        return grouped_files

    def document_orchestrator(self, path_file) -> str:

        ext = Path(path_file).suffix.lower()

        if not ext:
            print(f"\033[93mWARNING: invalid file with no extension {path_file}. Skipping file...\033[0m")
            return None

        strategy = {
            ".json": json_data_extractor,
            ".pdf": pdf_data_extractor,
            ".xlsm": excel_data_extractor,
            ".xls": excel_data_extractor
            }

        extractor = strategy.get(ext)

        if extractor:
            return extractor(path_file)
        else:
            print(f"\033[93mWARNING: inregistered extension. '{ext}. Skipping file...'\033[0m")
            return None

    def data_builder(self, target_folder_name: str):

        available_deals = self.scan_available_deals_data()

        target_files = []
        for folder_data in available_deals:
            if folder_data[0] == target_folder_name:
                target_files = folder_data[1]
                break

        extracted_strings = []
        for path_file in target_files:
            result = self.document_orchestrator(path_file)

            if result:
                file_name = Path(path_file).name
                
                extracted_strings.append(f"<documento name='{file_name}'>\n{result}\n</documento>")

        string_final = "\n\n".join(extracted_strings)

        return string_final


data_extractor_factory = DataExtractorFactory()

