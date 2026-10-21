# ops check phi4 olmo2 readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-phi4-olmo2-readiness_20260518T205519_result.json`
- **Structured JSON:** [`3e8abce110e24a367c32.json`](../../sessions/3e/3e8abce110e24a367c32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总报告：

## 模型下载状态

| 模型 | 路径 | 大小 | Shards | 状态 |
|------|------|------|--------|------|
| **Phi-4** (14.7B, `Phi3ForCausalLM`) | `/root/autodl-tmp/models/phi-4` | 28G | 6/6 | **完整** |
| **OLMo-2-1124-7B** (7B, `Olmo2ForCausalLM`) | `/root/autodl-tmp/models/OLMo-2-1124-7B` | 28G | 6/6 | **完整** |

之前两个模型各缺 1 个 shard（Phi-4 缺 5/6，OLMo-2 缺 3/6），已通过 `hf-mirror.com` 补全。

## 其他已有模型
- Qwen2.5-14B, Qwen2.5-7B, Llama-3.1-8B, gemma-2-9b

## SFT 数据
5 个 dosage 文件完整：d000(50000), d005(50826), d025(54133), d050(58266), d100(66533)

## 训练脚本兼容性
- `train_sft.py` 使用 `AutoModelForCausalLM.from_pretrained()`，通用架构加载
- transformers 5.8.1，支持 `phi3` 和 `olmo2` model types
- **无需改代码**，直接传 `--model_name /root/autodl-tmp/models/phi-4` 或 `--model_name /root/autodl-tmp/models/OLMo-2-1124-7B` 即可

## 注意事项
- 服务器无法直连 `huggingface.co`，需设 `HF_ENDPOINT=https://hf-mirror.com`
- OLMo-2 权重为 float32（28G），训练时会自动转 bf16（取决于 training args），显存占用可能略高于预期
- Phi-4 是 14.7B 参数模型（比 Qwen2.5-14B 略小），单卡 LoRA SFT 应可行

**两个模型现在可以立即开始训练。**

---
