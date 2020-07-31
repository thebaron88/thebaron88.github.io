create table if not exists transactions
(
	can INTEGER not null,
	price INTEGER not null,
	transid STRING not null,
	timestamp TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP
);