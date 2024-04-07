import logging
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class DataProcessor:
    content: Dict[str, int] = field(default_factory=dict)

    def process_file(self, file_path: str) -> None:
        if not file_path:
            err_msg = "No file path provided"
            logging.critical(err_msg, exc_info=True)
            exit(1)

        self.content.clear()

        try:
            with open(file_path, "r", newline="") as f:
                for line in f:
                    key, value = line.strip().split(" ")
                    self.content[key] = int(value)

        except:
            logging.critical(f"Error processing file {file_path}", exc_info=True)
            exit(1)
