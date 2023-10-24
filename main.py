import os
import shutil
import time
from coverts import convert_json_to_csv
from running import check_program_status

while True:
    # Define the root directory where you want to start searching
    root_directory = r'property_json1'

    # Define the output folder where 'input.json' files will be copied
    output_directory = r'IO1'

    # Define the file names to search for
    input_file = 'input.json'
    result_file = 'result.json'

    # Initialize a counter for directories with the file
    count = 0

    # Walk through the directory tree to count directories with 'input.json'
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if input_file in filenames:
            count += 1
            
    print("********************************")
    print("              AiCan             ")
    print("********************************")
            
    program_name_to_check = "Spotify.exe"
    check_program_status(program_name_to_check)
    
    print(f"Total 'input.json' files to transfer: {count}")

    # Prompt the user to start or not
    print("--------------------------------")
    print("[1] Program elkezdese")
    print("[2] CSV konvertel")
    print("[3] AiCAN elinditása")
    print("[4] Program ujrainditasa")
    print("[0] Program leallitasa")
    print("--------------------------------")
    
    user_input = input("Press 1 if you want to start, Press 0 if you do not want to start: ")
    transferred_count = 0
    
    if user_input == '1':
        # Initialize a counter for successfully transferred files
        
        if count == 0:
            print("Nincsen falj megaddva")
            time.sleep(1)
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
                    print(f"{transferred_count}/{count} 'input.json' transferred")

                    while True:
                        # Check if 'result.json' exists in the output folder
                        result_file_path = os.path.join(output_directory, result_file)
                        if os.path.exists(result_file_path):
                            # Move 'result.json' back to the input folder
                            shutil.move(result_file_path, os.path.join(dirpath, result_file))
                            print(f"{transferred_count}/{count} 'input.json' files have corresponding 'result.json' files.")
                            break
                        else:
                            print("Waiting for 'result.json'...")
                            time.sleep(1)  # Wait for 1 second before checking again

            print("'input.json' files trasfer end")
            print("###############################")
            input_directory = r"property_json1" #coverts.py call
            print("Files coverting...")
            convert_json_to_csv(input_directory)
            print(f"{transferred_count}/{count} 'input.json' files have a 'result.json'")
            print("###############################")
            input(" ")
            break
    
    elif user_input == '0':
        print("Process not started.")
        time.sleep(1)
        break
        
    elif user_input == '2':
        if count == 0:
            print("Nincsen falj megaddva")
            time.sleep(1)
            os.system('cls')
        else:
            input_directory = r"property_json1"
            convert_json_to_csv(input_directory)
            input(" ")
            break

    elif user_input == '3':
        file_path = 'C:/Users/David/AppData/Roaming/Spotify/Spotify.exe'
        if os.path.exists(file_path):
            os.startfile(file_path)
            print("Alkalmazas megnyitása...")
            time.sleep(3)
            os.system('cls')
        else:
            print(f"{file_path} File does not exists")
            time.sleep(3)
            os.system('cls')
            
    elif user_input == '4':
        print("Restarting the process.")
        os.system('cls')
    
    else:
        print("Invalid input. Process not started.")
