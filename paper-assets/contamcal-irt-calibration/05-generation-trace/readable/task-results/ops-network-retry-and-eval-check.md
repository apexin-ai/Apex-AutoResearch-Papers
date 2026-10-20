# ops network retry and eval check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_network-retry-and-eval-check_20260518T203619_result.json`
- **Structured JSON:** [`9f80501796a2bb43db8c.json`](../../sessions/9f/9f80501796a2bb43db8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

### 1. 网络状态（westd-29999）
**NETWORK_DOWN** — HuggingFace 不可达，无法重启 Phi-4 和 OLMo-2 下载。

### 2. Eval 状态（westd-29999）
**所有 12 个 checkpoint 均无 eval 结果：**

| Model | Checkpoints | Eval Status |
|-------|------------|-------------|
| Qwen2.5-7B | d000_s42, d000_s123, d005_s42, d005_s123, d025_s42, d025_s123, d050_s42, d050_s123, d100_s42, d100_s123 | 全部 NO EVAL |
| Qwen2.5-14B | d000_s42, d005_s42 | 全部 NO EVAL |

**可用 eval 脚本：**
- `exp001/evaluate.py` — 主评估脚本（MMLU 5-shot, GSM8K 8-shot CoT, ARC-Challenge 25-shot, HumanEval pass@1）
- 多个 shell 脚本：`run_aligned_eval_*.sh` 系列（0.5B/1.5B/3B 用），但没有 7B/14B 的 eval shell 脚本

### 3. cqa1-21977 环境
- **GPU**: 1x RTX 4090D (24GB)，当前空闲（0 MiB used, 0% util）
- **Python**: 3.12.3（via miniconda3）
- **关键包**: torch 2.11.0, transformers 4.57.6, lm_eval 0.4.11, vllm 0.20.2
- **问题**: 4090D 24GB 跑 7B eval 可以（需量化或 vllm），跑 14B 吃力
- exp001 目录已存在于 cqa1

**结论**: westd-29999 网络断了无法下载模型；12 个 checkpoint 全部未做 eval；cqa1-21977 GPU 空闲且环境齐全，可以开始跑 7B eval。需要确认 7B checkpoint 在 cqa1 上是否可访问，或是否需要从 westd 传输。

---
