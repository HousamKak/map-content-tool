### Documentation for File Selector Script

---

#### **Overview**
The **File Selector Script** is a Python application that allows users to interactively browse, select, and retrieve file content from a directory tree. The application uses the `urwid` library to provide a terminal-based user interface and outputs the selected files' content embedded within the folder structure in a JSON file.

---

#### **Key Features**
1. **Recursive Folder Structure Analysis**:
   - The script scans a directory tree, excluding specific directories (e.g., `node_modules`, `.git`), and constructs a structured representation of files and folders.

2. **Interactive Selection**:
   - Users can navigate the directory tree using arrow keys, toggle file selection using the spacebar, and finalize their selection by pressing Enter.

3. **Content Embedding**:
   - The script embeds the content of selected files directly into the JSON representation of the folder structure.

4. **Logging**:
   - Comprehensive logging is provided to track actions, errors, and the overall flow of the application. Logs are stored in `file_selector.log`.

5. **Error Handling**:
   - Handles uncaught exceptions and logs errors gracefully.

6. **Output**:
   - The output is written to `output.json`, containing the folder structure with the content of selected files.

---

#### **Components**

##### 1. **Folder Structure Retrieval**
The function `get_folder_structure` scans a directory recursively and builds a tree-like structure.

- **Parameters**:
  - `path`: The root directory path to scan.
  - `exclude_dirs`: A list of directories to exclude (default: `node_modules`, `.git`).

- **Output**:
  - A dictionary representation of the folder and its contents.

##### 2. **File Content Embedding**
The function `embed_selected_contents` traverses the folder structure and embeds the content of selected files into their respective nodes.

- **Parameters**:
  - `folder_structure`: The folder tree representation.
  - `selected_files`: A list of selected file nodes.

##### 3. **Interactive File Selector**
The `FileSelector` class provides an interactive terminal UI using the `urwid` library.

- **Features**:
  - Toggle file selection with the spacebar.
  - Navigate the tree with arrow keys.
  - Submit selected files with Enter.

##### 4. **Output File Writing**
The selected files and their contents are saved in a JSON format to `output.json`.

---

#### **How to Use**

##### 1. **Run the Script**
Execute the script in the terminal from the root directory you wish to scan:
```bash
python file_selector.py
```

##### 2. **Navigate the Directory Tree**
- Use the **arrow keys** to navigate through the files and folders.
- Use the **spacebar** to toggle file selection.
- Press **Enter** to submit your selection.

##### 3. **Output**
The folder structure and content of selected files will be written to `output.json` in the current working directory.

---

#### **Configuration**

1. **Excluded Directories**:
   - Modify the `exclude_dirs` parameter in `get_folder_structure` to customize directories to be skipped.

2. **Log File**:
   - All logs are written to `file_selector.log`. Update the logging configuration to change the file name or format.

---

#### **Sample JSON Output**
```json
{
    "name": "MyProject",
    "path": "/path/to/MyProject",
    "type": "directory",
    "items": [
        {
            "name": "file1.txt",
            "path": "/path/to/MyProject/file1.txt",
            "type": "file",
            "contents": "This is the content of file1.txt."
        },
        {
            "name": "subdir",
            "path": "/path/to/MyProject/subdir",
            "type": "directory",
            "items": [
                {
                    "name": "file2.txt",
                    "path": "/path/to/MyProject/subdir/file2.txt",
                    "type": "file",
                    "contents": "This is the content of file2.txt."
                }
            ]
        }
    ]
}
```

---

#### **Error Handling**
1. **Log File**:
   - All errors and exceptions are logged to `file_selector.log`.

2. **Missing File Content**:
   - If a file cannot be read, an error message is stored in the `contents` field of the corresponding node.

---

#### **Dependencies**

1. **Python Libraries**:
   - `os`: For directory and file management.
   - `json`: To generate the JSON output.
   - `urwid`: For the terminal-based UI.
   - `logging`: For detailed logging.
   - `sys`: For exception handling.

2. **Installation**:
   Install the `urwid` library if not already installed:
   ```bash
   pip install urwid
   ```

---

#### **Customization Options**
1. Modify the output file name:
   - Change `"output.json"` in the `main` function to a preferred file name.

2. Update excluded directories:
   - Add/remove directories in the `exclude_dirs` list in `get_folder_structure`.

---

#### **Example Execution**
1. Navigate to the directory containing the script:
   ```bash
   cd /path/to/script
   ```
2. Run the script:
   ```bash
   python file_selector.py
   ```
3. Select files interactively and press Enter.

4. View the results in `output.json`:
   ```bash
   cat output.json
   ```

---

#### **Future Enhancements**
- Add support for filtering files by extensions.
- Enable saving selections for reuse.
- Add options for output format customization.

---

Let me know if further adjustments or additional sections are required.