# Directory structure
- `exercise_json` package:
  - `flatterner.py` : function having the flatten logic.
  - `main.py`       : the entry point to the command line, also having the JSON decoding/encoding logic using `json`.
  - `tests.py`      : having tests to test all JSON input primitive types.
# To run from linux command line
- Download the project. It contains a python package `exercise_json`.
```shell
cd ${PROJECT_DIR}
```
- To run with provided example `json` file:
```shell
cat exercise_json/example_test_input.json | python3 -m exercise_json.main
```

- To run written tests:
```shell
python3 -m unittest
```