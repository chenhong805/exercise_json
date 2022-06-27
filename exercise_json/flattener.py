from typing import List, Optional

none_type = type(None)


def flatten(obj: dict) -> dict:
  return flatten_recursive(obj)


def flatten_recursive(current_obj: dict, path: Optional[List[str]]=None) -> dict:
  """
  Takes a parsed JSON object (of type dict) as input and outputs a flattened version of the JSON object (of type dict),
  with keys as the path to every terminal value in the JSON structure.

  - Input JSON object will not contain arrays.
  - All keys in the input JSON object will be simple strings without "." character.
  - This function assumes the input is already parsed with `json` library.
  - This function returns a `dict` representation of the constructed JSON object.

  :param current_obj: A JSON object.
  :param path: the optional path to the current JSON object. Should be empty at the first call.
  :return: A flattened JSON object.
  """

  if path is None:
    path = []

  if isinstance(current_obj, (int, str, bool, float, none_type)):
    return {".".join(path): current_obj}

  flattened = {}
  for key in current_obj:
    flattened_child_object = flatten_recursive(current_obj[key], path + [key])
    flattened.update(flattened_child_object)
  return flattened
