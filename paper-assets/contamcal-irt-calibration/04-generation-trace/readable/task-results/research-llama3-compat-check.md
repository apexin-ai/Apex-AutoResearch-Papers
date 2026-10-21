# research llama3 compat check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_llama3-compat-check_20260521T075305_result.json`
- **Structured JSON:** [`f526681e7b3fc497196b.json`](../../sessions/f5/f526681e7b3fc497196b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

兼容性报告如下：

---

## LLaMA-3.1-8B 兼容性报告

### 1. 模型可用性：需下载

`/root/autodl-tmp/models/Llama-3.1-8B/` 目录存在但**只有 README + LICENSE（68K）**，权重文件未下载。HF cache 中也无 safetensors。之前下载尝试中断（.lock 文件残留）。

**磁盘空间**：数据盘剩余 35GB，LLaMA-3.1-8B bf16 约 16GB，可容纳但偏紧（SFT 输出还需额外空间）。需要 Director 审批下载。

### 2. 训练脚本（train_sft.py）：完全兼容，零改动

- **模型加载**：`AutoModelForCausalLM` + `AutoTokenizer`，模型无关
- **LoRA target modules**：默认 `[q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj]`——**与 LLaMA-3 完全匹配**
- **Chat template**：已内置 `LLAMA3_CHAT_TEMPLATE`，`make_formatting_func` 使用 `tokenizer.apply_chat_template`，模型无关
- **Tokenizer**：无硬编码，LLaMA-3 的 tiktoken-based tokenizer 通过 AutoTokenizer 自动处理
- 脚本 docstring 已提及 "Llama-3.2-3B" 支持

### 3. Evaluate 脚本（evaluate.py）：完全兼容，零改动

- `load_model_and_tokenizer` 已有 LLaMA-3 特判：当 `tokenizer.chat_template is None` 且模型名含 "llama" 时自动设置 `LLAMA3_CHAT_TEMPLATE`
- `pad_token` fallback 到 `eos_token` 已处理
- MCQ/GSM8K/HumanEval 所有评估路径均模型无关

### 4. 数据准备脚本（prepare_sft_data.py）：完全兼容

- 纯数据处理，输出 chat-format JSONL，无模型依赖

### 5. 预估改动量：0 行

所有三个脚本对 LLaMA-3 架构完全兼容，无需任何代码修改。只需在运行时传 `--model-name /root/autodl-tmp/models/Llama-3.1-8B`。

### 6. GPU 资源估算（LLaMA-3.1-8B + LoRA r=16, A100-80G）

| 项目 | 估算 |
|------|------|
| 模型显存 (bf16) | ~16 GB |
| LoRA 参数 + optimizer states | ~2-3 GB |
| 激活 (batch=4, seq=2048, grad_ckpt) | ~8-12 GB |
| **总计** | **~26-31 GB** |
| 单 dosage 训练时间 | ~30-60 min（取决于数据量） |
| 单 benchmark eval 时间 | ~20-40 min |

A100-80G 单卡充裕，无需 QLoRA 4-bit。若启用 gradient checkpointing 可进一步降低显存。

### 阻塞项

1. **需要下载模型权重**（~16GB），需 Director 审批
2. **磁盘空间偏紧**（35GB 剩余），下载模型后仅剩 ~19GB，SFT 输出（LoRA adapter ~200MB × dosage 数）可承受，但合并后的 full model（~16GB）可能放不下——建议只保存 adapter 不 merge

---
