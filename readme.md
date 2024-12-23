# Map Content Tool Documentation

## Overview

The **Map Content Tool** is a command-line utility that allows users to recursively scan a directory structure, interactively select files, and embed their content into a structured output file (JSON or TXT). The tool is versatile, supporting exclusion of specific directories and customizable output formats.

---

## Features

1. **Interactive Directory Scanning**:
   - Recursively scans the specified directory or the current working directory by default.
   - Excludes specified directories (e.g., `node_modules`, `.git`) during the scan.
   - Provides an interactive terminal-based UI to select files for embedding their contents.

2. **Output Formats**:
   - Outputs the directory structure and selected file contents in **JSON** or **TXT** formats.

3. **Command-Line Interface**:
   - Supports intuitive command-line commands with various options for customization.
   - Includes a `map-content` command to initiate the interactive mode.

4. **Exclusion of Directories**:
   - Specify directories to exclude during the scan.

5. **Error Logging**:
   - Logs all operations and errors to a `file_selector.log` file for easy troubleshooting.

---

## Usage

### Basic Command
```bash
python map_content_tool.py map-content
```
- This scans the current working directory and provides an interactive UI for file selection.

### Command-Line Options

| Option                   | Description                                                                                       | Default               |
|--------------------------|---------------------------------------------------------------------------------------------------|-----------------------|
| `-o`, `--output`         | Specify the output file name. Supports `.json` or `.txt` formats.                                 | `output.json`         |
| `-e`, `--exclude`        | Specify directories to exclude during the scan.                                                  | `["node_modules", ".git"]` |

### Examples

#### Map the Current Directory and Save Output as JSON
```bash
python map_content_tool.py map-content
```

#### Exclude Additional Directories
```bash
python map_content_tool.py map-content -e dist build
```

#### Save Output as TXT
```bash
python map_content_tool.py map-content -o output.txt
```

---

## Output Details

### JSON Format
The JSON output includes the directory structure, with embedded content for selected files:
```json
{
  "name": "my_project",
  "path": "/path/to/my_project",
  "type": "directory",
  "items": [
    {
      "name": "example.txt",
      "path": "/path/to/my_project/example.txt",
      "type": "file",
      "contents": "File content here..."
    }
  ]
}
```

### TXT Format
The TXT output is a human-readable representation of the directory structure:
```
my_project (directory)
  example.txt (file)
    Contents:
    File content here...
```

---

## Interactive UI

When the tool is run with `map-content`, an interactive UI is launched:
- **Navigation**:
  - Use **arrow keys** to navigate the directory tree.
- **Selection**:
  - Press **Space** to toggle file selection.
- **Submit**:
  - Press **Enter** to finalize the selection and generate the output.
- **Exit**:
  - Press **Q** to quit without saving.

---

## Logs

- All operations and errors are logged in `file_selector.log` for debugging.
- Example log entries:
  ```
  2024-12-23 10:00:00,123 - INFO - Scanning folder structure at path: /path/to/my_project
  2024-12-23 10:01:00,456 - INFO - Selected file: example.txt
  2024-12-23 10:02:00,789 - ERROR - Error reading file: example.txt
  ```

---

## Error Handling

- If an error occurs, it is logged to `file_selector.log` and displayed in the terminal.
- Common error scenarios include:
  - Invalid directory paths.
  - Permission issues when reading files or writing output.

---

## Requirements

- **Python 3.6+**
- Required Python libraries:
  - `os`
  - `json`
  - `urwid`
  - `argparse`
  - `logging`

---

## Installation

1. Clone or download the repository.
2. Install dependencies using `pip`:
   ```bash
   pip install urwid
   ```

---

## Notes

- The tool is optimized for use in Unix-like systems and Windows environments.
- The default exclusions (`node_modules`, `.git`) can be overridden with the `-e` option.