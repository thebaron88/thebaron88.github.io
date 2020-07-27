create table if not exists types
(
    type INTEGER not null primary key autoincrement,
    name STRING not null unique,
    image STRING not null
);

create table if not exists batches
(
	batch INTEGER not null primary key autoincrement,
	type INTEGER not null references types,
	expiry TIMESTAMP not null
);

create table if not exists cans
(
	can INTEGER not null primary key autoincrement,
	batch INTEGER not null references batches
);