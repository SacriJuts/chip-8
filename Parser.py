"""Sys = {"address" : 0, "byte" : 1, "register" : 2}

instructions = (
    ("SYS", 0),
    ("CLS", 0),
    ("RET", 0),
    ("JP", 1, ),
    ("CALL", ),
    ("SE", ),
    ("SNE", ),
    ("SE", ),
    ("LD", ),
    ("ADD", ),
    ("LD", ),
    ("OR", ),
    ("AND", ),
    ("XOR", ),
    ("ADD", ),
    ("SUB", ),
    ("SHR", ),
    ("SUBN", ),
    ("SHL", ),
    ("SNE", ),
    ("LD", ),
    ("JP", ),
    ("RND", ),
    ("DRW", ),
    ("SKP", ),
    ("SKNP", ),
    ("LD", ),
    ("LD", ),
    ("LD", ),
    ("LD", ),
    ("ADD", ),
    ("LD", ),
    ("LD", ),
    ("LD", ),
    ("LD", ),
)"""

class Parser:

    def __init__(self, path):
        self.FilePath = path
        self.instructions = list()

    def parse(self):
        f = open(self.FilePath, 'r')

        file = f.read().split("\n")
        print(file)
        #reading the file
        i = 0
        while i < len(file):
            line = file[i].split(" ")
            for x in range(len(line)):
                pass


            i += 1

        f.close()

p = Parser("dafile.c8")
p.parse()
