# verify seed corpus factcheck

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_seed_corpus_factcheck_20260515T173753_result.json`
- **Structured JSON:** [`4aa09088f369841b7d51.json`](../../sessions/4a/4aa09088f369841b7d51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

事实核查完成，结论清晰。

---

## 种子语料事实核查结果

### 1. depth-0 种子数据的实际来源

**English Wikipedia (`wikimedia/wikipedia`, `20231101.en` snapshot)**

证据：`scripts/prepare_seed_data.py` 第 21-22 行：
```python
ds = load_dataset("wikimedia/wikipedia", "20231101.en", split="train", streaming=True)
source = "wikipedia"
```
fallback 是 `allenai/c4`（第 25 行），但实际数据文件中 5000/5000 条记录的 `"source"` 字段均为 `"wikipedia"`，说明 **C4 fallback 从未触发**。

数据内容也印证了这一点——首条记录就是 Wikipedia 的 "Anarchism" 词条。

### 2. 三个模型是否用同一份种子数据？

**是，完全相同的一份 `data/depth_0.jsonl`（5000 条）。**

三个 pipeline 脚本的 Step 1 都指向同一文件：
- `run_pipeline.sh`（Pythia）：`--input_data data/depth_0.jsonl`
- `run_pipeline_olmo.sh`：`--input_data data/depth_0.jsonl`
- `run_pipeline_gpt2xl.sh`：`--input_data data/depth_0.jsonl`

depth-1+ 的数据各模型独立生成（输出到 `data/olmo/`、`data/gpt2xl/` 等子目录），但种子数据共享。

### 3. "Wikipedia subset" 的说法是否准确？

**准确。** 论文中写 "Wikipedia subset" 是正确的。数据来自 `wikimedia/wikipedia` 2023-11-01 英文快照，取前 5000 条满足 256-512 token 长度约束的文章（用 Qwen2.5-1.5B tokenizer 截断）。

### 4. 正确的表述

论文现有说法 **无需修改**。精确表述为：

> We sample 5,000 articles from the English Wikipedia (November 2023 snapshot, `wikimedia/wikipedia` on HuggingFace), truncated to 256–512 tokens, as the shared depth-0 seed corpus for all three model families.

method worker 改用 OpenWebText/Dolma/WebText 的说法**与代码不符**——这些是各模型的预训练数据，不是本项目的种子数据。种子数据统一是 Wikipedia。

---
