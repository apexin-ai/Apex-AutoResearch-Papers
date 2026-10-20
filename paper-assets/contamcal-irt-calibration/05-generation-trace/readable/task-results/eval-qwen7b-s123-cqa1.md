# eval qwen7b s123 cqa1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen7b-s123-cqa1_20260519T141614_result.json`
- **Structured JSON:** [`9346876afdf41af178e0.json`](../../sessions/93/9346876afdf41af178e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

整理发现：

**cqa1 现状**:
- GPU: RTX 4090D 24GB, 空闲 ✓
- evaluate.py v3: ✓ `/root/contamcal-irt-calibration/exp001/evaluate.py`
- 5 个 Qwen-7B s123 LoRA adapters: ✓ (lora_alpha=32, C006 合规)
- HF 数据集缓存 (mmlu, arc): ✓
- **Qwen2.5-7B 基础模型: ✗ 缺失 (需 15GB)**
- **磁盘: 仅剩 11GB，差 ~5GB**

需要释放空间。以下是与 contamcal 项目无关的可清理项：

| 目录 | 大小 | 说明 |
|------|------|------|
| `models/._____temp` | 2.0GB | 不完整的临时下载 |
| `gpt2-ms` | 4.9GB | ModelScope GPT2 缓存 |
| `gpt2-small` | 478MB | GPT2 模型 |
| `.ms_cache` | 917MB | ModelScope 缓存 |

合计 ~8.3GB，清理后可用 ~19GB，足够放 15GB 模型。

**是否批准清理以上 4 项，然后下载 Qwen2.5-7B 并启动 eval？**

---
