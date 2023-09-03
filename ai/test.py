from data_process import load_data
from TabNet import train_model
from graph import plot_model_results
import numpy as np

test_data = [
    ['니트/스웨터', '코튼팬츠', 0, 1, 0, -10, -7, 50, 0, 1],
    ['후드티셔츠', '코튼팬츠', 2, 4, 2, -4, -1, 50, 2, 4],
    ['후드티셔츠', '트레이닝/조거팬츠', 2, 1, 5, -1, 2, 50, 2, 1],
    ['맨투맨/스웨트셔츠', '트레이닝/조거팬츠', 1, 4, 11, 5, 8, 50, 1, 4],
    ['긴소매티셔츠', '데님팬츠', 0, 1, 14, 8, 11, 50, 0, 1],
    ['긴소매티셔츠', '데님팬츠', 1, 3, 17, 11, 14, 50, 1, 3],
    ['반소매티셔츠', '데님팬츠', 0, 4, 20, 14, 17, 50, 0, 4],
    ['스포츠상의', '스포츠하의', 0, 3, 26, 20, 23, 50, 0, 3],
    ['스포츠상의', '숏팬츠', 1, 4, 29, 23, 26, 50, 1, 4],
    ['민소매티셔츠', '스포츠하의', 1, 3, 35, 29, 32, 50, 1, 3]
]

#data process
features, labels_tops, labels_bottoms, [tops_enc, bottoms_enc] = load_data(test_data)

#모델 학습
clf_tops, clf_bottoms = train_model(features, labels_tops, labels_bottoms)

# 테스트 데이터
X_test = np.array([0, 4, 20, 14, 17, 50, 0, 4]).reshape(1, -1)

# 테스트 데이터에 대한 예측 수행
preds_tops = clf_tops.predict(X_test)
preds_bottoms = clf_bottoms.predict(X_test)

# 디코드된 예측 결과
decoded_preds_tops = tops_enc.inverse_transform(preds_tops)
decoded_preds_bottoms = bottoms_enc.inverse_transform(preds_bottoms)

print(decoded_preds_tops, decoded_preds_bottoms)

# 모델 결과 시각화
plot_model_results(clf_tops, clf_bottoms)