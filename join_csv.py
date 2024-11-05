import csv
import os
ENG_CHAR_IDX = 4
ENG_TEXT_IDX = 5
ENG_HTML_TEXT_IDX = 6
ENG_JAP_CHAR_IDX = 7
def main():
    jp_to_en_names = get_jp_to_en_names()
    # file_name = "c0"
    file_name = "m2100"
    for file in os.listdir("./files/refined_csv_files/"):
        file_name = os.path.splitext(file)[0]
    # with open("./c0.csv", "r+",encoding='utf-8') as f:
        with open(f"./files/refined_csv_files/{file_name}.csv", "r+",encoding='utf-8') as f:
        # with open
            # my_csv = list(csv.reader(f))[1:]
            my_csv = list(csv.reader(f))
            print(my_csv)
            header = my_csv.pop(0)
            if len(my_csv)<=0:
                continue

            # with open("./c0.txt","r+",encoding='utf-8') as f2:
            with open(f"./files/refined_texts/refined_dialogues_{file_name}.txt","r+",encoding='utf-8') as f2:

                # print(my_csv)
                lines = f2.read().split("\n")
                lines_csv = []
                for line in lines:
                    if len(line) >0:
                        # line = line.split(",",1)[1][:-1][1:-1][1:]
                        line = line.split(",",1)[1][2:-2]
                        lines_csv.append(line)
                for csv_line in my_csv:
                    eng_text =lines_csv.pop(0)
                    csv_line[ENG_TEXT_IDX] =  eng_text.replace("<br/>"," ")
                    csv_line[ENG_HTML_TEXT_IDX] = eng_text
                    csv_line[ENG_CHAR_IDX] = jp_to_en_names.get(csv_line[ENG_JAP_CHAR_IDX],'')
                # with open("./c0_j.csv","w+",encoding='utf-8',newline='') as f3:
                with open(f"./final_csvs/{file_name}.csv","w+",encoding='utf-8',newline='') as f3:
                    writer = csv.writer(f3,delimiter=',',quoting=csv.QUOTE_MINIMAL,quotechar='"',escapechar='\\')
                    writer.writerow(header)
                    for row in my_csv:
                        writer.writerow(row[1:][:-1])
             
    pass
"""
Crates a dictionary in the form of {jp_name:en_name} from the unique_jp_names.txt and unique_translated_names.txt files, 
containing all characters/npc names.
"""
def get_jp_to_en_names():
    jp_to_en_names = {}
    with open("./files/unique_jp_names.txt", "r",encoding='utf-8') as f:
        jp_names = f.read().split("\n")
    with open("./files/unique_translated_names.txt", "r",encoding='utf-8') as f:
        en_names = f.read().split("\n")
    for jp_name,en_name in zip(jp_names,en_names):
        jp_to_en_names[jp_name] = en_name
    return jp_to_en_names
if __name__ == "__main__":
    main()