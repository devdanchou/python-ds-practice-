def list_manipulation(lst, command, location, value=None):


    if command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst
    elif command == "remove":
        if location == "beginning":
            lst.pop(0)
            return lst
        if location == "end":
            lst.pop(-1)
            return lst
