# 사용한 모델
## tabnet
### 모델에 대한 설명
+ XGBoost와의 앙상블 고려중

https://www.intelligencelabs.tech/3ac72939-db45-4804-9b9d-3ec2c08ef504

https://github.com/dreamquark-ai/tabnet

### 파라미터
+ eval_metric: 이 매개변수는 평가 지표를 지정합니다. 이 예제에서는 'accuracy'가 사용됩니다. 이 값을 바꾸면 모델의 성능 평가 기준이 변경됩니다.

+ max_epochs: 이 매개변수는 모델이 전체 훈련 데이터셋에 대해 학습하는 횟수, 즉 에포크(epoch)의 최대 수를 지정합니다. 이 값을 크게 하면 모델이 더 많이 학습하지만, 과적합(overfitting)의 위험이 커질 수 있습니다.

+ patience: 이 매개변수는 조기 종료를 위한 인내심을 설정합니다. 검증 손실이 patience 에포크 동안 개선되지 않으면 학습이 조기 종료됩니다. 이 값을 크게 하면 모델이 더 오랫동안 학습하지만, 과적합의 위험이 커질 수 있습니다.

+ batch_size: 이 매개변수는 각 에포크에서 사용하는 미니 배치의 크기를 지정합니다. 이 값을 크게 하면 한 번에 더 많은 데이터를 처리할 수 있지만, 메모리 사용량이 늘어나고, 모델의 업데이트가 덜 자주 일어나게 됩니다.

+ virtual_batch_size: 이 매개변수는 TabNet의 특징 중 하나인 가상 배치 크기를 지정합니다. 가상 배치는 각 배치 내에서 공유되는 스텝(step)의 수를 줄임으로써 일반화를 돕습니다. 이 값을 변경하면 모델의 학습 동작이 바뀌게 됩니다.

+ num_workers: 이 매개변수는 데이터 로딩에 사용할 작업자(worker)의 수를 지정합니다. 이 값을 늘리면 데이터 로딩 속도가 빨라지지만, 더 많은 CPU 자원을 사용하게 됩니다.

+ weights: 이 매개변수는 각 클래스에 대한 가중치를 지정합니다. 이 값을 변경하면 모델이 각 클래스에 대해 얼마나 중요하게 생각하는지가 바뀌게 됩니다. 이는 불균형한 데이터셋에서 유용합니다.

+ drop_last: 이 매개변수는 마지막 배치가 배치 크기보다 작을 경우 해당 배치를 무시할지 여부를 지정합니다. 이 값을 True로 설정하면 마지막 배치가 배치 크기보다 작을 때 그 배치를 무시하게 됩니다. 이는 배치 크기를 일정하게 유지하려는 경우에 유용합니다.




# 가상 환경 설정

### CUDA 버전
11.7.0

### python 버전
3.9

### pytorch 설치
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia
### scikit-learn 설치
conda install scikit-learn

### pandas 설치
conda install pandas

### tabnet 설치
conda install -c conda-forge pytorch-tabnet
