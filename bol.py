import os
import cv2

# Görsellerin bulunduğu klasörler
segmentation_folder = '' # label_images_semantic klasörü'nün konumu 
original_images_folder = '' # original_images klasörü'nün konumu 

# Çıktı klasörleri aynı klasörün içinde olmalı
output_folder_seg = ' Çıktı konumu '
output_folder_img = ' Çıktı konumu '

# Klasörleri oluştur (varsa kontrol et)
if not os.path.exists(output_folder_seg):
    os.makedirs(output_folder_seg)
if not os.path.exists(output_folder_img):
    os.makedirs(output_folder_img)

# 256'nın en büyük katını hesaplama fonksiyonu
def get_max_multiple_of_256(n):
    return (n // 256) * 256

# Görselleri ölçeklendirme ve parçalama fonksiyonu
def resize_and_split_image(image_path, output_folder, output_prefix, file_format):
    img = cv2.imread(image_path)
    img_name = os.path.basename(image_path).split('.')[0]

    height, width = img.shape[:2]
    new_height = get_max_multiple_of_256(height)
    new_width = get_max_multiple_of_256(width)

    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

    tile_size = 256
    num_tiles_x = new_width // tile_size
    num_tiles_y = new_height // tile_size
    tile_count = 1

    for i in range(num_tiles_y):
        for j in range(num_tiles_x):
            left = j * tile_size
            upper = i * tile_size
            right = left + tile_size
            lower = upper + tile_size
            img_tile = resized_img[upper:lower, left:right]
            cv2.imwrite(os.path.join(output_folder, f"{output_prefix}_{tile_count}.{file_format}"), img_tile)
            tile_count += 1

# Segmentasyon resimlerini işleyelim
for img_name in os.listdir(segmentation_folder):
    if img_name.endswith('.png'):
        resize_and_split_image(os.path.join(segmentation_folder, img_name), output_folder_seg, img_name.split('.')[0], 'png')

# Normal resimleri işleyelim
for img_name in os.listdir(original_images_folder):
    if img_name.endswith('.png'):
        resize_and_split_image(os.path.join(original_images_folder, img_name), output_folder_img, img_name.split('.')[0], 'jpg')
