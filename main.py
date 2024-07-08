import os
from PIL import Image


#
def collect_images_from_folders(base_folder, folder_list):
    images = []
    for folder_name in folder_list:
        folder_path = os.path.join(base_folder, folder_name)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(
                    (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff")
                ):
                    file_path = os.path.join(folder_path, file_name)
                    images.append(Image.open(file_path))

    return images


def create_gallery(images, images_per_row, padding=10):
    if not images:
        return None

    # Set the size for each image in the gallery
    widths, heights = zip(*(i.size for i in images))
    max_width = max(widths) + padding
    max_height = max(heights) + padding

    # Create the gallery image
    num_rows = (len(images) + images_per_row - 1) // images_per_row
    total_width = images_per_row * max_width + padding
    total_height = num_rows * max_height + padding

    gallery_image = Image.new("RGB", (total_width, total_height), (255, 255, 255))

    for index, img in enumerate(images):
        x = (index % images_per_row) * max_width + padding // 2
        y = (index // images_per_row) * max_height + padding // 2
        gallery_image.paste(img, (x, y))

    return gallery_image


def save_image_as_tiff(image, output_path):
    if image:
        image.save(output_path, compression="tiff_deflate")
    else:
        print("No image to save.")


def main():
    base_folder = "folders/"  # root folder
    folder_list = [
        "1369_12_Наклейки 3-D_3",
        "1388_12_Наклейки 3-D_3",
        "1388_2_Наклейки 3-D_1",
        "1388_6_Наклейки 3-D_2",
    ]  # List of folders to search for images
    output_file = "Result.tif"
    images_per_row = 5  # number of images per row
    padding = 50  # padding between images

    images = collect_images_from_folders(base_folder, folder_list)
    gallery_image = create_gallery(images, images_per_row, padding)
    save_image_as_tiff(gallery_image, output_file)
    print(f"TIFF file saved as {output_file}")


if __name__ == "__main__":
    main()
