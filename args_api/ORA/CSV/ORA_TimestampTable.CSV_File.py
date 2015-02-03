from args_api import args_api
api=args_api([('-w', '--copy_vector', 'ora2csv', 'Data copy direction.'), ('-o', '--pool_size', 1, 'Pool size.'), ('-r', '--num_of_shards', 1, 'Number of shards.'), ('-t', '--field_term', '"|"', 'Field terminator.')], [('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.'), ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), ('-e', '--nls_date_format', '"YYYY/MM/DD"', 'nls_date_format for source.'), ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for source.'), ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for source.'), ('-z', '--source_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home.')], [('-g', '--to_file', 'c:\\Python27\\data_migrator_1239\\CSV_OUT\\testORA_TimestampTable.data', 'To CSV file.')])
	