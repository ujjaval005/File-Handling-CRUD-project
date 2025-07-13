from pathlib import Path

def readfileandfolder():
    path=Path('')
    items=list(path.glob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} - {item.name}")

def createfile():
    try:
        readfileandfolder()
        filename = input('Enter the name of the file to create: ')
        p=Path(filename)
        if not p.exists():
            with open(p, 'w') as f:
                Data = input('Enter the content of the file: ')
                f.write(Data)

            print(F"FILE CREATED SUCCEFULLY")

        else:
            print(f"File '{filename}' already exists.")

    except Exception as e:
        print(f"An error occurred: {e}")

def readfile():
    try:
        readfileandfolder()
        filename = input('Enter the name of the file to read: ')
        p = Path(filename)
        if p.exists() and p.is_file():
            with open(p, 'r') as f:
                content = f.read()
                print(content)

            print(F'FILE READ SUCCEFULLY')
        else:
            print(f"File '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def updatefile():
    try:
        readfileandfolder()
        filename = input('Enter the name of the file to update: ')
        p = Path(filename)
        if p.exists() and p.is_file():
            print('Press 1 for renaming the file')
            print('Press 2 for overwriting the file')
            print('Press 3 for appending to the file')
            choice = int(input('Enter your choice: '))

            if choice == 1:
                new_name = input('Enter the new name for the file: ')
                p2= Path(new_name)
                if not p2.exists():
                    p.rename(p2)
                    print(f'FILE RENAMED TO {new_name} SUCCEFULLY')
                else:
                    print(f"File '{new_name}' already exists.")
            if choice == 2:
                with open(p, 'w') as f:
                    Data = input('Enter the new content to overwrite the file: ')
                    f.write(Data)
                print(F'FILE OVERWRITTEN SUCCEFULLY')

            elif choice == 3:
                with open(p, 'a') as f:
                    Data = input('Enter the content to append to the file: ')
                    f.write(' '+ Data +'\n')
                    

            print(F'FILE UPDATED SUCCEFULLY')
        else:
            print(f"File '{filename}' does not exist.")

    except Exception as e:
        print(f"An error occurred: {e}")

def deletefile():
    try:
        readfileandfolder()
        filename = input('Enter the name of the file to delete: ')
        p = Path(filename)
        if p.exists() and p.is_file():
            p.unlink()
            print(f"File '{filename}' deleted successfully.")
        else:
            print(f"File '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

print('Enter 1 to create a file')
print('Enter 2 to read a file')
print('Enter 3 to update a file')
print('Enter 4 to delete a file')

choice = input('Enter your choice: ')

match choice:
    case '1':
        createfile()
    case '2':
        readfile()
    case '3':
        updatefile()
    case '4':
        deletefile()
    case _:
        print('Invalid choice, please try again.')
