import os, shutil

VERSION = 'Steam v1.02'
MAINPATH = os.getcwd()

def remove(files, path):
    for file in files:
        localpath = os.path.join(path, file)
        
        if os.path.isfile(localpath):
            os.remove(localpath)
            print(f'REMOVED: {localpath}')
        elif os.path.isdir(localpath):
            shutil.rmtree(localpath)
            print(f'REMOVED: {localpath}')
        elif os.path.exists(localpath):
            print(f'**********Unable to remove {localpath}**********')
        else:
            print(f'**********{localpath} not found**********')

def copy(files, path):
    for file in files:
        copy_from = os.path.join(path, file)
        copy_to = os.path.join(MAINPATH, file)

        if os.path.isfile(copy_from):
            shutil.copyfile(copy_from, copy_to)
            print(f'COPIED: {copy_from} to {copy_to}')
        elif os.path.isdir(copy_from):
            shutil.copytree(copy_from, copy_to, dirs_exist_ok=True)
            print(f'COPIED: {copy_from} to {copy_to}')
        elif os.path.exists(copy_from):
            print(f'**********Unable to copy {copy_from} to {copy_to}**********')
        else:
            print(f'**********{copy_from} not found**********')

def main():
    print(f'VERSION = {VERSION}')

    mainfiles = ['dbghelp.dll', 'dxrender9.dll', 'fmod.dll', 'hta.exe', 
                'input_di8.dll', 'memlog.txt', 'mfc71.dll', 'mfc71u.dll', 
                'msvcp71.dll', 'msvcr71.dll', 'sound.dll']

    datafiles = ['beachsets.xml', 'config.cfg', 'config.cfg_', 'datasources.txt', 
                 'devicecompatible.xml', 'grid.dds', 'gsmed.cfg', 'm3deditor.cfg', 
                 'mips.dds', 'posteffects.xml', 'prefabgrid.dds', 'truxxconstructor.cfg', 
                 'weather.xml', 'cursors', 'editor', 'effects', 'env', 'fx', 'gamedata', 
                 'if', 'maps', 'models', 'music', 'scripts', 'shaders', 'sounds', 
                 'textures', 'tiles', 'video', 'weathertexs']

    datapath = os.path.join(MAINPATH, 'data')
    backuppath = os.path.join(MAINPATH, 'backup')

    print(f'\nGame folder: {MAINPATH}')
    print(f'Backup folder: {backuppath}')

    if os.path.exists(backuppath):
        if os.path.exists(datapath):

            print('\nRemoving files in root...\n')
            remove(mainfiles, MAINPATH)
            
            print('\nRemoving files in data...\n')
            remove(datafiles, datapath)

            print('\nCopying main files from backup...\n')
            copy(mainfiles, backuppath)

            print('\nCopying data from backup...\n')
            copy(['data'], backuppath)

            complete = input('\nCOMPLETED')
        else:
            print('Error! Data folder not found.')
    else:
        print('Error! Backup folder not found.')

if __name__ == '__main__':
    main()