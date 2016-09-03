import pandas, sys

mode = sys.argv[1]
data = pandas.read_csv(sys.argv[2])

# First remove the ampersand in the author list
data['Author'] = [i.replace('&', ';') for i in data['Author']]
#print(data['Author'])

for row in range(len(data['Author'])):
    # Then, swap the first name and last name
    d = data['Author'][row]
    author_list = [j[1].strip() + " " + j[0].strip() for j in [i.split(',') for i in d.split(';')]]
    # Next, split the name
    author_list = [i.split(sep=' ', maxsplit=1) for i in author_list]
    # Reduce the first name to an initial
    author_list = ', '.join([(i[0][0] + " " + i[1]).replace(' ', '. ') for i in author_list])
    # Finally, boldify the required author
    if len(sys.argv) > 2:
        author_list = author_list.replace(sys.argv[3], "<strong>" + sys.argv[3] + "</strong>")
    data.loc[row,('Author')] = author_list

    # Now output the HTML
    if mode == "conference":
        print("<li>", end="")
        print(data['Author'][row] + ", ", end="")
        print("<em>", end="")
        print('"' + data['Title'][row] + '," ', end="")
        print("</em>", end="")
        print(data['Booktitle'][row] + " - ", end="")
        print(data['Year'][row], end="")
        print("</li>")
    elif mode == "journal":
        print("<li>", end="")
        print(data['Author'][row] + ", ", end="")
        print("<em>", end="")
        print('"' + data['Title'][row] + '," ', end="")
        print("</em>", end="")
        print(data['Journal'][row] + ", ", end="")
        print('vol. ' + str(int(data['Volume'][row])) + ", no. " + str(int(data['Number'][row])) + ' - ', end="")
        print(data['Year'][row], end="")
        print("</li>")
