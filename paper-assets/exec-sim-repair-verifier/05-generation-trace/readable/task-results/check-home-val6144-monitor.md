# check home val6144 monitor

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-val6144-monitor_20260514T113458_result.json`
- **Structured JSON:** [`2fe4e7c7d881905c29ee.json`](../../sessions/2f/2fe4e7c7d881905c29ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下：

---

## 进度状态

**val_6144 当前：** 正在跑 `seed123_home/checkpoint-400`，进度 800/9335（~8.6%），started at 04:32 PDT。

**已完成的前置任务：** `val_sweep`（val set, seq_len=2048）已全部完成，结果在 `val_eval_results/`。

## val_sweep 结果（val set, max_seq_length=2048）

### seed123_home checkpoints

| Checkpoint | accuracy | f1_macro | f1_fail | f1_pass | recall_fail | n_unparseable |
|------------|----------|----------|---------|---------|-------------|---------------|
| 200 | 62.51 | 55.54 | 37.94 | 73.14 | 47.51 | 1883 |
| 400 | 80.72 | **67.03** | 45.78 | 88.27 | 33.75 | 1883 |
| 600 | 76.78 | 66.81 | 48.63 | 85.00 | 45.56 | 1883 |
| 800 | 81.81 | **69.14** | 49.37 | 88.91 | 36.77 | 1883 |
| 1000 | 82.30 | 67.63 | 45.84 | 89.42 | 31.04 | 1883 |

另外还有 `repo_cls_home/ckpt-200`（非seed123）：f1_macro=**70.93**

### Val (seq_len=2048) ranking by f1_macro:
**ckpt-800 (69.14) > ckpt-1000 (67.63) > ckpt-400 (67.03) > ckpt-600 (66.81) > ckpt-200 (55.54)**

### 对比 test set (seq_len=2048) ranking:
**ckpt-600 (77.31) > ckpt-400 (67.47) > ckpt-800 (66.03) > ckpt-1000 (52.10)**

## 关键发现

**Val 和 test 的 ranking 不一致！** Test 上 ckpt-600 最佳，val 上 ckpt-800 最佳。

**可疑：val set unparseable 高达 1883/9335 (20.2%)**，而 test set 只有 132/9784 (1.3%)。这极可能是 seq_len=2048 截断导致，正是 val_6144 要验证的——seq_len=6144 应该能大幅降低 unparseable 率，获得更可靠的 val ranking。

## ETA

- 推理速度：~200 samples/min（batch_size=4, 6144 seq_len）
- **ckpt-400 完成 ETA：~05:19 PDT**（还剩 ~43 min）
- **ckpt-600 完成 ETA：~06:06 PDT**（再 ~47 min）
- **总完成 ETA：~06:06 PDT（约1.5小时后）**

---
