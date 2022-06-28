from GUI import *
from function import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTreeWidgetItem
from PyQt5.QtCore import QDate, QTime, Qt
from PyQt5 import QtCore
import sys
import MySQLdb

class MainWindow(QMainWindow, Ui_MainWindow):
	# 初始化类
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)
		self.setWindowTitle('银行业务系统-----PB19071535徐昊天')
		self.clicked()
		self.command = ""
		self.g_infer = ""
		self.l_infer = ""
		self.op = [' = ', ' != ', ' > ', ' < ', ' >= ', ' <= ']
		self.comboBox_1.setCurrentIndex(0)
		self.comboBox_2.setCurrentIndex(0)
		self.comboBox_3.setCurrentIndex(0)
	def clicked(self):
		# 客户管理
		self.pushButton_1.clicked.connect(self.insert_client)
		self.pushButton_2.clicked.connect(self.delete_client)
		self.pushButton_3.clicked.connect(self.modify_client)
		self.pushButton_4.clicked.connect(self.inquire_client)
		self.pushButton_5.clicked.connect(self.empty_client)
		self.treeWidget_1.itemDoubleClicked.connect(self.doubleclicked_client)
		# 账户管理
		self.pushButton_6.clicked.connect(self.insert_account)
		self.pushButton_7.clicked.connect(self.delete_account)
		self.pushButton_8.clicked.connect(self.modify_account)
		self.pushButton_9.clicked.connect(self.inquire_account)
		self.pushButton_10.clicked.connect(self.empty_account)
		self.treeWidget_2.itemDoubleClicked.connect(self.doubleclicked_account)
		# 贷款管理
		self.pushButton_11.clicked.connect(self.insert_loan)
		self.pushButton_12.clicked.connect(self.delete_loan)
		self.pushButton_13.clicked.connect(self.inquire_loan)
		self.pushButton_14.clicked.connect(self.issue_loan)
		self.pushButton_15.clicked.connect(self.empty_loan)
		self.treeWidget_3.itemDoubleClicked.connect(self.doubleclicked_loan)
		# 业务统计
		self.pushButton_16.clicked.connect(self.saving_statistic)
		self.pushButton_17.clicked.connect(self.loan_statistic)
		self.pushButton_18.clicked.connect(self.empty_statistic)

	def execute(self, return_data):
		global db
		result = []
		print(self.command)
		if status == 0:
			cursor = db.cursor()
			try:
				cursor.execute(self.command)
			except Exception as e:
				print(e)
				QMessageBox.warning(self, '警告', 'SQL执行错误')
				return False
			if return_data:
				result = cursor.fetchall()
			else:
				result = True
			db.commit()
			cursor.close()
		self.g_infer = ''
		return result

	#客户管理

	#增加客户
	def insert_client(self):
		if self.lineEdit_0.text() == '' or self.lineEdit_1.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' or self.lineEdit_4.text() == '' or self.lineEdit_5.text() == '' or self.lineEdit_6.text() == '' or self.lineEdit_7.text() == '' or self.lineEdit_8.text() == '' or self.lineEdit_9.text() == '':
			QMessageBox.warning(self, '警告', '请输入完整信息!')
			return
		if self.lineEdit_1.text().find('‘') != -1 or self.lineEdit_1.text().find('’') != -1:
			QMessageBox.warning(self, '警告', '客户姓名中不可带单引号!')
			return
		if self.lineEdit_6.text().find('@') == -1:
			QMessageBox.warning(self, '警告', '请输入正确的邮箱地址!')
			return
		sure = QMessageBox.question(self, '确认', "确定增加客户?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if sure == QMessageBox.No:
			return
		self.command = 'insert into 客户(客户姓名, 客户联系电话, 客户家庭住址, 客户身份证号, 联系人姓名, 联系人手机号, 联系人Email, 联系人关系, 员工身份证号, 负责人类型) Values(' + add_qmark(self.lineEdit_1.text()) + ', '+ add_qmark(self.lineEdit_4.text()) + ', '+ add_qmark(self.lineEdit_3.text()) + ', '+ add_qmark(self.lineEdit_2.text())  + ', '+ add_qmark(self.lineEdit_5.text()) +  ', '+ add_qmark(self.lineEdit_8.text()) + ', '+ add_qmark(self.lineEdit_6.text()) + ', '+ add_qmark(self.lineEdit_7.text()) + ', '+ add_qmark(self.lineEdit_9.text()) + ',' + add_qmark(self.lineEdit_0.text()) + ')'
		if self.execute(False):
			QMessageBox.information(self, '信息', '客户添加成功!')
		else:
			QMessageBox.warning(self, '警告', '该客户已经存在!')

	# 删除客户
	def delete_client(self):
		if self.lineEdit_2.text() == '':
			QMessageBox.warning(self, '警告', '请选择待删除的客户！')
			return
		self.inquire_client()
		sure = QMessageBox.question(self, '确认', "确定删除客户?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if sure == QMessageBox.No:
			return
		self.command = 'delete from 客户 where ' + get_equation('客户姓名', self.lineEdit_1.text()) + ' and ' + get_equation('客户联系电话', self.lineEdit_4.text()) + ' and ' + get_equation('客户家庭住址', self.lineEdit_3.text()) + ' and ' + get_equation('客户身份证号', self.lineEdit_2.text()) + ' and ' + get_equation('联系人姓名', self.lineEdit_5.text()) + ' and ' + get_equation('联系人手机号', self.lineEdit_8.text()) + ' and ' + get_equation('联系人Email', self.lineEdit_6.text()) + ' and ' + get_equation('联系人关系', self.lineEdit_7.text()) + ' and ' + get_equation('员工身份证号', self.lineEdit_9.text()) + ' and ' + get_equation('负责人类型', self.lineEdit_0.text())
		if self.execute(False):
			QMessageBox.information(self, '信息', '客户删除成功!')
		else:
			QMessageBox.warning(self, '警告', '客户存在关联账户或者贷款记录')
		self.treeWidget_1.clear()

	# 修改客户
	def modify_client(self):
		if self.lineEdit_0.text() == '' or self.lineEdit_1.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' or self.lineEdit_4.text() == '' or self.lineEdit_5.text() == '' or self.lineEdit_6.text() == '' or self.lineEdit_7.text() == '' or self.lineEdit_8.text() == '' or self.lineEdit_9.text() == '':
			QMessageBox.warning(self, '警告', '请输入完整信息!')
			return
		if self.g_infer == '':
			QMessageBox.warning(self, '警告', '请选择待修改的客户')
			return
		if self.lineEdit_1.text().find('‘') != -1 or self.lineEdit_1.text().find('’') != -1:
			QMessageBox.warning(self, '警告', '客户姓名中不可带单引号!')
			return
		if self.lineEdit_6.text().find('@') == -1:
			QMessageBox.warning(self, '警告', '请输入正确的邮箱地址!')
			return
		self.command = 'update 客户 set ' +  get_equation('客户姓名', self.lineEdit_1.text()) + ' , ' + get_equation('客户联系电话', self.lineEdit_4.text()) + ' , ' + get_equation('客户家庭住址', self.lineEdit_3.text()) + ' , ' + get_equation('客户身份证号', self.lineEdit_2.text()) + ' , ' + get_equation('联系人姓名', self.lineEdit_5.text()) + ' , ' + get_equation('联系人手机号', self.lineEdit_8.text()) + ' , ' + get_equation('联系人Email', self.lineEdit_6.text()) + ' , ' + get_equation('联系人关系', self.lineEdit_7.text()) + ' , ' + get_equation('员工身份证号', self.lineEdit_9.text()) + ' , ' + get_equation('负责人类型', self.lineEdit_0.text()) + ' where ' + self.g_infer
		# print(self.command)
		sure = QMessageBox.question(self, '确认', "确定修改客户信息?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
		if sure == QMessageBox.No:
			return
		self.execute(False)
		QMessageBox.information(self, '信息', '客户信息修改成功!')

	# 查询客户
	def inquire_client(self):
		self.command = 'select * from 客户 where ' + get_equation('客户姓名', self.lineEdit_1.text()) + ' and ' + get_equation('客户联系电话', self.lineEdit_4.text()) + ' and ' + get_equation('客户家庭住址', self.lineEdit_3.text()) + ' and ' + get_equation('客户身份证号', self.lineEdit_2.text()) + ' and ' + get_equation('联系人姓名', self.lineEdit_5.text()) + ' and ' + get_equation('联系人手机号', self.lineEdit_8.text()) + ' and ' + get_equation('联系人Email', self.lineEdit_6.text()) + ' and ' + get_equation('联系人关系', self.lineEdit_7.text()) + ' and ' + get_equation('员工身份证号', self.lineEdit_9.text()) + ' and ' + get_equation('负责人类型', self.lineEdit_0.text())
		result = self.execute(True)
		if status == 0 and result is not None:
			self.treeWidget_1.clear()
			infer = []
			for i in result:
				infer.append(QTreeWidgetItem([str(i[0]), str(i[3]), str(i[2]), str(i[1]), str(i[4]), str(i[6]), str(i[7]), str(i[5]), str(i[8]), str(i[9])]))
			self.treeWidget_1.addTopLevelItems(infer)

	# 清空客户
	def empty_client(self):
		self.lineEdit_0.setText('')
		self.lineEdit_1.setText('')
		self.lineEdit_3.setText('')
		self.lineEdit_4.setText('')
		self.lineEdit_7.setText('')
		self.lineEdit_8.setText('')
		self.lineEdit_2.setText('')
		self.lineEdit_9.setText('')
		self.lineEdit_5.setText('')
		self.lineEdit_6.setText('')

	def doubleclicked_client(self, item):
		self.lineEdit_1.setText(item.text(0))	# 客户姓名
		self.lineEdit_4.setText(item.text(3))	# 客户联系电话
		self.lineEdit_3.setText(item.text(2))	# 客户家庭住址
		self.lineEdit_2.setText(item.text(1))	# 客户身份证号
		self.lineEdit_5.setText(item.text(4))	# 联系人姓名
		self.lineEdit_8.setText(item.text(7))	# 联系人手机号
		self.lineEdit_6.setText(item.text(5))	# 联系人Email
		self.lineEdit_7.setText(item.text(6))	# 联系人关系
		self.lineEdit_9.setText(item.text(8))	# 员工身份证号
		self.lineEdit_0.setText(item.text(9))	# 负责人类型
		self.g_infer = get_equation('客户姓名', self.lineEdit_1.text()) + ' and ' + get_equation('客户联系电话', self.lineEdit_4.text()) + ' and ' + get_equation('客户家庭住址', self.lineEdit_3.text()) + ' and ' + get_equation('客户身份证号', self.lineEdit_2.text()) + ' and ' + get_equation('联系人姓名', self.lineEdit_5.text()) + ' and ' + get_equation('联系人手机号', self.lineEdit_8.text()) + ' and ' + get_equation('联系人Email', self.lineEdit_6.text()) + ' and ' + get_equation('联系人关系', self.lineEdit_7.text()) + ' and ' + get_equation('员工身份证号', self.lineEdit_9.text()) + ' and ' + get_equation('负责人类型', self.lineEdit_0.text())

	# 账户管理

	# 增加账户
	def insert_account(self):
		if self.comboBox_2.currentIndex() == 0 :
			if self.lineEdit_10.text() == '' or self.lineEdit_11.text() == '' or self.lineEdit_12.text() == '' or self.lineEdit_13.text() == '' or self.lineEdit_14.text() == '' or self.lineEdit_15.text() == '':
				QMessageBox.warning(self, '警告', '请将储蓄账户信息补全!')
				return
			self.comboBox_1.setCurrentIndex(0)
			sure = QMessageBox.question(self, '确认', "确定添加账户?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
			if sure == QMessageBox.No:
				return
			self.command = 'insert into 储蓄合作(客户身份证号, 支行名字) Values(' + add_qmark(self.lineEdit_13.text()) +  ", " + add_qmark(self.lineEdit_12.text()) + ')'
			if self.execute(False):
				self.command = 'select * from 账户 where ' + get_equation('账户号', self.lineEdit_10.text())
				if self.execute(True):
					pass
				else:
					self.command = 'insert into 账户(账户号, 开户日期, 余额) Values(' + add_qmark(self.lineEdit_10.text()) + ', ' + 'str_to_date(' + add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ', ' + add_qmark(self.lineEdit_11.text(), False) + ')'
					self.execute(False)
					self.command = 'select * from 储蓄账户 where ' + get_equation('账户号', self.lineEdit_10.text())
					if self.execute(True):
						pass
					else:
						self.command = 'insert into 储蓄账户(账户号, 开户日期, 余额, 利率, 货币类型) Values(' + add_qmark(self.lineEdit_10.text()) + ', '+ 'str_to_date('+ add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ', '+ add_qmark(self.lineEdit_11.text(), False) + ', ' + add_qmark(self.lineEdit_14.text(), False) + ', ' + add_qmark(self.lineEdit_15.text()) + ')'
						self.execute(False)
				self.command = 'insert into 储蓄开户(客户身份证号, 支行名字, 账户号, 最近访问日期) Values (' + add_qmark(self.lineEdit_13.text()) + ',' + add_qmark(self.lineEdit_12.text()) + ',' + add_qmark(self.lineEdit_10.text(), False) + ', NULL)'
				self.execute(False)
				QMessageBox.information(self, '信息', '账户添加成功!')
			else:
				QMessageBox.warning(self, '警告', '客户在一个支行只能拥有一个储蓄账户')

		else:
			if self.lineEdit_10.text() == '' or self.lineEdit_11.text() == '' or self.lineEdit_12.text() == '' or self.lineEdit_13.text() == '' or self.lineEdit_16.text() == '':
				QMessageBox.warning(self, '警告', '请将支票账户信息补全！')
				return
			self.comboBox_1.setCurrentIndex(0)
			sure = QMessageBox.question(self, '确认', "确定添加账户?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
			if sure == QMessageBox.No:
				return
			self.command = 'insert into 支票合作(客户身份证号, 支行名字) Values(' + add_qmark(self.lineEdit_13.text()) + ', ' + add_qmark(self.lineEdit_12.text()) + ')'
			if self.execute(False):
				self.command = 'select * from 账户 where ' + get_equation('账户号', self.lineEdit_10.text())
				if self.execute(True):
					pass
				else:
					self.command = 'insert into 账户(账户号, 开户日期, 余额) Values(' + add_qmark(self.lineEdit_10.text()) + ', ' + 'str_to_date(' + add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ', ' + add_qmark(self.lineEdit_11.text(), False) + ')'
					self.execute(False)
					self.command = 'select * from 支票账户 where ' + get_equation('账户号', self.lineEdit_10.text())
					if self.execute(True):
						pass
					else:
						self.command = 'insert into 支票账户(账户号, 开户日期, 余额, 透支额) Values(' + add_qmark(self.lineEdit_10.text(), False) + ', '+ 'str_to_date('+ add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ', '+ add_qmark(self.lineEdit_11.text(), False) +  ', ' + add_qmark(self.lineEdit_16.text(), False) + ')'
						self.execute(False)
				self.command = 'insert into 支票开户(客户身份证号, 支行名字, 账户号, 最近访问日期) Values (' + add_qmark(self.lineEdit_13.text()) + ',' + add_qmark(self.lineEdit_12.text()) + ',' + add_qmark(self.lineEdit_10.text()) + ', NULL)'
				self.execute(False)
				QMessageBox.information(self, '信息', '账户添加成功!')
			else:
				QMessageBox.warning(self, '警告', '客户在一个支行只能拥有一个支票账户')

	# 删除账户
	def delete_account(self):
		if self.lineEdit_10.text() == '':
			QMessageBox.warning(self, '警告', '请输入待销户的账户号！')
			return
		self.inquire_account()
		sure = QMessageBox.question(self, '确认', "确定删除账户?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if sure == QMessageBox.No:
			return
		if self.comboBox_2.currentIndex() == 0 :
			self.command = 'delete from 储蓄合作 where ' + get_equation('客户身份证号', self.lineEdit_13.text())
			self.execute(False)
			self.command = 'delete from 储蓄开户 where ' + get_equation('账户号', self.lineEdit_10.text())
			self.execute(False)
			self.command = 'delete from 储蓄账户 where ' + get_equation('账户号', self.lineEdit_10.text()) + ' and ' + '开户日期' + self.op[self.comboBox_1.currentIndex()] + 'str_to_date('+ add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ' and ' + get_equation('余额', self.lineEdit_11.text(), False) + ' and ' + get_equation('利率', self.lineEdit_14.text(), False) + ' and ' + get_equation('货币类型', self.lineEdit_15.text())
			self.execute(False)
		else:
			self.command = 'delete from 支票合作 where ' + get_equation('客户身份证号', self.lineEdit_13.text())
			self.execute(False)
			self.command = 'delete from 支票开户 where ' + get_equation('账户号', self.lineEdit_10.text())
			self.execute(False)
			self.command = 'delete from 支票账户 where ' + get_equation('账户号', self.lineEdit_10.text()) + ' and ' + '开户日期' + self.op[self.comboBox_1.currentIndex()] + 'str_to_date('+ add_qmark(self.dateEdit_2.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ' and ' + get_equation('余额', self.lineEdit_11.text(), False) + ' and ' + get_equation('透支额', self.lineEdit_16.text(), False)
			self.execute(False)
		self.command = 'delete from 账户 where ' + get_equation('账户号', self.lineEdit_10.text())
		self.execute(False)
		QMessageBox.information(self, '信息', '账户删除成功!')

	# 修改账户
	def modify_account(self):
		if self.lineEdit_10.text() == '':
			QMessageBox.warning(self, '警告', '请输入账户号！')
			return
		if self.g_infer == '':
			QMessageBox.warning(self, '警告', '请选择待修改的账户')
			return
		self.comboBox_1.setCurrentIndex(0)
		sure = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if sure == QMessageBox.No:
			return
		if self.comboBox_2.currentIndex() == 0 :
			infer = get_equation('账户号', self.lineEdit_10.text()) + ', ' + '开户日期 = str_to_date('+ add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ', ' + get_equation('余额', self.lineEdit_11.text(), False) +  ', ' + get_equation('利率', self.lineEdit_14.text(), False) + ', ' + get_equation('货币类型', self.lineEdit_15.text())
			self.command = 'update 储蓄账户 set ' + infer + ' where ' + self.g_infer
		else:
			infer = get_equation('账户号', self.lineEdit_10.text()) + ', ' + '开户日期 = str_to_date('+ add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ', ' + get_equation('余额', self.lineEdit_11.text(), False) +  ', ' + get_equation('透支额', self.lineEdit_16.text(), False)
			self.command = 'update 支票账户 set ' + infer + ' where ' + self.g_infer

		if self.execute(False):
			infer = get_equation('账户号', self.lineEdit_10.text(), False) + ', ' + '开户日期 = str_to_date(' + add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ', ' + get_equation('余额', self.lineEdit_11.text(), False)
			self.command = 'update 账户 set ' + infer + ' where ' + self.l_infer
			self.execute(False)
			QMessageBox.information(self, '信息', '账户修改成功!')
		else:
			QMessageBox.warning(self, '警告', '请勿修改账户号或检查您的输入')
		self.l_infer = ""

	# 查询账户
	def inquire_account(self):
		if self.comboBox_2.currentIndex() == 0 :
			self.command = 'select 储蓄账户.账户号 as 账户号, 开户日期, 余额, 利率, 货币类型, 储蓄开户.支行名字 as 开户支行, 客户身份证号 from 储蓄账户, 储蓄开户 where 储蓄账户.账户号 = 储蓄开户.账户号 and ' + get_equation('储蓄账户.账户号', self.lineEdit_10.text()) + ' and ' + '开户日期' + self.op[self.comboBox_1.currentIndex()] + 'str_to_date('+ add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ' and ' + get_equation('余额', self.lineEdit_11.text(), False) + ' and ' + get_equation('利率', self.lineEdit_14.text(), False) + ' and ' + get_equation('货币类型', self.lineEdit_15.text()) + ' and ' + get_equation('支行名字', self.lineEdit_12.text()) + ' and ' + get_equation('客户身份证号', self.lineEdit_13.text())
		else:
			self.command = 'select 支票账户.账户号 as 账户号, 开户日期, 余额, 透支额, 支票开户.支行名字 as 开户支行, 客户身份证号 from 支票账户, 支票开户 where 支票账户.账户号 = 支票开户.账户号 and ' + get_equation('支票账户.账户号', self.lineEdit_10.text()) + ' and ' + '开户日期' + self.op[self.comboBox_1.currentIndex()] + 'str_to_date('+ add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ' and ' + get_equation('余额', self.lineEdit_11.text(), False) + ' and ' + get_equation('支行名字', self.lineEdit_12.text()) + ' and ' + get_equation('客户身份证号', self.lineEdit_13.text()) + ' and ' + get_equation('透支额', self.lineEdit_16.text(), False)
		result = self.execute(True)
		if status == 0 and result is not None:
			self.print_account(result)

	def print_account(self, result):
		_translate = QtCore.QCoreApplication.translate
		self.treeWidget_2.clear()
		infer = []
		if self.comboBox_2.currentIndex() == 0:
			self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "账户号"))
			self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "身份证号"))
			self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "开户支行"))
			self.treeWidget_2.headerItem().setText(3, _translate("MainWindow", "开户日期"))
			self.treeWidget_2.headerItem().setText(4, _translate("MainWindow", "余额"))
			self.treeWidget_2.headerItem().setText(5, _translate("MainWindow", "利率"))
			self.treeWidget_2.headerItem().setText(6, _translate("MainWindow", "货币类型"))
			for i in result:
				infer.append(QTreeWidgetItem([str(i[0]), str(i[6]), str(i[5]), to_date(str(i[1])), str(i[2]), str(i[3]), str(i[4])]))
		else:
			self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "账户号"))
			self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "身份证号"))
			self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "开户支行"))
			self.treeWidget_2.headerItem().setText(3, _translate("MainWindow", "开户日期"))
			self.treeWidget_2.headerItem().setText(4, _translate("MainWindow", "余额"))
			self.treeWidget_2.headerItem().setText(5, _translate("MainWindow", "透支额"))
			self.treeWidget_2.headerItem().setText(6, _translate("MainWindow", ""))
			for i in result:
				infer.append(QTreeWidgetItem([str(i[0]), str(i[5]), str(i[4]), to_date(str(i[1])), str(i[2]), str(i[3])]))
		self.treeWidget_2.addTopLevelItems(infer)

	# 清空账户
	def empty_account(self):
		self.lineEdit_10.setText('')
		self.lineEdit_11.setText('')
		self.lineEdit_12.setText('')
		self.lineEdit_13.setText('')
		self.lineEdit_14.setText('')
		self.lineEdit_15.setText('')
		self.lineEdit_16.setText('')
		self.comboBox_1.setCurrentIndex(0)
		self.comboBox_2.setCurrentIndex(0)
		self.dateEdit_1.setDate(QDate.fromString('2000/01/01', 'yyyy/MM/dd'))

	def doubleclicked_account(self, item):
		self.lineEdit_10.setText(item.text(0))
		self.lineEdit_11.setText(item.text(4))
		self.lineEdit_12.setText(item.text(2))
		self.lineEdit_13.setText(item.text(1))
		self.comboBox_1.setCurrentIndex(0)
		self.dateEdit_1.setDate(QDate.fromString(item.text(3), 'yyyy/MM/dd'))
		self.l_infer = get_equation('账户号', item.text(0)) + ' and ' + '开户日期 = str_to_date('+ add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ' and ' + get_equation('余额', item.text(4), False)
		if self.comboBox_2.currentIndex() == 0 :
			self.lineEdit_14.setText(item.text(5))
			self.lineEdit_15.setText(item.text(6))
			self.g_infer = get_equation('账户号', item.text(0)) + ' and ' + '开户日期 = str_to_date('+ add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ' and ' + get_equation('余额', item.text(4), False) + ' and ' + get_equation('利率', item.text(5), False) +  ' and ' + get_equation('货币类型', item.text(6))
		else:
			self.lineEdit_16.setText(item.text(5))
			self.g_infer = get_equation('账户号', item.text(0)) + ' and ' + '开户日期 = str_to_date('+ add_qmark(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ' and ' + get_equation('余额', item.text(4), False) +' and ' + get_equation('透支额', item.text(5), False)

	# 贷款管理

	# 添加贷款
	def insert_loan(self):
		if self.lineEdit_17.text() == '' or self.lineEdit_18.text() == '' or self.lineEdit_19.text() == '':
			QMessageBox.warning(self, '警告', '请输入完整信息!')
			return
		self.comboBox_3.setCurrentIndex(0)
		sure = QMessageBox.question(self, '确认', "确定添加贷款?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if sure == QMessageBox.No:
			return
		self.command = 'insert into 贷款(贷款金额, 贷款号, 支行名字) Values(' + add_qmark(self.lineEdit_19.text(), False) + ', '+ add_qmark(self.lineEdit_17.text()) + ', '+ add_qmark(self.lineEdit_18.text()) + ')'
		if self.execute(False):
			QMessageBox.information(self, '信息', '贷款添加成功!')
		else:
			QMessageBox.warning(self, '警告', '该贷款已经存在!')

	# 删除贷款
	def delete_loan(self):
		if self.lineEdit_17.text() == '':
			QMessageBox.warning(self, '警告', '请选择待删除的贷款！')
			return
		self.inquire_loan()
		sure = QMessageBox.question(self, '确认', "确定删除贷款?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if sure == QMessageBox.No:
			return
		self.command = 'select 贷款金额 from 贷款 where 贷款号 = ' + self.lineEdit_17.text()
		result = self.execute(True)
		amount = result[0][0]
		self.command = 'select 贷款.贷款号, sum(支付.支付金额) from 贷款, 支付 where 贷款.贷款号 = 支付.贷款号 and 贷款.贷款号 = ' + self.lineEdit_17.text() + ' group by 贷款.贷款号'
		result = self.execute(True)
		if len(result) != 0 and result[0][1] != 0 and result[0][1] < amount:
			QMessageBox.warning(self, '警告', '贷款还在发放')
			return
		else:
			self.command = 'delete from 支付 where ' + get_equation('贷款号', self.lineEdit_17.text())
			self.execute(False)
			self.command = 'delete from 贷款 where ' + get_equation('贷款号', self.lineEdit_17.text())
			self.execute(False)
			QMessageBox.information(self, '信息', '贷款删除成功！')

	# 查询贷款
	def inquire_loan(self):
		if self.lineEdit_19.text() == '':
			amount = 'True'
		else:
			amount = '贷款金额' + self.op[self.comboBox_3.currentIndex()] + self.lineEdit_19.text()
		self.command = 'select * from 贷款 where ' + amount + ' and ' + get_equation('贷款号', self.lineEdit_17.text()) + ' and ' + get_equation('支行名字', self.lineEdit_18.text())
		result = self.execute(True)
		if status == 0 and result is not None:
			self.print_loan(result)

	def print_loan(self, result):
		self.treeWidget_3.clear()
		infer = []
		for i in result:
			self.command = 'select 贷款.贷款号, sum(支付.支付金额) from 贷款, 支付 where 贷款.贷款号 = 支付.贷款号 and 贷款.贷款号 = ' + str(i[0]) +' group by 贷款.贷款号'
			result = self.execute(True)
			if result == () or result[0][1] == 0:
				pos = '未开始发放'
			elif result[0][1] < i[2]:
				pos = '发放中，已发:' + str(result[0][1])
			else:
				pos = '已全部发放'
			infer.append(QTreeWidgetItem([str(i[0]), str(i[1]), str(i[2]), pos]))
		self.treeWidget_3.addTopLevelItems(infer)

	# 发放贷款
	def issue_loan(self):
		if self.lineEdit_17.text() == '' or self.lineEdit_20.text() == '' or self.lineEdit_21.text() == '':
			QMessageBox.warning(self, '警告', '输入贷款信息不足！')
			return
		self.command = 'select 贷款金额 from 贷款 where 贷款号 = ' + self.lineEdit_17.text()
		result_1 = self.execute(True)
		if result_1 == ():
			QMessageBox.warning(self, '警告', '贷款号不存在!')
			return
		self.command = 'select 贷款.贷款号, sum(支付.支付金额) from 贷款, 支付 where 贷款.贷款号 = 支付.贷款号 and 贷款.贷款号 = ' + self.lineEdit_17.text() + ' group by 贷款.贷款号'
		result_2 = self.execute(True)
		if len(result_2) == 0:
			a = 0
		else:
			a = result_2[0][1]
		if a + int(self.lineEdit_20.text()) > result_1[0][0]:
			QMessageBox.warning(self, '警告', '发放金额超出限制！')
			return
		self.command = 'insert into 支付(贷款号, 客户身份证号, 支付金额, 支付日期, 支付时间) values('+ add_qmark(self.lineEdit_17.text()) + ', ' + add_qmark(self.lineEdit_21.text()) + ', '  + add_qmark(self.lineEdit_20.text(), False) + ', str_to_date(' + add_qmark(QDate.currentDate().toString('yyyy/MM/dd')) + ', ' + add_qmark('%Y/%m/%d') + ') ,' + add_qmark(QTime.currentTime().toString(Qt.DefaultLocaleLongDate)) + ')'
		sure = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
		if sure == QMessageBox.No:
			return
		self.execute(False)
		QMessageBox.information(self, '信息', '贷款发放成功!')
		self.inquire_loan()

	# 清空贷款
	def empty_loan(self):
		self.lineEdit_17.setText('')
		self.lineEdit_18.setText('')
		self.lineEdit_19.setText('')
		self.lineEdit_20.setText('')
		self.lineEdit_21.setText('')
		self.comboBox_3.setCurrentIndex(0)

	def doubleclicked_loan(self, item):
		self.lineEdit_17.setText(item.text(0))
		self.lineEdit_18.setText(item.text(1))
		self.lineEdit_19.setText(item.text(2))
		self.comboBox_3.setCurrentIndex(0)
		self.g_infer = get_equation('贷款金额', self.lineEdit_19.text(), False) + ' and ' + get_equation('贷款号', self.lineEdit_17.text()) + ' and ' + get_equation('支行名字', self.lineEdit_18.text())

	# 业务统计

	# 储蓄统计
	def saving_statistic(self):
		time_limitation = '储蓄账户.开户日期 > str_to_date('+ add_qmark(self.dateEdit_2.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ' and 储蓄账户.开户日期 < str_to_date('+ add_qmark(self.dateEdit_3.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')'
		self.command = 'select 支行.支行名字,  COUNT(*) from 支行, 储蓄开户, 储蓄账户 where 支行.支行名字 = 储蓄开户.支行名字 and 储蓄开户.账户号 = 储蓄账户.账户号' + ' and ' + time_limitation + ' group by 支行.支行名字'
		result_1 = self.execute(True)
		# print(result)
		money = []
		for i in result_1:
			profit = 0
			bank = i[0]
			self.command = 'select 余额 from 支行, 储蓄开户, 储蓄账户 where 支行.支行名字 = 储蓄开户.支行名字 and 储蓄开户.账户号 = 储蓄账户.账户号' + ' and ' + '支行.支行名字 = '  + add_qmark(bank) + ' and ' + time_limitation + ' group by 储蓄账户.账户号'
			result_2 = self.execute(True)
			# print(result)
			for col in result_2:
				profit += col[0]
			money.append(profit)
		if result_1 is not None:
			self.treeWidget_4.clear()
			infer = []
			for i in range(len(result_1)):
				infer.append(QTreeWidgetItem([str(result_1[i][0]), str(money[i]), str(result_1[i][1])]))
			self.treeWidget_4.addTopLevelItems(infer)

	# 贷款统计
	def loan_statistic(self):
		time_limitation = '支付.支付日期 > str_to_date(' + add_qmark(self.dateEdit_2.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')' + ' and 支付.支付日期 < str_to_date(' + add_qmark(self.dateEdit_3.date().toString("yyyy/MM/dd")) + ', ' + add_qmark('%Y/%m/%d') + ')'
		self.command = 'select 名字, COUNT(*), SUM(金额) from ( select Distinct 支付.客户身份证号 as 身份证号, 贷款.支行名字 as 名字, SUM(支付.支付金额) as 金额 from 贷款, 支付 where 贷款.贷款号 = 支付.贷款号 and ' + time_limitation + ' group by 贷款.支行名字, 支付.客户身份证号) as test group by 名字 '
		command_result = self.execute(True)
		if command_result is not None:
			self.treeWidget_4.clear()
			L = []
			for i in command_result:
				L.append(QTreeWidgetItem([str(i[0]), str(i[2]), str(i[1])]))
			self.treeWidget_4.addTopLevelItems(L)

	# 清空统计框
	def empty_statistic(self):
		self.treeWidget_4.clear()

if __name__ == "__main__":
	try:
		db = MySQLdb.connect("localhost","root","12345abcxyz","bank", charset = "utf8")
		print("连接成功!")
		status = 0
	except:
		status = 1
		print("连接失败!")

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = MainWindow()
	MainWindow.show()
	sys.exit(app.exec_())
	if status == 0:
		db.close()