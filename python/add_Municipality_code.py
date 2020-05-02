import datetime
# python csv https://note.nkmk.me/python-csv-reader-writer/
# python pands query https://note.nkmk.me/python-pandas-query/
# python pandas replace https://qiita.com/kazetof/items/992638be821a617b900a
# python pandas all https://qiita.com/ysdyt/items/9ccca82fc5b504e7913a

municipality_code = "../data/Municipality_code.csv"
todays_tokyo_cases = "../data/tokyo_" + datetime.date.today().strftime("%Y_%m_%d") + ".csv"
addedcode_tokyo_cases = "../data/addedcode_tokyo_" + datetime.date.today().strftime("%Y_%m_%d") + ".csv"

# df = pd.read_csv(todays_tokyo_cases)
# df["Municipality_code"] = 0
# print(df)

def main():
    municipality_code_dict = read_municipality_code()
    add_municipality_code(municipality_code_dict)

def read_municipality_code():
    import csv
    with open(municipality_code, "r", encoding = "utf-8-sig") as f: # encoding = "utf-8-sig" でutf-8を指定
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows += [row]
    return dict(rows[1:])

def add_municipality_code(municipality_code_dict):
    ""
    # 参考 https://note.nkmk.me/python-csv-reader-writer/
    import pandas as pd
    df = pd.read_csv(todays_tokyo_cases)
    df.insert(4, "Municipality_code", 0)
    for municipality in municipality_code_dict.keys():
        df_subset = df.query("Municipality == @municipality") # https://note.nkmk.me/python-pandas-query/, https://qiita.com/kazetof/items/992638be821a617b900a
        df.loc[df_subset.index, "Municipality_code"] = int(municipality_code_dict[municipality])
    df.sort_values(by="Municipality_code", inplace=True) # https://qiita.com/ysdyt/items/9ccca82fc5b504e7913a
    df.to_csv(addedcode_tokyo_cases, index=False)

if __name__ == "__main__":
    main()