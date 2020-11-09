# Designing an end-to-end communication channel for servo control
### Dosya Hiyerarşisi
-> bpsk_servo_control_vFinal
	->arduino
		receiver ve transmitter Arduino .ino dosyalarını barındırır
	->share
		db.py 
		(GNU Radio alıcı tarafında UDP’ye bağlanarak yaratılan udp_sink.db’ye veri akışı yapar)
		db2ser.py
		(Veritabanından Seri Porta veri akışı yapar)
		gui_receiver_db.py
		(Veritabanındaki bilgileri arayüze yazar)
		gui_receiver_db2.py
		(Veritabanındaki bilgileri arayüze yazar - Türkçe)
		ser2udp.py
		(Verici tarafı için Seri Porttan GNU Radio UDP Source için köprü oluşturur)
	->utils
		gui_receiver.py
		(UDP’deki bilgileri arayüze yazar)
		listen_receiver.py
		(UDP’deki bilgileri konsola yazar)
		udp2ser.py
		(Alıcı tarafı için UDP Sink’ten servo kontrolü yapacak Arduino’ya veri akışı yapar)

### Program Akışı
->Verici bilgisayarda GNU Radio ve udp2ser.py çalıştırılır.	
->Alıcı bilgisayarda GNU Radio ardından;
UDP’den veri tabanına akış sağlayacak db.py,
Veritabanı bilgisini okuyacak arayüz gui_receiver_db.py,
Veritabanından alıcı Arduino için db2ser.py çalıştırılır.
	
