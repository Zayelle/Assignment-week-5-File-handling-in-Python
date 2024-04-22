try:
     # Open the file in write mode('w')

     with open("my_file.txt", "w" ) as file:
     
     # Write three lines of text to the file:

          file.write ("Hello...welcome to our platform.\n")
          file.write ("This is a beauty and wellness platform.\n")
          file.write ("Call these number if interested:+254700\n")

    #Open the file in append mode ('a') and append three additional lines of text

     with open("my_file.txt","a") as file:
          file.write("We offer a couple affordable services.\n")
          file.write("The services range from 1000 and above.\n")
          file.write("We have discounts every Wednesdays.\n")
          
    # Open the file in read mode ('r') and read its content

     with open("my_file.txt", "r") as file:
     
# Read each line and display it on the console

         for line in file:
             print(line.strip())

except FileNotFoundError:
       print("File not found. Ensure the file exists or create a new one")


except PermissionError:
       print("Permission denied. You do not have permission to access this file at the moment. ")


finally:
        print("Script execution completed")