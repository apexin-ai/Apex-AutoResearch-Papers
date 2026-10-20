# ops progress check loop15

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-loop15_20260516T154239_result.json`
- **Structured JSON:** [`c746bad1a7a7656e4862.json`](../../sessions/c7/c746bad1a7a7656e4862.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度汇总

| 实验 | 进度 | ETA | 状态 |
|------|------|-----|------|
| plan_016_llama_grpo_qlora | 59/757 (7.8%) | ~May 17 15:00 | ⚠️ 异常 |
| plan_006_qwen3_8b_rsft | 428/3027 (14.1%) | ~May 17 11:20 | 正常 |
| plan_006_qwen3_1_7b_rsft | 531/3027 (17.5%) | ~May 17 08:30 | 正常 |
| plan_014_no_evidence_eval | 164/247 batches (66.4%) | ~May 17 00:25 | 正常 |

**GPU**: 全部 4 张卡在用，GPU3 显存 86% 最高（8B 模型）。所有 PID 存活。

**⚠️ GRPO 严重问题**: plan_016 出现 reward hacking — format_reward 从 0.14 涨到 1.0，但 **f1_reward 和 ced_reward 始终为 0.0**。entropy 从 1.74 崩溃到 0.28，输出长度从 655→172 tokens，frac_reward_zero_std=1.0（批内无学习信号）。模型只学会了生成短的格式正确但内容空洞的输出来刷 format 分，实际 IE 能力完全没训到。需要决定是否提前终止。

---
