import os

def get_all_folders(root_dir):
    """Recursively get all folders in the root directory."""
    folder_set = set()
    for dirpath, dirnames, _ in os.walk(root_dir):
        for dirname in dirnames:
            # Adding folder paths relative to the root directory
            folder_set.add(os.path.relpath(os.path.join(dirpath, dirname), root_dir))
    return folder_set

def create_missing_folders(source_root, dest_root):
    """Create folders missing in destination based on the source folder structure."""
    source_folders = get_all_folders(source_root)
    dest_folders = get_all_folders(dest_root)
    
    print("Source Folders:")
    for folder in sorted(source_folders):
        print(folder)

    print("\nDestination Folders:")
    for folder in sorted(dest_folders):
        print(folder)

    missing_folders = source_folders - dest_folders

    if not missing_folders:
        print("\nAll folders are present. No missing folders to create.")
        return

    print("\nMissing Folders:")
    for folder in sorted(missing_folders):
        print(folder)
        full_path = os.path.join(dest_root, folder)
        os.makedirs(full_path, exist_ok=True)
        print(f"Created: {full_path}")

    print(f"\n{len(missing_folders)} folders were created.")

# Example usage
source_server_path = r"C:\Users\prana\test2"
destination_server_path = r"C:\Users\prana\test"

create_missing_folders(source_server_path, destination_server_path)