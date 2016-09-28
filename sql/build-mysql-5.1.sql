-- For MySQL 5.1

CREATE TABLE IF NOT EXISTS users (
	id		SERIAL PRIMARY KEY,
	user_id		VARCHAR(30) NOT NULL UNIQUE,
	password	VARCHAR(50), -- sha hex digest of password with 10 digits of salt
	surname		VARCHAR(255),
	first_name	VARCHAR(255)
) ENGINE=InnoDB CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS machines (
	id		SERIAL PRIMARY KEY,
	name		VARCHAR(10) NOT NULL UNIQUE,
	description	TEXT NOT NULL
) ENGINE=InnoDB CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS user_machines (
	id		SERIAL PRIMARY KEY,
	user_id		BIGINT UNSIGNED NOT NULL,
	machine_id	BIGINT UNSIGNED NOT NULL,
	settings	TEXT,
	enabled		ENUM('y','n') NOT NULL DEFAULT 'y', 
	UNIQUE KEY (user_id, machine_id),
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (machine_id) REFERENCES machines(id)
) ENGINE=InnoDB CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS sessions (
	id		SERIAL PRIMARY KEY,
	user_id		BIGINT UNSIGNED NOT NULL,
	started		DATETIME NOT NULL,
	duration	TIME NOT NULL DEFAULT '00:00',
	notes		TEXT,
	FOREIGN KEY (user_id) REFERENCES users(id)
) ENGINE=InnoDB CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS session_results (
	id		SERIAL PRIMARY KEY,
	session_id	BIGINT UNSIGNED NOT NULL,
	user_machine_id	BIGINT UNSIGNED NOT NULL,
	loading		INT UNSIGNED,
	duration	INT UNSIGNED,
	FOREIGN KEY (session_id) REFERENCES sessions(id),
	FOREIGN KEY (user_machine_id) REFERENCES user_machines(id)
) ENGINE=InnoDB CHARACTER SET 'utf8';

-- End
