import os 
import shutil
##os.system("date")

##os.system("time")
##print (os.getcwd())
##print(os.listdir())


##source="C:/Users/Hp/Downloads/class97 coding/test1.txt"
##os.remove(source)

#source="C:/Users/Hp/Downloads/class97 coding/test2.txt"
#destination = "C:/Users/Hp/Downloads/class97 coding/test3.txt"
##shutil.copy(source,destination)

source1="C:/Users/Hp/Downloads/class97 coding/test2.txt"
source2="C:/Users/Hp/Downloads/class97 coding/test3.txt"
destination="C:/Users/Hp/Downloads/class97 coding/files"
shutil.move(source1,destination)
shutil.move(source2,destination)
