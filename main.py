import os

choice = input("Do you want to autoremove the OpenVRDriver from the config file (y/n): ")

if choice == "y":
    choice2 = input("Do you know the path to the file (y/n): ")

    if choice2 == "y":
        propable_path = r"C:\Users\NAME\AppData\Local\openvr"
        print("path should be here " + propable_path)
        path = input("Enter the path to the file: ")

        path = path.replace('"', '')

        #path = r"C:\Users\MomoH\AppData\Local\openvr\openvrpaths.vrpath"

        assert os.path.isfile(path)
        with open(path, "r") as f:
            lines = f.readlines()
            #print(lines)

        for line in lines:
            # Check if the line contains the string we are looking for
            if 'OpenVRDriver' in line:
                # If it does, remove the line from the list
                lines.remove(line)


        assert os.path.isfile(path)
        with open(path, "w") as f:
            text = f.writelines(lines)
            #print(text)

        print("done.\npls check if it worked on your own :)")

    if choice2 == "n":
        usr = input("Enter your username: ")
        propable_path = r"C:\Users\NAME\AppData\Local\openvr\openvrpaths.vrpath"
        path = propable_path.replace("NAME", usr)
        print("path should be here " + path)
        path = path.replace('"', '')
        

        #path = r"C:\Users\MomoH\AppData\Local\openvr\openvrpaths.vrpath"

        assert os.path.isfile(path)
        with open(path, "r") as f:
            lines = f.readlines()
            #print(lines)

        for line in lines:
            # Check if the line contains the string we are looking for
            if 'OpenVRDriver' in line:
                # If it does, remove the line from the list
                lines.remove(line)


        assert os.path.isfile(path)
        with open(path, "w") as f:
            text = f.writelines(lines)
            #print(text)

        print("done.\npls check if it worked on your own :)")
    

elif choice == "n":
    propable_path = r"C:\Users\NAME\AppData\Local\openvr"
    print("path should be here " + propable_path)
    deletethis = input("What do you want to delete: ")
    path = input("Enter the path to the file: ")

    path = path.replace('"', '')

    #path = r"C:\Users\MomoH\AppData\Local\openvr\openvrpaths.vrpath"

    assert os.path.isfile(path)
    with open(path, "r") as f:
        lines = f.readlines()
        #print(lines)

    for line in lines:
        # Check if the line contains the string we are looking for
        if deletethis in line:
            # If it does, remove the line from the list
            lines.remove(line)


    assert os.path.isfile(path)
    with open(path, "w") as f:
        text = f.writelines(lines)
        #print(text)

    print("done.\npls check if it worked on your own :)")