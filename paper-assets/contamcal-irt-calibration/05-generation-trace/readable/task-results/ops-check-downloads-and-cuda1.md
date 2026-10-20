# ops check downloads and cuda1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-downloads-and-cuda1_20260518T180904_result.json`
- **Structured JSON:** [`cb213697271675a7600f.json`](../../sessions/cb/cb213697271675a7600f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

## 模型下载状态

| 模型 | 需要 shards | 已有 | 缺少 | 状态 |
|------|------------|------|------|------|
| **Phi-4** | 6 | 5 | `model-00005-of-00006.safetensors` | **不完整** |
| **OLMo-2-1124-7B** | 6 | 5 | `model-00003-of-00006.safetensors` | **不完整** |
| **Gemma-2-9B** | 8 | 8 | 无 | **完成** |

无下载进程在运行，缺失的 shards 不会自动补全。

## GPU 状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| cuda:0 | 62.6G/97.9G | 86% | PID 46066 - 训练中 |
| **cuda:1** | **0/97.9G** | **0%** | **空闲** |
| cuda:2 | 63.6G/97.9G | 69% | PID 38920 - Qwen2.5-14B d005 s42 |
| cuda:3 | 62.8G/97.9G | 99% | PID 46876 - Qwen2.5-7B d100 s123 |

## 磁盘

137G/250G used，剩余 114G (45%)。

## 结论

- **cuda:1 完全空闲**，可用
- **Phi-4 不能训练**：缺 shard 5，需先补下载
- **Gemma-2-9B 可以训练**：8/8 shards 完整，可立即在 cuda:1 启动
- **OLMo-2 也不完整**：缺 shard 3

下一步需要：恢复 Phi-4 和 OLMo-2 的下载（`huggingface-cli download --resume`），或者先用已就绪的 Gemma-2-9B 在 cuda:1 开训。

---
