# diagnose v71 scorer only failed

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v71_scorer_only_failed_20260517T095725_result.json`
- **Structured JSON:** [`78c3c081566d57ffbe03.json`](../../sessions/78/78c3c081566d57ffbe03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 训练状态：两个实验均正常完成 20000 步

| | seed1 (GPU 0) | seed2 (GPU 1) |
|---|---|---|
| 状态 | ✅ 完成 | ✅ 完成 |
| 耗时 | 3.1h | 3.1h |
| Checkpoints | 5000/10000/15000/20000 | 5000/10000/15000/20000 |

### 最终指标 (Step 20000)

| 指标 | seed1 | seed2 |
|---|---|---|
| total loss | 0.3170 | 0.3493 |
| task_loss | 0.1973 | 0.1701 |
| ib_loss | 0.3881 | 0.3579 |
| div | -0.2754 | -0.2793 |
| ctr_loss | 1.2840 | 1.8565 |
| scorer_mean | 0.426 | 0.467 |
| scorer_std | 0.318 | 0.348 |

**Probe A/B**: 无。日志中没有 Eval/Probe 输出（虽然 config 有 eval_freq=2000，但实际训练脚本未执行 eval 步骤）。

### Checkpoint 路径
- `/root/autodl-tmp/acib_v7.1_scorer_only_seed1/checkpoint-20000/checkpoint.pt` (866MB)
- `/root/autodl-tmp/acib_v7.1_scorer_only_seed2/checkpoint-20000/checkpoint.pt` (866MB)

### EXIT_CODE=127 根因

**Cron wrapper 误报，与训练无关。**

Wrapper 的 `.log` 文件 (`acib_v71_scorer_only_seed1.log`) 仅含 2 行：
```
bash: line 1: python3: command not found
EXIT_CODE=127
```

训练实际输出在 `v71_seed1.log` / `v71_seed2.log`。训练进程正常结束后，cron wrapper 尝试调用 `python3`（可能是 post-training 回调脚本），但当前环境中 `python3` 不在 PATH 上（需通过 conda/venv 激活），导致 exit code 127。训练本身已成功完成且 checkpoint 完整。

---
