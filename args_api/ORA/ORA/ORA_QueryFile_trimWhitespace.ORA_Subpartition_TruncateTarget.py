from args_api import args_api
api=args_api([('-w', '--copy_vector', 'ora2ora', 'Data copy direction.'), ('-o', '--pool_size', 1, 'Pool size.'), ('-r', '--num_of_shards', 1, 'Number of shards.'), ('-t', '--field_term', '"|"', 'Field terminator.'), ('-U', '--truncate_target', 1, 'Truncate target table/partition/subpartition.')], [('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\oracle_query.sql', 'Input file with Oracle query sql.'), ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for source.'), ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for source.'), ('-z', '--source_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home.'), ('-W', '--trim_whitespace', 1, 'Trim whitespace from varchar2 in "Oracle" extract.')], [('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Oracle database.'), ('-a', '--to_table', 'SCOTT.Sub_Partitioned_test_to', 'To Oracle table.'), ('-N', '--to_sub_partition', 'part_15_sp1', 'To Oracle table.'), ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home bin dir.')])
	