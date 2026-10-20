# code mvp2 prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 76
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/workers/worker_code_mvp2-prep_20260514T060832.log`
- **Structured JSON:** [`a6e4bb80386f6799970c.json`](../../sessions/a6/a6e4bb80386f6799970c.json)

## Before a recorded user message

76 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "73fea973-0ab3-4285-a784-16838247ccf3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778748000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f6a53976-9ac3-46e8-aa7b-992f1d81a474",
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0"
}
```

---

### Assistant

_source line 4_

Let me start by reading all the files that need to be modified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "bd66c6ed-9a07-42cc-a02e-a3812f97f290",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7fvKH42Er9jmjHQzrFxK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12691,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12691
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01XhBmvjUn2KfkGBKMTE2bNd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "f70a094c-6501-445f-b50c-22ac1f7ec504",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7fvKH42Er9jmjHQzrFxK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12691,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12691
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T06:08:46.987Z_

<details><summary>↩ Tool result · `toolu_01XhBmvjUn2KfkGBKMTE2bNd`</summary>

```text
1	"""SFT 训练脚本: Qwen3-4B + QLoRA 在 DocRED 上微调。
2	
3	支持单卡和多卡（DeepSpeed ZeRO-2/3）训练。
4	默认启用 4-bit QLoRA 量化，适配 RTX 5090 32GB x4。
5	
6	单卡:   python -m freige.training.sft_trainer --output_dir ./sft_output
7	多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
8	            -m freige.training.sft_trainer --deepspeed configs/deepspeed_zero2.json
9	不量化: 加 --no_quantize
10	"""
11	
12	import argparse
13	import json
14	import logging
15	import os
16	from dataclasses import dataclass, field
17	from pathlib import Path
18	from typing import Optional
19	
20	import torch
21	from datasets import Dataset
22	from peft import LoraConfig, TaskType, get_peft_model
23	from transformers import (
24	    AutoModelForCausalLM,
25	    AutoTokenizer,
26	    BitsAndBytesConfig,
27	    TrainingArguments,
28	)
29	from trl import SFTTrainer, SFTConfig
30	
31	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
32	logger = logging.getLogger(__name__)
33	
34	SYSTEM_PROMPT = (
35	    "You are an information extraction model. Given a document with numbered sentences "
36	    "and a list of entities, extract all relation triples. For each triple, provide the "
37	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
38	    "Output as a JSON list."
39	)
40	
41	DEFAULT_MODEL = "Qwen/Qwen3-4B"
42	
43	
44	def build_chat_messages(instruction: str, input_text: str, output_text: str = None):
45	    """构建 Qwen3 chat 格式的消息列表。"""
46	    messages = [
47	        {"role": "system", "content": SYSTEM_PROMPT},
48	        {"role": "user", "content": f"{instruction}\n\n{input_text}"},
49	    ]
50	    if output_text is not None:
51	        messages.append({"role": "assistant", "content": output_text})
52	    return messages
53	
54	
55	def prepare_dataset(
56	    data_dir: str = None,
57	    split: str = "train",
58	    tokenizer=None,
59	    max_length: int = 4096,
60	) -> Dataset:
61	    """加载并格式化 DocRED 数据为 SFT 训练格式。"""
62	    from freige.data.docred_processor import DocREDProcessor
63	
64	    processor = DocREDProcessor(data_dir=data_dir)
65	    samples = processor.process(split)
66	    groups = processor.group_by_document(samples)
67	
68	    formatted = []
69	    for doc_id, doc_samples in groups.items():
70	        sft_sample = processor.format_sft_sample(doc_samples)
71	        messages = build_chat_messages(
72	            sft_sample["instruction"],
73	            sft_sample["input"],
74	            sft_sample["output"],
75	        )
76	        text = tokenizer.apply_chat_template(
77	            messages,
78	            tokenize=False,
79	            add_generation_prompt=False,
80	            enable_thinking=False,
81	        )
82	        formatted.append({"text": text})
83	
84	    logger.info("Prepared %d SFT samples from %d documents", len(formatted), len(groups))
85	    return Dataset.from_list(formatted)
86	
87	
88	def main():
89	    parser = argparse.ArgumentParser(description="FREIGE SFT Training")
90	    parser.add_argument("--model_name", type=str, default=DEFAULT_MODEL)
91	    parser.add_argument("--data_dir", type=str, default=None,
92	                        help="DocRED JSON 目录")
93	    parser.add_argument("--output_dir", type=str, default="./sft_output")
94	    parser.add_argument("--lora_rank", type=int, default=64)
95	    parser.add_argument("--lora_alpha", type=int, default=128)
96	    parser.add_argument("--lora_dropout", type=float, default=0.05)
97	    parser.add_argument("--max_length", type=int, default=4096)
98	    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction, default=True,
99	                        help="启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）")
100	    parser.add_argument("--deepspeed", type=str, default=None,
101	                        help="DeepSpeed 配置文件路径")
102	    parser.add_argument("--per_device_batch_size", type=int, default=1)
103	    parser.add_argument("--gradient_accumulation_steps", type=int, default=16)
104	    parser.add_argument("--num_epochs", type=int, default=3)
105	    parser.add_argument("--learning_rate", type=float, default=2e-4)
106	    parser.add_argument("--warmup_ratio", type=float, default=0.05)
107	    parser.add_argument("--bf16", action="store_true", default=True)
108	    parser.add_argument("--seed", type=int, default=42)
109	    parser.add_argument("--wandb_project", type=str, default="freige-sft")
110	    parser.add_argument("--wandb_run_name", type=str, default=None)
111	    args = parser.parse_args()
112	
113	    if args.wandb_project and "WANDB_API_KEY" in os.environ:
114	        os.environ["WANDB_PROJECT"] = args.wandb_project
115	        if args.wandb_run_name:
116	            os.environ["WANDB_NAME"] = args.wandb_run_name
117	
118	    logger.info("Loading tokenizer: %s", args.model_name)
119	    tokenizer = AutoTokenizer.from_pretrained(
120	        args.model_name,
121	        trust_remote_code=True,
122	        padding_side="right",
123	    )
124	    if tokenizer.pad_token is None:
125	        tokenizer.pad_token = tokenizer.eos_token
126	
127	    logger.info("Preparing dataset...")
128	    train_dataset = prepare_dataset(
129	        data_dir=args.data_dir,
130	        split="train",
131	        tokenizer=tokenizer,
132	        max_length=args.max_length,
133	    )
134	    eval_dataset = prepare_dataset(
135	        data_dir=args.data_dir,
136	        split="dev",
137	        tokenizer=tokenizer,
138	        max_length=args.max_length,
139	    )
140	
141	    logger.info("Loading model: %s", args.model_name)
142	    model_kwargs = dict(
143	        trust_remote_code=True,
144	        attn_implementation="flash_attention_2",
145	    )
146	    if args.quantize:
147	        logger.info("Using 4-bit QLoRA quantization")
148	        model_kwargs["quantization_config"] = BitsAndBytesConfig(
149	            load_in_4bit=True,
150	            bnb_4bit_compute_dtype=torch.bfloat16,
151	            bnb_4bit_quant_type="nf4",
152	            bnb_4bit_use_double_quant=True,
153	        )
154	    else:
155	        model_kwargs["torch_dtype"] = torch.bfloat16 if args.bf16 else torch.float16
156	    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)
157	    model.config.use_cache = False
158	    model.gradient_checkpointing_enable()
159	
160	    lora_config = LoraConfig(
161	        task_type=TaskType.CAUSAL_LM,
162	        r=args.lora_rank,
163	        lora_alpha=args.lora_alpha,
164	        lora_dropout=args.lora_dropout,
165	        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
166	                         "gate_proj", "up_proj", "down_proj"],
167	    )
168	    model = get_peft_model(model, lora_config)
169	    model.print_trainable_parameters()
170	
171	    training_args = SFTConfig(
172	        output_dir=args.output_dir,
173	        num_train_epochs=args.num_epochs,
174	        per_device_train_batch_size=args.per_device_batch_size,
175	        per_device_eval_batch_size=args.per_device_batch_size,
176	        gradient_accumulation_steps=args.gradient_accumulation_steps,
177	        learning_rate=args.learning_rate,
178	        warmup_ratio=args.warmup_ratio,
179	        bf16=args.bf16,
180	        logging_steps=10,
181	        eval_strategy="epoch",
182	        save_strategy="epoch",
183	        save_total_limit=2,
184	        load_best_model_at_end=True,
185	        metric_for_best_model="eval_loss",
186	        greater_is_better=False,
187	        seed=args.seed,
188	        max_seq_length=args.max_length,
189	        dataset_text_field="text",
190	        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
191	        gradient_checkpointing=True,
192	        gradient_checkpointing_kwargs={"use_reentrant": False},
193	        deepspeed=args.deepspeed,
194	    )
195	
196	    trainer = SFTTrainer(
197	        model=model,
198	        args=training_args,
199	        train_dataset=train_dataset,
200	        eval_dataset=eval_dataset,
201	        tokenizer=tokenizer,
202	    )
203	
204	    logger.info("Starting SFT training...")
205	    trainer.train()
206	
207	    logger.info("Saving model to %s", args.output_dir)
208	    trainer.save_model(args.output_dir)
209	    tokenizer.save_pretrained(args.output_dir)
210	    logger.info("SFT training complete.")
211	
212	
213	if __name__ == "__main__":
214	    main()
215	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "89a8585e-3912-4aea-aee0-469b3334975c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
      "content": "\"\"\"SFT 训练脚本: Qwen3-4B + QLoRA 在 DocRED 上微调。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练。\n默认启用 4-bit QLoRA 量化，适配 RTX 5090 32GB x4。\n\n单卡:   python -m freige.training.sft_trainer --output_dir ./sft_output\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.sft_trainer --deepspeed configs/deepspeed_zero2.json\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nfrom dataclasses import dataclass, field\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, TaskType, get_peft_model\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    BitsAndBytesConfig,\n    TrainingArguments,\n)\nfrom trl import SFTTrainer, SFTConfig\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\nDEFAULT_MODEL = \"Qwen/Qwen3-4B\"\n\n\ndef build_chat_messages(instruction: str, input_text: str, output_text: str = None):\n    \"\"\"构建 Qwen3 chat 格式的消息列表。\"\"\"\n    messages = [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": f\"{instruction}\\n\\n{input_text}\"},\n    ]\n    if output_text is not None:\n        messages.append({\"role\": \"assistant\", \"content\": output_text})\n    return messages\n\n\ndef prepare_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n    max_length: int = 4096,\n) -> Dataset:\n    \"\"\"加载并格式化 DocRED 数据为 SFT 训练格式。\"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    formatted = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = build_chat_messages(\n            sft_sample[\"instruction\"],\n            sft_sample[\"input\"],\n            sft_sample[\"output\"],\n        )\n        text = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=False,\n            enable_thinking=False,\n        )\n        formatted.append({\"text\": text})\n\n    logger.info(\"Prepared %d SFT samples from %d documents\", len(formatted), len(groups))\n    return Dataset.from_list(formatted)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE SFT Training\")\n    parser.add_argument(\"--model_name\", type=str, default=DEFAULT_MODEL)\n    parser.add_argument(\"--data_dir\", type=str, default=None,\n                        help=\"DocRED JSON 目录\")\n    parser.add_argument(\"--output_dir\", type=str, default=\"./sft_output\")\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--lora_dropout\", type=float, default=0.05)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=3)\n    parser.add_argument(\"--learning_rate\", type=float, default=2e-4)\n    parser.add_argument(\"--warmup_ratio\", type=float, default=0.05)\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-sft\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"right\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n        max_length=args.max_length,\n    )\n    eval_dataset = prepare_dataset(\n        data_dir=args.data_dir,\n        split=\"dev\",\n        tokenizer=tokenizer,\n        max_length=args.max_length,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n    model.config.use_cache = False\n    model.gradient_checkpointing_enable()\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=args.lora_dropout,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n    model = get_peft_model(model, lora_config)\n    model.print_trainable_parameters()\n\n    training_args = SFTConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        per_device_eval_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        warmup_ratio=args.warmup_ratio,\n        bf16=args.bf16,\n        logging_steps=10,\n        eval_strategy=\"epoch\",\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        load_best_model_at_end=True,\n        metric_for_best_model=\"eval_loss\",\n        greater_is_better=False,\n        seed=args.seed,\n        max_seq_length=args.max_length,\n        dataset_text_field=\"text\",\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = SFTTrainer(\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        eval_dataset=eval_dataset,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting SFT training...\")\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"SFT training complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 215,
      "startLine": 1,
      "totalLines": 215
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01BK4JnBPBupRcpv8AaxXrwv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "7b2fac7a-7664-4915-a8d2-eb205c427828",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7fvKH42Er9jmjHQzrFxK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12691,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12691
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T06:08:47.751Z_

<details><summary>↩ Tool result · `toolu_01BK4JnBPBupRcpv8AaxXrwv`</summary>

```text
1	"""GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。
2	
3	支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。
4	
5	单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1
6	多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
7	            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero3.json \
8	            --stage 1 --reward_device cpu
9	不量化: 加 --no_quantize
10	"""
11	
12	import argparse
13	import json
14	import logging
15	import os
16	import re
17	from pathlib import Path
18	from typing import Optional
19	
20	import torch
21	from datasets import Dataset
22	from peft import LoraConfig, PeftModel, TaskType
23	from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
24	from trl import GRPOConfig, GRPOTrainer
25	
26	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
27	logger = logging.getLogger(__name__)
28	
29	SYSTEM_PROMPT = (
30	    "You are an information extraction model. Given a document with numbered sentences "
31	    "and a list of entities, extract all relation triples. For each triple, provide the "
32	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
33	    "Output as a JSON list."
34	)
35	
36	
37	def _parse_json_output(text: str) -> list[dict]:
38	    """从模型输出中解析 JSON 列表。"""
39	    try:
40	        return json.loads(text)
41	    except json.JSONDecodeError:
42	        start = text.find("[")
43	        end = text.rfind("]") + 1
44	        if start >= 0 and end > start:
45	            try:
46	                return json.loads(text[start:end])
47	            except json.JSONDecodeError:
48	                return []
49	    return []
50	
51	
52	def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
53	    """格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。"""
54	    rewards = []
55	    for text in completions:
56	        parsed = _parse_json_output(text)
57	        if not isinstance(parsed, list):
58	            rewards.append(0.0)
59	            continue
60	        if not parsed:
61	            rewards.append(0.1)
62	            continue
63	        valid = 0
64	        for item in parsed:
65	            if (isinstance(item, dict) and "head" in item
66	                    and "relation" in item and "tail" in item
67	                    and "evidence" in item
68	                    and isinstance(item["evidence"], list)):
69	                valid += 1
70	        rewards.append(valid / len(parsed))
71	    return rewards
72	
73	
74	def f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:
75	    """F1 奖励: 预测三元组与 gold 三元组的 micro-F1。
76	
77	    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。
78	    completions 中每 num_generations 个对应同一个 prompt。
79	    """
80	    num_gen = len(completions) // len(gold_triples)
81	    rewards = []
82	
83	    for i, text in enumerate(completions):
84	        gold_idx = i // num_gen
85	        gold_str = gold_triples[gold_idx]
86	        try:
87	            gold = json.loads(gold_str)
88	        except (json.JSONDecodeError, IndexError):
89	            rewards.append(0.0)
90	            continue
91	
92	        pred = _parse_json_output(text)
93	
94	        gold_set = set()
95	        for g in gold:
96	            gold_set.add((
97	                g.get("head", "").lower().strip(),
98	                g.get("relation", "").lower().strip(),
99	                g.get("tail", "").lower().strip(),
100	            ))
101	
102	        pred_set = set()
103	        for p in pred:
104	            if isinstance(p, dict):
105	                pred_set.add((
106	                    p.get("head", "").lower().strip(),
107	                    p.get("relation", "").lower().strip(),
108	                    p.get("tail", "").lower().strip(),
109	                ))
110	
111	        if not gold_set:
112	            rewards.append(1.0 if not pred_set else 0.0)
113	            continue
114	
115	        tp = len(pred_set & gold_set)
116	        prec = tp / len(pred_set) if pred_set else 0.0
117	        rec = tp / len(gold_set) if gold_set else 0.0
118	        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
119	        rewards.append(f1)
120	
121	    return rewards
122	
123	
124	class CEDRewardWrapper:
125	    """将 CED 奖励封装为 GRPO 兼容的 reward function。
126	
127	    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，
128	    返回所有 triples 的平均 CED reward。
129	    """
130	
131	    def __init__(
132	        self,
133	        nli_model: str = "cross-encoder/nli-deberta-v3-base",
134	        tau: float = 0.5,
135	        mode: str = "ced",
136	        device: str = None,
137	    ):
138	        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple
139	        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)
140	        self.verbalize = verbalize_triple
141	        self.tau = tau
142	        self.mode = mode
143	
144	    def __call__(
145	        self,
146	        completions: list[str],
147	        all_sents: list[str],
148	        gold_triples: list[str],
149	        **kwargs,
150	    ) -> list[float]:
151	        """计算 CED/flat-NLI 奖励。
152	
153	        all_sents: JSON 字符串列表，每个元素为文档句子列表。
154	        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。
155	        """
156	        num_gen = len(completions) // len(all_sents)
157	        rewards = []
158	
159	        for i, text in enumerate(completions):
160	            prompt_idx = i // num_gen
161	            try:
162	                sents = json.loads(all_sents[prompt_idx])
163	                gold = json.loads(gold_triples[prompt_idx])
164	            except (json.JSONDecodeError, IndexError):
165	                rewards.append(0.0)
166	                continue
167	
168	            pred = _parse_json_output(text)
169	            if not pred:
170	                rewards.append(0.0)
171	                continue
172	
173	            gold_map = {}
174	            for g in gold:
175	                key = (
176	                    g.get("head", "").lower().strip(),
177	                    g.get("relation", "").lower().strip(),
178	                    g.get("tail", "").lower().strip(),
179	                )
180	                gold_map[key] = g
181	
182	            triple_rewards = []
183	            for p in pred:
184	                if not isinstance(p, dict):
185	                    continue
186	                pred_evi_ids = p.get("evidence", [])
187	                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:
188	                    triple_rewards.append(0.0)
189	                    continue
190	
191	                claim = self.verbalize(
192	                    p.get("head", ""),
193	                    p.get("relation", ""),
194	                    p.get("tail", ""),
195	                )
196	                cited_sents = [sents[idx] for idx in pred_evi_ids
197	                               if isinstance(idx, int) and 0 <= idx < len(sents)]
198	                if not cited_sents:
199	                    triple_rewards.append(0.0)
200	                    continue
201	
202	                key = (
203	                    p.get("head", "").lower().strip(),
204	                    p.get("relation", "").lower().strip(),
205	                    p.get("tail", "").lower().strip(),
206	                )
207	                matched_gold = gold_map.get(key, {})
208	                hard_neg_ids = matched_gold.get("hard_negative_sent_ids", [])
209	                hard_neg_sents = [sents[idx] for idx in hard_neg_ids
210	                                  if isinstance(idx, int) and 0 <= idx < len(sents)]
211	
212	                if self.mode == "flat_nli":
213	                    result = self.reward_model.compute_flat_nli_reward(
214	                        claim, cited_sents, tau=self.tau,
215	                    )
216	                else:
217	                    result = self.reward_model.compute_ced_reward(
218	                        claim, cited_sents, hard_neg_sents, tau=self.tau,
219	                    )
220	                triple_rewards.append(result["reward"])
221	
222	            rewards.append(
223	                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0
224	            )
225	
226	        return rewards
227	
228	
229	def prepare_grpo_dataset(
230	    data_dir: str = None,
231	    split: str = "train",
232	    tokenizer=None,
233	) -> Dataset:
234	    """准备 GRPO prompt 数据集。
235	
236	    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。
237	    """
238	    from freige.data.docred_processor import DocREDProcessor
239	
240	    processor = DocREDProcessor(data_dir=data_dir)
241	    samples = processor.process(split)
242	    groups = processor.group_by_document(samples)
243	
244	    dataset_items = []
245	    for doc_id, doc_samples in groups.items():
246	        sft_sample = processor.format_sft_sample(doc_samples)
247	        messages = [
248	            {"role": "system", "content": SYSTEM_PROMPT},
249	            {"role": "user", "content": f"{sft_sample['instruction']}\n\n{sft_sample['input']}"},
250	        ]
251	        prompt = tokenizer.apply_chat_template(
252	            messages,
253	            tokenize=False,
254	            add_generation_prompt=True,
255	            enable_thinking=False,
256	        )
257	
258	        gold_triples = []
259	        for s in doc_samples:
260	            gold_triples.append({
261	                "head": s.head.name,
262	                "relation": s.relation_name,
263	                "tail": s.tail.name,
264	                "evidence": s.evidence_sent_ids,
265	                "hard_negative_sent_ids": s.hard_negative_sent_ids,
266	            })
267	
268	        ref = doc_samples[0]
269	        dataset_items.append({
270	            "prompt": prompt,
271	            "gold_triples": json.dumps(gold_triples, ensure_ascii=False),
272	            "all_sents": json.dumps(ref.sents, ensure_ascii=False),
273	        })
274	
275	    logger.info("Prepared %d GRPO prompts", len(dataset_items))
276	    return Dataset.from_list(dataset_items)
277	
278	
279	def main():
280	    parser = argparse.ArgumentParser(description="FREIGE GRPO Training")
281	    parser.add_argument("--model_name", type=str, default="Qwen/Qwen3-4B",
282	                        help="基础模型或 SFT checkpoint 路径")
283	    parser.add_argument("--sft_adapter", type=str, default=None,
284	                        help="SFT LoRA adapter 路径（如果与 model_name 不同）")
285	    parser.add_argument("--data_dir", type=str, default=None)
286	    parser.add_argument("--output_dir", type=str, default="./grpo_output")
287	    parser.add_argument("--stage", type=int, default=1, choices=[1, 2, 3],
288	                        help="Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED")
289	    parser.add_argument("--nli_model", type=str, default="cross-encoder/nli-deberta-v3-base")
290	    parser.add_argument("--num_generations", type=int, default=4)
291	    parser.add_argument("--lora_rank", type=int, default=64)
292	    parser.add_argument("--lora_alpha", type=int, default=128)
293	    parser.add_argument("--max_length", type=int, default=4096)
294	    parser.add_argument("--max_new_tokens", type=int, default=1024)
295	    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction, default=True,
296	                        help="启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）")
297	    parser.add_argument("--deepspeed", type=str, default=None,
298	                        help="DeepSpeed 配置文件路径")
299	    parser.add_argument("--reward_device", type=str, default="cpu",
300	                        help="CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）")
301	    parser.add_argument("--per_device_batch_size", type=int, default=1)
302	    parser.add_argument("--gradient_accumulation_steps", type=int, default=16)
303	    parser.add_argument("--num_epochs", type=int, default=1)
304	    parser.add_argument("--learning_rate", type=float, default=5e-5)
305	    parser.add_argument("--tau", type=float, default=0.5)
306	    parser.add_argument("--bf16", action="store_true", default=True)
307	    parser.add_argument("--seed", type=int, default=42)
308	    parser.add_argument("--wandb_project", type=str, default="freige-grpo")
309	    parser.add_argument("--wandb_run_name", type=str, default=None)
310	    args = parser.parse_args()
311	
312	    if args.wandb_project and "WANDB_API_KEY" in os.environ:
313	        os.environ["WANDB_PROJECT"] = args.wandb_project
314	        if args.wandb_run_name:
315	            os.environ["WANDB_NAME"] = args.wandb_run_name
316	
317	    logger.info("Loading tokenizer: %s", args.model_name)
318	    tokenizer = AutoTokenizer.from_pretrained(
319	        args.model_name,
320	        trust_remote_code=True,
321	        padding_side="left",
322	    )
323	    if tokenizer.pad_token is None:
324	        tokenizer.pad_token = tokenizer.eos_token
325	
326	    logger.info("Preparing dataset...")
327	    train_dataset = prepare_grpo_dataset(
328	        data_dir=args.data_dir,
329	        split="train",
330	        tokenizer=tokenizer,
331	    )
332	
333	    logger.info("Loading model: %s", args.model_name)
334	    model_kwargs = dict(
335	        trust_remote_code=True,
336	        attn_implementation="flash_attention_2",
337	    )
338	    if args.quantize:
339	        logger.info("Using 4-bit QLoRA quantization")
340	        model_kwargs["quantization_config"] = BitsAndBytesConfig(
341	            load_in_4bit=True,
342	            bnb_4bit_compute_dtype=torch.bfloat16,
343	            bnb_4bit_quant_type="nf4",
344	            bnb_4bit_use_double_quant=True,
345	        )
346	    else:
347	        model_kwargs["torch_dtype"] = torch.bfloat16 if args.bf16 else torch.float16
348	    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)
349	
350	    if args.sft_adapter:
351	        logger.info("Loading SFT adapter from %s", args.sft_adapter)
352	        model = PeftModel.from_pretrained(model, args.sft_adapter)
353	        model = model.merge_and_unload()
354	
355	    reward_fns = [format_reward_fn, f1_reward_fn]
356	
357	    if args.stage >= 2:
358	        mode = "flat_nli" if args.stage == 2 else "ced"
359	        ced_wrapper = CEDRewardWrapper(
360	            nli_model=args.nli_model,
361	            tau=args.tau,
362	            mode=mode,
363	            device=args.reward_device,
364	        )
365	        reward_fns.append(ced_wrapper)
366	        logger.info("Stage %d: using %s reward", args.stage, mode)
367	    else:
368	        logger.info("Stage 1: extraction-only (format + F1 rewards)")
369	
370	    lora_config = LoraConfig(
371	        task_type=TaskType.CAUSAL_LM,
372	        r=args.lora_rank,
373	        lora_alpha=args.lora_alpha,
374	        lora_dropout=0.05,
375	        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
376	                         "gate_proj", "up_proj", "down_proj"],
377	    )
378	
379	    grpo_config = GRPOConfig(
380	        output_dir=args.output_dir,
381	        num_train_epochs=args.num_epochs,
382	        per_device_train_batch_size=args.per_device_batch_size,
383	        gradient_accumulation_steps=args.gradient_accumulation_steps,
384	        learning_rate=args.learning_rate,
385	        bf16=args.bf16,
386	        logging_steps=5,
387	        save_strategy="epoch",
388	        save_total_limit=2,
389	        seed=args.seed,
390	        num_generations=args.num_generations,
391	        max_completion_length=args.max_new_tokens,
392	        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
393	        gradient_checkpointing=True,
394	        gradient_checkpointing_kwargs={"use_reentrant": False},
395	        deepspeed=args.deepspeed,
396	    )
397	
398	    trainer = GRPOTrainer(
399	        model=model,
400	        args=grpo_config,
401	        train_dataset=train_dataset,
402	        reward_funcs=reward_fns,
403	        peft_config=lora_config,
404	        tokenizer=tokenizer,
405	    )
406	
407	    logger.info("Starting GRPO training (stage %d)...", args.stage)
408	    trainer.train()
409	
410	    logger.info("Saving model to %s", args.output_dir)
411	    trainer.save_model(args.output_dir)
412	    tokenizer.save_pretrained(args.output_dir)
413	    logger.info("GRPO training (stage %d) complete.", args.stage)
414	
415	
416	if __name__ == "__main__":
417	    main()
418	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "fae39760-590e-4ce2-9d97-8825643da81d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
      "content": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero3.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.tau = tau\n        self.mode = mode\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=self.tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=self.tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau\", type=float, default=0.5)\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 418,
      "startLine": 1,
      "totalLines": 418
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01BWwK14JW2RpRGzXkF31Qw9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "7cc29188-0c36-4c50-aa4e-7920d44745dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7fvKH42Er9jmjHQzrFxK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12691,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12691
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T06:08:48.079Z_

<details><summary>↩ Tool result · `toolu_01BWwK14JW2RpRGzXkF31Qw9`</summary>

```text
1	"""CED（Contrastive Evidence Discrimination）对比证据判别奖励。
2	
3	核心公式:
4	  p_pos = NLI_entail(concat(cited_evidence), claim)
5	  p_neg = max_j NLI_entail(neg_sent_j, claim)
6	  R_CED = max(0, p_pos - p_neg) * I(p_pos > tau)
7	
8	输入: 关系三元组 + gold evidence 句子 + hard negative 句子
9	输出: CED 奖励值 ∈ [0, 1]
10	依赖: transformers, torch
11	"""
12	
13	import logging
14	from typing import Optional
15	
16	import torch
17	import torch.nn.functional as F
18	from transformers import AutoModelForSequenceClassification, AutoTokenizer
19	
20	logger = logging.getLogger(__name__)
21	
22	DEFAULT_NLI_MODEL = "cross-encoder/nli-deberta-v3-base"
23	
24	VERBALIZATION_TEMPLATES = {
25	    "P6": "The head of government of {head} is {tail}.",
26	    "P17": "{head} is located in the country {tail}.",
27	    "P19": "{head} was born in {tail}.",
28	    "P20": "{head} died in {tail}.",
29	    "P22": "The father of {head} is {tail}.",
30	    "P25": "The mother of {head} is {tail}.",
31	    "P26": "{head} is married to {tail}.",
32	    "P27": "{head} is a citizen of {tail}.",
33	    "P30": "{head} is located in the continent of {tail}.",
34	    "P31": "{head} is an instance of {tail}.",
35	    "P35": "The head of state of {head} is {tail}.",
36	    "P36": "The capital of {head} is {tail}.",
37	    "P37": "The official language of {head} is {tail}.",
38	    "P39": "{head} held the position of {tail}.",
39	    "P40": "{head} has a child named {tail}.",
40	    "P50": "The author of {head} is {tail}.",
41	    "P54": "{head} is a member of the sports team {tail}.",
42	    "P57": "The director of {head} is {tail}.",
43	    "P58": "The screenwriter of {head} is {tail}.",
44	    "P69": "{head} was educated at {tail}.",
45	    "P86": "The composer of {head} is {tail}.",
46	    "P102": "{head} is a member of the political party {tail}.",
47	    "P108": "{head} is employed by {tail}.",
48	    "P112": "{head} was founded by {tail}.",
49	    "P118": "{head} plays in the league {tail}.",
50	    "P123": "The publisher of {head} is {tail}.",
51	    "P127": "{head} is owned by {tail}.",
52	    "P131": "{head} is located in {tail}.",
53	    "P136": "The genre of {head} is {tail}.",
54	    "P137": "{head} is operated by {tail}.",
55	    "P140": "The religion of {head} is {tail}.",
56	    "P150": "{head} contains the administrative territory {tail}.",
57	    "P155": "{head} follows {tail}.",
58	    "P156": "{head} is followed by {tail}.",
59	    "P159": "The headquarters of {head} is located in {tail}.",
60	    "P161": "{head} features the cast member {tail}.",
61	    "P162": "The producer of {head} is {tail}.",
62	    "P166": "{head} received the award {tail}.",
63	    "P170": "The creator of {head} is {tail}.",
64	    "P171": "The parent taxon of {head} is {tail}.",
65	    "P172": "{head} belongs to the ethnic group {tail}.",
66	    "P175": "The performer of {head} is {tail}.",
67	    "P176": "The manufacturer of {head} is {tail}.",
68	    "P178": "The developer of {head} is {tail}.",
69	    "P179": "{head} is part of the series {tail}.",
70	    "P190": "{head} is a sister city of {tail}.",
71	    "P194": "The legislative body of {head} is {tail}.",
72	    "P205": "{head} is in the basin of {tail}.",
73	    "P206": "{head} is located near the body of water {tail}.",
74	    "P241": "{head} is a branch of the military {tail}.",
75	    "P264": "The record label of {head} is {tail}.",
76	    "P272": "The production company of {head} is {tail}.",
77	    "P276": "{head} is located in {tail}.",
78	    "P279": "{head} is a subclass of {tail}.",
79	    "P355": "{head} has the subsidiary {tail}.",
80	    "P361": "{head} is part of {tail}.",
81	    "P364": "The original language of {head} is {tail}.",
82	    "P400": "{head} is available on the platform {tail}.",
83	    "P403": "{head} flows into {tail}.",
84	    "P449": "The original network of {head} is {tail}.",
85	    "P463": "{head} is a member of {tail}.",
86	    "P488": "The chairperson of {head} is {tail}.",
87	    "P495": "{head} originates from the country {tail}.",
88	    "P527": "{head} has the part {tail}.",
89	    "P551": "{head} resides in {tail}.",
90	    "P569": "{head} was born on {tail}.",
91	    "P570": "{head} died on {tail}.",
92	    "P571": "{head} was established in {tail}.",
93	    "P576": "{head} was dissolved in {tail}.",
94	    "P577": "{head} was published on {tail}.",
95	    "P580": "{head} started in {tail}.",
96	    "P582": "{head} ended in {tail}.",
97	    "P585": "{head} occurred at the time {tail}.",
98	    "P607": "{head} was involved in the conflict {tail}.",
99	    "P674": "{head} features the character {tail}.",
100	    "P676": "The lyrics of {head} were written by {tail}.",
101	    "P706": "{head} is located on the terrain {tail}.",
102	    "P710": "{head} participated in {tail}.",
103	    "P737": "{head} was influenced by {tail}.",
104	    "P740": "{head} was formed in {tail}.",
105	    "P749": "The parent organization of {head} is {tail}.",
106	    "P800": "The notable work of {head} is {tail}.",
107	    "P807": "{head} was separated from {tail}.",
108	    "P840": "The narrative of {head} is set in {tail}.",
109	    "P937": "{head} worked in {tail}.",
110	    "P1001": "{head} applies to the jurisdiction of {tail}.",
111	    "P1056": "{head} produces {tail}.",
112	    "P1198": "The unemployment rate of {head} is {tail}.",
113	    "P1336": "{head} is claimed by {tail}.",
114	    "P1344": "{head} participated in {tail}.",
115	    "P1365": "{head} replaces {tail}.",
116	    "P1366": "{head} was replaced by {tail}.",
117	    "P1376": "{head} is the capital of {tail}.",
118	    "P1412": "{head} speaks the language {tail}.",
119	    "P1441": "{head} is present in the work {tail}.",
120	    "P3373": "{head} is a sibling of {tail}.",
121	}
122	
123	
124	def verbalize_triple(head: str, relation: str, tail: str) -> str:
125	    """将 (head, relation_id, tail) 三元组转为自然语言 claim。
126	
127	    Args:
128	        head: 头实体名称
129	        relation: Wikidata 属性 ID (如 "P17") 或关系名称
130	        tail: 尾实体名称
131	
132	    Returns:
133	        自然语言 claim 字符串
134	    """
135	    template = VERBALIZATION_TEMPLATES.get(relation)
136	    if template:
137	        return template.format(head=head, tail=tail)
138	    from freige.data.docred_processor import DOCRED_REL_INFO
139	    rel_name = DOCRED_REL_INFO.get(relation, relation)
140	    return f"{head} {rel_name} {tail}."
141	
142	
143	class CEDRewardModel:
144	    """CED 对比证据判别奖励模型。
145	
146	    Args:
147	        model_name: NLI 模型 HuggingFace ID
148	        device: torch 设备
149	        max_length: tokenizer 最大长度
150	    """
151	
152	    def __init__(
153	        self,
154	        model_name: str = DEFAULT_NLI_MODEL,
155	        device: Optional[str] = None,
156	        max_length: int = 512,
157	    ):
158	        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
159	        self.max_length = max_length
160	
161	        logger.info("Loading NLI model: %s", model_name)
162	        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
163	        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
164	        self.model.to(self.device)
165	        self.model.eval()
166	
167	        self._resolve_entailment_idx()
168	
169	    def _resolve_entailment_idx(self):
170	        """从 model.config.id2label 确定 entailment 类别的索引。"""
171	        id2label = self.model.config.id2label
172	        self.entail_idx = None
173	        for idx, label in id2label.items():
174	            if label.lower() in ("entailment", "entail"):
175	                self.entail_idx = int(idx)
176	                break
177	        if self.entail_idx is None:
178	            logger.warning(
179	                "Could not find 'entailment' in id2label=%s, defaulting to index 1",
180	                id2label,
181	            )
182	            self.entail_idx = 1
183	        logger.info("Entailment index: %d (id2label=%s)", self.entail_idx, id2label)
184	
185	    @torch.no_grad()
186	    def nli_entailment_prob(
187	        self, premises: list[str], hypotheses: list[str]
188	    ) -> torch.Tensor:
189	        """计算 batch 的 NLI entailment 概率。
190	
191	        Args:
192	            premises: 前提文本列表（evidence 句子）
193	            hypotheses: 假设文本列表（verbalized claim）
194	
195	        Returns:
196	            shape (batch_size,) 的 entailment 概率张量
197	        """
198	        inputs = self.tokenizer(
199	            premises,
200	            hypotheses,
201	            padding=True,
202	            truncation=True,
203	            max_length=self.max_length,
204	            return_tensors="pt",
205	        ).to(self.device)
206	
207	        logits = self.model(**inputs).logits
208	        probs = F.softmax(logits, dim=-1)
209	        return probs[:, self.entail_idx].cpu()
210	
211	    def compute_ced_reward(
212	        self,
213	        claim: str,
214	        cited_evidence_sents: list[str],
215	        hard_negative_sents: list[str],
216	        tau: float = 0.5,
217	    ) -> dict:
218	        """计算单个样本的 CED 奖励。
219	
220	        R_CED = max(0, p_pos - p_neg) * I(p_pos > tau)
221	
222	        Args:
223	            claim: verbalized 关系 claim
224	            cited_evidence_sents: gold evidence 句子列表
225	            hard_negative_sents: hard negative 句子列表
226	            tau: p_pos 阈值
227	
228	        Returns:
229	            {"reward": float, "p_pos": float, "p_neg": float, "margin": float}
230	        """
231	        evidence_concat = " ".join(cited_evidence_sents)
232	        p_pos = self.nli_entailment_prob(
233	            [evidence_concat], [claim]
234	        ).item()
235	
236	        if not hard_negative_sents:
237	            p_neg = 0.0
238	        else:
239	            neg_probs = self.nli_entailment_prob(
240	                hard_negative_sents, [claim] * len(hard_negative_sents)
241	            )
242	            p_neg = neg_probs.max().item()
243	
244	        margin = p_pos - p_neg
245	        reward = max(0.0, margin) * float(p_pos > tau)
246	
247	        return {
248	            "reward": reward,
249	            "p_pos": p_pos,
250	            "p_neg": p_neg,
251	            "margin": margin,
252	        }
253	
254	    def compute_ced_reward_batch(
255	        self,
256	        claims: list[str],
257	        cited_evidence_list: list[list[str]],
258	        hard_negative_list: list[list[str]],
259	        tau: float = 0.5,
260	    ) -> list[dict]:
261	        """批量计算 CED 奖励。
262	
263	        先合并所有 NLI 请求到两个大 batch（positive 和 negative），
264	        一次前向传播后拆分结果，减少 GPU kernel launch 开销。
265	
266	        Args:
267	            claims: N 个 claim
268	            cited_evidence_list: N 个 evidence 句子列表
269	            hard_negative_list: N 个 hard negative 句子列表
270	            tau: p_pos 阈值
271	
272	        Returns:
273	            N 个 {"reward", "p_pos", "p_neg", "margin"} 字典
274	        """
275	        n = len(claims)
276	        assert len(cited_evidence_list) == n and len(hard_negative_list) == n
277	
278	        pos_premises = [" ".join(ev) for ev in cited_evidence_list]
279	        pos_probs = self.nli_entailment_prob(pos_premises, claims)
280	
281	        all_neg_premises = []
282	        all_neg_hyps = []
283	        neg_counts = []
284	        for i in range(n):
285	            negs = hard_negative_list[i]
286	            neg_counts.append(len(negs))
287	            all_neg_premises.extend(negs)
288	            all_neg_hyps.extend([claims[i]] * len(negs))
289	
290	        if all_neg_premises:
291	            all_neg_probs = self.nli_entailment_prob(all_neg_premises, all_neg_hyps)
292	        else:
293	            all_neg_probs = torch.tensor([])
294	
295	        results = []
296	        offset = 0
297	        for i in range(n):
298	            p_pos = pos_probs[i].item()
299	            nc = neg_counts[i]
300	            if nc > 0:
301	                p_neg = all_neg_probs[offset:offset + nc].max().item()
302	            else:
303	                p_neg = 0.0
304	            offset += nc
305	
306	            margin = p_pos - p_neg
307	            reward = max(0.0, margin) * float(p_pos > tau)
308	            results.append({
309	                "reward": reward,
310	                "p_pos": p_pos,
311	                "p_neg": p_neg,
312	                "margin": margin,
313	            })
314	
315	        return results
316	
317	    def compute_flat_nli_reward(
318	        self,
319	        claim: str,
320	        cited_evidence_sents: list[str],
321	        tau: float = 0.5,
322	    ) -> dict:
323	        """Flat NLI 奖励（无对比项），用于 curriculum 第二阶段。
324	
325	        R_flat = p_pos * I(p_pos > tau)
326	        """
327	        evidence_concat = " ".join(cited_evidence_sents)
328	        p_pos = self.nli_entailment_prob(
329	            [evidence_concat], [claim]
330	        ).item()
331	        reward = p_pos * float(p_pos > tau)
332	        return {"reward": reward, "p_pos": p_pos}
333	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "a51c5d98-5e27-4230-aaed-5adb631c9f5b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py",
      "content": "\"\"\"CED（Contrastive Evidence Discrimination）对比证据判别奖励。\n\n核心公式:\n  p_pos = NLI_entail(concat(cited_evidence), claim)\n  p_neg = max_j NLI_entail(neg_sent_j, claim)\n  R_CED = max(0, p_pos - p_neg) * I(p_pos > tau)\n\n输入: 关系三元组 + gold evidence 句子 + hard negative 句子\n输出: CED 奖励值 ∈ [0, 1]\n依赖: transformers, torch\n\"\"\"\n\nimport logging\nfrom typing import Optional\n\nimport torch\nimport torch.nn.functional as F\nfrom transformers import AutoModelForSequenceClassification, AutoTokenizer\n\nlogger = logging.getLogger(__name__)\n\nDEFAULT_NLI_MODEL = \"cross-encoder/nli-deberta-v3-base\"\n\nVERBALIZATION_TEMPLATES = {\n    \"P6\": \"The head of government of {head} is {tail}.\",\n    \"P17\": \"{head} is located in the country {tail}.\",\n    \"P19\": \"{head} was born in {tail}.\",\n    \"P20\": \"{head} died in {tail}.\",\n    \"P22\": \"The father of {head} is {tail}.\",\n    \"P25\": \"The mother of {head} is {tail}.\",\n    \"P26\": \"{head} is married to {tail}.\",\n    \"P27\": \"{head} is a citizen of {tail}.\",\n    \"P30\": \"{head} is located in the continent of {tail}.\",\n    \"P31\": \"{head} is an instance of {tail}.\",\n    \"P35\": \"The head of state of {head} is {tail}.\",\n    \"P36\": \"The capital of {head} is {tail}.\",\n    \"P37\": \"The official language of {head} is {tail}.\",\n    \"P39\": \"{head} held the position of {tail}.\",\n    \"P40\": \"{head} has a child named {tail}.\",\n    \"P50\": \"The author of {head} is {tail}.\",\n    \"P54\": \"{head} is a member of the sports team {tail}.\",\n    \"P57\": \"The director of {head} is {tail}.\",\n    \"P58\": \"The screenwriter of {head} is {tail}.\",\n    \"P69\": \"{head} was educated at {tail}.\",\n    \"P86\": \"The composer of {head} is {tail}.\",\n    \"P102\": \"{head} is a member of the political party {tail}.\",\n    \"P108\": \"{head} is employed by {tail}.\",\n    \"P112\": \"{head} was founded by {tail}.\",\n    \"P118\": \"{head} plays in the league {tail}.\",\n    \"P123\": \"The publisher of {head} is {tail}.\",\n    \"P127\": \"{head} is owned by {tail}.\",\n    \"P131\": \"{head} is located in {tail}.\",\n    \"P136\": \"The genre of {head} is {tail}.\",\n    \"P137\": \"{head} is operated by {tail}.\",\n    \"P140\": \"The religion of {head} is {tail}.\",\n    \"P150\": \"{head} contains the administrative territory {tail}.\",\n    \"P155\": \"{head} follows {tail}.\",\n    \"P156\": \"{head} is followed by {tail}.\",\n    \"P159\": \"The headquarters of {head} is located in {tail}.\",\n    \"P161\": \"{head} features the cast member {tail}.\",\n    \"P162\": \"The producer of {head} is {tail}.\",\n    \"P166\": \"{head} received the award {tail}.\",\n    \"P170\": \"The creator of {head} is {tail}.\",\n    \"P171\": \"The parent taxon of {head} is {tail}.\",\n    \"P172\": \"{head} belongs to the ethnic group {tail}.\",\n    \"P175\": \"The performer of {head} is {tail}.\",\n    \"P176\": \"The manufacturer of {head} is {tail}.\",\n    \"P178\": \"The developer of {head} is {tail}.\",\n    \"P179\": \"{head} is part of the series {tail}.\",\n    \"P190\": \"{head} is a sister city of {tail}.\",\n    \"P194\": \"The legislative body of {head} is {tail}.\",\n    \"P205\": \"{head} is in the basin of {tail}.\",\n    \"P206\": \"{head} is located near the body of water {tail}.\",\n    \"P241\": \"{head} is a branch of the military {tail}.\",\n    \"P264\": \"The record label of {head} is {tail}.\",\n    \"P272\": \"The production company of {head} is {tail}.\",\n    \"P276\": \"{head} is located in {tail}.\",\n    \"P279\": \"{head} is a subclass of {tail}.\",\n    \"P355\": \"{head} has the subsidiary {tail}.\",\n    \"P361\": \"{head} is part of {tail}.\",\n    \"P364\": \"The original language of {head} is {tail}.\",\n    \"P400\": \"{head} is available on the platform {tail}.\",\n    \"P403\": \"{head} flows into {tail}.\",\n    \"P449\": \"The original network of {head} is {tail}.\",\n    \"P463\": \"{head} is a member of {tail}.\",\n    \"P488\": \"The chairperson of {head} is {tail}.\",\n    \"P495\": \"{head} originates from the country {tail}.\",\n    \"P527\": \"{head} has the part {tail}.\",\n    \"P551\": \"{head} resides in {tail}.\",\n    \"P569\": \"{head} was born on {tail}.\",\n    \"P570\": \"{head} died on {tail}.\",\n    \"P571\": \"{head} was established in {tail}.\",\n    \"P576\": \"{head} was dissolved in {tail}.\",\n    \"P577\": \"{head} was published on {tail}.\",\n    \"P580\": \"{head} started in {tail}.\",\n    \"P582\": \"{head} ended in {tail}.\",\n    \"P585\": \"{head} occurred at the time {tail}.\",\n    \"P607\": \"{head} was involved in the conflict {tail}.\",\n    \"P674\": \"{head} features the character {tail}.\",\n    \"P676\": \"The lyrics of {head} were written by {tail}.\",\n    \"P706\": \"{head} is located on the terrain {tail}.\",\n    \"P710\": \"{head} participated in {tail}.\",\n    \"P737\": \"{head} was influenced by {tail}.\",\n    \"P740\": \"{head} was formed in {tail}.\",\n    \"P749\": \"The parent organization of {head} is {tail}.\",\n    \"P800\": \"The notable work of {head} is {tail}.\",\n    \"P807\": \"{head} was separated from {tail}.\",\n    \"P840\": \"The narrative of {head} is set in {tail}.\",\n    \"P937\": \"{head} worked in {tail}.\",\n    \"P1001\": \"{head} applies to the jurisdiction of {tail}.\",\n    \"P1056\": \"{head} produces {tail}.\",\n    \"P1198\": \"The unemployment rate of {head} is {tail}.\",\n    \"P1336\": \"{head} is claimed by {tail}.\",\n    \"P1344\": \"{head} participated in {tail}.\",\n    \"P1365\": \"{head} replaces {tail}.\",\n    \"P1366\": \"{head} was replaced by {tail}.\",\n    \"P1376\": \"{head} is the capital of {tail}.\",\n    \"P1412\": \"{head} speaks the language {tail}.\",\n    \"P1441\": \"{head} is present in the work {tail}.\",\n    \"P3373\": \"{head} is a sibling of {tail}.\",\n}\n\n\ndef verbalize_triple(head: str, relation: str, tail: str) -> str:\n    \"\"\"将 (head, relation_id, tail) 三元组转为自然语言 claim。\n\n    Args:\n        head: 头实体名称\n        relation: Wikidata 属性 ID (如 \"P17\") 或关系名称\n        tail: 尾实体名称\n\n    Returns:\n        自然语言 claim 字符串\n    \"\"\"\n    template = VERBALIZATION_TEMPLATES.get(relation)\n    if template:\n        return template.format(head=head, tail=tail)\n    from freige.data.docred_processor import DOCRED_REL_INFO\n    rel_name = DOCRED_REL_INFO.get(relation, relation)\n    return f\"{head} {rel_name} {tail}.\"\n\n\nclass CEDRewardModel:\n    \"\"\"CED 对比证据判别奖励模型。\n\n    Args:\n        model_name: NLI 模型 HuggingFace ID\n        device: torch 设备\n        max_length: tokenizer 最大长度\n    \"\"\"\n\n    def __init__(\n        self,\n        model_name: str = DEFAULT_NLI_MODEL,\n        device: Optional[str] = None,\n        max_length: int = 512,\n    ):\n        self.device = device or (\"cuda\" if torch.cuda.is_available() else \"cpu\")\n        self.max_length = max_length\n\n        logger.info(\"Loading NLI model: %s\", model_name)\n        self.tokenizer = AutoTokenizer.from_pretrained(model_name)\n        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)\n        self.model.to(self.device)\n        self.model.eval()\n\n        self._resolve_entailment_idx()\n\n    def _resolve_entailment_idx(self):\n        \"\"\"从 model.config.id2label 确定 entailment 类别的索引。\"\"\"\n        id2label = self.model.config.id2label\n        self.entail_idx = None\n        for idx, label in id2label.items():\n            if label.lower() in (\"entailment\", \"entail\"):\n                self.entail_idx = int(idx)\n                break\n        if self.entail_idx is None:\n            logger.warning(\n                \"Could not find 'entailment' in id2label=%s, defaulting to index 1\",\n                id2label,\n            )\n            self.entail_idx = 1\n        logger.info(\"Entailment index: %d (id2label=%s)\", self.entail_idx, id2label)\n\n    @torch.no_grad()\n    def nli_entailment_prob(\n        self, premises: list[str], hypotheses: list[str]\n    ) -> torch.Tensor:\n        \"\"\"计算 batch 的 NLI entailment 概率。\n\n        Args:\n            premises: 前提文本列表（evidence 句子）\n            hypotheses: 假设文本列表（verbalized claim）\n\n        Returns:\n            shape (batch_size,) 的 entailment 概率张量\n        \"\"\"\n        inputs = self.tokenizer(\n            premises,\n            hypotheses,\n            padding=True,\n            truncation=True,\n            max_length=self.max_length,\n            return_tensors=\"pt\",\n        ).to(self.device)\n\n        logits = self.model(**inputs).logits\n        probs = F.softmax(logits, dim=-1)\n        return probs[:, self.entail_idx].cpu()\n\n    def compute_ced_reward(\n        self,\n        claim: str,\n        cited_evidence_sents: list[str],\n        hard_negative_sents: list[str],\n        tau: float = 0.5,\n    ) -> dict:\n        \"\"\"计算单个样本的 CED 奖励。\n\n        R_CED = max(0, p_pos - p_neg) * I(p_pos > tau)\n\n        Args:\n            claim: verbalized 关系 claim\n            cited_evidence_sents: gold evidence 句子列表\n            hard_negative_sents: hard negative 句子列表\n            tau: p_pos 阈值\n\n        Returns:\n            {\"reward\": float, \"p_pos\": float, \"p_neg\": float, \"margin\": float}\n        \"\"\"\n        evidence_concat = \" \".join(cited_evidence_sents)\n        p_pos = self.nli_entailment_prob(\n            [evidence_concat], [claim]\n        ).item()\n\n        if not hard_negative_sents:\n            p_neg = 0.0\n        else:\n            neg_probs = self.nli_entailment_prob(\n                hard_negative_sents, [claim] * len(hard_negative_sents)\n            )\n            p_neg = neg_probs.max().item()\n\n        margin = p_pos - p_neg\n        reward = max(0.0, margin) * float(p_pos > tau)\n\n        return {\n            \"reward\": reward,\n            \"p_pos\": p_pos,\n            \"p_neg\": p_neg,\n            \"margin\": margin,\n        }\n\n    def compute_ced_reward_batch(\n        self,\n        claims: list[str],\n        cited_evidence_list: list[list[str]],\n        hard_negative_list: list[list[str]],\n        tau: float = 0.5,\n    ) -> list[dict]:\n        \"\"\"批量计算 CED 奖励。\n\n        先合并所有 NLI 请求到两个大 batch（positive 和 negative），\n        一次前向传播后拆分结果，减少 GPU kernel launch 开销。\n\n        Args:\n            claims: N 个 claim\n            cited_evidence_list: N 个 evidence 句子列表\n            hard_negative_list: N 个 hard negative 句子列表\n            tau: p_pos 阈值\n\n        Returns:\n            N 个 {\"reward\", \"p_pos\", \"p_neg\", \"margin\"} 字典\n        \"\"\"\n        n = len(claims)\n        assert len(cited_evidence_list) == n and len(hard_negative_list) == n\n\n        pos_premises = [\" \".join(ev) for ev in cited_evidence_list]\n        pos_probs = self.nli_entailment_prob(pos_premises, claims)\n\n        all_neg_premises = []\n        all_neg_hyps = []\n        neg_counts = []\n        for i in range(n):\n            negs = hard_negative_list[i]\n            neg_counts.append(len(negs))\n            all_neg_premises.extend(negs)\n            all_neg_hyps.extend([claims[i]] * len(negs))\n\n        if all_neg_premises:\n            all_neg_probs = self.nli_entailment_prob(all_neg_premises, all_neg_hyps)\n        else:\n            all_neg_probs = torch.tensor([])\n\n        results = []\n        offset = 0\n        for i in range(n):\n            p_pos = pos_probs[i].item()\n            nc = neg_counts[i]\n            if nc > 0:\n                p_neg = all_neg_probs[offset:offset + nc].max().item()\n            else:\n                p_neg = 0.0\n            offset += nc\n\n            margin = p_pos - p_neg\n            reward = max(0.0, margin) * float(p_pos > tau)\n            results.append({\n                \"reward\": reward,\n                \"p_pos\": p_pos,\n                \"p_neg\": p_neg,\n                \"margin\": margin,\n            })\n\n        return results\n\n    def compute_flat_nli_reward(\n        self,\n        claim: str,\n        cited_evidence_sents: list[str],\n        tau: float = 0.5,\n    ) -> dict:\n        \"\"\"Flat NLI 奖励（无对比项），用于 curriculum 第二阶段。\n\n        R_flat = p_pos * I(p_pos > tau)\n        \"\"\"\n        evidence_concat = \" \".join(cited_evidence_sents)\n        p_pos = self.nli_entailment_prob(\n            [evidence_concat], [claim]\n        ).item()\n        reward = p_pos * float(p_pos > tau)\n        return {\"reward\": reward, \"p_pos\": p_pos}\n",
      "numLines": 333,
      "startLine": 1,
      "totalLines": 333
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01URtuQKTjQX4qpKzD2iTwpC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "25b037bb-db50-485b-b151-0283a4dc43a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7fvKH42Er9jmjHQzrFxK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12691,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12691
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T06:08:48.359Z_

<details><summary>↩ Tool result · `toolu_01URtuQKTjQX4qpKzD2iTwpC`</summary>

```text
1	#!/usr/bin/env python3
2	# Launch:
3	#   accelerate launch --num_processes 4 --mixed_precision bf16 training/smoke_test.py
4	#   deepspeed --num_gpus 4 training/smoke_test.py
5	"""Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-3 on 4xRTX 5090 (32GB).
6	
7	Uses synthetic data only. No freige imports. Runs 10 training steps and reports
8	loss trend, peak VRAM, gradient norms, and PASS/FAIL.
9	"""
10	
11	import json
12	import math
13	import os
14	import random
15	import time
16	
17	import torch
18	from datasets import Dataset
19	from peft import LoraConfig, TaskType
20	from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
21	from trl import GRPOConfig, GRPOTrainer
22	
23	os.environ.setdefault("WANDB_DISABLED", "true")
24	
25	SEED = 42
26	NUM_STEPS = 10
27	NUM_GENERATIONS = 4
28	MAX_COMPLETION_LENGTH = 256
29	MODEL_NAME = "Qwen/Qwen3-4B"
30	
31	SYSTEM_PROMPT = (
32	    "You are an information extraction model. Given a document with numbered sentences "
33	    "and a list of entities, extract all relation triples. For each triple, provide the "
34	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
35	    "Output as a JSON list."
36	)
37	
38	DEEPSPEED_CONFIG = {
39	    "bf16": {"enabled": True},
40	    "zero_optimization": {
41	        "stage": 3,
42	        "offload_optimizer": {"device": "cpu", "pin_memory": True},
43	        "offload_param": {"device": "cpu", "pin_memory": True},
44	        "overlap_comm": True,
45	        "contiguous_gradients": True,
46	        "sub_group_size": 1e9,
47	        "reduce_bucket_size": "auto",
48	        "stage3_prefetch_bucket_size": "auto",
49	        "stage3_param_persistence_threshold": "auto",
50	        "stage3_max_live_parameters": 1e9,
51	        "stage3_max_reuse_distance": 1e9,
52	        "stage3_gather_16bit_weights_on_model_save": True,
53	    },
54	    "gradient_accumulation_steps": "auto",
55	    "gradient_clipping": "auto",
56	    "train_batch_size": "auto",
57	    "train_micro_batch_size_per_gpu": "auto",
58	}
59	
60	DUMMY_DOCS = [
61	    {
62	        "sents": [
63	            "Albert Einstein was born in Ulm, Germany in 1879.",
64	            "He developed the theory of relativity while working at the Swiss Patent Office.",
65	            "Einstein later moved to the United States and joined Princeton University.",
66	            "He received the Nobel Prize in Physics in 1921 for his work on the photoelectric effect.",
67	        ],
68	        "entities": ["Albert Einstein", "Ulm", "Germany", "United States", "Princeton University"],
69	        "triples": [
70	            {"head": "Albert Einstein", "relation": "place of birth", "tail": "Ulm", "evidence": [0]},
71	            {"head": "Albert Einstein", "relation": "country of citizenship", "tail": "Germany", "evidence": [0]},
72	            {"head": "Albert Einstein", "relation": "employer", "tail": "Princeton University", "evidence": [2]},
73	        ],
74	    },
75	    {
76	        "sents": [
77	            "The Eiffel Tower is a wrought-iron lattice tower in Paris, France.",
78	            "It was designed by Gustave Eiffel's company and built between 1887 and 1889.",
79	            "The tower is 330 metres tall and the tallest structure in Paris.",
80	            "It has become a global cultural icon of France.",
81	        ],
82	        "entities": ["Eiffel Tower", "Paris", "France", "Gustave Eiffel"],
83	        "triples": [
84	            {"head": "Eiffel Tower", "relation": "located in", "tail": "Paris", "evidence": [0]},
85	            {"head": "Eiffel Tower", "relation": "country", "tail": "France", "evidence": [0, 3]},
86	            {"head": "Eiffel Tower", "relation": "creator", "tail": "Gustave Eiffel", "evidence": [1]},
87	        ],
88	    },
89	    {
90	        "sents": [
91	            "Tokyo is the capital and most populous city of Japan.",
92	            "The Greater Tokyo Area is the most populous metropolitan area in the world.",
93	            "Tokyo was originally known as Edo and was renamed in 1868.",
94	            "The city hosted the Summer Olympics in 1964 and 2021.",
95	        ],
96	        "entities": ["Tokyo", "Japan", "Edo"],
97	        "triples": [
98	            {"head": "Tokyo", "relation": "capital of", "tail": "Japan", "evidence": [0]},
99	            {"head": "Tokyo", "relation": "country", "tail": "Japan", "evidence": [0]},
100	        ],
101	    },
102	    {
103	        "sents": [
104	            "Marie Curie was a Polish-French physicist and chemist.",
105	            "She conducted pioneering research on radioactivity at the University of Paris.",
106	            "Curie was the first woman to win a Nobel Prize in 1903.",
107	            "She won a second Nobel Prize in Chemistry in 1911.",
108	            "Marie Curie was born in Warsaw, Poland.",
109	        ],
110	        "entities": ["Marie Curie", "University of Paris", "Warsaw", "Poland"],
111	        "triples": [
112	            {"head": "Marie Curie", "relation": "employer", "tail": "University of Paris", "evidence": [1]},
113	            {"head": "Marie Curie", "relation": "place of birth", "tail": "Warsaw", "evidence": [4]},
114	            {"head": "Marie Curie", "relation": "country of citizenship", "tail": "Poland", "evidence": [0, 4]},
115	        ],
116	    },
117	    {
118	        "sents": [
119	            "Amazon was founded by Jeff Bezos in Bellevue, Washington on July 5, 1994.",
120	            "The company started as an online bookstore.",
121	            "Amazon's headquarters is located in Seattle, Washington.",
122	            "It is one of the Big Five American technology companies.",
123	        ],
124	        "entities": ["Amazon", "Jeff Bezos", "Bellevue", "Seattle", "Washington"],
125	        "triples": [
126	            {"head": "Amazon", "relation": "founded by", "tail": "Jeff Bezos", "evidence": [0]},
127	            {"head": "Amazon", "relation": "headquarters location", "tail": "Seattle", "evidence": [2]},
128	            {"head": "Amazon", "relation": "location of formation", "tail": "Bellevue", "evidence": [0]},
129	        ],
130	    },
131	]
132	
133	
134	def generate_dummy_dataset(tokenizer, n_samples: int = 20, seed: int = SEED) -> Dataset:
135	    rng = random.Random(seed)
136	    items = []
137	    for i in range(n_samples):
138	        doc = DUMMY_DOCS[i % len(DUMMY_DOCS)]
139	        numbered = "\n".join(f"[{j}] {s}" for j, s in enumerate(doc["sents"]))
140	        entity_str = ", ".join(doc["entities"])
141	        user_msg = (
142	            f"Document:\n{numbered}\n\n"
143	            f"Entities: {entity_str}\n\n"
144	            "Extract all relation triples with evidence sentence IDs."
145	        )
146	        messages = [
147	            {"role": "system", "content": SYSTEM_PROMPT},
148	            {"role": "user", "content": user_msg},
149	        ]
150	        prompt = tokenizer.apply_chat_template(
151	            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,
152	        )
153	        gold = rng.sample(doc["triples"], k=min(len(doc["triples"]), rng.randint(1, 3)))
154	        items.append({
155	            "prompt": prompt,
156	            "gold_triples": json.dumps(gold, ensure_ascii=False),
157	        })
158	    return Dataset.from_list(items)
159	
160	
161	def _parse_json_output(text: str) -> list[dict]:
162	    try:
163	        return json.loads(text)
164	    except json.JSONDecodeError:
165	        start = text.find("[")
166	        end = text.rfind("]") + 1
167	        if start >= 0 and end > start:
168	            try:
169	                return json.loads(text[start:end])
170	            except json.JSONDecodeError:
171	                return []
172	    return []
173	
174	
175	def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
176	    rewards = []
177	    for text in completions:
178	        parsed = _parse_json_output(text)
179	        if not isinstance(parsed, list):
180	            rewards.append(0.0)
181	            continue
182	        if not parsed:
183	            rewards.append(0.1)
184	            continue
185	        valid = 0
186	        for item in parsed:
187	            if (isinstance(item, dict) and "head" in item
188	                    and "relation" in item and "tail" in item
189	                    and "evidence" in item
190	                    and isinstance(item["evidence"], list)):
191	                valid += 1
192	        rewards.append(valid / len(parsed))
193	    return rewards
194	
195	
196	class LossLogger:
197	    def __init__(self):
198	        self.losses = []
199	        self.grad_norms = []
200	
201	
202	loss_logger = LossLogger()
203	_orig_log = None
204	
205	
206	def _patch_trainer_logging(trainer):
207	    global _orig_log
208	    _orig_log = trainer.log
209	
210	    def patched_log(logs, **kwargs):
211	        if "loss" in logs:
212	            loss_logger.losses.append(logs["loss"])
213	        if "grad_norm" in logs:
214	            loss_logger.grad_norms.append(logs["grad_norm"])
215	        return _orig_log(logs, **kwargs)
216	
217	    trainer.log = patched_log
218	
219	
220	def main():
221	    t0 = time.time()
222	    local_rank = int(os.environ.get("LOCAL_RANK", 0))
223	
224	    print(f"[rank {local_rank}] Loading tokenizer: {MODEL_NAME}")
225	    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, padding_side="left")
226	    if tokenizer.pad_token is None:
227	        tokenizer.pad_token = tokenizer.eos_token
228	
229	    print(f"[rank {local_rank}] Generating dummy dataset...")
230	    dataset = generate_dummy_dataset(tokenizer, n_samples=20, seed=SEED)
231	
232	    print(f"[rank {local_rank}] Loading model with 4-bit QLoRA...")
233	    bnb_config = BitsAndBytesConfig(
234	        load_in_4bit=True,
235	        bnb_4bit_compute_dtype=torch.bfloat16,
236	        bnb_4bit_quant_type="nf4",
237	        bnb_4bit_use_double_quant=True,
238	    )
239	    model = AutoModelForCausalLM.from_pretrained(
240	        MODEL_NAME,
241	        quantization_config=bnb_config,
242	        trust_remote_code=True,
243	        attn_implementation="flash_attention_2",
244	    )
245	
246	    lora_config = LoraConfig(
247	        task_type=TaskType.CAUSAL_LM,
248	        r=64,
249	        lora_alpha=128,
250	        lora_dropout=0.05,
251	        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
252	    )
253	
254	    output_dir = "/tmp/freige_smoke_test"
255	    grpo_config = GRPOConfig(
256	        output_dir=output_dir,
257	        max_steps=NUM_STEPS,
258	        per_device_train_batch_size=1,
259	        gradient_accumulation_steps=2,
260	        learning_rate=5e-5,
261	        bf16=True,
262	        logging_steps=1,
263	        save_strategy="no",
264	        seed=SEED,
265	        num_generations=NUM_GENERATIONS,
266	        max_completion_length=MAX_COMPLETION_LENGTH,
267	        report_to="none",
268	        gradient_checkpointing=True,
269	        gradient_checkpointing_kwargs={"use_reentrant": False},
270	        deepspeed=DEEPSPEED_CONFIG,
271	    )
272	
273	    trainer = GRPOTrainer(
274	        model=model,
275	        args=grpo_config,
276	        train_dataset=dataset,
277	        reward_funcs=[format_reward_fn],
278	        peft_config=lora_config,
279	        processing_class=tokenizer,
280	    )
281	    _patch_trainer_logging(trainer)
282	
283	    print(f"[rank {local_rank}] Starting GRPO smoke test ({NUM_STEPS} steps)...")
284	    torch.cuda.reset_peak_memory_stats()
285	    trainer.train()
286	    elapsed = time.time() - t0
287	
288	    if local_rank == 0:
289	        print("\n" + "=" * 60)
290	        print("SMOKE TEST RESULTS")
291	        print("=" * 60)
292	
293	        print(f"\n--- Loss per step ---")
294	        for i, loss in enumerate(loss_logger.losses):
295	            print(f"  step {i + 1}: {loss:.4f}")
296	
297	        print(f"\n--- Gradient norms ---")
298	        for i, gn in enumerate(loss_logger.grad_norms):
299	            print(f"  step {i + 1}: {gn:.4f}")
300	
301	        print(f"\n--- GPU peak memory ---")
302	        for i in range(torch.cuda.device_count()):
303	            peak_mb = torch.cuda.max_memory_allocated(i) / 1024**2
304	            print(f"  GPU {i}: {peak_mb:.0f} MB ({peak_mb / 1024:.1f} GB)")
305	
306	        print(f"\n--- Total time: {elapsed:.1f}s ---")
307	
308	        has_nan_loss = any(math.isnan(l) for l in loss_logger.losses)
309	        has_nan_grad = any(math.isnan(g) for g in loss_logger.grad_norms) if loss_logger.grad_norms else False
310	        has_zero_grad = all(g == 0.0 for g in loss_logger.grad_norms) if loss_logger.grad_norms else True
311	
312	        if len(loss_logger.losses) >= 4:
313	            last3_avg = sum(loss_logger.losses[-3:]) / 3
314	            first_loss = loss_logger.losses[0]
315	            loss_decreased = last3_avg < first_loss
316	        else:
317	            loss_decreased = True
318	
319	        passed = loss_decreased and not has_nan_loss and not has_nan_grad and not has_zero_grad
320	
321	        print(f"\n--- Diagnostics ---")
322	        print(f"  Loss decreased (last 3 avg < first): {loss_decreased}")
323	        print(f"  NaN in loss: {has_nan_loss}")
324	        print(f"  NaN in grad_norm: {has_nan_grad}")
325	        print(f"  All-zero grad_norm: {has_zero_grad}")
326	        print(f"\n{'PASS' if passed else 'FAIL'}")
327	        print("=" * 60)
328	
329	
330	if __name__ == "__main__":
331	    main()
332	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "f12811b8-0def-42e2-8f98-db7e9ab9fe0f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
      "content": "#!/usr/bin/env python3\n# Launch:\n#   accelerate launch --num_processes 4 --mixed_precision bf16 training/smoke_test.py\n#   deepspeed --num_gpus 4 training/smoke_test.py\n\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-3 on 4xRTX 5090 (32GB).\n\nUses synthetic data only. No freige imports. Runs 10 training steps and reports\nloss trend, peak VRAM, gradient norms, and PASS/FAIL.\n\"\"\"\n\nimport json\nimport math\nimport os\nimport random\nimport time\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nos.environ.setdefault(\"WANDB_DISABLED\", \"true\")\n\nSEED = 42\nNUM_STEPS = 10\nNUM_GENERATIONS = 4\nMAX_COMPLETION_LENGTH = 256\nMODEL_NAME = \"Qwen/Qwen3-4B\"\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\nDEEPSPEED_CONFIG = {\n    \"bf16\": {\"enabled\": True},\n    \"zero_optimization\": {\n        \"stage\": 3,\n        \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"offload_param\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"overlap_comm\": True,\n        \"contiguous_gradients\": True,\n        \"sub_group_size\": 1e9,\n        \"reduce_bucket_size\": \"auto\",\n        \"stage3_prefetch_bucket_size\": \"auto\",\n        \"stage3_param_persistence_threshold\": \"auto\",\n        \"stage3_max_live_parameters\": 1e9,\n        \"stage3_max_reuse_distance\": 1e9,\n        \"stage3_gather_16bit_weights_on_model_save\": True,\n    },\n    \"gradient_accumulation_steps\": \"auto\",\n    \"gradient_clipping\": \"auto\",\n    \"train_batch_size\": \"auto\",\n    \"train_micro_batch_size_per_gpu\": \"auto\",\n}\n\nDUMMY_DOCS = [\n    {\n        \"sents\": [\n            \"Albert Einstein was born in Ulm, Germany in 1879.\",\n            \"He developed the theory of relativity while working at the Swiss Patent Office.\",\n            \"Einstein later moved to the United States and joined Princeton University.\",\n            \"He received the Nobel Prize in Physics in 1921 for his work on the photoelectric effect.\",\n        ],\n        \"entities\": [\"Albert Einstein\", \"Ulm\", \"Germany\", \"United States\", \"Princeton University\"],\n        \"triples\": [\n            {\"head\": \"Albert Einstein\", \"relation\": \"place of birth\", \"tail\": \"Ulm\", \"evidence\": [0]},\n            {\"head\": \"Albert Einstein\", \"relation\": \"country of citizenship\", \"tail\": \"Germany\", \"evidence\": [0]},\n            {\"head\": \"Albert Einstein\", \"relation\": \"employer\", \"tail\": \"Princeton University\", \"evidence\": [2]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"The Eiffel Tower is a wrought-iron lattice tower in Paris, France.\",\n            \"It was designed by Gustave Eiffel's company and built between 1887 and 1889.\",\n            \"The tower is 330 metres tall and the tallest structure in Paris.\",\n            \"It has become a global cultural icon of France.\",\n        ],\n        \"entities\": [\"Eiffel Tower\", \"Paris\", \"France\", \"Gustave Eiffel\"],\n        \"triples\": [\n            {\"head\": \"Eiffel Tower\", \"relation\": \"located in\", \"tail\": \"Paris\", \"evidence\": [0]},\n            {\"head\": \"Eiffel Tower\", \"relation\": \"country\", \"tail\": \"France\", \"evidence\": [0, 3]},\n            {\"head\": \"Eiffel Tower\", \"relation\": \"creator\", \"tail\": \"Gustave Eiffel\", \"evidence\": [1]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Tokyo is the capital and most populous city of Japan.\",\n            \"The Greater Tokyo Area is the most populous metropolitan area in the world.\",\n            \"Tokyo was originally known as Edo and was renamed in 1868.\",\n            \"The city hosted the Summer Olympics in 1964 and 2021.\",\n        ],\n        \"entities\": [\"Tokyo\", \"Japan\", \"Edo\"],\n        \"triples\": [\n            {\"head\": \"Tokyo\", \"relation\": \"capital of\", \"tail\": \"Japan\", \"evidence\": [0]},\n            {\"head\": \"Tokyo\", \"relation\": \"country\", \"tail\": \"Japan\", \"evidence\": [0]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Marie Curie was a Polish-French physicist and chemist.\",\n            \"She conducted pioneering research on radioactivity at the University of Paris.\",\n            \"Curie was the first woman to win a Nobel Prize in 1903.\",\n            \"She won a second Nobel Prize in Chemistry in 1911.\",\n            \"Marie Curie was born in Warsaw, Poland.\",\n        ],\n        \"entities\": [\"Marie Curie\", \"University of Paris\", \"Warsaw\", \"Poland\"],\n        \"triples\": [\n            {\"head\": \"Marie Curie\", \"relation\": \"employer\", \"tail\": \"University of Paris\", \"evidence\": [1]},\n            {\"head\": \"Marie Curie\", \"relation\": \"place of birth\", \"tail\": \"Warsaw\", \"evidence\": [4]},\n            {\"head\": \"Marie Curie\", \"relation\": \"country of citizenship\", \"tail\": \"Poland\", \"evidence\": [0, 4]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Amazon was founded by Jeff Bezos in Bellevue, Washington on July 5, 1994.\",\n            \"The company started as an online bookstore.\",\n            \"Amazon's headquarters is located in Seattle, Washington.\",\n            \"It is one of the Big Five American technology companies.\",\n        ],\n        \"entities\": [\"Amazon\", \"Jeff Bezos\", \"Bellevue\", \"Seattle\", \"Washington\"],\n        \"triples\": [\n            {\"head\": \"Amazon\", \"relation\": \"founded by\", \"tail\": \"Jeff Bezos\", \"evidence\": [0]},\n            {\"head\": \"Amazon\", \"relation\": \"headquarters location\", \"tail\": \"Seattle\", \"evidence\": [2]},\n            {\"head\": \"Amazon\", \"relation\": \"location of formation\", \"tail\": \"Bellevue\", \"evidence\": [0]},\n        ],\n    },\n]\n\n\ndef generate_dummy_dataset(tokenizer, n_samples: int = 20, seed: int = SEED) -> Dataset:\n    rng = random.Random(seed)\n    items = []\n    for i in range(n_samples):\n        doc = DUMMY_DOCS[i % len(DUMMY_DOCS)]\n        numbered = \"\\n\".join(f\"[{j}] {s}\" for j, s in enumerate(doc[\"sents\"]))\n        entity_str = \", \".join(doc[\"entities\"])\n        user_msg = (\n            f\"Document:\\n{numbered}\\n\\n\"\n            f\"Entities: {entity_str}\\n\\n\"\n            \"Extract all relation triples with evidence sentence IDs.\"\n        )\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": user_msg},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,\n        )\n        gold = rng.sample(doc[\"triples\"], k=min(len(doc[\"triples\"]), rng.randint(1, 3)))\n        items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold, ensure_ascii=False),\n        })\n    return Dataset.from_list(items)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\nclass LossLogger:\n    def __init__(self):\n        self.losses = []\n        self.grad_norms = []\n\n\nloss_logger = LossLogger()\n_orig_log = None\n\n\ndef _patch_trainer_logging(trainer):\n    global _orig_log\n    _orig_log = trainer.log\n\n    def patched_log(logs, **kwargs):\n        if \"loss\" in logs:\n            loss_logger.losses.append(logs[\"loss\"])\n        if \"grad_norm\" in logs:\n            loss_logger.grad_norms.append(logs[\"grad_norm\"])\n        return _orig_log(logs, **kwargs)\n\n    trainer.log = patched_log\n\n\ndef main():\n    t0 = time.time()\n    local_rank = int(os.environ.get(\"LOCAL_RANK\", 0))\n\n    print(f\"[rank {local_rank}] Loading tokenizer: {MODEL_NAME}\")\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, padding_side=\"left\")\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"[rank {local_rank}] Generating dummy dataset...\")\n    dataset = generate_dummy_dataset(tokenizer, n_samples=20, seed=SEED)\n\n    print(f\"[rank {local_rank}] Loading model with 4-bit QLoRA...\")\n    bnb_config = BitsAndBytesConfig(\n        load_in_4bit=True,\n        bnb_4bit_compute_dtype=torch.bfloat16,\n        bnb_4bit_quant_type=\"nf4\",\n        bnb_4bit_use_double_quant=True,\n    )\n    model = AutoModelForCausalLM.from_pretrained(\n        MODEL_NAME,\n        quantization_config=bnb_config,\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=64,\n        lora_alpha=128,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    output_dir = \"/tmp/freige_smoke_test\"\n    grpo_config = GRPOConfig(\n        output_dir=output_dir,\n        max_steps=NUM_STEPS,\n        per_device_train_batch_size=1,\n        gradient_accumulation_steps=2,\n        learning_rate=5e-5,\n        bf16=True,\n        logging_steps=1,\n        save_strategy=\"no\",\n        seed=SEED,\n        num_generations=NUM_GENERATIONS,\n        max_completion_length=MAX_COMPLETION_LENGTH,\n        report_to=\"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=DEEPSPEED_CONFIG,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=dataset,\n        reward_funcs=[format_reward_fn],\n        peft_config=lora_config,\n        processing_class=tokenizer,\n    )\n    _patch_trainer_logging(trainer)\n\n    print(f\"[rank {local_rank}] Starting GRPO smoke test ({NUM_STEPS} steps)...\")\n    torch.cuda.reset_peak_memory_stats()\n    trainer.train()\n    elapsed = time.time() - t0\n\n    if local_rank == 0:\n        print(\"\\n\" + \"=\" * 60)\n        print(\"SMOKE TEST RESULTS\")\n        print(\"=\" * 60)\n\n        print(f\"\\n--- Loss per step ---\")\n        for i, loss in enumerate(loss_logger.losses):\n            print(f\"  step {i + 1}: {loss:.4f}\")\n\n        print(f\"\\n--- Gradient norms ---\")\n        for i, gn in enumerate(loss_logger.grad_norms):\n            print(f\"  step {i + 1}: {gn:.4f}\")\n\n        print(f\"\\n--- GPU peak memory ---\")\n        for i in range(torch.cuda.device_count()):\n            peak_mb = torch.cuda.max_memory_allocated(i) / 1024**2\n            print(f\"  GPU {i}: {peak_mb:.0f} MB ({peak_mb / 1024:.1f} GB)\")\n\n        print(f\"\\n--- Total time: {elapsed:.1f}s ---\")\n\n        has_nan_loss = any(math.isnan(l) for l in loss_logger.losses)\n        has_nan_grad = any(math.isnan(g) for g in loss_logger.grad_norms) if loss_logger.grad_norms else False\n        has_zero_grad = all(g == 0.0 for g in loss_logger.grad_norms) if loss_logger.grad_norms else True\n\n        if len(loss_logger.losses) >= 4:\n            last3_avg = sum(loss_logger.losses[-3:]) / 3\n            first_loss = loss_logger.losses[0]\n            loss_decreased = last3_avg < first_loss\n        else:\n            loss_decreased = True\n\n        passed = loss_decreased and not has_nan_loss and not has_nan_grad and not has_zero_grad\n\n        print(f\"\\n--- Diagnostics ---\")\n        print(f\"  Loss decreased (last 3 avg < first): {loss_decreased}\")\n        print(f\"  NaN in loss: {has_nan_loss}\")\n        print(f\"  NaN in grad_norm: {has_nan_grad}\")\n        print(f\"  All-zero grad_norm: {has_zero_grad}\")\n        print(f\"\\n{'PASS' if passed else 'FAIL'}\")\n        print(\"=\" * 60)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 332,
      "startLine": 1,
      "totalLines": 332
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now I have all four files read. Let me make the changes:

1. **sft_trainer.py**: 
   - `DEFAULT_MODEL` → `/root/autodl-tmp/models/Qwen3-4B`
   - `attn_implementation` → `"sdpa"`
   - Header comment deepspeed reference is already `deepspeed_zero2.json` - good

2. **grpo_trainer.py**:
   - `--model_name` default → `/root/autodl-tmp/models/Qwen3-4B`
   - `attn_implementation` → `"sdpa"`
   - Header comment `deepspeed_zero3.json` → `deepspeed_zero2.json`
   - Add `--tau_start` and `--tau_end` params with tau scheduling in CEDRewardWrapper

3. **ced_reward.py**: Looking at the no-hard-negative handling around line 236-237, when `hard_negative_sents` is empty, `p_neg` gets set to 0.0, which simplifies the reward calculation to `R_CED = max(0, p_pos - 0) * I(p_pos > tau) = p_pos * I(p_pos > tau)`.

4. **smoke_test.py**: Need to update the DeepSpeed config stage to 2 and remove `offload_param`, change the model path to `/root/autodl-tmp/models/Qwen3-4B`, set `attn_implementation` to `"sdpa"`, and verify `NUM_GENERATIONS` is already set to 4. Ready to apply these changes now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "d62caa03-710b-48ad-90ca-a066c6ff3eb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tfkCpbx2ZMuK5NAoxaC9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18476,
      "cache_read_input_tokens": 24138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18476
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 14_

All files read. Now applying the changes.

**ced_reward.py** — confirmed: `compute_ced_reward()` lines 236-237 already handle empty `hard_negative_sents` correctly (`p_neg = 0.0`, reward degrades to flat NLI). No changes needed.

Now making the edits to the other three files plus tau scheduling in grpo_trainer.py.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "9a915dae-0fa4-49ac-9622-4f03a16722e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tfkCpbx2ZMuK5NAoxaC9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18476,
      "cache_read_input_tokens": 24138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18476
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01YEHCTL43k65VTDwgxBYUP5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
  "old_string": "DEFAULT_MODEL = \"Qwen/Qwen3-4B\"",
  "new_string": "DEFAULT_MODEL = \"/root/autodl-tmp/models/Qwen3-4B\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "bba106ba-5174-438a-ad4d-b2183001e1b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tfkCpbx2ZMuK5NAoxaC9s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18476,
      "cache_read_input_tokens": 24138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18476
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T06:09:05.473Z_

<details><summary>↩ Tool result · `toolu_01YEHCTL43k65VTDwgxBYUP5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "2f78dbc9-1aaf-4da6-9f64-4fd65ab361b3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
    "oldString": "DEFAULT_MODEL = \"Qwen/Qwen3-4B\"",
    "newString": "DEFAULT_MODEL = \"/root/autodl-tmp/models/Qwen3-4B\"",
    "originalFile": "\"\"\"SFT 训练脚本: Qwen3-4B + QLoRA 在 DocRED 上微调。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练。\n默认启用 4-bit QLoRA 量化，适配 RTX 5090 32GB x4。\n\n单卡:   python -m freige.training.sft_trainer --output_dir ./sft_output\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.sft_trainer --deepspeed configs/deepspeed_zero2.json\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nfrom dataclasses import dataclass, field\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, TaskType, get_peft_model\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    BitsAndBytesConfig,\n    TrainingArguments,\n)\nfrom trl import SFTTrainer, SFTConfig\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\nDEFAULT_MODEL = \"Qwen/Qwen3-4B\"\n\n\ndef build_chat_messages(instruction: str, input_text: str, output_text: str = None):\n    \"\"\"构建 Qwen3 chat 格式的消息列表。\"\"\"\n    messages = [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": f\"{instruction}\\n\\n{input_text}\"},\n    ]\n    if output_text is not None:\n        messages.append({\"role\": \"assistant\", \"content\": output_text})\n    return messages\n\n\ndef prepare_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n    max_length: int = 4096,\n) -> Dataset:\n    \"\"\"加载并格式化 DocRED 数据为 SFT 训练格式。\"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    formatted = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = build_chat_messages(\n            sft_sample[\"instruction\"],\n            sft_sample[\"input\"],\n            sft_sample[\"output\"],\n        )\n        text = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=False,\n            enable_thinking=False,\n        )\n        formatted.append({\"text\": text})\n\n    logger.info(\"Prepared %d SFT samples from %d documents\", len(formatted), len(groups))\n    return Dataset.from_list(formatted)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE SFT Training\")\n    parser.add_argument(\"--model_name\", type=str, default=DEFAULT_MODEL)\n    parser.add_argument(\"--data_dir\", type=str, default=None,\n                        help=\"DocRED JSON 目录\")\n    parser.add_argument(\"--output_dir\", type=str, default=\"./sft_output\")\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--lora_dropout\", type=float, default=0.05)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=3)\n    parser.add_argument(\"--learning_rate\", type=float, default=2e-4)\n    parser.add_argument(\"--warmup_ratio\", type=float, default=0.05)\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-sft\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"right\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n        max_length=args.max_length,\n    )\n    eval_dataset = prepare_dataset(\n        data_dir=args.data_dir,\n        split=\"dev\",\n        tokenizer=tokenizer,\n        max_length=args.max_length,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n    model.config.use_cache = False\n    model.gradient_checkpointing_enable()\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=args.lora_dropout,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n    model = get_peft_model(model, lora_config)\n    model.print_trainable_parameters()\n\n    training_args = SFTConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        per_device_eval_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        warmup_ratio=args.warmup_ratio,\n        bf16=args.bf16,\n        logging_steps=10,\n        eval_strategy=\"epoch\",\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        load_best_model_at_end=True,\n        metric_for_best_model=\"eval_loss\",\n        greater_is_better=False,\n        seed=args.seed,\n        max_seq_length=args.max_length,\n        dataset_text_field=\"text\",\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = SFTTrainer(\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        eval_dataset=eval_dataset,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting SFT training...\")\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"SFT training complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 38,
        "oldLines": 7,
        "newStart": 38,
        "newLines": 7,
        "lines": [
          "     \"Output as a JSON list.\"",
          " )",
          " ",
          "-DEFAULT_MODEL = \"Qwen/Qwen3-4B\"",
          "+DEFAULT_MODEL = \"/root/autodl-tmp/models/Qwen3-4B\"",
          " ",
          " ",
          " def build_chat_messages(instruction: str, input_text: str, output_text: str = None):"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01WnxXkyV55EDju1sByi4tBV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
  "old_string": "        attn_implementation=\"flash_attention_2\",",
  "new_string": "        attn_implementation=\"sdpa\","
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "62ca53e1-2c5e-482e-a96a-85996fb7f607",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8XkomEhobhkau4wGnwN58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 42614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 757
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T06:09:09.068Z_

<details><summary>↩ Tool result · `toolu_01WnxXkyV55EDju1sByi4tBV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "a96fb713-f25a-4d3c-bb52-7e6956a4498f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
    "oldString": "        attn_implementation=\"flash_attention_2\",",
    "newString": "        attn_implementation=\"sdpa\",",
    "originalFile": "\"\"\"SFT 训练脚本: Qwen3-4B + QLoRA 在 DocRED 上微调。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练。\n默认启用 4-bit QLoRA 量化，适配 RTX 5090 32GB x4。\n\n单卡:   python -m freige.training.sft_trainer --output_dir ./sft_output\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.sft_trainer --deepspeed configs/deepspeed_zero2.json\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nfrom dataclasses import dataclass, field\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, TaskType, get_peft_model\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    BitsAndBytesConfig,\n    TrainingArguments,\n)\nfrom trl import SFTTrainer, SFTConfig\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\nDEFAULT_MODEL = \"/root/autodl-tmp/models/Qwen3-4B\"\n\n\ndef build_chat_messages(instruction: str, input_text: str, output_text: str = None):\n    \"\"\"构建 Qwen3 chat 格式的消息列表。\"\"\"\n    messages = [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": f\"{instruction}\\n\\n{input_text}\"},\n    ]\n    if output_text is not None:\n        messages.append({\"role\": \"assistant\", \"content\": output_text})\n    return messages\n\n\ndef prepare_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n    max_length: int = 4096,\n) -> Dataset:\n    \"\"\"加载并格式化 DocRED 数据为 SFT 训练格式。\"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    formatted = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = build_chat_messages(\n            sft_sample[\"instruction\"],\n            sft_sample[\"input\"],\n            sft_sample[\"output\"],\n        )\n        text = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=False,\n            enable_thinking=False,\n        )\n        formatted.append({\"text\": text})\n\n    logger.info(\"Prepared %d SFT samples from %d documents\", len(formatted), len(groups))\n    return Dataset.from_list(formatted)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE SFT Training\")\n    parser.add_argument(\"--model_name\", type=str, default=DEFAULT_MODEL)\n    parser.add_argument(\"--data_dir\", type=str, default=None,\n                        help=\"DocRED JSON 目录\")\n    parser.add_argument(\"--output_dir\", type=str, default=\"./sft_output\")\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--lora_dropout\", type=float, default=0.05)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=3)\n    parser.add_argument(\"--learning_rate\", type=float, default=2e-4)\n    parser.add_argument(\"--warmup_ratio\", type=float, default=0.05)\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-sft\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"right\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n        max_length=args.max_length,\n    )\n    eval_dataset = prepare_dataset(\n        data_dir=args.data_dir,\n        split=\"dev\",\n        tokenizer=tokenizer,\n        max_length=args.max_length,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n    model.config.use_cache = False\n    model.gradient_checkpointing_enable()\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=args.lora_dropout,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n    model = get_peft_model(model, lora_config)\n    model.print_trainable_parameters()\n\n    training_args = SFTConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        per_device_eval_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        warmup_ratio=args.warmup_ratio,\n        bf16=args.bf16,\n        logging_steps=10,\n        eval_strategy=\"epoch\",\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        load_best_model_at_end=True,\n        metric_for_best_model=\"eval_loss\",\n        greater_is_better=False,\n        seed=args.seed,\n        max_seq_length=args.max_length,\n        dataset_text_field=\"text\",\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = SFTTrainer(\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        eval_dataset=eval_dataset,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting SFT training...\")\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"SFT training complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 141,
        "oldLines": 7,
        "newStart": 141,
        "newLines": 7,
        "lines": [
          "     logger.info(\"Loading model: %s\", args.model_name)",
          "     model_kwargs = dict(",
          "         trust_remote_code=True,",
          "-        attn_implementation=\"flash_attention_2\",",
          "+        attn_implementation=\"sdpa\",",
          "     )",
          "     if args.quantize:",
          "         logger.info(\"Using 4-bit QLoRA quantization\")"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 19_

sft_trainer.py done (header comment already references `deepspeed_zero2.json`). Now grpo_trainer.py:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "6329689d-1308-447c-9575-edcec18dc810",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzMnkZYN7Wyeyx7Uwjw7Cd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 43371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01GYvg9QVN4cGiY7n3EKDa1A`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero3.json \\\n            --stage 1 --reward_device cpu",
  "new_string": "多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "b34ce3b0-a6e4-4e95-94ad-5f8611917eab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzMnkZYN7Wyeyx7Uwjw7Cd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 43371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T06:09:14.756Z_

<details><summary>↩ Tool result · `toolu_01GYvg9QVN4cGiY7n3EKDa1A`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "3eb89fe2-a387-4610-b48a-fc029df03ad1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero3.json \\\n            --stage 1 --reward_device cpu",
    "newString": "多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero3.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.tau = tau\n        self.mode = mode\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=self.tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=self.tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau\", type=float, default=0.5)\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 7,
        "newStart": 4,
        "newLines": 7,
        "lines": [
          " ",
          " 单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1",
          " 多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\",
          "-            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero3.json \\",
          "+            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\",
          "             --stage 1 --reward_device cpu",
          " 不量化: 加 --no_quantize",
          " \"\"\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_015sW1G2FAZbfsxiQhMtHYRR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")",
  "new_string": "    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "434ffcc6-3f6a-49fa-880f-219aa6ca8543",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013H8exVGr8PcMmu7VJQoHKr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 43599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
      },
      "output_tokens": 73,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T06:09:19.193Z_

<details><summary>↩ Tool result · `toolu_015sW1G2FAZbfsxiQhMtHYRR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "fde4e47b-5544-4283-9650-2a83a1f68d38",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")",
    "newString": "    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.tau = tau\n        self.mode = mode\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=self.tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=self.tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau\", type=float, default=0.5)\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 278,
        "oldLines": 7,
        "newStart": 278,
        "newLines": 7,
        "lines": [
          " ",
          " def main():",
          "     parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")",
          "-    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-4B\",",
          "+    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",",
          "                         help=\"基础模型或 SFT checkpoint 路径\")",
          "     parser.add_argument(\"--sft_adapter\", type=str, default=None,",
          "                         help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01VuQMvPtbcHgLoEvPQPq2jX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "        attn_implementation=\"flash_attention_2\",",
  "new_string": "        attn_implementation=\"sdpa\","
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "0f1e3966-2297-4d32-b133-45b73c166875",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KT6rcvpsNR4aK7FRztX7HW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 44066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T06:09:24.606Z_

<details><summary>↩ Tool result · `toolu_01VuQMvPtbcHgLoEvPQPq2jX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "c59b88c1-726c-4903-9d72-4065594d4013",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "        attn_implementation=\"flash_attention_2\",",
    "newString": "        attn_implementation=\"sdpa\",",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.tau = tau\n        self.mode = mode\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=self.tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=self.tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau\", type=float, default=0.5)\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 333,
        "oldLines": 7,
        "newStart": 333,
        "newLines": 7,
        "lines": [
          "     logger.info(\"Loading model: %s\", args.model_name)",
          "     model_kwargs = dict(",
          "         trust_remote_code=True,",
          "-        attn_implementation=\"flash_attention_2\",",
          "+        attn_implementation=\"sdpa\",",
          "     )",
          "     if args.quantize:",
          "         logger.info(\"Using 4-bit QLoRA quantization\")"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 26_

Now replacing `--tau` with `--tau_start` / `--tau_end` and updating CEDRewardWrapper for tau scheduling:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "d2c96be5-8c0c-4740-bdf0-9bd566bf8720",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4NeBxi9xQoTVZS3VXVThr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 44376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01QYUsgeaaVjKDDjKsSkoLXd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "    parser.add_argument(\"--tau\", type=float, default=0.5)",
  "new_string": "    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "1637b2e5-8ad7-44c4-ad9d-74650a6a6f48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4NeBxi9xQoTVZS3VXVThr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 44376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T06:09:30.502Z_

<details><summary>↩ Tool result · `toolu_01QYUsgeaaVjKDDjKsSkoLXd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "7eed8293-25ca-41fd-9eab-796c54e1136c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "    parser.add_argument(\"--tau\", type=float, default=0.5)",
    "newString": "    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.tau = tau\n        self.mode = mode\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=self.tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=self.tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau\", type=float, default=0.5)\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 302,
        "oldLines": 7,
        "newStart": 302,
        "newLines": 10,
        "lines": [
          "     parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)",
          "     parser.add_argument(\"--num_epochs\", type=int, default=1)",
          "     parser.add_argument(\"--learning_rate\", type=float, default=5e-5)",
          "-    parser.add_argument(\"--tau\", type=float, default=0.5)",
          "+    parser.add_argument(\"--tau_start\", type=float, default=0.3,",
          "+                        help=\"CED tau 初始值\")",
          "+    parser.add_argument(\"--tau_end\", type=float, default=0.5,",
          "+                        help=\"CED tau 最终值（线性调度）\")",
          "     parser.add_argument(\"--bf16\", action=\"store_true\", default=True)",
          "     parser.add_argument(\"--seed\", type=int, default=42)",
          "     parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 29_

Now update CEDRewardWrapper to support tau scheduling:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "0b0c2198-a5b5-4d61-bf53-bda0b81e96a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JArCCs9CNpMV99XQ2Pxi9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 335,
      "cache_read_input_tokens": 44604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 335
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01KYzhQY269dFh53nFhzZQe1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.tau = tau\n        self.mode = mode",
  "new_string": "    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n        tau_start: float = None,\n        tau_end: float = None,\n        total_steps: int = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.mode = mode\n        self._call_count = 0\n        if tau_start is not None and tau_end is not None:\n            self.tau_start = tau_start\n            self.tau_end = tau_end\n            self.total_steps = total_steps\n        else:\n            self.tau_start = tau\n            self.tau_end = tau\n            self.total_steps = None"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "87f9f22c-c9e4-49ff-9108-0d4932d1525d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JArCCs9CNpMV99XQ2Pxi9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 335,
      "cache_read_input_tokens": 44604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 335
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T06:09:38.145Z_

<details><summary>↩ Tool result · `toolu_01KYzhQY269dFh53nFhzZQe1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "95a9ba33-5f99-436b-8905-b97d3018dbc7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.tau = tau\n        self.mode = mode",
    "newString": "    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n        tau_start: float = None,\n        tau_end: float = None,\n        total_steps: int = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.mode = mode\n        self._call_count = 0\n        if tau_start is not None and tau_end is not None:\n            self.tau_start = tau_start\n            self.tau_end = tau_end\n            self.total_steps = total_steps\n        else:\n            self.tau_start = tau\n            self.tau_end = tau\n            self.total_steps = None",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.tau = tau\n        self.mode = mode\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=self.tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=self.tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 134,
        "oldLines": 12,
        "newStart": 134,
        "newLines": 23,
        "lines": [
          "         tau: float = 0.5,",
          "         mode: str = \"ced\",",
          "         device: str = None,",
          "+        tau_start: float = None,",
          "+        tau_end: float = None,",
          "+        total_steps: int = None,",
          "     ):",
          "         from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple",
          "         self.reward_model = CEDRewardModel(model_name=nli_model, device=device)",
          "         self.verbalize = verbalize_triple",
          "-        self.tau = tau",
          "         self.mode = mode",
          "+        self._call_count = 0",
          "+        if tau_start is not None and tau_end is not None:",
          "+            self.tau_start = tau_start",
          "+            self.tau_end = tau_end",
          "+            self.total_steps = total_steps",
          "+        else:",
          "+            self.tau_start = tau",
          "+            self.tau_end = tau",
          "+            self.total_steps = None",
          " ",
          "     def __call__(",
          "         self,"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 32_

Now update the `__call__` method to compute tau dynamically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "cc626fb0-f60d-452b-9c4e-7e73654a22a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Du414StYfKVmMRh1AxjeM6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 44939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 616
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01V3Qwd9pJLZKwtmWjEpnnLX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):",
  "new_string": "    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = min(self._call_count / max(self._call_count, 1), 1.0)\n        return self.tau_start + (self.tau_end - self.tau_start) * progress\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        current_tau = self.tau\n        self._call_count += 1\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "5b8c3128-49f5-4ccf-904a-ffb701f54892",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Du414StYfKVmMRh1AxjeM6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 44939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 616
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T06:09:47.446Z_

<details><summary>↩ Tool result · `toolu_01V3Qwd9pJLZKwtmWjEpnnLX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "19c77ae0-c467-4c4e-acd1-d4b3dded7a44",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):",
    "newString": "    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = min(self._call_count / max(self._call_count, 1), 1.0)\n        return self.tau_start + (self.tau_end - self.tau_start) * progress\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        current_tau = self.tau\n        self._call_count += 1\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n        tau_start: float = None,\n        tau_end: float = None,\n        total_steps: int = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.mode = mode\n        self._call_count = 0\n        if tau_start is not None and tau_end is not None:\n            self.tau_start = tau_start\n            self.tau_end = tau_end\n            self.total_steps = total_steps\n        else:\n            self.tau_start = tau\n            self.tau_end = tau\n            self.total_steps = None\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=self.tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=self.tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 152,
        "oldLines": 6,
        "newStart": 152,
        "newLines": 14,
        "lines": [
          "             self.tau_end = tau",
          "             self.total_steps = None",
          " ",
          "+    @property",
          "+    def tau(self) -> float:",
          "+        if self.total_steps and self.total_steps > 0:",
          "+            progress = min(self._call_count / self.total_steps, 1.0)",
          "+        else:",
          "+            progress = min(self._call_count / max(self._call_count, 1), 1.0)",
          "+        return self.tau_start + (self.tau_end - self.tau_start) * progress",
          "+",
          "     def __call__(",
          "         self,",
          "         completions: list[str],"
        ]
      },
      {
        "oldStart": 164,
        "oldLines": 6,
        "newStart": 172,
        "newLines": 8,
        "lines": [
          "         all_sents: JSON 字符串列表，每个元素为文档句子列表。",
          "         gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。",
          "         \"\"\"",
          "+        current_tau = self.tau",
          "+        self._call_count += 1",
          "         num_gen = len(completions) // len(all_sents)",
          "         rewards = []",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 35_

Now update the reward computation inside `__call__` to use `current_tau` instead of `self.tau`:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "96eeb60f-9684-4c15-97da-605e169d6558",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ua9hrdiatWosZp4ujQWrC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 45555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 695
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01NzRhzoTuCuTvsrFoip7Gwi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=self.tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=self.tau,\n                    )",
  "new_string": "                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=current_tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=current_tau,\n                    )"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "81232ad2-a4f2-4169-8487-f957a35b8acc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ua9hrdiatWosZp4ujQWrC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 695,
      "cache_read_input_tokens": 45555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 695
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T06:09:55.071Z_

<details><summary>↩ Tool result · `toolu_01NzRhzoTuCuTvsrFoip7Gwi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "511fde7a-45b6-461d-9439-b4c64a4e704d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=self.tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=self.tau,\n                    )",
    "newString": "                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=current_tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=current_tau,\n                    )",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n        tau_start: float = None,\n        tau_end: float = None,\n        total_steps: int = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.mode = mode\n        self._call_count = 0\n        if tau_start is not None and tau_end is not None:\n            self.tau_start = tau_start\n            self.tau_end = tau_end\n            self.total_steps = total_steps\n        else:\n            self.tau_start = tau\n            self.tau_end = tau\n            self.total_steps = None\n\n    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = min(self._call_count / max(self._call_count, 1), 1.0)\n        return self.tau_start + (self.tau_end - self.tau_start) * progress\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        current_tau = self.tau\n        self._call_count += 1\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=self.tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=self.tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 232,
        "oldLines": 11,
        "newStart": 232,
        "newLines": 11,
        "lines": [
          " ",
          "                 if self.mode == \"flat_nli\":",
          "                     result = self.reward_model.compute_flat_nli_reward(",
          "-                        claim, cited_sents, tau=self.tau,",
          "+                        claim, cited_sents, tau=current_tau,",
          "                     )",
          "                 else:",
          "                     result = self.reward_model.compute_ced_reward(",
          "-                        claim, cited_sents, hard_neg_sents, tau=self.tau,",
          "+                        claim, cited_sents, hard_neg_sents, tau=current_tau,",
          "                     )",
          "                 triple_rewards.append(result[\"reward\"])",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 38_

Now update the `main()` where CEDRewardWrapper is instantiated to pass tau_start/tau_end:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "dd8f5579-4302-4fd3-8cf1-45656a2fe605",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUwA8YXS5LiMPxmdLorGRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 46250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 539
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_016q6zQNLsyZJL7C2bqLBzau`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )",
  "new_string": "        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n        )"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "7ea1bedd-286c-4afa-a4e0-12a19e18a5e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUwA8YXS5LiMPxmdLorGRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 46250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 539
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T06:10:00.923Z_

<details><summary>↩ Tool result · `toolu_016q6zQNLsyZJL7C2bqLBzau`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "77241d0b-18d7-4eb1-b79b-5d16116f97f0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )",
    "newString": "        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n        )",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n        tau_start: float = None,\n        tau_end: float = None,\n        total_steps: int = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.mode = mode\n        self._call_count = 0\n        if tau_start is not None and tau_end is not None:\n            self.tau_start = tau_start\n            self.tau_end = tau_end\n            self.total_steps = total_steps\n        else:\n            self.tau_start = tau\n            self.tau_end = tau\n            self.total_steps = None\n\n    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = min(self._call_count / max(self._call_count, 1), 1.0)\n        return self.tau_start + (self.tau_end - self.tau_start) * progress\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        current_tau = self.tau\n        self._call_count += 1\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=current_tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=current_tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            tau=args.tau,\n            mode=mode,\n            device=args.reward_device,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 382,
        "oldLines": 9,
        "newStart": 382,
        "newLines": 10,
        "lines": [
          "         mode = \"flat_nli\" if args.stage == 2 else \"ced\"",
          "         ced_wrapper = CEDRewardWrapper(",
          "             nli_model=args.nli_model,",
          "-            tau=args.tau,",
          "             mode=mode,",
          "             device=args.reward_device,",
          "+            tau_start=args.tau_start,",
          "+            tau_end=args.tau_end,",
          "         )",
          "         reward_fns.append(ced_wrapper)",
          "         logger.info(\"Stage %d: using %s reward\", args.stage, mode)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 41_

Now update smoke_test.py:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "0771cdd0-ecff-4203-926c-da00531c4093",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpausRbkf58XmjivjcoVFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 46789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 356
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01U3LLvRPrVUqqASDMN9ySTn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
  "old_string": "\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-3 on 4xRTX 5090 (32GB).",
  "new_string": "\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-2 on 4xRTX 5090 (32GB)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "adcffd66-a78b-40b1-8c6d-db279deb1694",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpausRbkf58XmjivjcoVFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 46789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 356
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T06:10:06.025Z_

<details><summary>↩ Tool result · `toolu_01U3LLvRPrVUqqASDMN9ySTn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "e09ca4e1-20f9-44f0-87e8-49474d5a0034",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
    "oldString": "\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-3 on 4xRTX 5090 (32GB).",
    "newString": "\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-2 on 4xRTX 5090 (32GB).",
    "originalFile": "#!/usr/bin/env python3\n# Launch:\n#   accelerate launch --num_processes 4 --mixed_precision bf16 training/smoke_test.py\n#   deepspeed --num_gpus 4 training/smoke_test.py\n\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-3 on 4xRTX 5090 (32GB).\n\nUses synthetic data only. No freige imports. Runs 10 training steps and reports\nloss trend, peak VRAM, gradient norms, and PASS/FAIL.\n\"\"\"\n\nimport json\nimport math\nimport os\nimport random\nimport time\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nos.environ.setdefault(\"WANDB_DISABLED\", \"true\")\n\nSEED = 42\nNUM_STEPS = 10\nNUM_GENERATIONS = 4\nMAX_COMPLETION_LENGTH = 256\nMODEL_NAME = \"Qwen/Qwen3-4B\"\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\nDEEPSPEED_CONFIG = {\n    \"bf16\": {\"enabled\": True},\n    \"zero_optimization\": {\n        \"stage\": 3,\n        \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"offload_param\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"overlap_comm\": True,\n        \"contiguous_gradients\": True,\n        \"sub_group_size\": 1e9,\n        \"reduce_bucket_size\": \"auto\",\n        \"stage3_prefetch_bucket_size\": \"auto\",\n        \"stage3_param_persistence_threshold\": \"auto\",\n        \"stage3_max_live_parameters\": 1e9,\n        \"stage3_max_reuse_distance\": 1e9,\n        \"stage3_gather_16bit_weights_on_model_save\": True,\n    },\n    \"gradient_accumulation_steps\": \"auto\",\n    \"gradient_clipping\": \"auto\",\n    \"train_batch_size\": \"auto\",\n    \"train_micro_batch_size_per_gpu\": \"auto\",\n}\n\nDUMMY_DOCS = [\n    {\n        \"sents\": [\n            \"Albert Einstein was born in Ulm, Germany in 1879.\",\n            \"He developed the theory of relativity while working at the Swiss Patent Office.\",\n            \"Einstein later moved to the United States and joined Princeton University.\",\n            \"He received the Nobel Prize in Physics in 1921 for his work on the photoelectric effect.\",\n        ],\n        \"entities\": [\"Albert Einstein\", \"Ulm\", \"Germany\", \"United States\", \"Princeton University\"],\n        \"triples\": [\n            {\"head\": \"Albert Einstein\", \"relation\": \"place of birth\", \"tail\": \"Ulm\", \"evidence\": [0]},\n            {\"head\": \"Albert Einstein\", \"relation\": \"country of citizenship\", \"tail\": \"Germany\", \"evidence\": [0]},\n            {\"head\": \"Albert Einstein\", \"relation\": \"employer\", \"tail\": \"Princeton University\", \"evidence\": [2]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"The Eiffel Tower is a wrought-iron lattice tower in Paris, France.\",\n            \"It was designed by Gustave Eiffel's company and built between 1887 and 1889.\",\n            \"The tower is 330 metres tall and the tallest structure in Paris.\",\n            \"It has become a global cultural icon of France.\",\n        ],\n        \"entities\": [\"Eiffel Tower\", \"Paris\", \"France\", \"Gustave Eiffel\"],\n        \"triples\": [\n            {\"head\": \"Eiffel Tower\", \"relation\": \"located in\", \"tail\": \"Paris\", \"evidence\": [0]},\n            {\"head\": \"Eiffel Tower\", \"relation\": \"country\", \"tail\": \"France\", \"evidence\": [0, 3]},\n            {\"head\": \"Eiffel Tower\", \"relation\": \"creator\", \"tail\": \"Gustave Eiffel\", \"evidence\": [1]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Tokyo is the capital and most populous city of Japan.\",\n            \"The Greater Tokyo Area is the most populous metropolitan area in the world.\",\n            \"Tokyo was originally known as Edo and was renamed in 1868.\",\n            \"The city hosted the Summer Olympics in 1964 and 2021.\",\n        ],\n        \"entities\": [\"Tokyo\", \"Japan\", \"Edo\"],\n        \"triples\": [\n            {\"head\": \"Tokyo\", \"relation\": \"capital of\", \"tail\": \"Japan\", \"evidence\": [0]},\n            {\"head\": \"Tokyo\", \"relation\": \"country\", \"tail\": \"Japan\", \"evidence\": [0]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Marie Curie was a Polish-French physicist and chemist.\",\n            \"She conducted pioneering research on radioactivity at the University of Paris.\",\n            \"Curie was the first woman to win a Nobel Prize in 1903.\",\n            \"She won a second Nobel Prize in Chemistry in 1911.\",\n            \"Marie Curie was born in Warsaw, Poland.\",\n        ],\n        \"entities\": [\"Marie Curie\", \"University of Paris\", \"Warsaw\", \"Poland\"],\n        \"triples\": [\n            {\"head\": \"Marie Curie\", \"relation\": \"employer\", \"tail\": \"University of Paris\", \"evidence\": [1]},\n            {\"head\": \"Marie Curie\", \"relation\": \"place of birth\", \"tail\": \"Warsaw\", \"evidence\": [4]},\n            {\"head\": \"Marie Curie\", \"relation\": \"country of citizenship\", \"tail\": \"Poland\", \"evidence\": [0, 4]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Amazon was founded by Jeff Bezos in Bellevue, Washington on July 5, 1994.\",\n            \"The company started as an online bookstore.\",\n            \"Amazon's headquarters is located in Seattle, Washington.\",\n            \"It is one of the Big Five American technology companies.\",\n        ],\n        \"entities\": [\"Amazon\", \"Jeff Bezos\", \"Bellevue\", \"Seattle\", \"Washington\"],\n        \"triples\": [\n            {\"head\": \"Amazon\", \"relation\": \"founded by\", \"tail\": \"Jeff Bezos\", \"evidence\": [0]},\n            {\"head\": \"Amazon\", \"relation\": \"headquarters location\", \"tail\": \"Seattle\", \"evidence\": [2]},\n            {\"head\": \"Amazon\", \"relation\": \"location of formation\", \"tail\": \"Bellevue\", \"evidence\": [0]},\n        ],\n    },\n]\n\n\ndef generate_dummy_dataset(tokenizer, n_samples: int = 20, seed: int = SEED) -> Dataset:\n    rng = random.Random(seed)\n    items = []\n    for i in range(n_samples):\n        doc = DUMMY_DOCS[i % len(DUMMY_DOCS)]\n        numbered = \"\\n\".join(f\"[{j}] {s}\" for j, s in enumerate(doc[\"sents\"]))\n        entity_str = \", \".join(doc[\"entities\"])\n        user_msg = (\n            f\"Document:\\n{numbered}\\n\\n\"\n            f\"Entities: {entity_str}\\n\\n\"\n            \"Extract all relation triples with evidence sentence IDs.\"\n        )\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": user_msg},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,\n        )\n        gold = rng.sample(doc[\"triples\"], k=min(len(doc[\"triples\"]), rng.randint(1, 3)))\n        items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold, ensure_ascii=False),\n        })\n    return Dataset.from_list(items)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\nclass LossLogger:\n    def __init__(self):\n        self.losses = []\n        self.grad_norms = []\n\n\nloss_logger = LossLogger()\n_orig_log = None\n\n\ndef _patch_trainer_logging(trainer):\n    global _orig_log\n    _orig_log = trainer.log\n\n    def patched_log(logs, **kwargs):\n        if \"loss\" in logs:\n            loss_logger.losses.append(logs[\"loss\"])\n        if \"grad_norm\" in logs:\n            loss_logger.grad_norms.append(logs[\"grad_norm\"])\n        return _orig_log(logs, **kwargs)\n\n    trainer.log = patched_log\n\n\ndef main():\n    t0 = time.time()\n    local_rank = int(os.environ.get(\"LOCAL_RANK\", 0))\n\n    print(f\"[rank {local_rank}] Loading tokenizer: {MODEL_NAME}\")\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, padding_side=\"left\")\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"[rank {local_rank}] Generating dummy dataset...\")\n    dataset = generate_dummy_dataset(tokenizer, n_samples=20, seed=SEED)\n\n    print(f\"[rank {local_rank}] Loading model with 4-bit QLoRA...\")\n    bnb_config = BitsAndBytesConfig(\n        load_in_4bit=True,\n        bnb_4bit_compute_dtype=torch.bfloat16,\n        bnb_4bit_quant_type=\"nf4\",\n        bnb_4bit_use_double_quant=True,\n    )\n    model = AutoModelForCausalLM.from_pretrained(\n        MODEL_NAME,\n        quantization_config=bnb_config,\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=64,\n        lora_alpha=128,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    output_dir = \"/tmp/freige_smoke_test\"\n    grpo_config = GRPOConfig(\n        output_dir=output_dir,\n        max_steps=NUM_STEPS,\n        per_device_train_batch_size=1,\n        gradient_accumulation_steps=2,\n        learning_rate=5e-5,\n        bf16=True,\n        logging_steps=1,\n        save_strategy=\"no\",\n        seed=SEED,\n        num_generations=NUM_GENERATIONS,\n        max_completion_length=MAX_COMPLETION_LENGTH,\n        report_to=\"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=DEEPSPEED_CONFIG,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=dataset,\n        reward_funcs=[format_reward_fn],\n        peft_config=lora_config,\n        processing_class=tokenizer,\n    )\n    _patch_trainer_logging(trainer)\n\n    print(f\"[rank {local_rank}] Starting GRPO smoke test ({NUM_STEPS} steps)...\")\n    torch.cuda.reset_peak_memory_stats()\n    trainer.train()\n    elapsed = time.time() - t0\n\n    if local_rank == 0:\n        print(\"\\n\" + \"=\" * 60)\n        print(\"SMOKE TEST RESULTS\")\n        print(\"=\" * 60)\n\n        print(f\"\\n--- Loss per step ---\")\n        for i, loss in enumerate(loss_logger.losses):\n            print(f\"  step {i + 1}: {loss:.4f}\")\n\n        print(f\"\\n--- Gradient norms ---\")\n        for i, gn in enumerate(loss_logger.grad_norms):\n            print(f\"  step {i + 1}: {gn:.4f}\")\n\n        print(f\"\\n--- GPU peak memory ---\")\n        for i in range(torch.cuda.device_count()):\n            peak_mb = torch.cuda.max_memory_allocated(i) / 1024**2\n            print(f\"  GPU {i}: {peak_mb:.0f} MB ({peak_mb / 1024:.1f} GB)\")\n\n        print(f\"\\n--- Total time: {elapsed:.1f}s ---\")\n\n        has_nan_loss = any(math.isnan(l) for l in loss_logger.losses)\n        has_nan_grad = any(math.isnan(g) for g in loss_logger.grad_norms) if loss_logger.grad_norms else False\n        has_zero_grad = all(g == 0.0 for g in loss_logger.grad_norms) if loss_logger.grad_norms else True\n\n        if len(loss_logger.losses) >= 4:\n            last3_avg = sum(loss_logger.losses[-3:]) / 3\n            first_loss = loss_logger.losses[0]\n            loss_decreased = last3_avg < first_loss\n        else:\n            loss_decreased = True\n\n        passed = loss_decreased and not has_nan_loss and not has_nan_grad and not has_zero_grad\n\n        print(f\"\\n--- Diagnostics ---\")\n        print(f\"  Loss decreased (last 3 avg < first): {loss_decreased}\")\n        print(f\"  NaN in loss: {has_nan_loss}\")\n        print(f\"  NaN in grad_norm: {has_nan_grad}\")\n        print(f\"  All-zero grad_norm: {has_zero_grad}\")\n        print(f\"\\n{'PASS' if passed else 'FAIL'}\")\n        print(\"=\" * 60)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " # Launch:",
          " #   accelerate launch --num_processes 4 --mixed_precision bf16 training/smoke_test.py",
          " #   deepspeed --num_gpus 4 training/smoke_test.py",
          "-\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-3 on 4xRTX 5090 (32GB).",
          "+\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-2 on 4xRTX 5090 (32GB).",
          " ",
          " Uses synthetic data only. No freige imports. Runs 10 training steps and reports",
          " loss trend, peak VRAM, gradient norms, and PASS/FAIL."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01Mj5AxDdTqdjrueeJ43AdtT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
  "old_string": "MODEL_NAME = \"Qwen/Qwen3-4B\"",
  "new_string": "MODEL_NAME = \"/root/autodl-tmp/models/Qwen3-4B\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "4cf23c94-ef17-4db2-b0e4-5d8852dc94cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNARB9TsYZgqm8F4F3zwCp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 47145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 292
      },
      "output_tokens": 73,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T06:10:09.803Z_

<details><summary>↩ Tool result · `toolu_01Mj5AxDdTqdjrueeJ43AdtT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "a3f29b0d-1f28-4a99-bb54-2883e7ec2da4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
    "oldString": "MODEL_NAME = \"Qwen/Qwen3-4B\"",
    "newString": "MODEL_NAME = \"/root/autodl-tmp/models/Qwen3-4B\"",
    "originalFile": "#!/usr/bin/env python3\n# Launch:\n#   accelerate launch --num_processes 4 --mixed_precision bf16 training/smoke_test.py\n#   deepspeed --num_gpus 4 training/smoke_test.py\n\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-2 on 4xRTX 5090 (32GB).\n\nUses synthetic data only. No freige imports. Runs 10 training steps and reports\nloss trend, peak VRAM, gradient norms, and PASS/FAIL.\n\"\"\"\n\nimport json\nimport math\nimport os\nimport random\nimport time\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nos.environ.setdefault(\"WANDB_DISABLED\", \"true\")\n\nSEED = 42\nNUM_STEPS = 10\nNUM_GENERATIONS = 4\nMAX_COMPLETION_LENGTH = 256\nMODEL_NAME = \"Qwen/Qwen3-4B\"\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\nDEEPSPEED_CONFIG = {\n    \"bf16\": {\"enabled\": True},\n    \"zero_optimization\": {\n        \"stage\": 3,\n        \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"offload_param\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"overlap_comm\": True,\n        \"contiguous_gradients\": True,\n        \"sub_group_size\": 1e9,\n        \"reduce_bucket_size\": \"auto\",\n        \"stage3_prefetch_bucket_size\": \"auto\",\n        \"stage3_param_persistence_threshold\": \"auto\",\n        \"stage3_max_live_parameters\": 1e9,\n        \"stage3_max_reuse_distance\": 1e9,\n        \"stage3_gather_16bit_weights_on_model_save\": True,\n    },\n    \"gradient_accumulation_steps\": \"auto\",\n    \"gradient_clipping\": \"auto\",\n    \"train_batch_size\": \"auto\",\n    \"train_micro_batch_size_per_gpu\": \"auto\",\n}\n\nDUMMY_DOCS = [\n    {\n        \"sents\": [\n            \"Albert Einstein was born in Ulm, Germany in 1879.\",\n            \"He developed the theory of relativity while working at the Swiss Patent Office.\",\n            \"Einstein later moved to the United States and joined Princeton University.\",\n            \"He received the Nobel Prize in Physics in 1921 for his work on the photoelectric effect.\",\n        ],\n        \"entities\": [\"Albert Einstein\", \"Ulm\", \"Germany\", \"United States\", \"Princeton University\"],\n        \"triples\": [\n            {\"head\": \"Albert Einstein\", \"relation\": \"place of birth\", \"tail\": \"Ulm\", \"evidence\": [0]},\n            {\"head\": \"Albert Einstein\", \"relation\": \"country of citizenship\", \"tail\": \"Germany\", \"evidence\": [0]},\n            {\"head\": \"Albert Einstein\", \"relation\": \"employer\", \"tail\": \"Princeton University\", \"evidence\": [2]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"The Eiffel Tower is a wrought-iron lattice tower in Paris, France.\",\n            \"It was designed by Gustave Eiffel's company and built between 1887 and 1889.\",\n            \"The tower is 330 metres tall and the tallest structure in Paris.\",\n            \"It has become a global cultural icon of France.\",\n        ],\n        \"entities\": [\"Eiffel Tower\", \"Paris\", \"France\", \"Gustave Eiffel\"],\n        \"triples\": [\n            {\"head\": \"Eiffel Tower\", \"relation\": \"located in\", \"tail\": \"Paris\", \"evidence\": [0]},\n            {\"head\": \"Eiffel Tower\", \"relation\": \"country\", \"tail\": \"France\", \"evidence\": [0, 3]},\n            {\"head\": \"Eiffel Tower\", \"relation\": \"creator\", \"tail\": \"Gustave Eiffel\", \"evidence\": [1]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Tokyo is the capital and most populous city of Japan.\",\n            \"The Greater Tokyo Area is the most populous metropolitan area in the world.\",\n            \"Tokyo was originally known as Edo and was renamed in 1868.\",\n            \"The city hosted the Summer Olympics in 1964 and 2021.\",\n        ],\n        \"entities\": [\"Tokyo\", \"Japan\", \"Edo\"],\n        \"triples\": [\n            {\"head\": \"Tokyo\", \"relation\": \"capital of\", \"tail\": \"Japan\", \"evidence\": [0]},\n            {\"head\": \"Tokyo\", \"relation\": \"country\", \"tail\": \"Japan\", \"evidence\": [0]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Marie Curie was a Polish-French physicist and chemist.\",\n            \"She conducted pioneering research on radioactivity at the University of Paris.\",\n            \"Curie was the first woman to win a Nobel Prize in 1903.\",\n            \"She won a second Nobel Prize in Chemistry in 1911.\",\n            \"Marie Curie was born in Warsaw, Poland.\",\n        ],\n        \"entities\": [\"Marie Curie\", \"University of Paris\", \"Warsaw\", \"Poland\"],\n        \"triples\": [\n            {\"head\": \"Marie Curie\", \"relation\": \"employer\", \"tail\": \"University of Paris\", \"evidence\": [1]},\n            {\"head\": \"Marie Curie\", \"relation\": \"place of birth\", \"tail\": \"Warsaw\", \"evidence\": [4]},\n            {\"head\": \"Marie Curie\", \"relation\": \"country of citizenship\", \"tail\": \"Poland\", \"evidence\": [0, 4]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Amazon was founded by Jeff Bezos in Bellevue, Washington on July 5, 1994.\",\n            \"The company started as an online bookstore.\",\n            \"Amazon's headquarters is located in Seattle, Washington.\",\n            \"It is one of the Big Five American technology companies.\",\n        ],\n        \"entities\": [\"Amazon\", \"Jeff Bezos\", \"Bellevue\", \"Seattle\", \"Washington\"],\n        \"triples\": [\n            {\"head\": \"Amazon\", \"relation\": \"founded by\", \"tail\": \"Jeff Bezos\", \"evidence\": [0]},\n            {\"head\": \"Amazon\", \"relation\": \"headquarters location\", \"tail\": \"Seattle\", \"evidence\": [2]},\n            {\"head\": \"Amazon\", \"relation\": \"location of formation\", \"tail\": \"Bellevue\", \"evidence\": [0]},\n        ],\n    },\n]\n\n\ndef generate_dummy_dataset(tokenizer, n_samples: int = 20, seed: int = SEED) -> Dataset:\n    rng = random.Random(seed)\n    items = []\n    for i in range(n_samples):\n        doc = DUMMY_DOCS[i % len(DUMMY_DOCS)]\n        numbered = \"\\n\".join(f\"[{j}] {s}\" for j, s in enumerate(doc[\"sents\"]))\n        entity_str = \", \".join(doc[\"entities\"])\n        user_msg = (\n            f\"Document:\\n{numbered}\\n\\n\"\n            f\"Entities: {entity_str}\\n\\n\"\n            \"Extract all relation triples with evidence sentence IDs.\"\n        )\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": user_msg},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,\n        )\n        gold = rng.sample(doc[\"triples\"], k=min(len(doc[\"triples\"]), rng.randint(1, 3)))\n        items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold, ensure_ascii=False),\n        })\n    return Dataset.from_list(items)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\nclass LossLogger:\n    def __init__(self):\n        self.losses = []\n        self.grad_norms = []\n\n\nloss_logger = LossLogger()\n_orig_log = None\n\n\ndef _patch_trainer_logging(trainer):\n    global _orig_log\n    _orig_log = trainer.log\n\n    def patched_log(logs, **kwargs):\n        if \"loss\" in logs:\n            loss_logger.losses.append(logs[\"loss\"])\n        if \"grad_norm\" in logs:\n            loss_logger.grad_norms.append(logs[\"grad_norm\"])\n        return _orig_log(logs, **kwargs)\n\n    trainer.log = patched_log\n\n\ndef main():\n    t0 = time.time()\n    local_rank = int(os.environ.get(\"LOCAL_RANK\", 0))\n\n    print(f\"[rank {local_rank}] Loading tokenizer: {MODEL_NAME}\")\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, padding_side=\"left\")\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"[rank {local_rank}] Generating dummy dataset...\")\n    dataset = generate_dummy_dataset(tokenizer, n_samples=20, seed=SEED)\n\n    print(f\"[rank {local_rank}] Loading model with 4-bit QLoRA...\")\n    bnb_config = BitsAndBytesConfig(\n        load_in_4bit=True,\n        bnb_4bit_compute_dtype=torch.bfloat16,\n        bnb_4bit_quant_type=\"nf4\",\n        bnb_4bit_use_double_quant=True,\n    )\n    model = AutoModelForCausalLM.from_pretrained(\n        MODEL_NAME,\n        quantization_config=bnb_config,\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=64,\n        lora_alpha=128,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    output_dir = \"/tmp/freige_smoke_test\"\n    grpo_config = GRPOConfig(\n        output_dir=output_dir,\n        max_steps=NUM_STEPS,\n        per_device_train_batch_size=1,\n        gradient_accumulation_steps=2,\n        learning_rate=5e-5,\n        bf16=True,\n        logging_steps=1,\n        save_strategy=\"no\",\n        seed=SEED,\n        num_generations=NUM_GENERATIONS,\n        max_completion_length=MAX_COMPLETION_LENGTH,\n        report_to=\"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=DEEPSPEED_CONFIG,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=dataset,\n        reward_funcs=[format_reward_fn],\n        peft_config=lora_config,\n        processing_class=tokenizer,\n    )\n    _patch_trainer_logging(trainer)\n\n    print(f\"[rank {local_rank}] Starting GRPO smoke test ({NUM_STEPS} steps)...\")\n    torch.cuda.reset_peak_memory_stats()\n    trainer.train()\n    elapsed = time.time() - t0\n\n    if local_rank == 0:\n        print(\"\\n\" + \"=\" * 60)\n        print(\"SMOKE TEST RESULTS\")\n        print(\"=\" * 60)\n\n        print(f\"\\n--- Loss per step ---\")\n        for i, loss in enumerate(loss_logger.losses):\n            print(f\"  step {i + 1}: {loss:.4f}\")\n\n        print(f\"\\n--- Gradient norms ---\")\n        for i, gn in enumerate(loss_logger.grad_norms):\n            print(f\"  step {i + 1}: {gn:.4f}\")\n\n        print(f\"\\n--- GPU peak memory ---\")\n        for i in range(torch.cuda.device_count()):\n            peak_mb = torch.cuda.max_memory_allocated(i) / 1024**2\n            print(f\"  GPU {i}: {peak_mb:.0f} MB ({peak_mb / 1024:.1f} GB)\")\n\n        print(f\"\\n--- Total time: {elapsed:.1f}s ---\")\n\n        has_nan_loss = any(math.isnan(l) for l in loss_logger.losses)\n        has_nan_grad = any(math.isnan(g) for g in loss_logger.grad_norms) if loss_logger.grad_norms else False\n        has_zero_grad = all(g == 0.0 for g in loss_logger.grad_norms) if loss_logger.grad_norms else True\n\n        if len(loss_logger.losses) >= 4:\n            last3_avg = sum(loss_logger.losses[-3:]) / 3\n            first_loss = loss_logger.losses[0]\n            loss_decreased = last3_avg < first_loss\n        else:\n            loss_decreased = True\n\n        passed = loss_decreased and not has_nan_loss and not has_nan_grad and not has_zero_grad\n\n        print(f\"\\n--- Diagnostics ---\")\n        print(f\"  Loss decreased (last 3 avg < first): {loss_decreased}\")\n        print(f\"  NaN in loss: {has_nan_loss}\")\n        print(f\"  NaN in grad_norm: {has_nan_grad}\")\n        print(f\"  All-zero grad_norm: {has_zero_grad}\")\n        print(f\"\\n{'PASS' if passed else 'FAIL'}\")\n        print(\"=\" * 60)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 7,
        "newStart": 26,
        "newLines": 7,
        "lines": [
          " NUM_STEPS = 10",
          " NUM_GENERATIONS = 4",
          " MAX_COMPLETION_LENGTH = 256",
          "-MODEL_NAME = \"Qwen/Qwen3-4B\"",
          "+MODEL_NAME = \"/root/autodl-tmp/models/Qwen3-4B\"",
          " ",
          " SYSTEM_PROMPT = (",
          "     \"You are an information extraction model. Given a document with numbered sentences \""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_015r8E398DvmDUQQzn3yXzhm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
  "old_string": "DEEPSPEED_CONFIG = {\n    \"bf16\": {\"enabled\": True},\n    \"zero_optimization\": {\n        \"stage\": 3,\n        \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"offload_param\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"overlap_comm\": True,\n        \"contiguous_gradients\": True,\n        \"sub_group_size\": 1e9,\n        \"reduce_bucket_size\": \"auto\",\n        \"stage3_prefetch_bucket_size\": \"auto\",\n        \"stage3_param_persistence_threshold\": \"auto\",\n        \"stage3_max_live_parameters\": 1e9,\n        \"stage3_max_reuse_distance\": 1e9,\n        \"stage3_gather_16bit_weights_on_model_save\": True,\n    },\n    \"gradient_accumulation_steps\": \"auto\",\n    \"gradient_clipping\": \"auto\",\n    \"train_batch_size\": \"auto\",\n    \"train_micro_batch_size_per_gpu\": \"auto\",\n}",
  "new_string": "DEEPSPEED_CONFIG = {\n    \"bf16\": {\"enabled\": True},\n    \"zero_optimization\": {\n        \"stage\": 2,\n        \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"overlap_comm\": True,\n        \"contiguous_gradients\": True,\n        \"reduce_bucket_size\": \"auto\",\n        \"allgather_bucket_size\": 5e8,\n        \"allgather_partitions\": True,\n    },\n    \"gradient_accumulation_steps\": \"auto\",\n    \"gradient_clipping\": \"auto\",\n    \"train_batch_size\": \"auto\",\n    \"train_micro_batch_size_per_gpu\": \"auto\",\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "c1d28f4c-45a4-4d0b-82b8-9016d1057f78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFm523aYTL34xJHAnoMfXm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 47437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 244
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T06:10:17.443Z_

<details><summary>↩ Tool result · `toolu_015r8E398DvmDUQQzn3yXzhm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "0946a70a-32d6-4b9d-bd74-257147e0a8e1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
    "oldString": "DEEPSPEED_CONFIG = {\n    \"bf16\": {\"enabled\": True},\n    \"zero_optimization\": {\n        \"stage\": 3,\n        \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"offload_param\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"overlap_comm\": True,\n        \"contiguous_gradients\": True,\n        \"sub_group_size\": 1e9,\n        \"reduce_bucket_size\": \"auto\",\n        \"stage3_prefetch_bucket_size\": \"auto\",\n        \"stage3_param_persistence_threshold\": \"auto\",\n        \"stage3_max_live_parameters\": 1e9,\n        \"stage3_max_reuse_distance\": 1e9,\n        \"stage3_gather_16bit_weights_on_model_save\": True,\n    },\n    \"gradient_accumulation_steps\": \"auto\",\n    \"gradient_clipping\": \"auto\",\n    \"train_batch_size\": \"auto\",\n    \"train_micro_batch_size_per_gpu\": \"auto\",\n}",
    "newString": "DEEPSPEED_CONFIG = {\n    \"bf16\": {\"enabled\": True},\n    \"zero_optimization\": {\n        \"stage\": 2,\n        \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"overlap_comm\": True,\n        \"contiguous_gradients\": True,\n        \"reduce_bucket_size\": \"auto\",\n        \"allgather_bucket_size\": 5e8,\n        \"allgather_partitions\": True,\n    },\n    \"gradient_accumulation_steps\": \"auto\",\n    \"gradient_clipping\": \"auto\",\n    \"train_batch_size\": \"auto\",\n    \"train_micro_batch_size_per_gpu\": \"auto\",\n}",
    "originalFile": "#!/usr/bin/env python3\n# Launch:\n#   accelerate launch --num_processes 4 --mixed_precision bf16 training/smoke_test.py\n#   deepspeed --num_gpus 4 training/smoke_test.py\n\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-2 on 4xRTX 5090 (32GB).\n\nUses synthetic data only. No freige imports. Runs 10 training steps and reports\nloss trend, peak VRAM, gradient norms, and PASS/FAIL.\n\"\"\"\n\nimport json\nimport math\nimport os\nimport random\nimport time\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nos.environ.setdefault(\"WANDB_DISABLED\", \"true\")\n\nSEED = 42\nNUM_STEPS = 10\nNUM_GENERATIONS = 4\nMAX_COMPLETION_LENGTH = 256\nMODEL_NAME = \"/root/autodl-tmp/models/Qwen3-4B\"\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\nDEEPSPEED_CONFIG = {\n    \"bf16\": {\"enabled\": True},\n    \"zero_optimization\": {\n        \"stage\": 3,\n        \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"offload_param\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"overlap_comm\": True,\n        \"contiguous_gradients\": True,\n        \"sub_group_size\": 1e9,\n        \"reduce_bucket_size\": \"auto\",\n        \"stage3_prefetch_bucket_size\": \"auto\",\n        \"stage3_param_persistence_threshold\": \"auto\",\n        \"stage3_max_live_parameters\": 1e9,\n        \"stage3_max_reuse_distance\": 1e9,\n        \"stage3_gather_16bit_weights_on_model_save\": True,\n    },\n    \"gradient_accumulation_steps\": \"auto\",\n    \"gradient_clipping\": \"auto\",\n    \"train_batch_size\": \"auto\",\n    \"train_micro_batch_size_per_gpu\": \"auto\",\n}\n\nDUMMY_DOCS = [\n    {\n        \"sents\": [\n            \"Albert Einstein was born in Ulm, Germany in 1879.\",\n            \"He developed the theory of relativity while working at the Swiss Patent Office.\",\n            \"Einstein later moved to the United States and joined Princeton University.\",\n            \"He received the Nobel Prize in Physics in 1921 for his work on the photoelectric effect.\",\n        ],\n        \"entities\": [\"Albert Einstein\", \"Ulm\", \"Germany\", \"United States\", \"Princeton University\"],\n        \"triples\": [\n            {\"head\": \"Albert Einstein\", \"relation\": \"place of birth\", \"tail\": \"Ulm\", \"evidence\": [0]},\n            {\"head\": \"Albert Einstein\", \"relation\": \"country of citizenship\", \"tail\": \"Germany\", \"evidence\": [0]},\n            {\"head\": \"Albert Einstein\", \"relation\": \"employer\", \"tail\": \"Princeton University\", \"evidence\": [2]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"The Eiffel Tower is a wrought-iron lattice tower in Paris, France.\",\n            \"It was designed by Gustave Eiffel's company and built between 1887 and 1889.\",\n            \"The tower is 330 metres tall and the tallest structure in Paris.\",\n            \"It has become a global cultural icon of France.\",\n        ],\n        \"entities\": [\"Eiffel Tower\", \"Paris\", \"France\", \"Gustave Eiffel\"],\n        \"triples\": [\n            {\"head\": \"Eiffel Tower\", \"relation\": \"located in\", \"tail\": \"Paris\", \"evidence\": [0]},\n            {\"head\": \"Eiffel Tower\", \"relation\": \"country\", \"tail\": \"France\", \"evidence\": [0, 3]},\n            {\"head\": \"Eiffel Tower\", \"relation\": \"creator\", \"tail\": \"Gustave Eiffel\", \"evidence\": [1]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Tokyo is the capital and most populous city of Japan.\",\n            \"The Greater Tokyo Area is the most populous metropolitan area in the world.\",\n            \"Tokyo was originally known as Edo and was renamed in 1868.\",\n            \"The city hosted the Summer Olympics in 1964 and 2021.\",\n        ],\n        \"entities\": [\"Tokyo\", \"Japan\", \"Edo\"],\n        \"triples\": [\n            {\"head\": \"Tokyo\", \"relation\": \"capital of\", \"tail\": \"Japan\", \"evidence\": [0]},\n            {\"head\": \"Tokyo\", \"relation\": \"country\", \"tail\": \"Japan\", \"evidence\": [0]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Marie Curie was a Polish-French physicist and chemist.\",\n            \"She conducted pioneering research on radioactivity at the University of Paris.\",\n            \"Curie was the first woman to win a Nobel Prize in 1903.\",\n            \"She won a second Nobel Prize in Chemistry in 1911.\",\n            \"Marie Curie was born in Warsaw, Poland.\",\n        ],\n        \"entities\": [\"Marie Curie\", \"University of Paris\", \"Warsaw\", \"Poland\"],\n        \"triples\": [\n            {\"head\": \"Marie Curie\", \"relation\": \"employer\", \"tail\": \"University of Paris\", \"evidence\": [1]},\n            {\"head\": \"Marie Curie\", \"relation\": \"place of birth\", \"tail\": \"Warsaw\", \"evidence\": [4]},\n            {\"head\": \"Marie Curie\", \"relation\": \"country of citizenship\", \"tail\": \"Poland\", \"evidence\": [0, 4]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Amazon was founded by Jeff Bezos in Bellevue, Washington on July 5, 1994.\",\n            \"The company started as an online bookstore.\",\n            \"Amazon's headquarters is located in Seattle, Washington.\",\n            \"It is one of the Big Five American technology companies.\",\n        ],\n        \"entities\": [\"Amazon\", \"Jeff Bezos\", \"Bellevue\", \"Seattle\", \"Washington\"],\n        \"triples\": [\n            {\"head\": \"Amazon\", \"relation\": \"founded by\", \"tail\": \"Jeff Bezos\", \"evidence\": [0]},\n            {\"head\": \"Amazon\", \"relation\": \"headquarters location\", \"tail\": \"Seattle\", \"evidence\": [2]},\n            {\"head\": \"Amazon\", \"relation\": \"location of formation\", \"tail\": \"Bellevue\", \"evidence\": [0]},\n        ],\n    },\n]\n\n\ndef generate_dummy_dataset(tokenizer, n_samples: int = 20, seed: int = SEED) -> Dataset:\n    rng = random.Random(seed)\n    items = []\n    for i in range(n_samples):\n        doc = DUMMY_DOCS[i % len(DUMMY_DOCS)]\n        numbered = \"\\n\".join(f\"[{j}] {s}\" for j, s in enumerate(doc[\"sents\"]))\n        entity_str = \", \".join(doc[\"entities\"])\n        user_msg = (\n            f\"Document:\\n{numbered}\\n\\n\"\n            f\"Entities: {entity_str}\\n\\n\"\n            \"Extract all relation triples with evidence sentence IDs.\"\n        )\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": user_msg},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,\n        )\n        gold = rng.sample(doc[\"triples\"], k=min(len(doc[\"triples\"]), rng.randint(1, 3)))\n        items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold, ensure_ascii=False),\n        })\n    return Dataset.from_list(items)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\nclass LossLogger:\n    def __init__(self):\n        self.losses = []\n        self.grad_norms = []\n\n\nloss_logger = LossLogger()\n_orig_log = None\n\n\ndef _patch_trainer_logging(trainer):\n    global _orig_log\n    _orig_log = trainer.log\n\n    def patched_log(logs, **kwargs):\n        if \"loss\" in logs:\n            loss_logger.losses.append(logs[\"loss\"])\n        if \"grad_norm\" in logs:\n            loss_logger.grad_norms.append(logs[\"grad_norm\"])\n        return _orig_log(logs, **kwargs)\n\n    trainer.log = patched_log\n\n\ndef main():\n    t0 = time.time()\n    local_rank = int(os.environ.get(\"LOCAL_RANK\", 0))\n\n    print(f\"[rank {local_rank}] Loading tokenizer: {MODEL_NAME}\")\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, padding_side=\"left\")\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"[rank {local_rank}] Generating dummy dataset...\")\n    dataset = generate_dummy_dataset(tokenizer, n_samples=20, seed=SEED)\n\n    print(f\"[rank {local_rank}] Loading model with 4-bit QLoRA...\")\n    bnb_config = BitsAndBytesConfig(\n        load_in_4bit=True,\n        bnb_4bit_compute_dtype=torch.bfloat16,\n        bnb_4bit_quant_type=\"nf4\",\n        bnb_4bit_use_double_quant=True,\n    )\n    model = AutoModelForCausalLM.from_pretrained(\n        MODEL_NAME,\n        quantization_config=bnb_config,\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=64,\n        lora_alpha=128,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    output_dir = \"/tmp/freige_smoke_test\"\n    grpo_config = GRPOConfig(\n        output_dir=output_dir,\n        max_steps=NUM_STEPS,\n        per_device_train_batch_size=1,\n        gradient_accumulation_steps=2,\n        learning_rate=5e-5,\n        bf16=True,\n        logging_steps=1,\n        save_strategy=\"no\",\n        seed=SEED,\n        num_generations=NUM_GENERATIONS,\n        max_completion_length=MAX_COMPLETION_LENGTH,\n        report_to=\"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=DEEPSPEED_CONFIG,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=dataset,\n        reward_funcs=[format_reward_fn],\n        peft_config=lora_config,\n        processing_class=tokenizer,\n    )\n    _patch_trainer_logging(trainer)\n\n    print(f\"[rank {local_rank}] Starting GRPO smoke test ({NUM_STEPS} steps)...\")\n    torch.cuda.reset_peak_memory_stats()\n    trainer.train()\n    elapsed = time.time() - t0\n\n    if local_rank == 0:\n        print(\"\\n\" + \"=\" * 60)\n        print(\"SMOKE TEST RESULTS\")\n        print(\"=\" * 60)\n\n        print(f\"\\n--- Loss per step ---\")\n        for i, loss in enumerate(loss_logger.losses):\n            print(f\"  step {i + 1}: {loss:.4f}\")\n\n        print(f\"\\n--- Gradient norms ---\")\n        for i, gn in enumerate(loss_logger.grad_norms):\n            print(f\"  step {i + 1}: {gn:.4f}\")\n\n        print(f\"\\n--- GPU peak memory ---\")\n        for i in range(torch.cuda.device_count()):\n            peak_mb = torch.cuda.max_memory_allocated(i) / 1024**2\n            print(f\"  GPU {i}: {peak_mb:.0f} MB ({peak_mb / 1024:.1f} GB)\")\n\n        print(f\"\\n--- Total time: {elapsed:.1f}s ---\")\n\n        has_nan_loss = any(math.isnan(l) for l in loss_logger.losses)\n        has_nan_grad = any(math.isnan(g) for g in loss_logger.grad_norms) if loss_logger.grad_norms else False\n        has_zero_grad = all(g == 0.0 for g in loss_logger.grad_norms) if loss_logger.grad_norms else True\n\n        if len(loss_logger.losses) >= 4:\n            last3_avg = sum(loss_logger.losses[-3:]) / 3\n            first_loss = loss_logger.losses[0]\n            loss_decreased = last3_avg < first_loss\n        else:\n            loss_decreased = True\n\n        passed = loss_decreased and not has_nan_loss and not has_nan_grad and not has_zero_grad\n\n        print(f\"\\n--- Diagnostics ---\")\n        print(f\"  Loss decreased (last 3 avg < first): {loss_decreased}\")\n        print(f\"  NaN in loss: {has_nan_loss}\")\n        print(f\"  NaN in grad_norm: {has_nan_grad}\")\n        print(f\"  All-zero grad_norm: {has_zero_grad}\")\n        print(f\"\\n{'PASS' if passed else 'FAIL'}\")\n        print(\"=\" * 60)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 38,
        "oldLines": 18,
        "newStart": 38,
        "newLines": 13,
        "lines": [
          " DEEPSPEED_CONFIG = {",
          "     \"bf16\": {\"enabled\": True},",
          "     \"zero_optimization\": {",
          "-        \"stage\": 3,",
          "+        \"stage\": 2,",
          "         \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},",
          "-        \"offload_param\": {\"device\": \"cpu\", \"pin_memory\": True},",
          "         \"overlap_comm\": True,",
          "         \"contiguous_gradients\": True,",
          "-        \"sub_group_size\": 1e9,",
          "         \"reduce_bucket_size\": \"auto\",",
          "-        \"stage3_prefetch_bucket_size\": \"auto\",",
          "-        \"stage3_param_persistence_threshold\": \"auto\",",
          "-        \"stage3_max_live_parameters\": 1e9,",
          "-        \"stage3_max_reuse_distance\": 1e9,",
          "-        \"stage3_gather_16bit_weights_on_model_save\": True,",
          "+        \"allgather_bucket_size\": 5e8,",
          "+        \"allgather_partitions\": True,",
          "     },",
          "     \"gradient_accumulation_steps\": \"auto\",",
          "     \"gradient_clipping\": \"auto\","
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01RXgm4Ed4DAra35fryKRkMJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
  "old_string": "        attn_implementation=\"flash_attention_2\",",
  "new_string": "        attn_implementation=\"sdpa\","
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "4a28a5eb-102e-4159-991e-2d163f2f8ac5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgXdDJdU4Cz5RFf4eWgu2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 47681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T06:10:21.121Z_

<details><summary>↩ Tool result · `toolu_01RXgm4Ed4DAra35fryKRkMJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "739690c6-5717-46a4-8ad5-1970cad7bdbd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
    "oldString": "        attn_implementation=\"flash_attention_2\",",
    "newString": "        attn_implementation=\"sdpa\",",
    "originalFile": "#!/usr/bin/env python3\n# Launch:\n#   accelerate launch --num_processes 4 --mixed_precision bf16 training/smoke_test.py\n#   deepspeed --num_gpus 4 training/smoke_test.py\n\"\"\"Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-2 on 4xRTX 5090 (32GB).\n\nUses synthetic data only. No freige imports. Runs 10 training steps and reports\nloss trend, peak VRAM, gradient norms, and PASS/FAIL.\n\"\"\"\n\nimport json\nimport math\nimport os\nimport random\nimport time\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nos.environ.setdefault(\"WANDB_DISABLED\", \"true\")\n\nSEED = 42\nNUM_STEPS = 10\nNUM_GENERATIONS = 4\nMAX_COMPLETION_LENGTH = 256\nMODEL_NAME = \"/root/autodl-tmp/models/Qwen3-4B\"\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\nDEEPSPEED_CONFIG = {\n    \"bf16\": {\"enabled\": True},\n    \"zero_optimization\": {\n        \"stage\": 2,\n        \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"overlap_comm\": True,\n        \"contiguous_gradients\": True,\n        \"reduce_bucket_size\": \"auto\",\n        \"allgather_bucket_size\": 5e8,\n        \"allgather_partitions\": True,\n    },\n    \"gradient_accumulation_steps\": \"auto\",\n    \"gradient_clipping\": \"auto\",\n    \"train_batch_size\": \"auto\",\n    \"train_micro_batch_size_per_gpu\": \"auto\",\n}\n\nDUMMY_DOCS = [\n    {\n        \"sents\": [\n            \"Albert Einstein was born in Ulm, Germany in 1879.\",\n            \"He developed the theory of relativity while working at the Swiss Patent Office.\",\n            \"Einstein later moved to the United States and joined Princeton University.\",\n            \"He received the Nobel Prize in Physics in 1921 for his work on the photoelectric effect.\",\n        ],\n        \"entities\": [\"Albert Einstein\", \"Ulm\", \"Germany\", \"United States\", \"Princeton University\"],\n        \"triples\": [\n            {\"head\": \"Albert Einstein\", \"relation\": \"place of birth\", \"tail\": \"Ulm\", \"evidence\": [0]},\n            {\"head\": \"Albert Einstein\", \"relation\": \"country of citizenship\", \"tail\": \"Germany\", \"evidence\": [0]},\n            {\"head\": \"Albert Einstein\", \"relation\": \"employer\", \"tail\": \"Princeton University\", \"evidence\": [2]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"The Eiffel Tower is a wrought-iron lattice tower in Paris, France.\",\n            \"It was designed by Gustave Eiffel's company and built between 1887 and 1889.\",\n            \"The tower is 330 metres tall and the tallest structure in Paris.\",\n            \"It has become a global cultural icon of France.\",\n        ],\n        \"entities\": [\"Eiffel Tower\", \"Paris\", \"France\", \"Gustave Eiffel\"],\n        \"triples\": [\n            {\"head\": \"Eiffel Tower\", \"relation\": \"located in\", \"tail\": \"Paris\", \"evidence\": [0]},\n            {\"head\": \"Eiffel Tower\", \"relation\": \"country\", \"tail\": \"France\", \"evidence\": [0, 3]},\n            {\"head\": \"Eiffel Tower\", \"relation\": \"creator\", \"tail\": \"Gustave Eiffel\", \"evidence\": [1]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Tokyo is the capital and most populous city of Japan.\",\n            \"The Greater Tokyo Area is the most populous metropolitan area in the world.\",\n            \"Tokyo was originally known as Edo and was renamed in 1868.\",\n            \"The city hosted the Summer Olympics in 1964 and 2021.\",\n        ],\n        \"entities\": [\"Tokyo\", \"Japan\", \"Edo\"],\n        \"triples\": [\n            {\"head\": \"Tokyo\", \"relation\": \"capital of\", \"tail\": \"Japan\", \"evidence\": [0]},\n            {\"head\": \"Tokyo\", \"relation\": \"country\", \"tail\": \"Japan\", \"evidence\": [0]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Marie Curie was a Polish-French physicist and chemist.\",\n            \"She conducted pioneering research on radioactivity at the University of Paris.\",\n            \"Curie was the first woman to win a Nobel Prize in 1903.\",\n            \"She won a second Nobel Prize in Chemistry in 1911.\",\n            \"Marie Curie was born in Warsaw, Poland.\",\n        ],\n        \"entities\": [\"Marie Curie\", \"University of Paris\", \"Warsaw\", \"Poland\"],\n        \"triples\": [\n            {\"head\": \"Marie Curie\", \"relation\": \"employer\", \"tail\": \"University of Paris\", \"evidence\": [1]},\n            {\"head\": \"Marie Curie\", \"relation\": \"place of birth\", \"tail\": \"Warsaw\", \"evidence\": [4]},\n            {\"head\": \"Marie Curie\", \"relation\": \"country of citizenship\", \"tail\": \"Poland\", \"evidence\": [0, 4]},\n        ],\n    },\n    {\n        \"sents\": [\n            \"Amazon was founded by Jeff Bezos in Bellevue, Washington on July 5, 1994.\",\n            \"The company started as an online bookstore.\",\n            \"Amazon's headquarters is located in Seattle, Washington.\",\n            \"It is one of the Big Five American technology companies.\",\n        ],\n        \"entities\": [\"Amazon\", \"Jeff Bezos\", \"Bellevue\", \"Seattle\", \"Washington\"],\n        \"triples\": [\n            {\"head\": \"Amazon\", \"relation\": \"founded by\", \"tail\": \"Jeff Bezos\", \"evidence\": [0]},\n            {\"head\": \"Amazon\", \"relation\": \"headquarters location\", \"tail\": \"Seattle\", \"evidence\": [2]},\n            {\"head\": \"Amazon\", \"relation\": \"location of formation\", \"tail\": \"Bellevue\", \"evidence\": [0]},\n        ],\n    },\n]\n\n\ndef generate_dummy_dataset(tokenizer, n_samples: int = 20, seed: int = SEED) -> Dataset:\n    rng = random.Random(seed)\n    items = []\n    for i in range(n_samples):\n        doc = DUMMY_DOCS[i % len(DUMMY_DOCS)]\n        numbered = \"\\n\".join(f\"[{j}] {s}\" for j, s in enumerate(doc[\"sents\"]))\n        entity_str = \", \".join(doc[\"entities\"])\n        user_msg = (\n            f\"Document:\\n{numbered}\\n\\n\"\n            f\"Entities: {entity_str}\\n\\n\"\n            \"Extract all relation triples with evidence sentence IDs.\"\n        )\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": user_msg},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,\n        )\n        gold = rng.sample(doc[\"triples\"], k=min(len(doc[\"triples\"]), rng.randint(1, 3)))\n        items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold, ensure_ascii=False),\n        })\n    return Dataset.from_list(items)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\nclass LossLogger:\n    def __init__(self):\n        self.losses = []\n        self.grad_norms = []\n\n\nloss_logger = LossLogger()\n_orig_log = None\n\n\ndef _patch_trainer_logging(trainer):\n    global _orig_log\n    _orig_log = trainer.log\n\n    def patched_log(logs, **kwargs):\n        if \"loss\" in logs:\n            loss_logger.losses.append(logs[\"loss\"])\n        if \"grad_norm\" in logs:\n            loss_logger.grad_norms.append(logs[\"grad_norm\"])\n        return _orig_log(logs, **kwargs)\n\n    trainer.log = patched_log\n\n\ndef main():\n    t0 = time.time()\n    local_rank = int(os.environ.get(\"LOCAL_RANK\", 0))\n\n    print(f\"[rank {local_rank}] Loading tokenizer: {MODEL_NAME}\")\n    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, padding_side=\"left\")\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"[rank {local_rank}] Generating dummy dataset...\")\n    dataset = generate_dummy_dataset(tokenizer, n_samples=20, seed=SEED)\n\n    print(f\"[rank {local_rank}] Loading model with 4-bit QLoRA...\")\n    bnb_config = BitsAndBytesConfig(\n        load_in_4bit=True,\n        bnb_4bit_compute_dtype=torch.bfloat16,\n        bnb_4bit_quant_type=\"nf4\",\n        bnb_4bit_use_double_quant=True,\n    )\n    model = AutoModelForCausalLM.from_pretrained(\n        MODEL_NAME,\n        quantization_config=bnb_config,\n        trust_remote_code=True,\n        attn_implementation=\"flash_attention_2\",\n    )\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=64,\n        lora_alpha=128,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\", \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    output_dir = \"/tmp/freige_smoke_test\"\n    grpo_config = GRPOConfig(\n        output_dir=output_dir,\n        max_steps=NUM_STEPS,\n        per_device_train_batch_size=1,\n        gradient_accumulation_steps=2,\n        learning_rate=5e-5,\n        bf16=True,\n        logging_steps=1,\n        save_strategy=\"no\",\n        seed=SEED,\n        num_generations=NUM_GENERATIONS,\n        max_completion_length=MAX_COMPLETION_LENGTH,\n        report_to=\"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=DEEPSPEED_CONFIG,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=dataset,\n        reward_funcs=[format_reward_fn],\n        peft_config=lora_config,\n        processing_class=tokenizer,\n    )\n    _patch_trainer_logging(trainer)\n\n    print(f\"[rank {local_rank}] Starting GRPO smoke test ({NUM_STEPS} steps)...\")\n    torch.cuda.reset_peak_memory_stats()\n    trainer.train()\n    elapsed = time.time() - t0\n\n    if local_rank == 0:\n        print(\"\\n\" + \"=\" * 60)\n        print(\"SMOKE TEST RESULTS\")\n        print(\"=\" * 60)\n\n        print(f\"\\n--- Loss per step ---\")\n        for i, loss in enumerate(loss_logger.losses):\n            print(f\"  step {i + 1}: {loss:.4f}\")\n\n        print(f\"\\n--- Gradient norms ---\")\n        for i, gn in enumerate(loss_logger.grad_norms):\n            print(f\"  step {i + 1}: {gn:.4f}\")\n\n        print(f\"\\n--- GPU peak memory ---\")\n        for i in range(torch.cuda.device_count()):\n            peak_mb = torch.cuda.max_memory_allocated(i) / 1024**2\n            print(f\"  GPU {i}: {peak_mb:.0f} MB ({peak_mb / 1024:.1f} GB)\")\n\n        print(f\"\\n--- Total time: {elapsed:.1f}s ---\")\n\n        has_nan_loss = any(math.isnan(l) for l in loss_logger.losses)\n        has_nan_grad = any(math.isnan(g) for g in loss_logger.grad_norms) if loss_logger.grad_norms else False\n        has_zero_grad = all(g == 0.0 for g in loss_logger.grad_norms) if loss_logger.grad_norms else True\n\n        if len(loss_logger.losses) >= 4:\n            last3_avg = sum(loss_logger.losses[-3:]) / 3\n            first_loss = loss_logger.losses[0]\n            loss_decreased = last3_avg < first_loss\n        else:\n            loss_decreased = True\n\n        passed = loss_decreased and not has_nan_loss and not has_nan_grad and not has_zero_grad\n\n        print(f\"\\n--- Diagnostics ---\")\n        print(f\"  Loss decreased (last 3 avg < first): {loss_decreased}\")\n        print(f\"  NaN in loss: {has_nan_loss}\")\n        print(f\"  NaN in grad_norm: {has_nan_grad}\")\n        print(f\"  All-zero grad_norm: {has_zero_grad}\")\n        print(f\"\\n{'PASS' if passed else 'FAIL'}\")\n        print(\"=\" * 60)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 235,
        "oldLines": 7,
        "newStart": 235,
        "newLines": 7,
        "lines": [
          "         MODEL_NAME,",
          "         quantization_config=bnb_config,",
          "         trust_remote_code=True,",
          "-        attn_implementation=\"flash_attention_2\",",
          "+        attn_implementation=\"sdpa\",",
          "     )",
          " ",
          "     lora_config = LoraConfig("
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 50_

Let me verify the final state of grpo_trainer.py to make sure the tau scheduling logic is coherent:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "65b467a8-1ee9-4ca4-b184-7aa8f6354498",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmvKj9ArvbDiTn7YNU3Pwb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 48328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 226
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_011tRjKQMm3MzSNwSbrCGLuZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "offset": 123,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "23ce498a-cefa-492c-b316-4eb25210ff51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmvKj9ArvbDiTn7YNU3Pwb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 48328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 226
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T06:10:25.732Z_

<details><summary>↩ Tool result · `toolu_011tRjKQMm3MzSNwSbrCGLuZ`</summary>

```text
123	
124	class CEDRewardWrapper:
125	    """将 CED 奖励封装为 GRPO 兼容的 reward function。
126	
127	    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，
128	    返回所有 triples 的平均 CED reward。
129	    """
130	
131	    def __init__(
132	        self,
133	        nli_model: str = "cross-encoder/nli-deberta-v3-base",
134	        tau: float = 0.5,
135	        mode: str = "ced",
136	        device: str = None,
137	        tau_start: float = None,
138	        tau_end: float = None,
139	        total_steps: int = None,
140	    ):
141	        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple
142	        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)
143	        self.verbalize = verbalize_triple
144	        self.mode = mode
145	        self._call_count = 0
146	        if tau_start is not None and tau_end is not None:
147	            self.tau_start = tau_start
148	            self.tau_end = tau_end
149	            self.total_steps = total_steps
150	        else:
151	            self.tau_start = tau
152	            self.tau_end = tau
153	            self.total_steps = None
154	
155	    @property
156	    def tau(self) -> float:
157	        if self.total_steps and self.total_steps > 0:
158	            progress = min(self._call_count / self.total_steps, 1.0)
159	        else:
160	            progress = min(self._call_count / max(self._call_count, 1), 1.0)
161	        return self.tau_start + (self.tau_end - self.tau_start) * progress
162	
163	    def __call__(
164	        self,
165	        completions: list[str],
166	        all_sents: list[str],
167	        gold_triples: list[str],
168	        **kwargs,
169	    ) -> list[float]:
170	        """计算 CED/flat-NLI 奖励。
171	
172	        all_sents: JSON 字符串列表，每个元素为文档句子列表。
173	        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。
174	        """
175	        current_tau = self.tau
176	        self._call_count += 1
177	        num_gen = len(completions) // len(all_sents)
178	        rewards = []
179	
180	        for i, text in enumerate(completions):
181	            prompt_idx = i // num_gen
182	            try:
183	                sents = json.loads(all_sents[prompt_idx])
184	                gold = json.loads(gold_triples[prompt_idx])
185	            except (json.JSONDecodeError, IndexError):
186	                rewards.append(0.0)
187	                continue
188	
189	            pred = _parse_json_output(text)
190	            if not pred:
191	                rewards.append(0.0)
192	                continue
193	
194	            gold_map = {}
195	            for g in gold:
196	                key = (
197	                    g.get("head", "").lower().strip(),
198	                    g.get("relation", "").lower().strip(),
199	                    g.get("tail", "").lower().strip(),
200	                )
201	                gold_map[key] = g
202	
203	            triple_rewards = []
204	            for p in pred:
205	                if not isinstance(p, dict):
206	                    continue
207	                pred_evi_ids = p.get("evidence", [])
208	                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:
209	                    triple_rewards.append(0.0)
210	                    continue
211	
212	                claim = self.verbalize(
213	                    p.get("head", ""),
214	                    p.get("relation", ""),
215	                    p.get("tail", ""),
216	                )
217	                cited_sents = [sents[idx] for idx in pred_evi_ids
218	                               if isinstance(idx, int) and 0 <= idx < len(sents)]
219	                if not cited_sents:
220	                    triple_rewards.append(0.0)
221	                    continue
222	
223	                key = (
224	                    p.get("head", "").lower().strip(),
225	                    p.get("relation", "").lower().strip(),
226	                    p.get("tail", "").lower().strip(),
227	                )
228	                matched_gold = gold_map.get(key, {})
229	                hard_neg_ids = matched_gold.get("hard_negative_sent_ids", [])
230	                hard_neg_sents = [sents[idx] for idx in hard_neg_ids
231	                                  if isinstance(idx, int) and 0 <= idx < len(sents)]
232	
233	                if self.mode == "flat_nli":
234	                    result = self.reward_model.compute_flat_nli_reward(
235	                        claim, cited_sents, tau=current_tau,
236	                    )
237	                else:
238	                    result = self.reward_model.compute_ced_reward(
239	                        claim, cited_sents, hard_neg_sents, tau=current_tau,
240	                    )
241	                triple_rewards.append(result["reward"])
242	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "ba7c4e18-7161-4783-89ea-107a795ca46b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
      "content": "\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n        tau_start: float = None,\n        tau_end: float = None,\n        total_steps: int = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.mode = mode\n        self._call_count = 0\n        if tau_start is not None and tau_end is not None:\n            self.tau_start = tau_start\n            self.tau_end = tau_end\n            self.total_steps = total_steps\n        else:\n            self.tau_start = tau\n            self.tau_end = tau\n            self.total_steps = None\n\n    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = min(self._call_count / max(self._call_count, 1), 1.0)\n        return self.tau_start + (self.tau_end - self.tau_start) * progress\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        current_tau = self.tau\n        self._call_count += 1\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=current_tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=current_tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n",
      "numLines": 120,
      "startLine": 123,
      "totalLines": 443
    }
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

````text
The tau scheduling logic has a subtle issue. When `total_steps` is None (which happens when tau_start == tau_end from the fallback), the progress calculation at line 160 is:

```python
progress = min(self._call_count / max(self._call_count, 1), 1.0)
```

When `_call_count == 0`: `progress = 0 / max(0, 1) = 0/1 = 0`, so `tau = tau_start + 0 = tau_start` ✓


When `_call_count > 0`: `progress = _call_count / _call_count = 1.0`, so `tau = tau_start + (tau_end - tau_start) * 1.0 = tau_end`, which is fine when they're equal in the fallback case.

But the real problem is when `tau_start != tau_end` with the new CLI args—`total_steps` will be `None` since we're not passing it from `main()`, so I need to trace through what actually happens in that scenario.

When we instantiate the wrapper with `tau_start=0.3` and `tau_end=0.5`, we skip the `total_steps` initialization and it stays `None`. Then in the `tau` property, the condition `if self.total_steps and self.total_steps > 0` evaluates to `False`, so we fall into the else branch where progress is calculated as `min(_call_count / max(_call_count, 1), 1.0)`. This means when `_call_count == 0`, progress starts at 0.

3, but then jumps to 0.5 on the very next call when `_call_count == 1` and progress becomes 1.0 — completely defeating the gradual scheduling. I need to fix this by either computing `total_steps` from the training config or adding a parameter to estimate the total number of reward calls, but the task asks to keep it simple.

Looking back at the requirements, the approach is to use an internal counter since TRL doesn't easily expose step information through kwargs. The challenge is that without knowing the total number of steps upfront, I can't implement proper linear interpolation. I could compute `total_steps` from the dataset size, batch size, gradient accumulation, and number of epochs, but determining the number of GPUs adds complexity. Another option is to add a `--total_steps` argument to the CLI or compute it from the trainer after initialization. I need to figure out how to pass the total training steps to the reward wrapper so it can compute the tau interpolation schedule. The cleanest approach is to calculate total_steps in main after preparing the dataset—since I won't know the exact dataset size until then—and pass it directly to CEDRewardWrapper. The reward function gets called once per optimizer step, so this count should align with how many times the interpolation needs to happen. Calculating step counts...

The multi-GPU case will naturally reduce the actual steps needed, so this estimate serves as a safe upper bound for the tau schedule—finishing the ramp early is acceptable since we're being conservative.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "83bc7d45-101b-435b-8514-2fc50507557f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fz8WD4w2tP9kgTJUmdnveR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 48554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 54_

The tau scheduling has a bug — when `total_steps` is None, progress jumps to 1.0 immediately after the first call. Let me fix this by computing total_steps in `main()` and passing it through.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "5f20c32e-c0ca-4de6-92b9-bc7465a017aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fz8WD4w2tP9kgTJUmdnveR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 48554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01Hu6reaacsDdjVzAfqgFU37`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "offset": 280,
  "limit": 140
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "b8e643e6-ac52-4293-8549-f15b0307355a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fz8WD4w2tP9kgTJUmdnveR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 48554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T06:11:08.074Z_

<details><summary>↩ Tool result · `toolu_01Hu6reaacsDdjVzAfqgFU37`</summary>

```text
280	        for s in doc_samples:
281	            gold_triples.append({
282	                "head": s.head.name,
283	                "relation": s.relation_name,
284	                "tail": s.tail.name,
285	                "evidence": s.evidence_sent_ids,
286	                "hard_negative_sent_ids": s.hard_negative_sent_ids,
287	            })
288	
289	        ref = doc_samples[0]
290	        dataset_items.append({
291	            "prompt": prompt,
292	            "gold_triples": json.dumps(gold_triples, ensure_ascii=False),
293	            "all_sents": json.dumps(ref.sents, ensure_ascii=False),
294	        })
295	
296	    logger.info("Prepared %d GRPO prompts", len(dataset_items))
297	    return Dataset.from_list(dataset_items)
298	
299	
300	def main():
301	    parser = argparse.ArgumentParser(description="FREIGE GRPO Training")
302	    parser.add_argument("--model_name", type=str, default="/root/autodl-tmp/models/Qwen3-4B",
303	                        help="基础模型或 SFT checkpoint 路径")
304	    parser.add_argument("--sft_adapter", type=str, default=None,
305	                        help="SFT LoRA adapter 路径（如果与 model_name 不同）")
306	    parser.add_argument("--data_dir", type=str, default=None)
307	    parser.add_argument("--output_dir", type=str, default="./grpo_output")
308	    parser.add_argument("--stage", type=int, default=1, choices=[1, 2, 3],
309	                        help="Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED")
310	    parser.add_argument("--nli_model", type=str, default="cross-encoder/nli-deberta-v3-base")
311	    parser.add_argument("--num_generations", type=int, default=4)
312	    parser.add_argument("--lora_rank", type=int, default=64)
313	    parser.add_argument("--lora_alpha", type=int, default=128)
314	    parser.add_argument("--max_length", type=int, default=4096)
315	    parser.add_argument("--max_new_tokens", type=int, default=1024)
316	    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction, default=True,
317	                        help="启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）")
318	    parser.add_argument("--deepspeed", type=str, default=None,
319	                        help="DeepSpeed 配置文件路径")
320	    parser.add_argument("--reward_device", type=str, default="cpu",
321	                        help="CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）")
322	    parser.add_argument("--per_device_batch_size", type=int, default=1)
323	    parser.add_argument("--gradient_accumulation_steps", type=int, default=16)
324	    parser.add_argument("--num_epochs", type=int, default=1)
325	    parser.add_argument("--learning_rate", type=float, default=5e-5)
326	    parser.add_argument("--tau_start", type=float, default=0.3,
327	                        help="CED tau 初始值")
328	    parser.add_argument("--tau_end", type=float, default=0.5,
329	                        help="CED tau 最终值（线性调度）")
330	    parser.add_argument("--bf16", action="store_true", default=True)
331	    parser.add_argument("--seed", type=int, default=42)
332	    parser.add_argument("--wandb_project", type=str, default="freige-grpo")
333	    parser.add_argument("--wandb_run_name", type=str, default=None)
334	    args = parser.parse_args()
335	
336	    if args.wandb_project and "WANDB_API_KEY" in os.environ:
337	        os.environ["WANDB_PROJECT"] = args.wandb_project
338	        if args.wandb_run_name:
339	            os.environ["WANDB_NAME"] = args.wandb_run_name
340	
341	    logger.info("Loading tokenizer: %s", args.model_name)
342	    tokenizer = AutoTokenizer.from_pretrained(
343	        args.model_name,
344	        trust_remote_code=True,
345	        padding_side="left",
346	    )
347	    if tokenizer.pad_token is None:
348	        tokenizer.pad_token = tokenizer.eos_token
349	
350	    logger.info("Preparing dataset...")
351	    train_dataset = prepare_grpo_dataset(
352	        data_dir=args.data_dir,
353	        split="train",
354	        tokenizer=tokenizer,
355	    )
356	
357	    logger.info("Loading model: %s", args.model_name)
358	    model_kwargs = dict(
359	        trust_remote_code=True,
360	        attn_implementation="sdpa",
361	    )
362	    if args.quantize:
363	        logger.info("Using 4-bit QLoRA quantization")
364	        model_kwargs["quantization_config"] = BitsAndBytesConfig(
365	            load_in_4bit=True,
366	            bnb_4bit_compute_dtype=torch.bfloat16,
367	            bnb_4bit_quant_type="nf4",
368	            bnb_4bit_use_double_quant=True,
369	        )
370	    else:
371	        model_kwargs["torch_dtype"] = torch.bfloat16 if args.bf16 else torch.float16
372	    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)
373	
374	    if args.sft_adapter:
375	        logger.info("Loading SFT adapter from %s", args.sft_adapter)
376	        model = PeftModel.from_pretrained(model, args.sft_adapter)
377	        model = model.merge_and_unload()
378	
379	    reward_fns = [format_reward_fn, f1_reward_fn]
380	
381	    if args.stage >= 2:
382	        mode = "flat_nli" if args.stage == 2 else "ced"
383	        ced_wrapper = CEDRewardWrapper(
384	            nli_model=args.nli_model,
385	            mode=mode,
386	            device=args.reward_device,
387	            tau_start=args.tau_start,
388	            tau_end=args.tau_end,
389	        )
390	        reward_fns.append(ced_wrapper)
391	        logger.info("Stage %d: using %s reward", args.stage, mode)
392	    else:
393	        logger.info("Stage 1: extraction-only (format + F1 rewards)")
394	
395	    lora_config = LoraConfig(
396	        task_type=TaskType.CAUSAL_LM,
397	        r=args.lora_rank,
398	        lora_alpha=args.lora_alpha,
399	        lora_dropout=0.05,
400	        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
401	                         "gate_proj", "up_proj", "down_proj"],
402	    )
403	
404	    grpo_config = GRPOConfig(
405	        output_dir=args.output_dir,
406	        num_train_epochs=args.num_epochs,
407	        per_device_train_batch_size=args.per_device_batch_size,
408	        gradient_accumulation_steps=args.gradient_accumulation_steps,
409	        learning_rate=args.learning_rate,
410	        bf16=args.bf16,
411	        logging_steps=5,
412	        save_strategy="epoch",
413	        save_total_limit=2,
414	        seed=args.seed,
415	        num_generations=args.num_generations,
416	        max_completion_length=args.max_new_tokens,
417	        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
418	        gradient_checkpointing=True,
419	        gradient_checkpointing_kwargs={"use_reentrant": False},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "bc9aedf7-3d3f-45af-8b79-40f298f01038",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
      "content": "        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},",
      "numLines": 140,
      "startLine": 280,
      "totalLines": 443
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

Now I need to: 1) add `import math` for total_steps computation, 2) compute total_steps after dataset preparation, 3) pass it to CEDRewardWrapper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "b47ea7cb-2ab3-465e-a412-0a3c41975bde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7vPDmWStEYj1b41x6JLzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4261,
      "cache_read_input_tokens": 50254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4261
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_013dpDdqwT55hCLkBmuhww5L`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "import argparse\nimport json\nimport logging\nimport os\nimport re",
  "new_string": "import argparse\nimport json\nimport logging\nimport math\nimport os\nimport re"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "d23ded03-c6c2-473b-85bb-ef233f13a3f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7vPDmWStEYj1b41x6JLzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4261,
      "cache_read_input_tokens": 50254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4261
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T06:11:14.437Z_

<details><summary>↩ Tool result · `toolu_013dpDdqwT55hCLkBmuhww5L`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "69a74ac4-1ce9-4f63-83f9-279d2e56f5c5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "import argparse\nimport json\nimport logging\nimport os\nimport re",
    "newString": "import argparse\nimport json\nimport logging\nimport math\nimport os\nimport re",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n        tau_start: float = None,\n        tau_end: float = None,\n        total_steps: int = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.mode = mode\n        self._call_count = 0\n        if tau_start is not None and tau_end is not None:\n            self.tau_start = tau_start\n            self.tau_end = tau_end\n            self.total_steps = total_steps\n        else:\n            self.tau_start = tau\n            self.tau_end = tau\n            self.total_steps = None\n\n    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = min(self._call_count / max(self._call_count, 1), 1.0)\n        return self.tau_start + (self.tau_end - self.tau_start) * progress\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        current_tau = self.tau\n        self._call_count += 1\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=current_tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=current_tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 6,
        "newStart": 12,
        "newLines": 7,
        "lines": [
          " import argparse",
          " import json",
          " import logging",
          "+import math",
          " import os",
          " import re",
          " from pathlib import Path"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 60_

Now compute total_steps and pass it to CEDRewardWrapper:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "952c4e67-3c07-4a9c-913a-26cbd28eb941",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PG48QEhfyXcCKLu99t8Ffr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 54515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 283
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Edit · `toolu_0129u8faiRiyZ8XK7j69xFET`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)",
  "new_string": "    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        steps_per_epoch = math.ceil(\n            len(train_dataset) / (args.per_device_batch_size * args.gradient_accumulation_steps)\n        )\n        total_steps = steps_per_epoch * args.num_epochs\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n            total_steps=total_steps,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\n            \"Stage %d: using %s reward, tau %.2f→%.2f over %d steps\",\n            args.stage, mode, args.tau_start, args.tau_end, total_steps,\n        )"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "36291474-8d5b-4c3b-b3ad-56ba4ae9768a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PG48QEhfyXcCKLu99t8Ffr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 54515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 283
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T06:11:25.666Z_

<details><summary>↩ Tool result · `toolu_0129u8faiRiyZ8XK7j69xFET`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "b471135c-eeeb-4b73-b6f4-e850413fe385",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)",
    "newString": "    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        steps_per_epoch = math.ceil(\n            len(train_dataset) / (args.per_device_batch_size * args.gradient_accumulation_steps)\n        )\n        total_steps = steps_per_epoch * args.num_epochs\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n            total_steps=total_steps,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\n            \"Stage %d: using %s reward, tau %.2f→%.2f over %d steps\",\n            args.stage, mode, args.tau_start, args.tau_end, total_steps,\n        )",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport math\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n        tau_start: float = None,\n        tau_end: float = None,\n        total_steps: int = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.mode = mode\n        self._call_count = 0\n        if tau_start is not None and tau_end is not None:\n            self.tau_start = tau_start\n            self.tau_end = tau_end\n            self.total_steps = total_steps\n        else:\n            self.tau_start = tau\n            self.tau_end = tau\n            self.total_steps = None\n\n    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = min(self._call_count / max(self._call_count, 1), 1.0)\n        return self.tau_start + (self.tau_end - self.tau_start) * progress\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        current_tau = self.tau\n        self._call_count += 1\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=current_tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=current_tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\"Stage %d: using %s reward\", args.stage, mode)\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 381,
        "oldLines": 15,
        "newStart": 381,
        "newLines": 23,
        "lines": [
          " ",
          "     if args.stage >= 2:",
          "         mode = \"flat_nli\" if args.stage == 2 else \"ced\"",
          "+        steps_per_epoch = math.ceil(",
          "+            len(train_dataset) / (args.per_device_batch_size * args.gradient_accumulation_steps)",
          "+        )",
          "+        total_steps = steps_per_epoch * args.num_epochs",
          "         ced_wrapper = CEDRewardWrapper(",
          "             nli_model=args.nli_model,",
          "             mode=mode,",
          "             device=args.reward_device,",
          "             tau_start=args.tau_start,",
          "             tau_end=args.tau_end,",
          "+            total_steps=total_steps,",
          "         )",
          "         reward_fns.append(ced_wrapper)",
          "-        logger.info(\"Stage %d: using %s reward\", args.stage, mode)",
          "+        logger.info(",
          "+            \"Stage %d: using %s reward, tau %.2f→%.2f over %d steps\",",
          "+            args.stage, mode, args.tau_start, args.tau_end, total_steps,",
          "+        )",
          "     else:",
          "         logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 63_

Now let me also simplify the `tau` property — with total_steps always provided when tau scheduling is active, we can remove the fallback branch that was broken:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "0cd68956-baf4-4418-a125-5e2e77f96035",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjKwUPEfP9Yf6aMFAvcgBp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 54798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 646
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Edit · `toolu_01RZEzQDqZRaxpaJY2QySrEY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "old_string": "    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = min(self._call_count / max(self._call_count, 1), 1.0)\n        return self.tau_start + (self.tau_end - self.tau_start) * progress",
  "new_string": "    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = 1.0\n        return self.tau_start + (self.tau_end - self.tau_start) * progress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "842eb459-141f-43a1-9934-c98ab0f7a263",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjKwUPEfP9Yf6aMFAvcgBp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 54798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 646
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-14T06:11:32.333Z_

<details><summary>↩ Tool result · `toolu_01RZEzQDqZRaxpaJY2QySrEY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "183ce9d7-d9d4-4699-b864-d0e5ddee83da",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
    "oldString": "    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = min(self._call_count / max(self._call_count, 1), 1.0)\n        return self.tau_start + (self.tau_end - self.tau_start) * progress",
    "newString": "    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = 1.0\n        return self.tau_start + (self.tau_end - self.tau_start) * progress",
    "originalFile": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport math\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n        tau_start: float = None,\n        tau_end: float = None,\n        total_steps: int = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.mode = mode\n        self._call_count = 0\n        if tau_start is not None and tau_end is not None:\n            self.tau_start = tau_start\n            self.tau_end = tau_end\n            self.total_steps = total_steps\n        else:\n            self.tau_start = tau\n            self.tau_end = tau\n            self.total_steps = None\n\n    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = min(self._call_count / max(self._call_count, 1), 1.0)\n        return self.tau_start + (self.tau_end - self.tau_start) * progress\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        current_tau = self.tau\n        self._call_count += 1\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=current_tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=current_tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        steps_per_epoch = math.ceil(\n            len(train_dataset) / (args.per_device_batch_size * args.gradient_accumulation_steps)\n        )\n        total_steps = steps_per_epoch * args.num_epochs\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n            total_steps=total_steps,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\n            \"Stage %d: using %s reward, tau %.2f→%.2f over %d steps\",\n            args.stage, mode, args.tau_start, args.tau_end, total_steps,\n        )\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 158,
        "oldLines": 7,
        "newStart": 158,
        "newLines": 7,
        "lines": [
          "         if self.total_steps and self.total_steps > 0:",
          "             progress = min(self._call_count / self.total_steps, 1.0)",
          "         else:",
          "-            progress = min(self._call_count / max(self._call_count, 1), 1.0)",
          "+            progress = 1.0",
          "         return self.tau_start + (self.tau_end - self.tau_start) * progress",
          " ",
          "     def __call__("
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 66_

Let me do a final verification of all four files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "bd0f3e6f-ddef-4853-956e-13b65e6f1c20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpGf28s1Evp3SwxUY86mtk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 55444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 443
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_018gXLXiDNjf9WuaovvV8yaN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "offset": 1,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "92e7a9a3-587d-4e2f-afee-f14999d15a67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpGf28s1Evp3SwxUY86mtk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 55444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 443
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T06:11:40.227Z_

<details><summary>↩ Tool result · `toolu_018gXLXiDNjf9WuaovvV8yaN`</summary>

```text
1	"""GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。
2	
3	支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。
4	
5	单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1
6	多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
7	            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \
8	            --stage 1 --reward_device cpu
9	不量化: 加 --no_quantize
10	"""
11	
12	import argparse
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "e8c8a589-1c0b-4c7e-87d1-5609b284b2c0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
      "content": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 452
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01FutNVhPZdabxNDPFpRTqhk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
  "offset": 41,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "f179b1f6-8d39-4255-86b8-0bba1845eb66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpGf28s1Evp3SwxUY86mtk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 55444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 443
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T06:11:41.322Z_

<details><summary>↩ Tool result · `toolu_01FutNVhPZdabxNDPFpRTqhk`</summary>

```text
41	DEFAULT_MODEL = "/root/autodl-tmp/models/Qwen3-4B"
42	
43	
44	def build_chat_messages(instruction: str, input_text: str, output_text: str = None):
45	    """构建 Qwen3 chat 格式的消息列表。"""
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "2bf9bfe5-7b4d-44d2-b394-387d63f8e381",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
      "content": "DEFAULT_MODEL = \"/root/autodl-tmp/models/Qwen3-4B\"\n\n\ndef build_chat_messages(instruction: str, input_text: str, output_text: str = None):\n    \"\"\"构建 Qwen3 chat 格式的消息列表。\"\"\"",
      "numLines": 5,
      "startLine": 41,
      "totalLines": 215
    }
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_018RNNgj78BxZm5nV3uXyFsu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
  "offset": 142,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "f11d90d4-0105-456d-8ede-2ba8006e2639",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpGf28s1Evp3SwxUY86mtk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 55444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 443
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T06:11:41.654Z_

<details><summary>↩ Tool result · `toolu_018RNNgj78BxZm5nV3uXyFsu`</summary>

```text
142	    model_kwargs = dict(
143	        trust_remote_code=True,
144	        attn_implementation="sdpa",
145	    )
146	    if args.quantize:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "2451e177-4240-4470-83e6-502449946c1d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
      "content": "    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:",
      "numLines": 5,
      "startLine": 142,
      "totalLines": 215
    }
  }
}
```

</details>

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Read · `toolu_01TtycePCghAocCvtiZtqAnM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
  "offset": 29,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "02bb762d-26d4-4a84-884c-78455659bd91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpGf28s1Evp3SwxUY86mtk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 55444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 443
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T06:11:42.540Z_

<details><summary>↩ Tool result · `toolu_01TtycePCghAocCvtiZtqAnM`</summary>

```text
29	MODEL_NAME = "/root/autodl-tmp/models/Qwen3-4B"
30	
31	SYSTEM_PROMPT = (
32	    "You are an information extraction model. Given a document with numbered sentences "
33	    "and a list of entities, extract all relation triples. For each triple, provide the "
34	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
35	    "Output as a JSON list."
36	)
37	
38	DEEPSPEED_CONFIG = {
39	    "bf16": {"enabled": True},
40	    "zero_optimization": {
41	        "stage": 2,
42	        "offload_optimizer": {"device": "cpu", "pin_memory": True},
43	        "overlap_comm": True,
44	        "contiguous_gradients": True,
45	        "reduce_bucket_size": "auto",
46	        "allgather_bucket_size": 5e8,
47	        "allgather_partitions": True,
48	    },
49	    "gradient_accumulation_steps": "auto",
50	    "gradient_clipping": "auto",
51	    "train_batch_size": "auto",
52	    "train_micro_batch_size_per_gpu": "auto",
53	}
54	
55	DUMMY_DOCS = [
56	    {
57	        "sents": [
58	            "Albert Einstein was born in Ulm, Germany in 1879.",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "68c6e8e9-8529-460c-9955-44e503e971d1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py",
      "content": "MODEL_NAME = \"/root/autodl-tmp/models/Qwen3-4B\"\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\nDEEPSPEED_CONFIG = {\n    \"bf16\": {\"enabled\": True},\n    \"zero_optimization\": {\n        \"stage\": 2,\n        \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": True},\n        \"overlap_comm\": True,\n        \"contiguous_gradients\": True,\n        \"reduce_bucket_size\": \"auto\",\n        \"allgather_bucket_size\": 5e8,\n        \"allgather_partitions\": True,\n    },\n    \"gradient_accumulation_steps\": \"auto\",\n    \"gradient_clipping\": \"auto\",\n    \"train_batch_size\": \"auto\",\n    \"train_micro_batch_size_per_gpu\": \"auto\",\n}\n\nDUMMY_DOCS = [\n    {\n        \"sents\": [\n            \"Albert Einstein was born in Ulm, Germany in 1879.\",",
      "numLines": 30,
      "startLine": 29,
      "totalLines": 327
    }
  }
}
```

</details>

---

### Assistant

_source line 75_

所有修改完成。汇总如下：

---

## 修改汇总

### 1. `training/sft_trainer.py`
- `DEFAULT_MODEL` → `"/root/autodl-tmp/models/Qwen3-4B"`（本地模型路径）
- `attn_implementation` → `"sdpa"`（替代 flash_attention_2）
- 头部注释已经引用 `deepspeed_zero2.json`，无需改动

### 2. `training/grpo_trainer.py`
- `--model_name` default → `"/root/autodl-tmp/models/Qwen3-4B"`
- `attn_implementation` → `"sdpa"`
- 头部注释 `deepspeed_zero3.json` → `deepspeed_zero2.json`
- 新增 `--tau_start`（default=0.3）和 `--tau_end`（default=0.5），替换原 `--tau`
- `CEDRewardWrapper` 新增 tau 线性调度：接受 `tau_start`/`tau_end`/`total_steps`，通过内部计数器 `_call_count` 实现 `tau = tau_start + (tau_end - tau_start) * (step / total_steps)`
- `main()` 中根据 dataset 大小和训练参数计算 `total_steps` 传入 wrapper

### 3. `rewards/ced_reward.py`
- **无需修改**。确认 `compute_ced_reward()` 第236-237行：`hard_negative_sents` 为空时 `p_neg = 0.0`，奖励退化为 `p_pos * I(p_pos > tau)` = flat NLI，行为正确

### 4. `training/smoke_test.py`
- `MODEL_NAME` → `"/root/autodl-tmp/models/Qwen3-4B"`
- `attn_implementation` → `"sdpa"`
- `DS_CONFIG.zero_optimization.stage` → 2，移除 `offload_param`，移除 stage3 专属参数，添加 ZeRO-2 参数（`allgather_bucket_size`、`allgather_partitions`）
- `NUM_GENERATIONS` 已为 4，无需改动

---

## MVP-2 训练计划

### Phase 1: SFT warmup（~3h）
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.sft_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --output_dir /root/autodl-tmp/freige/sft_output \
    --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 \
    --learning_rate 2e-4 --wandb_run_name sft-warmup-v1
```

### Phase 2: GRPO 三路对比（每路 ~2-3h）

**Stage 1: extraction-only**
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.grpo_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --sft_adapter /root/autodl-tmp/freige/sft_output \
    --stage 1 --output_dir /root/autodl-tmp/freige/grpo_s1 \
    --reward_device cpu --wandb_run_name grpo-s1-extract
```

**Stage 2: flat-NLI**
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.grpo_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --sft_adapter /root/autodl-tmp/freige/sft_output \
    --stage 2 --output_dir /root/autodl-tmp/freige/grpo_s2 \
    --tau_start 0.3 --tau_end 0.5 \
    --reward_device cpu --wandb_run_name grpo-s2-flatnli
```

**Stage 3: CED**
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.grpo_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --sft_adapter /root/autodl-tmp/freige/sft_output \
    --stage 3 --output_dir /root/autodl-tmp/freige/grpo_s3 \
    --tau_start 0.3 --tau_end 0.5 \
    --reward_device cpu --wandb_run_name grpo-s3-ced
```

### 预计 GPU 时间

| 阶段 | 4x RTX 5090 预估 | 说明 |
|------|-------------------|------|
| SFT warmup | ~3h | 3 epochs, ~3k docs, QLoRA |
| GRPO Stage 1 | ~2h | 1 epoch, 无 NLI 模型开销 |
| GRPO Stage 2 | ~3h | 1 epoch, CPU 上跑 DeBERTa |
| GRPO Stage 3 | ~3h | 1 epoch, CPU 上跑 DeBERTa + hard neg |
| **总计** | **~11h** | 三路 GRPO 可并行则 ~6h |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "uuid": "3c61f29d-ecf5-4653-9be2-f92f7c198537",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RNf2xkCiTHTib5teHnJ61M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1396,
      "cache_read_input_tokens": 55887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1396
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 76_

所有修改完成。汇总如下：

---

## 修改汇总

### 1. `training/sft_trainer.py`
- `DEFAULT_MODEL` → `"/root/autodl-tmp/models/Qwen3-4B"`（本地模型路径）
- `attn_implementation` → `"sdpa"`（替代 flash_attention_2）
- 头部注释已经引用 `deepspeed_zero2.json`，无需改动

### 2. `training/grpo_trainer.py`
- `--model_name` default → `"/root/autodl-tmp/models/Qwen3-4B"`
- `attn_implementation` → `"sdpa"`
- 头部注释 `deepspeed_zero3.json` → `deepspeed_zero2.json`
- 新增 `--tau_start`（default=0.3）和 `--tau_end`（default=0.5），替换原 `--tau`
- `CEDRewardWrapper` 新增 tau 线性调度：接受 `tau_start`/`tau_end`/`total_steps`，通过内部计数器 `_call_count` 实现 `tau = tau_start + (tau_end - tau_start) * (step / total_steps)`
- `main()` 中根据 dataset 大小和训练参数计算 `total_steps` 传入 wrapper

### 3. `rewards/ced_reward.py`
- **无需修改**。确认 `compute_ced_reward()` 第236-237行：`hard_negative_sents` 为空时 `p_neg = 0.0`，奖励退化为 `p_pos * I(p_pos > tau)` = flat NLI，行为正确

### 4. `training/smoke_test.py`
- `MODEL_NAME` → `"/root/autodl-tmp/models/Qwen3-4B"`
- `attn_implementation` → `"sdpa"`
- `DS_CONFIG.zero_optimization.stage` → 2，移除 `offload_param`，移除 stage3 专属参数，添加 ZeRO-2 参数（`allgather_bucket_size`、`allgather_partitions`）
- `NUM_GENERATIONS` 已为 4，无需改动

---

## MVP-2 训练计划

### Phase 1: SFT warmup（~3h）
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.sft_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --output_dir /root/autodl-tmp/freige/sft_output \
    --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 \
    --learning_rate 2e-4 --wandb_run_name sft-warmup-v1
```

### Phase 2: GRPO 三路对比（每路 ~2-3h）

**Stage 1: extraction-only**
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.grpo_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --sft_adapter /root/autodl-tmp/freige/sft_output \
    --stage 1 --output_dir /root/autodl-tmp/freige/grpo_s1 \
    --reward_device cpu --wandb_run_name grpo-s1-extract
```

**Stage 2: flat-NLI**
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.grpo_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --sft_adapter /root/autodl-tmp/freige/sft_output \
    --stage 2 --output_dir /root/autodl-tmp/freige/grpo_s2 \
    --tau_start 0.3 --tau_end 0.5 \
    --reward_device cpu --wandb_run_name grpo-s2-flatnli
```

**Stage 3: CED**
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.grpo_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --sft_adapter /root/autodl-tmp/freige/sft_output \
    --stage 3 --output_dir /root/autodl-tmp/freige/grpo_s3 \
    --tau_start 0.3 --tau_end 0.5 \
    --reward_device cpu --wandb_run_name grpo-s3-ced
```

### 预计 GPU 时间

| 阶段 | 4x RTX 5090 预估 | 说明 |
|------|-------------------|------|
| SFT warmup | ~3h | 3 epochs, ~3k docs, QLoRA |
| GRPO Stage 1 | ~2h | 1 epoch, 无 NLI 模型开销 |
| GRPO Stage 2 | ~3h | 1 epoch, CPU 上跑 DeBERTa |
| GRPO Stage 3 | ~3h | 1 epoch, CPU 上跑 DeBERTa + hard neg |
| **总计** | **~11h** | 三路 GRPO 可并行则 ~6h |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 206988,
  "duration_api_ms": 208190,
  "num_turns": 28,
  "stop_reason": "end_turn",
  "session_id": "2ea21df7-2318-4e4f-9781-eeee3dd15ab0",
  "total_cost_usd": 1.0421555,
  "usage": {
    "input_tokens": 23,
    "cache_creation_input_tokens": 45836,
    "cache_read_input_tokens": 991791,
    "output_tokens": 10295,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 45836,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1453,
        "cache_read_input_tokens": 55887,
        "cache_creation_input_tokens": 1396,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1396
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2160,
      "outputTokens": 27,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002295,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 23,
      "outputTokens": 10295,
      "cacheReadInputTokens": 991791,
      "cacheCreationInputTokens": 45836,
      "webSearchRequests": 0,
      "costUSD": 1.0398604999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0630e88f-6edc-4c17-9ad7-ac825daebe31"
}
```

</details>

---
