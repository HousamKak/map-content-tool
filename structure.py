import os
import json
import urwid
import logging
import sys

# Set up logging
logging.basicConfig(
    filename="file_selector.log",  # Log filename
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Default to INFO
)

# Global exception handler
def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    """Log all uncaught exceptions to the error log."""
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    print("An error occurred. Check 'file_selector.log' for details.")
    sys.exit(1)

# Assign the handler to sys.excepthook
sys.excepthook = log_uncaught_exceptions

# Recursively get the folder structure excluding specified directories
def get_folder_structure(path, exclude_dirs=None):
    logging.info(f"Scanning folder structure at path: {path}")
    if exclude_dirs is None:
        exclude_dirs = ["node_modules", ".git"]

    folder_structure = {}

    # Skip excluded directories
    if os.path.basename(path) in exclude_dirs:
        logging.info(f"Skipping excluded directory: {path}")
        return None

    if os.path.isdir(path):
        logging.info(f"Processing directory: {path}")
        folder_structure["name"] = os.path.basename(path)
        folder_structure["path"] = path
        folder_structure["type"] = "directory"
        folder_structure["items"] = []

        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            item_structure = get_folder_structure(item_path, exclude_dirs)
            if item_structure:
                folder_structure["items"].append(item_structure)
    else:
        logging.info(f"Processing file: {path}")
        folder_structure["name"] = os.path.basename(path)
        folder_structure["path"] = path
        folder_structure["type"] = "file"

    return folder_structure

# Write the selected file contents directly to the structure
def embed_selected_contents(folder_structure, selected_files):
    if folder_structure["type"] == "file" and folder_structure in selected_files:
        try:
            logging.info(f"Reading content for file: {folder_structure['path']}")
            with open(folder_structure["path"], "r", encoding="utf-8") as f:
                folder_structure["contents"] = f.read()
        except Exception as e:
            logging.error(f"Error reading file {folder_structure['name']}: {e}")
            folder_structure["contents"] = f"Error reading file: {e}"
    elif folder_structure["type"] == "directory":
        for item in folder_structure.get("items", []):
            embed_selected_contents(item, selected_files)

# Class representing a tree node (directory or file)
class TreeNode(urwid.WidgetWrap):
    def __init__(self, file, is_selected=False, depth=0):
        self.file = file
        self.depth = depth  # Depth in the tree
        symbol = "+" if file["type"] == "directory" else "-"
        display_name = f"{'|   ' * depth}{symbol} {file['name']}"
        self.attr_map = urwid.AttrMap(
            urwid.Text(display_name),
            "selected" if is_selected else "normal",
            focus_map="focus",
        )
        super().__init__(self.attr_map)

    def selectable(self):
        return True

    def update_state(self, is_selected):
        """Update the row's appearance based on its selection state."""
        logging.info(f"Updating state for: {self.file['name']} - {'Selected' if is_selected else 'Deselected'}")
        self.attr_map.set_attr_map({"normal": "selected" if is_selected else "normal"})

# Generate the tree structure recursively
def generate_tree_structure(folder_structure, selected_files, depth=0):
    logging.info(f"Generating tree structure at depth: {depth}")
    rows = []
    for item in folder_structure.get("items", []):
        rows.append(TreeNode(item, item in selected_files, depth))
        if item["type"] == "directory":
            rows.extend(generate_tree_structure(item, selected_files, depth + 1))
    return rows

# Interactive terminal UI using urwid
class FileSelector:
    def __init__(self, folder_structure):
        logging.info("Initializing FileSelector UI")
        self.folder_structure = folder_structure
        self.selected_files = []
        self.palette = [
            ("normal", "default", "default"),
            ("focus", "light gray", "dark blue"),
            ("selected", "light green", "default"),
        ]
        self.rows = generate_tree_structure(folder_structure, self.selected_files)
        self.walker = urwid.SimpleFocusListWalker(self.rows)
        self.listbox = urwid.ListBox(self.walker)
        self.view = urwid.Frame(
            self.listbox,
            footer=urwid.Text("Use arrow keys to navigate, Space or click to toggle, Enter to submit, Q to quit."),
        )

    def toggle_selection(self, index):
        logging.info(f"Toggling selection for index: {index}")
        file = self.rows[index].file
        if file in self.selected_files:
            self.selected_files.remove(file)
        else:
            self.selected_files.append(file)

        self.rows[index].update_state(file in self.selected_files)

    def main(self):
        logging.info("Starting the FileSelector UI main loop")
        def unhandled_input(key):
            logging.info(f"Unhandled input: {key}")
            if key in ("q", "Q"):
                logging.info("Quitting the application")
                raise urwid.ExitMainLoop()
            if key == " ":
                focus_widget, focus_index = self.listbox.get_focus()
                if focus_index is not None:
                    self.toggle_selection(focus_index)
                self.update_footer()
            elif key == "enter":
                logging.info("Submitting selected files")
                raise urwid.ExitMainLoop()

        urwid.MainLoop(self.view, self.palette, unhandled_input=unhandled_input).run()

    def update_footer(self):
        selected_names = ", ".join([file["name"] for file in self.selected_files])
        logging.info(f"Updating footer with selected files: {selected_names}")
        self.view.footer = urwid.Text(f"Selected: {selected_names}")

# Main function
def main():
    try:
        logging.info("Application started")
        current_directory = os.getcwd()
        logging.info(f"Current working directory: {current_directory}")
        folder_structure = get_folder_structure(current_directory)
        if not folder_structure:
            logging.error("Error: Could not retrieve folder structure.")
            return

        selector = FileSelector(folder_structure)
        selector.main()

        if selector.selected_files:
            embed_selected_contents(folder_structure, selector.selected_files)
            with open("output.json", "w", encoding="utf-8") as f:
                json.dump(folder_structure, f, indent=4)
            logging.info("Output successfully written to 'output.json'")
            print("Output written to 'output.json'.")
        else:
            logging.info("No files selected.")
            print("No files selected.")
    except Exception as e:
        logging.error(f"Unhandled exception: {e}", exc_info=True)
        print("An error occurred. Check 'file_selector.log' for details.")

if __name__ == "__main__":
    main()
