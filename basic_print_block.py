"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block

    def __init__(self):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='Basic Print Block',   # will show up in GRC
            in_sig=[np.byte],
            out_sig=[np.byte]
        )


    def work(self, input_items, output_items):
        output_items[0] = input_items[0]
        print input_items[0], len(input_items[0])

        return len(output_items[0])
