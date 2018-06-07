# !/usr/bin/env python
# -*- coding:utf-8 -*-

import csv

from tkinter import *

import os

write_one_col_way = 1
"""
    if (write_one_col_way == 1)
        we set one row str to a list, and then append this list to the final result str list
    else if (write_one_col_way == 2)
        we use a fixed str, each set with default value None. Then fill the value into list.  
"""

result_str = []


def clear_csv_data_buf():
    result_str.clear()


def read_color_resut(color_file_list):
    # awb_err = []
    SNR_result = []
    exposure_err = []
    noise_result = [[], [], [], []]
    # currently we can handle 4 color files at most, ie, 4 rows of noise result at most
    color_sat = []
    color_delta_c_mean_corr = []
    color_delta_c_max_corr = []
    color_delta_c_mean_uncorr = []
    color_delta_c_max_uncorr = []
    color_delta_e_mean_uncorr = []
    color_delta_e_max_uncorr = []

    # ten_space = ' ' * 10  # used for output format
    awb_err_fmt_5 = []
    awb_err_fmt_6 = []
    awb_err_fmt_7 = []
    awb_err_fmt_8 = []
    awb_err_fmt_9 = []
    awb_err_fmt_10 = []

    file_name_del_ext = [None, None, None, None]

    flag_add_for_left_title = True  # used to judge whether we are processing the first file and adding title

    for i, color_file in enumerate(color_file_list):
        if (color_file is None) or (os.path.splitext(color_file)[1] != '.csv'):
            continue

        # print("os.path.splitext(color_file)[0] = %s , os.path.splitext(color_file)[1] = %s" %
        #      (os.path.splitext(color_file)[0], os.path.splitext(color_file)[1]))
        # if color_file is None:
        #    continue
        else:
            print('color file : ' + color_file)
            file_path_without_ext = os.path.splitext(color_file)[0]
            file_name = os.path.split(file_path_without_ext)[1]
            print('color file without extension is  : ' + file_name)

            file_name_del_ext.append("")

            with open(color_file, mode='r', newline='') as fd_read_color_csv:
                reader = csv.reader(fd_read_color_csv)
                row_sel = 0

                print("in file %s " % color_file)

                for row in reader:
                    """
                    if (row_sel >= 5 and row_sel <= 10):
                        print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                        #result_str.append(([row[9]]))
                        if(row_sel == 7):
                            #awb_err_fmt_item.append('awb_err   ')
                            #awb_err_fmt_item.append(row[9].strip())
                            awb_err.append(['awb_err   '])
                            awb_err.append([row[9].strip()])
                        else:
                            #awb_err_fmt_item.append(ten_space)
                            #awb_err_fmt_item.append(row[9].strip())
                            #awb_err.append([awb_err_fmt_item])
                            awb_err.append([ten_space])
                            awb_err.append([row[9].strip()])
                    """

                    if (row_sel == 5):
                        # awb_err_fmt_item.append('awb_err   ')
                        # awb_err_fmt_item.append(row[9].strip())
                        print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                        print("flag_add_for_left_title = %d" % flag_add_for_left_title)
                        if flag_add_for_left_title:
                            print('Line %03d, column %02d :  Add item title to left' % (row_sel, 9))
                            awb_err_fmt_5.append('awb error result')
                        awb_err_fmt_5.append(row[9].strip())
                        # awb_err.append([awb_err_fmt_5])

                    if (row_sel == 6):
                        # awb_err_fmt_item.append('awb_err   ')
                        # awb_err_fmt_item.append(row[9].strip())
                        print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                        if flag_add_for_left_title:
                            awb_err_fmt_6.append('awb error result')
                        awb_err_fmt_6.append(row[9].strip())
                        # awb_err.append([awb_err_fmt_5])

                    if (row_sel == 7):
                        # awb_err_fmt_item.append('awb_err   ')
                        # awb_err_fmt_item.append(row[9].strip())
                        print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                        if flag_add_for_left_title:
                            awb_err_fmt_7.append('awb error result')
                        awb_err_fmt_7.append(row[9].strip())
                        # awb_err.append([awb_err_fmt_5])

                    if (row_sel == 8):
                        # awb_err_fmt_item.append('awb_err   ')
                        # awb_err_fmt_item.append(row[9].strip())
                        print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                        if flag_add_for_left_title:
                            awb_err_fmt_8.append('awb error result')
                        awb_err_fmt_8.append(row[9].strip())
                        # awb_err.append([awb_err_fmt_5])

                    if (row_sel == 9):
                        # awb_err_fmt_item.append('awb_err   ')
                        # awb_err_fmt_item.append(row[9].strip())
                        print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                        if flag_add_for_left_title:
                            awb_err_fmt_9.append('awb error result')
                        awb_err_fmt_9.append(row[9].strip())
                        # awb_err.append([awb_err_fmt_5])

                    if (row_sel == 10):
                        # awb_err_fmt_item.append('awb_err   ')
                        # awb_err_fmt_item.append(row[9].strip())
                        print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                        if flag_add_for_left_title:
                            awb_err_fmt_10.append('awb error result')
                        awb_err_fmt_10.append(row[9].strip())
                        # awb_err.append([awb_err_fmt_5])

                    if (row_sel == 49):
                        print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                        # result_str.append(([row[9]]))
                        if flag_add_for_left_title:
                            SNR_result.append('SNR result: ')
                        SNR_result.append(row[1].strip())

                    if (row_sel == 133):
                        print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                        # result_str.append(([row[9]]))
                        if flag_add_for_left_title:
                            exposure_err.append('exposure_error')
                        exposure_err.append(row[1].strip())

                    if (row_sel == 135):
                        print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                        # result_str.append(([row[9]]))
                        left_title = [""]
                        not_used_str = "_summary"
                        if file_name is not None:
                            index = file_name.rfind(not_used_str)
                            if (index == -1):
                                noise_result[i].append('Avg_noise : ' + file_name)
                            else:
                                noise_result[i].append('Avg_noise : ' + file_name[:index])

                        noise_result[i].append(row[1].strip())
                        noise_result[i].append(row[2].strip())
                        noise_result[i].append(row[3].strip())
                        noise_result[i].append(row[4].strip())
                    if (row_sel == 136):
                        print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                        # result_str.append(([row[9]]))
                        if flag_add_for_left_title:
                            color_sat.append('Saturation')
                        color_sat.append(row[1].strip())

                    if (row_sel == 137):
                        print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                        # result_str.append(([row[9]]))
                        if flag_add_for_left_title:
                            color_delta_c_mean_corr.append('Delta-C mean corr')
                        color_delta_c_mean_corr.append(row[1].strip())

                    if (row_sel == 139):
                        print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                        # result_str.append(([row[9]]))
                        if flag_add_for_left_title:
                            color_delta_c_max_corr.append('Delta-C max corr')
                        color_delta_c_max_corr.append(row[1].strip())

                    if (row_sel == 140):
                        print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                        # result_str.append(([row[9]]))
                        if flag_add_for_left_title:
                            color_delta_c_mean_uncorr.append('Delta-C mean uncorr')
                        color_delta_c_mean_uncorr.append(row[1].strip())

                    if (row_sel == 142):
                        print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                        # result_str.append(([row[9]]))
                        if flag_add_for_left_title:
                            color_delta_c_max_uncorr.append('Delta-C max uncorr')
                        color_delta_c_max_uncorr.append(row[1].strip())

                    if (row_sel == 143):
                        print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                        # result_str.append(([row[9]]))
                        if flag_add_for_left_title:
                            color_delta_e_mean_uncorr.append('Delta-E mean uncorr')
                        color_delta_e_mean_uncorr.append(row[1].strip())

                    if (row_sel == 145):
                        print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                        # result_str.append(([row[9]]))
                        if flag_add_for_left_title:
                            color_delta_e_max_uncorr.append('Delta-E max uncorr')
                        color_delta_e_max_uncorr.append(row[1].strip())
                        break

                    row_sel = row_sel + 1

                file_name_del_ext[i] = file_name

            flag_add_for_left_title = False
            # print(row)

    # result_str.append(awb_err)
    # result_str.extend(awb_err)

    """ Indicates that no file is read.
        We may need to check whether file_name_del_ext list is 
        filled with None as well
    """
    print(" Add for debug ")
    if flag_add_for_left_title:
        return

    """
    add top title
    
    we will remove '_summary' string in file name
    
    """

    top_file_title = [""]
    not_used_str = "_summary"
    for name in file_name_del_ext:
        if name is not None:
            index = name.rfind(not_used_str)
            if(index == -1):
                top_file_title.append(name)
            else:
                top_file_title.append(name[:index])
    result_str.append(top_file_title)
    result_str.append([])

    result_str.append(awb_err_fmt_5)
    result_str.append(awb_err_fmt_6)
    result_str.append(awb_err_fmt_7)
    result_str.append(awb_err_fmt_8)
    result_str.append(awb_err_fmt_9)
    result_str.append(awb_err_fmt_10)
    result_str.append([])

    # add top title
    result_str.append(top_file_title)
    result_str.append([])

    result_str.append(SNR_result)
    result_str.append([])

    # add top title
    result_str.append(top_file_title)
    result_str.append([])
    result_str.append(exposure_err)
    result_str.append([])

    # add top title for noise
    noise_top_title = ["", "R", "G", "B", "Y"]
    result_str.append(noise_top_title)
    result_str.append([])
    # highlight : should use extend, not append
    result_str.extend(noise_result)
    result_str.append([])

    # add top title
    # add top title
    result_str.append(top_file_title)
    result_str.append([])
    result_str.append(color_sat)
    result_str.append(color_delta_c_mean_corr)
    result_str.append(color_delta_c_max_corr)
    result_str.append(color_delta_c_mean_uncorr)
    result_str.append(color_delta_e_max_uncorr)
    result_str.append(color_delta_e_mean_uncorr)
    result_str.append(color_delta_e_max_uncorr)
    result_str.append([])


def read_shading_result(shading_file_list):
    """
    lens_shading = [None, None, None, None]
    for i, shading_file in enumerate(color_file_list):
        if (shading_file is None) or (os.path.splitext(color_file)[1] != '.csv'):
            continue

    """
    if shading_file_list[0] is None:
        return

    print("process shading file : " + shading_file_list[0])
    with open(shading_file_list[0], mode='r', newline='') as fd_read_shading_csv:
        shading_result_reader = csv.reader(fd_read_shading_csv)

        row_sel = 0
        lens_shading = ['lens_shading mean']

        for row in shading_result_reader:
            if (row_sel == 15):
                print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                # result_str.append(([row[9]]))
                lens_shading.append(row[1].strip() + '%')
            if (row_sel == 33):
                print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                lens_shading.append(('%.1f' % (float(row[1].strip()) * 100)) + '%')
                break
            row_sel = row_sel + 1

    # add top title for shading result
    shading_result_top_title = ["", "Lens Shading", "Color Shading"]
    result_str.append(shading_result_top_title)
    result_str.append([])
    result_str.append(lens_shading)
    result_str.append([])


def read_stepchart_result(stepchart_file_list):
    if stepchart_file_list[0] is None:
        return

    print("process step chart file : " + stepchart_file_list[0])
    with open(stepchart_file_list[0], mode='r', newline='') as fd_read_stepchart_csv:
        stepchart_result_reader = csv.reader(fd_read_stepchart_csv)

        one_step = 8.0
        row_sel = 0
        stepchart_result_str = []
        stepchart_list = []

        stepchart_result_str.append('stepchart ( num, max, min, range )')

        for row in stepchart_result_reader:
            if (row_sel >= 8 and row_sel <= 25):
                print('Line %03d, column %02d :  %s' % (row_sel, 1, ('%.1f' % float(row[1].strip()))))
                # result_str.append(([row[9]]))
                stepchart_list.append(float(row[1].strip()))
                # stepchart_list.append(float('%.1f' % float(row[1].strip())))  # same as above , useless
            row_sel = row_sel + 1

    step_num = 1

    max_lumi = max(stepchart_list)
    min_lumi = min(stepchart_list)
    lumi_range = max_lumi - min_lumi

    for i in range(0, len(stepchart_list) - 1):
        print('stepchart list %02d : %f' % (i, stepchart_list[i]))
        if (stepchart_list[i] - stepchart_list[i + 1] >= one_step):
            step_num = step_num + 1

    stepchart_result_str.append(max_lumi)
    stepchart_result_str.append(min_lumi)
    stepchart_result_str.append(lumi_range)
    stepchart_result_str.append(step_num)

    # add top title for step chart result
    step_chart_title = ["", "Max", "Min", "Range", "Step num"]
    result_str.append(step_chart_title)
    result_str.append([])
    result_str.append(stepchart_result_str)
    result_str.append([])


def decide_file_save_path(color_file_list, step_file_list, shading_file_list):
    print("decide file save path (last added file) ")

    temp_path = None

    if shading_file_list[0] is not None:
        temp_path = shading_file_list[0]
    elif step_file_list[0] is not None:
        temp_path = step_file_list[0]
    else:
        i = 3
        while i >= 0:
            if color_file_list[i] is not None:
                temp_path = color_file_list[i]
                break
            i = i - 1

    """ Add only for debug
        if temp_path is None:
            print(" No file is selected to process, do nothing")
        else:
            print(" file save path is " + temp_path)

    return os.path.join(os.path.split(temp_path)[0], "result.csv")
    
    r"C:/Users/linchao/.spyder/Normal-Cap-SNR/Results \ result.csv"
    
    we expect it output "C:/Users/linchao/.spyder/Normal-Cap-SNR/Results/result.csv",
    however, it outputs strange path
    
    """

    if temp_path is None:
        return None
    else:
        return os.path.split(temp_path)[0] + r"/" + "result.csv"


def write_result_csv(file_path):
    print("Save result to file result.csv to the last added file path on UI")

    if file_path is None:
        print(" No file is selected to process, do nothing")
    else:
        print("file will be saved under path: " + file_path)
        print("check abs path call : " + os.path.abspath(file_path))
        file_path_title = ["result file : ", os.path.abspath(file_path)]

        with open(file_path, mode='w', newline='') as fd_write_result_csv:
            writer = csv.writer(fd_write_result_csv)
            writer.writerow(file_path_title)
            writer.writerow([])  # add blank line to sep different content
            writer.writerows(result_str)

        """
        If we use os.path.join, we will get path with double slash . 
        To use 'join' function of string , or connector "+" may be a good solution
        """
        last_path_config = os.getcwd() + os.path.sep + "last_data_path.txt"
        print("check default config file path :　%s " % last_path_config)
        with open(last_path_config, mode="w") as fd_last_path:
            print("write last work dir to config file last_data_path.txt ")
            print("last work dir =   " + os.path.split(os.path.abspath(file_path))[0])
            print("try os dir name  =  " + os.path.dirname(file_path))
            fd_last_path.write(os.path.split(file_path)[0])

def tkinter_gui_start():
    init_window = Tk()
    init_window.title("客观测试csv文件数据处理工具")
    init_window.geometry('720x480+600+320')  # 290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
    # init_window["bg"] = "pink"                 #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
    # init_window.attributes("-alpha", 0.8)       #虚化 值越小虚化程度越高，设置为100为非透明
    init_window.mainloop()


if __name__ == "__main__":
    tkinter_gui_start()
    color_file_path = [
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\D65-Cap_summary.csv',
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\CWF-Cap_summary.csv',
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\TL84-Cap_summary.csv',
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\A-Cap_summary.csv']

    step_file_path = [
        r'C:\Users\linchao\.spyder\Grayscale\Results\flare_104_summary.csv', None]
    shading_file_path = [
        r'C:\Users\linchao\.spyder\Shading-Setting-0.8-Ratio-32\Results\DNP-Normal-Cap-Ratio-32_LF_Y.csv', None]

    read_color_resut(color_file_path)
    read_shading_result(shading_file_path)
    read_stepchart_result(step_file_path)

    file_save_path = decide_file_save_path(color_file_path, step_file_path, shading_file_path)
    write_result_csv(file_save_path)
