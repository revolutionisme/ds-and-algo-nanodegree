import os

def recursive_list(suffix, path, list_of_path):
    #print(path, list_of_path)
    file_list = os.listdir(path)

    if not file_list:
        return None
    
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


print(find_files(".c", "."))