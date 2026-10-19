# diagnose v71 scorer only failure

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v71_scorer_only_failure_20260517T095722_result.json`
- **Structured JSON:** [`ca8006450fb5bee04421.json`](../../sessions/ca/ca8006450fb5bee04421.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**两个实验均正常完成，cron EXIT_CODE=127 是误报。**

### 根因

Cron wrapper 脚本中 `python3` 不在 PATH 中（`bash: line 1: python3: command not found`），导致 wrapper 本身立即失败并报 EXIT_CODE=127。但训练是通过其他方式启动的（可能是 tmux 或手动 nohup），日志写到了 `v71_seed1.log` / `v71_seed2.log`（而非 `acib_v71_scorer_only_*.log`），训练本身完全不受 wrapper 失败影响。

### 训练完成确认

两个 seed 日志末尾均有 `Training complete: 20000 steps in 3.1h`，checkpoint-20000 已保存。

### 最终 Metrics（Step 20000）

| Metric | Seed 1 | Seed 2 |
|---|---|---|
| loss | 0.3170 | 0.3493 |
| task_loss | 0.1973 | 0.1701 |
| ib_loss | 0.3881 | 0.3579 |
| div_loss | -0.2754 | -0.2793 |
| ctr_loss | 1.2840 | 1.8565 |
| β | 0.0100 | 0.0100 |
| scorer_mean | 0.426 | 0.467 |
| scorer_std | 0.318 | 0.348 |

### Checkpoint 信息

| | Seed 1 | Seed 2 |
|---|---|---|
| 路径 | `/root/autodl-tmp/acib_v7.1_scorer_only_seed1/checkpoint-20000/` | `/root/autodl-tmp/acib_v7.1_scorer_only_seed2/checkpoint-20000/` |
| 大小 | 867M（单文件 `checkpoint.pt` = 908,369,429 bytes） | 867M（同） |
| Checkpoints | 5000, 10000, 15000, 20000 | 5000, 10000, 15000, 20000 |

注：checkpoint 867MB 偏大（scorer 只有 123K params），可能包含了完整 base model state 或 optimizer state。如果后续只需 scorer 权重，加载时可以只提取 scorer 部分。

---
