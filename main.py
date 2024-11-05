import ast
import json
import re
import os
SINGLE_FILE = "a0000.py"
def main():
    name_lens = []
    
    # .dat files converted to .py files with the p3h tool
    for file in os.listdir("./files/converted_files/"):
    # for file in [SINGLE_FILE]:
        # file = SINGLE_FILE
        script_file = "./files/converted_files/" + file
        t_name_file = "./files/t_name.json"

        with open(script_file, "r",encoding='utf-8') as f:
            script = f.read()
        with open(t_name_file, "r",encoding='utf-8') as f:
            t_name = f.read()
        t_name = t_name_to_dict(t_name)

        # Get only the "script" lines
        dialogues= get_cmd_text_06_08(script)
        # Debug only
        with open("./files/debug/post_get_cmd_text_06_08.txt", "w",encoding='utf-8') as f:
            for dialogue in dialogues:
                f.write(dialogue)
                f.write("\n")
        # End of Debug
        
        # Refine the dialogues by removing
        refined_dialogues = []
        for dialogue in dialogues:
            chara,text = pre_process_cmd_text_06_08(t_name,dialogue)
            if chara != "" and text != "":
                refined_dialogues.append((chara,text))

        file_name = file.split(".")[0]
        len_refined_dialogues = len(refined_dialogues)
        name_lens.append((file_name,len_refined_dialogues))
        # Dump into a file the refined dialogues
        if len_refined_dialogues > 0:
            with open("./files/refined_texts/refined_dialogues_"+file_name+".txt", "w",encoding='utf-8') as f:
            # with open("./debug.txt", "w",encoding='utf-8') as f:
                for dialogue in refined_dialogues:
                    f.write(str(dialogue))
                    f.write("\n")
    # Debug only
    with open("./files/debug/name_lens_ref.txt", "w",encoding='utf-8') as f:
        for name_len in name_lens:
            f.write(str(name_len))
            f.write("\n")
    # End of debug
"""
From the raw script extract all the lines that contain "Cmd_text_0", except those that contains "LoadVar" and empty lines
script: raw .py script converted from .dat file
return: a list of lines that contain "Cmd_text_0"
"""
def get_cmd_text_06_08(script):
    lines = script.split("\n")
    result = []
    for line in lines:
        # if "Cmd_text_06" in line or "Cmd_text_08" in line:
        if "Cmd_text_0" in line  and line != " " and "Cmd_text_0C" not in line:
            result.append(line)
    return result
"""
From a raw line in the format of "Command("Cmd_text_06",[...])", extract the character id and the text
t_name: a dictionary that maps character ids to character names
line: raw line
return: a tuple of (character name, text)
"""
def pre_process_cmd_text_06_08(t_name,line):
    line = line.split("Command(\"Cmd_text_")[1][:-1][6:-1]
    # with open("./files/pre_preprocess.txt", "a",encoding='utf-8') as f:
    #     f.write(line)
    #     f.write("\n")
    if line[:3] == "INT":
        chara_id = line[4:]
        chara_id_str =""
        last_id = 0
        texts = []
        for (idx,id) in enumerate(chara_id):
            if id == ")":
                last_id = idx
                break
            chara_id_str += id
    else:
        # to handle the case where there's no INT() in the line
        chara_id_str = "65535"
        last_id = -3
    texts = line[last_id+3:]
    chara = get_chara_name(t_name,chara_id_str)

    # removing  ..Var("..") pattern
    var = re.findall(r'Var\(".*"\)', texts)
    if len(var) > 0:
        texts = [texts.replace(v, "") for v in var]
        texts = "".join(texts).strip()
    # texts = re.sub(r'.*Var\(".*"\)', "", texts).strip()

    # removing the <..> pattern
    sub_texts = re.findall(r'<[^<>]*>', texts)
    if len(sub_texts) > 0:
        for v in sub_texts:
            # print(f'v: {v} type:{type(v)}')
            texts = texts.replace(v, "")
        texts = "".join(texts).strip()
    # texts = re.sub(r'<[^<>]*>', "", texts).strip()

    # joining all the strings in the texts
    # texts = " ".join(re.findall(r'\"([^\"]*)\"', texts)).strip()
    texts = "<br/>".join(re.findall(r'\"([^\"]*)\"', texts)).strip()
    #removing the first and last <br/> if they exist
    if texts[:5] == "<br/>":
        texts = texts[5:]
    if texts[-5:] == "<br/>":
        texts = texts[:-5]
    return (chara,texts)

"""
From the t_name.json file, create a dictionary that maps character ids to character names
t_name: raw t_name.json file
return: a dictionary that maps character ids to character names
"""
def t_name_to_dict(t_name):

    dict_result = dict()
    t_name_dict = json.loads(t_name)["data"][0]["data"]
    for elem in t_name_dict:
        dict_result[elem["character_id"]] = elem["name"]
    with open("./files/debug/t_name_dump_dict.json", "w",encoding='utf-8') as f:
        json.dump(dict_result, f)
    return dict_result

"""
From the t_name dictionary,retrieve the character name from the character id
t_name: a dictionary that maps character ids to character names
chara_id: character id
return the character name
"""
def get_chara_name(t_name, chara_id):
    try:
        chara_id = int(chara_id)
        if chara_id == 65535 or chara_id == 65534:
            return "System"
    except:
        return t_name.get(chara_id,chara_id)
    return t_name.get(int(chara_id),chara_id)

if __name__ == "__main__":
    main()