import reduction_functions as rf
if __name__ == '__main__':
    (path,size) = rf.get_path_and_size_of_largest_file()
    print("Largest file: from " + path + ", size " + str(size) + "B.")