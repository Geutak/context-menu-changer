import os

directory = os.getcwd()
directory = directory.replace("\\","\\\\")
print(directory)
reg_contenu = 'Windows Registry Editor Version 5.00\n[HKEY_CLASSES_ROOT\\*\\shell\\lire ce fichier\\Command]\n@="{0}\\\\bat_file.bat lu %1"\nWindows Registry Editor Version 5.00\n[HKEY_CLASSES_ROOT\\*\\shell\\verifier ce fichier\\Command]\n@="{0}\\\\bat_file.bat vérifié %1"\nWindows Registry Editor Version 5.00\n[HKEY_CLASSES_ROOT\\*\\shell\\signer ce document\\Command]\n@="{0}\\\\bat_file.bat signé %1"\n'.format(directory)

reg_file = open("reg.reg","w")

directory = directory.replace("\\\\","\\")
reg_file.write(reg_contenu)
reg_file.close()
bat_file = open("bat_file.bat","w")

bat_contenu="@echo off\npython {}\\main.py %1 %2".format(directory)

bat_file.write(bat_contenu)
bat_file.close()
os.system("reg.reg")
