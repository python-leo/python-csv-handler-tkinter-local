#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 05, 2018 12:31:24 PM


import csv
import pandas as pd

import sys
from PyQt5 import QtWidgets

if __name__ == "__main__":
    color_file_path = [
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\test_panda.csv',
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\D65-Cap_summary.csv',
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\CWF-Cap_summary.csv',
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\TL84-Cap_summary.csv',
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\A-Cap_summary.csv']

    step_file_path = [
        r'C:\Users\linchao\.spyder\Grayscale\Results\flare_104_summary.csv', None]
    shading_file_path = [
        r'C:\Users\linchao\.spyder\Shading-Setting-0.8-Ratio-32\Results\DNP-Normal-Cap-Ratio-32_LF_Y.csv', None]

    d = pd.read_csv(color_file_path[0], usecols=['Zone', 'Gray', 'Pixel', 'WB ERR S(HSV)'],
                    nrows=5, skiprows=[1, 3])

    print(d)

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    widget.resize(360, 360)
    widget.setWindowTitle("Hello, PyQt5!")
    widget.show()
    sys.exit(app.exec_())
