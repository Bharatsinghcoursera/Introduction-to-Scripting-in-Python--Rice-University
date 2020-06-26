IDENTICAL = -1 # define IDENTICAL value

# Problem 1: Finding the first difference between two lines
def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if len(line1) == len(line2):
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                return i
        return IDENTICAL
    else:
        min_len = min(len(line1), len(line2))
        for i in range(min_len):
            if line1[i] != line2[i]:
                return i
        if min_len == 0:
            return 0
        return i+1
#print(singleline_diff(line1, line2))



# Problem 2: Presenting the differences between two lines in a nicely formatted way
def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    idx = singleline_diff(line1, line2)
    if idx != -1:
        return "{0}\n{2}\n{1}\n".format(line1, line2, "=" * idx + "^")
    elif idx == -1:
        return ''
    else:
        return ''
         
#print(singleline_diff_format(line1, line2, idx))



# Problem 3: Finding the first difference across multiple lines

lines1 = ['abcdefg', 'abcd']
lines2 = ['abcdefg', 'abce']
print(lines1)

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if len(lines1) == len(lines2):
        for i in range(len(lines1)):
            diff = singleline_diff(lines1[i], lines2[i])
            if diff != IDENTICAL:
                return (i, diff)
        return (IDENTICAL, IDENTICAL)
    else:
        min_len = min(len(lines1), len(lines2))
        for i in range(min_len):
            diff = singleline_diff(lines1[i], lines2[i])
            if diff != IDENTICAL:
                return (i, diff)
        if  min_len == 0:
            return (0, 0)
        return (i+1, 0)



# Problem 4: Getting lines from a file

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    myfile = open(filename, 'rt')
    mylines = myfile.readlines()
    fhand = []
    for lines in mylines:
        newlines = lines.rstrip()
        fhand.append(newlines)
    return fhand

    myfile.close()



# Problem 5: Finding and formatting the first difference between two files
def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    indx = multiline_diff(lines1, lines2)
    if indx == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    else:
        (line, index) = indx
        l1 = lines1[line] if line < len(lines1) else ''
        l2 = lines2[line] if line < len(lines2) else ''
        return "Line {0}:\n{1}\n{3}\n{2}\n".format(line, l1, l2, "=" * index + "^")



