import pandas as pd
import yaml


def excel_data_extractor(path_excel) -> str:
    try:
        df = pd.read_excel(path_excel, engine="openpyxl")

        df.dropna(how="all", inplace=True)
        df.dropna(axis=1, how="all", inplace=True)

        df.fillna("N/A", inplace=True)

        registros = df.to_dict(orient="records")

        return yaml.dump(
            registros, 
            default_flow_style=False, 
            allow_unicode=True, 
            sort_keys=False
        )
    except Exception:
        print(f"\033[93mWARNING: Verify file integrity since the information could not be processed {path_excel}\033[0m")
        return None
