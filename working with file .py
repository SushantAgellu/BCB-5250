import os


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "rosalind_ini5.txt")
output_path = os.path.join(os.path.expanduser("~"), "Desktop", "final_output.txt")

try:
    with open(desktop_path, "r") as infile:
        lines = infile.readlines()  

    even_lines = [lines[i] for i in range(1, len(lines), 2)]

    with open(output_path, "w") as outfile:
        outfile.writelines(even_lines)

    print(f"Processing complete! Check 'output.txt' on your Desktop.")

except FileNotFoundError:
    print("Error: input.txt not found on your Desktop. Make sure the file exists and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
