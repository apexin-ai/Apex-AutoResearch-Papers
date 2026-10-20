# prep medium seed456 scripts

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_medium_seed456_scripts_20260514T032116_result.json`
- **Structured JSON:** [`386583ab93158305aff0.json`](../../sessions/38/386583ab93158305aff0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 报告

### 1. 创建的脚本（6个）

| 脚本 | 用途 |
|------|------|
| `run_medium_uncurated_seed456.sh` | uncurated 100% data |
| `run_medium_rgds_seed456.sh` | RGDS 50% embedding selection |
| `run_medium_random50_seed456.sh` | Random 50% selection |
| `run_medium_external_seed456.sh` | External (Contriever) 50% selection |
| `chain_cuda0_s456.sh` | cuda:0 串行: uncurated → rgds → random50 |
| `chain_cuda1_s456.sh` | cuda:1 单跑: external |

### 2. 参数差异确认

所有脚本相对 seed=123 模板**仅改了两处**：
- `--seed 123` → `--seed 456`
- `--output_dir ...seed123` → `...seed456`

其余参数完全一致：gpt2-medium, 8 gen, 500K tokens, lr=5e-5, epochs=3, batch=4, grad_accum=8, seq_len=512。

注：random50_seed456 去掉了 seed=123 模板中的 cuda:1 flag check（那是 seed=123 特有的调度逻辑）。

### 3. Chain 串行顺序

- **chain_cuda0_s456.sh**: uncurated → rgds → random50（用 `set -e` 在各子脚本中保证失败即停）
- **chain_cuda1_s456.sh**: external only

### 4. 当前 seed=123 进度

| GPU | 实验 | 进度 |
|-----|------|------|
| cuda:0 | uncurated_seed123 | gen_0~gen_5 已完成，正在跑 gen_6 (共8代) |
| cuda:1 | external_seed123 | gen_0 已完成，正在跑 gen_1 (共8代) |
| — | rgds_seed123 | 未开始 |
| — | random50_seed123 | 未开始 |

---
