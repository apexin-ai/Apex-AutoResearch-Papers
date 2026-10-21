# analysis taxonomy check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_taxonomy-check_20260522T035438_result.json`
- **Structured JSON:** [`dfd31281ee4dbf3e03cd.json`](../../sessions/df/dfd31281ee4dbf3e03cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ANALYZING → RUNNING 不允许。Registry 状态机限制，不影响判断。

## 实验状态：**正在运行**

**进程**：VLLM EngineCore (PID 73796)，GPU 1 占用 85.8GB / 97.9GB，利用率 100%

**进度**：Phase 1 数据收集中，`phase1_complete: false`
- 每个模型需跑 8 个评分任务（2 数据集 × 4 条件：clean + verbosity_bias + position_bias + authority_bias）
- **已完成**：qwen2.5-72b（8/8 tasks，11:43–11:53，约 10 分钟）
- **进行中**：llama3.1-70b（11:55 开始 mmlu clean）
- **待跑**：还有 4 个模型（qwen2.5-32b, qwen2.5-14b, llama3.1-8b, mistral-large 等）

**预计剩余时间**：~50 分钟（5 个模型 × ~10 分钟/模型），之后还有 Phase 2 分析

**日志路径**：`/root/cert_manip_resist_eval/artifacts/logs/taxonomy_broadspectrum_20260522_114119.log`

---
