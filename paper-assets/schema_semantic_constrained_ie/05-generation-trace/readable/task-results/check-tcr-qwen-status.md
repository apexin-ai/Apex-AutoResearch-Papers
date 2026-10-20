# check tcr qwen status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_tcr-qwen-status_20260522T154715_result.json`
- **Structured JSON:** [`72256b54059616d379b6.json`](../../sessions/72/72256b54059616d379b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### TCR Beam4 Qwen SciERC — 已完成 (DONE, negative)

| 指标 | 值 |
|------|-----|
| Entity F1 | 67.26 (P=65.05, R=69.64) |
| Relation F1 | 44.24 (P=39.36, R=50.51) |
| D/R violations | 23/1250 (1.84%) |
| Entity type violations | 0/1802 (0%) |
| Relation vocab violations | 0/1250 (0%) |
| Cross-field violations | 1 |
| JSON failures | 0 |
| **TCR changed selection** | **0/551 (0.0%)** |

**关键发现**：TCR 完全没有生效——所有 551 个样本的 beam candidates 的 TCR score 都是 1.0，意味着 Qwen beam search 产出的所有候选序列本身就已经满足 type consistency，reranking 无事可做。结论标记为 negative。

---

### GPU 状态

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 81% | 40.4 / 97.9 GB |
| 1 | RTX PRO 6000 Blackwell | 91% | 18.3 / 97.9 GB |

### 其他实验进度

| 实验 | GPU | 进度 | 状态 |
|------|-----|------|------|
| `beam4_tcr_llama_scierc` | GPU 1 | 25/551 (~5%) | RUNNING |
| `70b_lora_scierc_beam4_s1` | GPU 0 | 183/551 (~33%) | RUNNING |

---
