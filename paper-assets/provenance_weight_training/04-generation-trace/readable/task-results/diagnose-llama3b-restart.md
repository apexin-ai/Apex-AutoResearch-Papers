# diagnose llama3b restart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama3b-restart_20260516T164454_result.json`
- **Structured JSON:** [`7ab91dc8ef8b66c9fb3e.json`](../../sessions/7a/7ab91dc8ef8b66c9fb3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：B) 从头训练（非 resume），但这是**正常的首次训练**，不是异常重跑

### 证据

**1. 进程命令行无 `--resume_from_checkpoint`**
两个进程（PID 3112 uniform, PID 4005 adaptive）的完整命令行中都没有 resume 参数。

**2. 日志显示从零开始**
- 启动时间：`2026-05-16 19:26`
- 模型从 `models/meta-llama/Llama-3.2-3B` 全新加载
- tqdm 从 `0/6103` 开始（后调整为 `/8477`）
- wandb 创建新 offline run

**3. step_metrics.jsonl 从 step 0 开始，无断层**
- uniform: 6000 行，step 0 → 1499（每 step 4 条记录，对应 gradient_accumulation_steps=4）
- adaptive: 6000 行，同样 step 0 → 1499
- 不存在"旧记录 + 新记录"的拼接痕迹，全部是本次运行产出

**4. Checkpoint 状态正常**
- 两个实验各有 checkpoint-500 和 checkpoint-1000，每个 6.1GB（符合 Llama-3.2-3B save_only_model 大小）
- checkpoint-500: May 16 ~21:36, checkpoint-1000: May 16 ~23:47（约 2 小时间隔，节奏正常）

**5. 当前进度**

| 实验 | 当前 step | 总 steps | 进度 | 速度 | 预计剩余 |
|------|----------|---------|------|------|---------|
| uniform | ~1510 | 8477 | 18% | 1.63 it/s | ~1h 11m |
| adaptive | ~1170 | 8477 | 14% | 1.64 it/s | ~1h 15m |

**注意**：训练配置显示 `max_steps=6103`，但 tqdm 实际总数为 8477——可能是脚本按实际 token 数重新计算后调整了。

### 总结

之前观察到的 "tqdm 从 step 0 开始" 是因为这本来就是首次训练，不是从已有 checkpoint resume 后又回到 0。step_metrics.jsonl 中到 step 1499 的记录就是当前运行的产出，不是旧数据。训练正常推进中，无需干预。

---
