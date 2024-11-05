import requests
import os
import json
import csv
"""
Downloads every csv file from the trailsinthedatabase website
"""
def main():
    # for each file in files7converted_files, make an api call to https://trailsinthedatabase.com/api/script/detail/11/{file_name} and download the csv file
    # for file in os.listdir("./files/converted_files/"):
    #     #rename file extension 
    #     # file_name =
    #     # script_file = "./files/converted_files/" + file
    #     file_name = file.split(".")[0]

    #     # make an api call to https://trailsinthedatabase.com/api/script/detail/11/{file_name} and download the csv file
    #     url = f"https://trailsinthedatabase.com/api/script/detail/11/{file_name}"
    #     response = requests.get(url)
    #     with open(f"./files/csv_files/{file_name}.csv", "wb+") as f:
    #         f.write(response.content)
    #     print(f"Downloaded {file_name}.csv")
    for file in os.listdir("./files/csv_files/"):
        # x = json.load(open("a0000_copy.csv","r",encoding='utf-8'))
        x = json.load(open(f"./files/csv_files/{file}","r",encoding='utf-8'))
        f = csv.writer(open(f"./files/refined_csv_files/{file}", "w",newline='',encoding='utf-8'))

        headers = "gameId,fname,scene,row,engChrName,engSearchText,engHtmlText,jpnChrName,jpnSearchText,jpnHtmlText,opName,pcIconHtml,evoIconHtml".split(",")
        f.writerow(headers)

        for x in x:
            f.writerow([x["gameId"],x["fname"],x["scene"],x["row"],x["engChrName"],x["engSearchText"],x["engHtmlText"],x["jpnChrName"],x["jpnSearchText"],x["jpnHtmlText"],x["opName"],x["pcIconHtml"],x["evoIconHtml"]])

if __name__ == "__main__":
    main()