# status westd 41312 check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-41312-check_20260516T163749_result.json`
- **Structured JSON:** [`4276e230a6b0555b2b6e.json`](../../sessions/42/4276e230a6b0555b2b6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

**实际路径**: `/root/autodl-tmp/provenance_weight_training/output/`  
**Total steps**: 8477（所有实验 tqdm 共用）

| exp_id | server:gpu | step/total | progress | loss (last logged) | speed | ETA |
|--------|-----------|-----------|---------|-------------------|-------|-----|
| llama3b_uniform_seed42 | westd-41312:0 | 824/8477 | 9.7% | ~1.70 (unwt avg@step1499) | 1.63 it/s | ~79 min |
| llama3b_adaptive_seed42 | westd-41312:1 | 499/8477 | 5.9% | ~1.74 (unwt avg@step1499) | 1.63 it/s | ~82 min |
| hybrid_rho04_seed42 | westd-41312:2 | 7234/8477 | 85.3% | ~2.17 (unwt avg@step2499) | 3.26 it/s | ~6 min |
| hybrid_rho06_seed42 | westd-41312:3 | 7926/8477 | 93.5% | ~1.96 (unwt avg@step2499) | 3.20 it/s | ~3 min |

### 注意事项

- **llama 实验疑似近期重启**：tqdm 仅跑了 8-5 分钟（从 step 0 开始），但 step_metrics.jsonl 有此前运行到 step 1499 的记录。当前跑的是新 run。
- **hybrid 实验即将完成**：rho06 约 3 分钟后完成，rho04 约 6 分钟。
- **Eval**: 4 个实验当前均在 train 阶段，未在 eval。

### Loss 趋势

- **uniform** (step 1499 batch avg): 1.70 — 初始 step 0 约 2.18，下降约 22%
- **adaptive** (step 1499 batch avg): 1.74 (weighted loss 更高 ~2.09，因为 adaptive 上调了难样本权重)
- **hybrid_rho04** (Qwen3-0.6B): unweighted loss ~2.17@step2499 — 相比同期下降较慢
- **hybrid_rho06** (Qwen3-0.6B): unweighted loss ~1.96@step2499 — 表现优于 rho04

### GPU & 磁盘

```
GPU 0: 79%  util, 71371/97887 MiB (73%)
GPU 1: 100% util, 71371/97887 MiB (73%)
GPU 2: 100% util, 75023/97887 MiB (77%)
GPU 3: 75%  util, 75023/97887 MiB (77%)

Root:     8.7G/30G  (29% used)
Data:     48G/250G  (20% used)
```

磁盘充裕，无压力。hybrid 两个实验即将训练完成。

---
