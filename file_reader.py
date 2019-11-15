"""
Author: Ibezim Ikenna
User function to read files for my homework
"""
def file_reading_gen(path,fields, sep, header=True):
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
                    print(f"{path} has {len1} fields on line {line_c} but expected {fields} fields")
                    continue
                else:
                    if line_c == 1 and header is True:
                        continue
                    else:
                        yield tuple(store2)
  
def main():
    """
    Test cases
    """  

    path="/Users/ikenna/Downloads/se810/grades.txt"
    for cwid, name, major, m in file_reading_gen(path, 4, '|', True):
        print(cwid, name, major,)
   
                                                                                                                                                                                                                                                                                                                                                                                                        
if __name__ == "__main__":
    main()
