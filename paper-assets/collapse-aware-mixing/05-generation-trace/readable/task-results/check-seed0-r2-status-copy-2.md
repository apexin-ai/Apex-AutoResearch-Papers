# check seed0 r2 status

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed0_r2_status_20260514T035612_result.json`
- **Structured JSON:** [`fda7041d42457c36df01.json`](../../sessions/fd/fda7041d42457c36df01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告：mvp_seed0_replication_r2

### 当前状态：**运行中** — G0 generation 阶段

| 阶段 | 状态 | 时间 |
|------|------|------|
| G0 Training | ✅ 完成 | 08:50 → 09:13 (~23 min, 305 steps) |
| G0 Evaluation | ✅ 完成 | 09:13 → 10:49 (~1h36m, 6 checkpoints) |
| G0 Generation | 🔄 **进行中** | 10:49 开始, 51/306 batches (17%) |
| G1 Training | ⏳ 等待 | |
| G1 Eval + Gen | ⏳ 等待 | |
| G2 Training + Eval | ⏳ 等待 | |

**Generation 速度**: ~80s/batch, 剩余 255 batches ≈ **5h40m**

### 预估剩余时间

| 阶段 | 预估 |
|------|------|
| G0 gen 剩余 | ~5h40m |
| G1 (train+eval+gen) | ~8h40m |
| G2 (train+eval) | ~2h (gen 可能跳过) |
| **总计剩余** | **~16h** |

### G0 Metrics (final_model) vs v7 参考值

| 指标 | seed=0 (本次) | seed=42 (v7 参考) | 差异 |
|------|-------------|-----------------|------|
| **eff_rank** | **676.89** | 676.96 | -0.01% |
| **perplexity** | **13.27** | 13.27 | 一致 |
| **unigram_entropy** | **6.93** | 6.93 | 一致 |
| **vocab_coverage** | **0.468** | 0.469 | -0.2% |
| unique_tokens | 23530 | — | — |
| bigram_entropy | 10.20 | — | — |
| trigram_entropy | 11.42 | — | — |
| spectral_entropy | 6.518 | — | — |

### G0 训练过程中各 checkpoint 的 eff_rank 变化

| checkpoint | step | tokens | eff_rank | ppl |
|-----------|------|--------|----------|-----|
| ckpt-76 | 76 | 5.0M | 679.68 | 13.53 |
| ckpt-152 | 152 | 10.0M | 677.79 | 13.34 |
| ckpt-228 | 228 | 14.9M | 677.02 | 13.28 |
| ckpt-304 | 304 | 19.9M | 676.89 | 13.27 |
| ckpt-305 | 305 | 20.0M | 676.89 | 13.27 |
| final_model | 305 | 20.0M | 676.89 | 13.27 |

### 初步结论

G0 metrics 与 v7 (seed=42) 高度一致，复现成功。需等 G1/G2 完成后才能验证关键问题：holdout eff_rank 上升趋势和 n-gram entropy collapse 是否在不同 seed 下可复现。

GPU 状态正常：RTX PRO 6000 (98GB), 40GB 已用, 50% 利用率, 48°C。

---
