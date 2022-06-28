drop trigger if exists update_status1;
drop trigger if exists update_status2;

Delimiter  //
create trigger update_status1 after insert on Borrow for each row
begin
	update Book set status=1 where ID=new.book_ID;
end  //

create trigger update_status2 after update on Borrow for each row
begin
	if new.Return_Date is not null then
		update Book set status=0 where ID=new.book_ID and status=1;
	end if;
end  //
Delimiter ;

select * from Book;
insert into Borrow value('b1','r5', '2021-08-12', NULL);
select * from Book;
update Borrow set Return_Date='2021-08-12' where book_ID='b7' and Reader_ID='r2';
select * from Book;