use bank;

insert into 支行 values('南昌', '南昌支行', 90000);
insert into 支行 values('合肥', '合肥支行', 40000);
insert into 支行 values('上海', '上海支行', 20000);
insert into 支行 values('北京', '北京支行', 10000);
insert into 支行 values('抚州', '抚州支行', 5000);

insert into 员工 values('刘至宇', '13213123132', '江西省抚州市临川区湖东一号', '1234231213', '1234231213', str_to_date('2022-05-09', '%Y-%m-%d'));
insert into 员工 values('周杰伦', '13243434322', '上海市浦东', '123443324342', '1234231213', str_to_date('2021-05-09', '%Y-%m-%d'));
insert into 员工 values('哈登', '90789632332', '北京市清华大学', '143341241', '1234231213', str_to_date('2022-03-16', '%Y-%m-%d'));
insert into 员工 values('姚明', '7236786723', '北京市北京大学', '798789', '798789', str_to_date('2018-03-09', '%Y-%m-%d'));
insert into 员工 values('易建联', '72389723', '安徽省合肥市中国科学技术大学', '98789689', '798789', str_to_date('2019-03-09', '%Y-%m-%d'));

insert into 客户 values('徐昊天', '15946901030', '江西省抚州市临川区穆堂路76号', '362502200202160214', '菲比', '12345', 'feibi@qq.com', '朋友', '1234231213','银行账户负责人');
insert into 客户 values('罗斯', '198789789', '江西省抚州市临川区若士路', '38927323', '瑞秋', '1232312321', 'ruiqiu@qq.com', '朋友', '143341241','贷款负责人');
insert into 客户 values('钱德勒', '159423123123', '江西省抚州市临川区新剪子口', '332817823', '莫妮卡', '1897239815', 'monica@qq.com', '朋友', '798789','贷款负责人');

insert into 贷款 values('2001', '北京支行', 50000.00);
insert into 贷款 values('2002', '上海支行', 60000.00);
insert into 贷款 values('2003', '合肥支行', 10000.00);
insert into 贷款 values('2004', '抚州支行', 3000.00);

insert into 支付 values('362502200202160214', str_to_date('2022-02-19', '%Y-%m-%d'), '13:20:39', 2000.00, '2001');
insert into 支付 values('38927323', str_to_date('2021-12-09', '%Y-%m-%d'), '19:51:02', 3000.00, '2002');
insert into 支付 values('332817823', str_to_date('2020-08-15', '%Y-%m-%d'), '16:30:00', 4000.00, '2003');

insert into 账户 values('3001', 2000.00, str_to_date('2020-02-19', '%Y-%m-%d'));
insert into 账户 values('3002', 3000.00, str_to_date('2021-08-21', '%Y-%m-%d'));
insert into 账户 values('3003', 2000.00, str_to_date('2021-05-18', '%Y-%m-%d'));
insert into 账户 values('3004', 3000.00, str_to_date('2022-01-21', '%Y-%m-%d'));
insert into 账户 values('3005', 4000.00, str_to_date('2022-02-14', '%Y-%m-%d'));
insert into 账户 values('3006', 7000.00, str_to_date('2022-05-12', '%Y-%m-%d'));
insert into 账户 values('3007', 2000.00, str_to_date('2022-03-14', '%Y-%m-%d'));

insert into 支票账户 values('3001', 2000, str_to_date('2020-02-19', '%Y-%m-%d'), 2000.00);
insert into 支票账户 values('3002', 1000, str_to_date('2021-08-21', '%Y-%m-%d'), 3000.00);
insert into 支票账户 values('3003', 3000, str_to_date('2021-05-18', '%Y-%m-%d'), 2000.00);

insert into 储蓄账户 values('3004', 0.002, '欧元', str_to_date('2022-01-21', '%Y-%m-%d'), 3000.00);
insert into 储蓄账户 values('3005', 0.003, '美元', str_to_date('2022-02-14', '%Y-%m-%d'), 4000.00);
insert into 储蓄账户 values('3006', 0.004, '人民币', str_to_date('2022-05-12', '%Y-%m-%d'), 7000.00);

insert into 支票合作 values('362502200202160214', '抚州支行');
insert into 支票合作 values('38927323', '北京支行');

insert into 支票开户 values('抚州支行', '3001', '362502200202160214', str_to_date('2020-02-19', '%Y-%m-%d'));
insert into 支票开户 values('北京支行', '3002', '38927323', str_to_date('2021-08-21', '%Y-%m-%d'));

insert into 储蓄合作 values('362502200202160214', '合肥支行');
insert into 储蓄合作 values('38927323', '南昌支行');

insert into 储蓄开户 values('合肥支行', '3004', '362502200202160214', str_to_date('2022-01-21', '%Y-%m-%d'));
insert into 储蓄开户 values('南昌支行', '3005', '38927323', str_to_date('2022-02-14', '%Y-%m-%d'));

# select * from 支付;
# select * from 储蓄账户 where 账户号 = '3009' and 开户日期 = str_to_date('2022/01/21', '%Y/%m/%d') and 余额 = 3000.0 and 利率 = 0.003 and 货币类型 = '欧元';
# select * from 储蓄账户 where 利率 = 0.002;

commit;