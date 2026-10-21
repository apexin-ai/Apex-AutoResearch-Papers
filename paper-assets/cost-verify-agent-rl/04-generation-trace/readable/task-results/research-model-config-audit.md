# research model config audit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_model-config-audit_20260515T035916_result.json`
- **Structured JSON:** [`bbae90d03baba6f8e77b.json`](../../sessions/bb/bbae90d03baba6f8e77b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. 模型变体
- **原始模型名**: `Qwen/Qwen3-1.7B`（下载路径 `/root/autodl-tmp/models/Qwen/Qwen3-1___7B/`）
- **Base / Instruct**: **Instruct**
- 证据:
  - 无 `-Base` 后缀。Qwen3 命名约定：默认名即 instruct 版，base 版需显式加 `-Base` 后缀
  - tokenizer 有完整 `chat_template`，包含 `&lt;think>` reasoning 标签、tool_call 支持 — 这是 instruct 模型特征
  - `<|im_start|>` / `<|im_end|>` special tokens 存在
- exp022 实际加载: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`（exp021 SFT checkpoint，基于 Qwen3-1.7B instruct 做的 SFT）

## 2. Qwen3-1.7B-Instruct 是否存在
- **不存在**（作为独立模型 ID）
- Qwen3 系列命名与 Qwen2.5 不同：
  - `Qwen3-1.7B` = instruct/chat 模型（就是我们用的）
  - `Qwen3-1.7B-Base` = 预训练 base 模型（如果存在）
  - **没有** `Qwen3-1.7B-Instruct` 这个独立模型
- HuggingFace 查询因服务器网络超时未返回，但基于 Qwen3 官方发布信息确认

## 3. Val Temperature
| 配置 | train temperature | val temperature |
|------|------------------|-----------------|
| **exp022** | **1.0** (L52) | **0.4** (L57) |
| exp018 | 1.0 | 0.4 |
| base.yaml 默认 | 1.0 | 0.5 |

- 当前 val temperature = **0.4**，与 Self-Guide 论文 val 0.4 **一致**

## 4. Reward Scale
- `AlfredEnvConfig.score` 默认 = **10.0**（`config.py` L18）
- exp022 yaml **无 score 覆盖** → 使用默认值 10.0
- 代码逻辑 (`env.py` L207): `reward = self.config.score * float(won)` → **成功=10.0, 失败=0.0**
- `valid_action_bonus = 0.0`（默认，exp022 无覆盖）
- `format_penalty = 0`（exp022 L79）
- **差异分析**: 实际传给 GRPO 的 reward 是 **0/10 scale**，不是论文标准的 **0/1 binary**。如果 GRPO 的 advantage normalization (`norm_adv_by_std_in_grpo: True`) 开启，10x 缩放理论上会被 std normalization 吸收，但对 KL penalty 项（`kl_loss_coef: 0.5`）的相对权重有影响 — reward scale 越大，KL 惩罚相对越弱。

---
