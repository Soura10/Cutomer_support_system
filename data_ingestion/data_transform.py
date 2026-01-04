import pandas as pd 
#from langchain_core.documents import Document



class data_converter:

    def __init__(self):
        print("data converter class has init..")
        self.product_data=pd.read_csv(r"data\\flipkart_product_review.csv")
        #print(f"dataframe shape:{self.product_data.shape}")
        print(self.product_data.head())

    def data_transformation(self):
        



if __name__=="__main__":
    data_transformation=data_converter()