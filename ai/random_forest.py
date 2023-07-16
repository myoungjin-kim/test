from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np

def build_random_forest(features, labels):
    # 하이퍼파라미터 그리드 설정
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 3, 5]
    }

    # GridSearchCV를 사용하여 최적의 하이퍼파라미터 탐색
    # 최소 클래스 샘플 수를 교차 검증 폴드 수로 사용
    min_samples_per_class = min(np.bincount(labels))
    cv = min(5, min_samples_per_class)

    model = GridSearchCV(RandomForestClassifier(), param_grid, cv=2)
    model.fit(features, labels)

    # 최적의 모델 반환
    return model.best_estimator_

# from sklearn.ensemble import RandomForestClassifier

# def build_random_forest(features, labels):
#     # 하이퍼파라미터 조정을 위한 변수
#     n_estimators = 100  # 트리의 개수
#     max_depth = None    # 트리의 최대 깊이, None으로 설정하면 트리의 깊이가 제한되지 않음
    
#     # Random Forest 모델 초기화
#     model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    
#     # 모델 훈련
#     model.fit(features, labels)
    
#     # 학습된 모델 반환
#     return model