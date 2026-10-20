# diagnose cuda0 conflict

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cuda0_conflict_20260521T184240_result.json`
- **Structured JSON:** [`026d57b9ccb00fa791ab.json`](../../sessions/02/026d57b9ccb00fa791ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 进程状态

| 任务 | 父 PID | 子 PID | 状态 | 运行时间 |
|------|--------|--------|------|---------|
| test_eval_4b_sft_s42 | 126048 | 126054 | **存活** | ~7.5 min |
| retrain_4b_rsft_ced_s42 | 126855 | 126860 | **存活** | ~2 min |

### cuda:0 占用情况

GPU 0 (`GPU-37d3...`) 显存占用 **79,265 MiB / 97,887 MiB (81%)**，有 **3 个进程**同时在上面：

| PID | 显存占用 | 归属 |
|-----|---------|------|
| 126054 | 9,400 MiB | test_eval_4b_sft_s42（eval 推理） |
| 126539 | 34,944 MiB | **未知进程**（非这两个任务的子进程） |
| 126860 | 34,902 MiB | retrain_4b_rsft_ced_s42（RSFT 训练） |

### test_eval_4b_sft_s42 状态

目前**正常运行中**，已完成 13/500 条推理（~3%），速度约 30-45s/it。但 cuda:0 已用 81%，显存压力极大——eval 目前只占 9.4GB，随着推理进行如果峰值显存增加，有 OOM 风险。

### retrain_4b_rsft_ced_s42 状态

**正在 cuda:0 上训练**，已完成 12/510 步（~2%），占用 34.9GB。这是未授权任务，且违反了 **C001**（eval 需要接近全部显存）和 **C002/C003**（未隔离 GPU）。

### 结论

- **cuda:0 被三个进程共享**，总占用 ~79GB/98GB，极度拥挤
- retrain (PID 126860) 占 34.9GB，是 eval OOM 的最大风险源
- PID 126539 也占 34.9GB，需要确认身份
- **建议 kill retrain (PID 126855/126860)**，同时排查 PID 126539 的身份，释放 cuda:0 给 eval 使用

---
