# code write eval runner

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_code_write-eval-runner_20260514T074007.jsonl`
- **Structured JSON:** [`e2b24f56dd8115e4eafc.json`](../../sessions/e2/e2b24f56dd8115e4eafc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-14T07:46:23.527717+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T07:46:23.528091+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T07:46:23.528352+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/freige/eval/evaluator.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/freige/eval/evaluator.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T07:46:23.528558+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/freige/training/grpo_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/freige/training/grpo_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T07:46:23.528749+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/freige/training/sft_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/freige/training/sft_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T07:46:23.528884+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/freige/data/docred_processor.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/freige/data/docred_processor.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T07:46:23.529021+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/freige/freige/eval/evaluator.py: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.01}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T07:46:23.529336+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/freige/freige/training/grpo_trainer.py: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T07:46:23.529511+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/freige/freige/training/sft_trainer.py: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T07:46:23.529845+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/freige/freige/data/docred_processor.py: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T07:46:23.530004+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige -type f -name \"*.py\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/freige -type f -name \"*.py\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T07:46:23.530155+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T07:46:23.530302+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige -type f -name \"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp/freige -type f -name \"*.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T07:46:23.530439+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/freige/freige/data/__init__.py\\n/root/autodl-tmp/freige/freige/rewards/__init__.py\\n/root/autodl-tmp/freige/freige/analysis/__init__.py\\n/root/autodl-tmp/freige/freige/training/__init__.py\\n/root/autodl-tmp/freige/freige/eval/__init__.py\\n/root/autodl-tmp/freige/freige/__init__.py\\n/root/autodl-tmp/freige/data/__init__.py\\n/root/autodl-tmp/freige/data/docred_processor.py\\n/root/autodl-tmp/freige/rewards/__init__.py\\n/root/autodl-tmp/freige/rewards/ced_reward.py\\n/root/autodl-tmp/freige/analysis/__init__.py\\n/root/autodl-tmp/freige/analysis/ced_signal_validation.py\\n/root/autodl-tmp/freige/training/__init__.py\\n/root/autodl-tmp/freige/training/sft_trainer.py\\n/root/autodl-tmp/freige/training/grpo_trainer.py\\n/root/autodl-tmp/freige/training/smoke_test.py\\n/root/autodl-tmp/freige/eval/__init__.py\\n/root/autodl-tmp/freige/eval/evaluator.py\\n/root/autodl-tmp/freige/__init__.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T07:46:23.530587+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/eval/evaluator.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/eval/evaluator.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T07:46:23.530868+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"DocRED 关系抽取评测模块。\\n\\n指标:\\n  - F1 / Ign-F1: 关系三元组级别 micro-F1，Ign-F1 排除训练集中出现的三元组\\n  - Evi-F1: 对正确预测的三元组，计算 evidence 句子级 F1\\n  - EDCR: Evidence Distractor Citation Rate，预测 evidence 中非 gold 的比例\\n\\n输入: 预测列表 + gold 标注列表（每个元素为文档级标注）\\n输出: 指标字典\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom collections import defaultdict\\nfrom typing import Optional\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef _triple_key(doc_id: str, head: str, tail: str, relation: str) -> tuple:\\n    return (doc_id, head.lower().strip(), tail.lower().strip(), relation)\\n\\n\\nclass DocREDEvaluator:\\n    \\\"\\\"\\\"DocRED 评测器。\\n\\n    Args:\\n        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。\\n                       每个元素为 (doc_title, head_name, tail_name, relation)。\\n                       为 None 时 Ign-F1 = F1。\\n    \\\"\\\"\\\"\\n\\n    def __init__(self, train_triples: Optional[set[tuple]] = None):\\n        self.train_triples = train_triples or set()\\n\\n    @classmethod\\n    def from_train_file(cls, train_path: str) -> \\\"DocREDEvaluator\\\":\\n        \\\"\\\"\\\"从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。\\\"\\\"\\\"\\n        from freige.data.docred_processor import DOCRED_REL_INFO\\n\\n        with open(train_path) as f:\\n            train_data = json.load(f)\\n\\n        train_triples = set()\\n        for doc in train_data:\\n            doc_id = doc.get(\\\"title\\\", \\\"\\\")\\n            vertex_set = doc[\\\"vertexSet\\\"]\\n            for label in doc.get(\\\"labels\\\", []):\\n                h_name = vertex_set[label[\\\"h\\\"]][0][\\\"name\\\"]\\n                t_name = vertex_set[label[\\\"t\\\"]][0][\\\"name\\\"]\\n                rel_name = DOCRED_REL_INFO.get(label[\\\"r\\\"], label[\\\"r\\\"])\\n                train_triples.add(\\n                    _triple_key(doc_id, h_name, t_name, rel_name)\\n                )\\n\\n        logger.info(\\\"Loaded %d training triples for Ign-F1\\\", 
…[truncated 7323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T07:46:23.531045+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/training/grpo_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/training/grpo_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T07:46:23.531316+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\\n\\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\\n\\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\\\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\\\\n            --stage 1 --reward_device cpu\\n不量化: 加 --no_quantize\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport math\\nimport os\\nimport re\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport torch\\nfrom datasets import Dataset\\nfrom peft import LoraConfig, PeftModel, TaskType\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\\nfrom trl import GRPOConfig, GRPOTrainer\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlogger = logging.getLogger(__name__)\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are an information extraction model. Given a document with numbered sentences \\\"\\n    \\\"and a list of entities, extract all relation triples. For each triple, provide the \\\"\\n    \\\"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \\\"\\n    \\\"Output as a JSON list.\\\"\\n)\\n\\n\\ndef _parse_json_output(text: str) -> list[dict]:\\n    \\\"\\\"\\\"从模型输出中解析 JSON 列表。\\\"\\\"\\\"\\n    try:\\n        return json.loads(text)\\n    except json.JSONDecodeError:\\n        start = text.find(\\\"[\\\")\\n        end = text.rfind(\\\"]\\\") + 1\\n        if start >= 0 and end > start:\\n            try:\\n                return json.loads(text[start:end])\\n            except json.JSONDecodeError:\\n                return []\\n    return []\\n\\n\\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\\n    \\\"\\\"\\\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\\\"\\\"\\\"\\n    rewards = []\\
…[truncated 7125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T07:46:23.531489+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/training/sft_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/training/sft_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T07:46:23.531798+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"SFT 训练脚本: Qwen3-4B + QLoRA 在 DocRED 上微调。\\n\\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练。\\n默认启用 4-bit QLoRA 量化，适配 RTX 5090 32GB x4。\\n\\n单卡:   python -m freige.training.sft_trainer --output_dir ./sft_output\\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\\\\n            -m freige.training.sft_trainer --deepspeed configs/deepspeed_zero2.json\\n不量化: 加 --no_quantize\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nfrom dataclasses import dataclass, field\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport torch\\nfrom datasets import Dataset\\nfrom peft import LoraConfig, TaskType, get_peft_model\\nfrom transformers import (\\n    AutoModelForCausalLM,\\n    AutoTokenizer,\\n    BitsAndBytesConfig,\\n    TrainingArguments,\\n)\\nfrom trl import SFTTrainer, SFTConfig\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlogger = logging.getLogger(__name__)\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are an information extraction model. Given a document with numbered sentences \\\"\\n    \\\"and a list of entities, extract all relation triples. For each triple, provide the \\\"\\n    \\\"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \\\"\\n    \\\"Output as a JSON list.\\\"\\n)\\n\\nDEFAULT_MODEL = \\\"/root/autodl-tmp/models/Qwen3-4B\\\"\\n\\n\\ndef build_chat_messages(instruction: str, input_text: str, output_text: str = None):\\n    \\\"\\\"\\\"构建 Qwen3 chat 格式的消息列表。\\\"\\\"\\\"\\n    messages = [\\n        {\\\"role\\\": \\\"system\\\", \\\"content\\\": SYSTEM_PROMPT},\\n        {\\\"role\\\": \\\"user\\\", \\\"content\\\": f\\\"{instruction}\\\\n\\\\n{input_text}\\\"},\\n    ]\\n    if output_text is not None:\\n        messages.append({\\\"role\\\": \\\"assistant\\\", \\\"content\\\": output_text})\\n    return messages\\n\\n\\ndef prepare_dataset(\\n    data_
…[truncated 6841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T07:46:23.531965+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/data/docred_processor.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/freige/data/docred_processor.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T07:46:23.532284+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"DocRED 数据预处理模块。\\n\\n加载 DocRED 数据集（train_annotated / dev / test），解析实体、关系、\\nevidence 标注，构建含 hard negatives 的训练样本。\\n\\n输入: DocRED JSON 文件目录或 HuggingFace dataset\\n输出: List[RelationSample]，每个样本包含 gold evidence 和 hard negative 句子\\n依赖: datasets (可选，用于 HF 加载)\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom dataclasses import dataclass, field\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nlogger = logging.getLogger(__name__)\\n\\nDOCRED_REL_INFO = {\\n    \\\"P6\\\": \\\"head of government\\\", \\\"P17\\\": \\\"country\\\", \\\"P19\\\": \\\"place of birth\\\",\\n    \\\"P20\\\": \\\"place of death\\\", \\\"P22\\\": \\\"father\\\", \\\"P25\\\": \\\"mother\\\",\\n    \\\"P26\\\": \\\"spouse\\\", \\\"P27\\\": \\\"country of citizenship\\\", \\\"P30\\\": \\\"continent\\\",\\n    \\\"P31\\\": \\\"instance of\\\", \\\"P35\\\": \\\"head of state\\\", \\\"P36\\\": \\\"capital\\\",\\n    \\\"P37\\\": \\\"official language\\\", \\\"P39\\\": \\\"position held\\\", \\\"P40\\\": \\\"child\\\",\\n    \\\"P50\\\": \\\"author\\\", \\\"P54\\\": \\\"member of sports team\\\", \\\"P57\\\": \\\"director\\\",\\n    \\\"P58\\\": \\\"screenwriter\\\", \\\"P69\\\": \\\"educated at\\\", \\\"P86\\\": \\\"composer\\\",\\n    \\\"P102\\\": \\\"member of political party\\\", \\\"P108\\\": \\\"employer\\\",\\n    \\\"P112\\\": \\\"founded by\\\", \\\"P118\\\": \\\"league\\\", \\\"P123\\\": \\\"publisher\\\",\\n    \\\"P127\\\": \\\"owned by\\\",\\n    \\\"P131\\\": \\\"located in the administrative territorial entity\\\",\\n    \\\"P136\\\": \\\"genre\\\", \\\"P137\\\": \\\"operator\\\", \\\"P140\\\": \\\"religion\\\",\\n    \\\"P150\\\": \\\"contains administrative territorial entity\\\",\\n    \\\"P155\\\": \\\"follows\\\", \\\"P156\\\": \\\"followed by\\\",\\n    \\\"P159\\\": \\\"headquarters location\\\", \\\"P161\\\": \\\"cast member\\\",\\n    \\\"P162\\\": \\\"producer\\\", \\\"P166\\\": \\\"award rece
…[truncated 8246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T07:46:23.532500+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -n \"def prepare_grpo_dataset\" /root/autodl-tmp/freige/training/grpo_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -n \"def prepare_grpo_dataset\" /root/autodl-tmp/freige/training/grpo_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T07:46:23.532637+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"252:def prepare_grpo_dataset(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T07:46:23.532764+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -n \"def compute_edcr\\|def compute_format\" /root/autodl-tmp/freige/eval/evaluator.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "grep -n \"def compute_edcr\\|def compute_format\" /root/autodl-tmp/freige/eval/evaluator.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T07:46:23.532886+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T07:46:23.533009+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -340 /root/autodl-tmp/freige/training/grpo_trainer.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "head -340 /root/autodl-tmp/freige/training/grpo_trainer.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T07:46:23.533270+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\\n\\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\\n\\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\\\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\\\\n            --stage 1 --reward_device cpu\\n不量化: 加 --no_quantize\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport math\\nimport os\\nimport re\\nfrom pathlib import Path\\nfrom typing import Optional\\n\\nimport torch\\nfrom datasets import Dataset\\nfrom peft import LoraConfig, PeftModel, TaskType\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\\nfrom trl import GRPOConfig, GRPOTrainer\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlogger = logging.getLogger(__name__)\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are an information extraction model. Given a document with numbered sentences \\\"\\n    \\\"and a list of entities, extract all relation triples. For each triple, provide the \\\"\\n    \\\"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \\\"\\n    \\\"Output as a JSON list.\\\"\\n)\\n\\n\\ndef _parse_json_output(text: str) -> list[dict]:\\n    \\\"\\\"\\\"从模型输出中解析 JSON 列表。\\\"\\\"\\\"\\n    try:\\n        return json.loads(text)\\n    except json.JSONDecodeError:\\n        start = text.find(\\\"[\\\")\\n        end = text.rfind(\\\"]\\\") + 1\\n        if start >= 0 and end > start:\\n            try:\\n                return json.loads(text[start:end])\\n            except json.JSONDecodeError:\\n                return []\\n    return []\\n\\n\\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\\n    \\\"\\\"\\\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\\\"\\\"\\\"\\n    rewards = []\\
…[truncated 7232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T07:46:23.533439+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -160 /root/autodl-tmp/freige/eval/evaluator.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "head -160 /root/autodl-tmp/freige/eval/evaluator.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T07:46:23.533648+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"DocRED 关系抽取评测模块。\\n\\n指标:\\n  - F1 / Ign-F1: 关系三元组级别 micro-F1，Ign-F1 排除训练集中出现的三元组\\n  - Evi-F1: 对正确预测的三元组，计算 evidence 句子级 F1\\n  - EDCR: Evidence Distractor Citation Rate，预测 evidence 中非 gold 的比例\\n\\n输入: 预测列表 + gold 标注列表（每个元素为文档级标注）\\n输出: 指标字典\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom collections import defaultdict\\nfrom typing import Optional\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef _triple_key(doc_id: str, head: str, tail: str, relation: str) -> tuple:\\n    return (doc_id, head.lower().strip(), tail.lower().strip(), relation)\\n\\n\\nclass DocREDEvaluator:\\n    \\\"\\\"\\\"DocRED 评测器。\\n\\n    Args:\\n        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。\\n                       每个元素为 (doc_title, head_name, tail_name, relation)。\\n                       为 None 时 Ign-F1 = F1。\\n    \\\"\\\"\\\"\\n\\n    def __init__(self, train_triples: Optional[set[tuple]] = None):\\n        self.train_triples = train_triples or set()\\n\\n    @classmethod\\n    def from_train_file(cls, train_path: str) -> \\\"DocREDEvaluator\\\":\\n        \\\"\\\"\\\"从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。\\\"\\\"\\\"\\n        from freige.data.docred_processor import DOCRED_REL_INFO\\n\\n        with open(train_path) as f:\\n            train_data = json.load(f)\\n\\n        train_triples = set()\\n        for doc in train_data:\\n            doc_id = doc.get(\\\"title\\\", \\\"\\\")\\n            vertex_set = doc[\\\"vertexSet\\\"]\\n            for label in doc.get(\\\"labels\\\", []):\\n                h_name = vertex_set[label[\\\"h\\\"]][0][\\\"name\\\"]\\n                t_name = vertex_set[label[\\\"t\\\"]][0][\\\"name\\\"]\\n                rel_name = DOCRED_REL_INFO.get(label[\\\"r\\\"], label[\\\"r\\\"])\\n                train_triples.add(\\n                    _triple_key(doc_id, h_name, t_name, rel_name)\\n                )\\n\\n        logger.info(\\\"Loaded %d training triples for Ign-F1\\\", 
…[truncated 3852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T07:46:23.534017+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat > /root/autodl-tmp/freige/eval/run_eval.py << 'SCRIPT_EOF'\n\"\"\"DocRED eval runner: 评估 SFT/GRPO checkpoint 在 DocRED dev set 上的 F1/Evi-F1/EDCR/format compliance。\n\n输入:\n  - base model (Qwen3-4B) + LoRA adapter (QLoRA 4-bit)\n  - DocRED JSON 数据目录 (含 dev.json, train_annotated.json)\n\n输出 (保存到 --output_dir):\n  - metrics.json: F1, Ign-F1, Evi-F1, EDCR, format_compliance_rate 等\n  - raw_predictions.json: 每个文档的原始模型输出\n\n用法:\n  cd /root/autodl-tmp && python -m freige.eval.run_eval \\\n    --model_name /root/autodl-tmp/models/Qwen3-4B \\\n    --adapter_path /root/autodl-tmp/sft_output \\\n    --data_dir /root/autodl-tmp/data/docred \\\n    --output_dir /root/autodl-tmp/eval_results/sft \\\n    --batch_size 4 --max_new_tokens 1024 --split dev\n\n依赖: transformers, peft, bitsandbytes, torch, tqdm\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport time\nfrom pathlib import Path\n\nimport torch\nfrom peft import PeftModel\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom tqdm import tqdm\n\nfrom freige.data.docred_processor import DocREDProcessor, SPLIT_FILENAMES\nfrom freige.eval.evaluator import DocREDEvaluator, gold_from_docred, parse_model_output\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\n# 与 sft_trainer / grpo_trainer 中定义一致\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef build_eval_prompt(tokenizer, instruction: str, input_text: str) -> str:\n    \"\"\"与训练时格式一致的 prompt，带 generation prompt。\"\"\"\n    messages = [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": f\"{instruction}\\n\\n{input_text}\"},\n    ]\n    return tokenizer.apply_chat_template(\n        messages,\n        tokenize=False,\n        add_generation_prompt=True,\n        enable_thinking=False,\n    )\n\n\ndef load_model_and_tokenizer(model_name: str, adapter_path: str, quantize: bool = True):\n    \"\"\"加载 base model + LoRA adapter (4-bit QLoRA)。\"\"\"\n    logger.info(\"Loading tokenizer: %s\", model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Loading model: %s\", model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n        device_map=\"auto\",\n    )\n    if quantize:\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)\n\n    if adapter_path:\n        logger.info(\"Loading LoRA adapter: %s\", adapter_path)\n        model = PeftModel.from_pretrained(model, adapter_path)\n\n    model.eval()\n    return model, tokenizer\n\n\ndef prepare_eval_data(data_dir: str, split: str, tokenizer):\n    \"\"\"加载 DocRED 数据，构建 eval prompts 和 gold 标注。\"\"\"\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    eval_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        prompt = build_eval_prompt(\n            tokenizer, sft_sample[\"instruction\"], sft_sample[\"input\"]\n        )\n        eval_items.append({\"doc_id\": doc_id, \"prompt\": prompt})\n\n    split_file = Path(data_dir) / SPLIT_FILENAMES[split]\n    with open(split_file) as f:\n        raw_docred = json.load(f)\n    gold = gold_from_docred(raw_docred)\n\n    logger.info(\"Prepared %d eval documents, %d gold triples\", len(eval_items), len(gold))\n    return eval_items, gold\n\n\ndef _get_input_device(model):\n    \"\"\"获取模型输入应放置的设备。\"\"\"\n    if hasattr(model, \"hf_device_map\"):\n        first_device = next(iter(model.hf_device_map.values()))\n        return f\"cuda:{first_device}\" if isinstance(first_device, int) else first_device\n    base = getattr(model, \"base_model\", model)\n    if hasattr(base, \"hf_device_map\"):\n        first_device = next(iter(base.hf_device_map.values()))\n        return f\"cuda:{first_device}\" if isinstance(first_device, int) else first_device\n    return model.device\n\n\n@torch.no_grad()\ndef run_inference(model, tokenizer, eval_items, batch_size, max_new_tokens):\n    \"\"\"Batch inference with greedy decoding.\"\"\"\n    results = []\n    n_truncated = 0\n    device = _get_input_device(model)\n\n    for i in tqdm(range(0, len(eval_items), batch_size), desc=\"Inference\"):\n        batch = eval_items[i : i + batch_size]\n        prompts = [item[\"prompt\"] for item in batch]\n\n        inputs = tokenizer(\n            prompts,\n            return_tensors=\"pt\",\n            padding=True,\n            truncation=True,\n            max_length=4096,\n        ).to(device)\n\n        prompt_len = inputs[\"input_ids\"].shape[1]\n\n        outputs = model.generate(\n            **inputs,\n            max_new_tokens=max_new_tokens,\n            do_sample=False,\n            pad_token_id=tokenizer.pad_token_id,\n        )\n\n        for j, item in enumerate(batch):\n            generated_ids = outputs[j][prompt_len:]\n\n            # 移除尾部 pad tokens（batch 中短序列会被 pad 到最长）\n            if tokenizer.pad_token_id is not None:\n                mask = generated_ids != tokenizer.pad_token_id\n                if mask.any():\n                    last_real = mask.nonzero()[-1].item() + 1\n                    generated_ids = generated_ids[:last_real]\n                else:\n                    generated_ids = generated_ids[:0]\n\n            generated_text = tokenizer.decode(\n                generated_ids, skip_special_tokens=True\n            )\n\n            truncated = len(generated_ids) >= max_new_tokens\n            if truncated:\n                n_truncated += 1\n                logger.warning(\"Truncated output for doc: %s\", item[\"doc_id\"])\n\n            results.append({\n                \"doc_id\": item[\"doc_id\"],\n                \"output\": generated_text,\n                \"truncated\": truncated,\n            })\n\n    logger.info(\"Inference done. %d/%d truncated.\", n_truncated, len(eval_items))\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"FREIGE Eval Runner: 评估 checkpoint 在 DocRED 上的 F1/Evi-F1/EDCR\"\n    )\n    parser.add_argument(\"--model_name\", type=str, required=True,\n                        help=\"Base model path (e.g. /root/autodl-tmp/models/Qwen3-4B)\")\n    parser.add_argument(\"--adapter_path\", type=str, default=None,\n                        help=\"LoRA adapter path (e.g. /root/autodl-tmp/sft_output)\")\n    parser.add_argument(\"--data_dir\", type=str, required=True,\n                        help=\"DocRED JSON directory (contains dev.json, train_annotated.json)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for metrics and predictions\")\n    parser.add_argument(\"--split\", type=str, default=\"dev\",\n                        choices=[\"dev\", \"test\"],\n                        help=\"Eval split (default: dev)\")\n    parser.add_argument(\"--batch_size\", type=int, default=4)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction,\n                        default=True,\n                        help=\"4-bit NF4 quantization (default: on, --no_quantize to disable)\")\n    args = parser.parse_args()\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    model, tokenizer = load_model_and_tokenizer(\n        args.model_name, args.adapter_path, args.quantize\n    )\n\n    eval_items, gold = prepare_eval_data(args.data_dir, args.split, tokenizer)\n\n    t0 = time.time()\n    raw_results = run_inference(\n        model, tokenizer, eval_items, args.batch_size, args.max_new_tokens\n    )\n    elapsed = time.time() - t0\n    logger.info(\n        \"Inference took %.1f seconds (%.2f s/doc)\",\n        elapsed, elapsed / len(eval_items),\n    )\n\n    # 解析模型输出 → 标准预测格式\n    all_predictions = []\n    raw_outputs = []\n    for r in raw_results:\n        preds = parse_model_output(r[\"doc_id\"], r[\"output\"])\n        all_predictions.extend(preds)\n        raw_outputs.append({\"doc_id\": r[\"doc_id\"], \"output\": r[\"output\"]})\n\n    # Ign-F1 需要训练集三元组\n    train_path = Path(args.data_dir) / \"train_annotated.json\"\n    if train_path.exists():\n        evaluator = DocREDEvaluator.from_train_file(str(train_path))\n    else:\n        logger.warning(\"train_annotated.json not found, Ign-F1 will equal F1\")\n        evaluator = DocREDEvaluator()\n\n    metrics = evaluator.evaluate(all_predictions, gold, raw_outputs)\n\n    metrics[\"n_documents\"] = len(eval_items)\n    metrics[\"n_predictions\"] = len(all_predictions)\n    metrics[\"n_truncated\"] = sum(1 for r in raw_results if r[\"truncated\"])\n    metrics[\"inference_time_seconds\"] = round(elapsed, 1)\n    metrics[\"config\"] = vars(args)\n\n    # 保存 metrics\n    metrics_path = output_dir / \"metrics.json\"\n    with open(metrics_path, \"w\") as f:\n        json.dump(metrics, f, indent=2, ensure_ascii=False)\n    logger.info(\"Metrics saved to %s\", metrics_path)\n\n    # 保存原始预测\n    raw_path = output_dir / \"raw_predictions.json\"\n    with open(raw_path, \"w\") as f:\n        json.dump(raw_results, f, indent=2, ensure_ascii=False)\n    logger.info(\"Raw predictions saved to %s\", raw_path)\n\n    # 打印关键指标\n    print(\"\\n\" + \"=\" * 50)\n    print(f\"  F1:         {metrics['f1']:.4f}\")\n    print(f\"  Ign-F1:     {metrics['ign_f1']:.4f}\")\n    print(f\"  Evi-F1:     {metrics['evi_f1']:.4f}\")\n    print(f\"  EDCR:       {metrics.get('edcr', 0):.4f}\")\n    print(f\"  Format OK:  {metrics.get('format_compliance_rate', 0):.4f}\")\n    print(f\"  Truncated:  {metrics['n_truncated']}/{metrics['n_documents']}\")\n    print(\"=\" * 50)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat > /root/autodl-tmp/freige/eval/run_eval.py << 'SCRIPT_EOF'\n\"\"\"DocRED eval runner: 评估 SFT/GRPO checkpoint 在 DocRED dev set 上的 F1/Evi-F1/EDCR/format compliance。\n\n输入:\n  - base model (Qwen3-4B) + LoRA adapter (QLoRA 4-bit)\n  - DocRED JSON 数据目录 (含 dev.json, train_annotated.json)\n\n输出 (保存到 --output_dir):\n  - metrics.json: F1, Ign-F1, Evi-F1, EDCR, format_compliance_rate 等\n  - raw_predictions.json: 每个文档的原始模型输出\n\n用法:\n  cd /root/autodl-tmp && python -m freige.eval.run_eval \\\n    --model_name /root/autodl-tmp/models/Qwen3-4B \\\n    --adapter_path /root/autodl-tmp/sft_output \\\n    --data_dir /root/autodl-tmp/data/docred \\\n    --output_dir /root/autodl-tmp/eval_results/sft \\\n    --batch_size 4 --max_new_tokens 1024 --split dev\n\n依赖: transformers, peft, bitsandbytes, torch, tqdm\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport time\nfrom pathlib import Path\n\nimport torch\nfrom peft import PeftModel\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom tqdm import tqdm\n\nfrom freige.data.docred_processor import DocREDProcessor, SPLIT_FILENAMES\nfrom freige.eval.evaluator import DocREDEvaluator, gold_from_docred, parse_model_output\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\n# 与 sft_trainer / grpo_trainer 中定义一致\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef build_eval_prompt(tokenizer, instruction: str, input_text: str) -> str:\n    \"\"\"与训练时格式一致的 prompt，带 generation prompt。\"\"\"\n    messages = [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": f\"{instruction}\\n\\n{input_text}\"},\n    ]\n    return tokenizer.apply_chat_template(\n        messages,\n        tokenize=False,\n        add_generation_prompt=True,\n        enable_thinking=False,\n    )\n\n\ndef load_model_and_tokenizer(model_name: str, adapter_path: str, quantize: bool = True):\n    \"\"\"加载 base model + LoRA adapter (4-bit QLoRA)。\"\"\"\n    logger.info(\"Loading tokenizer: %s\", model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Loading model: %s\", model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n        device_map=\"auto\",\n    )\n    if quantize:\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16\n\n    model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)\n\n    if adapter_path:\n        logger.info(\"Loading LoRA adapter: %s\", adapter_path)\n        model = PeftModel.from_pretrained(model, adapter_path)\n\n    model.eval()\n    return model, tokenizer\n\n\ndef prepare_eval_data(data_dir: str, split: str, tokenizer):\n    \"\"\"加载 DocRED 数据，构建 eval prompts 和 gold 标注。\"\"\"\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    eval_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        prompt = build_eval_prompt(\n            tokenizer, sft_sample[\"instruction\"], sft_sample[\"input\"]\n        )\n        eval_items.append({\"doc_id\": doc_id, \"prompt\": prompt})\n\n    split_file = Path(data_dir) / SPLIT_FILENAMES[split]\n    with open(split_file) as f:\n        raw_docred = json.load(f)\n    gold = gold_from_docred(raw_docred)\n\n    logger.info(\"Prepared %d eval documents, %d gold triples\", len(eval_items), len(gold))\n    return eval_items, gold\n\n\ndef _get_input_device(model):\n    \"\"\"获取模型输入应放置的设备。\"\"\"\n    if hasattr(model, \"hf_device_map\"):\n        first_device = next(iter(model.hf_device_map.values()))\n        return f\"cuda:{first_device}\" if isinstance(first_device, int) else first_device\n    base = getattr(model, \"base_model\", model)\n    if hasattr(base, \"hf_device_map\"):\n        first_device = next(iter(base.hf_device_map.values()))\n        return f\"cuda:{first_device}\" if isinstance(first_device, int) else first_device\n    return model.device\n\n\n@torch.no_grad()\ndef run_inference(model, tokenizer, eval_items, batch_size, max_new_tokens):\n    \"\"\"Batch inference with greedy decoding.\"\"\"\n    results = []\n    n_truncated = 0\n    device = _get_input_device(model)\n\n    for i in tqdm(range(0, len(eval_items), batch_size), desc=\"Inference\"):\n        batch = eval_items[i : i + batch_size]\n        prompts = [item[\"prompt\"] for item in batch]\n\n        inputs = tokenizer(\n            prompts,\n            return_tensors=\"pt\",\n            padding=True,\n            truncation=True,\n            max_length=4096,\n        ).to(device)\n\n        prompt_len = inputs[\"input_ids\"].shape[1]\n\n        outputs = model.generate(\n            **inputs,\n            max_new_tokens=max_new_tokens,\n            do_sample=False,\n            pad_token_id=tokenizer.pad_token_id,\n        )\n\n        for j, item in enumerate(batch):\n            generated_ids = outputs[j][prompt_len:]\n\n            # 移除尾部 pad tokens（batch 中短序列会被 pad 到最长）\n            if tokenizer.pad_token_id is not None:\n                mask = generated_ids != tokenizer.pad_token_id\n                if mask.any():\n                    last_real = mask.nonzero()[-1].item() + 1\n                    generated_ids = generated_ids[:last_real]\n                else:\n                    generated_ids = generated_ids[:0]\n\n            generated_text = tokenizer.decode(\n                generated_ids, skip_special_tokens=True\n            )\n\n            truncated = len(generated_ids) >= max_new_tokens\n            if truncated:\n                n_truncated += 1\n                logger.warning(\"Truncated output for doc: %s\", item[\"doc_id\"])\n\n            results.append({\n                \"doc_id\": item[\"doc_id\"],\n                \"output\": generated_text,\n                \"truncated\": truncated,\n            })\n\n    logger.info(\"Inference done. %d/%d truncated.\", n_truncated, len(eval_items))\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"FREIGE Eval Runner: 评估 checkpoint 在 DocRED 上的 F1/Evi-F1/EDCR\"\n    )\n    parser.add_argument(\"--model_name\", type=str, required=True,\n                        help=\"Base model path (e.g. /root/autodl-tmp/models/Qwen3-4B)\")\n    parser.add_argument(\"--adapter_path\", type=str, default=None,\n                        help=\"LoRA adapter path (e.g. /root/autodl-tmp/sft_output)\")\n    parser.add_argument(\"--data_dir\", type=str, required=True,\n                        help=\"DocRED JSON directory (contains dev.json, train_annotated.json)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for metrics and predictions\")\n    parser.add_argument(\"--split\", type=str, default=\"dev\",\n                        choices=[\"dev\", \"test\"],\n                        help=\"Eval split (default: dev)\")\n    parser.add_argument(\"--batch_size\", type=int, default=4)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction,\n                        default=True,\n                        help=\"4-bit NF4 quantization (default: on, --no_quantize to disable)\")\n    args = parser.parse_args()\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    model, tokenizer = load_model_and_tokenizer(\n        args.model_name, args.adapter_path, args.quantize\n    )\n\n    eval_items, gold = prepare_eval_data(args.data_dir, args.split, tokenizer)\n\n    t0 = time.time()\n    raw_results = run_inference(\n        model, tokenizer, eval_items, args.batch_size, args.max_new_tokens\n    )\n    elapsed = time.time() - t0\n    logger.info(\n        \"Inference took %.1f seconds (%.2f s/doc)\",\n        elapsed, elapsed / len(eval_items),\n    )\n\n    # 解析模型输出 → 标准预测格式\n    all_predictions = []\n    raw_outputs = []\n    for r in raw_results:\n        preds = parse_model_output(r[\"doc_id\"], r[\"output\"])\n        all_predictions.extend(preds)\n        raw_outputs.append({\"doc_id\": r[\"doc_id\"], \"output\": r[\"output\"]})\n\n    # Ign-F1 需要训练集三元组\n    train_path = Path(args.data_dir) / \"train_annotated.json\"\n    if train_path.exists():\n        evaluator = DocREDEvaluator.from_train_file(str(train_path))\n    else:\n        logger.warning(\"train_annotated.json not found, Ign-F1 will equal F1\")\n        evaluator = DocREDEvaluator()\n\n    metrics = evaluator.evaluate(all_predictions, gold, raw_outputs)\n\n    metrics[\"n_documents\"] = len(eval_items)\n    metrics[\"n_predictions\"] = len(all_predictions)\n    metrics[\"n_truncated\"] = sum(1 for r in raw_results if r[\"truncated\"])\n    metrics[\"inference_time_seconds\"] = round(elapsed, 1)\n    metrics[\"config\"] = vars(args)\n\n    # 保存 metrics\n    metrics_path = output_dir / \"metrics.json\"\n    with open(metrics_path, \"w\") as f:\n        json.dump(metrics, f, indent=2, ensure_ascii=False)\n    logger.info(\"Metrics saved to %s\", metrics_path)\n\n    # 保存原始预测\n    raw_path = output_dir / \"raw_predictions.json\"\n    with open(raw_path, \"w\") as f:\n        json.dump(raw_results, f, indent=2, ensure_ascii=False)\n    logger.info(\"Raw predictions saved to %s\", raw_path)\n\n    # 打印关键指标\n    print(\"\\n\" + \"=\" * 50)\n    print(f\"  F1:         {metrics['f1']:.4f}\")\n    print(f\"  Ign-F1:     {metrics['ign_f1']:.4f}\")\n    print(f\"  Evi-F1:     {metrics['evi_f1']:.4f}\")\n    print(f\"  EDCR:       {metrics.get('edcr', 0):.4f}\")\n    print(f\"  Format OK:  {metrics.get('format_compliance_rate', 0):.4f}\")\n    print(f\"  Truncated:  {metrics['n_truncated']}/{metrics['n_documents']}\")\n    print(\"=\" * 50)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T07:46:23.534302+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T07:46:23.534453+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cd /root/autodl-tmp && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -m freige.eval.run_eval --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cd /root/autodl-tmp && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -m freige.eval.run_eval --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T07:46:23.534601+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: run_eval.py [-h] --model_name MODEL_NAME [--adapter_path ADAPTER_PATH]\\n                   --data_dir DATA_DIR --output_dir OUTPUT_DIR\\n                   [--split {dev,test}] [--batch_size BATCH_SIZE]\\n                   [--max_new_tokens MAX_NEW_TOKENS]\\n                   [--quantize | --no-quantize]\\n\\nFREIGE Eval Runner: 评估 checkpoint 在 DocRED 上的 F1/Evi-F1/EDCR\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --model_name MODEL_NAME\\n                        Base model path (e.g. /root/autodl-\\n                        tmp/models/Qwen3-4B)\\n  --adapter_path ADAPTER_PATH\\n                        LoRA adapter path (e.g. /root/autodl-tmp/sft_output)\\n  --data_dir DATA_DIR   DocRED JSON directory (contains dev.json,\\n                        train_annotated.json)\\n  --output_dir OUTPUT_DIR\\n                        Output directory for metrics and predictions\\n  --split {dev,test}    Eval split (default: dev)\\n  --batch_size BATCH_SIZE\\n  --max_new_tokens MAX_NEW_TOKENS\\n  --quantize, --no-quantize\\n                        4-bit NF4 quantization (default: on, --no_quantize to\\n                        disable)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_write-eval-runner_20260514T074007",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T07:46:23.534774+00:00_

脚本已写入 `/root/autodl-tmp/freige/eval/run_eval.py`，导入和参数解析验证通过。

运行示例：
```bash
cd /root/autodl-tmp && python -m freige.eval.run_eval \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --adapter_path /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/eval_results/sft \
  --batch_size 4 --max_new_tokens 1024 --split dev
```

输出两个文件到 `--output_dir`：
- `metrics.json` — F1, Ign-F1, Evi-F1, EDCR, format_compliance_rate, n_truncated 等
- `raw_predictions.json` — 每个文档的原始模型输出 + truncated 标记

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_write-eval-runner_20260514T074007"
}
```

</details>

---
