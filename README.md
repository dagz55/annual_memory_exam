# annual_memory_exam
The annual memory exam script is the first to display the 'Wolverine' code. Please take a look at the wiki for more details.


# Annual Memory Examination

This script provides a Textual UI for examining system memory usage.

## Features

- Displays total physical memory, available memory, used memory, swap usage, and current process memory
- Shows system memory utilization with a progress bar
- Allows refreshing of memory information
- Provides an option to export the memory report (placeholder functionality)

## Installation

1. Ensure you have Python 3.6+ installed.
2. Clone this repository:
   ```
   git clone https://github.com/dagz55/anual_memory_exam.git
   cd anual_memory_exam
   ```
3. Run the script:
   ```
   python anual_memory_exam-BETA.py
   ```
   or
   ```
   python ame.py
   ```

The script will automatically install any required packages that are missing.

## Requirements

The script will automatically install the following packages if they're not present:

- textual
- psutil

## Usage

After running the script, you'll see a Textual UI with memory information. Use the mouse or keyboard to interact with the buttons:

- "Refresh": Updates the memory information
- "Export Report": Placeholder for exporting the memory report

Press Ctrl+C to exit the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
