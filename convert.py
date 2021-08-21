import pandas as pd
import re

df = pd.read_csv("glossary.tsv", sep="\t")
cats = pd.read_csv("categories.tsv", sep="\t", index_col="code")


df[(df.Recommendation == "R") | (df.Recommendation == "A")][
    ["English", "Chinese", "Recommendation", "Subfield1", "Subfield2"]
].drop_duplicates().rename(
    columns={
        "English": "eng",
        "Chinese": "chi",
        "Recommendation": "rec",
        "Subfield1": "field1",
        "Subfield2": "field2",
    }
).to_json(
    "glossary.json", orient="records"
)

cats[["description"]].to_json("categories.json")
