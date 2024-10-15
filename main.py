import moviepy.editor as mp
from moviepy.video.fx.all import resize

# Temel video ve resim dosyalarını yükleme fonksiyonu
def load_assets(video_path, image_paths):
    try:
        base_video = mp.VideoFileClip(video_path)  # Video dosyasını yükle
        images = [mp.ImageClip(img).set_duration(base_video.duration) for img in image_paths]  # Resimleri yükle
        return base_video, images
    except Exception as e:
        print(f"Hata: {e}")
        return None, None

# Yeşil alana görüntü yerleştirme fonksiyonu
def overlay_image_on_green_area(base_video, image, start_time=2, end_time=8):
    def make_zoom_clip(t):
        # 4. saniyede büyüt ve konumu değiştir
        if 4 <= t < 6:
            scale = 2  # Resmi 2 katına çıkar
            position = (200, 700)  # 4. saniyede yeni konuma al
        # 6. saniyede konumu 325, 850 yap
        elif 6 <= t < 7:
            scale = 1  # Resmin boyutunu değiştirme
            position = (325, 850)  # 6. saniyede bu konumda
        # 7. saniyede boyut ve konum belirle
        elif 7 < t < 8:
            scale = 1  # 7. saniyede normal boyut
            position = (200, 800)  # 7. saniyede bu konuma getir
        else:
            scale = 1  # Diğer zamanlarda normal boyut
            position = (325, 850)  # Başlangıçtaki konum

        return resize(image, newsize=(int(image.size[0] * scale), int(image.size[1] * scale))).set_position(position)

    # Tüm zaman dilimleri için yeni görüntü kliplerini oluştur
    clips = [make_zoom_clip(t).set_duration(1).set_start(t) for t in range(start_time, end_time)]

    # Resimlerin videoda birleştirilmesi
    video_with_image = mp.CompositeVideoClip([base_video] + clips)

    return video_with_image

# Video ve resmi birleştirerek çıktı oluşturma fonksiyonu
def create_video_with_image(base_video, image, output_path, start_time=2, end_time=8):
    # Resmi yeşil alana yerleştir
    video_with_image = overlay_image_on_green_area(base_video, image, start_time=start_time, end_time=end_time)
    
    # Son videoyu kaydet
    video_with_image.write_videofile(output_path, codec="libx264", fps=24)

# Ana fonksiyon
def process_video(video_path, image_path, output_path, start_time=2, end_time=8):
    try:
        # Video ve resim dosyasını yükle
        base_video, images = load_assets(video_path, [image_path])
        
        # Eğer video veya resimler yüklenememişse
        if base_video is None or images is None:
            print("Videoyu veya resmi yükleme sırasında bir hata oluştu.")
            return
        
        image = images[0]  # Tek resim kullandığımızı varsayıyoruz
        
        # Video ve resim birleştir
        create_video_with_image(base_video, image, output_path, start_time, end_time)
        
        print(f"Video oluşturuldu: {output_path}")
    
    except FileNotFoundError as e:
        print(f"Hata: {e}")
    except Exception as e:
        print(f"Bilinmeyen bir hata oluştu: {e}")

# Örnek kullanım
video_path = "C:/Users/mharu/OneDrive/Masaüstü/New folder (3)/video.mp4"
image_path = "C:/Users/mharu/OneDrive/Masaüstü/xx/image1.png"
output_path = "C:/Users/mharu/PycharmProjects/pythonProject2/output.mp4"
start_time = 2  # Resmin videoya eklenmeye başladığı zaman
end_time = 8    # Resmin videodan kaldırıldığı zaman

# Video işleme
process_video(video_path, image_path, output_path, start_time, end_time)
