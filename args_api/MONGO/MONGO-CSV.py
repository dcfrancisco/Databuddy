#do not change
aa={'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'arg_6': ['-6', '--arg_6', '', 'Generic string argument 1.'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'arg_8': ['-8', '--arg_8', '', 'Generic string argument 3.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'arg_7': ['-7', '--arg_7', '', 'Generic string argument 2.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-o', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'query_sql_file': ['-q', '--query_sql_file', '', 'Input file with MongoDB query sql.'], 'from_column_names': ['-P', '--from_column_names', '', 'From column list.'], 'from_db_name': ['-b', '--from_db_name', '', 'MongoDB source database.'], 'query_sql_dir': ['-Q', '--query_sql_dir', '', 'Input dir with MongoDB query sqls.'], 'header': ['-A', '--header', '', 'Include header to MongoDB extract.'], 'from_db_port': ['-z', '--from_db_port', '', 'MongoDB source database port.'], 'from_user': ['-j', '--from_user', '', 'MongoDB source user.'], 'from_passwd': ['-x', '--from_passwd', '', 'MongoDB source user password.'], 'from_db_server': ['-n', '--from_db_server', '', 'MongoDB source instance name.'], 'from_collection': ['-c', '--from_collection', '', 'From collection.']}, {'to_file': ['-g', '--to_file', '', 'To CSV file.'], 'to_dir': ['-D', '--to_dir', '', 'To directory.']}], 'MONGO_Table_withComaHeader.CSV_File': [{'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'mongo-csv', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150601_001313_181000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'header': ('-A', '--header', 1, 'Include header to MongoDB extract.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_file': ('-g', '--to_file', 'C:\\Python27\\data_migrator_1239_mongo\\CSV_OUT\\testMONGO_Table_withComaHeader.data', 'To CSV file.')}], 'MONGO_Table_withComaHeader.CSV_Dir': [{'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'mongo-csv', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150601_001313_156000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'header': ('-A', '--header', 1, 'Include header to MongoDB extract.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_dir': ('-D', '--to_dir', 'C:\\Python27\\data_migrator_1239_mongo\\CSV_OUT', 'To directory.')}]}