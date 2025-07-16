# mapping_loader/mapping_generator.py

import difflib
from typing import Dict, Any
from model.signal import SignalNode

def generate_mapping(
    vss_signals: Dict[str, SignalNode],
    hal_properties: Dict[str, Dict[str, str]],
    typemap: Dict[str, Any]
) -> Dict[str, Dict[str, Any]]:
    """
    Generate a VSS to Android property mapping by fuzzy matching signal names.

    Args:
        vss_signals (Dict[str, SignalNode]): Flattened VSS signal objects
        hal_properties (Dict[str, Dict[str, str]]): Parsed Android HAL metadata
        typemap (Dict[str, Any]): Typemap configuration

    Returns:
        Dict[str, Dict[str, Any]]: Mapping dictionary
    """
    result = {}

    for signal_path, signal_node in vss_signals.items():
        signal_leaf = signal_node.name.upper()  # Last token of path

        closest_match = difflib.get_close_matches(signal_leaf, hal_properties.keys(), n=1, cutoff=0.6)

        if closest_match:
            matched_prop = closest_match[0]
            hal_info = hal_properties[matched_prop]
            result[signal_path] = {
                "aospId": f"VehicleProperty::{matched_prop}",
                "aospArea": f"VehicleArea::{hal_info['aospArea']}",
                "vhal_type": hal_info['vhal_type']
            }
        else:
            result[signal_path] = {
                "aospId": None,
                "aospArea": None,
                "vhal_type": None
            }

    return result

