def start():
    ray = "█"
    notray = "0"
    try:
        loc = input("Enter file path or press enter to use the file provided with the code\n\nExample file path: "
                    "D:\\Folder\\filename.csv\n\n")
        if loc == "":
            loc = "Example.csv"
        file = open(loc, "r", encoding='utf-8-sig')
        RowArray = []
        col = 0
        counter = 1
        for i in file:
            indexesRays = []
            row = 0
            list = i.split(",")
            final = ""
            for word in list:
                ray = "█"
                notray = "0"
                add = "null"
                if word == "":
                    add = notray
                if word == "1":
                    add = ray
                if add != "null":
                    final += add + " "
                    row += 1
                if row == 15:
                    RowArray.append(final)
                    row = 0
                    final = ""
                    col += 1
            if col == 10:
                print(counter)
                counter += 1
                for k in RowArray:
                    print(k)
                rowValue = 0
                for k in RowArray:
                    rowValue += 1
                    splittedRow = k.split()
                    # print(splittedRow)
                    if "█" in splittedRow:
                        for item in splittedRow:
                            if item == "█":
                                rayCoordinates =[splittedRow.index(item) + 1, rowValue]
                                indexesRays.append(rayCoordinates)
                RowArray = ["\n"]
                # print(indexesRays)
                rayCounter = 0
                index = -1
                while True:
                    index += 1
                    try:
                        # print(str(indexesRays[index][0]) + " " + str(indexesRays[index][1]) + " " + str(indexesRays[index+1][0]) + " " + str(indexesRays[index + 1][1]) + " " + str(abs(indexesRays[index][0] - indexesRays[index][0])))
                        if abs(indexesRays[index][0] - indexesRays[index + 1][0]) <= 1 and abs(indexesRays[index][1] - indexesRays[index + 1][1]):
                            rayCounter += 1
                        elif rayCounter < 4:
                            rayCounter = 0
                    except IndexError:
                        # print("end")
                        break
                filteredDataArray = []
                filteredDataRow = []
                if rayCounter >= 4:
                    print("ray was found! It collided with the odoscope " + str(rayCounter + 1) + " times!")
                    row = 1
                    column = 1
                    c = 0
                    while True:
                        try:
                            # print(str(indexesRays[c]) + " " + str(column) + " " + str(row))
                            if indexesRays[c][0] != column or indexesRays[c][1] != row:
                                filteredDataRow.append(notray)
                            else:
                                filteredDataRow.append(ray)
                                c+= 1
                            if column == 15:
                                row += 1
                                column = 0
                                filteredDataArray.append(filteredDataRow)
                                filteredDataRow = []
                            column += 1
                            if row == 10:
                                break
                        except IndexError:
                            while row <= 10:
                                filteredDataRow.append(notray)
                                if column == 15:
                                    row += 1
                                    column = 0
                                    filteredDataArray.append(filteredDataRow)
                                    filteredDataRow = []
                                column += 1
                    # print(filteredDataArray)
                    print("\n")
                    c = 0
                    for k in filteredDataArray:
                        plane = ""
                        for i in k:
                            plane += i + " "
                        print(plane)
                col = 0
                input()
    except Exception as error:
        print(error)
        print("\n")
        start()


start()


# TODO: Algoritm doesn't work when two rays are on the same row