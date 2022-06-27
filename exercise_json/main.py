import sys
import json

from exercise_json import flattener

"""
Linux convention usage (reading a json object from stdin):
```
cat exercise_json/example_test_input.json | python3 -m exercise_json.main
```

Assumptions:
- Input will be a valid JSON object.
- All keys will not contain "." character in input.
- Using the `json` library to encode/decode JSON string.

Note:
- The output key order is sorted by the resulting composite key (e.g. "c.e" will appear after "c.d)".
- Floating points only support up to double precision (IEEE-754, fixed 8-bytes).
  - If more precision is needed, can implement a variable size floating point and override the JSON encoder/decoder on
  decoding/encoding large floating point.
"""

if __name__ == "__main__":
  # Accept input from stdin.
  input = ""
  for line in sys.stdin:
    input += line
  print(json.dumps(flattener.flatten(json.loads(input)), indent=4, sort_keys=True))
