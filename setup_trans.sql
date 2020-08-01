create table if not exists transactions
(
	can INTEGER not null,
	price INTEGER not null,
	description STRING not null,
	status INTEGER not null,
	timestamp TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP
);