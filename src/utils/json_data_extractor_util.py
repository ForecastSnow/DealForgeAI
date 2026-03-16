import json
import yaml

def json_data_extractor(path_json) -> str:
    try:
        
        with open(path_json, "r", encoding="utf-8") as f:
            data = json.load(f)

        return yaml.dump(
            data, 
            default_flow_style=False, 
            allow_unicode=True, 
            sort_keys=False
        )
    except Exception:
        print(f"\033[93mWARNING: Verify file integrity since the information could not be processed {path_json}\033[0m")
        return None
