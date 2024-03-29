from GUI import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTreeWidgetItem
from PyQt5.QtCore import QDate, QTime, Qt
from PyQt5 import QtCore
import sys
import MySQLdb

def to_date(string):
	date = str(string).split('-')
	return date[0] + '/' + date[1] + '/' + date[2][0:2]

def equal(left, right, String = True):
	if right == '':
		return 'True'
	else:
		return left + ' = ' + to_str(right, String)

def to_str(value, String = True):
	if String:
		return '\'' + value + '\''
	else:
		return value

class MainWindow(QMainWindow, Ui_MainWindow):
	# 初始化类
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)
		self.setWindowTitle('银行业务系统-----PB19071535徐昊天')
		self.bind_up()
		self.query = ""
		self.last = ""
		self.last2 = ""
		self.op = [' = ', ' != ', ' > ', ' < ']
		self.comboBox_1.setCurrentIndex(0)
		self.comboBox_2.setCurrentIndex(0)
		self.comboBox_3.setCurrentIndex(0)
	def bind_up(self):
		self.pushButton_1.clicked.connect(self.insert_custom)
		self.pushButton_2.clicked.connect(self.delete_custom)
		self.pushButton_3.clicked.connect(self.update_custom)
		self.pushButton_4.clicked.connect(self.select_custom)
		self.pushButton_5.clicked.connect(self.clear_custom)
		self.treeWidget_1.itemDoubleClicked.connect(self.double_click_client)

		self.pushButton_6.clicked.connect(self.insert_account)
		self.pushButton_7.clicked.connect(self.delete_account)
		self.pushButton_8.clicked.connect(self.update_account)
		self.pushButton_9.clicked.connect(self.select_account)
		self.pushButton_10.clicked.connect(self.clear_account)
		self.treeWidget_2.itemDoubleClicked.connect(self.double_click_account)

		self.pushButton_11.clicked.connect(self.insert_loan)
		self.pushButton_12.clicked.connect(self.delete_loan)
		self.pushButton_13.clicked.connect(self.select_loan)
		self.pushButton_14.clicked.connect(self.pay_loan)
		self.pushButton_15.clicked.connect(self.clear_loan)
		self.treeWidget_3.itemDoubleClicked.connect(self.double_click_loan)

		self.pushButton_16.clicked.connect(self.store_statistic)
		self.pushButton_17.clicked.connect(self.loan_statistic)
		self.pushButton_18.clicked.connect(self.clear_store_statistic)
	
	def execute(self, recieve):
		global db
		result = []
		print(self.query)
		if status == 0:
			cursor = db.cursor()
			try:
				cursor.execute(self.query)
			except Exception as e:
				print(e)
				self.error_input('SQL执行失败')
				return False
			# print(self.query)
			if recieve:
				result = cursor.fetchall()
			else:
				result = True
			db.commit()
			cursor.close()

		self.last = '' #每进行一次操作需要刷新 doubleclicked item时记录的待更改值
		return result

	def error_input(self, err_msg):
		QMessageBox.warning(self, "错误提示", err_msg)

	#client
	def insert_custom(self):
		if self.lineEdit_0.text() == '' or self.lineEdit_1.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' or self.lineEdit_4.text() == '' or self.lineEdit_5.text() == '' or self.lineEdit_6.text() == '' or self.lineEdit_7.text() == '' or self.lineEdit_8.text() == '' or self.lineEdit_9.text() == '':
			self.error_input('请输入完整信息!')
			return
		if self.lineEdit_1.text().find('‘') != -1 or self.lineEdit_1.text().find('’') != -1:
			self.error_input('客户姓名中不可带单引号!')
			return
		if self.lineEdit_6.text().find('@') == -1:
			self.error_input('请输入正确的邮箱地址!')
			return
		#确认插入
		reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if reply == QMessageBox.No:
			return
		self.query = 'insert into 客户(客户姓名, 客户联系电话, 客户家庭住址, 客户身份证号, 联系人姓名, 联系人手机号, 联系人Email, 联系人关系, 员工身份证号, 负责人类型) Values(' + to_str(self.lineEdit_1.text()) + ', '+ to_str(self.lineEdit_4.text()) + ', '+ to_str(self.lineEdit_3.text()) + ', '+ to_str(self.lineEdit_2.text())  + ', '+ to_str(self.lineEdit_5.text()) +  ', '+ to_str(self.lineEdit_8.text()) + ', '+ to_str(self.lineEdit_6.text()) + ', '+ to_str(self.lineEdit_7.text()) + ', '+ to_str(self.lineEdit_9.text()) + ',' + to_str(self.lineEdit_0.text()) + ')'
		self.execute(False)


	def delete_custom(self):
		self.select_custom()
		#确认删除
		reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.No:
			return
		self.query = 'delete from 客户 where ' + equal('客户姓名', self.lineEdit_1.text()) + ' and ' + equal('客户联系电话', self.lineEdit_4.text()) + ' and ' + equal('客户家庭住址', self.lineEdit_3.text()) + ' and ' + equal('客户身份证号', self.lineEdit_2.text()) + ' and ' + equal('联系人姓名', self.lineEdit_5.text()) + ' and ' + equal('联系人手机号', self.lineEdit_8.text()) + ' and ' + equal('联系人Email', self.lineEdit_6.text()) + ' and ' + equal('联系人关系', self.lineEdit_7.text()) + ' and ' + equal('员工身份证号', self.lineEdit_9.text()) + ' and ' + equal('负责人类型', self.lineEdit_0.text())
		# self.query = 'delete from 客户 where ' + equal('客户身份证号', self.lineEdit_1.text()) + ' and ' + equal('身份证号', self.lineEdit_3.text()) + ' and ' + equal('姓名', self.lineEdit_4.text()) + ' and ' + equal('联系电话 ', self.lineEdit_7.text()) + ' and ' + equal('家庭住址', self.lineEdit_8.text()) + ' and ' + equal('联系人姓名', self.lineEdit_2.text()) + ' and ' + equal('联系人手机号', self.lineEdit_9.text()) + ' and ' + equal('联系人Email', self.lineEdit_5.text()) + ' and ' + equal('联系人与客户关系', self.lineEdit_6.text())

		if self.execute(False):
			pass
		else:
			self.error_input('具体原因：客户存在着关联账户或者贷款记录!')
		self.treeWidget_1.clear()

	def update_custom(self):
		'''
		if self.lineEdit_1.text() == '' or self.lineEdit_3.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_4.text() == '':
			self.error_input('关键信息缺失!')
			return
		if self.lineEdit_7.text() == '' or self.lineEdit_8.text() == '' or self.lineEdit_7.text() == '' or self.lineEdit_9.text() == '' or self.lineEdit_5.text() == '' or self.lineEdit_6.text() == '':
			self.error_input('更新时请补全信息，没有则填 无 ')
			return
		'''
		if self.lineEdit_0.text() == '' or self.lineEdit_1.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' or self.lineEdit_4.text() == '' or self.lineEdit_5.text() == '' or self.lineEdit_6.text() == '' or self.lineEdit_7.text() == '' or self.lineEdit_8.text() == '' or self.lineEdit_9.text() == '':
			self.error_input('请输入完整信息!')
			return
		if self.last == '':
			self.error_input('请双击待修改的项目')
			return
		if self.lineEdit_1.text().find('‘') != -1 or self.lineEdit_1.text().find('’') != -1:
			self.error_input('客户姓名中不可带单引号!')
			return
		if self.lineEdit_6.text().find('@') == -1:
			self.error_input('请输入正确的邮箱地址!')
			return
		# setting = equal('客户身份证号', self.lineEdit_1.text()) + ', ' + equal('身份证号', self.lineEdit_3.text()) + ', ' + equal('姓名', self.lineEdit_4.text()) + ', ' + equal('联系电话 ', self.lineEdit_7.text(), True) + ', ' + equal('家庭住址', self.lineEdit_8.text()) + ', ' + equal('联系人姓名', self.lineEdit_2.text()) + ', ' + equal('联系人手机号', self.lineEdit_9.text()) + ', ' + equal('联系人Email', self.lineEdit_5.text()) + ', ' + equal('联系人与客户关系', self.lineEdit_6.text())

		# self.query = 'update 客户 set ' + setting + ' where ' + self.last
		self.query = 'update 客户 set ' +  equal('客户姓名', self.lineEdit_1.text()) + ' , ' + equal('客户联系电话', self.lineEdit_4.text()) + ' , ' + equal('客户家庭住址', self.lineEdit_3.text()) + ' , ' + equal('客户身份证号', self.lineEdit_2.text()) + ' , ' + equal('联系人姓名', self.lineEdit_5.text()) + ' , ' + equal('联系人手机号', self.lineEdit_8.text()) + ' , ' + equal('联系人Email', self.lineEdit_6.text()) + ' , ' + equal('联系人关系', self.lineEdit_7.text()) + ' , ' + equal('员工身份证号', self.lineEdit_9.text()) + ' , ' + equal('负责人类型', self.lineEdit_0.text()) + ' where ' + self.last
		# print(self.query)
		#确认更新
		reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.No :
			return
		self.execute(False)

	def select_custom(self):
		self.query = 'select * from 客户 where ' + equal('客户姓名', self.lineEdit_1.text()) + ' and ' + equal('客户联系电话', self.lineEdit_4.text()) + ' and ' + equal('客户家庭住址', self.lineEdit_3.text()) + ' and ' + equal('客户身份证号', self.lineEdit_2.text()) + ' and ' + equal('联系人姓名', self.lineEdit_5.text()) + ' and ' + equal('联系人手机号', self.lineEdit_8.text()) + ' and ' + equal('联系人Email', self.lineEdit_6.text()) + ' and ' + equal('联系人关系', self.lineEdit_7.text()) + ' and ' + equal('员工身份证号', self.lineEdit_9.text()) + ' and ' + equal('负责人类型', self.lineEdit_0.text())
		# print(self.query)

		query_result = self.execute(True)
		# print(query_result)
		if status == 0 and query_result is not None:
			self.show_client(query_result)

		# print(self.lineEdit_0.text())
	def double_click_client(self, item):
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
		self.last = equal('客户姓名', self.lineEdit_1.text()) + ' and ' + equal('客户联系电话', self.lineEdit_4.text()) + ' and ' + equal('客户家庭住址', self.lineEdit_3.text()) + ' and ' + equal('客户身份证号', self.lineEdit_2.text()) + ' and ' + equal('联系人姓名', self.lineEdit_5.text()) + ' and ' + equal('联系人手机号', self.lineEdit_8.text()) + ' and ' + equal('联系人Email', self.lineEdit_6.text()) + ' and ' + equal('联系人关系', self.lineEdit_7.text()) + ' and ' + equal('员工身份证号', self.lineEdit_9.text()) + ' and ' + equal('负责人类型', self.lineEdit_0.text())
		# self.last = equal('客户身份证号', self.lineEdit_1.text()) + ' and ' + equal('身份证号', self.lineEdit_3.text()) + ' and ' + equal('姓名', self.lineEdit_4.text()) + ' and ' + equal('联系电话 ', self.lineEdit_7.text()) + ' and ' + equal('家庭住址', self.lineEdit_8.text()) + ' and ' + equal('联系人姓名', self.lineEdit_2.text()) + ' and ' + equal('联系人手机号', self.lineEdit_9.text()) + ' and ' + equal('联系人Email', self.lineEdit_5.text()) + ' and ' + equal('联系人与客户关系', self.lineEdit_6.text())

	def clear_custom(self):
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


	def show_client(self, result):
		self.treeWidget_1.clear()
		L=[]
		for row in result:
			L.append(QTreeWidgetItem([str(row[0]), str(row[3]), str(row[2]), str(row[1]), str(row[4]), str(row[6]),str(row[7]), str(row[5]), str(row[8]), str(row[9])]))
		self.treeWidget_1.addTopLevelItems(L)

#account
	def insert_account(self):
		if self.lineEdit_10.text() == '' or self.lineEdit_11.text() == '' or self.lineEdit_12.text() == '' or self.lineEdit_13.text() == '':
			self.error_input('输入信息不足!')
			return
		#确认插入
		self.comboBox_1.setCurrentIndex(0)  # 插入操作强制设置日期 = op
		reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if reply == QMessageBox.No:
			return

		if self.comboBox_2.currentIndex() == 0 :
			if self.lineEdit_14.text() == '' or self.lineEdit_15.text() == '':
				self.error_input('请将储蓄账户信息补全！')
				return
			self.query = 'insert into 储蓄合作(客户身份证号, 支行名字) Values(' + to_str(self.lineEdit_13.text()) +  ", " + to_str(self.lineEdit_12.text()) + ')'
			if self.execute(False):
				self.query = 'select * from 账户 where ' + equal('账户号', self.lineEdit_10.text())
				if self.execute(True):
					pass
				else:
					self.query = 'insert into 账户(账户号, 开户日期, 余额) Values(' + to_str(self.lineEdit_10.text()) + ', ' + 'str_to_date(' + to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ', ' + to_str(self.lineEdit_11.text(), False) + ')'
					self.execute(False)
					self.query = 'select * from 储蓄账户 where ' + equal('账户号', self.lineEdit_10.text())
					if self.execute(True):
						pass
					else:
						self.query = 'insert into 储蓄账户(账户号, 开户日期, 余额, 利率, 货币类型) Values(' + to_str(self.lineEdit_10.text()) + ', '+ 'str_to_date('+ to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ', '+ to_str(self.lineEdit_11.text(), False) + ', ' + to_str(self.lineEdit_14.text(), False) + ', ' + to_str(self.lineEdit_15.text()) + ')'
						self.execute(False)
				self.query = 'insert into 储蓄开户(客户身份证号, 支行名字, 账户号, 最近访问日期) Values (' + to_str(self.lineEdit_13.text()) + ',' + to_str(self.lineEdit_12.text()) + ',' + to_str(self.lineEdit_10.text(), False) + ', NULL)'
				self.execute(False)
			else:
				self.error_input('详细信息：每个客户在一个支行只能拥有一个储蓄账户')

		else:
			if self.lineEdit_16.text() == '':
				self.error_input('请将支票账户信息补全！')
				return
			self.query = 'insert into 支票合作(客户身份证号, 支行名字) Values(' + to_str(self.lineEdit_13.text()) + ', ' + to_str(self.lineEdit_12.text()) + ')'
			if self.execute(False):
				self.query = 'select * from 账户 where ' + equal('账户号', self.lineEdit_10.text())
				if self.execute(True):
					pass
				else:
					self.query = 'insert into 账户(账户号, 开户日期, 余额) Values(' + to_str(self.lineEdit_10.text()) + ', ' + 'str_to_date(' + to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ', ' + to_str(self.lineEdit_11.text(), False) + ')'
					self.execute(False)
					self.query = 'select * from 支票账户 where ' + equal('账户号', self.lineEdit_10.text())
					if self.execute(True):
						pass
					else:
						self.query = 'insert into 支票账户(账户号, 开户日期, 余额, 透支额) Values(' + to_str(self.lineEdit_10.text(), False) + ', '+ 'str_to_date('+ to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ', '+ to_str(self.lineEdit_11.text(), False) +  ', ' + to_str(self.lineEdit_16.text(), False) + ')'
						self.execute(False)
				self.query = 'insert into 支票开户(客户身份证号, 支行名字, 账户号, 最近访问日期) Values (' + to_str(self.lineEdit_13.text()) + ',' + to_str(self.lineEdit_12.text()) + ',' + to_str(self.lineEdit_10.text()) + ', NULL)'
				self.execute(False)
			else:
				self.error_input('详细信息：每个客户在一个支行只能拥有一个支票账户')


	def delete_account(self):
		if self.lineEdit_10.text() == '':
			self.error_input('请给定销户账号！')
			return
		self.select_account()
		#确认删除
		reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.No:
			return
		if self.lineEdit_11.text() == '':
			money = 'True'
		else:
			money = '余额' + '=' + self.lineEdit_11.text()
		if self.comboBox_2.currentIndex() == 0 :
			self.query = 'delete from 储蓄合作 where ' + equal('客户身份证号', self.lineEdit_13.text())
			self.execute(False)
			self.query = 'delete from 储蓄开户 where ' + equal('账户号', self.lineEdit_10.text())
			self.execute(False)
			self.query = 'delete from 储蓄账户 where ' + equal('账户号', self.lineEdit_10.text()) + ' and ' + '开户日期' + self.op[self.comboBox_1.currentIndex()] + 'str_to_date('+ to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ' and ' + money + ' and ' + equal('利率', self.lineEdit_14.text(), False) + ' and ' + equal('货币类型', self.lineEdit_15.text())
		else:
			self.query = 'delete from 支票合作 where ' + equal('客户身份证号', self.lineEdit_13.text())
			self.execute(False)
			self.query = 'delete from 支票开户 where ' + equal('账户号', self.lineEdit_10.text())
			self.execute(False)
			self.query = 'delete from 支票账户 where ' + equal('账户号', self.lineEdit_10.text()) + ' and ' + '开户日期' + self.op[self.comboBox_1.currentIndex()] + 'str_to_date('+ to_str(self.dateEdit_2.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ' and ' + money + ' and ' + equal('透支额', self.lineEdit_16.text(), False)
		self.execute(False)
		self.query = 'delete from 账户 where ' + equal('账户号', self.lineEdit_10.text())
		self.execute(False)

	def update_account(self):
		if self.lineEdit_10.text() == '':
			self.error_input('请输入账户号!')
			return
		if self.last == '': #update 输入信息不足
			self.error_input('请双击待修改的项目')
			return

		self.comboBox_1.setCurrentIndex(0)  # 更新操作强制设置日期 = op
		# 确认更新
		reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.No:
			return
		if self.comboBox_2.currentIndex() == 0 :
			setting = equal('账户号', self.lineEdit_10.text()) + ', ' + '开户日期 = str_to_date('+ to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ', ' + equal('余额', self.lineEdit_11.text(), False) +  ', ' + equal('利率', self.lineEdit_14.text(), False) + ', ' + equal('货币类型', self.lineEdit_15.text())
			# self.query = 'update 客户 set ' + equal('客户姓名', self.lineEdit_1.text()) + ' , ' + equal('客户联系电话', self.lineEdit_4.text()) + ' , ' + equal('客户家庭住址', self.lineEdit_3.text()) + ' , ' + equal('客户身份证号', self.lineEdit_2.text()) + ' , ' + equal('联系人姓名', self.lineEdit_5.text()) + ' , ' + equal('联系人手机号', self.lineEdit_8.text()) + ' , ' + equal('联系人Email', self.lineEdit_6.text()) + ' , ' + equal('联系人关系', self.lineEdit_7.text()) + ' , ' + equal('员工身份证号', self.lineEdit_9.text()) + ' , ' + equal('负责人类型', self.lineEdit_0.text()) + ' where ' + self.last
			self.query = 'update 储蓄账户 set ' + setting + ' where ' + self.last
			tag = self.execute(False)
		else:
			setting = equal('账户号', self.lineEdit_10.text()) + ', ' + '开户日期 = str_to_date('+ to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ', ' + equal('余额', self.lineEdit_11.text(), False) +  ', ' + equal('透支额', self.lineEdit_16.text(), False)
			self.query = 'update 支票账户 set ' + setting + ' where ' + self.last
			tag = self.execute(False)

		if tag:
			setting = equal('账户号', self.lineEdit_10.text(), False) + ', ' + '开户日期 = str_to_date(' + to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ', ' + equal('余额', self.lineEdit_11.text(), False)
			self.query = 'update 账户 set ' + setting + ' where ' + self.last2
			self.execute(False)
		else:
			self.error_input('详细信息：请勿修改账户号或检查您的输入')
		self.last2 = ""

	def select_account(self):
		if self.lineEdit_11.text() == '':
			money = 'True'
		else:
			money = '余额' + '=' + self.lineEdit_11.text()
		if self.comboBox_2.currentIndex() == 0 :
			self.query = 'select 储蓄账户.账户号 as 账户号, 开户日期, 余额, 利率, 货币类型, 储蓄开户.支行名字 as 开户支行, 客户身份证号 from 储蓄账户, 储蓄开户 where 储蓄账户.账户号 = 储蓄开户.账户号 and ' + equal('储蓄账户.账户号', self.lineEdit_10.text()) + ' and ' + '开户日期' + self.op[self.comboBox_1.currentIndex()] + 'str_to_date('+ to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ' and ' + money + ' and ' + equal('利率', self.lineEdit_14.text(), False) + ' and ' + equal('货币类型', self.lineEdit_15.text()) + ' and ' + equal('支行名字', self.lineEdit_12.text()) + ' and ' + equal('客户身份证号', self.lineEdit_13.text())
		else:
			self.query = 'select 支票账户.账户号 as 账户号, 开户日期, 余额, 透支额, 支票开户.支行名字 as 开户支行, 客户身份证号 from 支票账户, 支票开户 where 支票账户.账户号 = 支票开户.账户号 and ' + equal('支票账户.账户号', self.lineEdit_10.text()) + ' and ' + '开户日期' + self.op[self.comboBox_1.currentIndex()] + 'str_to_date('+ to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ' and ' + money + ' and ' + equal('支行名字', self.lineEdit_12.text()) + ' and ' + equal('客户身份证号', self.lineEdit_13.text()) + ' and ' + equal('透支额', self.lineEdit_16.text(), False)
		query_result = self.execute(True)
		# print(self.query)
		if status == 0 and query_result is not None:
			self.show_account(query_result)

	def double_click_account(self, item, column):
		self.lineEdit_10.setText(item.text(0))
		self.lineEdit_11.setText(item.text(4))
		self.lineEdit_12.setText(item.text(2))
		self.lineEdit_13.setText(item.text(1))
		self.comboBox_1.setCurrentIndex(0)
		self.dateEdit_1.setDate(QDate.fromString(item.text(3), 'yyyy/MM/dd'))
		self.last2 = equal('账户号', item.text(0)) + ' and ' + '开户日期 = str_to_date('+ to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ' and ' + equal('余额', item.text(4), False)
		if self.comboBox_2.currentIndex() == 0 :
			self.lineEdit_14.setText(item.text(5))
			self.lineEdit_15.setText(item.text(6))
			self.last = equal('账户号', item.text(0)) + ' and ' + '开户日期 = str_to_date('+ to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ' and ' + equal('余额', item.text(4), False) + ' and ' + equal('利率', item.text(5), False) +  ' and ' + equal('货币类型', item.text(6))
		else:
			self.lineEdit_16.setText(item.text(5))
			self.last = equal('账户号', item.text(0)) + ' and ' + '开户日期 = str_to_date('+ to_str(self.dateEdit_1.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ' and ' + equal('余额', item.text(4), False) +' and ' + equal('透支额', item.text(5), False)

	def clear_account(self):
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

	def show_account(self, result):
		_translate = QtCore.QCoreApplication.translate
		self.treeWidget_2.clear()
		L=[]
		if self.comboBox_2.currentIndex() == 0:
			self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "账户号"))
			self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "身份证号"))
			self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "开户支行"))
			self.treeWidget_2.headerItem().setText(3, _translate("MainWindow", "开户日期"))
			self.treeWidget_2.headerItem().setText(4, _translate("MainWindow", "余额"))
			self.treeWidget_2.headerItem().setText(5, _translate("MainWindow", "利率"))
			self.treeWidget_2.headerItem().setText(6, _translate("MainWindow", "货币类型"))
			for row in result:
				# date = to_date(row[1])
				L.append(QTreeWidgetItem([str(row[0]), str(row[6]), str(row[5]), to_date(str(row[1])), str(row[2]),str(row[3]),str(row[4])]))
			self.treeWidget_2.addTopLevelItems(L)
		else:
			self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "账户号"))
			self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "身份证号"))
			self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "开户支行"))
			self.treeWidget_2.headerItem().setText(3, _translate("MainWindow", "开户日期"))
			self.treeWidget_2.headerItem().setText(4, _translate("MainWindow", "余额"))
			self.treeWidget_2.headerItem().setText(5, _translate("MainWindow", "透支额"))
			self.treeWidget_2.headerItem().setText(6, _translate("MainWindow", ""))
			for row in result:
				# date = to_date(row[1])
				L.append(QTreeWidgetItem([str(row[0]), str(row[5]), str(row[4]), to_date(str(row[1])), str(row[2]), str(row[3])]))
			self.treeWidget_2.addTopLevelItems(L)

	def insert_loan(self):
		if self.lineEdit_17.text() == '' or self.lineEdit_18.text() == '' or self.lineEdit_19.text() == '':
			self.error_input('输入信息不足!')
			return
		self.comboBox_3.setCurrentIndex(0)
		#确认插入
		reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if reply == QMessageBox.No:
			return
		self.query = 'insert into 贷款(贷款金额, 贷款号, 支行名字) Values(' + to_str(self.lineEdit_19.text(), False) + ', '+ to_str(self.lineEdit_17.text()) + ', '+ to_str(self.lineEdit_18.text()) + ')'
		self.execute(False)
		'''
		if self.execute(False):
			self.query = 'insert into 支付(贷款号, 客户身份证号, 支付金额, 支付日期, 支付时间) Values(' + to_str(self.lineEdit_17.text()) + ', ' + to_str(self.lineEdit_21.text())+ ', ' + to_str(self.lineEdit_20.text(), False)+', ' + 'str_to_date(' + to_str(QDate.currentDate().toString('yyyy/MM/dd')) + ', ' + to_str('%Y/%m/%d') + ') ,' + to_str(QTime.currentTime().toString(Qt.DefaultLocaleLongDate)) + ')'
			if self.execute(False):
				self.error_input('插入贷款成功')
			else:	#rollback
				self.query = 'delete from 贷款 where ' + equal(self.lineEdit_17.text())
				self.execute(False)
		'''
	def delete_loan(self):
		self.select_loan()
		#确认删除
		reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.No:
			return
		self.query = 'select 贷款金额 from 贷款 where 贷款号 = ' + self.lineEdit_17.text()
		result = self.execute(True)
		money = result[0][0]
		self.query = 'select 贷款.贷款号, sum(支付.支付金额) from 贷款, 支付 where 贷款.贷款号 = 支付.贷款号 and 贷款.贷款号 = ' + self.lineEdit_17.text() + ' group by 贷款.贷款号'
		result = self.execute(True)
		if result == ():
			self.query = 'delete from 支付 where ' + equal('贷款号', self.lineEdit_17.text())
			self.execute(False)
			self.query = 'delete from 贷款 where ' + equal('贷款号', self.lineEdit_17.text())
			self.execute(False)
			self.error_input('删除成功！')
			#self.treeWidget.clear()
		elif result[0][1] != 0 and result[0][1] < money:
			self.error_input('贷款还在发放')
			return
		else:
			self.query = 'delete from 支付 where ' + equal('贷款号', self.lineEdit_17.text())
			self.execute(False)
			self.query = 'delete from 贷款 where ' + equal('贷款号', self.lineEdit_17.text())
			self.execute(False)
			self.error_input('删除成功！')

	def select_loan(self):
		if self.lineEdit_19.text() == '':
			money = 'True'
		else:
			money = '贷款金额' + self.op[self.comboBox_3.currentIndex()] + self.lineEdit_19.text()
		self.query = 'select * from 贷款 where ' + money + ' and ' + equal('贷款号', self.lineEdit_17.text()) + ' and ' + equal('支行名字', self.lineEdit_18.text())
		query_result = self.execute(True)
		if status == 0 and query_result is not None:
			self.show_loan(query_result)

	def double_click_loan(self, item, column):
		self.lineEdit_17.setText(item.text(0))
		self.lineEdit_18.setText(item.text(1))
		self.lineEdit_19.setText(item.text(2))
		self.comboBox_3.setCurrentIndex(0)
		self.last = equal('贷款金额', self.lineEdit_19.text(), False) + ' and ' + equal('贷款号', self.lineEdit_17.text()) + ' and ' + equal('支行名字', self.lineEdit_18.text())

	def clear_loan(self):
		self.lineEdit_17.setText('')
		self.lineEdit_18.setText('')
		self.lineEdit_19.setText('')
		self.lineEdit_20.setText('')
		self.lineEdit_21.setText('')
		self.comboBox_3.setCurrentIndex(0)

	def show_loan(self, result):
		self.treeWidget_3.clear()
		L=[]
		for row in result:
			money = row[2]
			self.query = 'select 贷款.贷款号, sum(支付.支付金额) from 贷款, 支付 where 贷款.贷款号 = 支付.贷款号 and 贷款.贷款号 = ' + str(row[0]) +' group by 贷款.贷款号'
			result = self.execute(True)
			if result == () or result[0][1] == 0:
				status = '未发放'
			elif result[0][1] < money:
				status = '发放中，已发:' + str(result[0][1])
			else:
				status = '已全部发放'
			# print(result)
			L.append(QTreeWidgetItem([str(row[0]), str(row[1]), str(row[2]), status]))
		self.treeWidget_3.addTopLevelItems(L)

	def pay_loan(self):
		if self.lineEdit_17.text() == '' or self.lineEdit_20.text() == '' or self.lineEdit_21.text() == '':
			self.error_input('输入发放贷款信息不足！')
			return
		self.query = 'select 贷款金额 from 贷款 where 贷款号 = ' + self.lineEdit_17.text()
		result = self.execute(True)
		if result == ():
			self.error_input('贷款号不存在，请先添加记录')
			return
		money = result[0][0]
		# self.query = 'insert into 支付(贷款号, 客户身份证号, 支付金额, 支付日期, 支付时间) Values(' + to_str(self.lineEdit_17.text()) + ', ' + to_str(self.lineEdit_21.text()) + ', ' + to_str(self.lineEdit_20.text(), False) + ', ' + 'str_to_date(' + to_str(QDate.currentDate().toString('yyyy/MM/dd')) + ', ' + to_str('%Y/%m/%d') + ') ,' + to_str(QTime.currentTime().toString(Qt.DefaultLocaleLongDate)) + ')'
		# self.execute(False)
		self.query = 'select 贷款.贷款号, sum(支付.支付金额) from 贷款, 支付 where 贷款.贷款号 = 支付.贷款号 and 贷款.贷款号 = ' + self.lineEdit_17.text() + ' group by 贷款.贷款号'
		result = self.execute(True)
		if len(result) == 0:
			a = 0
		else:
			a = result[0][1]
		if a + int(self.lineEdit_20.text()) > money:
			self.error_input('发放金额超出限制！')
			return
		self.query = 'insert into 支付(贷款号, 客户身份证号, 支付金额, 支付日期, 支付时间) values('+ to_str(self.lineEdit_17.text()) + ', ' + to_str(self.lineEdit_21.text()) + ', '  + to_str(self.lineEdit_20.text(), False) + ', str_to_date(' + to_str(QDate.currentDate().toString('yyyy/MM/dd')) + ', ' + to_str('%Y/%m/%d') + ') ,' + to_str(QTime.currentTime().toString(Qt.DefaultLocaleLongDate)) + ')'

		#确认发放
		reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
		if reply == QMessageBox.No:
			return
		self.execute(False)
		self.select_loan()

	def store_statistic(self):
		time_interval = '储蓄账户.开户日期 > str_to_date('+ to_str(self.dateEdit_2.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ' and 储蓄账户.开户日期 < str_to_date('+ to_str(self.dateEdit_3.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')'
		self.query = 'select 支行.支行名字,  COUNT(*) from 支行, 储蓄开户, 储蓄账户 where 支行.支行名字 = 储蓄开户.支行名字 and 储蓄开户.账户号 = 储蓄账户.账户号' + ' and ' + time_interval + ' group by 支行.支行名字'
		# self.query = 'select 支行.支行名字, 储蓄开户.账户号, 余额 from 支行, 储蓄开户, 储蓄账户 where 支行.支行名字 = 储蓄开户.支行名字 and 储蓄开户.账户号 = 储蓄账户.账户号' + ' and ' + time_interval
		query_result = self.execute(True)
		print(query_result)
		money = []
		for row in query_result:
			profit = 0
			bank = row[0]
			self.query = 'select 余额 from 支行, 储蓄开户, 储蓄账户 where 支行.支行名字 = 储蓄开户.支行名字 and 储蓄开户.账户号 = 储蓄账户.账户号' + ' and ' + '支行.支行名字 = '  + to_str(bank) + ' and ' + time_interval + ' group by 储蓄账户.账户号'
			result = self.execute(True)
			# print(result)
			for col in result:
				profit += col[0]
			money.append(profit)
		# result = ()
		# self.query = 'select SUM(余额) from 支行, 储蓄开户, 储蓄账户 where 支行.支行名字 = 储蓄开户.支行名字 and 储蓄开户.账户号 = 储蓄账户.账户号' + ' and ' + time_interval + ' group by 支行.支行名字'
		if query_result is not None:
			self.treeWidget_4.clear()
			L = []
			for i in range(len(query_result)):
				L.append(QTreeWidgetItem([str(query_result[i][0]), str(money[i]), str(query_result[i][1])]))
			self.treeWidget_4.addTopLevelItems(L)

	def clear_store_statistic(self):
		self.treeWidget_4.clear()

	def loan_statistic(self):
		time_interval = '支付.支付日期 > str_to_date(' + to_str(self.dateEdit_2.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')' + ' and 支付.支付日期 < str_to_date(' + to_str(self.dateEdit_3.date().toString("yyyy/MM/dd")) + ', ' + to_str('%Y/%m/%d') + ')'
		self.query = 'select 名字, COUNT(*), SUM(金额) from ( select Distinct 支付.客户身份证号 as 身份证号, 贷款.支行名字 as 名字, SUM(支付.支付金额) as 金额 from 贷款, 支付 where 贷款.贷款号 = 支付.贷款号 and ' + time_interval + ' group by 贷款.支行名字, 支付.客户身份证号) as test group by 名字 '
		query_result = self.execute(True)
		if query_result is not None:
			self.treeWidget_4.clear()
			L = []
			for row in query_result:
				L.append(QTreeWidgetItem([str(row[0]), str(row[2]), str(row[1])]))
			self.treeWidget_4.addTopLevelItems(L)

if __name__ == "__main__":
	try:
		db = MySQLdb.connect("localhost","root","12345abcxyz","bank", charset = "utf8")
		print("Connected successfully!")
		status = 0
	except:
		status = 1
		print("Failed to connect the database!")

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = MainWindow()
	MainWindow.show()
	sys.exit(app.exec_())
	if status == 0:
		db.close()