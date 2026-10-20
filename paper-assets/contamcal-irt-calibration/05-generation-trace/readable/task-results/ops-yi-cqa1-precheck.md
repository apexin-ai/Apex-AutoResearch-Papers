# ops yi cqa1 precheck

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_yi-cqa1-precheck_20260522T180704_result.json`
- **Structured JSON:** [`0dc42d7589cab1ff10b3.json`](../../sessions/0d/0dc42d7589cab1ff10b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 1. 磁盘空间：不足

| 项目 | 大小 |
|------|------|
| /root/autodl-tmp 总量 | 169GB |
| 已用 | 156GB (93%) |
| **可用** | **14GB** |
| Yi-1.5-9B 需要 | ~18GB |

**差 ~4GB+，无法下载。**

可释放的候选（需确认是否仍在使用）：

| 路径 | 大小 | 说明 |
|------|------|------|
| models/gemma-2-9b/ | 35GB | 最大单项 |
| models/llama3-8b-tmp/ | 15GB | 名字含 tmp |
| models/Qwen2.5-7B/ | 15GB | 与 .hf_cache/Qwen 可能重复 |
| models/LLM-Research/ | 6GB | |
| .hf_cache/Falcon3-7B-Base/ | 14GB | |

### 2. VRAM 估算：QLoRA 4-bit 可行

| 方案 | 模型占用 | 总估算 | 4090D 24GB |
|------|---------|--------|------------|
| bf16 | ~18.8GB | >22GB | ✗ 超出 |
| 8-bit | ~10GB | ~16GB | △ 紧张 |
| **QLoRA 4-bit** | **~5GB** | **~10-12GB** | **✓ 充裕** |

当前 GPU 上 7B 模型 signals 任务占用 15.6GB/24GB（PID 716957），作为参考 9B bf16 必然超出。

**推荐方案：QLoRA 4-bit (nf4) + gradient_checkpointing**，预计 VRAM ~10-12GB，4090D 完全够用。

### 3. 下载状态：未下载

磁盘不足，需要先清理至少 5GB 空间。请确认哪些旧模型可以删除，我再执行下载。

---
