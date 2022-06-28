# drop procedure if exists check_status;

Delimiter  //
create procedure check_status(OUT num int)
begin
	declare num1 int default 0;
    declare num2 int default 0;
    select count(*) from Book where status=0 and ID in
    (select book_ID from Borrow where Return_Date is null) into num1;
    
    select count(*) from Book where status=1 and ID not in
    (select book_ID from Borrow where Return_Date is null) into num2;
    
    set num=num1+num2;
end  //
Delimiter ;

call check_status(@num);
select @num;