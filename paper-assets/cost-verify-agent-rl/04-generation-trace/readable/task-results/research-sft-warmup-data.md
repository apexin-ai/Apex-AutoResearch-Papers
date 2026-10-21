# research sft warmup data

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sft-warmup-data_20260514T001108_result.json`
- **Structured JSON:** [`201c169dad7d8251e250.json`](../../sessions/20/201c169dad7d8251e250.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案文档已写入 `artifacts/sft_warmup_plan.md`。核心结论：

---

### RAGEN 代码现状

RAGEN **无内置 SFT 训练功能**，只有 RL 训练流程。需要用外部工具（TRL SFTTrainer / ms-swift / LLaMA-Factory）做 SFT。

### 文献调研要点

| 论文 | SFT 数据量 | 数据来源 | Epochs |
|------|-----------|---------|--------|
| Warm Up Before You Train | warmup ~1000 CoT + target 50-100 条 | 强模型生成 CoT | 1-3 |
| SkillRL | 未明确 | 成功轨迹 + LLaMA-Factory | 2-3 |
| RAGEN | 不做 SFT（用 Instruct 模型） | - | - |

### 现成数据集

HuggingFace 上有 **现成 ALFWorld SFT 轨迹数据集**：[u-10bei/sft_alfworld_trajectory_dataset](https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset)（v1-v5），已是 chat messages 格式，支持 6 种任务类型。

### 推荐方案

**方案 C（混合）**：
1. 下载公开数据集 → 转换为 RAGEN 的 `&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>` 格式 + AlfworldSG system prompt
2. 用 TRL SFTTrainer 训练 Qwen3-1.7B，200-500 条数据，2-3 epochs
3. 训练时间约 20-30 分钟（单卡 RTX PRO 6000 足够）

### 下一步

可以立即开始执行——先下载数据集检查格式，然后写转换脚本和训练脚本。是否现在开始？

---
