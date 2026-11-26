from PIL import Image, ImageOps
import os

for fname in os.listdir("."):
    if fname.upper().endswith(".JPG"):
        with Image.open(fname) as img:
            # 1. 根據 EXIF 資訊自動將圖片轉正為實際像素方向
            img = ImageOps.exif_transpose(img)
            
            # 2. 確保色彩模式為 RGB（避免存檔報錯）
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
                
            # 3. 等比例縮小至寬度 1000px
            if img.width > 1000:
                ratio = 1000 / img.width
                img = img.resize((1000, int(img.height * ratio)), Image.Resampling.LANCZOS)
                
            img.save(fname, "JPEG", quality=82, optimize=True)

print("全部自動轉正並壓縮完成！")