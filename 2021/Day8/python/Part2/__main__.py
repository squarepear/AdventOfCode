import string

def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    tests = []

    for line in lines:
        test = line.split('|')


        tests.append((test[0].strip().split(' '), test[1].strip().split(' ')))

    for test in tests:
        calc = [ [], [], [], [], [], [], [] ]

        for digit in test[0]:
            length = len(digit)
            segs = []

            if length == 2: # 1
                segs = [2, 5]

            elif length == 3: # 7
                segs = [0, 2, 5]

            elif length == 4: # 4
                segs = [1, 2, 3, 5]
            

            if len(segs) > 0:
                for seg in segs:
                    print(seg, calc[seg], [char for char in digit])
                    calc[seg] += [char for char in digit]
            
            print(calc)
        
        output = [''] * 7

        vals = [list(dict.fromkeys(seg)) for seg in calc]

        print(calc)
        print(vals)

        while '' in output:
            tempOut = output.copy()

            for i in range(len(output)):
                if output[i] != '':
                    continue

                current = vals[i]

                print(current)

                if len(vals[i]) == 1:
                    val = string.ascii_lowercase[vals[i][0]]

                    for j in string.ascii_lowercase[:7]:
                        if not j in current:
                            val = j
                            break
                    
                    if val == '':
                        continue

                    for j in range(len(vals)):
                        vals[j].update([val])
                    
                    tempOut[i] = val
            
            print(output, tempOut)

            if output == tempOut:
                break

            output = tempOut
            
        
        print(output)
                    


        

            
        
                

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()