# Designing an end-to-end communication channel for servo control
### Dosya Hiyerarşisi
-\> bpsk\_servo\_control\_vFinal -\>arduino receiver ve transmitter
Arduino .ino dosyalarını barındırır -\>share db.py (GNU Radio alıcı
tarafında UDP’ye bağlanarak yaratılan udp\_sink.db’ye veri akışı yapar)
db2ser.py (Veritabanından Seri Porta veri akışı yapar)
gui\_receiver\_db.py (Veritabanındaki bilgileri arayüze yazar)
gui\_receiver\_db2.py (Veritabanındaki bilgileri arayüze yazar - Türkçe)
ser2udp.py (Verici tarafı için Seri Porttan GNU Radio UDP Source için
köprü oluşturur) -\>utils gui\_receiver.py (UDP’deki bilgileri arayüze
yazar) listen\_receiver.py (UDP’deki bilgileri konsola yazar) udp2ser.py
(Alıcı tarafı için UDP Sink’ten servo kontrolü yapacak Arduino’ya veri
akışı yapar)

### Program Akışı
<div style="margin-top:0pt;margin-bottom:0pt;margin-left:.63in;text-indent:-.63in;text-align:left;"><span style="font-size: 26px; font-family: Candara; color: black;">Verici bilgisayarda GNU&nbsp;</span><span style="font-size: 26px;"><span style="font-family: Candara; color: black;">Radio&nbsp;ve udp2ser.py &ccedil;alıştırılır. &nbsp;</span></span></div>
<div style="margin-top:0pt;margin-bottom:0pt;margin-left:.63in;text-indent:-.63in;text-align:left;"><span style="font-size: 26px;"><span style="font-family:Arial;">&bull;</span><span style="font-family: Candara; color: black;">Alıcı bilgisayarda GNU&nbsp;Radio&nbsp;ardından;</span></span></div>
<div style="margin-top:0pt;margin-bottom:0pt;margin-left:1.13in;text-indent:-.63in;text-align:left;"><span style="font-size: 26px;"><span style="font-family:Arial;">&bull;</span><span style="font-family: Candara; color: black;">UDP&rsquo;den&nbsp;veri tabanına akış sağlayacak db.py,</span></span></div>
<div style="margin-top:0pt;margin-bottom:0pt;margin-left:1.13in;text-indent:-.63in;text-align:left;"><span style="font-size: 26px;"><span style="font-family:Arial;">&bull;</span><span style="font-family: Candara; color: black;">Veritabanı&nbsp;bilgisini okuyacak&nbsp;aray&uuml;z&nbsp;gui_receiver_db.py,</span></span></div>
<div style="margin-top:0pt;margin-bottom:0pt;margin-left:1.13in;text-indent:-.63in;text-align:left;"><span style="font-size: 26px;"><span style="font-family:Arial;">&bull;</span><span style="font-family: Candara; color: black;">Veritabanından&nbsp;alıcı&nbsp;Arduino&nbsp;i&ccedil;in db2ser.py &ccedil;alıştırılır.</span></span></div>
<p style="margin-top:0pt;margin-bottom:0pt;margin-left:.5in;text-align:left;"><span style="font-size: 26px; font-family: Candara; color: black;">&nbsp; </span></p>
	
