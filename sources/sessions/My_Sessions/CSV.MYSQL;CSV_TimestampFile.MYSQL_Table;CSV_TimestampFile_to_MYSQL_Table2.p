(lp0
VCSV_TimestampFile_to_MYSQL_Table2
p1
a(lp2
S'CSV'
p3
aS'MYSQL'
p4
aaVCSV_TimestampFile.MYSQL_Table
p5
a(lp6
(dp7
S'lame_duck'
p8
(lp9
S'-l'
p10
aS'--lame_duck'
p11
aV0
p12
aS'Limit rows (lame duck run).'
p13
asS'field_term'
p14
(lp15
S'-t'
p16
aS'--field_term'
p17
aV,
p18
aS'Field terminator.'
p19
asS'num_of_shards'
p20
(lp21
S'-r'
p22
aS'--num_of_shards'
p23
aI1
aS'Number of shards.'
p24
asS'pool_size'
p25
(lp26
S'-ps'
p27
aS'--pool_size'
p28
aI1
aS'Pool size.'
p29
asS'debug_level'
p30
(lp31
S'-dbg'
p32
aS'--debug_level'
p33
aI1
aS'QC Debug level.'
p34
asS'copy_vector'
p35
(lp36
S'-w'
p37
aS'--copy_vector'
p38
aS'CSV-MYSQL'
p39
aS'Data copy direction.'
p40
asS'keep_data_file'
p41
(lp42
S'-K'
p43
aS'--keep_data_file'
p44
aI1
aS'Keep data dump.'
p45
asS'time_stamp'
p46
(lp47
S'-Y'
p48
aS'--time_stamp'
p49
aV20160603_134617_866000
p50
aS'Timestamp (log_dir/job_name/timestamp).'
p51
asS'log_dir'
p52
(lp53
S'-M'
p54
aS'--log_dir'
p55
aS'C:\\Temp\\qc_log'
p56
aS'Log destination.'
p57
asS'job_name'
p58
(lp59
S'-B'
p60
aS'--job_name'
p61
aS'qc_job'
p62
aS'Job name (log_dir/job_name).'
p63
asS'host_map'
p64
(lp65
S'-5'
p66
aS'--host_map'
p67
aVC:\u005cUsers\u005calex_buz\u005cDocuments\u005cGitHub\u005cDataBuddy\u005csources\u005csessions\u005cMy_Sessions\u005cCSV_TimestampFile_to_MYSQL_Table2\u005chost_map\u005chost_map.py
p68
aS'Host-to-shard map.'
p69
asa(dp70
S'input_files'
p71
(lp72
S'-i'
p73
aS'--input_files'
p74
aVC:\u005cPython35-32\u005cPROJECTS\u005cMySQL2Redshift\u005cCrime.csv
p75
aS'Input CSV file(s).'
p76
asa(dp77
S'to_db_name'
p78
(lp79
S'-d'
p80
aS'--to_db_name'
p81
aS'test'
p82
aS'Target database.'
p83
asS'target_client_home'
p84
(lp85
S'-Z'
p86
aS'--target_client_home'
p87
aS'"C:\\Temp\\mysql\\bin"'
p88
aS'Path to mysql client home.'
p89
asS'to_user'
p90
(lp91
S'-u'
p92
aS'--to_user'
p93
aS'alex'
p94
aS'Target MySQL db user.'
p95
asS'to_passwd'
p96
(lp97
S'-p'
p98
aS'--to_passwd'
p99
aS'mysql_pwd'
p100
aS'Target db user password.'
p101
asS'to_db_server'
p102
(lp103
S'-s'
p104
aS'--to_db_server'
p105
aS'localhost'
p106
aS'Target db instance name.'
p107
asS'to_table'
p108
(lp109
S'-a'
p110
aS'--to_table'
p111
aVcrime_test
p112
aS'Target table.'
p113
asaa.