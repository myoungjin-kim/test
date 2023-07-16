from sklearn.preprocessing import LabelEncoder, OneHotEncoder

#문자로 되어있는 라벨(의상)만 인코드와 디코드 진행
def data_encoder(low_data):
    # 각 분류 항목에 대한 레이블 인코더와 원-핫 인코더를 생성합니다.
    # 레이블 인코더는 각 레이블을 숫자로 변환하고,
    # 원-핫 인코더는 이 숫자를 벡터로 변환합니다.
    # 이렇게 하면, 각 레이블을 모델이 처리할 수 있는 형태로 변환할 수 있습니다.
    label_enc = LabelEncoder()
    onehot_enc = OneHotEncoder(sparse_output=False)
    
    # 입력 받은 데이터에 대한 각각의 레이블 인코더와 원-핫 인코더를 생성하고 학습시킵니다.
    label_enc = LabelEncoder().fit(low_data)
    onehot_enc = OneHotEncoder(sparse_output=False).fit(label_enc.transform(low_data).reshape(-1, 1))
    
    return label_enc, onehot_enc

def data_decoder(encoders, encoded_data):
    label_enc, onehot_enc = encoders
    
    # 원-핫 인코딩을 역변환하여 숫자 레이블로 변환합니다.
    decoded_labels = onehot_enc.inverse_transform(encoded_data)
    
    # 숫자 레이블을 다시 원래의 문자열 레이블로 변환합니다.
    decoded_data = label_enc.inverse_transform(decoded_labels.reshape(-1, 1))
    
    return decoded_data
