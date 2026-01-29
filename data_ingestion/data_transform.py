from xml.dom.minidom import Document
import pandas as pd 
from langchain_core.documents import Document



class data_converter:

    def __init__(self):
        print("data converter class has init..")
        self.product_data=pd.read_csv(r"data\\flipkart_product_review.csv")
        ##print(f"dataframe shape:{self.product_data.shape}")
        ##print(self.product_data.head())

    def data_transformation(self):
        '''
        # Combining relevant columns to create a comprehensive text field
        self.product_data['combined_text'] = self.product_data[['product_name', 'review_title', 'review_text']].astype(str).agg(' '.join, axis=1)
        
        # Creating a list of documents
        documents = []
        for _, row in self.product_data.iterrows():
            doc = {
                'text': row['combined_text'],
                'metadata': {
                    'product_id': row['product_id'],
                    'product_name': row['product_name'],
                    'review_rating': row['review_rating'],
                    'review_date': row['review_date']
                }
            }
            documents.append(doc)
        
        print(f"Total documents created: {len(documents)}")
        return documents
        
        '''
        required_columns =  self.product_data.columns
        required_columns = list(required_columns[1:])
        print(required_columns)
        ##iterate over each rows and create document object
        
        product_list=[]
        for index, row in self.product_data.iterrows():
            object={
                "product_name":row["product_title"],
                "product_rating":row["rating"],
                "product_summary":row["summary"],
                "product_review":row["review"]
            }
            product_list.append(object)

        ##print("***below is my product list***")
        ##print(f"total products:{len(product_list)}")   
        ##print(product_list[1]) 

        #iterate over product_list and create document object
        docs1=[]
        for entry in product_list:
            metadata={
                "product_name":entry["product_name"],
                "product_rating":entry["product_rating"],
                "product_summary":entry["product_summary"],
            }
            
            doc = Document(page_content=entry["product_review"],metadata=metadata)
            docs1.append(doc)

        #print(f"total document created:{len(docs1)}")   
        #print(docs1[0])
        return docs1;l


if __name__=="__main__":
    data_con=data_converter()
    data_con.data_transformation()