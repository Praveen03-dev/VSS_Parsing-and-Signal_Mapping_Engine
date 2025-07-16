# Constants and enums for types
# VSS types
VSS_TYPES = {
    "boolean", "uint8", "int8", "uint16", "int16", "uint32", "int32", "float", "string"
}

# Android VHAL types (from typemap.yml or types.hal)
VHAL_TYPES = {
    "BOOLEAN", "INT32", "UINT32", "FLOAT", "INT16", "UINT16", "INT8", "UINT8"
}

# Example enum-like structure (optional with type hinting)
class VssDataType:
    BOOLEAN = "boolean"
    UINT8 = "uint8"
    INT8 = "int8"
    UINT16 = "uint16"
    INT16 = "int16"
    UINT32 = "uint32"
    INT32 = "int32"
    FLOAT = "float"
    STRING = "string"

class VhalType:
    INT32 = "int32"
    FLOAT = "float"
    BOOLEAN = "boolean"
