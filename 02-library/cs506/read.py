def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    
    file = []
    with open(csv_file_path, 'r') as a:
        f = a.readlines()
        for line in f:
            data = line.split(",")
            data = [float(i) if i.isdigit() else i for i in data]
        file.append(data)
        
    
    #raise NotImplementedError()
    return data