# diagnosis exp 029b status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp_029b_status_20260518T014159_result.json`
- **Structured JSON:** [`8a3c12dc75f9c27f910c.json`](../../sessions/8a/8a3c12dc75f9c27f910c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_029b 状态：正在训练中

**旧日志 (exp_029b.log)**：之前的启动因 OOM 失败（Process 416808 占用 GPU 0 显存 29.52 GiB），模型加载阶段就崩溃了。

**当前状态**：已成功重启，正在正常训练。

| 项目 | 详情 |
|---|---|
| PID | 441471 (GPU 1) |
| 启动时间 | 09:37 (今天) |
| 总步数 | 1170 |
| 当前进度 | ~100 steps / 1170 (8.55%), epoch ≈ 0.86 |
| Loss | 0.83 → 0.11 (快速下降，正常) |
| 预计剩余 | ~50 分钟 |
| GPU | cuda:1, 30128MiB/32607MiB, 100% util |
| 磁盘 | 136G 可用，无问题 |

**同时运行**：exp_029a (3-epoch) 在 GPU 0 上 (PID 441469)，两个实验并行。

**Checkpoint 目录**：目前只有 `trainer_log.jsonl`，尚未保存模型 checkpoint（训练还在早期阶段）。

**结论**：exp_029b 从未成功启动的旧进程已失败，但已被重新启动并正在正常训练，预计约 50 分钟后完成。

---
