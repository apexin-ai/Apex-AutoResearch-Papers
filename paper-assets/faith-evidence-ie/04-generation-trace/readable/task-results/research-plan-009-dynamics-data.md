# research plan 009 dynamics data

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_009_dynamics_data_20260515T210649_result.json`
- **Structured JSON:** [`b6a3d2d9604b9d406fc3.json`](../../sessions/b6/b6a3d2d9604b9d406fc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出文件已保存并注册。

**汇总**：

`plan_009_dynamics_data.json` 包含：
- **6 个 GRPO runs**：
  - `qlora_ced_kl001_lr5e5`：20 训练步 + 5 eval 点（rel_f1 最高 0.2167，forgetting）
  - `qlora_ced_lr5e6`：20 训练步 + 5 eval 点（rel_f1<0.014 但 evi_f1→0.850，极端 decoupling）
  - `bf16_g8_grpo`：12 训练步 + 3 eval 点（rel_f1=0.4549，**无 forgetting**）
  - `qlora_extract_r4`：4 步后 collapse（f1_reward=0）
  - `qlora_flatnli_r6`：25 步 collapse
  - `qlora_flatnli_r3`：6 个时间点的 NLI reward hacking 数据
- **7 个 RSFT baselines**（3-seed CED mean=0.4596±0.0128 + flat-NLI + 变体）
- **SFT baseline**（量化/非量化）
- **5 个其他 baselines**（no-evidence SFT、CED reranker、random reranker、oracle、DPO 3ep）
- **6 个关键 decision 引用**（D024-D054）

核心 narrative：QLoRA GRPO 在结构化 IE 上导致 evidence-extraction decoupling（evi_f1↑ 但 rel_f1 catastrophic forgetting），bf16 GRPO 完全不出现此现象（Δrel_f1=+23.8pp），确认为 QLoRA-specific artifact（D054）。

---
