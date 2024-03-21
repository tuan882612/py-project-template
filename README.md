# How to run starter project

## Project structure

```bash
.
├── Makefile
├── README.md
├── data
│   └── sample.txt
└── src
    ├── data_processor.py
    └── main.py
```

## Requirements

- [Python latest](https://www.python.org/downloads/)

## How to run

1. to esnure a proper running environment, use the python virtual environment and install the requirements

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. running the program

    ```bash
    make run
    # or
    python src/main.py
    ```
