import time 
import webbrowser

total_breaks = 3 					#initialize number of breaks 
break_count = 0 					#counter initialization

print("This program started on " + time.ctime()) 	#printing the starting time 
while break_count < total_breaks :
	time.sleep(1*360*360) 				#wait an hour 
	webbrowser.open("https://www.youtube.com/watch?v=wWFJw5TnQgs") #open browser and play ur favourite vibe 
	break_count += 1





