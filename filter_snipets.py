import os
import sys

def remove_one_line_entries(lines):
    curr_count =0
    final_lines = []
    new_lines = []
    for line in lines:
        if line == "---------------------------------\n":
            if curr_count == 1:
                pass
            else:
                new_lines.append(line)
                final_lines.extend(new_lines)
            new_lines = []
            curr_count = 0
        else:
            new_lines.append(line)
            curr_count += 1
    return final_lines

if __name__ == "__main__":
    rootDir = sys.argv[1]    
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            if fname == 'snippets.java':
                f = open(dirName+ "/" + fname, 'r')
                body = f.readlines()
                f.close()
                f = open(dirName+"/" + fname, 'w')
                f.writelines(remove_one_line_entries(body))
                f.close()

