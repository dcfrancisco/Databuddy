from args_api import args_api
api=args_api([('-w', '--copy_vector', 'ora2ora', 'Data copy direction.'), ('-o', '--pool_size', 1, 'Pool size.'), ('-r', '--num_of_shards', 1, 'Number of shards.'), ('-t', '--field_term', '"|"', 'Field terminator.'), ('-U', '--truncate_target', 1, 'Truncate target table/partition/subpartition.')], [('-c', '--from_table', 'SCOTT.Sub_Partitioned_test_from', 'From table.'), ('-S', '--from_sub_partition', 'part_15_sp1', 'From sub-partition.'), ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for source.'), ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for source.'), ('-z', '--source_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home.')], [('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Oracle database.'), ('-a', '--to_table', 'SCOTT.Partitioned_test_to', 'To Oracle table.'), ('-G', '--to_partition', 'part_15', 'To Oracle table.'), ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home bin dir.')])
	