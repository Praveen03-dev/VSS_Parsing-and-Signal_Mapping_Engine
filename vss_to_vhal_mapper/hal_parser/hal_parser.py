import re
from typing import Dict

def parse_types_hal(hal_file_path: str) -> Dict[str, Dict[str, str]]:
    """
    Parses the types.hal file to extract Android vehicle property metadata.

    Args:
        hal_file_path (str): Path to the Android types.hal file

    Returns:
        Dict[str, Dict[str, str]]: A dictionary where each key is a property name (e.g., PERF_VEHICLE_SPEED),
        and value is a dictionary with vhal_type and aospArea.

        Example:
        {
            "PERF_VEHICLE_SPEED": {"vhal_type": "FLOAT", "aospArea": "GLOBAL"},
            "ABS_ACTIVE": {"vhal_type": "INT32", "aospArea": "GLOBAL"},
            ...
        }

    Time Complexity: O(n), where n = number of lines in the file
    Space Complexity: O(m), where m = number of valid property entries
    """
    hal_property_pattern = re.compile(
        r'(\w+)\s*=\s*0x[0-9A-Fa-f]+,\s*//\s*(\w+)\s*\|\s*VehicleArea:\s*(\w+)',
        re.IGNORECASE
    )

    hal_properties = {}

    try:
        with open(hal_file_path, 'r') as file:
            hal_contents = file.read()
            matches = hal_property_pattern.findall(hal_contents)

            for property_name, vhal_type, area in matches:
                hal_properties[property_name] = {
                    "vhal_type": vhal_type.upper(),
                    "aospArea": area.upper()
                }

    except FileNotFoundError:
        raise FileNotFoundError(f"The types.hal file was not found at: {hal_file_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to parse types.hal: {str(e)}")

    return hal_properties
