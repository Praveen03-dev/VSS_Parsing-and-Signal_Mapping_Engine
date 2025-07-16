if __name__ == "__main__":
    import os
    import yaml
    import json

    from hal_parser.hal_parser import parse_types_hal
    from mapping_loader.mapping_loader import load_mapping
    from mapping_loader.mapping_generator import generate_mapping
    from signal_parser.vss_parser import load_vss_signals
    from merger.signal_merger import merge_vss_with_mapping

    # Step 1: Load parsed VSS signals (as SignalNode objects)
    vss_signals = load_vss_signals("sample_data/VehicleSignalSpecification.vspec")

    # Step 2: Parse HAL file for Android properties
    hal_properties = parse_types_hal("sample_data/types.hal")

    # Step 3: Load type mapping
    with open("sample_data/typemap.yml", "r") as f:
        typemap = yaml.safe_load(f)

    # Step 4: Generate mapping using fuzzy matching
    generated_mapping = generate_mapping(vss_signals, hal_properties, typemap)

    # Step 5: Write generated mapping to file
    with open("sample_data/mapping.yml", "w") as f:
        yaml.dump(generated_mapping, f)

    # Step 6: Reload mapping for validation/merging
    loaded_mapping = load_mapping("sample_data/mapping.yml")

    # Step 7: Merge VSS signals with Android mapping metadata
    merged_signals = merge_vss_with_mapping(vss_signals, loaded_mapping)

    # Step 8: Export enriched SignalNode objects to JSON
    enriched_dict = {signal_path: signal.to_dict() for signal_path, signal in merged_signals.items()}

    with open("sample_data/unified_signal_model.json", "w") as f:
        json.dump(enriched_dict, f, indent=2)

    print("\n✅ Unified signal model saved to: sample_data/unified_signal_model.json")

