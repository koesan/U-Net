# Segmentation with U-Net 

This project aims to do image segmentation using the U-Net model. The project includes processing the dataset, training the model, and showing the results.

***

Bu proje, U-Net modelini kullanarak görüntü segmentasyonu yapmayı amaçlamaktadır. Proje kapsamında veri setinin işlenmesi, modelin eğitimi ve sonuçların görselleştirilmesi aşamaları gerçekleştirilmiştir.

## Dataset

The dataset used in this project is the **[Semantic Segmentation Drone Dataset](https://www.kaggle.com/datasets/santurini/semantic-segmentation-drone-dataset)**. This dataset has drone images for different segmentation tasks.

***

Projede kullanılan veri seti, dron görüntüleri üzerinde semantik segmentasyon için kullanılan **[Semantic Segmentation Drone Dataset](https://www.kaggle.com/datasets/santurini/semantic-segmentation-drone-dataset)**'tir. Bu veri seti, dron görüntüleri üzerinde çeşitli segmentasyon görevleri için kullanılır.

## Project Steps

### 1. Processing the Dataset

Before training the model, images in the dataset need to be resized and split into 256x256 pieces. This is done using the `böl.py` script.

- The images are resized to be multiples of 256.
- Then these images are cut into small pieces of 256x256 pixels.

This makes the data ready for training the model.

***

Veri setindeki görüntüler, eğitim için uygun hale getirilmeden önce yeniden boyutlandırılır ve 256x256 boyutlarında parçalara ayrılır. Bu işlem için `böl.py` betiği kullanılmıştır.

- Görseller, 256'nın katı olacak şekilde yeniden boyutlandırılır.
- Ardından, bu görseller 256x256 boyutlarında küçük parçalara bölünür.
  
Bu adımlar, modelin eğitiminde verilerin uygun şekilde kullanılmasını sağlar.

### 2. Uploading to Google Drive

The processed dataset is uploaded to Google Drive and used in the Colab environment. This allows the model to be trained on Google Colab.

***

İşlenmiş veri seti Google Drive'a yüklenir ve buradan Colab ortamında kullanılabilir hale getirilir. Bu sayede modelin eğitim süreci Google Colab üzerinde gerçekleştirilebilir.

### 3. Training the Model

model is trained using the U-Net architecture. During training dataset is fed into model along with labels and the model learns which class each pixel belongs to.

***

Model, U-Net mimarisi kullanılarak segmentasyon görevi için eğitilir. Eğitim sırasında veri seti, etiketleriyle birlikte modele beslenir ve model, her pikselin hangi sınıfa ait olduğunu öğrenir.

### 4. Visualizing the Results

After training, model's predicted segmentations are shown. Below is an example of a segmentation result:

***

Eğitim tamamlandıktan sonra modelin tahmin ettiği segmentasyon sonuçları görselleştirilir. Aşağıdaki görsel, eğitim sonucunda elde edilen segmentasyon çıktısına ait bir örnektir:

![indir](https://github.com/user-attachments/assets/19897ea5-1f3d-41e7-85fe-cdb22dea0fd7)
