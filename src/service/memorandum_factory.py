from pathlib import Path
from docxtpl import DocxTemplate


class MemorandumFactory:
    def __init__(self, project_root: str = "."):

        self.root = Path(project_root).resolve()
        self.templates_dir = self.root / "src" / "assets" / "docTemplates"
        self.output_dir = self.root / "output"
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.templates_map = self._scan_templates()

    def _scan_templates(self) -> dict:

        templates = {}
        if not self.templates_dir.exists():
            print(f"\033[93mWARNING: the templates folder does not exist in {self.templates_dir}\033[0m")
            return templates

        for docx_file in self.templates_dir.glob("*.docx"):
            templates[docx_file.stem] = str(docx_file.resolve())

        return templates

    def generate_memo(self, ia_response: dict) -> str:

        structure = ia_response.get("used_structure")
        payload = ia_response.get("payload", {})

        project_name = payload.get("project_name", "memo")

        path_template = self.templates_map.get(structure)

        if not path_template:

            print(f"\033[93mError: There is no registered template for the structure '{structure}'.\033[0m")

            print(f"Available templates: {list(self.templates_map.keys())}")
            return None

        try:
            doc = DocxTemplate(path_template)

            doc.render(payload)

            safe_project_name = project_name.replace(" ", "_")
            output_path = self.output_dir / f"{safe_project_name}.docx"

            doc.save(output_path)
            return str(output_path)

        except Exception as e:
            print(f"\033[93mError: error rendering or saving the docx: {e}\033[0m")
            return None


memorandum_factory = MemorandumFactory()
