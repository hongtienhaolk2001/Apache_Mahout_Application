import os
import re
import pandas as pd


class Mahout:
    def __init__(self, data_name):
        self.__data_path = f"./data/recommendation/{data_name}"

    def training(self, numRecommendations=3):
        try:
            cmd = f"hadoop fs -put {self.__data_path} /rating.csv"
            os.popen(cmd)
            cmd = f"mahout recommenditembased --input /rating.csv --output recommendations --numRecommendations {numRecommendations} \
            --outputPathForSimilarityMatrix similarity-matrix --similarityClassname SIMILARITY_COSINE"
            os.popen(cmd)

        except:
            pass

    def __preprocessing(self) -> dict:
        cmd_result = os.popen("hadoop fs -cat recommendations/part*")
        recommendation_lst = []
        for result in cmd_result:
            user_id, book_id = result.split('\t')
            book_id_lst = re.sub(r'[\[\]]', "", book_id)
            book_id_lst = re.findall(r'\d+(?=:)', book_id_lst)
            for i in book_id_lst:
                recommendation_lst.append([int(user_id), i])

        return recommendation_lst  # [[user_id, id], [user_id, id]]

    def export_csv(self, file_name="recommendation.csv"):
        try:
            recommendation_lst = self.__preprocessing()
            df = pd.DataFrame(recommendation_lst, columns=['User_id', 'book_id'])
            df.to_csv(f"./data/recommendation/{file_name}", index=False)

        except:
            pass

    def add_to_database(self):
        pass

# if __name__ == "__main__":
#     book_recommendation = Mahout(data_name="rating.csv")
#     # Pipeline
#     book_recommendation.training()
#     book_recommendation.export_csv()
