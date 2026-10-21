# code gpu snapshot fill all

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu-snapshot-fill-all_20260521T114444_result.json`
- **Structured JSON:** [`6145c6e6da5cf3689370.json`](../../sessions/61/6145c6e6da5cf3689370.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-35694 4/4 GPU 全部在用。** 19912 GPU 空闲（eval 已完成）。

---

## 产出汇总

### 1. GPU 状态表

| 服务器 | GPU | 状态 | 任务 | PID |
|--------|-----|------|------|-----|
| **westd-35694** | 0 | 95%, 27GB | Llama clean_s7 train | 135251 |
| | 1 | 78%, 31GB | Llama clean_s4 train | 133695 |
| | 2 | 97%, 18GB | Llama clean_s5 train | 134196 |
| | 3 | 97%, 17GB | Llama clean_s6 train | 134708 |
| **westd-19912** | 0-3 | 空闲 | ARC-C eval s3-s6 刚完成 | — |

### 2. 新启动的任务

| 服务器 | GPU | 任务 | PID |
|--------|-----|------|-----|
| 35694 | 0 | Llama clean_s7 (seed=304) | 135251 |
| 35694 | 1 | Llama clean_s4 (seed=301) | 133695 |
| 35694 | 2 | Llama clean_s5 (seed=302) | 134196 |
| 35694 | 3 | Llama clean_s6 (seed=303) | 134708 |
| 19912 | 0 | ARC-C eval clean_s3 | ✅ 完成 |
| 19912 | 1 | ARC-C eval clean_s4 | ✅ 完成 |
| 19912 | 2 | ARC-C eval clean_s5 | ✅ 完成 |
| 19912 | 3 | ARC-C eval clean_s6 | ✅ 完成 |

### 3. 已完成训练的 Eval 结果

**Llama MMLU (35694):**

| condition | theta | lz* | acc | n_items |
|-----------|-------|-----|-----|---------|
| clean_s2 | -0.630 | -0.182 | 0.595 | 14042 |
| clean_s3 | -0.640 | -1.084 | 0.594 | 14042 |

**ARC-C (19912) — 刚完成：**

| condition | theta | lz* | acc | n_items |
|-----------|-------|-----|-----|---------|
| clean_s3 | 0.714 | -5.524 | 0.895 | 295 |
| clean_s4 | 0.550 | -5.434 | 0.885 | 295 |
| clean_s5 | 0.781 | -5.232 | 0.898 | 295 |
| clean_s6 | 0.755 | -5.572 | 0.895 | 295 |

### 4. 修复项

- ✅ Llama `train.py` SEED_MAP 添加 s4-s8 (301-305)，DATA_DIR_MAP 添加 s4-s8→clean
- ✅ Llama `train.py` report_to 改为 "none"（wandb 未配置）
- ✅ ARC-C `train.py` (35694) report_to 改为 "none"

### 5. 待办

- **Llama s8** (seed=305)：等 s4-s7 其中一个完成后启动（~17min）
- **ARC-C s3 on 35694**：checkpoint 为空，需重训（wandb 已修复），等 GPU 释放
- **Mistral s2/s3 eval**：训练完成但未跑 eval，等 GPU 释放
- **19912 4 卡空闲**：可分配新任务（Llama 未部署在 19912）

---
