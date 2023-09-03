# 사용 예시
# features는 피쳐의 정보, labels_tops, labels_bottoms는 각각 상의와 하의의 라벨입니다. 각 자료형은 NumPy 형태이어야 합니다.
# 각각 상의(Tops)와 하의(Bottoms) 모델의 학습 결과를 담은 변수인 clf_tops와 clf_bottoms를 반환합니다.
# train_model(features, labels_tops, labels_bottoms)

from pytorch_tabnet.tab_model import TabNetClassifier
from sklearn.model_selection import train_test_split

#모델 학습 함수
def train_model(features, labels_tops, labels_bottoms):   
  #학습 데이터와 검증 데이터로 분할
  X_train_tops, X_valid_tops, y_train_tops, y_valid_tops = train_test_split(features, labels_tops, test_size=0.2, random_state=42)
  X_train_bottoms, X_valid_bottoms, y_train_bottoms, y_valid_bottoms = train_test_split(features, labels_bottoms, test_size=0.2, random_state=42)

  # 상의(Tops)를 위한 TabNet 모델 학습
  clf_tops = TabNetClassifier()  # TabNet 분류기 생성
  clf_tops.fit(
    X_train_tops, y_train_tops,  # 훈련 데이터의 특성과 라벨
    eval_set=[(X_train_tops, y_train_tops), (X_valid_tops, y_valid_tops)],  # 모델 성능 평가를 위한 데이터셋
    eval_name=['train', 'valid'],  # 데이터셋에 대한 이름
    eval_metric=['accuracy'],  # 평가 지표
    max_epochs=100,  # 에포크의 최대 수
    patience=10,  # 조기 종료를 위한 인내심 (과적합 방지)
    batch_size=256,  # 미니 배치의 크기
    virtual_batch_size=128,  # 가상 배치의 크기
    num_workers=0,  # 데이터 로딩에 사용할 작업자의 수
    weights=1,  # 클래스 가중치
    drop_last=False  # 마지막 배치를 무시할지 여부
  ) 

  # 하의(Bottoms)를 위한 TabNet 모델 학습
  clf_bottoms = TabNetClassifier()  # TabNet 분류기 생성
  clf_bottoms.fit(
    X_train_bottoms, y_train_bottoms,  # 훈련 데이터의 특성과 라벨
    eval_set=[(X_train_bottoms, y_train_bottoms), (X_valid_bottoms, y_valid_bottoms)],  # 모델 성능 평가를 위한 데이터셋
    eval_name=['train', 'valid'],  # 데이터셋에 대한 이름
    eval_metric=['accuracy'],  # 평가 지표
    max_epochs=100,  # 에포크의 최대 수
    patience=10,  # 조기 종료를 위한 인내심 (과적합 방지용)
    batch_size=256,  # 미니 배치의 크기
    virtual_batch_size=128,  # 가상 배치의 크기
    num_workers=0,  # 데이터 로딩에 사용할 작업자의 수
    weights=1,  # 클래스 가중치
    drop_last=False  # 마지막 배치를 무시할지 여부
  )
  
  return clf_tops, clf_bottoms