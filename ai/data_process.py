# 사용 예시
# raw_data는 이중 리스트 형태의 데이터셋입니다.
# 데이터 증강과 라벨인코딩, 넘파이형식으로의 변환을 거쳐 반환됩니다.
# features, labels_tops, labels_bottoms, [tops_enc, bottoms_enc]를 반환합니다.
# features는 피쳐, labels_tops, labels_bottoms는 각각 상의, 하의의 라벨을 [tops_enc, bottoms_enc]는 상의하의의 인코더를 뜻합니다.
# load_data(raw_data)

from sklearn.preprocessing import LabelEncoder
import numpy as np

#피쳐의 현재 온도, 습도, 일 최고 온도, 일 최저 온도를 +-1 조정 해서 데이터를 256배 증강시킵니다.
#원래의 데이터가 2개, 변형된 데이터는 각각 1개로 원래의 데이터의 개수가 더 많게 하였다.
def augment_feature(original_feature):
    new_feature = []
    tem_feature = []
    hum_feature = []
    max_tem_feature = []
    min_tem_feature = []

    for sublist in original_feature:
        for i in range(2):
            augmented_feature = sublist[:4] + [sublist[4] - i] + sublist[5:]
            tem_feature.append(augmented_feature)
            augmented_feature = sublist[:4] + [sublist[4] - i] + sublist[5:]
            tem_feature.append(augmented_feature)
        
    for sublist in tem_feature:
        for i in range(2):
            augmented_feature = sublist[:5] + [sublist[5] - i] + sublist[6:]
            hum_feature.append(augmented_feature)
            augmented_feature = sublist[:5] + [sublist[5] + i] + sublist[6:]
            hum_feature.append(augmented_feature)
            
    for sublist in hum_feature:
        for i in range(2):
            augmented_feature = sublist[:6] + [sublist[6] - i] + sublist[7:]
            max_tem_feature.append(augmented_feature)
            augmented_feature = sublist[:6] + [sublist[6] + i] + sublist[7:]
            max_tem_feature.append(augmented_feature)
            
    for sublist in max_tem_feature:
        for i in range(2):
            augmented_feature = sublist[:7] + [sublist[7] - i] + sublist[8:]
            min_tem_feature.append(augmented_feature)
            augmented_feature = sublist[:7] + [sublist[7] + i] + sublist[8:]
            min_tem_feature.append(augmented_feature)

    # new_feature 리스트에 증강된 데이터를 추가합니다.
    new_feature.extend(min_tem_feature)
    

    return new_feature


#라벨을 256배 증강시킵니다.
def augment_label(original_label):
    new_label = []

    for sublist in original_label:
        for i in range(256):
            new_label.append(sublist)

    return new_label

#입력 받은 위치의 텍스트 파일을 읽어와 ,를 기준으로 데이터를 구분해 피쳐와 라벨 추출
#추출된 라벨을 라벨 인코딩하여 피쳐와 인코딩된 라벨, 인코더를 반환
def load_data(raw_data):
    features = []
    tops = []
    bottoms = []
    
    for data in raw_data:
        top = data[0]  # 첫번째 라벨
        bottom = data[1]  # 두번째 라벨
        feature = [float(x) for x in data[2:]]  # 피처는 문자열을 실수형으로 변환하여 저장\

        features.append(feature)
        tops.append(top)
        bottoms.append(bottom)

    #라벨 인코딩
    tops_enc = LabelEncoder().fit(tops)
    encoded_tops = tops_enc.transform(tops)
    bottoms_enc = LabelEncoder().fit(bottoms)
    encoded_bottoms = bottoms_enc.transform(bottoms)
    
    # 각각의 라벨을 묶어 하나의 라벨 생성
    encoded_labels = list(zip(encoded_tops, encoded_bottoms))
    
    #데이터 증강 (256배)
    features = augment_feature(features)
    encoded_labels = augment_label(encoded_labels)
    
    #리스트를 넘파이 형으로 변형
    features = np.array(features)
    labels_tops = np.array([label[0] for label in encoded_labels])
    labels_bottoms = np.array([label[1] for label in encoded_labels])

    return features, labels_tops, labels_bottoms, [tops_enc, bottoms_enc]