#2주에 해당하는 14개의 데이터셋으로 학습
#현재온도, 현재습도, 강수형태(맑음, 눈, 비), 하늘 상태(흐림 같은), 일 최고기온, 일 최저기온, 교통수단, 실외/실내

#데이터셋은 학습이 잘 되었나 확인이 가능하게 온도를 -7에서 32까지 3도씩 증가해 변별력을 만듦
# 하늘상태(SKY) 코드 : 맑음(1), 구름많음(3), 흐림(4)
# 강수형태(PTY) 코드 : (초단기) 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7) 
#                      (단기) 없음(0), 비(1), 비/눈(2), 눈(3), 소나기(4) 
# 강수형태는 일단 없음, 비, 눈만 사용
#교통 수단은 도보 = 0, 버스/지하철 = 1, 자가용 = 2
#활동범위는 실내 = 0, 실외 = 1
#온도를 제외한 나머지는 임의 설정
#상의와 하의만 선정

#위의 조건을 기반으로 만든 데이터로 학습해 적절한 하이퍼파라미터 설정 예정
from sklearn.model_selection import cross_val_score
from voting_emsemble import build_voting_ensemble
from data_process import data_encoder, data_decoder

def calculate_error_rate(y_true, y_pred):
    error_count = sum(1 for true, pred in zip(y_true, y_pred) if true != pred)
    error_rate = error_count / len(y_true)
    return error_rate

def load_test_data(file_path):
    features = []
    label1s = []
    label2s = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            feature = [float(x) for x in data[:8]]  # 피처는 문자열을 실수형으로 변환하여 저장
            label1 = data[8]  # 첫번째 라벨
            label2 = data[9]  # 두번째 라벨
            features.append(feature)
            label1s.append(label1)
            label2s.append(label2)

    label1_enc, _ = data_encoder(label1s)
    label1s = label1_enc.transform(label1s)

    label2_enc, _ = data_encoder(label2s)
    label2s = label2_enc.transform(label2s)
    
    return features, label1s, label2s, label1_enc, label2_enc

def evaluate_ensemble_model(model, features, labels, enc, k):
    # k-fold 교차 검증 수행
    scores = cross_val_score(model, features, labels, cv=k)
    mean_accuracy = scores.mean()
    error_rates = [1 - accuracy for accuracy in scores]
    mean_error_rate = sum(error_rates) / k

    print('Accuracy Scores:', scores)
    print('Mean Accuracy:', mean_accuracy)
    print('Error Rates:', error_rates)
    print('Mean Error Rate:', mean_error_rate)

    # 예측 결과 디코딩
    predictions = model.predict(features)
    decoded_predictions = enc.inverse_transform(predictions)
    print('Decoded Predictions:', decoded_predictions)

# 테스트 데이터 로드
test_file = 'demo/ai/test_dataset_1.txt'
test_features, test_label1s, test_label2s, label1_enc, label2_enc = load_test_data(test_file)

# 첫 번째 라벨에 대한 앙상블 모델 빌드 및 평가
ensemble_model1 = build_voting_ensemble(test_features, test_label1s)
evaluate_ensemble_model(ensemble_model1, test_features, test_label1s, label1_enc, k=2)

# 두 번째 라벨에 대한 앙상블 모델 빌드 및 평가
ensemble_model2 = build_voting_ensemble(test_features, test_label2s)
evaluate_ensemble_model(ensemble_model2, test_features, test_label2s, label2_enc, k=2)

