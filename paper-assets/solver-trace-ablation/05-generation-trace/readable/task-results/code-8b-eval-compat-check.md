# code 8b eval compat check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b-eval-compat-check_20260516T100916_result.json`
- **Structured JSON:** [`43773e7476e78f952429.json`](../../sessions/43/43773e7476e78f952429.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：完全兼容，无需修改。**

### eval_sta.py 分析

| 检查项 | 状态 | 说明 |
|--------|------|------|
| model_path | ✅ | CLI 参数，无硬编码路径 |
| tokenizer | ✅ | `AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)`，泛型加载 |
| model 加载 | ✅ | `AutoModelForCausalLM` + `device_map="auto"` + `torch_dtype="auto"`，8B 在 96GB 单卡无压力 |
| enable_thinking | ✅ | `enable_thinking=False` 传给 `apply_chat_template`，Qwen3-4B/8B 共享此接口 |
| max_new_tokens | ✅ | 默认 512，CLI 可调，与模型大小无关 |
| batch 处理 | ✅ | 逐样本推理，无 batch_size 参数，不会 OOM |
| think tag 清理 | ✅ | `re.sub(r"&lt;think>.*?&lt;/think>")` 同样适用于 8B 输出 |

### classify_h7.py 分析

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 输入格式 | ✅ | 读 eval_sta.py 产出的 JSON，操作 `formalization` 字段（FOL 字符串） |
| normalize_for_match() | ✅ | 纯字符串操作（whitespace、paren strip、quantifier normalization），模型无关 |
| H7/H1/H8 分类 | ✅ | 全部基于 FOL 文本解析，不依赖任何模型特定 schema |
| 无模型加载 | ✅ | 只读 JSON 文件，不涉及模型 |

### dry-run 状态

8B 训练刚开始（step 1），两个 output 目录只有 `reward_log.jsonl`，尚无 checkpoint 可用于 dry-run eval。base model 在 `/root/autodl-tmp/models/Qwen3-8B/` 可用，但等 checkpoint 产出后再测更有意义。

---
