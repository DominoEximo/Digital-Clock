#!usr/bin/env python3



from datetime import datetime
import time
import os




def transform(time,list):
	elem = [*time] #1 3 : 1 5 : 0 1
	print(type(elem))
	k = 0
	for i in range(7):
		part = []
		
		for t in elem:
			if t == ":":
				part.append(list[10+k])
			else:
				part.append(list[int(t)+k])
		print(",".join(part).replace(","," "))
		k += 11







def main():

	

    DIGITS = [
	    " ┏━┓ ", "  ╻  ", " ┏━┓ ", " ┏━┓ ", " ╻ ╻ ", " ┏━┓ ", " ┏   ", " ┏━┓ ", " ┏━┓ ", " ┏━┓ ", "   ",
		" ┃ ┃ ", "  ┃  ", "   ┃ ", "   ┃ ", " ┃ ┃ ", " ┃   ", " ┃   ", "   ┃ ", " ┃ ┃ ", " ┃ ┃ ", " ╻ ",
		" ┃ ┃ ", "  ┃  ", "   ┃ ", "   ┃ ", " ┃ ┃ ", " ┃   ", " ┃   ", "   ┃ ", " ┃ ┃ ", " ┃ ┃ ", "   ",
		" ┃ ┃ ", "  ┃  ", " ┏━┛ ", " ┣━┫ ", " ┗━┫ ", " ┗━┓ ", " ┣━┓ ", "   ┃ ", " ┣━┫ ", " ┗━┫ ", "   ",
		" ┃ ┃ ", "  ┃  ", " ┃   ", "   ┃ ", "   ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", "   ",
		" ┃ ┃ ", "  ┃  ", " ┃   ", "   ┃ ", "   ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ╹ ",
		" ┗━┛ ", "  ╹  ", " ┗━━ ", " ┗━┛ ", "   ╹ ", " ┗━┛ ", " ┗━┛ ", "   ╹ ", " ┗━┛ ", " ┗━┛ ", "   ",
	]
    
    while True:
        
        
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        transform(current_time,DIGITS)
        time.sleep(1)
        os.system('cls')
        
        

    
		

    


if __name__ == "__main__":
    main()