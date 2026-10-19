# ops training progress check 0515d

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check-0515d_20260515T154054_result.json`
- **Structured JSON:** [`79d7fb680269e5feeacd.json`](../../sessions/79/79d7fb680269e5feeacd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 100% | 60.8 / 97.9 GB |
| 1 | 100% | 55.1 / 97.9 GB |

---

### Qwen chain (GPU 0, PID 337267, 运行 28h16m)

**脚本**: `run_m2_full_qwen.sh` — 3 strategies × 2 seeds + bm25_s42 = **7 runs**

| # | subrun | 状态 | best val_loss | best R@1 |
|---|--------|------|---------------|----------|
| 1 | random_s43 | done | — | — |
| 2 | random_s44 | done | — | — |
| 3 | embedding_distance_s43 | done | — | — |
| 4 | **embedding_distance_s44** | **刚完成** (early stop @ step 2000) | **0.4341** | **0.5813** |
| 5 | dataflow_aware_s43 | 即将开始 | — | — |
| 6 | dataflow_aware_s44 | 待运行 | — | — |
| 7 | bm25_s42 | 待运行 | — | — |

进度: **4/7 完成**，剩余 3 个 run。每个 run 最多 ~2816 步（可能 early stop 在 ~1500-2000 步），预估还需 **6-10 小时**。

之后 `watch_and_chain_qwen_s42.sh` 还会接力跑 s42 supplement。

---

### StarCoder chain (GPU 1, PID 519791, 运行 21h38m)

**脚本**: `run_m2_full_starcoder.sh` — 3 strategies × 2 seeds = **6 runs**

| # | subrun | 状态 | best val_loss | best R@1 |
|---|--------|------|---------------|----------|
| 1 | random_s43 | done (early stop @ 2500) | 0.5239 | 0.4905 |
| 2 | **random_s44** | **进行中, step 1350/~2816** | 0.5913 (@500) | 0.4848 (@500) |
| 3 | embedding_distance_s43 | 待运行 | — | — |
| 4 | embedding_distance_s44 | 待运行 | — | — |
| 5 | dataflow_aware_s43 | 待运行 | — | — |
| 6 | dataflow_aware_s44 | 待运行 | — | — |

进度: **1/6 完成，第 2 个 ~48%**。eval@1000 的 val_loss 未改善 (1/2 patience)。预估剩余 **15-24 小时**。

---

### m1_reextract_v2

- **all.jsonl**: 44,173 行
- **CodeQL**: 正在处理 `Project-MONAI__MONAI`
- **bootstrap_paired_test.py** (PID 4545): 正在运行，当前在加载 embedding_distance_s43 模型、编码 3052 queries

---

**关键观察**: Qwen embedding_distance_s44 的 best R@1=0.5813 显著优于 StarCoder random_s43 的 0.4905，符合预期（embedding distance 策略 + Qwen 编码器更强）。StarCoder random_s44 的 eval@1000 val_loss 未改善，可能也会在 step 1500 early stop。

---
