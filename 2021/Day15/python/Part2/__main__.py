def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0
    
    

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
