from sklearn.ensemble import VotingClassifier
from random_forest import build_random_forest
from gradient_boosting import build_gradient_boosting
from svm import build_svm
from sklearn.multioutput import MultiOutputClassifier

def build_voting_ensemble(features, labels):
    # VotingClassifier에 사용할 개별 모델 생성
    random_forest_model = build_random_forest(features, labels)
    gbm_model = build_gradient_boosting(features, labels)
    svm_model = build_svm(features, labels)

    # 가중치 조정을 위한 개별 모델의 성능 기준 설정
    weights = [0.5, 0.3, 0.2]  # 각 개별 모델에 대한 가중치 -----> 미세 조정 필요

    # VotingClassifier 초기화
    estimators = [
        ('random_forest', random_forest_model),
        ('gbm', gbm_model),
        ('svm', svm_model)
    ]

    voting_model = VotingClassifier(estimators=estimators, voting='hard', weights=weights)

    # 모델 훈련
    voting_model.fit(features, labels)

    # 학습된 앙상블 모델 반환
    return voting_model

