"""
Author: Ibezim Ikenna
User functions about date and time 
"""
import datetime #Importing the date library used for this task
import os # Importing library used for file paths and dir
from prettytable import PrettyTable

def date_arithmetic():
    """ This function would perform date arithmetic Operations""" 

    #Calculating the first Question and date 
    date1 = "Feb 27, 2000" # %b M, %d D, %Y
    dt1 = datetime.datetime.strptime(date1,"%b %d, %Y") #changing the date format into python date
    num_days = 3
    dt2 = dt1 + datetime.timedelta(days=num_days)

    #Calculating the second Question and date 
    date2 = "Feb 27, 2017"
    dm1 = datetime.datetime.strptime(date2,"%b %d, %Y")
    dm2 = dm1 + datetime.timedelta(days=num_days)
    
    #Calculating the third Question and date
    date3 = "Jan 1, 2017"
    date4 = "Oct 31, 2017"
    dm3 = datetime.datetime.strptime(date3, "%b %d, %Y")
    dm4 = datetime.datetime.strptime(date4, "%b %d, %Y")
    delta = dm4 - dm3

    #Returning the results in a tuple
    return dt2, dm2, delta.days

def file_reading_gen(path,fields=3, sep='|', header=True):
    """Reading through fields seperated text files and yield the text in each line"""
    try:
        fp = open(path,'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"can't find file {path}")
    else:
        with fp:
            line_c = 0
            for line in fp:
                line_c += 1
                store = line.strip("\n")
                store2 = store.split(sep)
                len1 = len(store2)
                if len1 != fields:
                    raise ValueError(f"{path} has{len1} fields on line {line_c} but expected 3 fields")
                    continue
                else:
                    if line_c == 1 and header is True:
                        continue
                    else:
                        yield tuple(store2)


class FileAnalyzer:
    """This class is used check for python files ending with .py"""

    def __init__(self, directory):
        """ This represents the class File Analyzer and stores the path in directory."""
        self.directory = directory
        self.files_summary = self.analyze_files()
        
    def analyze_files(self):
        """ This function computes the number of functions, classes, line and chars in every file and hold the record."""
        num_file = 0
        results = dict()
        try:
            list_files = os.listdir(self.directory)
        except FileNotFoundError:
            raise FileNotFoundError("Can't find any file")
        else:
            for file in list_files:  #looping the files in the directly
                num_file += 1
                if file.endswith(".py"): # Looking for files that end with .py
                    try:
                        fp = open(os.path.join(self.directory, file), "r")
                    except FileNotFoundError:
                        raise FileNotFoundError(f"Can't open file no {num_file}")
                    else:
                        with fp:
                            c_total = 0 #Total length of Characters for the entire file
                            filename = file # Storing the file name
                            t_line = 0 # Getting the total number of line
                            t_def = 0 #Getting the total number of functions
                            t_class = 0 #Getting the total number of classes
                
                            for line in fp:
                                t_line += 1 # Counting each line
                                t_char = len(line)  #Length of characters for each line
                                n_line = line.strip() # gets rid of white spaces and new lines
                                c_total += t_char # adding each total char in line to the pervious total char in line
                                if n_line.startswith("def "): 
                                    t_def += 1 
                                elif n_line.startswith("class "):
                                    t_class += 1
                        results[filename] = {'class': t_class, 'function': t_def, 'line': t_line, 'char': c_total }
        return results
        
    def pretty_print(self):
        """ Function to arrange my output from files sumary into a tabular form"""
        pt = PrettyTable()
        for i in self.files_summary:
            pt.field_names = ["File Name", "Classes", "Functions", "Lines", "Characters"]
            pt.add_row(list([i, self.files_summary[i]["class"], self.files_summary[i]["function"], self.files_summary[i]["line"], self.files_summary[i]["char"]]))
        print(pt)  #Using a Print statement here because i tried to return self.pt and it didnt give me anything but the print works
  
def main():
    """
    Test cases
    """  
    result = date_arithmetic()
    print(result) 

    path="/Users/ikenna/Downloads/SE540/filetxt.txt"
    for cwid, name, major in file_reading_gen(path, 3, '|', True):
        print(cwid, name, major)
   
    result2 = FileAnalyzer("/Users/ikenna/Downloads/se810")
    result2.pretty_print() # remember string classes
                                                                                                                                                                                                                                                                                                                                                                                                        
if __name__ == "__main__":
    main()
