# diagnose 14b gen progress and multiseed scan

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_14b-gen-progress-and-multiseed-scan_20260523T002521_result.json`
- **Structured JSON:** [`857c68b6d0679ba5a431.json`](../../sessions/85/857c68b6d0679ba5a431.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B s43 Generation

- **进度**: 1058/3027 docs (35%)
- **PID**: 194682, 运行 6h9m, CPU 100%, RSS 2.4GB
- **生成文件**: 8464 lines (8 gens/doc × 1058 docs)
- **速度**: ~21s/doc
- **剩余**: 1969 docs × 21s ≈ **11.5 小时**
- **ETA**: 约今天 ~19:30 UTC

---

## Multi-seed RSFT Test Eval 可行性

### 已有 RSFT Models (all verified with adapter_config.json)

| Scale | seed 42 | seed 43 | seed 44 |
|-------|---------|---------|---------|
| Qwen3-1.7B | `rsft_output_qwen3_1_7b_k1` | `rsft_output_qwen3_1_7b_k1_s43` | `rsft_output_qwen3_1_7b_k1_s44` |
| Qwen3-4B | `rsft_output_ced_s42_v2` | `rsft_output_ced_s43` | — |
| Qwen3-8B | `rsft_output_qwen3_8b_k1` | `rsft_output_qwen3_8b_k1_s43` | `rsft_output_qwen3_8b_k1_s44` |
| Qwen3-14B | `rsft_output_14b` | — (gen中) | — |
| LLaMA-3.1-8B | `rsft_output_llama_3_1_8b_k1` | `rsft_output_llama_3_1_8b_k1_s43` | `rsft_output_llama_3_1_8b_k1_s44` |

### 已有 Test Eval (全部仅 s42)

| Scale | s42 with-evi (ign_f1) | s42 no-evi | s43 w/ | s43 no | s44 w/ | s44 no |
|-------|-----------------------|------------|--------|--------|--------|--------|
| 1.7B | ✅ 0.293 | ✅ | — | — | — | — |
| 4B | ✅ 0.250 | ✅ | — | — | n/a | n/a |
| 8B | ✅ 0.335 | ✅ | — | — | — | — |
| 14B | ✅ 0.385 | ✅ | n/a | n/a | n/a | n/a |
| LLaMA | ✅ 0.360 | ✅ | — | — | — | — |

### 可立即跑的 Test Eval 清单 (14 evals)

| # | Scale | Seed | Mode | Model Path |
|---|-------|------|------|------------|
| 1 | 1.7B | s43 | with-evi | `rsft_output_qwen3_1_7b_k1_s43` |
| 2 | 1.7B | s43 | no-evi | 同上 |
| 3 | 1.7B | s44 | with-evi | `rsft_output_qwen3_1_7b_k1_s44` |
| 4 | 1.7B | s44 | no-evi | 同上 |
| 5 | 4B | s43 | with-evi | `rsft_output_ced_s43` |
| 6 | 4B | s43 | no-evi | 同上 |
| 7 | 8B | s43 | with-evi | `rsft_output_qwen3_8b_k1_s43` |
| 8 | 8B | s43 | no-evi | 同上 |
| 9 | 8B | s44 | with-evi | `rsft_output_qwen3_8b_k1_s44` |
| 10 | 8B | s44 | no-evi | 同上 |
| 11 | LLaMA | s43 | with-evi | `rsft_output_llama_3_1_8b_k1_s43` |
| 12 | LLaMA | s43 | no-evi | 同上 |
| 13 | LLaMA | s44 | with-evi | `rsft_output_llama_3_1_8b_k1_s44` |
| 14 | LLaMA | s44 | no-evi | 同上 |

### 预估运行时间 (from s42 test_summary.json)

| Scale | inference_time | batch_size | 备注 |
|-------|---------------|------------|------|
| 1.7B | 5.9h (21129s) | 1 | 可尝试 batch=16 加速 |
| 4B | **1.1h** (4124s) | 16 | 快 |
| 8B | **0.75h** (2711s) | 16 | 最快 |
| 14B | 5.3h (19086s) | 1 | — |
| LLaMA | 5.4h (19571s) | 1 | — |

**总计 14 evals**。4 卡并行调度估算：
- 快速组 (4B×2 + 8B×4 = 6 evals): ~2h 内全部完成
- 慢速组 (1.7B×4 + LLaMA×4 = 8 evals): 每个 ~6h, 4 卡并行需 2 轮 ≈ **~12h**
- **总墙钟时间: ~12-14h** (慢速组是瓶颈)
- 注意: 14B gen 正占 2 卡 (cuda:0,1)，当前只有 2 卡空闲可跑 eval，需等 gen 完成后才能 4 卡满载

---
