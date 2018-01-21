import os

class ReadFile():
    """This Class reads a file and returns a list of data.
    In case it's not possible to open the file, a message is throw."""

    def __init__(self, filename):
        self._data = []
        self.filename = filename
        self.read_content()

    def read_content(self):
        try:
            #dirpath = os.getcwd()
            #print(dirpath)

            # rU stands for: "open for input as a text file with universal newline interpretation".
            # Mode "rU" is also allowed, for symmetry with "rb".
            with open(self.filename, 'rU') as content:
                data = content.readlines()
                #print(data)

            for line in data:
                words = line.rstrip().split(';')
                # Removing data column name line.
                if 'PROPERTY_NAME' not in line:
                    self._data.append(words)

            #for i in range(1,2):
                #print(data[i])

        except IOError:
            raise IOError("Houston, we have a problem scanning the document :(")

    def get_data(self):
        return self._data