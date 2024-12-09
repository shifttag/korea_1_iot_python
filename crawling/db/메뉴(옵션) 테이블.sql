#--------------------<< DDL >>----------------------
truncate table menu_detail_tb;
truncate table menu_tb;
truncate table option_detail_tb;
truncate table option_tb;
truncate table order_detail_tb;
truncate table order_detail_option_tb;
truncate table order_detail_tb;
truncate table order_tb;


insert into menu_tb values
(default, '아메리카노', 4500),
(default, '라떼', 5000),
(default, '프라푸치노', 6500),
(default, '카푸치노', 5500);

insert into option_tb values
(default, '온도'),
(default, '사이즈'),
(default, '샷추가');

insert into option_detail_tb values
(default, 1, 'H', 0),
(default, 1, 'I', 500),
(default, 2, 'T', 0),
(default, 2, 'G', 500),
(default, 2, 'V', 1000),
(default, 3, '1샷', 500),
(default, 3, '2샷', 1000),
(default, 3, '3샷', 1500);

insert into menu_detail_tb values
(default, 1, 1, 1),
(default, 1, 2, 2),
(default, 1, 3, 3),
(default, 2, 1, 1),
(default, 2, 2, 2),
(default, 3, 2, 1),
(default, 4, 2, 1),
(default, 4, 3, 2);

insert into order_tb values
(default, 1, now(), 1),
(default, 2, now(), 1);

insert into order_detail_tb values
(default, 1, 1),
(default, 1, 1),
(default, 2, 1),
(default, 2, 2),
(default, 2, 3),
(default, 2, 4);

insert into order_detail_option_tb values
(default, 1, 2),
(default, 1, 3),
(default, 1, 7),
(default, 2, 1),
(default, 2, 4),
(default, 2, 6),
(default, 3, 3),
(default, 3, 6),
(default, 4, 2),
(default, 4, 4),
(default, 5, 4),
(default, 6, 5),
(default, 6, 6);

#--------------------<< DML >>----------------------

select * from menu_tb;
select * from menu_detail_tb;	# 연결 부분 (메뉴, 옵션)
select * from option_tb;
select * from option_detail_tb;	# 연결과 동시에 값 (옵션)
select * from order_detail_tb;	# 연결 부분 (주문, 메뉴)
select * from order_detail_option_tb;	# 연결 부분 (주문 상세, 옵션 상세)
select * from order_tb;

select
   mt.menu_id,
    mt.menu_name,
    mt.menu_price,
    mdt.option_id,
    mdt.option_sequence,
    ot.option_name,
    odt.option_detail_id,
    odt.option_detail_name,
    odt.option_detail_price
from
   menu_tb mt
    left outer join menu_detail_tb mdt on(mdt.menu_id = mt.menu_id)
    left outer join option_tb ot on(ot.option_id = mdt.option_id)
    left outer join option_detail_tb odt on(odt.option_id = ot.option_id)
order by
   menu_id,
   option_sequence,
    option_detail_id;
    

with menu_price_total_vtb as (
	select
		ot.order_id,
        sum(mt.menu_price) as menu_price_total
	from
		order_tb ot
		left outer join order_detail_tb odt on(odt.order_id = ot.order_id)
		left outer join menu_tb mt on(mt.menu_id = odt.menu_id)
	group by
		ot.order_id
), option_detail_price_total_vtb as (
	select
		ot.order_id,
		sum(opdt.option_detail_price) as option_detail_price_total
	from
		order_tb ot
		left outer join order_detail_tb odt on(odt.order_id = ot.order_id)
		left outer join order_detail_option_tb odot on(odot.order_detail_id = odt.order_detail_id)
		left outer join option_detail_tb opdt on(opdt.option_detail_id = odot.option_detail_id)
	group by
		ot.order_id
)
# select
# 	*
# from
# 	order_tb ot
# 	left outer join order_detail_tb odt on(odt.order_id = ot.order_id)
# 	left outer join menu_tb mt on(mt.menu_id = odt.menu_id)
# 	left outer join order_detail_option_tb odot on(odot.order_detail_id = odt.order_detail_id)
# 	left outer join option_detail_tb opdt on(opdt.option_detail_id = odot.option_detail_id)
select
 	*, 
    mptv.menu_price_total + odptv.option_detail_price_total as total_price
from
	order_tb ot
    left outer join menu_price_total_vtb mptv on(mptv.order_id = ot.order_id)
    left outer join option_detail_price_total_vtb odptv on(odptv.order_id = ot.order_id)
	left outer join order_detail_tb odt on(odt.order_id = ot.order_id)
	left outer join menu_tb mt on(mt.menu_id = odt.menu_id)
	left outer join order_detail_option_tb odot on(odot.order_detail_id = odt.order_detail_id)
	left outer join option_detail_tb opdt on(opdt.option_detail_id = odot.option_detail_id);
