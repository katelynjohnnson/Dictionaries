# this program writes three lines of data
# to a file
def main():

    # open a file named philosophers.txt
    outfile = open('philosophers.txt', 'w')

    # write the names of three philosophers to the file
    # john locke, david hume, and edmund burke
    outfile.write('John Locke, David Hume, Edmund Burke\n)
