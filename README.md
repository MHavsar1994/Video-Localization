Kodun Amacı
Bu kod, bir video üzerine bir resmi, belirli bir zaman aralığında (örn. 2. saniyeden 8. saniyeye kadar) yerleştirir. Ayrıca, resmin belirlenen zamanlarda boyut ve pozisyonunu değiştirerek zoom in ve zoom out efekti uygulanmaktadır.

Kullanım
Aşağıdaki fonksiyonları kullanarak videonun üzerine resim ekleyebilirsiniz:

1. load_assets(video_path, image_paths)
Bu fonksiyon, temel video ve resim dosyalarını yükler.

video_path: Video dosyasının yolu.
image_paths: Resim dosyasının yolu.
2. overlay_image_on_green_area(base_video, image, start_time, end_time)
Bu fonksiyon, belirli zaman dilimlerinde resim üzerinde büyütme ve konumlandırma efektlerini uygular.

base_video: Üzerine resim eklemek istediğiniz video.
image: Eklenecek resim.
start_time: Resmin videoya yerleştirilmeye başlanacağı saniye.
end_time: Resmin videodan kaldırılacağı saniye.
3. create_video_with_image(base_video, image, output_path, start_time, end_time)
Bu fonksiyon, videoya resmi ekler ve çıktı olarak birleştirilmiş videoyu oluşturur.

output_path: Son videonun kaydedileceği dosya yolu.
4. process_video(video_path, image_path, output_path, start_time, end_time)
Ana fonksiyon olup, video ve resim yollarını vererek sürecin tamamını çalıştırır.

Çıkış
Kodun başarılı bir şekilde çalıştırılmasından sonra, output.mp4 dosyası belirttiğiniz dizine kaydedilecektir. Videonun 2. ve 8. saniyeleri arasında resim görünür olacak ve belirli noktalarda zoom in/out efekti uygulanacaktır.

Hata Yönetimi
Eğer video ya da resim dosyaları yüklenemezse, hata mesajı terminalde görüntülenecektir. Ayrıca, dosya yolu hataları gibi sorunlar için FileNotFoundError ele alınmıştır.
