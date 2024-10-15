# Video-Localization
pip install moviepy
video_path = "C:/kullanici/video.mp4"
image_path = "C:/kullanici/resim.png"
output_path = "C:/kullanici/output.mp4"
start_time = 2  # Resmin videoya ekleneceği başlangıç saniyesi
end_time = 8    # Resmin videodan kaldırılacağı bitiş saniyesi

# Videoyu işleyip resim ekleme
process_video(video_path, image_path, output_path, start_time, end_time)
