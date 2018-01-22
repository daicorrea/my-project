class ReadFile():
    """This Class reads a file and returns a list of data.
    In case it's not possible to open the file, one message is throw."""

    # Creating File Constructor
    def __init__(self, filename):
        self._data = []
        self.filename = filename
        self.read_content()

    # Function to Read File Content
    def read_content(self):
        try:
            # Opening the file
            # rU stands for: "open for input as a text file with universal newline interpretation".
            # Mode "rU" is also allowed, for symmetry with "rb".
            with open(self.filename, 'rU') as content:
                data = content.readlines()  # Passing each line for a list
            for line in data:
                words = line.rstrip().split(';')  # Removing special character like space and splitting my list by ;
                # Removing data column name line.
                if 'PROPERTY_NAME' not in line:
                    self._data.append(words)
        except IOError:
            raise IOError("Houston, we have a problem scanning the document :(")

    # Function to Return the List of Data
    def get_data(self):
        return self._data