# (1)
select ID, address from Reader where name='Rose';
# (2)
select Book.name, Borrow_Date from Book,Reader,Borrow
where Book.ID=Borrow.book_ID and Reader.ID=Borrow.Reader_ID and Reader.name='Rose';
# (3)
select name from Reader where Reader.ID NOT IN (select distinct Reader_ID from Borrow);
# (4)
select name, price from Book where author='Ullman';
# (5)
select Book.ID, Book.name from Book,Reader,Borrow
where Book.ID=Borrow.book_ID and Reader.ID=Borrow.Reader_ID
and Reader.name='李林' and Borrow.Return_Date is NULL;
# (6)
select name from Reader,Borrow
where Reader.ID=Borrow.Reader_ID group by Reader.ID having count(Book_ID)>3;
# (7)
select name, ID from Reader where NOT exists(
	select * from Borrow where Reader.ID=Borrow.Reader_ID
    and book_ID in(
		select book_ID from Reader, Borrow where Reader.ID=Borrow.Reader_ID
        and Reader.name='李林'
    )
);
# (8)
select name,ID from Book where name like '%MySQL%';
# (9)
select Reader.ID, Reader.name, age, count(book_ID) as count 
from Book,Reader,Borrow
where Book.ID=Borrow.book_ID and Reader.ID=Borrow.Reader_ID
and Borrow_Date like "2021%" 
group by Reader.ID
order by count DESC limit 20;
# (10)
drop view b_view;
Create view b_view(reader_ID,reader_name,book_ID,book_name,borrow_date)
as select Reader.ID,Reader.name,Book.ID,Book.name,Borrow_date
from Book,Reader,Borrow
where Book.ID=Borrow.book_ID and Reader.ID=Borrow.Reader_ID;

select reader_ID,count(distinct book_ID) from b_view
where b_view.borrow_date>date_sub(now(),interval 1 year) 
group by reader_ID;
