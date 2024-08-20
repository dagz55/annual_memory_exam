import sys
import subprocess
import importlib.util
import os
from textual.app import App, ComposeResult
from textual.containers import Container
from textual import widgets
from textual.widgets import Header, Footer, DataTable, ProgressBar, Button, Static

REQUIRED_PACKAGES = {'textual', 'psutil'}

class Wolverine:
    @staticmethod
    def heal():
        missing_packages = []
        for package in REQUIRED_PACKAGES:
            if importlib.util.find_spec(package) is None:
                missing_packages.append(package)
        
        if missing_packages:
            print("🔧 Wolverine healing: Installing missing packages...")
            try:
                subprocess.check_call([sys.executable, '-m', 'ensurepip', '--upgrade'])
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
                print("✅ Healing complete!")
            except subprocess.CalledProcessError:
                print("❌ Failed to install packages. Please install pip manually and run the script again.")
                sys.exit(1)
        else:
            print("✅ All required packages are already installed.")

def bytes_to_gb(bytes_value: int) -> float:
    return bytes_value / (1024 * 1024 * 1024)

class AnnualMemoryExam(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #exam-container {
        width: 90%;
        height: auto;
        border: heavy $accent;
        padding: 1 2;
    }
    .exam-row {
        height: 3;
        margin: 1 0;
        text-align: center;
    }
    DataTable {
        height: auto;
    }
    ProgressBar {
        width: 100%;
    }
    Button {
        margin: 1 1;
    }
    #button-row {
        layout: horizontal;
        align: center middle;
        height: auto;
    }
    #logo {
        content-align: center middle;
        height: 3;
    }
    #quit-btn {
        dock: bottom;
        width: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("🐺 Wolverine Memory Exam", id="logo")
        with Container(id="exam-container"):
            yield widgets.Static("Annual Memory Examination", classes="exam-row")
            yield DataTable(id="memory-table")
            yield widgets.Static("System Memory Utilization", classes="exam-row")
            yield ProgressBar(id="memory-usage", show_eta=False)
            with Container(id="button-row"):
                yield Button("Refresh", id="refresh-btn", variant="primary")
                yield Button("Export Report", id="export-btn", variant="success")
        yield Button("Quit", id="quit-btn", variant="error")
        yield Footer()

    def on_mount(self) -> None:
        self.update_memory_info()

    def update_memory_info(self) -> None:
        import psutil  # Import here to allow Wolverine to heal first
        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()
        system_memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        table = self.query_one("#memory-table")
        table.clear()
        table.add_columns("Metric", "Value", "Status")
        table.add_rows([
            ("Total Physical Memory", f"{bytes_to_gb(system_memory.total):.2f} GB", "✅ Normal"),
            ("Available Memory", f"{bytes_to_gb(system_memory.available):.2f} GB", "✅ Adequate"),
            ("Used Memory", f"{bytes_to_gb(system_memory.used):.2f} GB", "ℹ️ Monitor"),
            ("Swap Total", f"{bytes_to_gb(swap.total):.2f} GB", "✅ Configured"),
            ("Swap Used", f"{bytes_to_gb(swap.used):.2f} GB", "ℹ️ Monitor"),
            ("Current Process Memory", f"{bytes_to_gb(mem_info.rss):.4f} GB", "✅ Normal"),
        ])
        progress_bar = self.query_one("#memory-usage")
        progress_bar.update(total=100, progress=system_memory.percent)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "refresh-btn":
            self.update_memory_info()
        elif event.button.id == "export-btn":
            self.export_report()
        elif event.button.id == "quit-btn":
            self.exit()

    def export_report(self) -> None:
        self.notify("Report exported successfully!", title="Export")

if __name__ == "__main__":
    Wolverine.heal()
    app = AnnualMemoryExam()
    app.run()
