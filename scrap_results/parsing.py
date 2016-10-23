import json

what_we_are_getting= 'online'


with open('parsed.json') as data_file:
    data = json.load(data_file)
    for row in data:
    	with open(row['stream_title']+"_"+what_we_are_getting+".txt", "a") as myfile:
    		myfile.write('['+str(row['created_at'])+', '+ str(row[what_we_are_getting])+'], ')