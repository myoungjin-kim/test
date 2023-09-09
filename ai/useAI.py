from ai.data_process import load_data
from ai.TabNet import train_model
import numpy as np
EXPECTED_LENGTH = 8 # 모델 사용시 필요한 인풋 데이터의 길이

class ClothingRecommendationModel:
    #모델 초기화
    def __init__(self):
        self.clf_tops = None
        self.clf_bottoms = None
        self.tops_enc = None
        self.bottoms_enc = None

    #모델 학습 및 재학습
    def retrain_model(self, train_data):
        features, labels_tops, labels_bottoms, [self.tops_enc, self.bottoms_enc] = load_data(train_data)
        self.clf_tops, self.clf_bottoms = train_model(features, labels_tops, labels_bottoms)

    #모델사용
    def get_clothing_recommendation(self, input_data):
        if self.clf_tops is None or self.clf_bottoms is None:
            raise ValueError("The models have not been trained yet. Please train the models first.")
        if not isinstance(input_data, (list, np.ndarray)) or len(input_data) != EXPECTED_LENGTH:
            raise ValueError("Invalid input data. Please provide valid input data.")
        processed_input_data = np.array(input_data).reshape(1, -1)
        preds_tops = self.clf_tops.predict(processed_input_data)
        preds_bottoms = self.clf_bottoms.predict(processed_input_data)
        decoded_preds_tops = self.tops_enc.inverse_transform(preds_tops)
        decoded_preds_bottoms = self.bottoms_enc.inverse_transform(preds_bottoms)
        return decoded_preds_tops, decoded_preds_bottoms

# # 사용 예시
# if __name__ == "__main__":
#     model = ClothingRecommendationModel()
#     model.retrain_model(train_data)
#     input_data = [...]  # 입력 데이터
#     tops, bottoms = model.get_clothing_recommendation(input_data)
#     print("Recommended tops:", tops)
#     print("Recommended bottoms:", bottoms)