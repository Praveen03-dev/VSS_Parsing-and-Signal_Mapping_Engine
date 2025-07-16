# Loads and validates YAML mapping config
import yaml
from typing import Dict, Any

def load_mapping(mapping_file_path: str) -> Dict[str, Dict[str, Any]]:
    """
    Loads a mapping.yml file and returns it as a dictionary

    Args:
        mapping_file_path (str): Path to YAML file

    Returns:
        Dict[str, Dict[str, Any]]: Loaded mapping dictionary
    """
    try:
        with open(mapping_file_path, 'r') as f:
            data = yaml.safe_load(f)
        return data
    except Exception as e:
        raise RuntimeError(f"Error loading mapping file: {e}")
