# code p0b qwen instruct prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0b-qwen-instruct-prep_20260514T032210_result.json`
- **Structured JSON:** [`6dff787bdf659c666107.json`](../../sessions/6d/6dff787bdf659c666107.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

## 产出总结

### 1. 模型路径
`/root/autodl-tmp/models/Qwen2.5-7B-Instruct`（14.2 GB，通过 ModelScope 下载）

### 2. Config 验证
| 属性 | 值 |
|------|-----|
| model_type | qwen2 |
| hidden_size | 3584 |
| num_hidden_layers | 28 |
| num_attention_heads | 28 |
| num_key_value_heads | 4 |
| vocab_size | 151643 |

与 DeepSeek-R1-Distill-Qwen-7B 同为 `qwen2` 架构。

### 3. 与 profiling 代码兼容性
**完全兼容，不需要代码改动。**

- `load_model_and_tokenizer()` 使用 `AutoModelForCausalLM`，无模型特定逻辑
- `_find_attention_layers()` 通过 `type(module).__name__.endswith("Attention")` 匹配 `Qwen2Attention`
- 生成使用 `model.generate(do_sample=False)` — 对任意 causal LM 通用
- 未使用 chat template（raw text prompt），Instruct 模型也支持

### 4. 注意事项
- 服务器需要 `source /etc/network_turbo` 才能联网（与 AutoDL 相同的代理环境）
- HF 直连下载大文件会超时，需用 ModelScope
- GPU 2、3 正在跑 DeepSeek random masking profiling（s020/s030），GPU 0、1 可用

---
