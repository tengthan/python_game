from config_reader import ConfigReader
# Don't remove any comments in this file
folder_path = "./invalid_files/"

# Please create appropriate invalid files in the folder "invalid_files"
# for each unit test according to the comments below and
# then complete them according to the function name

def test_file_not_found():
  invalid_path = "./invalid_files/not_found.txt"
  try:
    config_reader = ConfigReader(invalid_path)
    return print("test_file_not_found failed!")
  except FileNotFoundError:
    return True

def test_format_error():
  path = "./invalid_files/format_error_file.txt"
  try: 
    config_reader = ConfigReader(path)
    return print("test_format_error failed!")
  except SyntaxError:
    return True

def test_frame_format_error():
  path = "./invalid_files/frame_format_error_file.txt"
  try: 
    config_reader = ConfigReader(path)
    return print("test_frame_format_error failed!")
  except SyntaxError:
    return True

def test_frame_out_of_range():
  path = "./invalid_files/format_out_of_range_file.txt"
  try: 
    config_reader = ConfigReader(path)
    return print("test_frame_out_of_range failed!")
  except SyntaxError:
    return True

def test_non_integer():
  path = "./invalid_files/non_integer_file.txt"
  try: 
    config_reader = ConfigReader(path)
    return print("test_non_integer failed!")
  except ValueError:
    return True

def test_out_of_map():
  # add "out_of_map_file.txt" in "invalid_files"
  path = "./invalid_files/out_of_map_file.txt"
  try: 
    config_reader = ConfigReader(path)
    return print("test_out_of_map failed!")
  except SyntaxError:
    return True

def test_occupy_home_or_next_to_home():
  # add two invalid files: "occupy_home_file.txt" and
  # "occupy_next_to_home_file.txt" in "invalid_files"
  path = "./invalid_files/occupy_home_file.txt"
  try: 
    config_reader = ConfigReader(path)
    return print("test_occupy_home_or_next_to_home failed!")
  except ValueError:
    return True
  path = "./invalid_files/occupy_next_to_home_file.txt"
  try: 
    config_reader = ConfigReader(path)
    return print("test_occupy_home_or_next_to_home failed!")
  except ValueError:
    return True

def test_duplicate_position():
  # add two files: "dupli_pos_in_single_line.txt" and
  # "dupli_pos_in_multiple_lines.txt" in "invalid_files"
  path = "./invalid_files/dupli_pos_in_multiple_lines.txt"
  try: 
    config_reader = ConfigReader(path)
    return print("test_duplicate_position failed!")
  except SyntaxError:
    return True

def test_odd_length():
  # add "odd_length_file.txt" in "invalid_files"
  path = "./invalid_files/odd_length_file.txt"
  try: 
    config_reader = ConfigReader(path)
    return print("test_odd_length failed!")
  except SyntaxError:
    return True

def test_valid_file():
  # no need to create file for this one, just test loading config.txt
  path = "./config.txt"
  try: 
    config_reader = ConfigReader(path)
    return True
  except:
    return print("test_valid_file failed!")

# you can run this test file to check tests and load_config_file
if __name__ == "__main__":
  test_file_not_found()
  test_format_error()
  test_frame_format_error()
  test_frame_out_of_range()
  test_non_integer()
  test_out_of_map()
  test_occupy_home_or_next_to_home()
  test_duplicate_position()
  test_odd_length()
  test_valid_file()