# code deepseek 25 grpo pipeline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deepseek_25_grpo_pipeline_20260516T155120_result.json`
- **Structured JSON:** [`f854e3428cfbff433148.json`](../../sessions/f8/f854e3428cfbff433148.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**当前状态报告：**

| 任务 | GPU | PID | 状态 |
|------|-----|-----|------|
| grpo_rasp_25 | cuda:0 | 21408 | ✅ 模型已加载，正在准备 GSM8K 数据集 |
| sft_standard_25_westd | cuda:1 | 21488 | ✅ 模型已加载到 GPU (11.8GB)，训练中（日志有缓冲延迟） |

**模型来源：**
- `sft_rasp_25`：westd 上已存在完整模型，直接启动 GRPO
- `sft_standard_25`：目录为空，从 `pruned_standard_25` 做 SFT（从头训练）

**待办：** SFT 完成后（预计 30-60 分钟）需提交 `grpo_standard_25` 到 cuda:1。需要我设置定时监控并自动提交吗？

---
