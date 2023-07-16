from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np

def build_gradient_boosting(features, labels):
    # 하이퍼파라미터 그리드 설정
    param_grid = {
        'learning_rate': [0.1, 0.01, 0.001],
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 7]
    }
    
    # GridSearchCV를 사용하여 최적의 하이퍼파라미터 탐색
    model = GridSearchCV(GradientBoostingClassifier(), param_grid, cv=2)
    model.fit(features, labels)

    # 최적의 모델 반환
    return model.best_estimator_

# from sklearn.ensemble import GradientBoostingClassifier

# def build_gradient_boosting(features, labels):
#     # 하이퍼파라미터 조정을 위한 변수
#     learning_rate = 0.1   # 학습률
#     n_estimators = 100    # 부스팅 스테이지의 개수
#     max_depth = 3         # 트리의 최대 깊이
    
#     # Gradient Boosting 모델 초기화
#     model = GradientBoostingClassifier(learning_rate=learning_rate, n_estimators=n_estimators, max_depth=max_depth)
    
#     # 모델 훈련
#     model.fit(features, labels)
    
#     # 학습된 모델 반환
#     return model