# infra c4 1b5 data search

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_c4-1b5-data-search_20260519T201428_result.json`
- **Structured JSON:** [`f7d98654a57ea3164ca3.json`](../../sessions/f7/f7d98654a57ea3164ca3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。以下是结果：

---

## C4 1.5B-scale depth chain 原始文本数据搜索结果

### 目标模型覆盖情况

| Generator Model | 状态 | 路径 (cqa1-22115) | Depths | Docs |
|---|---|---|---|---|
| **Qwen2.5-1.5B (rewrite)** | ✅ 有 | `data_exp016_qwen_base/depth_*.jsonl` | 0-5 | 5000 |
| **Pythia-1.4B** | ✅ 有 | `data_exp020_pythia_greedy/depth_*.jsonl` | 0-5 | 5000 |
| **OLMo-1B** | ❌ 缺失 | `data/olmo_retrain_chain/` 只有 depth_0（seed） | - | - |
| **Qwen2.5-1.5B (continuation)** | ✅ 有 | `data/exp_021_length_256/depth_*.jsonl` | 0-5 | 5000 |

### 数据格式确认
全部 `{"text": "...", "doc_id": N}` 格式，可直接用于 DeBERTa。所有数据集共享同一批 C4 seed（doc_id=0 均为 "The woman who died after falling from a bridge over the A21..."）。

### cqa1-22115 上的额外 C4 数据（同一 seed 集）
- `data_exp020_pythia_nuc09/` — Pythia-1.4B nucleus p=0.9, depth 0-5, 5000 docs
- `data_exp020_pythia_t07/` — Pythia-1.4B temp=0.7, depth 0-5, 5000 docs
- `data_exp020_pythia_t12/` — Pythia-1.4B temp=1.2
- `data/exp_021_length_128/` — Qwen cont 128 tokens
- `data/exp_021_length_512/` — Qwen cont 512 tokens
- `data/exp_008_retrain_chain/` — Pythia retrain chain, depth 0-7
- `data/exp_qwen_retrain_chain/` — Qwen retrain chain, depth 0-7

### westd-42896
- `data/exp_14b_c4/` — **Qwen2.5-14B** on C4（不是 1.5B scale）
- `data/exp_32b_c4/` — **Qwen2.5-32B** on C4（不是 1.5B scale）
- DeBERTa 已在该服务器上对 14B/32B 数据训练中

### 结论
- 原始 exp_001/002/003/006 目录在两台服务器上均不存在（可能来自已释放的实例），但对应数据已在 cqa1-22115 上以新编号重新生成
- **OLMo-1B on C4 需要重新生成**，目前只有 seed，没有任何 depth chain 输出

---
