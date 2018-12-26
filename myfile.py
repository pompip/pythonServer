class MyFile(object):
    def __init__(self,address):
        self.address = address
        

    def writelines(self,text):
        file = open(self.address,"a")
        file.write(str(text))
        file.write('\n')
        file.flush()
        
    def read(self):
        file = open(self.address,"r")
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close()

        