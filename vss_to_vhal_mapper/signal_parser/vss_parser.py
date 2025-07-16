# Parses .vspec and overlays using vspec-tools + anytree
# signal_parser/vss_parser.py

import yaml
from typing import Dict, Any
from model.signal import SignalNode

def flatten_vss_tree_to_nodes(node: Dict[str, Any], path: str = "") -> Dict[str, SignalNode]:
    """
    Recursively flattens the VSS signal tree into a flat dictionary of SignalNode objects.

    Args:
        node (Dict[str, Any]): Current subtree from the VSS YAML spec.
        path (str): Current dot-separated path being traversed.

    Returns:
        Dict[str, SignalNode]: Flattened signal dictionary where each value is a SignalNode.
    """
    signals = {}

    for key, value in node.items():
        full_path = f"{path}.{key}" if path else key

        if isinstance(value, dict):
            if "type" in value:
                signals[full_path] = SignalNode(
                    name=key,
                    path=full_path,
                    node_type="signal",
                    datatype=value.get("type"),
                    unit=value.get("unit"),
                    description=value.get("description", "")
                )
            else:
                # It's a branch
                signals.update(flatten_vss_tree_to_nodes(value, full_path))

    return signals

def load_vss_signals(vss_file_path: str) -> Dict[str, SignalNode]:
    """
    Loads the VSS YAML file and returns flattened SignalNode objects.

    Args:
        vss_file_path (str): Path to the .vspec YAML file

    Returns:
        Dict[str, SignalNode]: Flat dictionary of signal paths to SignalNode objects
    """
    with open(vss_file_path, "r") as f:
        tree = yaml.safe_load(f)

    return flatten_vss_tree_to_nodes(tree)
