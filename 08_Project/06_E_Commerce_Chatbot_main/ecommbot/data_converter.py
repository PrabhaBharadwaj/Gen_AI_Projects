# In this script , we converts csv data into specific format data[each rows to Document format with value and its metadata info] inside list
import pandas as pd
from langchain_core.documents import Document


def dataconveter():
    product_data = pd.read_csv("../data/flipkart_product_review.csv")

    data = product_data[["product_title", "review"]]

    product_list = []

    # Iterate over the rows of the DataFrame
    for index, row in data.iterrows():
        # Construct an object with 'product_name' and 'review' attributes
        obj = {"product_name": row["product_title"], "review": row["review"]}
        # Append the object to the list
        product_list.append(obj)

    docs = []
    for entry in product_list:
        metadata = {"product_name": entry["product_name"]}
        doc = Document(
            page_content=entry["review"], metadata=metadata
        )  # Convert document format with page_content value and its metadat
        docs.append(doc)
    return docs


# if __name__ == "__main__":
#     data = dataconveter()
#     print(data)
