from args_api import args_api
api=args_api([('-w', '--copy_vector', 'csv2ora', 'Data copy direction.'), ('-o', '--pool_size', 1, 'Pool size.'), ('-r', '--num_of_shards', 1, 'Number of shards.'), ('-t', '--field_term', '"|"', 'Field terminator.'), ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).')], [('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\ora_data_dir', 'Input CSV directory.'), ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')], [('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Oracle database.'), ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.'), ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home bin dir.')])
	