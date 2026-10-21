# check mvp2 all status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mvp2_all_status_20260514T145214_result.json`
- **Structured JSON:** [`470becea1618b41321b7.json`](../../sessions/47/470becea1618b41321b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

| 实验 | 状态 | 进度 | 速度 | 预估剩余 | GPU 显存 |
|------|------|------|------|----------|---------|
| **mvp2_grpo_ced_r5** | 运行中 | 477/756 (63%) | ~12.7s/it | ~59 min | 13068 MiB |
| **mvp2_sft_eval_r2** | **已完成** (exit 0) | 985/985 | — | — | 已释放 |
| **mvp2_grpo_extract_r3** | 运行中 | 477/756 (63%) | ~12.0s/it | ~56 min | 13066 MiB |
| **mvp2_grpo_flatnli_r3** | 运行中 | 81/756 (11%) | ~124s/it | **~23h** | 13056 MiB |

### 详细指标

**mvp2_grpo_ced_r5** (cuda:0) — epoch 0.58
- reward: 1.199, ced_reward: 0.899, f1_reward: 0.0, format: 0.3
- f1_reward 一直为 0，entropy 已降至 0.0005（近乎坍缩）

**mvp2_sft_eval_r2** (cuda:1) — 成功完成
- F1: **0.4057**, Ign-F1: 0.4057, Evi-F1: **0.7979**, EDCR: **0.7118**
- Format OK: 983/985 (99.8%), Truncated: 367/985 (37.3%)
- 有大量 "Failed to parse output" 警告

**mvp2_grpo_extract_r3** (cuda:2) — epoch 0.60
- reward: 0.502, f1_reward: 0.202, format: 0.3
- f1_reward 在 0.14-0.25 之间波动，有学到但不稳定

**mvp2_grpo_flatnli_r3** (cuda:3) — epoch 0.05
- reward: 1.160, flat_nli_reward: 0.796, f1_reward: 0.067, format: 0.297
- 速度比其他 GRPO 慢 **10 倍**（~124s/it vs ~12s/it），原因是 NLI reward 计算在 CPU 上
- 按当前速度需要再跑约 23 小时

### 值得关注

1. **ced_r5 的 f1_reward=0** — 模型只优化了 ced_reward，三元组抽取能力未提升，entropy 极低说明输出已坍缩到固定模式
2. **flatnli_r3 极慢** — NLI 模型推理在 CPU 上，严重拖慢训练。cuda:1 已空出，如果可以把 NLI 模型放到 GPU 上会快很多
3. **sft_eval 的 truncated 37%** — 超过三分之一的预测被截断，可能影响 F1

---
