# code posthoc mistral llama unconstrained

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_posthoc_mistral_llama_unconstrained_20260518T102610_result.json`
- **Structured JSON:** [`283585edb7ff50794ea3.json`](../../sessions/28/283585edb7ff50794ea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下。

---

## Post-hoc Filtering 结果（WikiEvents EE, 246 docs）

| Model | Unconstrained (events / args) | Post-hoc (events / args) | EV removed | RoV removed | AC removed |
|-------|------|------|------|------|------|
| **Mistral** | 2405 / 6034 | 1507 / **0** | 898 (37%) | 3858 | 0 |
| **Llama** | 2447 / 5053 | 2189 / **3** | 258 (11%) | 4486 | 3 |
| **Qwen** | 3013 / 5467 | 2291 / **23** | 722 (24%) | ~5444 | — |

Post-hoc 几乎删除了所有 arguments（Mistral 100%, Llama 99.9%, Qwen 99.6%），原因是 unconstrained 模型生成的 role 名称（如 "speaker"/"bomb"/"bystanders"）完全不匹配 ontology 定义的合法 role，RoV 过滤直接清空。

---

## V3 进度

| Task | Server | Lines | Status |
|------|--------|-------|--------|
| Mistral constrained v3 | westd-21461 | 226/246 | **运行中**（tmux: mistral_v3_full, ~3.5h elapsed） |
| Llama constrained v3 | westd-21461 | 246/246 | **完成** |
| Mistral grammar_only v3 | westd-16980 | 242/246 | **完成**（4 条 skip/error） |
| Qwen constrained v3 | westd-16980 | 246/246 | **完成** |

---

## 70B 下载（westd-21461）

下载 `LLM-Research/Meta-Llama-3.1-70B-Instruct`（全量 FP16, 8 shards x 16.4GB = ~131GB）
- 当前进度: 每个 shard ~2-3%（~300-450MB）
- 速度: ~1.5 MB/s per shard
- ETA: **约 3 小时**
- 之前的 AWQ-INT4 下载已被取消（^C），当前是全量模型

---

Post-hoc 输出已写入：
- `westd-16980: outputs/ee_llama_wikievents_unconstrained_posthoc.jsonl`
- `westd-21461: outputs/ee_mistral_wikievents_unconstrained_posthoc.jsonl`

---
