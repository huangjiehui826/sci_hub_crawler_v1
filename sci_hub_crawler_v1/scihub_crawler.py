# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
                               QStatusBar, QTextEdit, QVBoxLayout, QWidget)
from http import cookies
import requests
import pymysql
from dbutils.pooled_db import PooledDB
from bs4 import BeautifulSoup
import logging
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import queue
import io
import os
import time
import traceback
from PyPDF2 import PdfFileReader
from enum import Enum
import csv
os.environ['no_proxy'] = '*'
'''format=%(asctime)s具体时间 %(filename)s文件名 %(lenvelname)s日志等级 %(message)s具体信息
datemt=%a星期 %d日期 %b月份 %Y年份 %H:%M:%S时间'''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(669, 486)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 13, 661, 430))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_3)

        self.software_name = QLabel(self.layoutWidget)
        self.software_name.setObjectName(u"software_name")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(20)
        font.setBold(True)
        self.software_name.setFont(font)
        self.software_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.software_name)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.input_type_label = QLabel(self.layoutWidget)
        self.input_type_label.setObjectName(u"input_type_label")
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.input_type_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.input_type_label)

        self.input_type = QComboBox(self.layoutWidget)
        self.input_type.addItem("")
        self.input_type.addItem("")
        self.input_type.setObjectName(u"input_type")
        font2 = QFont()
        font2.setFamilies([u"\u5b8b\u4f53"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.input_type.setFont(font2)

        self.horizontalLayout_3.addWidget(self.input_type)

        self.input_text_path = QLabel(self.layoutWidget)
        self.input_text_path.setObjectName(u"input_text_path")
        self.input_text_path.setFont(font1)

        self.horizontalLayout_3.addWidget(self.input_text_path)

        self.input_text = QLineEdit(self.layoutWidget)
        self.input_text.setObjectName(u"input_text")

        self.horizontalLayout_3.addWidget(self.input_text)

        self.clean_button_input = QPushButton(self.layoutWidget)
        self.clean_button_input.setObjectName(u"clean_button_input")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.clean_button_input.setFont(font3)

        self.horizontalLayout_3.addWidget(self.clean_button_input)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_dict_label = QLabel(self.layoutWidget)
        self.input_dict_label.setObjectName(u"input_dict_label")
        self.input_dict_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.input_dict_label)

        self.input_save_path = QLineEdit(self.layoutWidget)
        self.input_save_path.setObjectName(u"input_save_path")

        self.horizontalLayout_2.addWidget(self.input_save_path)

        self.input_start_label = QLabel(self.layoutWidget)
        self.input_start_label.setObjectName(u"input_start_label")
        self.input_start_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.input_start_label)

        self.input_start_num = QLineEdit(self.layoutWidget)
        self.input_start_num.setObjectName(u"input_start_num")

        self.horizontalLayout_2.addWidget(self.input_start_num)

        self.clean_save_text = QPushButton(self.layoutWidget)
        self.clean_save_text.setObjectName(u"clean_save_text")
        self.clean_save_text.setFont(font3)

        self.horizontalLayout_2.addWidget(self.clean_save_text)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_mysql_label = QLabel(self.layoutWidget)
        self.input_mysql_label.setObjectName(u"input_mysql_label")
        self.input_mysql_label.setFont(font1)

        self.horizontalLayout.addWidget(self.input_mysql_label)

        self.input_mysql = QLineEdit(self.layoutWidget)
        self.input_mysql.setObjectName(u"input_mysql")

        self.horizontalLayout.addWidget(self.input_mysql)

        self.mysql_clean = QPushButton(self.layoutWidget)
        self.mysql_clean.setObjectName(u"mysql_clean")
        self.mysql_clean.setFont(font3)

        self.horizontalLayout.addWidget(self.mysql_clean)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.process_label = QLabel(self.layoutWidget)
        self.process_label.setObjectName(u"process_label")
        self.process_label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.process_label)

        self.output_text = QTextEdit(self.layoutWidget)
        self.output_text.setObjectName(u"output_text")
        font4 = QFont()
        font4.setFamilies([u"\u5b8b\u4f53"])
        self.output_text.setFont(font4)

        self.horizontalLayout_5.addWidget(self.output_text)

        self.clean_output_process = QPushButton(self.layoutWidget)
        self.clean_output_process.setObjectName(u"clean_output_process")
        self.clean_output_process.setFont(font3)

        self.horizontalLayout_5.addWidget(self.clean_output_process)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.download_link = QPushButton(self.layoutWidget)
        self.download_link.setObjectName(u"download_link")
        self.download_link.setFont(font1)

        self.horizontalLayout_11.addWidget(self.download_link)

        self.download_pdf = QPushButton(self.layoutWidget)
        self.download_pdf.setObjectName(u"download_pdf")
        self.download_pdf.setFont(font1)

        self.horizontalLayout_11.addWidget(self.download_pdf)

        self.output_database = QPushButton(self.layoutWidget)
        self.output_database.setObjectName(u"output_database")
        self.output_database.setFont(font1)

        self.horizontalLayout_11.addWidget(self.output_database)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.line_7 = QFrame(self.layoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_7)

        self.verticalSpacer_4 = QSpacerItem(18, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 669, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.software_name.setText(QCoreApplication.translate("MainWindow", u"Sci-Hub\u6587\u732e\u722c\u866b\u4e0b\u8f7d\u548c\u7ba1\u7406\u7cfb\u7edf", None))
        self.input_type_label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7c7b\u578b\uff1a", None))
        self.input_type.setItemText(0, QCoreApplication.translate("MainWindow", u"DOI", None))
        self.input_type.setItemText(1, QCoreApplication.translate("MainWindow", u"DOI\u5217\u8868", None))

        self.input_text_path.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u672c\u6216\u8def\u5f84\uff1a", None))
        self.clean_button_input.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.input_dict_label.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u6587\u4ef6\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.input_start_label.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u4e0b\u8f7d\u8d77\u59cb\u4f4d\u7f6e\uff1a", None))
        self.clean_save_text.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.input_mysql_label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165mysql\u8bbe\u7f6e\uff1a", None))
        self.mysql_clean.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.process_label.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u6267\u884c\u60c5\u51b5\uff1a", None))
        self.clean_output_process.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.download_link.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u4e0b\u8f7d\u94fe\u63a5", None))
        self.download_pdf.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7dPDF\u6587\u732e", None))
        self.output_database.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e\u5e93\u6587\u4ef6", None))
    # retranslateUi


class ThreadPoolExecutor(ThreadPoolExecutor):
    """
    重写线程池修改线程池大小
    """

    def __init__(self, max_workers=None, thread_name_prefix=''):
        super().__init__(max_workers, thread_name_prefix)
        # 队列大小为最大线程数的两倍
        self._work_queue = queue.Queue(self._max_workers * 2)


class SciHub:
    """
    封装了scihub链接下载和文件下载
    """

    def __init__(self, headers, cookies, host, user, port, password, db, user_input_type, user_input_content,
                 user_input_filepath, thread_workers=5, log_file="file_log", sci_url=None, strat_num=0) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                            datefmt='%a %d %b %Y %H:%M:%S', filename=log_file, filemode='w')
        self.db_pool = PooledDB(
            pymysql,
            maxconnections=10,
            host=host,
            user=user,
            port=port,
            passwd=password,
            db=db,
            use_unicode=True)
        self.start_num = strat_num
        self.headers = headers
        self.cookies = cookies
        # {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
        self.sci_url = sci_url
        self.user_input_type = user_input_type
        self.user_input_content = user_input_content
        self.thread_pool = ThreadPoolExecutor(max_workers=thread_workers)
        self.retry_ip_count = 0
        # self.download_path=r"D:\scihub\scihub_paper"
        # 修改下载的pdf文件目录
        self.download_path = user_input_filepath
        # D:\阿里云盘\scihub\scihub_paper1
        self.is_proxy = False
        # self.is_proxy=False
        self.proxies = self._set_proxy()

    def _read_dois_txt(slef, input_filepath) -> dict:
        """
        read need download dois txt and finished dois txt
        """
        need_download_list = []
        with open(input_filepath, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                need_download_list.append(line)
        return {
            "need_download_list": need_download_list
        }

    def _set_proxy(self):
        """
        set proxy for requests
        :param proxy_dict
        :return:
        """
        if self.is_proxy:
            # http://api.haiwaidaili.net/abroad?token=10023cb4d877b10c68c9481b8ed3c3fa&num=1&format=1&protocol=http&country=&state=&city=&sep=1&csep=&type=datacenter
            res = requests.get(
                url="http://api.haiwaidaili.net/abroad?token=60c0b0fe4ae0426b79b1d5c27bcba6fb&num=1&format=1&protocol=http&country=&state=&city=&sep=1&csep=&type=datacenter").text.strip()
            return {
                "http": "http://{}".format(res),
                "https": "http://{}".format(res),
            }
        else:
            return None

    def _get_soup(self, html):
        """
        return html soup
        """
        return BeautifulSoup(html, 'html.parser')

    def _get_pdf_link(self, doi: str) -> str:
        """
        from doi get pdf_link
        """
        # 带+的论文都无法下载
        if "+" in doi:
            return False

        try:
            res = requests.get(url=self.sci_url + '/' + doi, headers=self.headers, proxies=self._set_proxy(), timeout=5,
                               cookies=self.cookies)
            # print('----')
            # print(res.raw._connection.sock.getpeername())
            html = self._get_soup(res.text)
            res.close()
            frame = html.find('iframe') or html.find('embed')
            if frame:
                return self.sci_url + frame.get('src').split('#')[0] if not frame.get('src').startswith('//') \
                    else 'http:' + frame.get('src').split('#')[0]
            else:
                if "未找到文章" in str(html):
                    # print(html)
                    self._save_to_mysql("insert into scihub_paper (doi,is_exist_scihub) values ('%s','%s') " % (doi, 0))
                    print("可能是 Scihub 上没有收录该文章, 请直接访问上述页面看是否正常。")
                    logging.warning("Error: 可能是 Scihub 上没有收录该文章, 请直接访问上述页面看是否正常。")
                    return False
                print("可能被防火墙拦截了")
                print(doi)
                logging.error("可能被防火墙拦截了")
                return False
        except Exception as error:
            print(error)
            print("下载pdf链接错误,错误是%s" % error)
            logging.error("下载pdf链接错误,错误是%s" % error)
            return False

    def _get_pdf_file(self, pdf_link: str, id: int) -> bool:
        try:
            # 设置connect 6 read 18 stram 设置遍历落盘,通过二进制流落盘
            response = requests.get(url=pdf_link, headers=self.headers, proxies=self._set_proxy(), cookies=self.cookies,
                                    timeout=(6, 18))
            if self._isValidPDF_bytes(response.content) == False:
                print("pdf 文件网络加载错误")
                print("错误链接是%s" % pdf_link)
                logging.error("pdf 文件网络加载错误")
                return False

            bytes_io = io.BytesIO(response.content)  # 转换为字节流
            pdf_name = os.path.basename(pdf_link)  # get fileName
            with open("%s/%s" % (self.download_path, str(id) + "_" + pdf_name), 'wb') as file:
                # save local file
                file.write(bytes_io.getvalue())
                # file.write(response.content)

            # # 添加下载到本地以防万一
            # with open("%s/%s"%("c:/scihub/scihub_paper",str(id)+"_"+pdf_name),'wb') as file1:
            #     # save local file
            #     file1.write(bytes_io.getvalue())
            #     # file1.write(response.content)

            # 文件保存完成后关闭连接
            response.close()  # close connect

            return True
        except Exception as error:
            print("pdf 文件下载出现错误，错误是%s" % error)
            logging.error("pdf 文件下载出现错误，错误是%s" % error)
            return False

    # ！！！！！！ pdf开始下载的id位置
    def _download_pdf_files(self):
        """
        get links from dois
        """
        download_link_list = self._select_to_mysql(
            "select pdf_link,id from scihub_paper where is_download_file=0 and is_exist_scihub=1 and id>'%s' " % str(
                self.start_num))
        for item_link_tuple in download_link_list:
            self.thread_pool.submit(self._multithreading_download_files, item_link_tuple[0], item_link_tuple[1])
        time.sleep(60)

    def _download_pdf_links(self):
        """
        download file from pdf link
        """
        # get dois and finished_dois
        if self.user_input_type == 'DOI列表':
            resp = self._read_dois_txt(self.user_input_content)
        else:
            resp = {"need_download_list": [self.user_input_content]}
        # 排除源数据表有多个重复的情况

        need_download_list = list(set(resp["need_download_list"]))
        finished_list = [item[0] for item in self._select_to_mysql("select doi from scihub_paper")]
        # 进行是否需要下载进行判断,删除不需要下载的
        need_download_list = list(set(need_download_list) - set(finished_list))
        # for item_doi_tuplue in finished_list:
        #     if item_doi_tuplue[0] in need_download_list:
        #         # print(item_doi_tuplue[0])
        #         need_download_list.remove(item_doi_tuplue[0])
        #         # print(len(need_download_list))
        print("去重加载完成,还剩下%s需要下载" % len(need_download_list))
        # 遍历需要下载的数据
        for item_doi in need_download_list:
            self.thread_pool.submit(self._multithreading_download_links, item_doi)
        time.sleep(5)

    def _multithreading_download_links(self, doi: str) -> None:
        try:
            pdf_link = self._get_pdf_link(doi)
            if pdf_link:
                # 保存到数据库中
                self._save_to_mysql("insert into scihub_paper (doi,pdf_link) values ('%s','%s') " % (doi, pdf_link))
                print("pdf链接下载成功,下载的 doi是%s" % doi)
        except Exception as error:
            logging.error("下载doi %s 出错 错误原因是%s" % (doi, error))

    def _multithreading_download_files(self, pdf_link: str, id: int) -> None:
        try:
            if self._get_pdf_file(pdf_link, id):
                # 下载完成后更新数据库
                self._save_to_mysql("update scihub_paper set is_download_file=1,pdf_name='%s' where pdf_link='%s'"
                                    % (str(id) + "_" + os.path.basename(pdf_link), pdf_link))
                print("pdf文件下载成功,下载的链接是%s" % pdf_link)
        except Exception as error:
            logging.error("下载pdf文件出现错误,错误是%s" % error)

    def _save_to_mysql(self, sql: str) -> None:
        """
        save pdf link to mysql
        """
        try:
            # 创建游标
            con = self.db_pool.connection()
            cursor = con.cursor()
            # 执行插入
            cursor.execute(sql)
            # 执行事务提交
            con.commit()
            # 关闭游标和连接
            cursor.close()
            con.close()
        except Exception as error:
            logging.error("insert sql error is %s" % error)

    def _select_to_mysql(self, sql: str) -> list:
        """
        get pdf link from mysql
        """
        try:
            # 创建游标
            con = self.db_pool.connection()
            cursor = con.cursor()
            # 执行查询
            cursor.execute(sql)
            # 返回结果
            result = cursor.fetchall()
            # 关闭连接和游标
            cursor.close()
            con.close()
            return list(result)
        except Exception as error:
            logging.error("select sql error is %s" % error)
            return []

    def _isValidPDF_bytes(self, pdfBytes: bytes):
        bValid = True
        try:
            b = io.BytesIO(pdfBytes)
            reader = PdfFileReader(b, strict=False)
            if reader.getNumPages() < 1:  # 进一步通过页数判断。
                bValid = False
        except:
            bValid = False
            print('*' + traceback.format_exc())

        return bValid


def export_mysql_table(host, user, password, database, table_name, output_csv):
    # Create a connection pool
    pool = PooledDB(
        creator=pymysql,
        maxconnections=5,
        host=host,
        user=user,
        password=password,
        database=database,
        charset='utf8mb4'
    )

    # Get a connection from the pool
    connection = pool.connection()

    try:
        # Create a cursor
        cursor = connection.cursor()

        # Execute a query to fetch data from the table
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write header
            csv_writer.writerow([i[0] for i in cursor.description])

            # Write data
            csv_writer.writerows(rows)

        print(f"Data from table '{table_name}' exported to '{output_csv}' successfully.")
        return len(rows)
    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()


def count_rows_with_value(host, user, password, database, table_name, column_name, value):
    # Create a connection pool
    pool = PooledDB(
        creator=pymysql,
        maxconnections=5,
        host=host,
        user=user,
        password=password,
        database=database,
        charset='utf8mb4'
    )

    # Get a connection from the pool
    connection = pool.connection()

    try:
        # Create a cursor
        cursor = connection.cursor()

        # Execute a query to count rows with the specified value
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = %s"
        cursor.execute(query, (value,))

        # Fetch the result
        count = cursor.fetchone()[0]
        print(f"Number of rows with {column_name} equal to {value}: {count}")
        return count

    except Exception as e:
        print(f"Error: {e}")
        return 0

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()


def count_rows_with_value_download_pdf(host, user, password, database, table_name, column_name, value, start_num):
    # Create a connection pool
    pool = PooledDB(
        creator=pymysql,
        maxconnections=5,
        host=host,
        user=user,
        password=password,
        database=database,
        charset='utf8mb4'
    )

    # Get a connection from the pool
    connection = pool.connection()

    try:
        # Create a cursor
        cursor = connection.cursor()

        # Execute a query to count rows with the specified value
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = %s and id >= {str(start_num)}"
        cursor.execute(query, (value,))

        # Fetch the result
        count = cursor.fetchone()[0]
        print(f"Number of rows with {column_name} equal to {value}: {count}")
        return count

    except Exception as e:
        print(f"Error: {e}")
        return 0

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()


download_file_headers = {
    'authority': 'moscow.sci-hub.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '__ddgid_=xP7arvQKPReMzyey; __ddgmark_=Vazrxf4EZlXxYrOL; __ddg5_=7Imm21wHHQT5EvrX; __ddg2_=094CqmKk7ggWsBZy; __ddg1_=SyPfFcsCCTgUbTpJXSCn; session=0b09ab14b4a69dae2f737de0305161f8; refresh=1671852101.6222',
    'pragma': 'no-cache',
    'referer': 'https://sci-hub.ru/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'embed',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

download_file_cookies = None


download_link_headers = {
    'authority': 'sci-hub.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__ddg1_=I4qppHXKvu1WjyssWV0M; session=d286b1000780789b45fe873c5b7431fc; __ddgid_=dPI1hsR0LD9lB3OY; __ddgmark_=06Fbbxxa3QbNhR40; __ddg5_=gBxBrEB1H0aH2odz; __ddg2_=xT9Yne3xhkDPY3qS; refresh=1669739325.5533',
    'referer': 'https://www.sci-hub.se/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
download_link_cookies = {
      '__ddg1_': 'I4qppHXKvu1WjyssWV0M',
    'session': 'd286b1000780789b45fe873c5b7431fc',
    '__ddgid_': 'dPI1hsR0LD9lB3OY',
    '__ddgmark_': '06Fbbxxa3QbNhR40',
    '__ddg5_': 'gBxBrEB1H0aH2odz',
    '__ddg2_': 'xT9Yne3xhkDPY3qS',
    'refresh': '1669739325.5533',
    }


class DownloadFileConfig(Enum):
    headers = download_file_headers
    cookies = download_file_cookies
    log_file = "fileLog/downPdfFile.log"
    thread_workers = 1


class DownloadLinkConfig(Enum):
    headers = download_link_headers
    cookies = download_link_cookies
    # 'https://www.sci-hub.se'
    # sci_url='https://www.sci-hub.ru'
    sci_url = 'https://www.sci-hub.se'
    log_file = "fileLog/downPdfLink.log"
    thread_workers = 2


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.band()

    def band(self):
        self.ui.download_link.clicked.connect(self.download_link)
        self.ui.download_pdf.clicked.connect(self.download_pdf)
        self.ui.output_database.clicked.connect(self.output_database)
        self.ui.clean_button_input.clicked.connect(self.clean_button_input)
        self.ui.clean_output_process.clicked.connect(self.clean_output_process)
        self.ui.clean_save_text.clicked.connect(self.clean_save_text)

    def download_pdf(self):
        if self.ui.input_mysql.text() == '':
            host = '127.0.0.1'
            user = 'root'
            password = '123456'
            database = 'scihub_download'
            table_name = 'scihub_paper'
        else:
            get_mysql_list = self.ui.input_mysql.text().split('|')
            host = get_mysql_list[0]
            user = get_mysql_list[1]
            password = get_mysql_list[2]
            database = get_mysql_list[3]
            table_name = get_mysql_list[4]
        output_csv = 'output.csv'
        link_key = 'is_exist_scihub'
        pdf_key = 'is_download_file'
        value = 1
        start_num = self.ui.input_start_num.text()
        if start_num == '':
            start_num = 0
        user_input_type = self.ui.input_type.currentText()
        user_input_content = self.ui.input_text.text()
        user_input_filepath = self.ui.input_save_path.text()
        sciHub = SciHub(headers=DownloadLinkConfig.headers.value, cookies=DownloadLinkConfig.cookies.value,
                        sci_url=DownloadLinkConfig.sci_url.value, host=host,
                        user=user, port=3306,
                        password=password, db=database,
                        log_file=DownloadLinkConfig.log_file.value,
                        thread_workers=DownloadLinkConfig.thread_workers.value,
                        strat_num=start_num, user_input_type=user_input_type,
                        user_input_content=user_input_content, user_input_filepath=user_input_filepath)

        sciHub._download_pdf_files()
        get_pdf_count = count_rows_with_value_download_pdf(host, user, password, database, table_name, pdf_key,
                                                           value, start_num)
        output_text = f"""已获取到PDF文件{str(get_pdf_count)}, 文件保存路径为{user_input_filepath}"""
        self.ui.output_text.setText(output_text)

    def download_link(self):
        if self.ui.input_mysql.text() == '':
            host = '127.0.0.1'
            user = 'root'
            password = '123456'
            database = 'scihub_download'
            table_name = 'scihub_paper'
        else:
            get_mysql_list = self.ui.input_mysql.text().split('|')
            host = get_mysql_list[0]
            user = get_mysql_list[1]
            password = get_mysql_list[2]
            database = get_mysql_list[3]
            table_name = get_mysql_list[4]
        output_csv = 'output.csv'
        link_key = 'is_exist_scihub'
        pdf_key = 'is_download_file'
        user_input_content = self.ui.input_text.text()
        user_input_type = self.ui.input_type.currentText()
        value = 1
        start_num = self.ui.input_start_num.text()
        if start_num == '':
            start_num = 0
        get_link_count_start = count_rows_with_value(host, user, password, database, table_name, link_key, value)
        sciHub = SciHub(headers=DownloadLinkConfig.headers.value, cookies=DownloadLinkConfig.cookies.value,
                        sci_url=DownloadLinkConfig.sci_url.value, host=host,
                        user=user, port=3306,
                        password=password, db=database,
                        log_file=DownloadLinkConfig.log_file.value,
                        thread_workers=DownloadLinkConfig.thread_workers.value, strat_num=start_num,
                        user_input_type=user_input_type, user_input_content=user_input_content, user_input_filepath='')
        sciHub._download_pdf_links()
        get_link_count = count_rows_with_value(host, user, password, database, table_name, link_key, value)
        output_text = f"""已获取到文献链接{str(get_link_count)}，新获取{str(get_link_count-get_link_count_start)}个文献链接"""
        self.ui.output_text.setText(output_text)

    def clean_button_input(self):
        self.ui.input_text.setText('')

    def clean_output_process(self):
        self.ui.output_text.setText('')

    def clean_save_text(self):
        self.ui.clean_save_text.setText('')

    def output_database(self):
        if self.ui.input_mysql.text() == '':
            host = '127.0.0.1'
            user = 'root'
            password = '123456'
            database = 'scihub_download'
            table_name = 'scihub_paper'
        else:
            get_mysql_list = self.ui.input_mysql.text().split('|')
            host = get_mysql_list[0]
            user = get_mysql_list[1]
            password = get_mysql_list[2]
            database = get_mysql_list[3]
            table_name = get_mysql_list[4]
        output_csv = 'output.csv'
        link_key = 'is_exist_scihub'
        pdf_key = 'is_download_file'
        value = 1
        start_num = self.ui.input_start_num.text()
        if start_num == '':
            start_num = 0
        get_count = export_mysql_table(host, user, password, database, table_name, output_csv)
        if get_count:
            current_path = os.getcwd()
            get_save_path = os.path.join(current_path, 'output.csv')
            get_link_count = count_rows_with_value(host, user, password, database, table_name, link_key, value)
            get_pdf_count = count_rows_with_value_download_pdf(host, user, password, database, table_name, pdf_key,
                                                               value, start_num)
            output_text = f"""已导出{str(get_count)}行数数据,文件保存在{get_save_path}\n已获取到文献链接{str(get_link_count)}\t已获取到PDF文件{str(get_pdf_count)}"""
            self.ui.output_text.setText(output_text)
        else:
            self.ui.output_text.setText('导出文件失败，请检查代码和mysql数据设置是否正确')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
