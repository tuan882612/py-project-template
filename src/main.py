import logging

from data_processor import DataProcessor


def main() -> None:
    proccessor = DataProcessor()
    proccessor.process_file("data/sample.txt")
    logging.debug(f"proccessed content: {proccessor.content}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()