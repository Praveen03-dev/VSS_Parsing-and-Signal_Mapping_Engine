# merger/signal_merger.py

from typing import Dict
from model.signal import SignalNode

def merge_vss_with_mapping(
    vss_signals: Dict[str, SignalNode],
    mapping_data: Dict[str, Dict[str, str]]
) -> Dict[str, SignalNode]:
    """
    Merges parsed VSS SignalNode objects with Android mapping data.

    Args:
        vss_signals (Dict[str, SignalNode]): Parsed signal nodes
        mapping_data (Dict[str, Dict[str, str]]): Mapping from mapping.yml

    Returns:
        Dict[str, SignalNode]: Enriched SignalNode objects with aospId, aospArea, vhal_type
    """
    for signal_path, signal_node in vss_signals.items():
        android_info = mapping_data.get(signal_path, {})

        signal_node.aospId = android_info.get("aospId")
        signal_node.aospArea = android_info.get("aospArea")
        signal_node.vhal_type = android_info.get("vhal_type")

    return vss_signals
