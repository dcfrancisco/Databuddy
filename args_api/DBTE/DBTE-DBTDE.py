#do not change
aa={'DBTE_QueryFile.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_434000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'query_sql_file': ('-q', '--query_sql_file', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Express query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_QueryDir.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_450000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Express query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_ShardedTable_Limit65.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 65, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_436000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_ParallelQueryDir.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_439000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Express query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'debug_level': ['-dbg', '--debug_level', '', 'QC Debug level.'], 'spool_type': ['-6', '--spool_type', '', 'Spool file type (CSV or JSON).'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-o', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'query_sql_file': ['-q', '--query_sql_file', '', 'Input file with DB2 Express query sql.'], 'from_db_name': ['-b', '--from_db_name', '', 'DB2 Express source database.'], 'from_partition': ['-P', '--from_partition', '', 'From partition.'], 'from_table': ['-c', '--from_table', '', 'From table.'], 'source_client_home': ['-z', '--source_client_home', '', 'Path to DB2 Express client home.'], 'from_user': ['-j', '--from_user', '', 'DB2 Express source user.'], 'from_passwd': ['-x', '--from_passwd', '', 'DB2 Express source user password.'], 'from_db_server': ['-n', '--from_db_server', '', 'DB2 Express source instance name.'], 'query_sql_dir': ['-Q', '--query_sql_dir', '', 'Input dir with DB2 Express query files sql.']}, {'to_db_name': ['-d', '--to_db_name', '', 'Target DB2 Developer Edition database.'], 'target_client_home': ['-Z', '--target_client_home', '', 'Path to DB2 Developer Edition client home bin dir.'], 'skip_rows': ['-k', '--skip_rows', '', 'Header size. Number of rows to skip in input file.'], 'to_user': ['-u', '--to_user', '', 'Target DB2 Developer Edition db user.'], 'to_passwd': ['-p', '--to_passwd', '', 'Target DB2 Developer Edition db user password.'], 'to_db_server': ['-s', '--to_db_server', '', 'Target DB2 Developer Edition db instance name.'], 'to_table': ['-a', '--to_table', '', 'Target DB2 Developer Edition table.']}], 'DBTE_ShardedQueryFile.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_447000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'query_sql_file': ('-q', '--query_sql_file', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Express query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_Table.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_441000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_Table_KeepSpoolFile.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_437000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_Partition_Limit30.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 30, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_443000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_ParallelQueryDir_Limit10.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_444000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Express query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_Partition.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_449000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_QueryFile_Limit10.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_440000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'query_sql_file': ('-q', '--query_sql_file', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Express query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_ShardedTable.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_456000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_ShardedPartition_Limit50.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 50, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_454000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_ShardedPartition.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_446000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTE_QueryDir_Limit10.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'dbte-dbtde', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150629_212728_451000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Express query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}]}