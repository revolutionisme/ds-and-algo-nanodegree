import os

def recursive_list(suffix, path, list_of_path):
    #print(path, list_of_path)
    try:
        file_list = os.listdir(path)
    except FileNotFoundError:
        print("ERROR: The provided path/directory doesn't exists")
        return None

    if not file_list:
        return []
    
    #print(f"file_list - {path} -> {file_list} ")

    for file in file_list:
        relative_path = f"{path}/{file}"
        if os.path.isfile(relative_path) and relative_path.endswith(suffix):
            list_of_path.append(relative_path)
        elif os.path.isdir(relative_path):
            #print(file)
            recursive_list(suffix, relative_path, list_of_path)
    
    return list_of_path


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return recursive_list(suffix, path, [])


print("==========Test case 1==========")
print(find_files('.c', './testdir')) # Should print all c files in 'testdir' directory and sub directories

print("==========Test case 2==========")
print(find_files('', './testdir'))   # Should print all files in the 'testdir' directory and subdirectories

print("==========Test case 3==========")
print(find_files('.c', './unavailbaledir')) # Should show an error message and return None

print("==========Test case 4==========")
print(find_files('.c', './empty'))      # SHould return empty list []