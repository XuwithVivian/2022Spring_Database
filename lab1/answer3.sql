# drop procedure if exists update_book_ID;

Delimiter //
create procedure update_book_ID(IN old_ID char(8),IN new_ID char(8),OUT state int)
begin
	declare s int default 1;
    declare count1 int default 0;
    declare count2 int default 0;
	declare b_name varchar(10);
	declare b_author varchar(10);
    declare b_price float;
    declare b_status int;
    declare continue handler for not found set s=2;
    declare continue handler for sqlexception set s=3;
    # declare continue handler for 1062 set s=4;
    start transaction;
    select count(Book.ID) from Book where Book.ID=old_ID into count1;
    if count1>0 then
		select name,author,price,status into b_name,b_author,b_price,b_status from Book where ID=old_ID;
        insert into Book value(new_ID,b_name,b_author,b_price,b_status);
    else
		set s=0;
	end if;
	select count(Borrow.book_ID) from Borrow where Borrow.book_ID=old_ID into count2;
    if count2>0 then
		update borrow set book_ID=new_ID where book_ID=old_ID;
    end if;
    delete from Book where ID=old_ID;
    if s=1 then
		set state=1;
        commit;
	else
		set state=s;
		rollback;
	end if;
end  //
Delimiter ;

call update_book_ID('b11','b20',@state);
select @state;
select * from Book;
# select * from Borrow;