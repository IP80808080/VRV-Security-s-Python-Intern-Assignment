# VRV Security Python Intern Assignment - Skills Overview

This table outlines the essential skills you'll need for the assignment. Each skill is associated with an emoji to make it visually appealing and easier to remember!

| **Skill**                  | **Description**                                                                | **Emoji**     | **Command/Method**                        |
|----------------------------|--------------------------------------------------------------------------------|---------------|-------------------------------------------|
| **File Handling**           | Working with files to read, write, and process data efficiently.               | 📂            | `open()`, `readlines()`, `write()`        |
| **String Manipulation**     | Techniques for modifying and analyzing text data, such as parsing and cleaning. | 🔠            | `split()`, `strip()`, `replace()`         |
| **Data Analysis**           | Extracting insights and key information from large datasets.                   | 📊            | `pandas.read_csv()`, `json.load()`        |
| **Regular Expressions**     | Using regex to find patterns or validate data within strings.                  | 🔍            | `re.match()`, `re.search()`, `re.findall()` |
| **Error Handling**          | Writing code to handle unexpected events and prevent crashes.                  | ⚠️            | `try`, `except`, `finally`                |
| **Log Parsing**             | Reading and interpreting log files to extract relevant details.                | 📜            | `open()`, `readlines()`, `split()`        |
| **Data Visualization**      | Creating meaningful graphs or charts from the extracted data.                   | 📈            | `matplotlib.pyplot`, `pandas.DataFrame.plot()` |
| **Security Best Practices** | Applying cybersecurity principles to ensure the script runs securely.          | 🔒            | `os.path.exists()`, `shutil.safe_copy()`  |
| **CSV File Handling**       | Writing and reading data in CSV format.                                        | 📝            | `csv.reader()`, `csv.writer()`            |

---

## Key Concepts to Remember

- **File Handling**: Use `open()` to handle files. `readlines()` is useful for reading a file line by line.
- **String Manipulation**: Use Python's built-in string methods like `split()`, `strip()`, and `replace()` for effective text processing.
- **Data Analysis**: Utilize `pandas.read_csv()` to read data into DataFrames, or `json.load()` to parse JSON logs.
- **Regular Expressions**: Regular expressions in the `re` module help match patterns and search within strings.
- **Error Handling**: Always protect your code with `try-except` blocks to gracefully handle unexpected errors.
- **Log Parsing**: When working with log files, `open()` and `readlines()` help process and extract relevant data.
- **CSV File Handling**: Use `csv.reader()` to read and `csv.writer()` to write CSV files for structured data handling.
  
**Example of CSV Writing**:
```python
import csv
with open('sample.log', 'r') as file:
