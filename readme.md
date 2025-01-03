# **Documentation for mapContentTool**

## **Overview**

`mapContentTool` is a command-line tool for mapping the structure of a directory, selecting files and folders interactively, and exporting the directory structure with selected file contents. The output can be saved as a `.txt` (default) or `.json` file. Additionally, the tool can be installed as a Python library to provide the `map-content` command for direct usage.

---

## **Features**

- **Interactive Selection**:
  - Navigate directory structures.
  - Select or deselect files and folders interactively.
- **Recursive Handling**:
  - Selecting a folder includes all its files and subfolders.
  - Deselecting a folder removes all its files and subfolders from the selection.
- **File Content Embedding**:
  - Embeds the content of selected files directly into the output structure.
- **Output Options**:
  - **Default**: `.txt` format.
  - **Optional**: `.json` format with a detailed structure.
  - **Clipboard**: Automatically copies output to clipboard when submitting.
- **Exclusion Capabilities**:
  - Exclude specific directories (e.g., `node_modules`, `.git`).
- **Convenient Command**:
  - Install as a Python library to use the `map-content` command directly.
- **Comprehensive Logging**:
  - Logs all actions and errors for debugging and tracking.
  - Outputs the full path of the generated file in the logs.
- **Full Directory Mapping**:
  - Outputs the directory structure even if no files are selected.

---

## **Installation**

Install `mapContentTool` as a Python package via pip:

```bash
pip install map-content-tool
```

---

## **Usage**

### **Command-Line Options**

```bash
python mapContentTool.py [directory] [options]
```

Or, after installation, use the standalone command:

```bash
map-content [directory] [options]
```

### **Options**

| Option          | Description                                                             | Default                |
| --------------- | ----------------------------------------------------------------------- | ---------------------- |
| `[directory]`   | Root directory to scan. If not provided, the current directory is used. | Current directory      |
| `-o, --output`  | Specify the output file. Supports `.txt` (default) and `.json`.         | `output.txt`           |
| `-e, --exclude` | Space-separated list of directories to exclude from scanning.           | `node_modules`, `.git` |

---

### **Examples**

#### **Using Python Script**

1. **Basic Usage**:

   ```bash
   python mapContentTool.py
   ```

   - Scans the current directory.
   - Outputs the structure to `output.txt`.

2. **Specify an Output File**:

   ```bash
   python mapContentTool.py -o my_directory.json
   ```

   - Outputs the directory structure to `my_directory.json`.

3. **Exclude Specific Directories**:

   ```bash
   python mapContentTool.py -e dist build
   ```

   - Excludes the `dist` and `build` directories from the scan.

4. **Scan a Custom Directory**:

   ```bash
   python mapContentTool.py /path/to/directory
   ```

   - Scans the `/path/to/directory` and outputs the structure to `output.txt`.

---

#### **Using the `map-content` Command**

1. **Basic Usage**:

   ```bash
   map-content
   ```

   - Scans the current directory.
   - Outputs the structure to `output.txt`.

2. **Custom Directory**:

   ```bash
   map-content /path/to/directory
   ```

3. **Exclude Specific Directories**:

   ```bash
   map-content -e dist build
   ```

4. **Output as JSON**:

   ```bash
   map-content -o output.json
   ```

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
  - Full path of the generated file

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
  - `setuptools`
  - `pyperclip`

---

## **Changelog**

### **Latest Updates**

#### 1.3.1

- Added: Automatic clipboard copying of the output when pressing Enter
- The tool now copies the complete structure (including file contents) to clipboard in addition to saving to file

#### 1.2.1

- Fixed: Directory structure is now saved even when no files are selected (previously required file selection)

#### Previous Versions

- Made `.txt` the default output format.
- Added `.json` as an optional output format.
- Restored the functionality of showing selected files inside a folder.
- Improved folder selection and deselection logic to include all nested items.
- Updated logging and documentation.
- Enabled the use of the `map-content` standalone command via setuptools.
- Outputs the full path of the generated file in the logs.

---

## **Known Issues**

- None at the moment.

For feature requests or bug reports, please contact the developer or create an issue in the repository.

