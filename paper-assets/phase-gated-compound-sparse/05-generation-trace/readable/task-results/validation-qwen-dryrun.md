# validation qwen dryrun

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validation_qwen-dryrun_20260514T053700_result.json`
- **Structured JSON:** [`26d48257ca749b236044.json`](../../sessions/26/26d48257ca749b236044.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。以下是验证总结：

---

## Qwen2.5-7B-Instruct 干跑验证结果

### 1. 模型完整性 ✓
- 4 个 safetensors 分片（共 ~14.3GB），config.json / tokenizer_config.json / generation_config.json 齐全

### 2. 代码兼容性 ✓ — 无需修改
- `run_profiling.py` 及整个 `pacs/profiling/` 目录中 **零** DeepSeek-specific 逻辑（无 "DeepSeek"、"deepseek" 字符串）
- `model_path` 是 CLI 参数 `--model_path`，非 hardcode
- `load_model_and_tokenizer()` 使用 `AutoModelForCausalLM` + `AutoTokenizer`，完全通用
- prompt 构建是纯文本模板 `"Solve the following math problem step by step.\n\nProblem: ...\n\nSolution:"`，不依赖 chat template
- `pad_token` 自动 fallback 到 `eos_token`（Qwen2.5 自带 pad_token `<|endoftext|>`，不会触发 fallback）
- bf16 已配置（line 71: `torch_dtype=torch.bfloat16`）

### 3. Thinking Tag 兼容性 ✓ — 不相关
- profiling 代码中 **零** thinking tag 处理。phase segmentation 完全基于 **attention sparsity quantile**（非文本标记）
- Qwen2.5-7B-Instruct 不是 reasoning 模型，不会生成 `&lt;think>` tag（那是 QwQ/Qwen3 才有的）
- DeepSeek-R1-Distill 虽然会生成 `&lt;think>` tag，但代码也没有用它做分割——所以两个模型在这方面完全一致

### 4. 架构对比

| 参数 | DeepSeek-R1-Distill-Qwen-7B | Qwen2.5-7B-Instruct |
|------|------|------|
| architecture | Qwen2ForCausalLM | Qwen2ForCausalLM |
| num_hidden_layers | 28 | 28 |
| num_attention_heads | 28 | 28 |
| num_key_value_heads | 4 | 4 |
| hidden_size | 3584 | 3584 |
| intermediate_size | 18944 | 18944 |
| vocab_size | 152064 | 152064 |
| rope_theta | 10000 | 1000000 |
| max_position_embeddings | 131072 | 32768 |

架构完全相同（同一 base model 微调），仅 rope_theta 和 max_position_embeddings 不同（不影响 profiling）。

### 5. 预估修改：零修改

### 6. 建议的 Qwen 实验命令

```bash
cd /root/autodl-tmp/pacs && CUDA_VISIBLE_DEVICES=X python -m pacs.profiling.run_profiling \
    --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct \
    --data_path /root/autodl-tmp/pacs/data/math500.json \
    --output_dir ./profiling_output/qwen25_7b_v6_importance \
    --masking_method importance
```

替换 `CUDA_VISIBLE_DEVICES=X` 为空闲 GPU 即可，无需额外参数。`--masking_method random` 同理。

---
