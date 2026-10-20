# code research gpu prep

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_research_gpu_prep_20260515T042556_result.json`
- **Structured JSON:** [`c51b9a181cfc8ea08c17.json`](../../sessions/c5/c51b9a181cfc8ea08c17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

---

### 1. Qwen3-Reranker-0.6B 下载
- 路径: `/root/autodl-tmp/models/Qwen/Qwen3-Reranker-0.6B/`
- 大小: **1.2GB** (model.safetensors)
- 架构: `Qwen3ForCausalLM`, BF16, 28层, hidden=1024
- 来源: HuggingFace (hf-mirror.com)

### 2. QLoRA 验证
- **已装包**: peft 0.19.0, bitsandbytes 0.49.2, accelerate 1.13.0
- **Qwen3-8B 4-bit 加载**: 5.8GB VRAM (GPU 0)
- **LoRA**: r=16, alpha=32, target=[q/k/v/o_proj], 15.3M 可训练参数 (0.19%)
- **前向传播**: logits shape [1, 2, 151936]
- **反向传播**: loss=10.6452, 梯度计算正常
- **结论**: QLoRA 环境就绪

### 3. 数据转换脚本 + Dry-run
- 脚本: `/root/trace_distill_repair/convert_scoring_to_training.py`
- 输出: `/root/trace_distill_repair/pipeline_output/training_data/`

**Line 模式** (v1 backup 数据):
| 指标 | 值 |
|------|-----|
| 总样本 | 2,256 |
| keep | 38 (1.7%) |
| drop | 2,218 (98.3%) |
| 跳过(error) | 1,666 |
| token 范围 | 127 ~ 2,031 (均值 400) |
| 覆盖实例 | 38 |

**Structural 模式**:
| 指标 | 值 |
|------|-----|
| 总样本 | 351 |
| keep | 13 (3.7%) |
| drop | 338 (96.3%) |
| 跳过(error) | 140 |
| token 范围 | 134 ~ 154,093 (均值 1,553) |
| 覆盖实例 | 38 |

**注意**: keep/drop 极度不平衡（~2-4% keep），Research 阶段训练时需要考虑过采样或 weighted loss。

---
