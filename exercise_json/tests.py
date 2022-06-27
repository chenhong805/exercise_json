import json
import unittest

from exercise_json.flattener import flatten

"""
To run this unit test with test discovery:
```
python3 -m unittest
```
"""

class MyTestCase(unittest.TestCase):
  def test_parse_all_type(self):
    input = json.loads(
      """
      {
        "a":1,
        "b": true,
        "c": {
          "d": 3,
          "e": "test",
          "nested_large": {
            "large_int": 14159265358979323846264338327950288419716939937510,
            "large_float": 3.141592653589793
          }
        },
        "f": null
      }
      """
    )
    output = flatten(input)
    print("------ Test case ----------")
    print("Input:")
    print(json.dumps(input, indent=4))
    print("Output:")
    print(json.dumps(output, indent=4))
    expect_output = {
      "a": 1,
      "b": True,
      "c.d": 3,
      "c.e": "test",
      "c.nested_large.large_int": 14159265358979323846264338327950288419716939937510,
      'c.nested_large.large_float': 3.141592653589793,
      "f": None
    }
    self.assertEqual(expect_output, output)
  def test_parse_all_types_unnested(self):
    input = json.loads(
      """
      {
        "a":1,
        "b": true,
        "d": 3,
        "e": "test",
        "large_int": 14159265358979323846264338327950288419716939937510,
        "large_float": 3.141592653589793,
        "f": null
      }
      """
    )
    output = flatten(input)
    print("------ Test case ----------")
    print("Input:")
    print(json.dumps(input, indent=4))
    print("Output:")
    print(json.dumps(output, indent=4))
    expect_output = {
      "a": 1,
      "b": True,
      "d": 3,
      "e": "test",
      "large_int": 14159265358979323846264338327950288419716939937510,
      'large_float': 3.141592653589793,
      "f": None
    }
    self.assertEqual(expect_output, output)
  def test_parse_empty(self):
    input = json.loads(
      """
      {}
      """
    )
    output = flatten(input)
    print("------ Test case ----------")
    print("Input:")
    print(json.dumps(input, indent=4))
    print("Output:")
    print(json.dumps(output, indent=4))
    expect_output = {
    }
    self.assertEqual(expect_output, output)


if __name__ == '__main__':
  unittest.main()
