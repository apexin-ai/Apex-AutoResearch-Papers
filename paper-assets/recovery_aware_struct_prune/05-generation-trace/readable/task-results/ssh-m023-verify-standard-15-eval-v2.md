# ssh m023 verify standard 15 eval v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m023_verify_standard_15_eval_v2_20260520T225244_result.json`
- **Structured JSON:** [`e9ea43b8b4f0d33b5b03.json`](../../sessions/e9/e9ea43b8b4f0d33b5b03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Standard 15% eval v2 — 两个都失败了

| Job | 状态 | 错误 |
|-----|------|------|
| seed123 (PID 292346) | **EXIT_CODE=1** | 模型加载成功，但 `HF_DATASETS_OFFLINE=1` 导致无法加载 GSM8K 数据集：`ConnectionError: Couldn't reach 'openai/gsm8k' on the Hub (OfflineModeIsEnabled)` |
| seed456 (PID 292428) | **EXIT_CODE=1** | tokenizer 加载失败：`JSONDecodeError: Expecting value: line 1 column 1 (char 0)` — `grpo_standard_15_seed456_v3/checkpoint-100` 的 tokenizer.json 文件为空或损坏 |

**根因分析**：
- **seed123**: 之前的 CKA-only eval 能跑是因为 GSM8K 数据集已缓存，但 v2 job 的环境可能用了不同的 cache 目录，或缓存被清理了。需要去掉 `HF_DATASETS_OFFLINE=1` 或确保数据集已缓存。
- **seed456**: checkpoint 的 tokenizer.json 损坏（空文件），需要检查并修复（从基础模型或 seed123 的 checkpoint 复制 tokenizer 文件）。

### CKA-only eval（GPU 0/1）— 正常运行中

| Job | 进度 | 当前 Accuracy | ETA |
|-----|------|--------------|-----|
| seed123 (GPU 0) | 761/1319 (58%) | 73.2% @ 750 | ~50min |
| seed456 (GPU 1) | 738/1319 (56%) | 72.7% @ 700 | ~55min |

---
