def update_probe_locations(grid_file, target_file):
    # Read probe grid locations from file
    with open(grid_file, 'r') as f:
        grid_lines = f.readlines()

    # Format probe grid lines
    formatted_lines = ["            " + line.strip() + "\n" for line in grid_lines]
    #print(formatted_lines)

    # Read target file contents
    with open(target_file, 'r') as f:
        content = f.readlines()

    # Locate the probeLocations section in the target file
    start_idx = None
    end_idx = None
    for i, line in enumerate(content):
        if "probeLocations" in line:
            start_idx = i + 2  # Start after the probeLocations line
        elif start_idx and ")" in line:
            end_idx = i
            break

    # Replace the probeLocations section
    if start_idx is not None and end_idx is not None:
        content = content[:start_idx] + formatted_lines + content[end_idx:]

    # Write updated content back to the target file
    with open(target_file, 'w') as f:
        f.writelines(content)

    print("Probe locations updated successfully.")

# Example usage
update_probe_locations('probe_grid.txt', 'system/controlDict_test')
