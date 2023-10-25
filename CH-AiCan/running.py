import subprocess
import time


def check_program_status(program_name):
    while True:
        # Run the 'tasklist' command to list running processes, and use 'findstr' to filter by program name
        command = f'tasklist /FI "IMAGENAME eq {program_name}"'
        output = subprocess.getoutput(command)

        if program_name in output:
            print(f"{program_name} fut.")
            break
        else:
            print(f"{program_name} nem fut.")
            print("Inditsa el vagy valasza ki a [2]")
            break

