import os
print("Virus Downloader")
choose = input("1- Trojan \n2- Ransomware \n3- Others \n")
if choose == 1:
    choose2 = input("1- Artemis \n2- Android Skygofree \n3- ElectroRAT")
    if choose2 == 1:
        os.system('cp virus/Trojan/Artemis.zip downloaded_virus')
        print("Downloading in downloaded_virus folder :)")
    elif choose2 == 2:
        os.system('cp virus/Trojan/Android.Skygofree.zip downloaded_virus')
        print("Downloading in downloaded_virus folder :)")
    elif choose2 == 3:
        os.system('cp virus/Trojan/All.ElectroRAT.zip downloaded_virus')
        print("Downloading in downloaded_virus folder :)")
    else:
        print("No valid option")
elif choose == 2:
    choose3 = input("1- Keypass \n2- Thanos \n3- RedBoot")
    if choose3 == 1:
        os.system('cp virus/Ransomware/Win32.KeyPass.zip downloaded_virus')
        print("Downloading in downloaded_virus folder :)")
    elif choose3 == 2:
         os.system('cp virus/Ransomware/Ransomware.Thanos.zip downloaded_virus')
         print("Downloading in downloaded_virus folder :)")
    elif choose3 == 3:
         os.system('cp virus/Ransomware/Ransomware.RedBoot.zip downloaded_virus')
         print("Downloading in downloaded_virus folder :)")
    else:
        print("No valid option")
elif choose == 3:
    choose4 = input("1- Rootkit \n2- Neurevt \n3- Mini Pig")
    if choose4 == 1:
        os.system('cp virus/Others/Rubilyn.zip downloaded_virus')
        print("Downloading in downloaded_virus folder :)")
    elif choose4 == 2:
        os.system('cp virus/Others/Neurevt.1.7.0.1.zip downloaded_virus')
        print("Downloading in downloaded_virus folder :)")
    elif choose4 == 3:
        os.system('cp virus/Others/Win32.MiniPig_Nov2006.zip downloaded_virus')
        print("Downloading in downloaded_virus folder :)")
else:
    print("Invalid Option")

