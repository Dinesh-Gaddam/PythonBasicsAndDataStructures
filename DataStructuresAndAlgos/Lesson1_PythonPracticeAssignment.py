class Lesson1_PythonPracticeAssignment(object):
    """description of class  def MultiLineComment(self):
        return 
                     Looks like we can't have comment as a block
                    There is no switch case in python
                   # switch(item):
                      #    case "tophat":
                      #        total+= 2
                      #    break
                      #    case "bowtie":
                       #       total+= 4
                       #   break
                        #  case "jacket":
                        #      total+= 2
                       #   break
                       #   case "monocle":
                       #       total+= 5
                       #   break
                    #  """


class Classy(object):
    def __init__(self):
        self.items = []
    def getClassiness(self): 
        total = 0
        for item in self.items: 
            if item == "tophat":
                total +=  2
            elif item == "bowtie":
                total +=  4

        #    elif item == "jacket":
               # total +=  2

            elif item == "monocle":
                total +=  5
        return total         
      
    def addItem(self,name):
        self.items.append(name)

def main():
    me = Classy()
    # Should be 0
    print (me.getClassiness())

    me.addItem("tophat")
    # Should be 2
    print (me.getClassiness())

    me.addItem("bowtie")
    me.addItem("jacket")
    me.addItem("monocle")
    # Should be 11
    print (me.getClassiness())

    me.addItem("bowtie")
    # Should be 15
   # print me.getClassiness()
    print (me.getClassiness())
    
print ("Dinesh")

if __name__ == "__main__":
    # execute only if run as a script
    main()