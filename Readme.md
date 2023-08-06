# HLA 9. MySQL InnoDB compare performance 

## Home work: 
InnoDB Indexes </br>
Use MySQL (or fork) with InnoDB </br>
Make a table for 40M users </br>
Compare performance of selections by date of birth: </br>
Without index </br>
With BTREE index </br>
With HASH index </br>
Check insert speed difference with different innodb_flush_log_at_trx_commit value and different ops per second </br>

## Application Description

## Task 1. Compare performance of selections by date of birth column

Inputs:
MySQL DB table on 40 mln rows

| Number or Rows |Selection W/O Index |Selection with HASH Index| Selection with BTREE Index  |
| --- | --- | --- | --- |
| 0.1% rows | 13455 - 13715 ms | 107-316 ms | 13758- 13589 ms  |
| 1 % rows | 17282 - 16613  | 1504-2263 ms | 12445-16679 ms  |
| 10 % rows | 23282 - 24469 ms | 23309 -24299 ms | 23773 - 24183 ms |
| 54 % rows | > 48 sec | > 51 sec | > 50 sec |

## Task 2. Insertion speed difference with different innodb_flush_log_at_trx_commit 
Simple Python code in app.py allow to insert multi rows in parallel into <b>users_with_hash_index</b> table in MySQL DB

###  Table with result of testing

| Input Settings| innodb_flush_log_at_trx_commit | Value = 1 (seconds)  | Value = 0 (seconds) | Value = 2 (seconds) |
| -- | -- | -- | -- | -- |
| Number of rows: 10000 </br> Number of threads:  5 |  | 40 | 31 | 33 |
| Number of rows: 15000 </br> Number of threads:  10 |  | 43 | 35 | 39 |

### Details of execution
- innodb_flush_log_at_trx_commit = 1 
Start time:  20:53:52.803100
num_users:  10000
num_threads:  5
End time:  20:54:32.308742
Duration, Sec:  40

- innodb_flush_log_at_trx_commit = 0
Start time:  21:07:30.009320
num_users:  10000
num_threads:  5
End time:  21:08:01.226900
Duration, Sec:  31

- innodb_flush_log_at_trx_commit = 2
Start time:  21:10:16.612205
num_users:  10000
num_threads:  5
End time:  21:10:49.867466
Duration, Sec:  33


- innodb_flush_log_at_trx_commit = 1
Start time:  21:17:36.405386
num_users:  15000
num_threads:  10
End time:  21:20:29.658613
Duration, Sec:  43

- innodb_flush_log_at_trx_commit = 0
Start time:  21:22:28.750501
num_users:  15000
num_threads:  10
End time:  21:23:04.296565
Duration, Sec:  35

- innodb_flush_log_at_trx_commit = 2
Start time:  21:17:50.304385
num_users:  15000
num_threads:  10
End time:  21:18:29.842787
Duration, Sec:  39