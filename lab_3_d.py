import reduction_functions as rf
if __name__ == '__main__':
    print("Ratio of downloads of graphical files to all the downloads is " + str(round(rf.get_graph_downloads_to_all_ratio(),2)))