from dataclasses import dataclass, field
from typing import Optional, Dict

@dataclass
class SignalNode:
    name: str
    path: str
    node_type: str  # e.g., "signal"
    datatype: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None

    aospId: Optional[str] = None
    aospArea: Optional[str] = None
    vhal_type: Optional[str] = None

    children: Dict[str, 'SignalNode'] = field(default_factory=dict)

    def to_dict(self):
        return {
            "name": self.name,
            "path": self.path,
            "type": self.node_type,
            "datatype": self.datatype,
            "unit": self.unit,
            "description": self.description,
            "aospId": self.aospId,
            "aospArea": self.aospArea,
            "vhal_type": self.vhal_type,
            "children": {k: v.to_dict() for k, v in self.children.items()}
        }

