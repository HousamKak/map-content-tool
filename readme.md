# **Documentation for mapContentTool.py**

## **Overview**
`mapContentTool.py` is a command-line tool for mapping the structure of a directory, selecting files and folders interactively, and exporting the directory structure with selected file contents. The output can be saved as a `.txt` (default) or `.json` file.

---

## **Features**
- Interactive selection of files and folders.
- Recursive handling of folder contents:
  - Selecting a folder includes all its files and subfolders.
  - Deselecting a folder removes all its files and subfolders from the selection.
- Embeds the content of selected files directly into the output structure.
- Outputs the directory structure in:
  - **Default**: `.txt` format.
  - **Optional**: `.json` format with a detailed structure.
- Exclude specific directories from scanning (e.g., `node_modules`, `.git`).
- Simple and intuitive user interface for navigation and selection.
- Comprehensive logging for debugging and tracking.

---

## **Usage**
### **Command-Line Arguments**
```bash
python mapContentTool.py [options]
```

### **Options**
| Option              | Description                                                                                     | Default                |
|---------------------|-------------------------------------------------------------------------------------------------|------------------------|
| `[directory]`       | Root directory to scan. If not provided, the current directory is used.                        | Current directory      |
| `-o, --output`      | Specify the output file. Supports `.txt` (default) and `.json`.                                | `output.txt`           |
| `-e, --exclude`     | Space-separated list of directories to exclude from scanning.                                  | `node_modules`, `.git` |

---

### **Examples**

#### **Basic Usage**
```bash
python mapContentTool.py
```
- Scans the current directory.
- Outputs the structure to `output.txt`.

#### **Specify an Output File**
```bash
python mapContentTool.py -o my_directory.json
```
- Outputs the directory structure to `my_directory.json`.

#### **Exclude Specific Directories**
```bash
python mapContentTool.py -e dist build
```
- Excludes the `dist` and `build` directories from the scan.

#### **Custom Directory**
```bash
python mapContentTool.py /path/to/directory
```
- Scans the `/path/to/directory` and outputs the structure to `output.txt`.

---

## **Output Format**
### **Default `.txt` Format**
- The `.txt` format retains the JSON-like structure for readability.

### **Optional `.json` Format**
- Example:
```json
{
  "name": "root_folder",
  "path": "/path/to/root_folder",
  "type": "directory",
  "items": [
    {
      "name": "subfolder1",
      "path": "/path/to/root_folder/subfolder1",
      "type": "directory",
      "items": [
        {
          "name": "file1.txt",
          "path": "/path/to/root_folder/subfolder1/file1.txt",
          "type": "file",
          "contents": "This is the content of file1.txt."
        }
      ]
    }
  ]
}
```

---

## **Interactive UI**
When run without the `-o` flag, the tool opens an interactive UI.

### **Navigation**
- **Arrow keys**: Move through the directory tree.
- **Space**: Select or deselect files and folders.
- **Enter**: Confirm selection and generate output.
- **Q**: Quit without saving.

---

## **Logs**
- Logs are written to `file_selector.log`.
- Tracks:
  - Errors
  - Directory scanning progress
  - File content embedding
  - User interactions

---

## **Error Handling**
- Handles missing directories and permission errors gracefully.
- If any uncaught exception occurs, it logs the error and exits with a message to check the logs.

---

## **Dependencies**
- Python 3.x
- Modules:
  - `os`
  - `json`
  - `urwid`
  - `logging`
  - `sys`
  - `argparse`

---

## **Changelog**
### **Latest Updates**
- Made `.txt` the default output format.
- Added `.json` as an optional output format.
- Restored the functionality of showing selected files inside a folder.
- Improved folder selection and deselection logic to include all nested items.
- Updated documentation to reflect the latest features and improvements.

---

## **Known Issues**
- None at the moment.

For feature requests or bug reports, please contact the developer or create an issue in the repository (if applicable).