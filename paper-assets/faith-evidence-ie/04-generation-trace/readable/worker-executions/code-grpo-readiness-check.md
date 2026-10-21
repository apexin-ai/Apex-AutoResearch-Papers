# code grpo readiness check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_code_grpo-readiness-check_20260514T070038.log`
- **Structured JSON:** [`170f3e5215646e20b0f8.json`](../../sessions/17/170f3e5215646e20b0f8.json)

## Before a recorded user message

16 recorded events

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
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
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
  "uuid": "c253d154-2d32-4a28-8d91-22e725395eb2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
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
    "resetsAt": 1778750400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c1bf66d2-abde-44df-87b5-30e93eb251e4",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Assistant

_source line 4_

我来逐步检查代码并生成验证报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "78101f8f-c4a3-4f8d-948d-f05884c09a6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YaZzP5dKJAdWRHMKepgZVC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12289,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12289
      },
      "output_tokens": 7,
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

<details open><summary>🔧 Tool call — Read · `toolu_01UtdjWfYTpjKxTjjAUqsFMj`</summary>

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
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "ed8e89ae-3b0d-4094-bebd-8bcdb64484c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YaZzP5dKJAdWRHMKepgZVC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12289,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12289
      },
      "output_tokens": 7,
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

_source line 6 · 2026-05-14T07:00:49.300Z_

<details><summary>↩ Tool result · `toolu_01UtdjWfYTpjKxTjjAUqsFMj`</summary>

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
13	import json
14	import logging
15	import math
16	import os
17	import re
18	from pathlib import Path
19	from typing import Optional
20	
21	import torch
22	from datasets import Dataset
23	from peft import LoraConfig, PeftModel, TaskType
24	from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
25	from trl import GRPOConfig, GRPOTrainer
26	
27	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
28	logger = logging.getLogger(__name__)
29	
30	SYSTEM_PROMPT = (
31	    "You are an information extraction model. Given a document with numbered sentences "
32	    "and a list of entities, extract all relation triples. For each triple, provide the "
33	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
34	    "Output as a JSON list."
35	)
36	
37	
38	def _parse_json_output(text: str) -> list[dict]:
39	    """从模型输出中解析 JSON 列表。"""
40	    try:
41	        return json.loads(text)
42	    except json.JSONDecodeError:
43	        start = text.find("[")
44	        end = text.rfind("]") + 1
45	        if start >= 0 and end > start:
46	            try:
47	                return json.loads(text[start:end])
48	            except json.JSONDecodeError:
49	                return []
50	    return []
51	
52	
53	def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
54	    """格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。"""
55	    rewards = []
56	    for text in completions:
57	        parsed = _parse_json_output(text)
58	        if not isinstance(parsed, list):
59	            rewards.append(0.0)
60	            continue
61	        if not parsed:
62	            rewards.append(0.1)
63	            continue
64	        valid = 0
65	        for item in parsed:
66	            if (isinstance(item, dict) and "head" in item
67	                    and "relation" in item and "tail" in item
68	                    and "evidence" in item
69	                    and isinstance(item["evidence"], list)):
70	                valid += 1
71	        rewards.append(valid / len(parsed))
72	    return rewards
73	
74	
75	def f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:
76	    """F1 奖励: 预测三元组与 gold 三元组的 micro-F1。
77	
78	    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。
79	    completions 中每 num_generations 个对应同一个 prompt。
80	    """
81	    num_gen = len(completions) // len(gold_triples)
82	    rewards = []
83	
84	    for i, text in enumerate(completions):
85	        gold_idx = i // num_gen
86	        gold_str = gold_triples[gold_idx]
87	        try:
88	            gold = json.loads(gold_str)
89	        except (json.JSONDecodeError, IndexError):
90	            rewards.append(0.0)
91	            continue
92	
93	        pred = _parse_json_output(text)
94	
95	        gold_set = set()
96	        for g in gold:
97	            gold_set.add((
98	                g.get("head", "").lower().strip(),
99	                g.get("relation", "").lower().strip(),
100	                g.get("tail", "").lower().strip(),
101	            ))
102	
103	        pred_set = set()
104	        for p in pred:
105	            if isinstance(p, dict):
106	                pred_set.add((
107	                    p.get("head", "").lower().strip(),
108	                    p.get("relation", "").lower().strip(),
109	                    p.get("tail", "").lower().strip(),
110	                ))
111	
112	        if not gold_set:
113	            rewards.append(1.0 if not pred_set else 0.0)
114	            continue
115	
116	        tp = len(pred_set & gold_set)
117	        prec = tp / len(pred_set) if pred_set else 0.0
118	        rec = tp / len(gold_set) if gold_set else 0.0
119	        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
120	        rewards.append(f1)
121	
122	    return rewards
123	
124	
125	class CEDRewardWrapper:
126	    """将 CED 奖励封装为 GRPO 兼容的 reward function。
127	
128	    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，
129	    返回所有 triples 的平均 CED reward。
130	    """
131	
132	    def __init__(
133	        self,
134	        nli_model: str = "cross-encoder/nli-deberta-v3-base",
135	        tau: float = 0.5,
136	        mode: str = "ced",
137	        device: str = None,
138	        tau_start: float = None,
139	        tau_end: float = None,
140	        total_steps: int = None,
141	    ):
142	        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple
143	        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)
144	        self.verbalize = verbalize_triple
145	        self.mode = mode
146	        self._call_count = 0
147	        if tau_start is not None and tau_end is not None:
148	            self.tau_start = tau_start
149	            self.tau_end = tau_end
150	            self.total_steps = total_steps
151	        else:
152	            self.tau_start = tau
153	            self.tau_end = tau
154	            self.total_steps = None
155	
156	    @property
157	    def tau(self) -> float:
158	        if self.total_steps and self.total_steps > 0:
159	            progress = min(self._call_count / self.total_steps, 1.0)
160	        else:
161	            progress = 1.0
162	        return self.tau_start + (self.tau_end - self.tau_start) * progress
163	
164	    def __call__(
165	        self,
166	        completions: list[str],
167	        all_sents: list[str],
168	        gold_triples: list[str],
169	        **kwargs,
170	    ) -> list[float]:
171	        """计算 CED/flat-NLI 奖励。
172	
173	        all_sents: JSON 字符串列表，每个元素为文档句子列表。
174	        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。
175	        """
176	        current_tau = self.tau
177	        self._call_count += 1
178	        num_gen = len(completions) // len(all_sents)
179	        rewards = []
180	
181	        for i, text in enumerate(completions):
182	            prompt_idx = i // num_gen
183	            try:
184	                sents = json.loads(all_sents[prompt_idx])
185	                gold = json.loads(gold_triples[prompt_idx])
186	            except (json.JSONDecodeError, IndexError):
187	                rewards.append(0.0)
188	                continue
189	
190	            pred = _parse_json_output(text)
191	            if not pred:
192	                rewards.append(0.0)
193	                continue
194	
195	            gold_map = {}
196	            for g in gold:
197	                key = (
198	                    g.get("head", "").lower().strip(),
199	                    g.get("relation", "").lower().strip(),
200	                    g.get("tail", "").lower().strip(),
201	                )
202	                gold_map[key] = g
203	
204	            triple_rewards = []
205	            for p in pred:
206	                if not isinstance(p, dict):
207	                    continue
208	                pred_evi_ids = p.get("evidence", [])
209	                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:
210	                    triple_rewards.append(0.0)
211	                    continue
212	
213	                claim = self.verbalize(
214	                    p.get("head", ""),
215	                    p.get("relation", ""),
216	                    p.get("tail", ""),
217	                )
218	                cited_sents = [sents[idx] for idx in pred_evi_ids
219	                               if isinstance(idx, int) and 0 <= idx < len(sents)]
220	                if not cited_sents:
221	                    triple_rewards.append(0.0)
222	                    continue
223	
224	                key = (
225	                    p.get("head", "").lower().strip(),
226	                    p.get("relation", "").lower().strip(),
227	                    p.get("tail", "").lower().strip(),
228	                )
229	                matched_gold = gold_map.get(key, {})
230	                hard_neg_ids = matched_gold.get("hard_negative_sent_ids", [])
231	                hard_neg_sents = [sents[idx] for idx in hard_neg_ids
232	                                  if isinstance(idx, int) and 0 <= idx < len(sents)]
233	
234	                if self.mode == "flat_nli":
235	                    result = self.reward_model.compute_flat_nli_reward(
236	                        claim, cited_sents, tau=current_tau,
237	                    )
238	                else:
239	                    result = self.reward_model.compute_ced_reward(
240	                        claim, cited_sents, hard_neg_sents, tau=current_tau,
241	                    )
242	                triple_rewards.append(result["reward"])
243	
244	            rewards.append(
245	                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0
246	            )
247	
248	        return rewards
249	
250	
251	def prepare_grpo_dataset(
252	    data_dir: str = None,
253	    split: str = "train",
254	    tokenizer=None,
255	) -> Dataset:
256	    """准备 GRPO prompt 数据集。
257	
258	    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。
259	    """
260	    from freige.data.docred_processor import DocREDProcessor
261	
262	    processor = DocREDProcessor(data_dir=data_dir)
263	    samples = processor.process(split)
264	    groups = processor.group_by_document(samples)
265	
266	    dataset_items = []
267	    for doc_id, doc_samples in groups.items():
268	        sft_sample = processor.format_sft_sample(doc_samples)
269	        messages = [
270	            {"role": "system", "content": SYSTEM_PROMPT},
271	            {"role": "user", "content": f"{sft_sample['instruction']}\n\n{sft_sample['input']}"},
272	        ]
273	        prompt = tokenizer.apply_chat_template(
274	            messages,
275	            tokenize=False,
276	            add_generation_prompt=True,
277	            enable_thinking=False,
278	        )
279	
280	        gold_triples = []
281	        for s in doc_samples:
282	            gold_triples.append({
283	                "head": s.head.name,
284	                "relation": s.relation_name,
285	                "tail": s.tail.name,
286	                "evidence": s.evidence_sent_ids,
287	                "hard_negative_sent_ids": s.hard_negative_sent_ids,
288	            })
289	
290	        ref = doc_samples[0]
291	        dataset_items.append({
292	            "prompt": prompt,
293	            "gold_triples": json.dumps(gold_triples, ensure_ascii=False),
294	            "all_sents": json.dumps(ref.sents, ensure_ascii=False),
295	        })
296	
297	    logger.info("Prepared %d GRPO prompts", len(dataset_items))
298	    return Dataset.from_list(dataset_items)
299	
300	
301	def main():
302	    parser = argparse.ArgumentParser(description="FREIGE GRPO Training")
303	    parser.add_argument("--model_name", type=str, default="/root/autodl-tmp/models/Qwen3-4B",
304	                        help="基础模型或 SFT checkpoint 路径")
305	    parser.add_argument("--sft_adapter", type=str, default=None,
306	                        help="SFT LoRA adapter 路径（如果与 model_name 不同）")
307	    parser.add_argument("--data_dir", type=str, default=None)
308	    parser.add_argument("--output_dir", type=str, default="./grpo_output")
309	    parser.add_argument("--stage", type=int, default=1, choices=[1, 2, 3],
310	                        help="Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED")
311	    parser.add_argument("--nli_model", type=str, default="cross-encoder/nli-deberta-v3-base")
312	    parser.add_argument("--num_generations", type=int, default=4)
313	    parser.add_argument("--lora_rank", type=int, default=64)
314	    parser.add_argument("--lora_alpha", type=int, default=128)
315	    parser.add_argument("--max_length", type=int, default=4096)
316	    parser.add_argument("--max_new_tokens", type=int, default=1024)
317	    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction, default=True,
318	                        help="启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）")
319	    parser.add_argument("--deepspeed", type=str, default=None,
320	                        help="DeepSpeed 配置文件路径")
321	    parser.add_argument("--reward_device", type=str, default="cpu",
322	                        help="CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）")
323	    parser.add_argument("--per_device_batch_size", type=int, default=1)
324	    parser.add_argument("--gradient_accumulation_steps", type=int, default=16)
325	    parser.add_argument("--num_epochs", type=int, default=1)
326	    parser.add_argument("--learning_rate", type=float, default=5e-5)
327	    parser.add_argument("--tau_start", type=float, default=0.3,
328	                        help="CED tau 初始值")
329	    parser.add_argument("--tau_end", type=float, default=0.5,
330	                        help="CED tau 最终值（线性调度）")
331	    parser.add_argument("--bf16", action="store_true", default=True)
332	    parser.add_argument("--seed", type=int, default=42)
333	    parser.add_argument("--wandb_project", type=str, default="freige-grpo")
334	    parser.add_argument("--wandb_run_name", type=str, default=None)
335	    args = parser.parse_args()
336	
337	    if args.wandb_project and "WANDB_API_KEY" in os.environ:
338	        os.environ["WANDB_PROJECT"] = args.wandb_project
339	        if args.wandb_run_name:
340	            os.environ["WANDB_NAME"] = args.wandb_run_name
341	
342	    logger.info("Loading tokenizer: %s", args.model_name)
343	    tokenizer = AutoTokenizer.from_pretrained(
344	        args.model_name,
345	        trust_remote_code=True,
346	        padding_side="left",
347	    )
348	    if tokenizer.pad_token is None:
349	        tokenizer.pad_token = tokenizer.eos_token
350	
351	    logger.info("Preparing dataset...")
352	    train_dataset = prepare_grpo_dataset(
353	        data_dir=args.data_dir,
354	        split="train",
355	        tokenizer=tokenizer,
356	    )
357	
358	    logger.info("Loading model: %s", args.model_name)
359	    model_kwargs = dict(
360	        trust_remote_code=True,
361	        attn_implementation="sdpa",
362	    )
363	    if args.quantize:
364	        logger.info("Using 4-bit QLoRA quantization")
365	        model_kwargs["quantization_config"] = BitsAndBytesConfig(
366	            load_in_4bit=True,
367	            bnb_4bit_compute_dtype=torch.bfloat16,
368	            bnb_4bit_quant_type="nf4",
369	            bnb_4bit_use_double_quant=True,
370	        )
371	    else:
372	        model_kwargs["torch_dtype"] = torch.bfloat16 if args.bf16 else torch.float16
373	    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)
374	
375	    if args.sft_adapter:
376	        logger.info("Loading SFT adapter from %s", args.sft_adapter)
377	        model = PeftModel.from_pretrained(model, args.sft_adapter)
378	        model = model.merge_and_unload()
379	
380	    reward_fns = [format_reward_fn, f1_reward_fn]
381	
382	    if args.stage >= 2:
383	        mode = "flat_nli" if args.stage == 2 else "ced"
384	        steps_per_epoch = math.ceil(
385	            len(train_dataset) / (args.per_device_batch_size * args.gradient_accumulation_steps)
386	        )
387	        total_steps = steps_per_epoch * args.num_epochs
388	        ced_wrapper = CEDRewardWrapper(
389	            nli_model=args.nli_model,
390	            mode=mode,
391	            device=args.reward_device,
392	            tau_start=args.tau_start,
393	            tau_end=args.tau_end,
394	            total_steps=total_steps,
395	        )
396	        reward_fns.append(ced_wrapper)
397	        logger.info(
398	            "Stage %d: using %s reward, tau %.2f→%.2f over %d steps",
399	            args.stage, mode, args.tau_start, args.tau_end, total_steps,
400	        )
401	    else:
402	        logger.info("Stage 1: extraction-only (format + F1 rewards)")
403	
404	    lora_config = LoraConfig(
405	        task_type=TaskType.CAUSAL_LM,
406	        r=args.lora_rank,
407	        lora_alpha=args.lora_alpha,
408	        lora_dropout=0.05,
409	        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
410	                         "gate_proj", "up_proj", "down_proj"],
411	    )
412	
413	    grpo_config = GRPOConfig(
414	        output_dir=args.output_dir,
415	        num_train_epochs=args.num_epochs,
416	        per_device_train_batch_size=args.per_device_batch_size,
417	        gradient_accumulation_steps=args.gradient_accumulation_steps,
418	        learning_rate=args.learning_rate,
419	        bf16=args.bf16,
420	        logging_steps=5,
421	        save_strategy="epoch",
422	        save_total_limit=2,
423	        seed=args.seed,
424	        num_generations=args.num_generations,
425	        max_completion_length=args.max_new_tokens,
426	        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
427	        gradient_checkpointing=True,
428	        gradient_checkpointing_kwargs={"use_reentrant": False},
429	        deepspeed=args.deepspeed,
430	    )
431	
432	    trainer = GRPOTrainer(
433	        model=model,
434	        args=grpo_config,
435	        train_dataset=train_dataset,
436	        reward_funcs=reward_fns,
437	        peft_config=lora_config,
438	        processing_class=tokenizer,
439	    )
440	
441	    logger.info("Starting GRPO training (stage %d)...", args.stage)
442	    trainer.train()
443	
444	    logger.info("Saving model to %s", args.output_dir)
445	    trainer.save_model(args.output_dir)
446	    tokenizer.save_pretrained(args.output_dir)
447	    logger.info("GRPO training (stage %d) complete.", args.stage)
448	
449	
450	if __name__ == "__main__":
451	    main()
452	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "67e14793-8e22-4b67-8882-ba4fbdc77857",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
      "content": "\"\"\"GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。\n\n支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。\n\n单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1\n多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \\\n            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \\\n            --stage 1 --reward_device cpu\n不量化: 加 --no_quantize\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport math\nimport os\nimport re\nfrom pathlib import Path\nfrom typing import Optional\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, PeftModel, TaskType\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\nfrom trl import GRPOConfig, GRPOTrainer\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlogger = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are an information extraction model. Given a document with numbered sentences \"\n    \"and a list of entities, extract all relation triples. For each triple, provide the \"\n    \"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \"\n    \"Output as a JSON list.\"\n)\n\n\ndef _parse_json_output(text: str) -> list[dict]:\n    \"\"\"从模型输出中解析 JSON 列表。\"\"\"\n    try:\n        return json.loads(text)\n    except json.JSONDecodeError:\n        start = text.find(\"[\")\n        end = text.rfind(\"]\") + 1\n        if start >= 0 and end > start:\n            try:\n                return json.loads(text[start:end])\n            except json.JSONDecodeError:\n                return []\n    return []\n\n\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n    \"\"\"格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。\"\"\"\n    rewards = []\n    for text in completions:\n        parsed = _parse_json_output(text)\n        if not isinstance(parsed, list):\n            rewards.append(0.0)\n            continue\n        if not parsed:\n            rewards.append(0.1)\n            continue\n        valid = 0\n        for item in parsed:\n            if (isinstance(item, dict) and \"head\" in item\n                    and \"relation\" in item and \"tail\" in item\n                    and \"evidence\" in item\n                    and isinstance(item[\"evidence\"], list)):\n                valid += 1\n        rewards.append(valid / len(parsed))\n    return rewards\n\n\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n    \"\"\"F1 奖励: 预测三元组与 gold 三元组的 micro-F1。\n\n    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。\n    completions 中每 num_generations 个对应同一个 prompt。\n    \"\"\"\n    num_gen = len(completions) // len(gold_triples)\n    rewards = []\n\n    for i, text in enumerate(completions):\n        gold_idx = i // num_gen\n        gold_str = gold_triples[gold_idx]\n        try:\n            gold = json.loads(gold_str)\n        except (json.JSONDecodeError, IndexError):\n            rewards.append(0.0)\n            continue\n\n        pred = _parse_json_output(text)\n\n        gold_set = set()\n        for g in gold:\n            gold_set.add((\n                g.get(\"head\", \"\").lower().strip(),\n                g.get(\"relation\", \"\").lower().strip(),\n                g.get(\"tail\", \"\").lower().strip(),\n            ))\n\n        pred_set = set()\n        for p in pred:\n            if isinstance(p, dict):\n                pred_set.add((\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                ))\n\n        if not gold_set:\n            rewards.append(1.0 if not pred_set else 0.0)\n            continue\n\n        tp = len(pred_set & gold_set)\n        prec = tp / len(pred_set) if pred_set else 0.0\n        rec = tp / len(gold_set) if gold_set else 0.0\n        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0\n        rewards.append(f1)\n\n    return rewards\n\n\nclass CEDRewardWrapper:\n    \"\"\"将 CED 奖励封装为 GRPO 兼容的 reward function。\n\n    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，\n    返回所有 triples 的平均 CED reward。\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model: str = \"cross-encoder/nli-deberta-v3-base\",\n        tau: float = 0.5,\n        mode: str = \"ced\",\n        device: str = None,\n        tau_start: float = None,\n        tau_end: float = None,\n        total_steps: int = None,\n    ):\n        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple\n        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)\n        self.verbalize = verbalize_triple\n        self.mode = mode\n        self._call_count = 0\n        if tau_start is not None and tau_end is not None:\n            self.tau_start = tau_start\n            self.tau_end = tau_end\n            self.total_steps = total_steps\n        else:\n            self.tau_start = tau\n            self.tau_end = tau\n            self.total_steps = None\n\n    @property\n    def tau(self) -> float:\n        if self.total_steps and self.total_steps > 0:\n            progress = min(self._call_count / self.total_steps, 1.0)\n        else:\n            progress = 1.0\n        return self.tau_start + (self.tau_end - self.tau_start) * progress\n\n    def __call__(\n        self,\n        completions: list[str],\n        all_sents: list[str],\n        gold_triples: list[str],\n        **kwargs,\n    ) -> list[float]:\n        \"\"\"计算 CED/flat-NLI 奖励。\n\n        all_sents: JSON 字符串列表，每个元素为文档句子列表。\n        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。\n        \"\"\"\n        current_tau = self.tau\n        self._call_count += 1\n        num_gen = len(completions) // len(all_sents)\n        rewards = []\n\n        for i, text in enumerate(completions):\n            prompt_idx = i // num_gen\n            try:\n                sents = json.loads(all_sents[prompt_idx])\n                gold = json.loads(gold_triples[prompt_idx])\n            except (json.JSONDecodeError, IndexError):\n                rewards.append(0.0)\n                continue\n\n            pred = _parse_json_output(text)\n            if not pred:\n                rewards.append(0.0)\n                continue\n\n            gold_map = {}\n            for g in gold:\n                key = (\n                    g.get(\"head\", \"\").lower().strip(),\n                    g.get(\"relation\", \"\").lower().strip(),\n                    g.get(\"tail\", \"\").lower().strip(),\n                )\n                gold_map[key] = g\n\n            triple_rewards = []\n            for p in pred:\n                if not isinstance(p, dict):\n                    continue\n                pred_evi_ids = p.get(\"evidence\", [])\n                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:\n                    triple_rewards.append(0.0)\n                    continue\n\n                claim = self.verbalize(\n                    p.get(\"head\", \"\"),\n                    p.get(\"relation\", \"\"),\n                    p.get(\"tail\", \"\"),\n                )\n                cited_sents = [sents[idx] for idx in pred_evi_ids\n                               if isinstance(idx, int) and 0 <= idx < len(sents)]\n                if not cited_sents:\n                    triple_rewards.append(0.0)\n                    continue\n\n                key = (\n                    p.get(\"head\", \"\").lower().strip(),\n                    p.get(\"relation\", \"\").lower().strip(),\n                    p.get(\"tail\", \"\").lower().strip(),\n                )\n                matched_gold = gold_map.get(key, {})\n                hard_neg_ids = matched_gold.get(\"hard_negative_sent_ids\", [])\n                hard_neg_sents = [sents[idx] for idx in hard_neg_ids\n                                  if isinstance(idx, int) and 0 <= idx < len(sents)]\n\n                if self.mode == \"flat_nli\":\n                    result = self.reward_model.compute_flat_nli_reward(\n                        claim, cited_sents, tau=current_tau,\n                    )\n                else:\n                    result = self.reward_model.compute_ced_reward(\n                        claim, cited_sents, hard_neg_sents, tau=current_tau,\n                    )\n                triple_rewards.append(result[\"reward\"])\n\n            rewards.append(\n                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0\n            )\n\n        return rewards\n\n\ndef prepare_grpo_dataset(\n    data_dir: str = None,\n    split: str = \"train\",\n    tokenizer=None,\n) -> Dataset:\n    \"\"\"准备 GRPO prompt 数据集。\n\n    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。\n    \"\"\"\n    from freige.data.docred_processor import DocREDProcessor\n\n    processor = DocREDProcessor(data_dir=data_dir)\n    samples = processor.process(split)\n    groups = processor.group_by_document(samples)\n\n    dataset_items = []\n    for doc_id, doc_samples in groups.items():\n        sft_sample = processor.format_sft_sample(doc_samples)\n        messages = [\n            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n            {\"role\": \"user\", \"content\": f\"{sft_sample['instruction']}\\n\\n{sft_sample['input']}\"},\n        ]\n        prompt = tokenizer.apply_chat_template(\n            messages,\n            tokenize=False,\n            add_generation_prompt=True,\n            enable_thinking=False,\n        )\n\n        gold_triples = []\n        for s in doc_samples:\n            gold_triples.append({\n                \"head\": s.head.name,\n                \"relation\": s.relation_name,\n                \"tail\": s.tail.name,\n                \"evidence\": s.evidence_sent_ids,\n                \"hard_negative_sent_ids\": s.hard_negative_sent_ids,\n            })\n\n        ref = doc_samples[0]\n        dataset_items.append({\n            \"prompt\": prompt,\n            \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n            \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n        })\n\n    logger.info(\"Prepared %d GRPO prompts\", len(dataset_items))\n    return Dataset.from_list(dataset_items)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"FREIGE GRPO Training\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/models/Qwen3-4B\",\n                        help=\"基础模型或 SFT checkpoint 路径\")\n    parser.add_argument(\"--sft_adapter\", type=str, default=None,\n                        help=\"SFT LoRA adapter 路径（如果与 model_name 不同）\")\n    parser.add_argument(\"--data_dir\", type=str, default=None)\n    parser.add_argument(\"--output_dir\", type=str, default=\"./grpo_output\")\n    parser.add_argument(\"--stage\", type=int, default=1, choices=[1, 2, 3],\n                        help=\"Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED\")\n    parser.add_argument(\"--nli_model\", type=str, default=\"cross-encoder/nli-deberta-v3-base\")\n    parser.add_argument(\"--num_generations\", type=int, default=4)\n    parser.add_argument(\"--lora_rank\", type=int, default=64)\n    parser.add_argument(\"--lora_alpha\", type=int, default=128)\n    parser.add_argument(\"--max_length\", type=int, default=4096)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=1024)\n    parser.add_argument(\"--quantize\", action=argparse.BooleanOptionalAction, default=True,\n                        help=\"启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）\")\n    parser.add_argument(\"--deepspeed\", type=str, default=None,\n                        help=\"DeepSpeed 配置文件路径\")\n    parser.add_argument(\"--reward_device\", type=str, default=\"cpu\",\n                        help=\"CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=1)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=16)\n    parser.add_argument(\"--num_epochs\", type=int, default=1)\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5)\n    parser.add_argument(\"--tau_start\", type=float, default=0.3,\n                        help=\"CED tau 初始值\")\n    parser.add_argument(\"--tau_end\", type=float, default=0.5,\n                        help=\"CED tau 最终值（线性调度）\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb_project\", type=str, default=\"freige-grpo\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None)\n    args = parser.parse_args()\n\n    if args.wandb_project and \"WANDB_API_KEY\" in os.environ:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n        if args.wandb_run_name:\n            os.environ[\"WANDB_NAME\"] = args.wandb_run_name\n\n    logger.info(\"Loading tokenizer: %s\", args.model_name)\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name,\n        trust_remote_code=True,\n        padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing dataset...\")\n    train_dataset = prepare_grpo_dataset(\n        data_dir=args.data_dir,\n        split=\"train\",\n        tokenizer=tokenizer,\n    )\n\n    logger.info(\"Loading model: %s\", args.model_name)\n    model_kwargs = dict(\n        trust_remote_code=True,\n        attn_implementation=\"sdpa\",\n    )\n    if args.quantize:\n        logger.info(\"Using 4-bit QLoRA quantization\")\n        model_kwargs[\"quantization_config\"] = BitsAndBytesConfig(\n            load_in_4bit=True,\n            bnb_4bit_compute_dtype=torch.bfloat16,\n            bnb_4bit_quant_type=\"nf4\",\n            bnb_4bit_use_double_quant=True,\n        )\n    else:\n        model_kwargs[\"torch_dtype\"] = torch.bfloat16 if args.bf16 else torch.float16\n    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)\n\n    if args.sft_adapter:\n        logger.info(\"Loading SFT adapter from %s\", args.sft_adapter)\n        model = PeftModel.from_pretrained(model, args.sft_adapter)\n        model = model.merge_and_unload()\n\n    reward_fns = [format_reward_fn, f1_reward_fn]\n\n    if args.stage >= 2:\n        mode = \"flat_nli\" if args.stage == 2 else \"ced\"\n        steps_per_epoch = math.ceil(\n            len(train_dataset) / (args.per_device_batch_size * args.gradient_accumulation_steps)\n        )\n        total_steps = steps_per_epoch * args.num_epochs\n        ced_wrapper = CEDRewardWrapper(\n            nli_model=args.nli_model,\n            mode=mode,\n            device=args.reward_device,\n            tau_start=args.tau_start,\n            tau_end=args.tau_end,\n            total_steps=total_steps,\n        )\n        reward_fns.append(ced_wrapper)\n        logger.info(\n            \"Stage %d: using %s reward, tau %.2f→%.2f over %d steps\",\n            args.stage, mode, args.tau_start, args.tau_end, total_steps,\n        )\n    else:\n        logger.info(\"Stage 1: extraction-only (format + F1 rewards)\")\n\n    lora_config = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=0.05,\n        target_modules=[\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                         \"gate_proj\", \"up_proj\", \"down_proj\"],\n    )\n\n    grpo_config = GRPOConfig(\n        output_dir=args.output_dir,\n        num_train_epochs=args.num_epochs,\n        per_device_train_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        bf16=args.bf16,\n        logging_steps=5,\n        save_strategy=\"epoch\",\n        save_total_limit=2,\n        seed=args.seed,\n        num_generations=args.num_generations,\n        max_completion_length=args.max_new_tokens,\n        report_to=\"wandb\" if \"WANDB_API_KEY\" in os.environ else \"none\",\n        gradient_checkpointing=True,\n        gradient_checkpointing_kwargs={\"use_reentrant\": False},\n        deepspeed=args.deepspeed,\n    )\n\n    trainer = GRPOTrainer(\n        model=model,\n        args=grpo_config,\n        train_dataset=train_dataset,\n        reward_funcs=reward_fns,\n        peft_config=lora_config,\n        processing_class=tokenizer,\n    )\n\n    logger.info(\"Starting GRPO training (stage %d)...\", args.stage)\n    trainer.train()\n\n    logger.info(\"Saving model to %s\", args.output_dir)\n    trainer.save_model(args.output_dir)\n    tokenizer.save_pretrained(args.output_dir)\n    logger.info(\"GRPO training (stage %d) complete.\", args.stage)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 452,
      "startLine": 1,
      "totalLines": 452
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01K66wfwh35rPGLkSWYG2a4z`</summary>

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
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "b6433bc6-8f43-4aa3-99e5-e0ee28cd77fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YaZzP5dKJAdWRHMKepgZVC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12289,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12289
      },
      "output_tokens": 7,
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

_source line 8 · 2026-05-14T07:00:49.661Z_

<details><summary>↩ Tool result · `toolu_01K66wfwh35rPGLkSWYG2a4z`</summary>

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
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "e18876be-e20e-43db-ac88-387edc336d69",
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

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_0176gxTRLKNXfFbFq8rgYVpx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/configs/deepspeed_zero2.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "d98b6e33-c014-4a37-9aad-c43b9fcb262d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YaZzP5dKJAdWRHMKepgZVC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12289,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12289
      },
      "output_tokens": 7,
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

_source line 10 · 2026-05-14T07:00:49.948Z_

<details><summary>↩ Tool result · `toolu_0176gxTRLKNXfFbFq8rgYVpx`</summary>

```text
1	{
2	  "bf16": {"enabled": true},
3	  "zero_optimization": {
4	    "stage": 2,
5	    "offload_optimizer": {"device": "cpu", "pin_memory": true},
6	    "allgather_partitions": true,
7	    "allgather_bucket_size": 2e8,
8	    "overlap_comm": true,
9	    "reduce_scatter": true,
10	    "reduce_bucket_size": 2e8,
11	    "contiguous_gradients": true
12	  },
13	  "gradient_accumulation_steps": "auto",
14	  "gradient_clipping": "auto",
15	  "train_batch_size": "auto",
16	  "train_micro_batch_size_per_gpu": "auto"
17	}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "48233c75-19dd-4bc9-9de5-15708def1ab9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/configs/deepspeed_zero2.json",
      "content": "{\n  \"bf16\": {\"enabled\": true},\n  \"zero_optimization\": {\n    \"stage\": 2,\n    \"offload_optimizer\": {\"device\": \"cpu\", \"pin_memory\": true},\n    \"allgather_partitions\": true,\n    \"allgather_bucket_size\": 2e8,\n    \"overlap_comm\": true,\n    \"reduce_scatter\": true,\n    \"reduce_bucket_size\": 2e8,\n    \"contiguous_gradients\": true\n  },\n  \"gradient_accumulation_steps\": \"auto\",\n  \"gradient_clipping\": \"auto\",\n  \"train_batch_size\": \"auto\",\n  \"train_micro_batch_size_per_gpu\": \"auto\"\n}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now let me check the TRL 1.1.0 GRPOTrainer behavior regarding how extra dataset columns are passed to reward functions. This is a critical question.

Let me also check if there's an accelerate config file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "10616ff2-9982-4d9d-bc3d-47212e3dc043",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lo31m6eHRFxkN2yvxG5pRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11515,
      "cache_read_input_tokens": 24130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11515
      },
      "output_tokens": 9,
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

_source line 12_

Let me check the accelerate config and TRL's reward function column-passing mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "59e4bba6-95c8-4763-835b-2f122a9d0ea9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lo31m6eHRFxkN2yvxG5pRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11515,
      "cache_read_input_tokens": 24130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11515
      },
      "output_tokens": 9,
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

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_01RDwrCM4yweZHF89GMbhM6M`</summary>

```json
{
  "pattern": "**/accelerate_4gpu.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "1b8c3fd3-3dcf-436f-84fb-12cac5fa345e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lo31m6eHRFxkN2yvxG5pRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11515,
      "cache_read_input_tokens": 24130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11515
      },
      "output_tokens": 9,
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

_source line 14 · 2026-05-14T07:00:57.944Z_

<details><summary>↩ Tool result · `toolu_01RDwrCM4yweZHF89GMbhM6M`</summary>

```text
artifacts/freige/configs/accelerate_4gpu.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "cfca0029-f59d-4e65-a671-1b6d7adace64",
  "tool_use_result": {
    "filenames": [
      "artifacts/freige/configs/accelerate_4gpu.yaml"
    ],
    "durationMs": 16,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Agent · `toolu_01G9kqGcKusX9a1cBvN8GPbC`</summary>

```json
{
  "description": "TRL 1.1.0 GRPO reward kwargs",
  "subagent_type": "Explore",
  "prompt": "I need to understand how TRL 1.1.0's GRPOTrainer passes extra dataset columns to reward functions.\n\nSpecifically: if the training dataset has columns beyond \"prompt\" (e.g., \"gold_triples\", \"all_sents\"), does GRPOTrainer automatically pass them as **kwargs to reward_funcs?\n\nSearch in the installed TRL package for how GRPOTrainer calls reward functions. Look at:\n1. The GRPOTrainer source code — find where reward_funcs are called during training\n2. Check if there's logic that collects non-standard dataset columns and passes them as kwargs to the reward functions\n3. Look for any \"reward_func_columns\" or similar mechanism\n\nSearch broadly — check /home/ubuntu/.agent-ml-research-idea_gen_0513_6/ and also any pip-installed trl package. Try `pip show trl` output or look in common venv/site-packages paths.\n\nReport: does TRL 1.1.0 GRPOTrainer automatically forward extra dataset columns to reward functions as kwargs? If yes, how exactly? If no, what's the mechanism?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "d196222a-a677-4f16-9bd8-9769b6df21fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lo31m6eHRFxkN2yvxG5pRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11515,
      "cache_read_input_tokens": 24130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11515
      },
      "output_tokens": 9,
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

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "TRL 1.1.0 GRPO reward kwargs",
  "task_type": "local_agent",
  "prompt": "I need to understand how TRL 1.1.0's GRPOTrainer passes extra dataset columns to reward functions.\n\nSpecifically: if the training dataset has columns beyond \"prompt\" (e.g., \"gold_triples\", \"all_sents\"), does GRPOTrainer automatically pass them as **kwargs to reward_funcs?\n\nSearch in the installed TRL package for how GRPOTrainer calls reward functions. Look at:\n1. The GRPOTrainer source code — find where reward_funcs are called during training\n2. Check if there's logic that collects non-standard dataset columns and passes them as kwargs to the reward functions\n3. Look for any \"reward_func_columns\" or similar mechanism\n\nSearch broadly — check /home/ubuntu/.agent-ml-research-idea_gen_0513_6/ and also any pip-installed trl package. Try `pip show trl` output or look in common venv/site-packages paths.\n\nReport: does TRL 1.1.0 GRPOTrainer automatically forward extra dataset columns to reward functions as kwargs? If yes, how exactly? If no, what's the mechanism?",
  "uuid": "54f8e207-36ab-4297-a54e-c1b6ca2ba68e",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

## Round 1

65 recorded events

### User

_source line 17 · 2026-05-14T07:01:05.643Z_

I need to understand how TRL 1.1.0's GRPOTrainer passes extra dataset columns to reward functions.

Specifically: if the training dataset has columns beyond "prompt" (e.g., "gold_triples", "all_sents"), does GRPOTrainer automatically pass them as **kwargs to reward_funcs?

Search in the installed TRL package for how GRPOTrainer calls reward functions. Look at:
1. The GRPOTrainer source code — find where reward_funcs are called during training
2. Check if there's logic that collects non-standard dataset columns and passes them as kwargs to the reward functions
3. Look for any "reward_func_columns" or similar mechanism

Search broadly — check /home/ubuntu/.agent-ml-research-idea_gen_0513_6/ and also any pip-installed trl package. Try `pip show trl` output or look in common venv/site-packages paths.

Report: does TRL 1.1.0 GRPOTrainer automatically forward extra dataset columns to reward functions as kwargs? If yes, how exactly? If no, what's the mechanism?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "3675114b-065c-4c1b-b584-9d42ed6c6da4"
}
```

</details>

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Running pip show trl",
  "usage": {
    "total_tokens": 18024,
    "tool_uses": 1,
    "duration_ms": 1380
  },
  "last_tool_name": "Bash",
  "uuid": "00b24336-ba2f-442e-8d25-261031d0095c",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mckrh4tCpHaZzawsWJ9qwo`</summary>

```json
{
  "command": "pip show trl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "068d2721-d476-4cf9-bc8d-af0a8600ef0d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LAqVhX7Zo1FQT5JUaXyHii",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18015,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18015,
        "ephemeral_1h_input_tokens": 0
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

_source line 20 · 2026-05-14T07:01:07.785Z_

<details><summary>↩ Tool result · reported error · `toolu_01Mckrh4tCpHaZzawsWJ9qwo`</summary>

```text
Exit code 1
WARNING: Package(s) not found: trl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "4e616a36-8f6d-43bb-8048-9a407b6c36fe",
  "tool_use_result": "Error: Exit code 1\nWARNING: Package(s) not found: trl"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Running python3 -c \"import trl; print(trl.__file__)\"",
  "usage": {
    "total_tokens": 18992,
    "tool_uses": 2,
    "duration_ms": 4107
  },
  "last_tool_name": "Bash",
  "uuid": "5100b01c-7b0a-4684-b6d0-99d658ba8495",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_019CkrptupdmfYaRT1uyWnTL`</summary>

```json
{
  "command": "python3 -c \"import trl; print(trl.__file__)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "2efd4bec-ca81-4ceb-bf58-0268b6ec9c2f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEF7dG1PyZ3vapBEq6dQE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 962,
      "cache_read_input_tokens": 18015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 962,
        "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-14T07:01:10.007Z_

<details><summary>↩ Tool result · reported error · `toolu_019CkrptupdmfYaRT1uyWnTL`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 1, in &lt;module>
    import trl; print(trl.__file__)
    ^^^^^^^^^^
ModuleNotFoundError: No module named 'trl'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "43eb90dd-7ed3-4aed-9b72-45906a7bf93c",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 1, in &lt;module>\n    import trl; print(trl.__file__)\n    ^^^^^^^^^^\nModuleNotFoundError: No module named 'trl'"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Running find /home/ubuntu -name \"*grpo*\" -type f 2>/dev/n…",
  "usage": {
    "total_tokens": 19159,
    "tool_uses": 3,
    "duration_ms": 6007
  },
  "last_tool_name": "Bash",
  "uuid": "40c5c40e-b592-48eb-be7a-708816069826",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_016jdigK1hmTQ4EYfhqDheuQ`</summary>

```json
{
  "command": "find /home/ubuntu -name \"*grpo*\" -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "36eefd7e-3a56-47a1-844b-d3f5287ac0de",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ETV9M5ak9BrGQEpbu2xoc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 165,
      "cache_read_input_tokens": 18977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 165,
        "ephemeral_1h_input_tokens": 0
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

_source line 26 · 2026-05-14T07:01:11.961Z_

<details><summary>↩ Tool result · `toolu_016jdigK1hmTQ4EYfhqDheuQ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/logs/workers/worker_code_grpo-readiness-check_20260514T070038.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/checkpoints/smoke_test_grpo_ALLOCATED_20260514T052256.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/checkpoints/smoke_test_grpo_DONE_20260514T060918.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/checkpoints/smoke_test_grpo_RUNNING_20260514T052302.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/checkpoints/smoke_test_grpo_RUNNING_20260514T054402.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/checkpoints/smoke_test_grpo_PREPARING_20260514T052000.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/checkpoints/smoke_test_grpo_QUEUED_20260514T052252.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/checkpoints/smoke_test_grpo_RUNNING_20260514T060913.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/__pycache__/grpo_trainer.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "f8340ec2-c0ac-4616-ae3e-1c31bea4266e"
}
```

</details>

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Reading artifacts/freige/training/grpo_trainer.py",
  "usage": {
    "total_tokens": 19758,
    "tool_uses": 4,
    "duration_ms": 7744
  },
  "last_tool_name": "Read",
  "uuid": "8fd56bd3-03bc-4b4c-af6c-9d1f80c857df",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01C6TKb1qZfUaTfYmnndHxvE`</summary>

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
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "4f0ec577-4adc-4111-9938-f902174b1fee",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XJKuymFg1jGcB5C4ojdQHr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 598,
      "cache_read_input_tokens": 19142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 598,
        "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-14T07:01:13.396Z_

<details><summary>↩ Tool result · `toolu_01C6TKb1qZfUaTfYmnndHxvE`</summary>

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
13	import json
14	import logging
15	import math
16	import os
17	import re
18	from pathlib import Path
19	from typing import Optional
20	
21	import torch
22	from datasets import Dataset
23	from peft import LoraConfig, PeftModel, TaskType
24	from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
25	from trl import GRPOConfig, GRPOTrainer
26	
27	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
28	logger = logging.getLogger(__name__)
29	
30	SYSTEM_PROMPT = (
31	    "You are an information extraction model. Given a document with numbered sentences "
32	    "and a list of entities, extract all relation triples. For each triple, provide the "
33	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
34	    "Output as a JSON list."
35	)
36	
37	
38	def _parse_json_output(text: str) -> list[dict]:
39	    """从模型输出中解析 JSON 列表。"""
40	    try:
41	        return json.loads(text)
42	    except json.JSONDecodeError:
43	        start = text.find("[")
44	        end = text.rfind("]") + 1
45	        if start >= 0 and end > start:
46	            try:
47	                return json.loads(text[start:end])
48	            except json.JSONDecodeError:
49	                return []
50	    return []
51	
52	
53	def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
54	    """格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。"""
55	    rewards = []
56	    for text in completions:
57	        parsed = _parse_json_output(text)
58	        if not isinstance(parsed, list):
59	            rewards.append(0.0)
60	            continue
61	        if not parsed:
62	            rewards.append(0.1)
63	            continue
64	        valid = 0
65	        for item in parsed:
66	            if (isinstance(item, dict) and "head" in item
67	                    and "relation" in item and "tail" in item
68	                    and "evidence" in item
69	                    and isinstance(item["evidence"], list)):
70	                valid += 1
71	        rewards.append(valid / len(parsed))
72	    return rewards
73	
74	
75	def f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:
76	    """F1 奖励: 预测三元组与 gold 三元组的 micro-F1。
77	
78	    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。
79	    completions 中每 num_generations 个对应同一个 prompt。
80	    """
81	    num_gen = len(completions) // len(gold_triples)
82	    rewards = []
83	
84	    for i, text in enumerate(completions):
85	        gold_idx = i // num_gen
86	        gold_str = gold_triples[gold_idx]
87	        try:
88	            gold = json.loads(gold_str)
89	        except (json.JSONDecodeError, IndexError):
90	            rewards.append(0.0)
91	            continue
92	
93	        pred = _parse_json_output(text)
94	
95	        gold_set = set()
96	        for g in gold:
97	            gold_set.add((
98	                g.get("head", "").lower().strip(),
99	                g.get("relation", "").lower().strip(),
100	                g.get("tail", "").lower().strip(),
101	            ))
102	
103	        pred_set = set()
104	        for p in pred:
105	            if isinstance(p, dict):
106	                pred_set.add((
107	                    p.get("head", "").lower().strip(),
108	                    p.get("relation", "").lower().strip(),
109	                    p.get("tail", "").lower().strip(),
110	                ))
111	
112	        if not gold_set:
113	            rewards.append(1.0 if not pred_set else 0.0)
114	            continue
115	
116	        tp = len(pred_set & gold_set)
117	        prec = tp / len(pred_set) if pred_set else 0.0
118	        rec = tp / len(gold_set) if gold_set else 0.0
119	        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
120	        rewards.append(f1)
121	
122	    return rewards
123	
124	
125	class CEDRewardWrapper:
126	    """将 CED 奖励封装为 GRPO 兼容的 reward function。
127	
128	    对每个 completion 解析 triples + evidence，用 CED 模型计算奖励，
129	    返回所有 triples 的平均 CED reward。
130	    """
131	
132	    def __init__(
133	        self,
134	        nli_model: str = "cross-encoder/nli-deberta-v3-base",
135	        tau: float = 0.5,
136	        mode: str = "ced",
137	        device: str = None,
138	        tau_start: float = None,
139	        tau_end: float = None,
140	        total_steps: int = None,
141	    ):
142	        from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple
143	        self.reward_model = CEDRewardModel(model_name=nli_model, device=device)
144	        self.verbalize = verbalize_triple
145	        self.mode = mode
146	        self._call_count = 0
147	        if tau_start is not None and tau_end is not None:
148	            self.tau_start = tau_start
149	            self.tau_end = tau_end
150	            self.total_steps = total_steps
151	        else:
152	            self.tau_start = tau
153	            self.tau_end = tau
154	            self.total_steps = None
155	
156	    @property
157	    def tau(self) -> float:
158	        if self.total_steps and self.total_steps > 0:
159	            progress = min(self._call_count / self.total_steps, 1.0)
160	        else:
161	            progress = 1.0
162	        return self.tau_start + (self.tau_end - self.tau_start) * progress
163	
164	    def __call__(
165	        self,
166	        completions: list[str],
167	        all_sents: list[str],
168	        gold_triples: list[str],
169	        **kwargs,
170	    ) -> list[float]:
171	        """计算 CED/flat-NLI 奖励。
172	
173	        all_sents: JSON 字符串列表，每个元素为文档句子列表。
174	        gold_triples: JSON 字符串列表，含 evidence_sent_ids 和 hard_negative_sent_ids。
175	        """
176	        current_tau = self.tau
177	        self._call_count += 1
178	        num_gen = len(completions) // len(all_sents)
179	        rewards = []
180	
181	        for i, text in enumerate(completions):
182	            prompt_idx = i // num_gen
183	            try:
184	                sents = json.loads(all_sents[prompt_idx])
185	                gold = json.loads(gold_triples[prompt_idx])
186	            except (json.JSONDecodeError, IndexError):
187	                rewards.append(0.0)
188	                continue
189	
190	            pred = _parse_json_output(text)
191	            if not pred:
192	                rewards.append(0.0)
193	                continue
194	
195	            gold_map = {}
196	            for g in gold:
197	                key = (
198	                    g.get("head", "").lower().strip(),
199	                    g.get("relation", "").lower().strip(),
200	                    g.get("tail", "").lower().strip(),
201	                )
202	                gold_map[key] = g
203	
204	            triple_rewards = []
205	            for p in pred:
206	                if not isinstance(p, dict):
207	                    continue
208	                pred_evi_ids = p.get("evidence", [])
209	                if not isinstance(pred_evi_ids, list) or not pred_evi_ids:
210	                    triple_rewards.append(0.0)
211	                    continue
212	
213	                claim = self.verbalize(
214	                    p.get("head", ""),
215	                    p.get("relation", ""),
216	                    p.get("tail", ""),
217	                )
218	                cited_sents = [sents[idx] for idx in pred_evi_ids
219	                               if isinstance(idx, int) and 0 <= idx < len(sents)]
220	                if not cited_sents:
221	                    triple_rewards.append(0.0)
222	                    continue
223	
224	                key = (
225	                    p.get("head", "").lower().strip(),
226	                    p.get("relation", "").lower().strip(),
227	                    p.get("tail", "").lower().strip(),
228	                )
229	                matched_gold = gold_map.get(key, {})
230	                hard_neg_ids = matched_gold.get("hard_negative_sent_ids", [])
231	                hard_neg_sents = [sents[idx] for idx in hard_neg_ids
232	                                  if isinstance(idx, int) and 0 <= idx < len(sents)]
233	
234	                if self.mode == "flat_nli":
235	                    result = self.reward_model.compute_flat_nli_reward(
236	                        claim, cited_sents, tau=current_tau,
237	                    )
238	                else:
239	                    result = self.reward_model.compute_ced_reward(
240	                        claim, cited_sents, hard_neg_sents, tau=current_tau,
241	                    )
242	                triple_rewards.append(result["reward"])
243	
244	            rewards.append(
245	                sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0
246	            )
247	
248	        return rewards
249	
250	
251	def prepare_grpo_dataset(
252	    data_dir: str = None,
253	    split: str = "train",
254	    tokenizer=None,
255	) -> Dataset:
256	    """准备 GRPO prompt 数据集。
257	
258	    每个样本包含 prompt（文档 + 指令）和 gold 信息（用于 reward 计算）。
259	    """
260	    from freige.data.docred_processor import DocREDProcessor
261	
262	    processor = DocREDProcessor(data_dir=data_dir)
263	    samples = processor.process(split)
264	    groups = processor.group_by_document(samples)
265	
266	    dataset_items = []
267	    for doc_id, doc_samples in groups.items():
268	        sft_sample = processor.format_sft_sample(doc_samples)
269	        messages = [
270	            {"role": "system", "content": SYSTEM_PROMPT},
271	            {"role": "user", "content": f"{sft_sample['instruction']}\n\n{sft_sample['input']}"},
272	        ]
273	        prompt = tokenizer.apply_chat_template(
274	            messages,
275	            tokenize=False,
276	            add_generation_prompt=True,
277	            enable_thinking=False,
278	        )
279	
280	        gold_triples = []
281	        for s in doc_samples:
282	            gold_triples.append({
283	                "head": s.head.name,
284	                "relation": s.relation_name,
285	                "tail": s.tail.name,
286	                "evidence": s.evidence_sent_ids,
287	                "hard_negative_sent_ids": s.hard_negative_sent_ids,
288	            })
289	
290	        ref = doc_samples[0]
291	        dataset_items.append({
292	            "prompt": prompt,
293	            "gold_triples": json.dumps(gold_triples, ensure_ascii=False),
294	            "all_sents": json.dumps(ref.sents, ensure_ascii=False),
295	        })
296	
297	    logger.info("Prepared %d GRPO prompts", len(dataset_items))
298	    return Dataset.from_list(dataset_items)
299	
300	
301	def main():
302	    parser = argparse.ArgumentParser(description="FREIGE GRPO Training")
303	    parser.add_argument("--model_name", type=str, default="/root/autodl-tmp/models/Qwen3-4B",
304	                        help="基础模型或 SFT checkpoint 路径")
305	    parser.add_argument("--sft_adapter", type=str, default=None,
306	                        help="SFT LoRA adapter 路径（如果与 model_name 不同）")
307	    parser.add_argument("--data_dir", type=str, default=None)
308	    parser.add_argument("--output_dir", type=str, default="./grpo_output")
309	    parser.add_argument("--stage", type=int, default=1, choices=[1, 2, 3],
310	                        help="Curriculum 阶段: 1=extraction-only, 2=flat-NLI, 3=CED")
311	    parser.add_argument("--nli_model", type=str, default="cross-encoder/nli-deberta-v3-base")
312	    parser.add_argument("--num_generations", type=int, default=4)
313	    parser.add_argument("--lora_rank", type=int, default=64)
314	    parser.add_argument("--lora_alpha", type=int, default=128)
315	    parser.add_argument("--max_length", type=int, default=4096)
316	    parser.add_argument("--max_new_tokens", type=int, default=1024)
317	    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction, default=True,
318	                        help="启用 4-bit QLoRA 量化（默认启用，--no_quantize 禁用）")
319	    parser.add_argument("--deepspeed", type=str, default=None,
320	                        help="DeepSpeed 配置文件路径")
321	    parser.add_argument("--reward_device", type=str, default="cpu",
322	                        help="CED reward 模型运行设备（默认 CPU，DeBERTa ~400MB 延迟可接受）")
323	    parser.add_argument("--per_device_batch_size", type=int, default=1)
324	    parser.add_argument("--gradient_accumulation_steps", type=int, default=16)
325	    parser.add_argument("--num_epochs", type=int, default=1)
326	    parser.add_argument("--learning_rate", type=float, default=5e-5)
327	    parser.add_argument("--tau_start", type=float, default=0.3,
328	                        help="CED tau 初始值")
329	    parser.add_argument("--tau_end", type=float, default=0.5,
330	                        help="CED tau 最终值（线性调度）")
331	    parser.add_argument("--bf16", action="store_true", default=True)
332	    parser.add_argument("--seed", type=int, default=42)
333	    parser.add_argument("--wandb_project", type=str, default="freige-grpo")
334	    parser.add_argument("--wandb_run_name", type=str, default=None)
335	    args = parser.parse_args()
336	
337	    if args.wandb_project and "WANDB_API_KEY" in os.environ:
338	        os.environ["WANDB_PROJECT"] = args.wandb_project
339	        if args.wandb_run_name:
340	            os.environ["WANDB_NAME"] = args.wandb_run_name
341	
342	    logger.info("Loading tokenizer: %s", args.model_name)
343	    tokenizer = AutoTokenizer.from_pretrained(
344	        args.model_name,
345	        trust_remote_code=True,
346	        padding_side="left",
347	    )
348	    if tokenizer.pad_token is None:
349	        tokenizer.pad_token = tokenizer.eos_token
350	
351	    logger.info("Preparing dataset...")
352	    train_dataset = prepare_grpo_dataset(
353	        data_dir=args.data_dir,
354	        split="train",
355	        tokenizer=tokenizer,
356	    )
357	
358	    logger.info("Loading model: %s", args.model_name)
359	    model_kwargs = dict(
360	        trust_remote_code=True,
361	        attn_implementation="sdpa",
362	    )
363	    if args.quantize:
364	        logger.info("Using 4-bit QLoRA quantization")
365	        model_kwargs["quantization_config"] = BitsAndBytesConfig(
366	            load_in_4bit=True,
367	            bnb_4bit_compute_dtype=torch.bfloat16,
368	            bnb_4bit_quant_type="nf4",
369	            bnb_4bit_use_double_quant=True,
370	        )
371	    else:
372	        model_kwargs["torch_dtype"] = torch.bfloat16 if args.bf16 else torch.float16
373	    model = AutoModelForCausalLM.from_pretrained(args.model_name, **model_kwargs)
374	
375	    if args.sft_adapter:
376	        logger.info("Loading SFT adapter from %s", args.sft_adapter)
377	        model = PeftModel.from_pretrained(model, args.sft_adapter)
378	        model = model.merge_and_unload()
379	
380	    reward_fns = [format_reward_fn, f1_reward_fn]
381	
382	    if args.stage >= 2:
383	        mode = "flat_nli" if args.stage == 2 else "ced"
384	        steps_per_epoch = math.ceil(
385	            len(train_dataset) / (args.per_device_batch_size * args.gradient_accumulation_steps)
386	        )
387	        total_steps = steps_per_epoch * args.num_epochs
388	        ced_wrapper = CEDRewardWrapper(
389	            nli_model=args.nli_model,
390	            mode=mode,
391	            device=args.reward_device,
392	            tau_start=args.tau_start,
393	            tau_end=args.tau_end,
394	            total_steps=total_steps,
395	        )
396	        reward_fns.append(ced_wrapper)
397	        logger.info(
398	            "Stage %d: using %s reward, tau %.2f→%.2f over %d steps",
399	            args.stage, mode, args.tau_start, args.tau_end, total_steps,
400	        )
401	    else:
402	        logger.info("Stage 1: extraction-only (format + F1 rewards)")
403	
404	    lora_config = LoraConfig(
405	        task_type=TaskType.CAUSAL_LM,
406	        r=args.lora_rank,
407	        lora_alpha=args.lora_alpha,
408	        lora_dropout=0.05,
409	        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
410	                         "gate_proj", "up_proj", "down_proj"],
411	    )
412	
413	    grpo_config = GRPOConfig(
414	        output_dir=args.output_dir,
415	        num_train_epochs=args.num_epochs,
416	        per_device_train_batch_size=args.per_device_batch_size,
417	        gradient_accumulation_steps=args.gradient_accumulation_steps,
418	        learning_rate=args.learning_rate,
419	        bf16=args.bf16,
420	        logging_steps=5,
421	        save_strategy="epoch",
422	        save_total_limit=2,
423	        seed=args.seed,
424	        num_generations=args.num_generations,
425	        max_completion_length=args.max_new_tokens,
426	        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
427	        gradient_checkpointing=True,
428	        gradient_checkpointing_kwargs={"use_reentrant": False},
429	        deepspeed=args.deepspeed,
430	    )
431	
432	    trainer = GRPOTrainer(
433	        model=model,
434	        args=grpo_config,
435	        train_dataset=train_dataset,
436	        reward_funcs=reward_fns,
437	        peft_config=lora_config,
438	        processing_class=tokenizer,
439	    )
440	
441	    logger.info("Starting GRPO training (stage %d)...", args.stage)
442	    trainer.train()
443	
444	    logger.info("Saving model to %s", args.output_dir)
445	    trainer.save_model(args.output_dir)
446	    tokenizer.save_pretrained(args.output_dir)
447	    logger.info("GRPO training (stage %d) complete.", args.stage)
448	
449	
450	if __name__ == "__main__":
451	    main()
452	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "3b89bb37-f35c-43f7-8f46-e7ebeeb3cb3a"
}
```

</details>

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Running find /usr -name \"grpo*\" -type f 2>/dev/null | gre…",
  "usage": {
    "total_tokens": 26069,
    "tool_uses": 5,
    "duration_ms": 10260
  },
  "last_tool_name": "Bash",
  "uuid": "5e8c384c-4a4f-4b9b-b976-4678ed4ac40b",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01LZDEQJGMNVKY211h2rGsQH`</summary>

```json
{
  "command": "find /usr -name \"grpo*\" -type f 2>/dev/null | grep -E \"\\.(py|txt)$\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "fbbd7fab-039d-4078-9491-9e6b1c4a9dd2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FfbEgfVkQM1C3paRwBCptS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6309,
      "cache_read_input_tokens": 19740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6309,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "boj0hky8s",
  "tool_use_id": "toolu_01LZDEQJGMNVKY211h2rGsQH",
  "description": "find /usr -name \"grpo*\" -type f 2>/dev/null | grep -E \"\\.(py|txt)$\" | head -10",
  "task_type": "local_bash",
  "uuid": "b96a2f4f-a064-4f59-a1b8-e90972fd7ba3",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "boj0hky8s",
  "tool_use_id": "toolu_01LZDEQJGMNVKY211h2rGsQH",
  "status": "completed",
  "output_file": "",
  "summary": "find /usr -name \"grpo*\" -type f 2>/dev/null | grep -E \"\\.(py|txt)$\" | head -10",
  "uuid": "35732d45-44ae-4d9c-9fd0-2772994cbd3c",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool result

_source line 34 · 2026-05-14T07:01:28.536Z_

<details><summary>↩ Tool result · `toolu_01LZDEQJGMNVKY211h2rGsQH`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "4ed6adf5-1344-4131-8ee0-1c85d0e982f3"
}
```

</details>

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Running find / -path \"*site-packages/trl*\" -name \"*.py\" -…",
  "usage": {
    "total_tokens": 26322,
    "tool_uses": 6,
    "duration_ms": 24702
  },
  "last_tool_name": "Bash",
  "uuid": "a793aef0-885e-4264-a9eb-2744554954e8",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_018we7L4NXbTixFUrwX8ARM2`</summary>

```json
{
  "command": "find / -path \"*site-packages/trl*\" -name \"*.py\" -type f 2>/dev/null | grep -i grpo | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "bf389720-bc4e-42c8-a608-b0996c17baae",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J78WMQjzw7VqNTcutRGJPg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 26049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 252,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T07:01:31.538Z_

<details><summary>↩ Tool result · `toolu_018we7L4NXbTixFUrwX8ARM2`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "87cbcc7d-dbd8-43c8-9528-2e96099b32ac"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Running python3 -m pip list | grep -i trl",
  "usage": {
    "total_tokens": 26447,
    "tool_uses": 7,
    "duration_ms": 27542
  },
  "last_tool_name": "Bash",
  "uuid": "cfa1e85b-dd07-4ebb-bbde-7c8913b5748f",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_017qyVv95HvaHFths5PundbV`</summary>

```json
{
  "command": "python3 -m pip list | grep -i trl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "bf6f8da5-7c12-40cf-a396-9548dc1a3cce",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01G7zbejHWsj8ivUgSZbs8j6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 124,
      "cache_read_input_tokens": 26301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 124,
        "ephemeral_1h_input_tokens": 0
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

_source line 40 · 2026-05-14T07:01:34.008Z_

<details><summary>↩ Tool result · `toolu_017qyVv95HvaHFths5PundbV`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "bbf94b91-69d5-428b-bafa-bf76af85bba7"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0513_6/p…",
  "usage": {
    "total_tokens": 26552,
    "tool_uses": 8,
    "duration_ms": 30064
  },
  "last_tool_name": "Glob",
  "uuid": "08ac422f-6d61-495e-b03c-2ecf49924133",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Glob · `toolu_01JvL3AF1sTBGkBR7PqRRygX`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "598441de-b502-485e-87a1-10fd0a32676c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MoCCcQ7o5QGp4mpwEcczGs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 94,
      "cache_read_input_tokens": 26425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 94,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 43 · 2026-05-14T07:01:35.729Z_

<details><summary>↩ Tool result · `toolu_01JvL3AF1sTBGkBR7PqRRygX`</summary>

```text
artifacts/freige/__init__.py
artifacts/freige/data/__init__.py
artifacts/freige/rewards/__init__.py
artifacts/freige/analysis/__init__.py
artifacts/freige/training/__init__.py
artifacts/freige/eval/__init__.py
artifacts/freige/data/docred_processor.py
artifacts/freige/rewards/ced_reward.py
artifacts/freige/eval/evaluator.py
artifacts/freige/analysis/ced_signal_validation.py
artifacts/freige/training/smoke_test.py
artifacts/freige/training/sft_trainer.py
artifacts/freige/training/grpo_trainer.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "9c5a503f-4510-4ee3-afb2-4f3a5ce1a136"
}
```

</details>

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 26828,
    "tool_uses": 9,
    "duration_ms": 31517
  },
  "last_tool_name": "Bash",
  "uuid": "83fa17fe-6774-48f5-89f2-6cec5f02cebf",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_013ocmQUgRmKdVHgopo4eNF9`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie -type f \\( -name \"*.txt\" -o -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.cfg\" -o -name \"*.toml\" \\) 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "33b002bc-94e9-4354-998c-6a29c0cd692d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0179iKyfadsEHY2F3rxcAyTY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 26519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 274,
        "ephemeral_1h_input_tokens": 0
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

_source line 46 · 2026-05-14T07:01:37.230Z_

<details><summary>↩ Tool result · `toolu_013ocmQUgRmKdVHgopo4eNF9`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/_project/intermediate/freige_codebase_manifest.txt
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/configs/accelerate_4gpu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/decisions.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "d4f4c56d-974d-4fb6-a1c5-c490e5320bc7"
}
```

</details>

---

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Running grep -r \"trl\\|GRPOTrainer\\|reward\" /home/ubuntu/.…",
  "usage": {
    "total_tokens": 27172,
    "tool_uses": 10,
    "duration_ms": 33049
  },
  "last_tool_name": "Bash",
  "uuid": "59e111a7-ce30-48a4-8855-30fa854c72dc",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_01DTYv5bihyoxZ8ZwWp7TgEs`</summary>

```json
{
  "command": "grep -r \"trl\\|GRPOTrainer\\|reward\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie --include=\"*.py\" --include=\"*.txt\" --include=\"*.yaml\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "4981bd0a-1a99-4514-9456-a6a76d546e81",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QLhSFNRHLFyQ4ZtXtdseWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 342,
      "cache_read_input_tokens": 26793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 342,
        "ephemeral_1h_input_tokens": 0
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

_source line 49 · 2026-05-14T07:01:38.777Z_

<details><summary>↩ Tool result · `toolu_01DTYv5bihyoxZ8ZwWp7TgEs`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/_project/intermediate/freige_codebase_manifest.txt:- rewards/ced_reward.py (332 lines): DeBERTa-v3-base NLI, verbalize_triple (96 relations), CED/flat-NLI reward, batch 计算
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/_project/intermediate/freige_codebase_manifest.txt:- training/grpo_trainer.py (403 lines): TRL GRPOTrainer, 3-stage curriculum, format+F1+CED rewards, num_generations=4
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:    def compute_ced_reward(
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:            {"reward": float, "p_pos": float, "p_neg": float, "margin": float}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:        reward = max(0.0, margin) * float(p_pos > tau)
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:            "reward": reward,
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:    def compute_ced_reward_batch(
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:            N 个 {"reward", "p_pos", "p_neg", "margin"} 字典
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:            reward = max(0.0, margin) * float(p_pos > tau)
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:                "reward": reward,
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:    def compute_flat_nli_reward(
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:        reward = p_pos * float(p_pos > tau)
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py:        return {"reward": reward, "p_pos": p_pos}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py:from trl import GRPOConfig, GRPOTrainer
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py:def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py:    rewards = []
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py:            rewards.append(0.0)
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py:            rewards.append(0.1)
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py:        rewards.append(valid / len(parsed))
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py:    return rewards
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py:    trainer = GRPOTrainer(
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/smoke_test.py:        reward_funcs=[format_reward_fn],
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py:"""GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py:            --stage 1 --reward_device cpu
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py:from trl import GRPOConfig, GRPOTrainer
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py:def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py:    rewards = []
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py:            rewards.append(0.0)
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py:            rewards.append(0.1)
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py:        rewards.append(valid / len(parsed))
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "77275996-12a5-4d11-acb8-f3468cd983af"
}
```

</details>

---

### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Reading artifacts/freige/training/smoke_test.py",
  "usage": {
    "total_tokens": 29177,
    "tool_uses": 11,
    "duration_ms": 34807
  },
  "last_tool_name": "Read",
  "uuid": "1681824f-975a-4090-9802-d6704543adba",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01GYs613dzZAVcyBJg8ur2mq`</summary>

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
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "ab5e82b0-5197-4bf9-8d32-f11dc435a4b8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015gXvoxv6NA3p1D9Kq6aKgh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 27135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
        "ephemeral_1h_input_tokens": 0
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

_source line 52 · 2026-05-14T07:01:40.484Z_

<details><summary>↩ Tool result · `toolu_01GYs613dzZAVcyBJg8ur2mq`</summary>

```text
1	#!/usr/bin/env python3
2	# Launch:
3	#   accelerate launch --num_processes 4 --mixed_precision bf16 training/smoke_test.py
4	#   deepspeed --num_gpus 4 training/smoke_test.py
5	"""Self-contained GRPO smoke test: QLoRA + DeepSpeed ZeRO-2 on 4xRTX 5090 (32GB).
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
59	            "He developed the theory of relativity while working at the Swiss Patent Office.",
60	            "Einstein later moved to the United States and joined Princeton University.",
61	            "He received the Nobel Prize in Physics in 1921 for his work on the photoelectric effect.",
62	        ],
63	        "entities": ["Albert Einstein", "Ulm", "Germany", "United States", "Princeton University"],
64	        "triples": [
65	            {"head": "Albert Einstein", "relation": "place of birth", "tail": "Ulm", "evidence": [0]},
66	            {"head": "Albert Einstein", "relation": "country of citizenship", "tail": "Germany", "evidence": [0]},
67	            {"head": "Albert Einstein", "relation": "employer", "tail": "Princeton University", "evidence": [2]},
68	        ],
69	    },
70	    {
71	        "sents": [
72	            "The Eiffel Tower is a wrought-iron lattice tower in Paris, France.",
73	            "It was designed by Gustave Eiffel's company and built between 1887 and 1889.",
74	            "The tower is 330 metres tall and the tallest structure in Paris.",
75	            "It has become a global cultural icon of France.",
76	        ],
77	        "entities": ["Eiffel Tower", "Paris", "France", "Gustave Eiffel"],
78	        "triples": [
79	            {"head": "Eiffel Tower", "relation": "located in", "tail": "Paris", "evidence": [0]},
80	            {"head": "Eiffel Tower", "relation": "country", "tail": "France", "evidence": [0, 3]},
81	            {"head": "Eiffel Tower", "relation": "creator", "tail": "Gustave Eiffel", "evidence": [1]},
82	        ],
83	    },
84	    {
85	        "sents": [
86	            "Tokyo is the capital and most populous city of Japan.",
87	            "The Greater Tokyo Area is the most populous metropolitan area in the world.",
88	            "Tokyo was originally known as Edo and was renamed in 1868.",
89	            "The city hosted the Summer Olympics in 1964 and 2021.",
90	        ],
91	        "entities": ["Tokyo", "Japan", "Edo"],
92	        "triples": [
93	            {"head": "Tokyo", "relation": "capital of", "tail": "Japan", "evidence": [0]},
94	            {"head": "Tokyo", "relation": "country", "tail": "Japan", "evidence": [0]},
95	        ],
96	    },
97	    {
98	        "sents": [
99	            "Marie Curie was a Polish-French physicist and chemist.",
100	            "She conducted pioneering research on radioactivity at the University of Paris.",
101	            "Curie was the first woman to win a Nobel Prize in 1903.",
102	            "She won a second Nobel Prize in Chemistry in 1911.",
103	            "Marie Curie was born in Warsaw, Poland.",
104	        ],
105	        "entities": ["Marie Curie", "University of Paris", "Warsaw", "Poland"],
106	        "triples": [
107	            {"head": "Marie Curie", "relation": "employer", "tail": "University of Paris", "evidence": [1]},
108	            {"head": "Marie Curie", "relation": "place of birth", "tail": "Warsaw", "evidence": [4]},
109	            {"head": "Marie Curie", "relation": "country of citizenship", "tail": "Poland", "evidence": [0, 4]},
110	        ],
111	    },
112	    {
113	        "sents": [
114	            "Amazon was founded by Jeff Bezos in Bellevue, Washington on July 5, 1994.",
115	            "The company started as an online bookstore.",
116	            "Amazon's headquarters is located in Seattle, Washington.",
117	            "It is one of the Big Five American technology companies.",
118	        ],
119	        "entities": ["Amazon", "Jeff Bezos", "Bellevue", "Seattle", "Washington"],
120	        "triples": [
121	            {"head": "Amazon", "relation": "founded by", "tail": "Jeff Bezos", "evidence": [0]},
122	            {"head": "Amazon", "relation": "headquarters location", "tail": "Seattle", "evidence": [2]},
123	            {"head": "Amazon", "relation": "location of formation", "tail": "Bellevue", "evidence": [0]},
124	        ],
125	    },
126	]
127	
128	
129	def generate_dummy_dataset(tokenizer, n_samples: int = 20, seed: int = SEED) -> Dataset:
130	    rng = random.Random(seed)
131	    items = []
132	    for i in range(n_samples):
133	        doc = DUMMY_DOCS[i % len(DUMMY_DOCS)]
134	        numbered = "\n".join(f"[{j}] {s}" for j, s in enumerate(doc["sents"]))
135	        entity_str = ", ".join(doc["entities"])
136	        user_msg = (
137	            f"Document:\n{numbered}\n\n"
138	            f"Entities: {entity_str}\n\n"
139	            "Extract all relation triples with evidence sentence IDs."
140	        )
141	        messages = [
142	            {"role": "system", "content": SYSTEM_PROMPT},
143	            {"role": "user", "content": user_msg},
144	        ]
145	        prompt = tokenizer.apply_chat_template(
146	            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,
147	        )
148	        gold = rng.sample(doc["triples"], k=min(len(doc["triples"]), rng.randint(1, 3)))
149	        items.append({
150	            "prompt": prompt,
151	            "gold_triples": json.dumps(gold, ensure_ascii=False),
152	        })
153	    return Dataset.from_list(items)
154	
155	
156	def _parse_json_output(text: str) -> list[dict]:
157	    try:
158	        return json.loads(text)
159	    except json.JSONDecodeError:
160	        start = text.find("[")
161	        end = text.rfind("]") + 1
162	        if start >= 0 and end > start:
163	            try:
164	                return json.loads(text[start:end])
165	            except json.JSONDecodeError:
166	                return []
167	    return []
168	
169	
170	def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
171	    rewards = []
172	    for text in completions:
173	        parsed = _parse_json_output(text)
174	        if not isinstance(parsed, list):
175	            rewards.append(0.0)
176	            continue
177	        if not parsed:
178	            rewards.append(0.1)
179	            continue
180	        valid = 0
181	        for item in parsed:
182	            if (isinstance(item, dict) and "head" in item
183	                    and "relation" in item and "tail" in item
184	                    and "evidence" in item
185	                    and isinstance(item["evidence"], list)):
186	                valid += 1
187	        rewards.append(valid / len(parsed))
188	    return rewards
189	
190	
191	class LossLogger:
192	    def __init__(self):
193	        self.losses = []
194	        self.grad_norms = []
195	
196	
197	loss_logger = LossLogger()
198	_orig_log = None
199	
200	
201	def _patch_trainer_logging(trainer):
202	    global _orig_log
203	    _orig_log = trainer.log
204	
205	    def patched_log(logs, **kwargs):
206	        if "loss" in logs:
207	            loss_logger.losses.append(logs["loss"])
208	        if "grad_norm" in logs:
209	            loss_logger.grad_norms.append(logs["grad_norm"])
210	        return _orig_log(logs, **kwargs)
211	
212	    trainer.log = patched_log
213	
214	
215	def main():
216	    t0 = time.time()
217	    local_rank = int(os.environ.get("LOCAL_RANK", 0))
218	
219	    print(f"[rank {local_rank}] Loading tokenizer: {MODEL_NAME}")
220	    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, padding_side="left")
221	    if tokenizer.pad_token is None:
222	        tokenizer.pad_token = tokenizer.eos_token
223	
224	    print(f"[rank {local_rank}] Generating dummy dataset...")
225	    dataset = generate_dummy_dataset(tokenizer, n_samples=20, seed=SEED)
226	
227	    print(f"[rank {local_rank}] Loading model with 4-bit QLoRA...")
228	    bnb_config = BitsAndBytesConfig(
229	        load_in_4bit=True,
230	        bnb_4bit_compute_dtype=torch.bfloat16,
231	        bnb_4bit_quant_type="nf4",
232	        bnb_4bit_use_double_quant=True,
233	    )
234	    model = AutoModelForCausalLM.from_pretrained(
235	        MODEL_NAME,
236	        quantization_config=bnb_config,
237	        trust_remote_code=True,
238	        attn_implementation="sdpa",
239	    )
240	
241	    lora_config = LoraConfig(
242	        task_type=TaskType.CAUSAL_LM,
243	        r=64,
244	        lora_alpha=128,
245	        lora_dropout=0.05,
246	        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
247	    )
248	
249	    output_dir = "/tmp/freige_smoke_test"
250	    grpo_config = GRPOConfig(
251	        output_dir=output_dir,
252	        max_steps=NUM_STEPS,
253	        per_device_train_batch_size=1,
254	        gradient_accumulation_steps=2,
255	        learning_rate=5e-5,
256	        bf16=True,
257	        logging_steps=1,
258	        save_strategy="no",
259	        seed=SEED,
260	        num_generations=NUM_GENERATIONS,
261	        max_completion_length=MAX_COMPLETION_LENGTH,
262	        report_to="none",
263	        gradient_checkpointing=True,
264	        gradient_checkpointing_kwargs={"use_reentrant": False},
265	        deepspeed=DEEPSPEED_CONFIG,
266	    )
267	
268	    trainer = GRPOTrainer(
269	        model=model,
270	        args=grpo_config,
271	        train_dataset=dataset,
272	        reward_funcs=[format_reward_fn],
273	        peft_config=lora_config,
274	        processing_class=tokenizer,
275	    )
276	    _patch_trainer_logging(trainer)
277	
278	    print(f"[rank {local_rank}] Starting GRPO smoke test ({NUM_STEPS} steps)...")
279	    torch.cuda.reset_peak_memory_stats()
280	    trainer.train()
281	    elapsed = time.time() - t0
282	
283	    if local_rank == 0:
284	        print("\n" + "=" * 60)
285	        print("SMOKE TEST RESULTS")
286	        print("=" * 60)
287	
288	        print(f"\n--- Loss per step ---")
289	        for i, loss in enumerate(loss_logger.losses):
290	            print(f"  step {i + 1}: {loss:.4f}")
291	
292	        print(f"\n--- Gradient norms ---")
293	        for i, gn in enumerate(loss_logger.grad_norms):
294	            print(f"  step {i + 1}: {gn:.4f}")
295	
296	        print(f"\n--- GPU peak memory ---")
297	        for i in range(torch.cuda.device_count()):
298	            peak_mb = torch.cuda.max_memory_allocated(i) / 1024**2
299	            print(f"  GPU {i}: {peak_mb:.0f} MB ({peak_mb / 1024:.1f} GB)")
300	
301	        print(f"\n--- Total time: {elapsed:.1f}s ---")
302	
303	        has_nan_loss = any(math.isnan(l) for l in loss_logger.losses)
304	        has_nan_grad = any(math.isnan(g) for g in loss_logger.grad_norms) if loss_logger.grad_norms else False
305	        has_zero_grad = all(g == 0.0 for g in loss_logger.grad_norms) if loss_logger.grad_norms else True
306	
307	        if len(loss_logger.losses) >= 4:
308	            last3_avg = sum(loss_logger.losses[-3:]) / 3
309	            first_loss = loss_logger.losses[0]
310	            loss_decreased = last3_avg < first_loss
311	        else:
312	            loss_decreased = True
313	
314	        passed = loss_decreased and not has_nan_loss and not has_nan_grad and not has_zero_grad
315	
316	        print(f"\n--- Diagnostics ---")
317	        print(f"  Loss decreased (last 3 avg < first): {loss_decreased}")
318	        print(f"  NaN in loss: {has_nan_loss}")
319	        print(f"  NaN in grad_norm: {has_nan_grad}")
320	        print(f"  All-zero grad_norm: {has_zero_grad}")
321	        print(f"\n{'PASS' if passed else 'FAIL'}")
322	        print("=" * 60)
323	
324	
325	if __name__ == "__main__":
326	    main()
327	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "eeccc84d-b7ae-4e8f-b5aa-26339b0e89d7"
}
```

</details>

---

### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 33787,
    "tool_uses": 12,
    "duration_ms": 37092
  },
  "last_tool_name": "Bash",
  "uuid": "322a71e7-c25d-49bc-a0ae-2550f8f38a4a",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01GSquSqwqVrWEmfdtGJHFQX`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie -type f -name \"*.md\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "196d5e6c-a913-4f55-b00a-26fea581743c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LRSFSDhV7iwPz9JnKc2Bmy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 4608,
      "cache_read_input_tokens": 29139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4608,
        "ephemeral_1h_input_tokens": 0
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

_source line 55 · 2026-05-14T07:01:42.791Z_

<details><summary>↩ Tool result · `toolu_01GSquSqwqVrWEmfdtGJHFQX`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_4b8948bb/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_4b8948bb/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/reviewer_3281a603/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/reviewer_3281a603/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "99173873-e1b5-4074-a365-f1d09bdc0d9c"
}
```

</details>

---

### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Reading memory.md",
  "usage": {
    "total_tokens": 34406,
    "tool_uses": 13,
    "duration_ms": 38397
  },
  "last_tool_name": "Read",
  "uuid": "b991d0e1-b5d9-4c15-98f8-8d06ef1e181d",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01RJ38emjpnWbC1W8pTRCvdV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "3076dd4e-75a2-4972-8aae-c9cdc7019345",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CqfHYJ1E8apKCbG7yY538K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 611,
      "cache_read_input_tokens": 33747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 611,
        "ephemeral_1h_input_tokens": 0
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

_source line 58 · 2026-05-14T07:01:44.065Z_

<details><summary>↩ Tool result · `toolu_01RJ38emjpnWbC1W8pTRCvdV`</summary>

```text
1	# faith-evidence-ie Memory
2	
3	## 环境与兼容性
4	
5	- **AutoDL HuggingFace 下载不可靠**：大模型（如 Qwen3-4B）从 HF 下载反复 ReadTimeout。解决方案：用 ModelScope (`from modelscope import snapshot_download`) 下载到本地缓存，再用本地路径加载。(2026-05-14)
6	- **vLLM 版本不兼容 TRL**：服务器预装 vLLM 0.18.1，但 TRL 支持范围为 0.11.0-0.17.1。MVP-2 若用 TRL 内部 vLLM rollout 可能有兼容问题，需提前测试。(2026-05-14)
7	- **flash_attn 未安装**：rtx5090-4x 服务器未预装 flash-attn，训练脚本需用 `attn_implementation="sdpa"` 替代。(2026-05-14)
8	- **Qwen3-4B 本地路径**：已通过 ModelScope 下载到 `/root/autodl-tmp/models/Qwen3-4B`（7.6GB）。后续训练脚本应指向此路径而非 HF model ID。(2026-05-14)
9	- **确认训练配置**：ZeRO-2 + QLoRA (4-bit NF4, rank 64, alpha 128) + SDPA。ZeRO-3 + QLoRA 不兼容（uint8 vs all_gather dtype）。(2026-05-14)
10	- **Smoke test 假阴性**：synthetic data reward variance=0 导致零梯度是数学必然（format reward 对所有 completions 输出相同分数），不是训练 bug。评估 smoke test 时只看兼容性和显存，不看 loss 趋势。(2026-05-14)
11	- **TRL 1.1.0 API 变更（关键）**：服务器 TRL 版本 1.1.0，与旧版有 3 个破坏性变更：(1) `SFTConfig.max_seq_length` → `max_length`；(2) `SFTTrainer(tokenizer=...)` → `SFTTrainer(processing_class=...)`；(3) 多 GPU 需要 accelerate `MULTI_GPU` + `device_map={"": local_rank}`。**grpo_trainer.py 也用了 `tokenizer=`，GRPO 提交前必须改为 `processing_class=`**。(2026-05-14)
12	
13	## 数据特征
14	
15	- **DocRED 训练数据量**：train 3027 docs, dev 985 docs。SFT 144 steps/epoch (bs=64), 3 epochs ≈ 432 steps, ~1h on 4x RTX 5090。(2026-05-14)
16	- **MVP-1 hard negative 覆盖率**：DocRED dev set 12275 samples，其中 6830 (55.6%) 有 hard negatives，44.4% 无 hard negatives。无 hard negatives 的样本 CED 退化为 flat NLI（p_neg=0），分析结果时需分层统计这两类样本的行为差异。(2026-05-14)
17	- **MVP-1 tau 阈值敏感度**：33.4% gold evidence p_pos < τ=0.5。GRPO Stage 2 应从 τ=0.3 开始，逐步提升到 0.5，避免过多正样本被丢弃。(2026-05-14)
18	
19	## 实验结论
20	
21	- **MVP-1 CED 信号验证 PASS**：mean margin=0.48 (阈值>0.1)，discrimination acc=81.5% (阈值>70%)，Pearson r=0.34 (阈值<0.7)。CED 信号强度远超阈值，且非词汇重叠驱动。(2026-05-14)
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "d3b50b16-d1e6-44b7-96e1-ce7474f46e90"
}
```

</details>

---

### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Searching for TRL GRPOTrainer 1.1.0 reward_funcs dataset column…",
  "usage": {
    "total_tokens": 35680,
    "tool_uses": 14,
    "duration_ms": 40057
  },
  "last_tool_name": "WebSearch",
  "uuid": "ead7792f-fa33-415d-ac32-06092325dc2c",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BkPBiksPBbqkZqR6SfnruE`</summary>

```json
{
  "query": "TRL GRPOTrainer 1.1.0 reward_funcs dataset columns kwargs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "f3805a2e-82c7-4cad-96eb-1be9d5c7dc00",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L29Gc1hD5vXHN5hDLKbt1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1266,
      "cache_read_input_tokens": 34358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1266,
        "ephemeral_1h_input_tokens": 0
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

_source line 61 · 2026-05-14T07:01:51.998Z_

<details><summary>↩ Tool result · `toolu_01BkPBiksPBbqkZqR6SfnruE`</summary>

````text
Web search results for query: "TRL GRPOTrainer 1.1.0 reward_funcs dataset columns kwargs"

Links: [{"title":"trl/trl/trainer/grpo_trainer.py at main · huggingface/trl","url":"https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_trainer.py"},{"title":"GRPO Trainer · Hugging Face","url":"https://huggingface.co/docs/trl/main/en/grpo_trainer"},{"title":"trl/docs/source/grpo_trainer.md at main · huggingface/trl","url":"https://github.com/huggingface/trl/blob/main/docs/source/grpo_trainer.md"},{"title":"Train a model to solve coding problems using GRPO and TRL | Modal Docs","url":"https://modal.com/docs/examples/grpo_trl"},{"title":"GRPO — swift 3.5.3 documentation","url":"https://swift.readthedocs.io/en/v3.5/Instruction/GRPO.html"},{"title":"GRPO Trainer","url":"https://huggingface.co/docs/trl/v0.15.2/en/grpo_trainer"},{"title":"Releases · huggingface/trl","url":"https://github.com/huggingface/trl/releases"},{"title":"Windows-Friendly GRPO Fine-Tuning with TRL — From Zero to Verifiable Rewards | by Pavan Kunchala | Medium","url":"https://pavankunchalapk.medium.com/windows-friendly-grpo-fine-tuning-with-trl-from-zero-to-verifiable-rewards-f28008c89323"},{"title":"GRPO using Transformer Reinforcement Learning | by Yugen.ai | Yugen.ai Technology Blog | Medium","url":"https://medium.com/yugen-ai-technology-blog/grpo-using-transformer-reinforcement-learning-791ff4e8bb1d"},{"title":"Implementing GRPO in TRL · Hugging Face","url":"https://huggingface.co/learn/llm-course/en/chapter12/4"}]

Based on the search results, here's what I found about TRL GRPOTrainer 1.1.0 regarding `reward_funcs`, dataset columns, and kwargs:

## Reward Functions

Any extra fields (per-completion) are forwarded to the reward functions. If the dataset contains a column named ground_truth, the function will be called with ground_truth as a keyword argument. The easiest way to comply with this requirement is to use **kwargs in the function signature.

## Dataset Columns

The `remove_unused_columns` parameter defaults to False. Whether to only keep the column "prompt" in the dataset. If you use a custom reward function that requires any column other than "prompts" and "completions", you should keep this to False.

The standard expected dataset structure requires at minimum:
- A "prompt" column (required by the trainer)
- Additional columns can be passed to reward functions as keyword arguments

## Reward Function Signature

Reward functions should accept:
- `completions` (list of strings) - the model completions
- `**kwargs` - any additional columns from the dataset

You can pass several reward functions as a list; this list may include both synchronous and asynchronous functions.

## Example

Here's a typical pattern:

```python
def reward_func(completions, ground_truth=None, **kwargs):
    # Custom reward logic here
    return rewards_list
```

Additional dataset columns are automatically forwarded to the reward function, making it flexible to pass custom fields through the `**kwargs` parameter.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "461acd75-fbde-4018-8974-d612519da1a2"
}
```

</details>

---

### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Fetching https://github.com/huggingface/trl/blob/main/trl/…",
  "usage": {
    "total_tokens": 36717,
    "tool_uses": 15,
    "duration_ms": 48078
  },
  "last_tool_name": "WebFetch",
  "uuid": "a4693ed3-6313-48b6-985c-31378a8ee351",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ShiSLHYf4jWzWM1V51TEsh`</summary>

```json
{
  "url": "https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_trainer.py",
  "prompt": "How does GRPOTrainer call reward functions? What dataset columns are passed as kwargs to reward_funcs? Look for the code that calls the reward functions and passes dataset columns."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "a8e81769-25d4-4760-82d5-cf2d3fefbc37",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018Ui1d2JZzBbAhYaaBQhEHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 35624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1032,
        "ephemeral_1h_input_tokens": 0
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

_source line 64 · 2026-05-14T07:02:14.780Z_

<details><summary>↩ Tool result · `toolu_01ShiSLHYf4jWzWM1V51TEsh`</summary>

```text
API Error: 522 {"type":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/","title":"Error 522: Connection timed out","status":522,"detail":"Cloudflare could not establish a TCP connection to the origin server. The TCP handshake timed out, which may indicate the origin is overloaded, firewalling Cloudflare, or unreachable at the network level.","instance":"9fb808cb49608169","error_code":522,"error_name":"connection_timeout","error_category":"origin","ray_id":"9fb808cb49608169","timestamp":"2026-05-14T07:02:14Z","zone":"api.anthropic.com","cloudflare_error":true,"retryable":true,"retry_after":120,"owner_action_required":true,"what_you_should_do":"**Wait and retry.** Back off for at least 120 seconds. If the error persists, the website operator should verify firewall rules and ensure the origin accepts connections from Cloudflare IP ranges.","footer":"This error was generated by Cloudflare on behalf of the website owner."}. This is a server-side issue, usually temporary — try again in a moment. If it persists, check status.claude.com.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "17afd6e7-6638-4922-8ba6-ff07a09db282"
}
```

</details>

---

### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Fetching https://huggingface.co/docs/trl/main/en/grpo_trai…",
  "usage": {
    "total_tokens": 37303,
    "tool_uses": 16,
    "duration_ms": 70922
  },
  "last_tool_name": "WebFetch",
  "uuid": "44b737ee-5f9e-49ad-9cbf-676e657cf8d1",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015zvy54To9KUMPdEoFHFUAi`</summary>

```json
{
  "url": "https://huggingface.co/docs/trl/main/en/grpo_trainer",
  "prompt": "How does GRPOTrainer pass dataset columns to reward functions? What is the mechanism for forwarding extra columns as kwargs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "d44c74a9-9f8d-4dac-8764-faedb7173f3f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011QxFjMLf66Bqus1JriGdFs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 36656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 585,
        "ephemeral_1h_input_tokens": 0
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

_source line 67 · 2026-05-14T07:02:17.170Z_

<details><summary>↩ Tool result · `toolu_015zvy54To9KUMPdEoFHFUAi`</summary>

```text
&lt;persisted-output>
Output too large (60.2KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/652a0167-bc8e-4a7c-b9ac-5173d41f57f7/tool-results/toolu_015zvy54To9KUMPdEoFHFUAi.txt

Preview (first 2KB):
# GRPO Trainer

[![model badge](https://img.shields.io/badge/All_models-GRPO-blue)](https://huggingface.co/models?other=grpo,trl)

## Overview

TRL supports the GRPO Trainer for training language models, as described in the paper [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://huggingface.co/papers/2402.03300) by [Zhihong Shao](https://huggingface.co/syhia), [Peiyi Wang](https://huggingface.co/peiyiwang89), [Qihao Zhu](https://huggingface.co/zqh11), Runxin Xu, [Junxiao Song](https://huggingface.co/haha-point), Mingchuan Zhang, Y. K. Li, Y. Wu, [Daya Guo](https://huggingface.co/guoday).

The abstract from the paper is the following:

> Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. In this paper, we introduce DeepSeekMath 7B, which continues pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, together with natural language and code data. DeepSeekMath 7B has achieved an impressive score of 51.7% on the competition-level MATH benchmark without relying on external toolkits and voting techniques, approaching the performance level of Gemini-Ultra and GPT-4. Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH. The mathematical reasoning capability of DeepSeekMath is attributed to two key factors: First, we harness the significant potential of publicly available web data through a meticulously engineered data selection pipeline. Second, we introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO.

This post-training method was contributed by [Quentin Gallouédec](https://huggingface.co/qgallouedec).

## Quick start

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "6a85bee2-cf08-483a-b2a5-94845f5f7bb4"
}
```

</details>

---

### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/652a0167-bc8e-4a7c-b9ac-5173d41f57f7/tool-results/toolu_015zvy54To9KUMPdEoFHFUAi.txt",
  "usage": {
    "total_tokens": 38134,
    "tool_uses": 17,
    "duration_ms": 74030
  },
  "last_tool_name": "Read",
  "uuid": "1c618188-2545-4c01-bee9-4e8d3cf9ec25",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01GdCtHESUN7rXDMX5K3omRg`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/652a0167-bc8e-4a7c-b9ac-5173d41f57f7/tool-results/toolu_015zvy54To9KUMPdEoFHFUAi.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "ef0893dd-8640-4399-92f6-a24972b94234",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014FpLWpj5sJ62A23Rt77HSw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 37241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 825,
        "ephemeral_1h_input_tokens": 0
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

_source line 70 · 2026-05-14T07:02:20.018Z_

<details><summary>↩ Tool result · `toolu_01GdCtHESUN7rXDMX5K3omRg`</summary>

````text
1	# GRPO Trainer
2	
3	[![model badge](https://img.shields.io/badge/All_models-GRPO-blue)](https://huggingface.co/models?other=grpo,trl)
4	
5	## Overview
6	
7	TRL supports the GRPO Trainer for training language models, as described in the paper [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://huggingface.co/papers/2402.03300) by [Zhihong Shao](https://huggingface.co/syhia), [Peiyi Wang](https://huggingface.co/peiyiwang89), [Qihao Zhu](https://huggingface.co/zqh11), Runxin Xu, [Junxiao Song](https://huggingface.co/haha-point), Mingchuan Zhang, Y. K. Li, Y. Wu, [Daya Guo](https://huggingface.co/guoday).
8	
9	The abstract from the paper is the following:
10	
11	> Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. In this paper, we introduce DeepSeekMath 7B, which continues pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, together with natural language and code data. DeepSeekMath 7B has achieved an impressive score of 51.7% on the competition-level MATH benchmark without relying on external toolkits and voting techniques, approaching the performance level of Gemini-Ultra and GPT-4. Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH. The mathematical reasoning capability of DeepSeekMath is attributed to two key factors: First, we harness the significant potential of publicly available web data through a meticulously engineered data selection pipeline. Second, we introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO.
12	
13	This post-training method was contributed by [Quentin Gallouédec](https://huggingface.co/qgallouedec).
14	
15	## Quick start
16	
17	This example demonstrates how to train a model using the GRPO method. We train a [Qwen2.5 0.5B Instruct model](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) with the prompts from the [DeepMath-103K dataset](https://huggingface.co/datasets/trl-lib/DeepMath-103K). You can view the data in the dataset here:
18	
19	&lt;iframe
20	  src="https://huggingface.co/datasets/trl-lib/DeepMath-103K/embed/viewer/default/train?row=0"
21	  frameborder="0"
22	  width="100%"
23	  height="560px"
24	>
25	
26	Below is the script to train the model.
27	
28	```python
29	# train_grpo.py
30	from datasets import load_dataset
31	from trl import GRPOTrainer
32	from trl.rewards import accuracy_reward
33	
34	dataset = load_dataset("trl-lib/DeepMath-103K", split="train")
35	
36	trainer = GRPOTrainer(
37	    model="Qwen/Qwen2.5-0.5B-Instruct",
38	    reward_funcs=accuracy_reward,
39	    train_dataset=dataset,
40	)
41	trainer.train()
42	```
43	
44	Execute the script using the following command:
45	
46	```bash
47	accelerate launch train_grpo.py
48	```
49	
50	Distributed across 8 GPUs, the training takes approximately 1 day.
51	
52	![GRPO curves](https://huggingface.co/datasets/trl-lib/documentation-images/resolve/main/grpo_curves.png)
53	
54	> **Note:** The reward curves above were generated with `Qwen/Qwen2-0.5B-Instruct`. Results with `Qwen/Qwen2.5-0.5B-Instruct` will be qualitatively similar.
55	
56	## Looking deeper into the GRPO method
57	
58	GRPO is an online learning algorithm, meaning it improves iteratively by using the data generated by the trained model itself during training. The intuition behind GRPO objective is to maximize the advantage of the generated completions, while ensuring that the model remains close to the reference policy. To understand how GRPO works, it can be broken down into four main steps: **Generating completions**, **computing the advantage**, **estimating the KL divergence**, and **computing the loss**.
59	
60	![GRPO visual](https://huggingface.co/datasets/trl-lib/documentation-images/resolve/main/grpo_visual.png)
61	
62	### Generating completions
63	
64	At each training step, we sample a batch of prompts and generate a set of  \\( G \\) completions for each prompt (denoted as  \\( o_i \\)).
65	
66	### Computing the advantage
67	
68	For each of the  \\( G \\) sequences, we compute the reward using a reward model or reward function. To align with the comparative nature of reward models—typically trained on datasets of comparisons between outputs for the same question—the advantage is calculated to reflect these relative comparisons. It is normalized as follows:
69	
70	$$\hat{A}_{i,t} = \frac{r_i - \text{mean}(\mathbf{r})}{\text{std}(\mathbf{r})}$$
71	
72	This approach gives the method its name: **Group Relative Policy Optimization (GRPO)**.
73	
74	> [!TIP]
75	> It was shown in the paper [Understanding R1-Zero-Like Training: A Critical Perspective](https://huggingface.co/papers/2503.20783) that scaling by  \\( \text{std}(\mathbf{r}) \\) may cause a question-level difficulty bias. You can disable this scaling by setting `scale_rewards=False` in [GRPOConfig](/docs/trl/main/en/grpo_trainer#trl.GRPOConfig).
76	> Note that turning off std-based scaling also removes variance normalization, so update magnitudes depend directly on the raw reward scale and batch composition.
77	
78	> [!TIP]
79	> As shown in [Part I: Tricks or Traps? A Deep Dive into RL for LLM Reasoning (Lite PPO)](https://huggingface.co/papers/2508.08221), calculating the mean at the local (group) level and the standard deviation at the global (batch) level enables more robust reward shaping. You can use this scaling strategy by setting `scale_rewards="batch"` in [GRPOConfig](/docs/trl/main/en/grpo_trainer#trl.GRPOConfig).
80	
81	### Estimating the KL divergence
82	
83	KL divergence is estimated using the approximator introduced by [Schulman et al. (2020)](http://joschu.net/blog/kl-approx.html). The approximator is defined as follows:
84	
85	$$\mathbb{D}_{\text{KL}}\left[\pi_\theta \|\pi_{\text{ref}}\right] = \frac{\pi_{\text{ref}}(o_{i,t} \mid q, o_{i,&lt;t})}{\pi_\theta(o_{i,t} \mid q, o_{i,&lt;t})} - \log \frac{\pi_{\text{ref}}(o_{i,t} \mid q, o_{i,&lt;t})}{\pi_\theta(o_{i,t} \mid q, o_{i,&lt;t})} - 1,
86	$$
87	
88	### Computing the loss
89	
90	The objective is to maximize the advantage while ensuring that the model remains close to the reference policy. Consequently, the loss is defined as follows:
91	
92	$$
93	\mathcal{L}_{\text{GRPO}}(\theta) = -\frac{1}{\sum_{i=1}^G |o_i|} \sum_{i=1}^G \sum_{t=1}^{|o_i|} \left[ \frac{\pi_\theta(o_{i,t} \mid q, o_{i,< t})}{\left[\pi_\theta(o_{i,t} \mid q, o_{i,< t})\right]_{\text{no grad}}} \hat{A}_{i,t} - \beta \mathbb{D}_{\text{KL}}\left[\pi_\theta \| \pi_{\text{ref}}\right] \right],
94	$$
95	
96	where the first term represents the scaled advantage and the second term penalizes deviations from the reference policy through KL divergence.
97	
98	> [!TIP]
99	> Note that compared to the original formulation in [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://huggingface.co/papers/2402.03300), we don't scale by  \\( \frac{1}{|o_i|} \\) because it was shown in the paper [Understanding R1-Zero-Like Training: A Critical Perspective](https://huggingface.co/papers/2503.20783) that this introduces a response-level length bias. More details in [loss types](#loss-types).
100	
101	> [!TIP]
102	> Note that compared to the original formulation in [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://huggingface.co/papers/2402.03300), we use  \\( \beta = 0.0 \\) by default, meaning that the KL divergence term is not used. This choice is motivated by several recent studies (e.g., [Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model](https://huggingface.co/papers/2503.24290)) which have shown that the KL divergence term is not essential for training with GRPO. As a result, it has become common practice to exclude it (e.g. [Understanding R1-Zero-Like Training: A Critical Perspective](https://huggingface.co/papers/2503.20783), [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://huggingface.co/papers/2503.14476)). If you wish to include the KL divergence term, you can set `beta` in [GRPOConfig](/docs/trl/main/en/grpo_trainer#trl.GRPOConfig) to a non-zero value.
103	
104	In the original paper, this formulation is generalized to account for multiple updates after each generation (denoted  \\( \mu \\), can be set with `num_iterations` in [GRPOConfig](/docs/trl/main/en/grpo_trainer#trl.GRPOConfig)) by leveraging the **clipped surrogate objective**:
105	
106	$$
107	\mathcal{L}_{\text{GRPO}}(\theta) = - \frac{1}{\sum_{i=1}^G |o_i|} \sum_{i=1}^G \sum_{t=1}^{|o_i|} \left[ \min \left( \frac{\pi_\theta(o_{i,t} \mid q, o_{i,< t})}{\pi_{\theta_{\text{old}}}(o_{i,t} \mid q, o_{i,< t})} \hat{A}_{i,t}, \, \text{clip}\left( \frac{\pi_\theta(o_{i,t} \mid q, o_{i,< t})}{\pi_{\theta_{\text{old}}}(o_{i,t} \mid q, o_{i,< t})}, 1 - \epsilon, 1 + \epsilon \right) \hat{A}_{i,t} \right) - \beta \mathbb{D}_{\text{KL}}\left[\pi_\theta \| \pi_{\text{ref}}\right] \right],
108	$$
109	
110	where  \\(\text{clip}(\cdot, 1 - \epsilon, 1 + \epsilon) \\) ensures that updates do not deviate excessively from the reference policy by bounding the policy ratio between  \\( 1 - \epsilon \\) and  \\( 1 + \epsilon \\).
111	When  \\( \mu = 1 \\) (default in TRL), the clipped surrogate objective simplifies to the original objective.
112	
113	#### Loss Types
114	
115	Several formulations of the objective have been proposed in the literature. Initially, the objective of GRPO was defined as follows:
116	
117	$$
118	\mathcal{L}_{\text{GRPO}}(\theta) = - \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} l_{i,t},
119	$$
120	
121	where
122	
123	$$
124	l_{i,t} = \frac{\pi_\theta(o_{i,t} \mid q, o_{i,< t})}{\left[\pi_\theta(o_{i,t} \mid q, o_{i,< t})\right]_{\text{no grad}}} \hat{A}_{i,t} - \beta \mathbb{D}_{\text{KL}}\left[\pi_\theta \| \pi_{\text{ref}}\right].
125	$$
126	
127	The [DAPO paper](https://huggingface.co/papers/2503.14476) highlights the limitations of the GRPO algorithm’s sample-level loss in long-CoT scenarios, where longer responses are under-penalized, leading to poorer quality outputs. The proposed solution is a token-level normalization, which better handles longer sequences by assigning more balanced rewards to individual tokens, regardless of response length:
128	
129	$$
130	\mathcal{L}_{\text{DAPO}}(\theta) = - \frac{1}{\sum_{i=1}^G |o_i|} \sum_{i=1}^G \sum_{t=1}^{|o_i|} l_{i,t},
131	$$
132	
133	To use this formulation, set `loss_type="dapo"` in [GRPOConfig](/docs/trl/main/en/grpo_trainer#trl.GRPOConfig).
134	
135	Furthermore, it was demonstrated in the paper [Understanding R1-Zero-Like Training: A Critical Perspective](https://huggingface.co/papers/2503.20783) that the initial GRPO formulation introduces a response length bias. They show that while the DAPO formulation reduces this bias, it does not eliminate it completely. To fully remove this bias, they propose dividing by a constant instead of the sequence length, resulting in the following formulation:
136	
137	$$
138	\mathcal{L}_{\text{Dr. GRPO}}(\theta) = - \frac{1}{LG} \sum_{i=1}^G \sum_{t=1}^{|o_i|} l_{i,t},
139	$$
140	
141	This constant is recommended to be the maximum completion length. To use this formulation, set `loss_type="dr_grpo"` in the [GRPOConfig](/docs/trl/main/en/grpo_trainer#trl.GRPOConfig).
142	
143	Alternatively, in the [SAPO paper](https://huggingface.co/papers/2511.20347), the Qwen team proposes replacing the "hard" clipping mechanism of GRPO with a smooth, temperature-controlled soft gating mechanism. While GRPO zeroes out gradients when the policy deviates too far from the reference, SAPO uses a soft trust region that smoothly decays the gradient weight. This allows the model to retain useful learning signals from "near-on-policy" tokens while suppressing noise from extreme deviations.
144	
145	The loss function is defined as:
146	
147	$$
148	\mathcal{L}_{\text{SAPO}}(\theta) = - \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} f_{i,t} \left( \frac{\pi_\theta(o_{i,t} | q, o_{i,&lt;t})}{\pi_{\theta_{old}}(o_{i,t} | q, o_{i,&lt;t})} \right) \hat{A}_{i,t}
149	$$
150	
151	The soft-gating function  \\( f_{i,t} \\) is defined using the sigmoid function  \\( \sigma \\) as:
152	
153	$$
154	f_{i,t}(x) = \sigma \left( \tau_{i,t} (x - 1) \right) \cdot \frac{4}{\tau_{i,t}}
155	$$
156	
157	The temperature  \\( \tau_{i,t} \\) is chosen based on the sign of the advantage  \\( \hat{A}_{i,t} \\):
158	
159	$$
160	\tau_{i,t} = \begin{cases} 
161	\tau_{\text{pos}}, & \text{if } \hat{A}_{i,t} > 0 \\
162	\tau_{\text{neg}}, & \text{otherwise}
163	\end{cases}
164	$$
165	
166	They recommend using asymmetric temperatures,  \\( \tau_{\text{neg}} > \tau_{\text{pos}} \\) (defaults are  \\( \tau_{\text{pos}}=1.0, \tau_{\text{neg}}=1.05 \\) ). This ensures that the model is penalized more strictly for "bad" actions to prevent instability, while being more permissive with "good" actions.
167	
168	To use this formulation, set `loss_type="sapo"` in the [GRPOConfig](/docs/trl/main/en/grpo_trainer#trl.GRPOConfig).
169	
170	## Logged metrics
171	
172	While training and evaluating, we record the following reward metrics:
173	
174	- `num_tokens`: The total number of tokens processed so far, including both prompts and completions. When using tools, only non-tool tokens are counted.
175	- `step_time`: The average time (in seconds) taken per training step (including generation).
176	- `completions/mean_length`: The average length of generated completions. When using tools, only non-tool tokens are counted.
177	- `completions/min_length`: The minimum length of generated completions. When using tools, only non-tool tokens are counted.
178	- `completions/max_length`: The maximum length of generated completions. When using tools, only non-tool tokens are counted.
179	- `completions/mean_terminated_length`: The average length of generated completions that terminate with EOS. When using tools, only non-tool tokens are counted.
180	- `completions/min_terminated_length`: The minimum length of generated completions that terminate with EOS. When using tools, only non-tool tokens are counted.
181	- `completions/max_terminated_length`: The maximum length of generated completions that terminate with EOS. When using tools, only non-tool tokens are counted.
182	- `completions/clipped_ratio`: The ratio of truncated (clipped) completions.
183	- `reward/{reward_func_name}/mean`: The average reward from a specific reward function.
184	- `reward/{reward_func_name}/std`: The standard deviation of the reward from a specific reward function.
185	- `reward`: The overall average reward after summing rewards across functions (weighted by `reward_weights`).
186	- `reward_std`: The standard deviation of summed rewards across functions (weighted by `reward_weights`), computed over the full batch.
187	- `frac_reward_zero_std`: The fraction of samples in the generation batch with a reward std of zero, implying there is little diversity for that prompt (all answers are correct or incorrect).
188	- `entropy`: Average entropy of token predictions across generated completions. (If `mask_truncated_completions=True`, masked sequences tokens are excluded.)
189	- `kl`: The average KL divergence between the model and the reference model, calculated over generated completions. Logged only if `beta` is nonzero.
190	- `clip_ratio/region_mean`: The ratio of token (or sequence, if `importance_sampling_level="sequence"`) probabilities where the GRPO objective is clipped to stay within the trust region:  \\( \text{clip}\left( r_{i,t}(\theta), 1 - \epsilon_\mathrm{low}, 1 + \epsilon_\mathrm{high} \right)\,, \quad r_{i,t}(\theta) = \frac{\pi_\theta(o_{i,t} \mid q, o_{i,< t})}{\pi_{\theta_{\text{old}}}(o_{i,t} \mid q, o_{i,< t})} \\). A higher value means more tokens are clipped, which constrains how much the policy $\pi_\theta$ can change.
191	- `clip_ratio/low_mean`: The average ratio of token (or sequence, if `importance_sampling_level="sequence"`) probabilities that were clipped on the lower bound of the trust region:  \\(r_{i,t}(\theta) < 1 - \epsilon_\mathrm{low}\\).
192	- `clip_ratio/low_min`: The minimum ratio of token (or sequence, if `importance_sampling_level="sequence"`) probabilities that were clipped on the lower bound of the trust region:  \\(r_{i,t}(\theta) < 1 - \epsilon_\mathrm{low}\\).
193	- `clip_ratio/high_mean`: The average ratio of token (or sequence, if `importance_sampling_level="sequence"`) probabilities that were clipped on the upper bound of the trust region:  \\(r_{i,t}(\theta) > 1 + \epsilon_\mathrm{high}\\).
194	- `clip_ratio/high_max`: The maximum ratio of token (or sequence, if `importance_sampling_level="sequence"`) probabilities that were clipped on the upper bound of the trust region:  \\(r_{i,t}(\theta) > 1 + \epsilon_\mathrm{high}\\).
195	
196	## Customization
197	
198	### Speed up training with vLLM-powered generation
199	
200	Generation is often the main bottleneck when training with online methods. To accelerate generation, you can use [vLLM](https://github.com/vllm-project/vllm), a high-throughput, low-latency inference engine for LLMs. To enable it, first install the package with
201	
202	```shell
203	pip install trl[vllm]
204	```
205	
206	We support two ways of using vLLM during training: **server mode** and **colocate mode**.
207	
208	> [!TIP]
209	> By default, Truncated Importance Sampling is activated for vLLM generation to address the generation-training mismatch that occurs when using different frameworks. This can be turned off by setting `vllm_importance_sampling_correction=False`. For more information, see [Truncated Importance Sampling](paper_index#truncated-importance-sampling)
210	
211	#### Option 1: Colocate mode
212	
213	In this mode, vLLM runs inside the trainer process and shares GPU memory with the training model. This avoids launching a separate server and can improve GPU utilization, but may lead to memory contention on the training GPUs. This is the default mode.
214	
215	```python
216	from trl import GRPOConfig
217	
218	training_args = GRPOConfig(
219	    ...,
220	    use_vllm=True,  # vllm_mode="colocate" by default
221	)
222	```
223	
224	#### Option 2: Server mode
225	
226	In this mode, vLLM runs in a separate process (and using separate GPUs) and communicates with the trainer via HTTP. This is ideal if you have dedicated GPUs for inference.
227	
228	1. **Start the vLLM server**:
229	
230	   ```bash
231	   trl vllm-serve --model &lt;model_name>
232	   ```
233	
234	2. **Enable server mode in your training script**:
235	
236	   ```python
237	   from trl import GRPOConfig
238	
239	   training_args = GRPOConfig(
240	       ...,
241	       use_vllm=True,
242	       vllm_mode="server",
243	   )
244	   ```
245	
246	> [!WARNING]
247	> Make sure that the server is using different GPUs than the trainer, otherwise you may run into NCCL errors. You can specify the GPUs to use with the `CUDA_VISIBLE_DEVICES` environment variable.
248	
249	> [!TIP]
250	> Depending on the model size and the overall GPU memory requirements for training, you may need to adjust the `vllm_gpu_memory_utilization` parameter in [GRPOConfig](/docs/trl/main/en/grpo_trainer#trl.GRPOConfig) to avoid underutilization or out-of-memory errors.
251	>
252	> We provide a [HF Space](https://huggingface.co/spaces/trl-lib/recommend-vllm-memory) to help estimate the recommended GPU memory utilization based on your model configuration and experiment settings. Simply use it as follows to get `vllm_gpu_memory_utilization` recommendation:
253	>
254	> 
255	>
256	> If the recommended value does not work in your environment, we suggest adding a small buffer (e.g., +0.05 or +0.1) to the recommended value to ensure stability.
257	>
258	> If you still find you are getting out-of-memory errors set `vllm_enable_sleep_mode` to True and the vllm parameters and cache will be offloaded during the optimization step. For more information, see [Reducing Memory Usage with vLLM Sleep Mode](reducing_memory_usage#vllm-sleep-mode).
259	
260	> [!TIP]
261	> By default, GRPO uses `MASTER_ADDR=localhost` and `MASTER_PORT=12345` for vLLM, but you can override these values by setting the environment variables accordingly.
262	
263	For more information, see [Speeding up training with vLLM](speeding_up_training#vllm-for-fast-generation-in-online-methods).
264	
265	#### Dealing with the Training-Inference Mismatch
266	While vLLM greatly accelerates inference, it also decouples the inference engine from the training engine. In theory these engines are mathematically identical, in practice however they can produce different outputs due to precision effects and hardware specific optimizations. This divergence reflects the different optimization objectives of the two systems. This divergence reflects the distinct optimization goals of the two systems. Inference engines aim to maximize sampling throughput, typically measured in tokens per second, while maintaining acceptable sampling fidelity. Training frameworks instead focus on numerical stability and precision for gradient computation, often using higher precision formats like FP32 for master weights and optimizer states. These differing priorities and constraints introduce an inevitable, albeit subtle, mismatch between training and inference.
267	
268	This mismatch leads to a biased gradient update which has been observed to destabilize training ([[1]](https://fengyao.notion.site/off-policy-rl)[[2]](https://yingru.notion.site/When-Speed-Kills-Stability-Demystifying-RL-Collapse-from-the-Training-Inference-Mismatch-271211a558b7808d8b12d403fd15edda)[[3]](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/#true-on-policy-rl)[[4]](https://huggingface.co/papers/2510.26788)[[5]](https://huggingface.co/papers/2510.18855)). For simplicity, consider the REINFORCE policy gradient:
269	
270	$$
271	\nabla_\theta \mathcal{J}(x,\theta)
272	= \mathbb{E}_{y \sim \pi^\text{train}(\cdot \mid x,\theta)}
273	\left[ \nabla_\theta \log \pi^\text{train}(y \mid x,\theta) \cdot R(x,y) \right]
274	$$
275	
276	Here  \\( x \\) denotes prompts sampled from some data distribution, and  \\( \pi^\text{train} \\) is the policy implemented by the training engine. With vLLM in the loop we obtain a separate inference policy  \\( \pi^\text{inference} \\), so the effective policy gradient becomes
277	
278	$$
279	\nabla_\theta \mathcal{J}_{\text{biased}}(x,\theta)
280	= \mathbb{E}_{y \sim \pi^\text{inference}(\cdot \mid x,\theta)}
281	\left[ \nabla_\theta \log \pi^\text{train}(y \mid x,\theta) \cdot R(x,y) \right].
282	$$
283	
284	This turns an otherwise on policy RL problem into an off policy one.
285	
286	The standard way to correct for this distribution shift is **importance sampling (IS)**. We provide two IS variants: [Truncated Importance Sampling (TIS)](paper_index#truncated-importance-sampling) and [Masked Importance Sampling (MIS)](paper_index#masked-importance-sampling). Both variants can be applied either at the token level or at the sequence level.Let  \\( \rho \\) denote the importance weight, for example  \\( \rho_t \\) per token or  \\( \rho_{\text{seq}} \\) per sequence. Under TIS, ratios larger than `vllm_importance_sampling_cap` are clipped,
287	
288	$$
289	\rho \leftarrow \min(\rho, C).
290	$$
291	
292	Under MIS, ratios larger than `vllm_importance_sampling_cap` are set to zero, so those samples do not contribute to the gradient. In other words, large ratio samples are downweighted under TIS and discarded under MIS. The configuration flag `vllm_importance_sampling_mode` chooses both the IS variant (masking or truncation) and the granularity (token level or sequence level).
293	
294	Importance sampling is the principled algorithmic response to the training–inference mismatch. However, there are also more direct approaches that attempt to reduce the mismatch between the two engines themselves. Most of these are engineering solutions. For example, [MiniMax M1 uses an FP32 language model head](https://huggingface.co/papers/2506.13585) in the inference engine. Thinking Machines has explored [deterministic inference kernels](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), although this comes with a significant efficiency cost. vLLM has shown [bitwise consistent policies](https://blog.vllm.ai/2025/11/10/bitwise-consistent-train-inference.html) by building on the batch invariant deterministic kernels from Thinking Machines, but as of November 2025 there remains a substantial throughput penalty relative to standard vLLM inference.
295	
296	### GRPO at scale: train a 70B+ Model on multiple nodes
297	
298	When training large models like **Qwen2.5-72B**, you need several key optimizations to make the training efficient and scalable across multiple GPUs and nodes. These include:
299	
300	- **DeepSpeed ZeRO Stage 3**: ZeRO leverages data parallelism to distribute model states (weights, gradients, optimizer states) across multiple GPUs and CPUs, reducing memory and compute requirements on each device. Since large models cannot fit on a single GPU, using ZeRO Stage 3 is required for training such models. For more details, see [DeepSpeed Integration](deepspeed_integration).
301	- **Accelerate**: Accelerate is a library that simplifies distributed training across multiple GPUs and nodes. It provides a simple API to launch distributed training and handles the complexities of distributed training, such as data parallelism, gradient accumulation, and distributed data loading. For more details, see [Distributing Training](distributing_training).
302	- **vLLM**: See the previous section on how to use vLLM to speed up generation.
303	
304	Below is an example SLURM script to train a 70B model with GRPO on multiple nodes. This script trains a model on 4 nodes and uses the 5th node for vLLM-powered generation.
305	
306	```sh
307	#!/bin/bash
308	#SBATCH --nodes=5
309	#SBATCH --gres=gpu:8
310	
311	# Get the list of allocated nodes
312	NODELIST=($(scontrol show hostnames $SLURM_JOB_NODELIST))
313	
314	# Assign the first 4 nodes for training and the 5th node for vLLM
315	TRAIN_NODES="${NODELIST[@]:0:4}"  # Nodes 0, 1, 2, 3 for training
316	VLLM_NODE="${NODELIST[4]}"  # Node 4 for vLLM
317	
318	# Run training on the first 4 nodes (Group 1)
319	srun --nodes=4 --ntasks=4 --nodelist="${NODELIST[@]:0:4}" accelerate launch \
320	     --config_file examples/accelerate_configs/deepspeed_zero3.yaml \
321	     --num_processes 32 \
322	     --num_machines 4 \
323	     --main_process_ip ${NODELIST[0]} \
324	     --machine_rank $SLURM_PROCID \
325	     --rdzv_backend c10d \
326	     train_grpo.py \
327	     --server_ip $VLLM_NODE &
328	
329	# Run vLLM server on the 5th node (Group 2)
330	srun --nodes=1 --ntasks=1 --nodelist="${NODELIST[4]}" trl vllm-serve --model Qwen/Qwen2.5-72B --tensor_parallel_size 8 &
331	
332	wait
333	```
334	
335	```python
336	import argparse
337	
338	from datasets import load_dataset
339	from trl import GRPOTrainer, GRPOConfig
340	from trl.rewards import accuracy_reward
341	
342	def main():
343	    parser = argparse.ArgumentParser()
344	    parser.add_argument("--vllm_server_host", type=str, default="", help="The server IP")
345	    args = parser.parse_args()
346	
347	    dataset = load_dataset("trl-lib/DeepMath-103K", split="train")
348	
349	    training_args = GRPOConfig(
350	        per_device_train_batch_size=4,
351	        use_vllm=True,
352	        vllm_mode="server",
353	        vllm_server_host=args.vllm_server_host.replace("ip-", "").replace("-", "."),  # from ip-X-X-X-X to X.X.X.X
354	    )
355	
356	    trainer = GRPOTrainer(
357	        model="Qwen/Qwen2.5-72B",
358	        args=training_args,
359	        reward_funcs=accuracy_reward,
360	        train_dataset=dataset
361	    )
362	    trainer.train()
363	
364	if __name__=="__main__":
365	    main()
366	```
367	
368	### Using a custom reward function
369	
370	The [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer) supports using custom reward functions instead of dense reward models. To ensure compatibility, your reward function must satisfy the following requirements:
371	
372	Reward functions can be either synchronous Python callables or asynchronous `async def` coroutines. When you provide multiple asynchronous reward functions, they are awaited concurrently (run in parallel via `asyncio.gather`) so their latency overlaps.
373	
374	1. **Input arguments**:
375	   - The function must accept the following as keyword arguments:
376	     - `prompts` (contains the prompts),
377	     - `completions` (contains the generated completions),
378	     - `completion_ids` (contains the tokenized completions),
379	     - `trainer_state` ([TrainerState](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.TrainerState)): The current state of the trainer. This can be used to implement dynamic reward functions, such as curriculum learning, where the reward is adjusted based on the training progress.
380	     - `log_extra`: a callable `log_extra(column: str, values: list)` to add extra columns to the completions table. See Example 6. In distributed training, it's important that all processes log the same set of keys.
381	     - `log_metric`: a callable `log_metric(name: str, value: float)` to log scalar metrics as plots alongside `kl`, `entropy`, etc. See Example 6. In distributed training, it's important that all processes log the same set of keys.
382	     - `environments`: a list of environment instances, one per completion. Only present when `environment_factory` is provided. Use this to read state accumulated during the episode (e.g., `env.reward`).
383	     - All column names (but `prompt`) that the dataset may have. For example, if the dataset contains a column named `ground_truth`, the function will be called with `ground_truth` as a keyword argument.
384	
385	     The easiest way to comply with this requirement is to use `**kwargs` in the function signature.
386	   - Depending on the dataset format, the input will vary:
387	     - For [standard format](dataset_formats#standard), `prompts` and `completions` will be lists of strings.
388	     - For [conversational format](dataset_formats#conversational), `prompts` and `completions` will be lists of message dictionaries.
389	
390	2. **Return value**: The function must return a list of floats. Each float represents the reward corresponding to a single completion.
391	
392	#### Example 1: Reward longer completions
393	
394	Below is an example of a reward function for a standard format that rewards longer completions:
395	
396	```python
397	def reward_func(completion_ids, **kwargs):
398	    """Reward function that assigns higher scores to longer completions (in terms of token count)."""
399	    return [float(len(ids)) for ids in completion_ids]
400	```
401	
402	You can test it as follows:
403	
404	```python
405	>>> prompts = ["The sky is", "The sun is"]  # not used in the reward function, but the trainer will pass it
406	>>> completions = [" blue.", " in the sky."]  # not used in the reward function, but the trainer will pass it
407	>>> completion_ids = [[6303, 13], [304, 279, 12884, 13]]
408	>>> reward_func(prompts=prompts, completions=completions, completion_ids=completion_ids)
409	[2.0, 4.0]
410	```
411	
412	#### Example 1.1: Reward longer completions (based on the number of characters)
413	
414	Same as the previous example, but this time the reward function is based on the number of characters instead of tokens.
415	
416	```python
417	def reward_func(completions, **kwargs):
418	    """Reward function that assigns higher scores to longer completions (in terms of character count)."""
419	    return [float(len(completion)) for completion in completions]
420	```
421	
422	You can test it as follows:
423	
424	```python
425	>>> prompts = ["The sky is", "The sun is"]
426	>>> completions = [" blue.", " in the sky."]
427	>>> completion_ids = [[6303, 13], [304, 279, 12884, 13]]  # not used in the reward function, but the trainer will pass it
428	>>> reward_func(prompts=prompts, completions=completions, completion_ids=completion_ids)
429	[6.0, 12.0]
430	```
431	
432	#### Example 2: Reward completions with a specific format
433	
434	Below is an example of a reward function that checks if the completion has a specific format. This example is inspired by the _format reward_ function used in the paper [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://huggingface.co/papers/2501.12948).
435	It is designed for a conversational format, where prompts and completions consist of structured messages.
436	
437	```python
438	import re
439	
440	def format_reward_func(completions, **kwargs):
441	    """Reward function that checks if the completion has a specific format."""
442	    pattern = r"^&lt;think>.*?&lt;/think>&lt;answer>.*?&lt;/answer>$"
443	    completion_contents = [completion[0]["content"] for completion in completions]
444	    matches = [re.match(pattern, content) for content in completion_contents]
445	    return [1.0 if match else 0.0 for match in matches]
446	```
447	
448	You can test this function as follows:
449	
450	```python
451	>>> prompts = [
452	...     [{"role": "assistant", "content": "What is the result of (1 + 2) * 4?"}],
453	...     [{"role": "assistant", "content": "What is the result of (3 + 1) * 2?"}],
454	... ]
455	>>> completions = [
456	...     [{"role": "assistant", "content": "&lt;think>The sum of 1 and 2 is 3, which we multiply by 4 to get 12.&lt;/think>&lt;answer>(1 + 2) * 4 = 12&lt;/answer>"}],
457	...     [{"role": "assistant", "content": "The sum of 3 and 1 is 4, which we multiply by 2 to get 8. So (3 + 1) * 2 = 8."}],
458	... ]
459	>>> format_reward_func(prompts=prompts, completions=completions)
460	[1.0, 0.0]
461	```
462	
463	#### Example 3: Reward completions based on a reference
464	
465	Below is an example of a reward function that checks if the completion is correct. This example is inspired by the _accuracy reward_ function used in the paper [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://huggingface.co/papers/2501.12948).
466	This example is designed for [standard format](dataset_formats#standard), where the dataset contains a column named `ground_truth`.
467	
468	```python
469	import re
470	
471	def reward_func(completions, ground_truth, **kwargs):
472	    # Regular expression to capture content inside \boxed{}
473	    matches = [re.search(r"\\boxed\{(.*?)\}", completion) for completion in completions]
474	    contents = [match.group(1) if match else "" for match in matches]
475	    # Reward 1 if the content is the same as the ground truth, 0 otherwise
476	    return [1.0 if c == gt else 0.0 for c, gt in zip(contents, ground_truth)]
477	```
478	
479	You can test this function as follows:
480	
481	```python
482	>>> prompts = ["Problem: Solve the equation $2x + 3 = 7$. Solution:", "Problem: Solve the equation $3x - 5 = 10$."]
483	>>> completions = [r" The solution is \boxed{2}.", r" The solution is \boxed{6}."]
484	>>> ground_truth = ["2", "5"]
485	>>> reward_func(prompts=prompts, completions=completions, ground_truth=ground_truth)
486	[1.0, 0.0]
487	```
488	
489	#### Example 4: Multi-task reward functions
490	
491	Below is an example of using multiple reward functions in the [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer). In this example, we define two task-specific reward functions: `math_reward_func` and `coding_reward_func`. The `math_reward_func` rewards math problems based on their correctness, while the `coding_reward_func` rewards coding problems based on whether the solution works.
492	
493	```python
494	from datasets import Dataset
495	from trl import GRPOTrainer
496	
497	# Define a dataset that contains both math and coding problems
498	dataset = Dataset.from_list(
499	    [
500	        {"prompt": "What is 2+2?", "task": "math"},
501	        {"prompt": "Write a function that returns the sum of two numbers.", "task": "code"},
502	        {"prompt": "What is 3*4?", "task": "math"},
503	        {"prompt": "Write a function that returns the product of two numbers.", "task": "code"},
504	    ]
505	)
506	
507	# Math-specific reward function
508	def math_reward_func(prompts, completions, task, **kwargs):
509	    rewards = []
510	    for prompt, completion, t in zip(prompts, completions, task):
511	        if t == "math":
512	            # Calculate math-specific reward
513	            correct = check_math_solution(prompt, completion)
514	            reward = 1.0 if correct else -1.0
515	            rewards.append(reward)
516	        else:
517	            # Return None for non-math tasks
518	            rewards.append(None)
519	    return rewards
520	
521	# Coding-specific reward function
522	def coding_reward_func(prompts, completions, task, **kwargs):
523	    rewards = []
524	    for prompt, completion, t in zip(prompts, completions, task):
525	        if t == "coding":
526	            # Calculate coding-specific reward
527	            works = test_code_solution(prompt, completion)
528	            reward = 1.0 if works else -1.0
529	            rewards.append(reward)
530	        else:
531	            # Return None for non-coding tasks
532	            rewards.append(None)
533	    return rewards
534	
535	# Use both task-specific reward functions
536	trainer = GRPOTrainer(
537	    model="Qwen/Qwen2.5-0.5B-Instruct",
538	    reward_funcs=[math_reward_func, coding_reward_func],
539	    train_dataset=dataset,
540	)
541	
542	trainer.train()
543	```
544	
545	In this example, the `math_reward_func` and `coding_reward_func` are designed to work with a mixed dataset that contains both math and coding problems. The `task` column in the dataset is used to determine which reward function to apply to each problem. If there is no relevant reward function for a sample in the dataset, the reward function will return `None`, and the [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer) will continue with the valid functions and tasks. This allows the [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer) to handle multiple reward functions with different applicability.
546	
547	Note that the [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer) will ignore the `None` rewards returned by the reward functions and only consider the rewards returned by the relevant functions. This ensures that the model is trained on the relevant tasks and ignores the tasks for which there is no relevant reward function.
548	
549	#### Example 5: Asynchronous reward functions
550	
551	Custom reward functions can also be defined as `async def` coroutines. This is useful if your reward depends on slow I/O (for example, calling a remote service). When you pass multiple async reward functions, [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer) executes them concurrently so their latency overlaps.
552	
553	Below is a minimal example of an async reward function that simulates an I/O-bound operation:
554	
555	```python
556	import asyncio
557	
558	async def async_reward_func(prompts, completions, **kwargs):
559	    # Simulate an I/O-bound call (e.g., HTTP request, database lookup)
560	    await asyncio.sleep(0.01)
561	    # Simple toy reward: 1.0 if the completion is non-empty, else 0.0
562	    return [1.0 if completion else 0.0 for completion in completions]
563	```
564	
565	#### Example 6: Logging extra columns and metrics
566	
567	Below is an example of a reward function that logs extra columns to the completions table and scalar metrics as plots.
568	
569	```python
570	import re
571	
572	def reward_func(completions, ground_truth, log_extra=None, log_metric=None, **kwargs):
573	    extracted = [re.search(r"\\boxed\{(.*?)\}", c) for c in completions]
574	    extracted = [m.group(1) if m else None for m in extracted]
575	    rewards = [1.0 if e == gt else 0.0 for e, gt in zip(extracted, ground_truth)]
576	
577	    if log_extra:
578	        log_extra("golden_answer", list(ground_truth))
579	        log_extra("extracted_answer", [e or "[none]" for e in extracted])
580	
581	    if log_metric:
582	        log_metric("accuracy", sum(rewards) / len(rewards))
583	
584	    return rewards
585	```
586	
587	#### Passing the reward function to the trainer
588	
589	To use your custom reward function, pass it to the [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer) as follows:
590	
591	```python
592	from trl import GRPOTrainer
593	
594	trainer = GRPOTrainer(
595	    reward_funcs=reward_func,
596	    ...,
597	)
598	```
599	
600	You can pass several reward functions as a list; this list may include both synchronous and asynchronous functions:
601	
602	```python
603	from trl import GRPOTrainer
604	
605	trainer = GRPOTrainer(
606	    reward_funcs=[reward_func, async_reward_func1, async_reward_func2],
607	    ...,
608	)
609	```
610	
611	and the reward will be computed as the sum of the rewards from each function, or the weighted sum if `reward_weights` is provided in the config.
612	
613	Note that [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer) supports multiple reward functions of different types. See the parameters documentation for more details.
614	
615	### Rapid Experimentation for GRPO
616	
617	RapidFire AI is an open-source experimentation engine that sits on top of TRL and lets you launch multiple GRPO configurations at once, even on a single GPU. Instead of trying configurations sequentially, RapidFire lets you **see all their learning curves earlier, stop underperforming runs, and clone promising ones with new settings in flight** without restarting. For more information, see [RapidFire AI Integration](rapidfire_integration).
618	
619	## Agent Training
620	
621	GRPO supports **agent training** through the `tools` argument in [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer).
622	This parameter expects a list of Python functions (sync or async) that define the tools available to the agent:
623	
624	```python
625	from trl import GRPOTrainer
626	
627	trainer = GRPOTrainer(
628	    tools=[tool1, tool2],
629	    ...,
630	)
631	```
632	
633	Each tool must be a standard Python function with **type-hinted arguments and return types**, along with a **Google-style docstring** describing its purpose, arguments, and return value.
634	For more details, see the [Passing tools guide](https://huggingface.co/docs/transformers/en/chat_extras#passing-tools).
635	
636	> [!TIP]
637	> The GRPO tool call loop requires the chat template to be *prefix-preserving* (appending a tool message must not change how earlier messages are rendered). For known model families (e.g. Qwen3, DeepSeek-V3), TRL automatically swaps in a patched training template when tools are enabled. See [Chat Templates](chat_templates#training-templates) for the full list.
638	
639	Example:
640	
641	```python
642	from trl import GRPOTrainer
643	
644	def multiply(a: int, b: int) -> int:
645	    """
646	    Multiplies two integers.
647	
648	    Args:
649	        a: The first integer.
650	        b: The second integer.
651	
652	    Returns:
653	        The product of the two integers.
654	    """
655	    return a * b
656	
657	async def async_add(a: int, b: int) -> int:
658	    """
659	    Asynchronously adds two integers.
660	
661	    Args:
662	        a: The first integer.
663	        b: The second integer.
664	
665	    Returns:
666	        The sum of the two integers.
667	    """
668	    return a + b
669	
670	trainer = GRPOTrainer(
671	    tools=[multiply, async_add],
672	    ...,
673	)
674	```
675	
676	You can also provide tools through `environment_factory`. In this mode, [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer) creates one environment instance per rollout and exposes the environment's public methods as tools.
677	
678	> [!IMPORTANT]
679	> `environment_factory` requires `transformers>=5.2.0`.
680	
681	The following is a minimal example of using `environment_factory` to define a simple environment with an `increment` method, which is exposed as a tool to the agent:
682	
683	```python
684	from datasets import Dataset
685	from trl import GRPOConfig, GRPOTrainer
686	
687	instructions = [f"Increment the counter by {i}." for i in range(1, 7)]
688	dataset = Dataset.from_dict({"prompt": [[{"role": "user", "content": instruction}] for instruction in instructions]})
689	
690	def reward_func(environments, **kwargs):  # dummy reward: the reward is the current value of the counter
691	    return [environment.counter for environment in environments]
692	
693	class IncrementEnv:
694	    def reset(self, **kwargs) -> str | None:  # required; receives sampled row fields as kwargs (e.g., `prompt`)
695	        self.counter = 0
696	        return "Counter reset to 0.\n"
697	
698	    def increment(self, step: int) -> int:  # the other public methods of the environment are exposed as tools
699	        """
700	        Increment the internal counter.
701	
702	        Args:
703	            step: Value to add to the counter.
704	
705	        Returns:
706	            The updated counter value.
707	        """
708	        self.counter += step
709	        return self.counter
710	
711	trainer = GRPOTrainer(
712	    model="Qwen/Qwen3-0.6B",
713	    args=GRPOConfig(chat_template_kwargs={"enable_thinking": False}),
714	    train_dataset=dataset,
715	    reward_funcs=reward_func,
716	    environment_factory=IncrementEnv,
717	)
718	trainer.train()
719	```
720	
721	`reset` can return either `None` or a string. In GRPO, when it returns a string, that string is appended to the last user message before generation.
722	
723	### Multimodal Tool Responses
724	
725	Tools can return images alongside text by returning a list of content blocks. This is useful for VLM agent training where the tool provides visual feedback (e.g., screenshots, plots, camera captures).
726	
727	```python
728	from PIL import Image
729	
730	def take_screenshot() -> list:
731	    """
732	    Takes a screenshot of the current screen.
733	
734	    Returns:
735	        The screenshot image with a description.
736	    """
737	    img = Image.open("screenshot.png")
738	    return [{"type": "image", "image": img}, {"type": "text", "text": "Here is the screenshot."}]
739	```
740	
741	The returned images are automatically injected into the conversation and passed to the VLM for subsequent generation turns.
742	
743	### Supported Models
744	
745	Tested with:
746	
747	- [**Gemma4**](https://huggingface.co/collections/google/gemma-4) — e.g., `google/gemma-4-E2B-it`
748	- **GLM-4-MoE** ([4.5](https://huggingface.co/collections/zai-org/glm-45), [4.6](https://huggingface.co/collections/zai-org/glm-46) or [4.7](https://huggingface.co/collections/zai-org/glm-47)) — e.g., `zai-org/GLM-4.7`
749	- [**GPT-OSS**](https://huggingface.co/collections/openai/gpt-oss) — e.g., `openai/gpt-oss-20b`
750	- [**Llama 3.1**](https://huggingface.co/collections/meta-llama/llama-31) — e.g., `meta-llama/Llama-3.1-8B-Instruct`
751	- [**Llama 3.2**](https://huggingface.co/collections/meta-llama/llama-32) — e.g., `meta-llama/Llama-3.2-3B-Instruct`
752	- [**Qwen2.5**](https://huggingface.co/collections/Qwen/qwen25) — e.g., `Qwen/Qwen2.5-0.5B-Instruct`
753	- [**Qwen3**](https://huggingface.co/collections/Qwen/qwen3) — e.g., `Qwen/Qwen3-0.6B`
754	- [**Qwen3-VL**](https://huggingface.co/collections/Qwen/qwen3-vl) — e.g., `Qwen/Qwen3-VL-2B-Instruct`
755	- [**Qwen3.5**](https://huggingface.co/collections/Qwen/qwen35) — e.g., `Qwen/Qwen3.5-2B`
756	- [**Qwen3.6**](https://huggingface.co/collections/Qwen/qwen36) — e.g., `Qwen/Qwen3.6-35B-A3B`
757	
758	> [!TIP]
759	> Compatibility with all LLMs is not guaranteed. If you believe a model should be supported, feel free to open an issue on GitHub — or better yet, submit a pull request with the required changes.
760	
761	### Quick Start
762	
763	Use [grpo\_agent.py](https://github.com/huggingface/trl/blob/main/examples/scripts/grpo_agent.py) to fine-tune a LLM for agentic workflows.
764	
765	```bash
766	accelerate launch \
767	  --config_file=examples/accelerate_configs/deepspeed_zero3.yaml \
768	  examples/scripts/grpo_agent.py \
769	  --model_name_or_path Qwen/Qwen3-0.6B
770	  ...
771	```
772	
773	## Vision-Language Model (VLM) Training
774	
775	GRPO supports training Vision-Language Models (VLMs) on multimodal datasets containing both text and images.
776	
777	### Supported Models
778	
779	Tested with:
780	
781	- **Gemma3** — e.g., `google/gemma-3-4b-it`
782	- **LLaVA-NeXT** — e.g., `llava-hf/llava-v1.6-mistral-7b-hf`
783	- **Qwen2-VL** — e.g., `Qwen/Qwen2-VL-2B-Instruct`
784	- **Qwen2.5-VL** — e.g., `Qwen/Qwen2.5-VL-3B-Instruct`
785	- **SmolVLM2** — e.g., `HuggingFaceTB/SmolVLM2-2.2B-Instruct`
786	  
787	> [!TIP]
788	> Compatibility with all VLMs is not guaranteed. If you believe a model should be supported, feel free to open an issue on GitHub — or better yet, submit a pull request with the required changes.
789	
790	### Quick Start
791	
792	Use [grpo\_vlm.py](https://github.com/huggingface/trl/blob/main/examples/scripts/grpo_vlm.py) to fine-tune a VLM. Example command for training on [`lmms-lab/multimodal-open-r1-8k-verified`](https://huggingface.co/datasets/lmms-lab/multimodal-open-r1-8k-verified):
793	
794	```bash
795	accelerate launch \
796	  --config_file=examples/accelerate_configs/deepspeed_zero3.yaml \
797	  examples/scripts/grpo_vlm.py \
798	  --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
799	  --output_dir grpo-Qwen2.5-VL-3B-Instruct \
800	  --learning_rate 1e-5 \
801	  --dtype bfloat16 \
802	  --max_completion_length 1024 \
803	  --use_vllm \
804	  --vllm_mode colocate \
805	  --use_peft \
806	  --lora_target_modules "q_proj", "v_proj" \
807	  --log_completions
808	```
809	
810	### Configuration Tips
811	
812	- Use LoRA on vision-language projection layers
813	- Enable 4-bit quantization to reduce memory usage
814	- VLMs are memory-intensive — start with smaller batch sizes
815	- Most models are compatible with vLLM (`server` and `colocate` modes)
816	
817	### Dataset Format
818	
819	Each training sample should include:
820	
821	- `prompt`: Text formatted via the processor's chat template
822	- `image`/`images`: PIL Image or list of PIL Images
823	
824	The trainer automatically handles image-to-tensor conversion via the model’s image processor.
825	
826	## GRPOTrainer[[trl.GRPOTrainer]]
827	
828	#### trl.GRPOTrainer[[trl.GRPOTrainer]]
829	
830	[Source](https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_trainer.py#L133)
831	
832	Trainer for the Group Relative Policy Optimization (GRPO) method. This algorithm was initially proposed in the
833	paper [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language
834	Models](https://huggingface.co/papers/2402.03300).
835	
836	Example:
837	
838	```python
839	from trl import GRPOTrainer
840	from trl.rewards import accuracy_reward
841	from datasets import load_dataset
842	
843	dataset = load_dataset("trl-lib/DeepMath-103K", split="train")
844	
845	trainer = GRPOTrainer(
846	    model="Qwen/Qwen2.5-0.5B-Instruct",
847	    reward_funcs=accuracy_reward,
848	    train_dataset=dataset,
849	)
850	trainer.train()
851	```
852	
853	traintrl.GRPOTrainer.trainhttps://github.com/huggingface/trl/blob/main/transformers/trainer.py#L1325[{"name": "resume_from_checkpoint", "val": ": str | bool | None = None"}, {"name": "trial", "val": ": optuna.Trial | dict[str, Any] | None = None"}, {"name": "ignore_keys_for_eval", "val": ": list[str] | None = None"}]- **resume_from_checkpoint** (`str` or `bool`, *optional*) --
854	  If a `str`, local path to a saved checkpoint as saved by a previous instance of `Trainer`. If a
855	  `bool` and equals `True`, load the last checkpoint in *args.output_dir* as saved by a previous instance
856	  of `Trainer`. If present, training will resume from the model/optimizer/scheduler states loaded here.
857	- **trial** (`optuna.Trial` or `dict[str, Any]`, *optional*) --
858	  The trial run or the hyperparameter dictionary for hyperparameter search.
859	- **ignore_keys_for_eval** (`list[str]`, *optional*) --
860	  A list of keys in the output of your model (if it is a dictionary) that should be ignored when
861	  gathering predictions for evaluation during the training.0`~trainer_utils.TrainOutput`Object containing the global step count, training loss, and metrics.
862	
863	Main training entry point.
864	
865	**Parameters:**
866	
867	model (`str` or [PreTrainedModel](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel) or [PeftModel](https://huggingface.co/docs/peft/main/en/package_reference/peft_model#peft.PeftModel)) : Model to be trained. Can be either:  - A string, being the *model id* of a pretrained model hosted inside a model repo on huggingface.co, or a path to a *directory* containing model weights saved using [save_pretrained](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel.save_pretrained), e.g., `'./my_model_directory/'`. The model is loaded using `&lt;ModelArchitecture>.from_pretrained` (where `&lt;ModelArchitecture>` is derived from the model config) with the keyword arguments in `args.model_init_kwargs`. - A [PreTrainedModel](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel) object. Only causal language models are supported. - A [PeftModel](https://huggingface.co/docs/peft/main/en/package_reference/peft_model#peft.PeftModel) object. Only causal language models are supported.
868	
869	reward_funcs (`RewardFunc | list[RewardFunc]`) : Reward functions to be used for computing the rewards. To compute the rewards, we call all the reward functions with the prompts and completions and sum the rewards. Can be either:  - A single reward function, such as: - A string: The *model ID* of a pretrained model hosted inside a model repo on huggingface.co, or a path to a *directory* containing model weights saved using [save_pretrained](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel.save_pretrained), e.g., `'./my_model_directory/'`. The model is loaded using [from_pretrained](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoModelForSequenceClassification.from_pretrained) with `num_labels=1` and the keyword arguments in `args.model_init_kwargs`. - A [PreTrainedModel](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel) object: Only sequence classification models are supported. - A custom reward function: The function is provided with the prompts and the generated completions, plus any additional columns in the dataset. It should return a list of rewards. Custom reward functions can be either synchronous or asynchronous and can also return `None` when the reward is not applicable to those samples. This is useful for multi-task training where different reward functions apply to different types of samples. When a reward function returns `None` for a sample, that reward function is excluded from the reward calculation for that sample. For more details, see [Using a custom reward function](#using-a-custom-reward-function).  The trainer's state is also passed to the reward function. The trainer's state is an instance of [TrainerState](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.TrainerState) and can be accessed by accessing the `trainer_state` argument to the reward function's signature. - A list of reward functions, where each item can independently be any of the above types. Mixing different types within the list (e.g., a string model ID and a custom reward function) is allowed.
870	
871	args ([GRPOConfig](/docs/trl/main/en/grpo_trainer#trl.GRPOConfig), *optional*) : Configuration for this trainer. If `None`, a default configuration is used.
872	
873	train_dataset ([Dataset](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset) or [IterableDataset](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.IterableDataset)) : Dataset to use for training. It must include a column `"prompt"`. Any additional columns in the dataset is ignored. The format of the samples can be either:  - [Standard](dataset_formats#standard): Each sample contains plain text. - [Conversational](dataset_formats#conversational): Each sample contains structured messages (e.g., role and content).
874	
875	eval_dataset ([Dataset](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset), [IterableDataset](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.IterableDataset) or `dict[str, Dataset | IterableDataset]`) : Dataset to use for evaluation. It must meet the same requirements as `train_dataset`.
876	
877	processing_class ([PreTrainedTokenizerBase](https://huggingface.co/docs/transformers/main/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase), [ProcessorMixin](https://huggingface.co/docs/transformers/main/en/main_classes/processors#transformers.ProcessorMixin), *optional*) : Processing class used to process the data. The padding side must be set to "left". If `None`, the processing class is loaded from the model's name with [from_pretrained](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoProcessor.from_pretrained). A padding token, `tokenizer.pad_token`, must be set. If the processing class has not set a padding token, `tokenizer.eos_token` will be used as the default.
878	
879	reward_processing_classes ([PreTrainedTokenizerBase](https://huggingface.co/docs/transformers/main/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase) or `list[PreTrainedTokenizerBase]`, *optional*) : Processing classes corresponding to the reward functions specified in `reward_funcs`. Can be either:  - A single processing class: Used when `reward_funcs` contains only one reward function. - A list of processing classes: Must match the order and length of the reward functions in `reward_funcs`. If set to `None`, or if an element of the list corresponding to a [PreTrainedModel](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel) is `None`, the tokenizer for the model is automatically loaded using [from_pretrained](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoTokenizer.from_pretrained). For elements in `reward_funcs` that are custom reward functions (not [PreTrainedModel](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel)), the corresponding entries in `reward_processing_classes` are ignored.
880	
881	callbacks (list of [TrainerCallback](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.TrainerCallback), *optional*) : List of callbacks to customize the training loop. Will add those to the list of default callbacks detailed in [here](https://huggingface.co/docs/transformers/main_classes/callback).  If you want to remove one of the default callbacks used, use the [remove_callback](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.Trainer.remove_callback) method.
882	
883	optimizers (`tuple[torch.optim.Optimizer | None, torch.optim.lr_scheduler.LambdaLR | None]`, *optional*, defaults to `(None, None)`) : A tuple containing the optimizer and the scheduler to use. Will default to an instance of `AdamW` on your model and a scheduler given by [get_linear_schedule_with_warmup](https://huggingface.co/docs/transformers/main/en/main_classes/optimizer_schedules#transformers.get_linear_schedule_with_warmup) controlled by `args`.
884	
885	peft_config ([PeftConfig](https://huggingface.co/docs/peft/main/en/package_reference/config#peft.PeftConfig), *optional*) : PEFT configuration used to wrap the model. If `None`, the model is not wrapped.
886	
887	tools (list of `Callable`, *optional*) : A list of callable tool functions (sync or async) that the model can invoke during generation. Each tool should be a standard Python function with properly type-hinted arguments and return values, and a Google-style docstring describing its purpose, arguments, and return value. For more details, see: https://huggingface.co/docs/transformers/en/chat_extras#passing-tools. The model uses the function's name, type hints, and docstring to determine how to call it. Ensure that the model's chat template supports tool use and that it has been fine-tuned for tool calling.
888	
889	rollout_func (`RolloutFunc`, *optional*) : Function to use for generating completions. It receives the list of prompts allocated to the current process and the trainer instance. It must return a dict with `"prompt_ids"`, `"completion_ids"`, and `"logprobs"` fields, and can optionally return `"logprob_token_ids"` (same shape as `"logprobs"`). Any other fields are forwarded to the reward functions. The function receives the raw per-process prompt slice with no duplication; it is responsible for returning the correct number of completions per prompt (see `num_generations` / `num_generations_eval` on the trainer). This feature is experimental and may change or be removed at any time without prior notice.
890	
891	environment_factory (`EnvironmentFactory`, *optional*) : A callable that creates and returns an environment instance. The environment class should define methods that can be invoked as tools during generation. Each method should comply with the same requirements as the `tools` described above. If `environment_factory` is provided, an instance of the environment is created for each generation in the batch, allowing for parallel and independent interactions. The environment must also implement a callable `reset` method that can be used to reset state between generations. The `reset` method should return either `None` or a string: when it returns a string, that string is appended to the last user message before generation. This feature is experimental and may change or be removed at any time without prior notice.
892	
893	**Returns:**
894	
895	``~trainer_utils.TrainOutput``
896	
897	Object containing the global step count, training loss, and metrics.
898	#### save_model[[trl.GRPOTrainer.save_model]]
899	
900	[Source](https://github.com/huggingface/trl/blob/main/transformers/trainer.py#L3752)
901	
902	Will save the model, so you can reload it using `from_pretrained()`.
903	
904	Will only save from the main process.
905	#### push_to_hub[[trl.GRPOTrainer.push_to_hub]]
906	
907	[Source](https://github.com/huggingface/trl/blob/main/transformers/trainer.py#L3999)
908	
909	Upload `self.model` and `self.processing_class` to the 🤗 model hub on the repo `self.args.hub_model_id`.
910	
911	**Parameters:**
912	
913	commit_message (`str`, *optional*, defaults to `"End of training"`) : Message to commit while pushing.
914	
915	blocking (`bool`, *optional*, defaults to `True`) : Whether the function should return only when the `git push` has finished.
916	
917	token (`str`, *optional*, defaults to `None`) : Token with write permission to overwrite Trainer's original args.
918	
919	revision (`str`, *optional*) : The git revision to commit from. Defaults to the head of the "main" branch.
920	
921	kwargs (`dict[str, Any]`, *optional*) : Additional keyword arguments passed along to `~Trainer.create_model_card`.
922	
923	**Returns:**
924	
925	The URL of the repository where the model was pushed if `blocking=False`, or a `Future` object tracking the
926	progress of the commit if `blocking=True`.
927	
928	## GRPOConfig[[trl.GRPOConfig]]
929	
930	#### trl.GRPOConfig[[trl.GRPOConfig]]
931	
932	[Source](https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_config.py#L23)
933	
934	Configuration class for the [GRPOTrainer](/docs/trl/main/en/gspo_token#trl.GRPOTrainer).
935	
936	This class includes only the parameters that are specific to GRPO training. For a full list of training arguments,
937	please refer to the [TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments) documentation. Note that default values in this class may
938	differ from those in [TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments).
939	
940	Using [HfArgumentParser](https://huggingface.co/docs/transformers/main/en/internal/trainer_utils#transformers.HfArgumentParser) we can turn this class into
941	[argparse](https://docs.python.org/3/library/argparse#module-argparse) arguments that can be specified on the
942	command line.
943	
944	> [!NOTE]
945	> These parameters have default values different from [TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments):
946	> - `logging_steps`: Defaults to `10` instead of `500`.
947	> - `gradient_checkpointing`: Defaults to `True` instead of `False`.
948	> - `bf16`: Defaults to `True` if `fp16` is not set, instead of `False`.
949	> - `learning_rate`: Defaults to `1e-6` instead of `5e-5`.
950	
951	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "e2e04523-55a4-4fa7-a78e-81d80368b3b9"
}
```

</details>

---

### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "description": "Running grep -A 5 \"def format_reward_fn\\|def f1_reward_fn…",
  "usage": {
    "total_tokens": 59233,
    "tool_uses": 18,
    "duration_ms": 80790
  },
  "last_tool_name": "Bash",
  "uuid": "29405b8e-f731-4e0e-a4ea-79968966ef1e",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_013TZzfPFeoramfx2JDsEF4G`</summary>

```json
{
  "command": "grep -A 5 \"def format_reward_fn\\|def f1_reward_fn\\|def __call__\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "e0d10ca4-e679-4877-a557-376051f8d9c8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018U9oyJLujWCCK2m86HVdVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 21097,
      "cache_read_input_tokens": 38066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21097,
        "ephemeral_1h_input_tokens": 0
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

_source line 73 · 2026-05-14T07:02:26.508Z_

<details><summary>↩ Tool result · `toolu_013TZzfPFeoramfx2JDsEF4G`</summary>

```text
def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
    """格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。"""
    rewards = []
    for text in completions:
        parsed = _parse_json_output(text)
        if not isinstance(parsed, list):
--
def f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:
    """F1 奖励: 预测三元组与 gold 三元组的 micro-F1。

    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。
    completions 中每 num_generations 个对应同一个 prompt。
    """
--
    def __call__(
        self,
        completions: list[str],
        all_sents: list[str],
        gold_triples: list[str],
        **kwargs,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "4dcdec0e-39e9-44c6-8948-4f06ac3d3117"
}
```

</details>

---

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a25ff345935908c50",
  "tool_use_id": "toolu_01G9kqGcKusX9a1cBvN8GPbC",
  "status": "completed",
  "output_file": "",
  "summary": "TRL 1.1.0 GRPO reward kwargs",
  "usage": {
    "total_tokens": 59969,
    "tool_uses": 18,
    "duration_ms": 143099
  },
  "uuid": "9fc2cc3d-2dd5-4425-959c-6c9154c16b26",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7"
}
```

---

### Tool result

_source line 75 · 2026-05-14T07:03:28.747Z_

<details><summary>↩ Tool result · `toolu_01G9kqGcKusX9a1cBvN8GPbC`</summary>

````text
Perfect! Now I have all the information needed. Let me create a comprehensive response.

## Report: TRL 1.1.0 GRPOTrainer Dataset Column Forwarding to Reward Functions

**Answer: YES - TRL 1.1.0 GRPOTrainer automatically forwards extra dataset columns to reward functions as kwargs.**

### How It Works

According to the official HuggingFace TRL documentation, GRPOTrainer has explicit support for passing dataset columns to reward functions:

**From the documentation** (section "Using a custom reward function"):
> All column names (but `prompt`) that the dataset may have are passed to the reward function. For example, if the dataset contains a column named `ground_truth`, the function will be called with `ground_truth` as a keyword argument.

The key mechanism is that GRPOTrainer inspects the dataset columns and:
1. Automatically extracts any columns beyond "prompt" 
2. Passes them as keyword arguments (`**kwargs`) to each reward function during training
3. The easiest way to receive these columns is to use `**kwargs` in the reward function signature

### Real-World Example from Your Project

Your project at `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py` demonstrates this perfectly:

**Dataset columns** (line 291-295):
```python
dataset_items.append({
    "prompt": prompt,
    "gold_triples": json.dumps(gold_triples, ensure_ascii=False),
    "all_sents": json.dumps(ref.sents, ensure_ascii=False),
})
```

**Reward functions receiving those columns**:

1. **format_reward_fn** (line 53) - simple case with `**kwargs`:
```python
def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
```

2. **f1_reward_fn** (line 75) - explicitly names the `gold_triples` parameter:
```python
def f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:
```

3. **CEDRewardWrapper.__call__** (line 164-169) - explicitly names both parameters:
```python
def __call__(
    self,
    completions: list[str],
    all_sents: list[str],
    gold_triples: list[str],
    **kwargs,
) -> list[float]:
```

All three reward functions are invoked by GRPOTrainer (line 436) via:
```python
trainer = GRPOTrainer(
    ...
    reward_funcs=[format_reward_fn, f1_reward_fn, ced_wrapper],
    ...
)
```

### Mechanism Details

- **No special configuration needed**: You don't need to specify which columns to pass; GRPOTrainer infers this automatically
- **Parameter matching**: Reward functions can explicitly name the columns they need (like `gold_triples`), or use `**kwargs` to capture everything
- **Multiple generations**: When `num_generations > 1`, the dataset columns are replicated to match the number of completions, so the reward function receives properly aligned batches
- **Index alignment**: For columns like `gold_triples` and `all_sents`, the code manually handles the indexing (via `num_gen = len(completions) // len(all_sents)`) to map completions back to their source prompts

### Official Documentation Examples

The HuggingFace documentation provides Example 4 (multi-task reward functions) showing exactly this pattern with a custom `task` column being passed to different reward functions.

---

**Sources:**
- [HuggingFace GRPO Trainer Documentation](https://huggingface.co/docs/trl/main/en/grpo_trainer)
- [Project grpo_trainer.py](file:///home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "a40d1a50-af95-4df2-879a-41e4fbed3a13",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to understand how TRL 1.1.0's GRPOTrainer passes extra dataset columns to reward functions.\n\nSpecifically: if the training dataset has columns beyond \"prompt\" (e.g., \"gold_triples\", \"all_sents\"), does GRPOTrainer automatically pass them as **kwargs to reward_funcs?\n\nSearch in the installed TRL package for how GRPOTrainer calls reward functions. Look at:\n1. The GRPOTrainer source code — find where reward_funcs are called during training\n2. Check if there's logic that collects non-standard dataset columns and passes them as kwargs to the reward functions\n3. Look for any \"reward_func_columns\" or similar mechanism\n\nSearch broadly — check /home/ubuntu/.agent-ml-research-idea_gen_0513_6/ and also any pip-installed trl package. Try `pip show trl` output or look in common venv/site-packages paths.\n\nReport: does TRL 1.1.0 GRPOTrainer automatically forward extra dataset columns to reward functions as kwargs? If yes, how exactly? If no, what's the mechanism?",
    "agentId": "a25ff345935908c50",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information needed. Let me create a comprehensive response.\n\n## Report: TRL 1.1.0 GRPOTrainer Dataset Column Forwarding to Reward Functions\n\n**Answer: YES - TRL 1.1.0 GRPOTrainer automatically forwards extra dataset columns to reward functions as kwargs.**\n\n### How It Works\n\nAccording to the official HuggingFace TRL documentation, GRPOTrainer has explicit support for passing dataset columns to reward functions:\n\n**From the documentation** (section \"Using a custom reward function\"):\n> All column names (but `prompt`) that the dataset may have are passed to the reward function. For example, if the dataset contains a column named `ground_truth`, the function will be called with `ground_truth` as a keyword argument.\n\nThe key mechanism is that GRPOTrainer inspects the dataset columns and:\n1. Automatically extracts any columns beyond \"prompt\" \n2. Passes them as keyword arguments (`**kwargs`) to each reward function during training\n3. The easiest way to receive these columns is to use `**kwargs` in the reward function signature\n\n### Real-World Example from Your Project\n\nYour project at `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py` demonstrates this perfectly:\n\n**Dataset columns** (line 291-295):\n```python\ndataset_items.append({\n    \"prompt\": prompt,\n    \"gold_triples\": json.dumps(gold_triples, ensure_ascii=False),\n    \"all_sents\": json.dumps(ref.sents, ensure_ascii=False),\n})\n```\n\n**Reward functions receiving those columns**:\n\n1. **format_reward_fn** (line 53) - simple case with `**kwargs`:\n```python\ndef format_reward_fn(completions: list[str], **kwargs) -> list[float]:\n```\n\n2. **f1_reward_fn** (line 75) - explicitly names the `gold_triples` parameter:\n```python\ndef f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:\n```\n\n3. **CEDRewardWrapper.__call__** (line 164-169) - explicitly names both parameters:\n```python\ndef __call__(\n    self,\n    completions: list[str],\n    all_sents: list[str],\n    gold_triples: list[str],\n    **kwargs,\n) -> list[float]:\n```\n\nAll three reward functions are invoked by GRPOTrainer (line 436) via:\n```python\ntrainer = GRPOTrainer(\n    ...\n    reward_funcs=[format_reward_fn, f1_reward_fn, ced_wrapper],\n    ...\n)\n```\n\n### Mechanism Details\n\n- **No special configuration needed**: You don't need to specify which columns to pass; GRPOTrainer infers this automatically\n- **Parameter matching**: Reward functions can explicitly name the columns they need (like `gold_triples`), or use `**kwargs` to capture everything\n- **Multiple generations**: When `num_generations > 1`, the dataset columns are replicated to match the number of completions, so the reward function receives properly aligned batches\n- **Index alignment**: For columns like `gold_triples` and `all_sents`, the code manually handles the indexing (via `num_gen = len(completions) // len(all_sents)`) to map completions back to their source prompts\n\n### Official Documentation Examples\n\nThe HuggingFace documentation provides Example 4 (multi-task reward functions) showing exactly this pattern with a custom `task` column being passed to different reward functions.\n\n---\n\n**Sources:**\n- [HuggingFace GRPO Trainer Documentation](https://huggingface.co/docs/trl/main/en/grpo_trainer)\n- [Project grpo_trainer.py](file:///home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py)"
      }
    ],
    "totalDurationMs": 143103,
    "totalTokens": 61621,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 59898,
      "output_tokens": 988,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 988,
          "cache_read_input_tokens": 59898,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 1,
      "bashCount": 10,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 3
    }
  }
}
````

</details>

---

### Assistant

_source line 76_

<details><summary>Logged reasoning block</summary>

```text
Good - TRL 1.1.0 GRPOTrainer automatically forwards extra dataset columns to reward functions as kwargs. Now let me read the accelerate config.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "a768d2bd-0911-4dac-b212-77a62d504973",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHkHS2UFSx2i8ejmH8vxMY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1601,
      "cache_read_input_tokens": 35645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1601
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

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_01SkNaJXikdrGN46zdUZDYy8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/configs/accelerate_4gpu.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "4c108a03-3cb2-42c0-94d4-54d0b4a6c4da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHkHS2UFSx2i8ejmH8vxMY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1601,
      "cache_read_input_tokens": 35645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1601
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

_source line 78 · 2026-05-14T07:03:32.476Z_

<details><summary>↩ Tool result · `toolu_01SkNaJXikdrGN46zdUZDYy8`</summary>

```text
1	compute_environment: LOCAL_MACHINE
2	distributed_type: DEEPSPEED
3	deepspeed_config:
4	  deepspeed_config_file: configs/deepspeed_zero2.json
5	  zero3_init_flag: false
6	machine_rank: 0
7	main_training_function: main
8	num_machines: 1
9	num_processes: 4
10	use_cpu: false
11	mixed_precision: bf16
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "c3e373d2-91da-4182-966b-c523541d6910",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/configs/accelerate_4gpu.yaml",
      "content": "compute_environment: LOCAL_MACHINE\ndistributed_type: DEEPSPEED\ndeepspeed_config:\n  deepspeed_config_file: configs/deepspeed_zero2.json\n  zero3_init_flag: false\nmachine_rank: 0\nmain_training_function: main\nnum_machines: 1\nnum_processes: 4\nuse_cpu: false\nmixed_precision: bf16\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information. Let me also check a potential issue: the accelerate config references `configs/deepspeed_zero2.json` as a relative path. When running from the project root, this should work. But the command-line also passes `--deepspeed freige/configs/deepspeed_zero2.json`. This could be a conflict — both the accelerate config and the GRPOConfig specify the deepspeed config. Let me think about this.

Actually, looking more carefully:
- The `accelerate_4gpu.yaml` has `deepspeed_config_file: configs/deepspeed_zero2.json` — this is relative to CWD


- The command line passes `--deepspeed freige/configs/deepspeed_zero2.json` which goes into GRPOConfig

The real issue is that the accelerate config's relative path depends on where the command is launched from. If accelerate is launched from `/root/autodl-tmp/freige/`, then `configs/deepspeed_zero2.json` resolves correctly. But if launched from `/root/autodl-tmp/`, it won't find the file since the path is relative to CWD, not to the config file's location.

There's also a potential conflict here — when using GRPOConfig with `deepspeed=`, that parameter might override the accelerate config's deepspeed settings entirely. With HuggingFace Transformers + Accelerate + DeepSpeed, if deepspeed is passed via TrainingArguments, it typically takes precedence over the accelerate config file's deepspeed configuration. The path resolution could fail if the working directory isn't set correctly when accelerate loads the config, though the trainer's deepspeed argument should take precedence. The standard HuggingFace approach is to use either the accelerate config or TrainingArguments for deepspeed, not both—when both exist, Transformers typically uses the TrainingArguments version. Now I'm wondering how TRL's GRPOTrainer handles extra columns when passing them to reward functions, specifically whether it replicates them for each generation or passes them once per prompt. but prompt) that the dataset may have are passed to the reward function."

Looking at the actual TRL source, when `num_generations > 1`, the completions list has `batch_size * num_generations` entries. The question is whether `gold_triples` also gets replicated.

Looking at TRL's code more carefully, I believe the extra columns are passed as-is from the batch, which means they have `batch_size` entries while completions have `batch_size * num_generations` entries. So the `num_gen = len(completions) // len(gold_triples)` logic in f1_reward_fn would be correct — it maps each completion back to its prompt's gold triples.

In newer TRL versions, the reward functions receive per-sample inputs where each completion gets its corresponding metadata, so `gold_triples` would have the same length as `completions` with each entry replicated per generation. Either way, the indexing logic handles both scenarios correctly: if replicated, `num_gen = 1` and each completion maps to its own gold entry; if not replicated, `num_gen = num_generations` and groups of completions map to single gold entries. The code is robust to both cases.

Let me verify the exact reward function signature in TRL 1.1.0 — I need to check whether `completions` comes as a list of strings or in a different format like chat messages. I'm uncertain about the exact reward function signature in TRL 1.1.0 since the library has changed this multiple times—it could expect either plain strings or conversation dictionaries, and if it's the latter, the current code treating completions as a list of strings would fail. This is a critical issue I need to flag for verification on the actual server. Let me also check the `steps_per_epoch` calculation...

The formula doesn't account for the 4 GPUs being used, so it's overestimating total steps by 4x, which means tau will increase much slower than intended and end up lower than `tau_end`. This is a bug affecting the tau scheduler in CEDRewardWrapper.

Now I'm reconsidering how the call count actually works — the reward function gets called once per batch during training, so the call count should roughly match the number of training steps. But I need to think through whether distributed training affects this calculation.

In TRL's GRPOTrainer with DeepSpeed, the reward is computed on a single process and then broadcast, so the call count tracks the total number of steps rather than per-GPU steps. The real issue is that `total_steps` is calculated without accounting for the fact that the dataset gets sharded across GPUs in distributed training, making it `num_gpus` times larger than the actual number of steps the trainer will execute. This means the tau schedule progresses much slower than intended — a significant bug.

For the accelerate config path, the command needs to reference the correct YAML file location relative to the current working directory.  The issue is that the deepspeed config path inside the accelerate config is relative to CWD, which would point to the wrong location — though this might not matter since the `--deepspeed` flag in GRPOConfig likely overrides it anyway.

But there's a real risk: accelerate could fail during initialization if it tries to load that invalid path before the override takes effect. I should flag the potential solutions — either remove the deepspeed_config_file from accelerate entirely, fix the path to point to `freige/configs/deepspeed_zero2.json`, or use a placeholder config instead. I also need to check whether having two deepspeed configs (one from accelerate, one from the command-line argument) could cause conflicts or warnings.

Now I'm realizing the working directory matters here. The command template uses `freige/configs/...` paths, which suggests the CWD is `/root/autodl-tmp/` with freige as a subdirectory. But the project root is actually `/root/autodl-tmp/freige`, so if we're running from there, those relative paths wouldn't resolve correctly — we'd need just `configs/...` instead. And the module invocation `-m freige.training.grpo_trainer` requires freige to be importable, which depends on whether `/root/autodl-tmp/` is in the Python path.

Let me set the working directory to `/root/autodl-tmp/` to make everything consistent with the command template.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "b77fe7ba-2c4e-4849-b45c-92341782e657",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sbs2rbkNPV8GjDtvG1j6y8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 37246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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

_source line 80_

Now I have all the data. Here's the verification report.

---

## GRPO 三路对比验证报告

### 检查清单

| # | 检查项 | 状态 |
|---|--------|------|
| 1 | Stage 切换 (`--stage 1/2/3`) | **PASS** — L309: `choices=[1,2,3]`; L382-402: stage≥2 加 CED/flat_nli，stage 1 只有 format+F1 |
| 2 | SFT adapter 加载 | **PASS** — L375-378: `PeftModel.from_pretrained` → `merge_and_unload()` |
| 3 | tau 调度 | **PASS** with caveat — L147-154 初始化, L156-162 线性插值。**但 total_steps 计算有 bug**（见下） |
| 4 | TRL 1.1.0 兼容 (`processing_class=`) | **PASS** — L438: `processing_class=tokenizer` |
| 5 | SDPA attention | **PASS** — L361: `attn_implementation="sdpa"` |
| 6 | 模型路径 | **PASS** — L303: default `/root/autodl-tmp/models/Qwen3-4B` |
| 7 | DeepSpeed 注释 | **PASS** — L7-8 引用 `deepspeed_zero2.json` |
| 8 | `compute_ced_reward` hard_neg=[] 退化 | **PASS** — `ced_reward.py` L236-237: `p_neg=0.0`，reward = `max(0, p_pos) * I(p_pos>tau)` = `p_pos * I(p_pos>tau)` |
| 9 | `compute_flat_nli_reward` 签名 | **PASS** — L317-332: `(claim, cited_evidence_sents, tau)` → `{"reward", "p_pos"}` |
| 10 | ZeRO-2 配置 | **PASS** — stage 2 + CPU offload optimizer + bf16 |
| 11 | TRL extra columns → reward kwargs | **PASS** — TRL 1.1.0 自动将 dataset 非 `prompt` 列作为 kwargs 传给 reward functions |
| 12 | accelerate_4gpu.yaml | **PASS** with caveat — 4 进程, DEEPSPEED, bf16。但 deepspeed_config_file 路径可能冲突（见下） |

### 发现的问题

#### BUG 1: `total_steps` 缺少 GPU 数量因子（中等严重）

`grpo_trainer.py` L385-387:
```python
steps_per_epoch = math.ceil(
    len(train_dataset) / (args.per_device_batch_size * args.gradient_accumulation_steps)
)
```

4 卡 DDP/DeepSpeed 下，dataset 被分片到 4 个 GPU。实际 steps = `dataset_size / (per_device_bs * num_gpus * grad_accum)`。当前计算结果 **高了 4 倍**。

**影响**：tau 调度进度只走到 ~25%。tau_start=0.3, tau_end=0.5 时，实际只调度到 ~0.35 而非 0.5。

**修复**：
```python
num_gpus = int(os.environ.get("WORLD_SIZE", 1))
steps_per_epoch = math.ceil(
    len(train_dataset) / (args.per_device_batch_size * num_gpus * args.gradient_accumulation_steps)
)
```

#### BUG 2: accelerate config 与 GRPOConfig 的 DeepSpeed 路径可能冲突（低严重）

`accelerate_4gpu.yaml` L3-4:
```yaml
deepspeed_config:
  deepspeed_config_file: configs/deepspeed_zero2.json
```

命令行同时传 `--deepspeed freige/configs/deepspeed_zero2.json` 到 GRPOConfig。两个路径相对于不同位置。GRPOConfig 的 `deepspeed` 参数会覆盖 accelerate config，但 accelerate 初始化时可能先尝试加载自己的路径导致报错。

**修复建议**：从 accelerate config 中删除 `deepspeed_config_file`，只保留 `distributed_type: DEEPSPEED` 和 `zero3_init_flag: false`，让 GRPOConfig 全权管理 deepspeed config。

#### 风险项 3: TRL 1.1.0 reward function 的 completions 格式（需服务器验证）

TRL 不同版本对 completions 参数格式不一致。当前代码假设 `completions: list[str]`。部分 TRL 版本传入 `list[list[dict]]`（chat format）。需在服务器上验证：

```python
python3 -c "import trl; print(trl.__version__)"
```

然后检查 GRPOTrainer 源码中 reward function 的调用方式。

#### 风险项 4: CED 退化 vs flat_nli 不完全等价

当 `hard_negative_sents=[]` 时：
- `compute_ced_reward`: R = `max(0, p_pos - 0) * I(p_pos > tau)` = `p_pos * I(p_pos > tau)`
- `compute_flat_nli_reward`: R = `p_pos * I(p_pos > tau)`

两者等价。Stage 2 (flat_nli mode) 通过 `CEDRewardWrapper` L234 显式调用 `compute_flat_nli_reward`，正确。

### 三组提交命令

CWD = `/root/autodl-tmp/`

**Stage 1: extraction-only (format + F1)**
```bash
bash -c 'source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export WANDB_API_KEY=[REDACTED] /root/.wandb_key 2>/dev/null) && \
cd /root/autodl-tmp && \
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --deepspeed freige/configs/deepspeed_zero2.json \
  --stage 1 \
  --output_dir /root/autodl-tmp/grpo_s1 \
  --num_generations 4 \
  --reward_device cpu \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 1 \
  --learning_rate 5e-5 \
  --seed 42 \
  --wandb_run_name grpo-s1-extraction'
```

**Stage 2: flat-NLI**
```bash
bash -c 'source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export WANDB_API_KEY=[REDACTED] /root/.wandb_key 2>/dev/null) && \
cd /root/autodl-tmp && \
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --deepspeed freige/configs/deepspeed_zero2.json \
  --stage 2 \
  --tau_start 0.3 --tau_end 0.5 \
  --output_dir /root/autodl-tmp/grpo_s2 \
  --num_generations 4 \
  --reward_device cpu \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 1 \
  --learning_rate 5e-5 \
  --seed 42 \
  --wandb_run_name grpo-s2-flatnli'
```

**Stage 3: CED**
```bash
bash -c 'source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export WANDB_API_KEY=[REDACTED] /root/.wandb_key 2>/dev/null) && \
cd /root/autodl-tmp && \
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --deepspeed freige/configs/deepspeed_zero2.json \
  --stage 3 \
  --tau_start 0.3 --tau_end 0.5 \
  --output_dir /root/autodl-tmp/grpo_s3 \
  --num_generations 4 \
  --reward_device cpu \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 1 \
  --learning_rate 5e-5 \
  --seed 42 \
  --wandb_run_name grpo-s3-ced'
```

### 待修复后再提交

1. **修复 total_steps 计算**（BUG 1）— 加入 `WORLD_SIZE` 因子，否则 tau 调度不达标
2. **清理 accelerate config 的 deepspeed 路径**（BUG 2）— 防止初始化冲突
3. **服务器验证 TRL completions 格式**（风险项 3）— `pip show trl` 确认版本后检查源码

是否需要我现在修复 BUG 1 和 BUG 2？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "uuid": "78baa407-6658-42b0-b54f-58e32b4df6aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sbs2rbkNPV8GjDtvG1j6y8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 37246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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

### Task result

_source line 81_

Now I have all the data. Here's the verification report.

---

## GRPO 三路对比验证报告

### 检查清单

| # | 检查项 | 状态 |
|---|--------|------|
| 1 | Stage 切换 (`--stage 1/2/3`) | **PASS** — L309: `choices=[1,2,3]`; L382-402: stage≥2 加 CED/flat_nli，stage 1 只有 format+F1 |
| 2 | SFT adapter 加载 | **PASS** — L375-378: `PeftModel.from_pretrained` → `merge_and_unload()` |
| 3 | tau 调度 | **PASS** with caveat — L147-154 初始化, L156-162 线性插值。**但 total_steps 计算有 bug**（见下） |
| 4 | TRL 1.1.0 兼容 (`processing_class=`) | **PASS** — L438: `processing_class=tokenizer` |
| 5 | SDPA attention | **PASS** — L361: `attn_implementation="sdpa"` |
| 6 | 模型路径 | **PASS** — L303: default `/root/autodl-tmp/models/Qwen3-4B` |
| 7 | DeepSpeed 注释 | **PASS** — L7-8 引用 `deepspeed_zero2.json` |
| 8 | `compute_ced_reward` hard_neg=[] 退化 | **PASS** — `ced_reward.py` L236-237: `p_neg=0.0`，reward = `max(0, p_pos) * I(p_pos>tau)` = `p_pos * I(p_pos>tau)` |
| 9 | `compute_flat_nli_reward` 签名 | **PASS** — L317-332: `(claim, cited_evidence_sents, tau)` → `{"reward", "p_pos"}` |
| 10 | ZeRO-2 配置 | **PASS** — stage 2 + CPU offload optimizer + bf16 |
| 11 | TRL extra columns → reward kwargs | **PASS** — TRL 1.1.0 自动将 dataset 非 `prompt` 列作为 kwargs 传给 reward functions |
| 12 | accelerate_4gpu.yaml | **PASS** with caveat — 4 进程, DEEPSPEED, bf16。但 deepspeed_config_file 路径可能冲突（见下） |

### 发现的问题

#### BUG 1: `total_steps` 缺少 GPU 数量因子（中等严重）

`grpo_trainer.py` L385-387:
```python
steps_per_epoch = math.ceil(
    len(train_dataset) / (args.per_device_batch_size * args.gradient_accumulation_steps)
)
```

4 卡 DDP/DeepSpeed 下，dataset 被分片到 4 个 GPU。实际 steps = `dataset_size / (per_device_bs * num_gpus * grad_accum)`。当前计算结果 **高了 4 倍**。

**影响**：tau 调度进度只走到 ~25%。tau_start=0.3, tau_end=0.5 时，实际只调度到 ~0.35 而非 0.5。

**修复**：
```python
num_gpus = int(os.environ.get("WORLD_SIZE", 1))
steps_per_epoch = math.ceil(
    len(train_dataset) / (args.per_device_batch_size * num_gpus * args.gradient_accumulation_steps)
)
```

#### BUG 2: accelerate config 与 GRPOConfig 的 DeepSpeed 路径可能冲突（低严重）

`accelerate_4gpu.yaml` L3-4:
```yaml
deepspeed_config:
  deepspeed_config_file: configs/deepspeed_zero2.json
```

命令行同时传 `--deepspeed freige/configs/deepspeed_zero2.json` 到 GRPOConfig。两个路径相对于不同位置。GRPOConfig 的 `deepspeed` 参数会覆盖 accelerate config，但 accelerate 初始化时可能先尝试加载自己的路径导致报错。

**修复建议**：从 accelerate config 中删除 `deepspeed_config_file`，只保留 `distributed_type: DEEPSPEED` 和 `zero3_init_flag: false`，让 GRPOConfig 全权管理 deepspeed config。

#### 风险项 3: TRL 1.1.0 reward function 的 completions 格式（需服务器验证）

TRL 不同版本对 completions 参数格式不一致。当前代码假设 `completions: list[str]`。部分 TRL 版本传入 `list[list[dict]]`（chat format）。需在服务器上验证：

```python
python3 -c "import trl; print(trl.__version__)"
```

然后检查 GRPOTrainer 源码中 reward function 的调用方式。

#### 风险项 4: CED 退化 vs flat_nli 不完全等价

当 `hard_negative_sents=[]` 时：
- `compute_ced_reward`: R = `max(0, p_pos - 0) * I(p_pos > tau)` = `p_pos * I(p_pos > tau)`
- `compute_flat_nli_reward`: R = `p_pos * I(p_pos > tau)`

两者等价。Stage 2 (flat_nli mode) 通过 `CEDRewardWrapper` L234 显式调用 `compute_flat_nli_reward`，正确。

### 三组提交命令

CWD = `/root/autodl-tmp/`

**Stage 1: extraction-only (format + F1)**
```bash
bash -c 'source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export WANDB_API_KEY=[REDACTED] /root/.wandb_key 2>/dev/null) && \
cd /root/autodl-tmp && \
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --deepspeed freige/configs/deepspeed_zero2.json \
  --stage 1 \
  --output_dir /root/autodl-tmp/grpo_s1 \
  --num_generations 4 \
  --reward_device cpu \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 1 \
  --learning_rate 5e-5 \
  --seed 42 \
  --wandb_run_name grpo-s1-extraction'
```

**Stage 2: flat-NLI**
```bash
bash -c 'source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export WANDB_API_KEY=[REDACTED] /root/.wandb_key 2>/dev/null) && \
cd /root/autodl-tmp && \
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --deepspeed freige/configs/deepspeed_zero2.json \
  --stage 2 \
  --tau_start 0.3 --tau_end 0.5 \
  --output_dir /root/autodl-tmp/grpo_s2 \
  --num_generations 4 \
  --reward_device cpu \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 1 \
  --learning_rate 5e-5 \
  --seed 42 \
  --wandb_run_name grpo-s2-flatnli'
```

**Stage 3: CED**
```bash
bash -c 'source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export WANDB_API_KEY=[REDACTED] /root/.wandb_key 2>/dev/null) && \
cd /root/autodl-tmp && \
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --deepspeed freige/configs/deepspeed_zero2.json \
  --stage 3 \
  --tau_start 0.3 --tau_end 0.5 \
  --output_dir /root/autodl-tmp/grpo_s3 \
  --num_generations 4 \
  --reward_device cpu \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 1 \
  --learning_rate 5e-5 \
  --seed 42 \
  --wandb_run_name grpo-s3-ced'
```

### 待修复后再提交

1. **修复 total_steps 计算**（BUG 1）— 加入 `WORLD_SIZE` 因子，否则 tau 调度不达标
2. **清理 accelerate config 的 deepspeed 路径**（BUG 2）— 防止初始化冲突
3. **服务器验证 TRL completions 格式**（风险项 3）— `pip show trl` 确认版本后检查源码

是否需要我现在修复 BUG 1 和 BUG 2？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 291627,
  "duration_api_ms": 254782,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "652a0167-bc8e-4a7c-b9ac-5173d41f57f7",
  "total_cost_usd": 0.581203,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 25684,
    "cache_read_input_tokens": 108862,
    "output_tokens": 7387,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25684,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 6432,
        "cache_read_input_tokens": 37246,
        "cache_creation_input_tokens": 279,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 279
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 23202,
      "outputTokens": 3898,
      "cacheReadInputTokens": 539825,
      "cacheCreationInputTokens": 59898,
      "webSearchRequests": 1,
      "costUSD": 0.18154699999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 7387,
      "cacheReadInputTokens": 108862,
      "cacheCreationInputTokens": 25684,
      "webSearchRequests": 0,
      "costUSD": 0.399656,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b939aef5-7920-401e-aecc-9b22291dcb04"
}
```

</details>

---
