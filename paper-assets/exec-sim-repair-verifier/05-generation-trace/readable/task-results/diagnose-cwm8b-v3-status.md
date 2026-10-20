# diagnose cwm8b v3 status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cwm8b-v3-status_20260516T011031_result.json`
- **Structured JSON:** [`2fcc31eec2cb3ad17031.json`](../../sessions/2f/2fcc31eec2cb3ad17031.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### PID 443216：**存活，正常运行**
- 已运行 24 分钟，进程是 submit_training_job 的 bash wrapper
- 实际 eval 子进程 PID 443221（`python3 eval_repo_cwm.py`），CPU 102%，正常推理中

### 进度
- **5480 / 9784** 样本已完成（56%）
- 其中 5287 条是从之前增量恢复的，新跑了 193 条
- running_acc ≈ 60.1%（新样本上的准确率）
- 每 batch（8 条）约 57 秒，预计剩余 ~50 分钟完成

### GPU 占用

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 17609/32607 MiB | 77% | cls8b eval (ckpt1000 mutation) |
| 1 | 17609/32607 MiB | 74% | cls8b eval (ckpt1000 mutation, resume) |
| 2 | 29273/32607 MiB | 96% | train_repo_cwm.py (继续训练 ckpt-6100) |
| 3 | 21133/32607 MiB | 92% | **cwm8b-ckpt400-test-eval-v3** ← 本任务 |

### 其他 eval 进程
- `eval_repo_cls.py` × 2（GPU 0 和 1，cls8b_s42 checkpoint-1000 test mutation）
- `train_repo_cwm.py` × 1（GPU 2，从 checkpoint-6100 继续训练）

### 结论
进程正常运行，registry 状态卡在 ALLOCATED 可能是 agent-ml 框架未轮询到 exit code 文件（进程还没结束所以 exit 文件不存在）。无需干预。

---
