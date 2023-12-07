
import csv
import json
import os

def readjson (FILEPATH):
    with open(FILEPATH, 'r') as f:
        json_data = json.load(f)

    json_type = json_data["Meta(Acqusition)"]["doc_type"]
    json_id = json_data["Meta(Acqusition)"]["doc_id"]
    json_origin = json_data["Meta(Acqusition)"]["doc_origin"]
    json_passage = json_data["Meta(Refine)"]["passage"]
    json_abstractive = json_data["Annotation"]["summary1"]
    if json_data["Annotation"]["summary2"] is None:
        json_extractive = json_data["Annotation"]["summary3"]
    else:
        json_extractive = json_data["Annotation"]["summary2"]

    csv_file = open('TestPassages_public.csv', 'a', newline='')
    jsonwriter = csv.writer(csv_file)
    # print(json_type, json_id, json_origin, json_passage, None, json_abstractive, json_extractive)
    #json_type
    jsonwriter.writerow([json_type, json_id, json_origin, json_passage, None, json_abstractive, json_extractive])

    csv_file.close()

'''
def readcsv () :
    input = open('TrainingPassages.csv', 'r')
    rd = csv.reader(input)

    output0 = open('TrainingPassages0.csv', 'a', newline='')
    wr0 = csv.writer(output0)
    output1 = open('TrainingPassages1.csv', 'a', newline='')
    wr1 = csv.writer(output1)
    output2 = open('TrainingPassages2.csv', 'a', newline='')
    wr2 = csv.writer(output2)
    output3 = open('TrainingPassages3.csv', 'a', newline='')
    wr3 = csv.writer(output3)

    for row in rd:
        id_str = row[1].split('-')
        id_str = id_str[-1]
            if id >= 1000 and id <3000:
                wr0.writerow(row)
            if id >= 3000 and id <5000:
                wr1.writerow(row)
            if id >= 5000 and id <7000:
                wr2.writerow(row)
            if id >= 7000 and id <9000:
                wr3.writerow(row)
        id = id_str[1:]
        if id=="id" or id=="d":
            continue
        else:
            id = int(id)
            if id >= 1000 and id <3000:
                wr0.writerow(row)
            if id >= 3000 and id <5000:
                wr1.writerow(row)
            if id >= 5000 and id <7000:
                wr2.writerow(row)
            if id >= 7000 and id <9000:
                wr3.writerow(row)

    output0.close()
    output1.close()
    output2.close()
    output3.close()
    input.close()

'''

'''
for i in range (0, 4):
    output_number = i
    OUTPUTPATH = 'TrainingPassages'+str(output_number)+'.csv'

    csvf = open(OUTPUTPATH, 'w', newline='')
    wr = csv.writer(csvf)
    wr.writerow(['type', 'id', 'origin', 'passage', 'passage_morp', 'abstractive', 'extractive'])

    csvf.close()

readcsv()
'''


csv_file = 'TestPassages_public.csv'
csvf = open(csv_file, 'w', newline='')
wr = csv.writer(csvf)
wr.writerow(['type', 'id', 'origin', 'passage', 'passage_morp', 'abstractive', 'extractive'])


ROOT = 'src/public/test/2~3sent'
filelst = os.listdir(ROOT)


for file in filelst:
    filepath = ROOT + '/' + file
    print(filepath)
    if file[0] != 'R':
        continue
    readjson(filepath)
