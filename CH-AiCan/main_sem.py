import os
import shutil
import time
from coverts import convert_json_to_csv
from running import check_program_status

while True:
    # Define the root directory where you want to start searching
    root_directory = r'property_json'

    # Define the output folder where 'input.json' files will be copied
    output_directory = r'C:/Users/Katka/AiCAN/run/IO'

    # Define the file names to search for
    input_file = 'input.json'
    result_file = 'result.json'
    
    #Define the app file path to open
    app_path = 'C:/Users/Katka/AiCAN/run/IO/run.exe'

    # Initialize a counter for directories with the file
    count = 0
    
    # Walk through the directory tree to count directories with 'input.json'
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if input_file in filenames:
            count += 1
            
    print("********************************")
    print("              AiCan             ")
    print("********************************")
            
    program_name_to_check = "run.exe"
    check_program_status(program_name_to_check)
    
    print(f"Összes átvinni kívánt 'input.json' fájl: {count}")

    # Prompt the user to start or not
    print("--------------------------------")
    print("[1] Program elkezdése")
    print("[2] AiCAN elindítása")
    print("[3] Mappák Info")
    print("[4] Program újraindítása")
    print("[0] Program leállítása")
    print("--------------------------------")
    
    user_input = input("Nyomja meg a listában levő számot és az ENTER-t: ")
    transferred_count = 0
    
    if user_input == '1':
        # Initialize a counter for successfully transferred files
        
        if count == 0:
            print("Nincsen fálj megadva.")
            time.sleep(1)
            os.system('cls')
            
        elif not os.path.exists(output_directory):
            print(f"{output_directory} A mappa nem létezik")
            time.sleep(2)
            os.system('cls')

        # If there are directories with 'input.json', copy and wait for 'result.json'
        elif count > 0:
            for dirpath, dirnames, filenames in os.walk(root_directory):
                if input_file in filenames:
                    input_file_path = os.path.join(dirpath, input_file)
                    output_file_path = os.path.join(output_directory, input_file)

                    # Copy 'input.json' to the output folder
                    shutil.copy(input_file_path, output_file_path)
                    transferred_count += 1
                    print(f"{transferred_count}/{count} 'input.json' átvitele")

                    while True:
                        # Check if 'result.json' exists in the output folder
                        result_file_path = os.path.join(output_directory, result_file)
                        if os.path.exists(result_file_path):
                            # Move 'result.json' back to the input folder
                            shutil.move(result_file_path, os.path.join(dirpath, result_file))
                            print(f"{transferred_count}/{count} 'input.json' fájl sikeresen rendelkezik 'result.json' fájllal")
                            break
                        else:
                            print("Várakozás a 'result.json' fájlra...")
                            time.sleep(1)  # Wait for 1 second before checking again

            print("'input.json' fájl átvitel vége.")
            print("###############################")
            input_directory = r"property_json" #coverts.py call
            print("CSV konverter...")
            convert_json_to_csv(input_directory)
            if transferred_count == count:
                print(f"{transferred_count}/{count} 'input.json' fájl sikeresen rendelkezik 'result.json' fájllal")
            else:
                print(f"{transferred_count}/{count} 'input.json' fájl sikeresen rendelkezik 'result.json' fájllal")
            print("###############################")
            input(" ")
            break
    
    elif user_input == '0':
        print("Program bezárása.")
        time.sleep(1)
        break
    
    elif user_input == '3':
        print("   ")
        print("Elenőrizze a mapák helyesek!")
        print(f"Bemeneti mappa: '{root_directory}'")
        if os.path.exists(root_directory):
            print("Mappa megtalálva")
        else:
            print("Mappa nem tálalható")
        
        print(f"Kimeneti mappa: '{output_directory}'")
        if os.path.exists(output_directory):
            print("Mappa megtalálva")
        else:
            print("Mappa nem tálalható")
            
        print(f"AiCAN alkalmazás: '{app_path}'")
        if os.path.exists(app_path):
            print("Mappa megtalálva")
        else:
            print("Mappa nem tálalható")
            
        input(" ")
        os.system('cls')
        
    elif user_input == '2':
        if os.path.exists(app_path):
            os.startfile(app_path)
            print("Alkalmazás megnyitása...")
            time.sleep(3)
            os.system('cls')
        else:
            print(f"{app_path} Alkalmazás nem létezik")
            time.sleep(3)
            os.system('cls')
            
            
    elif user_input == '4':
        print("Program újraindítása")
        os.system('cls')
    
    else:
        print("Hibás bemenet. Program nem indult el.")
        time.sleep(1)
        os.system('cls')
