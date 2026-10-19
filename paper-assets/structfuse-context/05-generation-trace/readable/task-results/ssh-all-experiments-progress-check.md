# ssh all experiments progress check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_all_experiments_progress_check_20260514T000504_result.json`
- **Structured JSON:** [`e7e5ade317bd9bc666d0.json`](../../sessions/e7/e7e5ade317bd9bc666d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部命令执行完毕，以下是原始输出：

---

```
=== nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total,temperature.gpu --format=csv,noheader ===
0, 100 %, 51621 MiB, 97887 MiB, 72
1, 100 %, 55187 MiB, 97887 MiB, 76
```

```
=== ps -p 73558 -o pid=,etime= (Qwen train process) ===
 73558    06:26:00
QWEN_ALIVE
```

```
=== ps -p 73544 -o pid=,etime= (Qwen parent) ===
 73544    06:26:00
QWEN_PARENT_ALIVE
```

```
=== find /root/autodl-tmp/structfuse/ -path "*qwen*" -name "checkpoint-*" -type d ===
（无输出，无 checkpoint 目录）
```

```
=== tail -50 /root/runs/m2_full_qwen/random_s42.log ===
wandb: Tracking run with wandb version 0.26.0
wandb: W&B syncing is set to `offline` in this directory. Run `wandb online` or set WANDB_MODE=online to enable cloud syncing.
wandb: Run data is saved locally in /root/autodl-tmp/structfuse/wandb_logs/wandb/offline-run-20260514_013934-pthrowuk

Loading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.87it/s]
[Epoch 1] Using pre-mined negatives (random)...
  Training loop start: 1414 batches/epoch, total_steps_per_epoch=1414
  step 50  loss=0.6716  lr=2.36e-06
  step 100  loss=0.6195  lr=4.67e-06
  step 150  loss=0.7127  lr=7.03e-06
  step 200  loss=0.6318  lr=9.34e-06
  step 250  loss=0.3339  lr=1.17e-05
  step 300  loss=0.5918  lr=1.40e-05
  step 350  loss=0.5738  lr=1.64e-05
  step 400  loss=0.2005  lr=1.87e-05
  step 450  loss=0.4374  lr=2.00e-05
  step 500  loss=0.6168  lr=2.00e-05
  [eval@500] {'val_loss': 0.486931758338973, 'recall@1': 0.5332214765100671, 'recall@5': 0.9540268456375839, 'recall@10': 1.0}
  New best val_loss=0.4869, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss
  New best R@1=0.5332, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1
  step 550  loss=0.2608  lr=1.99e-05
  step 600  loss=0.1666  lr=1.99e-05
  step 650  loss=0.2760  lr=1.98e-05
  step 700  loss=0.1415  lr=1.97e-05
  step 750  loss=0.0966  lr=1.96e-05
  step 800  loss=0.3779  lr=1.95e-05
  step 850  loss=0.1694  lr=1.94e-05
  step 900  loss=0.1534  lr=1.93e-05
  step 950  loss=0.1034  lr=1.91e-05
  step 1000  loss=0.2367  lr=1.89e-05
  [eval@1000] {'val_loss': 0.4650662785708504, 'recall@1': 0.5526845637583893, 'recall@5': 0.9593959731543624, 'recall@10': 1.0}
  New best val_loss=0.4651, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss
  New best R@1=0.5527, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1
  step 1050  loss=0.1787  lr=1.87e-05
  step 1100  loss=0.1914  lr=1.85e-05
  step 1150  loss=0.4897  lr=1.83e-05
  step 1200  loss=0.3260  lr=1.80e-05
  step 1250  loss=0.2007  lr=1.78e-05
  step 1300  loss=0.0690  lr=1.75e-05
  step 1350  loss=0.1074  lr=1.73e-05
  step 1400  loss=0.2393  lr=1.70e-05
[Epoch 2] Using pre-mined negatives (random)...
  step 1450  loss=0.0597  lr=1.67e-05
  step 1500  loss=0.1601  lr=1.63e-05
  [eval@1500] {'val_loss': 0.5364526285221113, 'recall@1': 0.5228187919463088, 'recall@5': 0.9550335570469799, 'recall@10': 1.0}
  val_loss not improved (1/0)
  step 1550  loss=0.1807  lr=1.60e-05
```

```
=== find /root/runs/ -name "*qwen*" -type f -mmin -60 ===
（无输出）
```

```
=== ps -p 76627 -o pid=,etime= (StarCoder train process) ===
 76627    05:35:21
STARCODER_ALIVE
```

```
=== ps -p 74122 -o pid=,etime= (StarCoder parent) ===
 74122    06:25:09
STARCODER_PARENT_ALIVE
```

```
=== tail -50 /root/runs/m2_full_starcoder/random_s42.log ===
wandb: Tracking run with wandb version 0.26.0
wandb: W&B syncing is set to `offline` in this directory. Run `wandb online` or set WANDB_MODE=online to enable cloud syncing.
wandb: Run data is saved locally in /root/structfuse/wandb/offline-run-20260514_023015-ov878za5
[Epoch 1] Using pre-mined negatives (random)...
  Training loop start: 1414 batches/epoch, total_steps_per_epoch=1414
  step 50  loss=0.8462  lr=2.26e-06
  step 100  loss=0.6929  lr=4.62e-06
  step 150  loss=0.5942  lr=6.93e-06
  step 200  loss=0.4387  lr=9.25e-06
  step 250  loss=0.5274  lr=1.16e-05
  step 300  loss=0.5294  lr=1.40e-05
  step 350  loss=0.3092  lr=1.63e-05
  step 400  loss=0.2138  lr=1.87e-05
  step 450  loss=0.5400  lr=2.00e-05
  step 500  loss=0.3269  lr=2.00e-05
  [eval@500] {'val_loss': 0.6194413630354324, 'recall@1': 0.43523489932885906, 'recall@5': 0.9053691275167786, 'recall@10': 1.0}
  New best val_loss=0.6194, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss
  New best R@1=0.4352, saved to /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1
  step 550  loss=0.2826  lr=2.00e-05
  step 600  loss=0.3563  lr=1.99e-05
  step 650  loss=0.6108  lr=1.98e-05
  step 700  loss=0.4037  lr=1.98e-05
  step 750  loss=0.5464  lr=1.97e-05
  step 800  loss=0.2657  lr=1.95e-05
  step 850  loss=0.3973  lr=1.94e-05
  step 900  loss=0.4681  lr=1.93e-05
  step 950  loss=0.1187  lr=1.91e-05
  step 1000  loss=0.2258  lr=1.89e-05
  [eval@1000] {'val_loss': 0.6134329466611746, 'recall@1': 0.45369127516778524, 'recall@5': 0.9201342281879195, 'recall@10': 1.0}
```

```
=== find /root/runs/ -name "*starcoder*" -type f -mmin -60 ===
/root/runs/structfuse-context/m2_full_starcoder.log
```

```
=== ps aux | grep reextract (m1_reextract_v2) ===
（多个 CodeQL 进程正在运行，正在处理 repos: pyparsing, sunpy, marshmallow, pylint-dev/astroid, deepdiff）
```

```
=== tail -30 /root/runs/structfuse-context/m1_reextract_v2.log ===
2026-05-14 08:04:22,483 [INFO] batch_extract: [seperman__deepdiff.ed252022.pr_390] CodeQL call_graph: 34 entries, 9 reachable files (threshold=1)
2026-05-14 08:04:25,554 [INFO] batch_extract: [pylint-dev__astroid.b114f6b5.combine_file__dgwjbf1g] CodeQL call_graph: 17 entries, 7 reachable files (threshold=1)
2026-05-14 08:04:29,220 [INFO] batch_extract: [pyparsing__pyparsing.533adf47.func_basic__s7sacnas] CodeQL call_graph: 47 entries, 4 reachable files (threshold=1)
2026-05-14 08:04:31,406 [INFO] batch_extract: [marshmallow-code__marshmallow.9716fc62.func_basic__od9uqzzl] CodeQL call_graph: 11 entries, 2 reachable files (threshold=1)
2026-05-14 08:04:33,538 [INFO] batch_extract: [seperman__deepdiff.ed252022.pr_403] CodeQL call_graph: 192 entries, 12 reachable files (threshold=1)
2026-05-14 08:04:38,556 [INFO] batch_extract: [pylint-dev__astroid.b114f6b5.combine_file__dju7odgi] CodeQL call_graph: 72 entries, 25 reachable files (threshold=1)
2026-05-14 08:04:41,225 [INFO] batch_extract: [pyparsing__pyparsing.533adf47.func_basic__sdd4sbt6] CodeQL call_graph: 345 entries, 9 reachable files (threshold=1)
2026-05-14 08:04:41,631 [INFO] batch_extract: [marshmallow-code__marshmallow.9716fc62.func_basic__ohgxt4f0] CodeQL call_graph: 169 entries, 9 reachable files (threshold=1)
2026-05-14 08:04:47,561 [INFO] batch_extract: [seperman__deepdiff.ed252022.pr_419] CodeQL call_graph: 0 entries, 0 reachable files (threshold=1)
2026-05-14 08:04:51,542 [INFO] batch_extract: [seperman__deepdiff.ed252022.pr_422] CodeQL call_graph: 0 entries, 0 reachable files (threshold=1)
2026-05-14 08:04:52,298 [INFO] batch_extract: [pylint-dev__astroid.b114f6b5.combine_file__du37dhzc] CodeQL call_graph: 10 entries, 2 reachable files (threshold=1)
2026-05-14 08:04:53,389 [INFO] batch_extract: [marshmallow-code__marshmallow.9716fc62.func_basic__on4io8dl] CodeQL call_graph: 176 entries, 9 reachable files (threshold=1)
2026-05-14 08:04:55,011 [INFO] batch_extract: [pyparsing__pyparsing.533adf47.func_basic__sk57zi2q] CodeQL call_graph: 68 entries, 7 reachable files (threshold=1)
2026-05-14 08:04:55,562 [INFO] batch_extract: [seperman__deepdiff.ed252022.pr_467] CodeQL call_graph: 192 entries, 12 reachable files (threshold=1)
2026-05-14 08:05:05,601 [INFO] batch_extract: [pylint-dev__astroid.b114f6b5.combine_file__e00s4dcn] CodeQL call_graph: 25 entries, 3 reachable files (threshold=1)
2026-05-14 08:05:05,906 [INFO] batch_extract: [marshmallow-code__marshmallow.9716fc62.func_basic__oou5e48o] CodeQL call_graph: 177 entries, 9 reachable files (threshold=1)
2026-05-14 08:05:08,071 [INFO] batch_extract: [pyparsing__pyparsing.533adf47.func_basic__ssrx9y5a] CodeQL call_graph: 256 entries, 9 reachable files (threshold=1)
2026-05-14 08:05:08,861 [INFO] batch_extract: [seperman__deepdiff.ed252022.pr_492] CodeQL call_graph: 153 entries, 13 reachable files (threshold=1)
2026-05-14 08:05:18,348 [INFO] batch_extract: [pylint-dev__astroid.b114f6b5.combine_file__ecw8m286] CodeQL call_graph: 168 entries, 29 reachable files (threshold=1)
2026-05-14 08:05:18,541 [INFO] batch_extract: [marshmallow-code__marshmallow.9716fc62.func_basic__orde97hx] CodeQL call_graph: 80 entries, 8 reachable files (threshold=1)
2026-05-14 08:05:21,889 [INFO] batch_extract: [seperman__deepdiff.ed252022.pr_496] CodeQL call_graph: 0 entries, 0 reachable files (threshold=1)
2026-05-14 08:05:23,075 [INFO] batch_extract: [seperman/deepdiff] cleaned up CodeQL database
2026-05-14 08:05:23,678 [INFO] batch_extract: [pyparsing__pyparsing.533adf47.func_basic__sulg4rmc] CodeQL call_graph: 84 entries, 8 reachable files (threshold=1)
2026-05-14 08:05:30,058 [INFO] batch_extract: [sunpy/sunpy] 722 pending, 0 done
2026-05-14 08:05:30,125 [INFO] batch_extract: [sunpy/sunpy] creating CodeQL database...
2026-05-14 08:05:30,130 [INFO] batch_extract: [marshmallow-code__marshmallow.9716fc62.func_basic__p1u6iqc6] CodeQL call_graph: 59 entries, 8 reachable files (threshold=1)
2026-05-14 08:05:35,465 [INFO] batch_extract: [pylint-dev__astroid.b114f6b5.combine_file__eeo3zas1] CodeQL call_graph: 1 entries, 1 reachable files (threshold=1)
2026-05-14 08:05:37,203 [INFO] batch_extract: [pyparsing__pyparsing.533adf47.func_basic__svzuu39s] CodeQL call_graph: 427 entries, 10 reachable files (threshold=1)
2026-05-14 08:05:38,954 [INFO] batch_extract: [sunpy/sunpy] CodeQL DB created
2026-05-14 08:05:42,982 [INFO] batch_extract: [marshmallow-code__marshmallow.9716fc62.func_basic__prul2ma5] CodeQL call_graph: 161 entries, 9 reachable files (threshold=1)
```

```
=== wc -l /root/autodl-tmp/structfuse/full_m1_data/all.jsonl ===
44173 /root/autodl-tmp/structfuse/full_m1_data/all.jsonl
```

```
=== find /root/autodl-tmp/structfuse/ -name "eval_*" -type f -mmin -180 ===
（无输出）
```

```
=== find /root/runs/ -name "*eval*" -type f -mmin -180 ===
（无输出）
```

```
=== ls -lt /root/structfuse-context/wandb/ ===
total 0
drwxr-xr-x 5 root root 88 May 14 02:30 offline-run-20260514_023015-ov878za5
lrwxrwxrwx 1 root root 60 May 14 02:30 debug-internal.log -> ...
lrwxrwxrwx 1 root root 51 May 14 02:30 debug.log -> ...
lrwxrwxrwx 1 root root 36 May 14 02:30 latest-run -> offline-run-20260514_023015-ov878za5
drwxr-xr-x 5 root root 88 May 14 01:00 offline-run-20260514_010017-x4vmv7bj
```

```
=== find wandb -name "wandb-summary.json" -mmin -180 ===
（无输出）
```

```
=== grep -r "Starting training" /root/runs/m2_full_qwen/ ===
（无匹配）
```

```
=== ls -lt /root/runs/m2_full_qwen/ ===
total 4
-rw-r--r-- 1 root root 2922 May 14 08:04 random_s42.log
```

```
=== ls -lt /root/runs/m2_full_starcoder/ ===
total 4
-rw-r--r-- 1 root root 1963 May 14 08:05 random_s42.log
```

---
