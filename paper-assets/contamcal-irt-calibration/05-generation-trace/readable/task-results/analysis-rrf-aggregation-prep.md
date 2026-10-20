# analysis rrf aggregation prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rrf_aggregation_prep_20260516T143136_result.json`
- **Structured JSON:** [`eafee0ff52c6b2812660.json`](../../sessions/ea/eafee0ff52c6b2812660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pooled IRT 正常运行中 — MMLU 1.5B 组 chain 1 已到 90% sampling。

## 汇总

### 状态

| 任务 | 状态 |
|------|------|
| **exp_006_mmlu_domain_gamma_n24_v4** | RUNNING — 已完成 Social_Sciences (γ=-0.4965)，正在 fit Business_Law |
| **exp_003_rrf_full_n25_latest** | DONE ✅ — 25 模型 × 3 benchmark，output 在 `/root/autodl-tmp/exp003/rrf_full_n_latest/` |
| **exp_006_pooled_irt_rrf_n25_v2** | RUNNING (PID=795897) — 4PL+γ, Stan sampling 进行中 |

### Signals 完整性盘点

**完整 (3 signals × 3 benchmarks):**
- 0.5B: d000/d005/d025/d100 × s42/s123 = 8 ✅
- 1.5B: d000/d005/d025/d100 × s42/s123 = 8 ✅
- 3B s42: d000_a32/d005_a32/d025_v3/d100_a32 = 4 ✅
- 3B s123: d005/d025/d100_a32 = 3 ✅
- 0.5B-Instruct: mmlu only = 1 ✅

**部分完整:**
- 3B_d000_s123_a32: arc/gsm8k 完整，mmlu 缺 s4_selfcritique（chunks 目录存在，未合并）

**总计: 25 模型纳入 RRF**

### Pipeline 状态
```
exp-002 signals (DONE) → exp-003 RRF (DONE, 22:21) → exp-006 pooled IRT (RUNNING)
                                                   → exp-006 mmlu_domain_gamma (RUNNING)
```

两个 CPU 任务并行运行，不冲突。pooled IRT 预计 ~15-30min 完成（每 benchmark 3 个 scale 组 × 4 chains × 2000 iterations）。

---
