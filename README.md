# U-Net Segmentasyonu

Bu proje, segmentasyon modelinin eğitimini gerçekleştirmeyi amaçlamaktadır. Proje, veri setinin işlenmesi, model eğitimi ve tahmin sonuçlarının görselleştirilmesi adımlarını içerir.

## Proje Özeti

## Kullanılan Kütüphaneler

Bu projede aşağıdaki kütüphaneler kullanılmaktadır:

- **TensorFlow**
- **OpenCV**
- **NumPy**
- **Matplotlib**
- **scikit-learn**

## Veri Seti

https://www.kaggle.com/datasets/santurini/semantic-segmentation-drone-dataset

### Veri Seti Adımları

1. **Veri Setinin İşlenmesi**: `böl.py` betiği kullanılarak veri setindeki görselleri 256 nın katına yeniden boyutlandırılmalı ardından resimleri 256x256 boyutlarında parçalara bölünmeli.
2. **Google Drive'a Yükleme**: İşlenmiş veri seti, Google Drive'a yüklenerek Colab ortamında kullanılabilir hale getiril.
