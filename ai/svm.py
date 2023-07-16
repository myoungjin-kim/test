from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import numpy as np

def build_svm(features, labels):
    # 하이퍼파라미터 그리드 설정
    param_grid = {
        'C': [1.0, 10.0, 100.0],
        'kernel': ['linear', 'rbf']
    }
    
    # GridSearchCV를 사용하여 최적의 하이퍼파라미터 탐색
    model = GridSearchCV(SVC(), param_grid, cv=2)
    model.fit(features, labels)

    # 최적의 모델 반환
    return model.best_estimator_

from sklearn.svm import SVC

# def build_svm(features, labels):
#     # 하이퍼파라미터 조정을 위한 변수
#     C = 1.0      # 오차 허용 범위 (소프트 마진)
#     kernel = 'rbf'  # 커널 타입 (여기서는 방사 기저 함수(RBF) 커널 사용)
    
#     # SVM 모델 초기화
#     model = SVC(C=C, kernel=kernel)
    
#     # 모델 훈련
#     model.fit(features, labels)
    
#     # 학습된 모델 반환
#     return model
