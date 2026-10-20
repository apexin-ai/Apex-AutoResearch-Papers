# ops gpu process inventory

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-process-inventory_20260523T140915_result.json`
- **Structured JSON:** [`c57ae0e9176b44471245.json`](../../sessions/c5/c57ae0e9176b44471245.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 进程盘点

### 当前 GPU 状态

4x NVIDIA RTX PRO 6000 Black (98GB)，全部 ~96% 利用率。**无训练进程，全部为 eval。**

| GPU | PID | 类型 | 任务描述 | 运行时间 | 进度 | 状态 |
|-----|-----|------|----------|----------|------|------|
| 0 | 142856 | eval | contam_5 mistral | ~29min | 14042/14042 | ✅ 已完成，等待链式下一任务 |
| 0 | 146513 | eval | clean_s7 (llama) | ~7min | ~25% | 进行中 |
| 1 | 143357 | eval | contam_15_s3 llama | ~29min | 14042/14042 | ✅ 已完成，等待链式下一任务 |
| 1 | 145868 | eval | clean (llama) | ~12min | ~39% | 进行中 |
| 2 | 143837 | eval | contam_50_s3 llama | ~28min | 13500/14042 | 进行中 (~96%) |
| 2 | 145368 | eval | clean_s4 (llama) | ~12min | ~43% | 进行中 |
| 3 | 141492 | eval | clean_s9 (llama) | ~34min | 13500/14042 | 进行中 (~96%) |
| 3 | 144338 | eval | contam_25_s2 llama | ~28min | 10500/14042 | 进行中 (~75%) |

### 已完成 eval 结果

| 任务 | acc_overall | acc_seen | acc_unseen | lz*_seen | lz*_unseen |
|------|------------|----------|------------|----------|------------|
| contam_5 mistral | 0.5707 | 0.7664 | 0.5604 | -2.815 | -0.722 |
| contam_15_s3 llama | 0.6584 | 0.7854 | 0.6360 | -1.378 | -3.737 |

### 链式任务队列

每个 GPU 有两条并行链：

| GPU | 链1 (contam eval) | 链2 (clean eval) |
|-----|-------------------|------------------|
| 0 | ~~contam_5 mistral~~ → **contam_5_s2 llama** | clean_s6 ✅ → **clean_s7** → clean_s8 |
| 1 | ~~contam_15_s3 llama~~ → **contam_15_s3 mistral** | ~~contam_15_s1 llama~~ → **clean** → clean_s2 |
| 2 | **contam_50_s3 llama** → contam_50_s3 mistral | clean_s3 ✅ → **clean_s4** → clean_s5 |
| 3 | **contam_25_s2 llama** → contam_5_s2 mistral | **clean_s9** → clean_s10 → contam_5 mistral |

---

### Batch 4/5 训练状态：全部完成 ✅

| Batch | 任务 | Checkpoint 路径 | 完成时间 | 最终 ckpt |
|-------|------|----------------|----------|-----------|
| 4 | Mistral 25% s1 | `checkpoints/mistral/contam_25/` | ~21:59 | checkpoint-1596 |
| 5 | Llama 5% s3 | `checkpoints/llama/contam_5_s3/` | ~21:14 | checkpoint-1071 |
| 5 | Llama 25% s3 | `checkpoints/llama/contam_25_s3/` | ~21:13 | checkpoint-1596 |
| 5 | Mistral 25% s2 | `checkpoints/mistral/contam_25_s2/` | ~21:39 | checkpoint-1596 |

注意：Mistral 25% s1 的 checkpoint 保存在 `contam_25/` 而非 `contam_25_s1/`（目录不存在）。

### 新完成的 checkpoint 路径

```
/root/autodl-tmp/ctrl_contam_pilot/checkpoints/mistral/contam_25/          # Batch 4: Mistral 25% s1
/root/autodl-tmp/ctrl_contam_pilot/checkpoints/llama/contam_5_s3/          # Batch 5: Llama 5% s3
/root/autodl-tmp/ctrl_contam_pilot/checkpoints/llama/contam_25_s3/         # Batch 5: Llama 25% s3
/root/autodl-tmp/ctrl_contam_pilot/checkpoints/mistral/contam_25_s2/       # Batch 5: Mistral 25% s2
```

---
