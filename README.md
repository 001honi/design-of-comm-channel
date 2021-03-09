# Servo kontrolü için uçtan uca haberleşme kanalı tasarımı

Proje arkadaşım Bengü BİLGİÇ ile hazırladığımız final sunumu [linktedir](assets/final_sunum.pdf).

<p align="center">
  <img src="https://github.com/001honi/design-of-comm-channel/blob/main/assets/scheme.png" />
</p> 

## Dosya Hiyerarşisi
#### arduino
- receiver.ino <br> _Servoya bağlı alıcı Arduino kodlarını içerir_
- transmitter.ino <br> _Potansiyometrelere bağlı verici Arduino kodlarını içerir_
#### share
- db.py <br> _GNU Radio alıcı tarafında UDP’ye bağlanarak yaratılan udp_sink.db’ye veri akışı yapar_ 
- db2ser.py <br> _Veritabanından Seri Porta veri akışı yapar_ 
- gui_receiver_db.py <br> _Veritabanındaki bilgileri arayüze yazar_
- gui_receiver_db2.py <br> _Veritabanındaki bilgileri arayüze yazar - Türkçe_ 
- ser2udp.py <br> _Verici tarafı için Seri Porttan GNU Radio UDP Source için köprü oluşturur_ 
#### utils
- gui_receiver.py <br> _UDP’deki bilgileri arayüze yazar_ 
- listen_receiver.py <br> _UDP’deki bilgileri konsola yazar_ 
- udp2ser.py <br> _Alıcı tarafı için UDP Sink’ten servo kontrolü yapacak Arduino’ya veri akışı yapar_ 
## Program Akışı
- **Verici bilgisayarda GNU Radio ve udp2ser.py çalıştırılır.**
- **Alıcı bilgisayarda GNU Radio ardından;**
- UDP'den veri tabanına akış sağlayacak db.py,
- Veritabanı bilgisini okuyacak arayüz gui_receiver_db.py,
- Veritabanından alıcı Arduino için db2ser.py çalıştırılır.
