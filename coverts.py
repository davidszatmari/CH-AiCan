import os
import csv
import json



def convert_json_to_csv(input_directory):
    cov = 0
    lis = 0
    for root, dirs, files in os.walk(input_directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            file1_path = os.path.join(dir_path, 'file1.json')
            file2_path = os.path.join(dir_path, 'file2.json')
            

            if os.path.exists(file1_path) and os.path.exists(file2_path):
                output_filename = os.path.join(dir_path, 'output.csv')
                cov += 1
                lis += 1
                
                with open(file1_path, 'r') as json_file1, open(file2_path, 'r') as json_file2:
                    data1 = json.load(json_file1)
                    data2 = json.load(json_file2)

                with open(output_filename, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile, delimiter=';')

                    # Write the header row
                    csv_writer.writerow(["Field", "Value", "", "Field", "Value"])

                    # Write the rows with merged data
                    for field in data1:
                        csv_writer.writerow([field, data1[field].get(''), '', field, data2[field].get('')])
                        

                print(f"CSV file '{output_filename}' has been created with semicolon (;) delimiter in '{dir_path}'.")
                print(f"{cov}/{lis} konvertalva.")
                
            elif file1_path == file1_path and file2_path == file2_path:
                cov == cov
                lis += 1
                print(f"{file1_path},{file2_path} hibas.")
                print(f"{cov}/{lis} konvertalva.")
                
                
            else:
                print("Convertalas sikertelen")
                cov = 0
                print(f"{cov}/{lis} konvertalva.")

