# 사용 예시
# clf_tops와 clf_bottoms는 각각 상의(Tops)와 하의(Bottoms) 모델의 학습 결과를 담은 변수라고 가정합니다.
# plot_model_results(clf_tops, clf_bottoms)

import matplotlib.pyplot as plt

def plot_model_results(clf_tops, clf_bottoms):
    # 상의(Tops) 모델과 하의(Bottoms) 모델에 대한 그래프를 한 페이지에 표시
    fig, axs = plt.subplots(4, 1, figsize=(10, 20), sharex=True)

    # 상의(Tops) 학습 손실 그래프
    axs[0].plot(clf_tops.history['loss'])
    axs[0].set_title('Model loss for Tops')
    axs[0].set_ylabel('Loss')
    axs[0].legend(['Train'], loc='upper left')

    # 상의(Tops) 학습 및 검증 정확도 그래프
    axs[1].plot(clf_tops.history['train_accuracy'])
    axs[1].plot(clf_tops.history['valid_accuracy'])
    axs[1].set_title('Model accuracy for Tops')
    axs[1].set_ylabel('Accuracy')
    axs[1].legend(['Train', 'Validation'], loc='upper left')

    # 하의(Bottoms) 학습 손실 그래프
    axs[2].plot(clf_bottoms.history['loss'])
    axs[2].set_title('Model loss for Bottoms')
    axs[2].set_ylabel('Loss')
    axs[2].legend(['Train'], loc='upper left')

    # 하의(Bottoms) 학습 및 검증 정확도 그래프
    axs[3].plot(clf_bottoms.history['train_accuracy'])
    axs[3].plot(clf_bottoms.history['valid_accuracy'])
    axs[3].set_title('Model accuracy for Bottoms')
    axs[3].set_ylabel('Accuracy')
    axs[3].set_xlabel('Epoch')
    axs[3].legend(['Train', 'Validation'], loc='upper left')

    plt.tight_layout()
    plt.show()