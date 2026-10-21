# check home val sweep progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-val-sweep-progress_20260514T061451_result.json`
- **Structured JSON:** [`4921c5391edc8964814d.json`](../../sessions/49/4921c5391edc8964814d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

### GPU 状态
- GPU 0 (RTX 5090): **100% 使用率**，17.8GB/32.6GB 显存，PID 3046727 (python3)
- 无冲突 — ckpt-4600 test eval 已完成，当前 GPU 被 val sweep 独占

### Val Sweep 进度
- **正在跑第 1 个 checkpoint**: `checkpoint-200`，进度 1440/9335 (~15%)
- 已完成 val eval 结果: **0 个**（`val_eval_results/` 目录为空）
- 按当前速度 (~28s/160 samples)，单个 checkpoint 约需 **27 分钟**，10 个 checkpoint 总计约 **4.5 小时**
- 当前 running_acc = 63.5%（checkpoint-200 表现较差，符合预期——早期 checkpoint）

### ckpt-4600 Test Eval 结果 (已完成)
| 指标 | 值 |
|------|-----|
| **accuracy** | **82.35%** |
| **f1_macro** | **74.74** |
| **f1_fail** | **60.87** |
| f1_pass | 88.60 |
| precision_fail | 76.00 |
| recall_fail | 50.76 |
| majority baseline | 72.96% |
| gap vs majority | +9.39pp |
| n_instances | 9784 (test) |
| unparseable | 132 |

### `--split` 修改验证
- `eval_repo_cls.py` 第 245 行: `--split` 参数已正确实现，choices=["val", "test"]，default="test"
- 数据路径模板: `swebench_{args.split}.jsonl`
- val 日志确认加载了 `swebench_val.jsonl`，9335 条样本（label: 2252 fail / 7083 pass）

### Val 数据文件
- `/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_val.jsonl` — **9335 行**，确认存在

### 总结
Val sweep 刚启动，正在跑第一个 checkpoint (checkpoint-200)，预计全部完成需约 4.5 小时。ckpt-4600 test eval 已出结果，accuracy 82.35%，f1_macro 74.74，f1_fail 60.87。无 GPU 冲突，无报错。

---
