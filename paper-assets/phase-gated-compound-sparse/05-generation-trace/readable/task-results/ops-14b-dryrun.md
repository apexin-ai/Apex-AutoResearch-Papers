# ops 14b dryrun

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b_dryrun_20260516T071726_result.json`
- **Structured JSON:** [`e0c772eaffdf77923937.json`](../../sessions/e0/e0c772eaffdf77923937.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 模型位置和大小
- **路径**: `/root/autodl-tmp/models/Qwen/Qwen2___5-14B-Instruct/`
- **Symlink**: `/root/autodl-tmp/models/Qwen/Qwen2.5-14B-Instruct` → 可用
- **大小**: 28G（8 个 safetensors 分片，全部完整）
- **架构**: Qwen2ForCausalLM, hidden_size=5120, 48 layers, GQA (40 heads / 8 KV heads), bfloat16

### Tokenizer 加载结果
- **TOKENIZER_OK**
- vocab_size=151643, model_max_length=131072
- encode 测试通过

### 脚本适配需求
现有脚本（如 `c10_gen_s020_s025.py`）默认模型路径是 `DeepSeek-R1-Distill-Qwen-7B`，通过 `--model` 参数切换即可，无需改代码。运行时传：
```
--model /root/autodl-tmp/models/Qwen/Qwen2.5-14B-Instruct
```

### Ready to run: **Yes**
模型文件完整，tokenizer 可加载，脚本支持 `--model` 参数切换。

---
