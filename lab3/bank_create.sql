drop database if exists bank;
create database bank;
use bank;

/*==============================================================*/
/* Table: 客户表                                                */
/*==============================================================*/
create table 客户 
(
   客户姓名                 varchar(50),
   客户联系电话             varchar(50),
   客户家庭住址             varchar(50),
   客户身份证号             varchar(50)   not null,
   联系人姓名               varchar(50)   not null,
   联系人手机号             varchar(50),
   联系人Email              varchar(50),
   联系人关系               varchar(50),
   员工身份证号             varchar(50),
   负责人类型               varchar(50),
   constraint PK primary key (客户身份证号)
);

/*==============================================================*/
/* Table: 账户表                                                */
/*==============================================================*/
create table 账户 
(
   账户号                   varchar(50)   not null,
   余额                     double,
   开户日期                 DATE,
   constraint PK primary key (账户号)
);

/*==============================================================*/
/* Table: 支票账户表                                            */
/*==============================================================*/
create table 支票账户 
(
   账户号                  varchar(50)   not null,
   透支额                  double,
   开户日期                DATE,
   余额                    double,
   constraint PK primary key (账户号)
);

/*==============================================================*/
/* Table: 储蓄账户表                                            */
/*==============================================================*/
create table 储蓄账户 
(
   账户号                  varchar(50)   not null,
   利率                    double,
   货币类型                varchar(50),
   开户日期                DATE,
   余额                    double,
   constraint PK primary key (账户号)
);

/*==============================================================*/
/* Table: 员工表                                                */
/*==============================================================*/
create table 员工 
(
   员工姓名                  varchar(50),
   员工电话号码              varchar(50),
   员工家庭住址              varchar(50),
   员工身份证号              varchar(50)   not null,
   经理身份证号              varchar(50),
   开始工作日期              DATE,
   constraint PK primary key (员工身份证号)
);

/*==============================================================*/
/* Table: 支行表                                                */
/*==============================================================*/
create table 支行 
(
   城市                      varchar(50)   not null,
   支行名字                  varchar(50)   not null,
   资产                      double   not null,
   constraint PK primary key (支行名字)
);

/*==============================================================*/
/* Table: 贷款表                                                */
/*==============================================================*/
create table 贷款 
(
   贷款号                    varchar(50)   not null,
   支行名字                  varchar(50),
   贷款金额                  double,
   constraint PK primary key (贷款号)
);

/*==============================================================*/
/* Table: 支付表                                                */
/*==============================================================*/
create table 支付 
(
   客户身份证号              varchar(50)   not null,
   支付日期                  DATE,
   支付时间				     varchar(50),
   支付金额                  double,
   贷款号                    varchar(50)   not null,
   constraint PK primary key (客户身份证号,支付日期,支付时间,贷款号)
);

/*==============================================================*/
/* Table: 支票开户表                                            */
/*==============================================================*/
create table 支票开户 
(
   支行名字                  varchar(50)   not null,
   账户号                    varchar(50)   not null,
   客户身份证号              varchar(50)   not null,
   最近访问日期              DATE,
   constraint PK primary key (支行名字, 账户号, 客户身份证号)
);


/*==============================================================*/
/* Table: 储蓄开户表                                            */
/*==============================================================*/
create table 储蓄开户 
(
   支行名字                  varchar(50)   not null,
   账户号                    varchar(50)   not null,
   客户身份证号              varchar(50)   not null,
   最近访问日期              DATE,
   constraint PK primary key (支行名字, 账户号, 客户身份证号)
);

/*==============================================================*/
/* Table: 支票合作表                                            */
/*==============================================================*/
create table 支票合作
(
   客户身份证号               varchar(50)   not null,
   支行名字                   varchar(50)   not null,
   constraint PK primary key (客户身份证号, 支行名字)
);

/*==============================================================*/
/* Table: 储蓄合作表                                            */
/*==============================================================*/
create table 储蓄合作
(
   客户身份证号               varchar(50)   not null,
   支行名字                   varchar(50)   not null,
   constraint PK primary key (客户身份证号, 支行名字)
);

alter table 客户 add constraint FK_客户_员工 foreign key (员工身份证号)
      references 员工 (员工身份证号);
      
alter table 员工 add constraint FK_员工_员工 foreign key (经理身份证号)
      references 员工 (员工身份证号);
      
alter table 支票账户 add constraint FK_支票账户_账户 foreign key (账户号)
      references 账户 (账户号);
      
alter table 储蓄账户 add constraint FK_储蓄账户_账户 foreign key (账户号)
      references 账户 (账户号);
      
alter table 贷款 add constraint FK_贷款_支行 foreign key (支行名字)
      references 支行 (支行名字);
      
alter table 支付 add constraint FK_支付_客户 foreign key (客户身份证号)
      references 客户 (客户身份证号);
      
alter table 支付 add constraint FK_支付_贷款 foreign key (贷款号)
      references 贷款 (贷款号);

alter table 支票开户 add constraint FK_支票开户_支行 foreign key (支行名字)
      references 支行 (支行名字);

alter table 支票开户 add constraint FK_支票开户_支票账户 foreign key (账户号)
      references 支票账户 (账户号);
      
alter table 支票开户 add constraint FK_支票开户_客户 foreign key (客户身份证号)
      references 客户 (客户身份证号);
      
alter table 储蓄开户 add constraint FK_储蓄开户_支行 foreign key (支行名字)
      references 支行 (支行名字);
      
alter table 储蓄开户 add constraint FK_储蓄开户_储蓄账户 foreign key (账户号)
      references 储蓄账户 (账户号);
      
alter table 储蓄开户 add constraint FK_储蓄开户_客户 foreign key (客户身份证号)
      references 客户 (客户身份证号);
      
alter table 支票合作 add constraint FK_支票合作_客户 foreign key (客户身份证号)
      references 客户 (客户身份证号);

alter table 支票合作 add constraint FK_支票合作_支行 foreign key (支行名字)
      references 支行 (支行名字);

alter table 储蓄合作 add constraint FK_储蓄合作_客户 foreign key (客户身份证号)
      references 客户 (客户身份证号);

alter table 储蓄合作 add constraint FK_储蓄合作_支行 foreign key (支行名字)
      references 支行 (支行名字);