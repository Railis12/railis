def line_count():
    file = open("story.txt","r")
    count=0
    for line in file:
        if line[0] not in 'T':
            count+= 1
    file.close()
    print("Teksta rindas, kas nesākas ar burtu 'T'=",count)
