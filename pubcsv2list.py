import pandas, sys

mode = sys.argv[1]
data = pandas.read_csv(sys.argv[2])
data.sort_values('Identifier')

# First remove the ampersand in the author list
data['Author'] = [i.replace('&', ';') for i in data['Author']]

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
    data.loc[row,('Author')] = author_list.replace('..', '.')

    urlstring = str(data['URL'][row])
    if not 'http' in urlstring:
        urlstring = None

    # Now output the HTML
    print("<li>", end="")
    print(data['Author'][row] + ", ", end="")
    print("<em>", end="")
    print('&ldquo;' + data['Title'][row] + ',&rdquo; ', end="")
    print("</em>", end="")
    if mode == "conference":
        print(data['Booktitle'][row] + " - ", end="")
    elif mode == "journal":
        print(data['Journal'][row] + ", ", end="")
        print('vol. ' + str(int(data['Volume'][row])) + ", no. " + str(int(data['Number'][row])) + ' - ', end="")
    print(data['Year'][row], end="")
    if urlstring:
        print(" <a href=\"" + urlstring + "\">(link)</a>",end="")
    print("</li>")
