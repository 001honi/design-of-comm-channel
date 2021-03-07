#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BPSK 2 Parametre
# Description: 2 parametreyi UDP'den BPSK ile iletir; yine UDP'ye yonlendirir
# GNU Radio version: 3.7.13.5
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import limesdr
import sip
import sys
from gnuradio import qtgui


class bpsk_servo_kontrol_vFinal(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BPSK 2 Parametre")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BPSK 2 Parametre")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "bpsk_servo_kontrol_vFinal")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 15
        self.nfilts = nfilts = 180
        self.samp_rate = samp_rate = 100e3
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 45*nfilts)
        self.payload = payload = 21
        self.interpolation = interpolation = 20
        self.baseband_LO = baseband_LO = 20e3
        self.access_code = access_code = '010110011011101100010101011111101001001110001011010001101010001'

        self.BPSK = BPSK = digital.constellation_bpsk().base()


        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=interpolation,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 10e3, 1.6E3, firdes.WIN_HAMMING, 6.76))
        self.limesdr_source_0 = limesdr.source('', 1, '')
        self.limesdr_source_0.set_sample_rate(samp_rate*interpolation)
        self.limesdr_source_0.set_center_freq(850e6, 0)
        self.limesdr_source_0.set_bandwidth(5e6,1)
        self.limesdr_source_0.set_gain(30,1)
        self.limesdr_source_0.set_antenna(2,1)
        self.limesdr_source_0.calibrate(5e6, 1)

        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, .062, (rrc_taps), nfilts, nfilts/2, 1.5, 2)
        self.digital_lms_dd_equalizer_cc_0 = digital.lms_dd_equalizer_cc(8, .01, 2, BPSK)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(0.0628, 2, False)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(BPSK)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(1)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, '127.0.0.1', 5006, payload, False)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code='',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -baseband_LO, 0.5, 0)
        self.analog_feedforward_agc_cc_0 = analog.feedforward_agc_cc(1024, 1.55)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_feedforward_agc_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_lms_dd_equalizer_cc_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.limesdr_source_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_feedforward_agc_cc_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_xx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "bpsk_servo_kontrol_vFinal")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 45*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 45*self.nfilts))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 10e3, 1.6E3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload

    def get_interpolation(self):
        return self.interpolation

    def set_interpolation(self, interpolation):
        self.interpolation = interpolation

    def get_baseband_LO(self):
        return self.baseband_LO

    def set_baseband_LO(self, baseband_LO):
        self.baseband_LO = baseband_LO
        self.analog_sig_source_x_0_0.set_frequency(-self.baseband_LO)

    def get_access_code(self):
        return self.access_code

    def set_access_code(self, access_code):
        self.access_code = access_code

    def get_BPSK(self):
        return self.BPSK

    def set_BPSK(self, BPSK):
        self.BPSK = BPSK


def main(top_block_cls=bpsk_servo_kontrol_vFinal, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
