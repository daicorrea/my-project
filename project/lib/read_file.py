import os

class ReadFile():
    """This Class reads a file and returns a list of data.
    In case it's not possible to open the file, a message is throw."""

    def __init__(self, filename):
        self._data = []
        self.filename = filename
        self.read_content()

    #rU stands for: "open for input as a text file with universal newline interpretation".
    #Mode "rU" is also allowed, for symmetry with "rb".
    def read_content(self):
        try:
            #dirpath = os.getcwd()
            #print(dirpath)
            #content = open(self.filename, 'rU')
            #rows = content.read()
            #content.close()
            #self._data = rows

            lines = []
            with open(self.filename, 'rU') as content:
                for line in content:
                    lines.append(line)
            print(lines)

        except IOError:
            raise IOError("Houston, we have a problem scanning the document :(")

    def get_data(self):
        return self._data