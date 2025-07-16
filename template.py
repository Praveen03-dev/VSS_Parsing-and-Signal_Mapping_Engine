import os

def touch(path, content=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_project_structure(base_path="."):
    # Top-level files
    files = {
        ".gitignore": "# Python\n__pycache__/\n*.pyc\n.venv/\n",
        "LICENSE": "MIT License\n\nCopyright (c) 2025",
        "README.md": "# VSS Parsing and Signal Mapping Engine\n\nThis project maps VSS signals to Android VHAL format.",
        "requirements.txt": "pyyaml\nanytree\nvspec-tools\nfuzzywuzzy\n"
    }

    for name, content in files.items():
        touch(os.path.join(base_path, name), content)

    # Main project directory
    mapper = os.path.join(base_path, "vss_to_vhal_mapper")
    os.makedirs(mapper, exist_ok=True)
    touch(os.path.join(mapper, "__init__.py"))
    touch(os.path.join(mapper, "main.py"),
          '# CLI entrypoint: calls parser, loader, merger\n')

    subdirs_with_files = {
        "signal_parser": {
            "vss_parser.py": "# Parses .vspec and overlays using vspec-tools + anytree"
        },
        "mapping_loader": {
            "mapping_loader.py": "# Loads and validates YAML mapping config",
            "mapping_generator.py": "# Auto-generates mapping.yml from VSS using fuzzy matching"
        },
        "hal_parser": {
            "hal_parser.py": "# Parses Android's types.hal and extracts aospId → type mappings"
        },
        "merger": {
            "signal_merger.py": "# Merges parsed VSS + mapping + HAL to final structure"
        },
        "model": {
            "signal.py": "# Data classes: Signal, MappedSignal",
            "constants.py": "# Constants and enums for types"
        },
        "tests": {
            "test_parser.py": "# Unit tests for parsers and merger"
        },
        "sample_data": {
            "VehicleSignalSpecification.vspec": "# Sample VSS file",
            "overlays/.keep": "",  # To keep empty overlays folder
            "mapping.yml": "# Output mapping file",
            "types.hal": "// Sample Android HAL definitions",
            "typemap.yml": "# Cross-type compatibility mappings"
        }
    }

    for subdir, files in subdirs_with_files.items():
        full_path = os.path.join(mapper, subdir)
        os.makedirs(full_path, exist_ok=True)
        touch(os.path.join(full_path, "__init__.py"))
        for filename, content in files.items():
            touch(os.path.join(full_path, filename), content)

    # README for the mapper folder
    touch(os.path.join(mapper, "README.md"),
          "# vss_to_vhal_mapper\n\nContains all logic for parsing, loading, merging VSS → VHAL mappings.")

    print(f"✅ Project structure created under: {os.path.abspath(base_path)}")

if __name__ == "__main__":
    create_project_structure()

