USE infoset;

CREATE TABLE iset_department (
	idx_department BIGINT NOT NULL, 
	code VARBINARY(512), 
	name VARBINARY(512), 
	enabled INTEGER DEFAULT '1', 
	ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY (idx_department), 
	UNIQUE (code)
);


CREATE TABLE iset_device (
	idx_device BIGINT NOT NULL, 
	devicename VARBINARY(512), 
	description VARBINARY(512), 
	enabled INTEGER DEFAULT '1', 
	ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY (idx_device), 
	UNIQUE (devicename)
);


CREATE TABLE iset_billcode (
	idx_billcode BIGINT NOT NULL, 
	code VARBINARY(512), 
	name VARBINARY(512), 
	enabled INTEGER DEFAULT '1', 
	ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY (idx_billcode), 
	UNIQUE (code)
);



CREATE TABLE iset_agentname (
	idx_agentname BIGINT NOT NULL, 
	name VARBINARY(512), 
	enabled INTEGER DEFAULT '1', 
	ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY (idx_agentname), 
	UNIQUE (name)
);

CREATE TABLE iset_agent (
	idx_agent BIGINT NOT NULL, 
	idx_agentname BIGINT DEFAULT '1' NOT NULL, 
	id_agent VARBINARY(512), 
	enabled INTEGER DEFAULT '1', 
	ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY (idx_agent), 
	FOREIGN KEY(idx_agentname) REFERENCES iset_agentname (idx_agentname), 
	UNIQUE (id_agent)
);

CREATE TABLE iset_deviceagent (
	idx_deviceagent BIGINT NOT NULL, 
	idx_device BIGINT DEFAULT '1' NOT NULL, 
	idx_agent BIGINT DEFAULT '1' NOT NULL, 
	enabled INTEGER DEFAULT '1', 
	last_timestamp BIGINT DEFAULT '0' NOT NULL, 
	ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY (idx_deviceagent), 
	UNIQUE (idx_device, idx_agent), 
	FOREIGN KEY(idx_device) REFERENCES iset_device (idx_device), 
	FOREIGN KEY(idx_agent) REFERENCES iset_agent (idx_agent)
);

CREATE TABLE iset_datapoint (
	idx_datapoint BIGINT NOT NULL, 
	idx_deviceagent BIGINT DEFAULT '1' NOT NULL, 
	idx_department BIGINT DEFAULT '1' NOT NULL, 
	idx_billcode BIGINT DEFAULT '1' NOT NULL, 
	id_datapoint VARBINARY(512), 
	agent_label VARBINARY(512), 
	agent_source VARBINARY(512), 
	enabled INTEGER DEFAULT '1', 
	billable INTEGER DEFAULT '0', 
	timefixed_value VARBINARY(512), 
	base_type INTEGER DEFAULT '1', 
	last_timestamp BIGINT DEFAULT '0' NOT NULL, 
	ts_modified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	ts_created DATETIME DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY (idx_datapoint), 
	FOREIGN KEY(idx_deviceagent) REFERENCES iset_deviceagent (idx_deviceagent), 
	FOREIGN KEY(idx_department) REFERENCES iset_department (idx_department), 
	FOREIGN KEY(idx_billcode) REFERENCES iset_billcode (idx_billcode), 
	UNIQUE (id_datapoint)
);
