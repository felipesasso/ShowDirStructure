import os
import pprint

def get_directory_structure_dict(path=None, structure_dict=None):
    ''' Returns dictionary-like structure containing all the directories and size
        of each file under each directory

        Args:
            path ('str'): Optional. Full path of a directory
            structure_dict ('dict'): Optional. Dictionary where the structure
                information will be saved
        Returns:
            dictionary: Directory structure
        Raises:
            None
    '''

    if structure_dict is None:
        structure_dict = {}

    if path is None:
        path = os.getcwd()

    listdir = os.listdir(path)

    for name in listdir:
        if (name.startswith('.') or
            name.startswith('_')):
            continue
        curpath =  path + '/' + name
        if os.path.isdir(curpath):
            get_directory_structure_dict(path=curpath,
                structure_dict=structure_dict.setdefault(name, {}))
        elif os.path.isfile(curpath):
            structure_dict[name] = os.path.getsize(curpath)

    return structure_dict

if __name__ == '__main__':
    # If not being imported as module, it will only pprint structure
    pprint.pprint(get_directory_structure_dict())
