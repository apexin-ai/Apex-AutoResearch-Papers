# code rsft bugfix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_code_rsft-bugfix_20260515T010036.jsonl`
- **Structured JSON:** [`e293edc9530e349afb6a.json`](../../sessions/e2/e293edc9530e349afb6a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-15T01:01:19.881718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_generate.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_rsft-bugfix_20260515T010036",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_generate.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T01:01:19.882422+00:00_

1	"""RSFT Step 1: 批量生成候选输出。
2	
3	用 SFT warmup 模型对每个训练样本生成 N 个候选输出 (temperature sampling)，
4	保存为 JSONL 供后续 CED 打分筛选。
5	
6	输入:
7	  - base model (Qwen3-4B) + QLoRA adapter (SFT checkpoint)
8	  - DocRED train_annotated.json
9	
10	输出 (保存到 --output_dir):
11	  - generations.jsonl: 每行一个生成结果
12	    {"doc_id", "generation_idx", "prompt", "output", "raw_text", "parsed_triples", "format_ok"}
13	  - progress.json: 已完成的 doc_id 列表（用于断点续传）
14	
15	依赖: transformers, peft, bitsandbytes, torch, tqdm
16	
17	用法:
18	  python -m freige.training.rsft_generate \
19	      --base_model /root/autodl-tmp/models/Qwen3-4B \
20	      --sft_adapter /root/autodl-tmp/sft_output \
21	      --data_path /root/autodl-tmp/data/docred \
22	      --output_dir /root/autodl-tmp/rsft_generations \
23	      --num_generations 8 --temperature 0.7 --batch_size 4
24	"""
25	
26	import argparse
27	import json
28	import logging
29	import os
30	from pathlib import Path
31	
32	import torch
33	from peft import PeftModel
34	from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
35	from tqdm import tqdm
36	
37	from freige.data.docred_processor import DocREDProcessor
38	from freige.eval.evaluator import parse_model_output
39	
40	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
41	logger = logging.getLogger(__name__)
42	
43	SYSTEM_PROMPT = (
44	    "You are an information extraction model. Given a document with numbered sentences "
45	    "and a list of entities, extract all relation triples. For each triple, provide the "
46	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
47	    "Output as a JSON list."
48	)
49	
50	
51	def load_model_and_tokenizer(base_model, sft_adapter=None, quantize=True):
52	    """加载 base model + 可选 QLoRA adapter，merge 后返回。"""
53	    logger.info("Loading tokenizer: %s", base_model)
54	    tokenizer = AutoTokenizer.from_pretrained(
55	        base_model, trust_remote_code=True, padding_side="left
…[truncated 9812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_rsft-bugfix_20260515T010036",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T01:01:19.882735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_score_filter.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_rsft-bugfix_20260515T010036",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_score_filter.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T01:01:19.883050+00:00_

1	"""RSFT Step 2: CED 打分 + 筛选。
2	
3	读取 rsft_generate.py 生成的 JSONL，对每个候选输出计算三种奖励:
4	  - format_reward: JSON 格式合规性
5	  - f1_reward: 与 gold triples 的 micro-F1
6	  - ced_reward: CED 对比证据判别奖励
7	
8	按组合阈值筛选高质量样本，输出 SFT 训练兼容格式。
9	
10	输入:
11	  - generations.jsonl (rsft_generate.py 的输出)
12	
13	输出 (保存到 --output_path):
14	  - rsft_train.json: 筛选后的 SFT 训练数据
15	  - rsft_scores.jsonl: 带分数的完整记录（供分析）
16	  - rsft_report.json: 统计报告
17	
18	依赖: transformers, torch, freige.rewards.ced_reward
19	
20	用法:
21	  python -m freige.training.rsft_score_filter \
22	      --input_dir /root/autodl-tmp/rsft_generations \
23	      --output_path /root/autodl-tmp/rsft_filtered \
24	      --selection_strategy top_pct --top_pct 25 \
25	      --nli_model_path /root/autodl-tmp/models/nli-deberta-v3-base
26	"""
27	
28	import argparse
29	import json
30	import logging
31	import os
32	from collections import defaultdict
33	from pathlib import Path
34	
35	import numpy as np
36	
37	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
38	logger = logging.getLogger(__name__)
39	
40	SYSTEM_PROMPT = (
41	    "You are an information extraction model. Given a document with numbered sentences "
42	    "and a list of entities, extract all relation triples. For each triple, provide the "
43	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
44	    "Output as a JSON list."
45	)
46	
47	
48	# ---------------------------------------------------------------------------
49	# Reward functions — 复用 grpo_trainer 中的逻辑
50	# ---------------------------------------------------------------------------
51	
52	def compute_format_reward(parsed_triples, format_ok):
53	    """格式奖励，复用 grpo_trainer.format_reward_fn 的逻辑。"""
54	    if not format_ok:
55	        return 0.0
56	    if not parsed_triples:
57	        return 0.1
58	    valid = 0
59	    for item in parsed_triples:
60	        if (isinstance(item, dict) and "head" in item
61	                and "relation" in ite
…[truncated 16518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_rsft-bugfix_20260515T010036",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T01:01:19.883255+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_trainer.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_rsft-bugfix_20260515T010036",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_trainer.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T01:01:19.883529+00:00_

1	"""RSFT (Rejection Sampling Fine-Tuning) 训练脚本。
2	
3	从 SFT warmup checkpoint 继续训练，使用经 CED 打分筛选的高质量生成数据。
4	流程: base model → merge SFT adapter → 新 QLoRA → 在 RSFT 数据上训练。
5	
6	输入: JSONL，每行 {"doc_id": ..., "input": ..., "output": ..., "ced_score": ..., ...}
7	输出: QLoRA adapter checkpoint
8	依赖: transformers, trl, peft, bitsandbytes, datasets
9	
10	单卡:   python -m freige.training.rsft_trainer --rsft_data_path data.jsonl --output_dir ./rsft_output
11	多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
12	            -m freige.training.rsft_trainer --rsft_data_path data.jsonl --output_dir ./rsft_output
13	"""
14	
15	import argparse
16	import json
17	import logging
18	import os
19	
20	import torch
21	from datasets import Dataset
22	from peft import LoraConfig, PeftModel, TaskType, get_peft_model
23	from torch.utils.data import WeightedRandomSampler
24	from transformers import (
25	    AutoModelForCausalLM,
26	    AutoTokenizer,
27	    BitsAndBytesConfig,
28	)
29	from trl import SFTConfig, SFTTrainer
30	
31	from freige.training.sft_trainer import SYSTEM_PROMPT
32	
33	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
34	logger = logging.getLogger(__name__)
35	
36	DEFAULT_BASE_MODEL = "/root/autodl-tmp/models/Qwen3-4B"
37	DEFAULT_SFT_ADAPTER = "/root/autodl-tmp/sft_output"
38	
39	
40	def load_rsft_data(data_path: str, tokenizer, max_length: int = 2048):
41	    """加载 CED 筛选后的 RSFT 数据，格式化为 chat template 文本。
42	
43	    每行 JSONL 的 input 字段作为 user message，output 字段作为 assistant response，
44	    经 apply_chat_template 拼接后用于 SFT 训练。超过 max_length 的样本被跳过
45	    而非截断，避免训练在不完整 JSON 输出上。
46	
47	    Returns:
48	        (Dataset, list[float]): 训练数据集和对应的 CED scores
49	    """
50	    samples = []
51	    with open(data_path) as f:
52	        for line in f:
53	            if line.strip():
54	                samples.append(json.loads(line))
55	
56	    logger.info("Loaded %d RSFT samples from %s", len(samples), data_path)
57	
58	    formatted = 
…[truncated 8178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_rsft-bugfix_20260515T010036",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T01:01:19.883747+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_generate.py",
  "old_string": "    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction,\n                        default=True, help=\"4-bit 量化 (default: on)\")",
  "new_string": "    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction,\n                        default=False, help=\"4-bit 量化 (default: off, bf16 sufficient for 4B model)\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_rsft-bugfix_20260515T010036",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_generate.py",
    "old_string": "    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction,\n                        default=True, help=\"4-bit 量化 (default: on)\")",
    "new_string": "    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction,\n                        default=False, help=\"4-bit 量化 (default: off, bf16 sufficient for 4B model)\")"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T01:01:19.883941+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_generate.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_rsft-bugfix_20260515T010036",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T01:01:19.884089+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_score_filter.py",
  "old_string": "    sft_data = format_sft_training_data(selected)\n    train_path = output_dir / \"rsft_train.json\"\n    with open(train_path, \"w\") as f:\n        json.dump(sft_data, f, ensure_ascii=False, indent=2)\n    logger.info(\"Training data → %s (%d samples)\", train_path, len(sft_data))",
  "new_string": "    sft_data = format_sft_training_data(selected)\n    train_path = output_dir / \"rsft_train.jsonl\"\n    with open(train_path, \"w\") as f:\n        for item in sft_data:\n            user_msg = next(m[\"content\"] for m in item[\"messages\"] if m[\"role\"] == \"user\")\n            asst_msg = next(m[\"content\"] for m in item[\"messages\"] if m[\"role\"] == \"assistant\")\n            record = {\n                \"input\": user_msg,\n                \"output\": asst_msg,\n                \"ced_score\": item[\"scores\"][\"ced_reward\"],\n                \"doc_id\": item.get(\"doc_id\"),\n                \"generation_idx\": item.get(\"generation_idx\"),\n                \"scores\": item[\"scores\"],\n            }\n            f.write(json.dumps(record, ensure_ascii=False) + \"\\n\")\n    logger.info(\"Training data → %s (%d samples)\", train_path, len(sft_data))"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_rsft-bugfix_20260515T010036",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_score_filter.py",
    "old_string": "    sft_data = format_sft_training_data(selected)\n    train_path = output_dir / \"rsft_train.json\"\n    with open(train_path, \"w\") as f:\n        json.dump(sft_data, f, ensure_ascii=False, indent=2)\n    logger.info(\"Training data → %s (%d samples)\", train_path, len(sft_data))",
    "new_string": "    sft_data = format_sft_training_data(selected)\n    train_path = output_dir / \"rsft_train.jsonl\"\n    with open(train_path, \"w\") as f:\n        for item in sft_data:\n            user_msg = next(m[\"content\"] for m in item[\"messages\"] if m[\"role\"] == \"user\")\n            asst_msg = next(m[\"content\"] for m in item[\"messages\"] if m[\"role\"] == \"assistant\")\n            record = {\n                \"input\": user_msg,\n                \"output\": asst_msg,\n                \"ced_score\": item[\"scores\"][\"ced_reward\"],\n                \"doc_id\": item.get(\"doc_id\"),\n                \"generation_idx\": item.get(\"generation_idx\"),\n                \"scores\": item[\"scores\"],\n            }\n            f.write(json.dumps(record, ensure_ascii=False) + \"\\n\")\n    logger.info(\"Training data → %s (%d samples)\", train_path, len(sft_data))"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T01:01:19.884662+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_score_filter.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_rsft-bugfix_20260515T010036",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T01:01:19.885538+00:00_

验证结果：

1. **Bug 1** — `rsft_generate.py:210`: `--quantize` default 已改为 `False`
2. **Bug 2** — `rsft_score_filter.py:437-448`: 输出改为 JSONL (`rsft_train.jsonl`)，每行含 `input`/`output`/`ced_score` 字段，与 `rsft_trainer.py:62-78` 的 `load_rsft_data` 完全匹配（读 JSONL，取 `s["input"]`、`s["output"]`、`s.get("ced_score", 1.0)`）
3. **Bug 3** — NLI 模型路径逻辑正确，无需修改
4. `rsft_trainer.py` 无需改动

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_rsft-bugfix_20260515T010036"
}
```

</details>

---
