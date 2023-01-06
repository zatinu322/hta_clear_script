import os
import shutil
import subprocess

VERSION = 'Community Patch v1.13'
COMPATCH_REPOSITORY = 'K:\\EM-CommunityPatch'
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

    mainfiles = [
        'dbghelp.dll', 
        'dxrender9.dll', 
        'fmod.dll', 
        'hta.exe', 
        'input_di8.dll', 
        'memlog.txt', 
        'mfc71.dll', 
        'mfc71u.dll', 
        'msvcp71.dll', 
        'msvcr71.dll', 
        'sound.dll'
    ]

    compatch_files = [
        'commod.exe', 
        'remaster', 
        'patch', 
        'libs'
    ]

    compatch_trash = [
        'library.dll', 
        'library.pdb'
    ]

    datafiles = [
        'beachsets.xml', 
        'config.cfg', 
        'config.cfg_', 
        'datasources.txt', 
        'devicecompatible.xml', 
        'grid.dds', 
        'gsmed.cfg', 
        'm3deditor.cfg', 
        'mod_manifest.yaml',
        'mips.dds', 
        'posteffects.xml', 
        'prefabgrid.dds', 
        'truxxconstructor.cfg', 
        'weather.xml', 
        'cursors', 
        'editor', 
        'effects', 
        'env', 
        'fx', 
        'gamedata', 
        'if', 
        'maps', 
        'models', 
        'music', 
        'scripts', 
        'shaders', 
        'sounds', 
        'textures', 
        'tiles', 
        'video', 
        'weathertexs'
    ]

    datapath = os.path.join(MAINPATH, 'data')
    backuppath = os.path.join(MAINPATH, 'backup')

    print(f'\nGame folder: {MAINPATH}')
    print(f'Backup folder: {backuppath}')
    print(f'Compatch repository folder: {COMPATCH_REPOSITORY}')

    if os.path.exists(backuppath):
        if os.path.exists(datapath):

            print('\nRemoving files in root...\n')
            remove(mainfiles, MAINPATH)

            print('\nRemoving ComPatch main files...\n')
            remove(compatch_files, MAINPATH)

            print('\nRemoving ComPatch trash...\n')
            remove(compatch_trash, MAINPATH)
            
            print('\nRemoving files in data...\n')
            remove(datafiles, datapath)

            print('\nCopying main files from backup...\n')
            copy(mainfiles, backuppath)

            print('\nCopying data from backup...\n')
            copy(['data'], backuppath)

            print('\nCopying ComPatch files...\n')
            copy(compatch_files, COMPATCH_REPOSITORY)

            run_commod = input('\nWould you like to run \'commod.exe\'? [Y/N]\n')
            if run_commod.lower() == 'y':
                subprocess.run('commod.exe')

        else:
            print('Error! Data folder not found.')
    else:
        print('Error! Backup folder not found.')

if __name__ == '__main__':
    main()