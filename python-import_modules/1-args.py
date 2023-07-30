import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    num_args = len(args)

    if num_args == 0:
        print(f"{num_args} arguments.")
    
    elif num_args == 1:
        number = args[0]
        print("1 argument:")
        print(f"{args.index(number)+1}: {number}")

    else:
        length = len(args)
        print(length, "arguments:")
        for argument in args:
            print(f"{args.index(argument)+1} : {argument}")
