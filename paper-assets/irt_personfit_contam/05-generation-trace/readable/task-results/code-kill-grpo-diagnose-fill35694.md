# code kill grpo diagnose fill35694

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kill-grpo-diagnose-fill35694_20260521T112401_result.json`
- **Structured JSON:** [`374f1f990bd2a73a0a6b.json`](../../sessions/37/374f1f990bd2a73a0a6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全满。下面输出完整产出。

---

## 产出汇总

### 1. GRPO Kill 确认
PID 97791 已 kill（SIGTERM 成功，无需 force kill）。

### 2. train_grpo.py 诊断报告

**核心问题**：`mmlu_reward` 是 binary reward（correct=1.0, wrong=-1.0），SFT 模型 83%+ 准确率 + `num_generations=8` + 默认 temperature（~0.7-1.0）→ 8 个 completion 大概率全答对 → reward 全 1.0 → **zero variance → GRPO loss=0，参数不更新**。

**关键参数**：
- `num_generations=8`
- `max_completion_length=128`
- `per_device_train_batch_size=2, gradient_accumulation_steps=4`
- `learning_rate=5e-6`
- 无显式 temperature/top_p 设置（用 TRL 默认值）
- LoRA r=16, alpha=32, dropout=0.05

**修复方案**：

| 方案 | 做法 | Pros | Cons |
|------|------|------|------|
| **(a) 增大 num_generations** | 8→32（或更大） | 最简单，不改 reward logic | VRAM 需求线性增长，32 在 4bit 下可能 OOM；准确率 83% 时 32 个仍可能全对 |
| **(b) Soft reward** | 按 completion 的 format quality / token-level confidence 给连续分 | 消除 zero-variance 问题的根源 | 实现复杂，需设计合理的 scoring rubric，且与 MMLU 正确性目标可能脱耦 |
| **(c) 增大 temperature** | temperature 1.5~2.0 | 增加 diversity，简单一行改动 | 太高会生成 garbage，reward 信号变弱 |
| **(d) 换 DPO** | 用 SFT 模型生成 chosen/rejected pairs，跑 offline DPO | 不需要 online generation，无 variance 问题 | 需要额外数据准备（生成 pairs），训练目标和 GRPO 不同 |

**推荐**：先试 **(a)+(c)** 组合——`num_generations=16, temperature=1.2`。如果仍然 zero variance，再考虑 **(b)** 或 **(d)**。

### 3. GPU 任务分配

| GPU | Task | PID | VRAM | Util |
|-----|------|-----|------|------|
| 0 | Llama clean_s2 (seed=123) | 129109 | 27.4GB | 91% |
| 1 | Mistral clean_s2 (seed=123) | 126817 | 9.0GB | 86% |
| 2 | Llama clean_s3 (seed=456) | 129635 | 30.1GB | 91% |
| 3 | Mistral clean_s3 (seed=123→456) | 127345 | 10.1GB | 88% |

### 4. Llama seeds 数据状态
- Llama train.py 已内置 `SEED_MAP`（clean_s2=123, clean_s3=456）和 `DATA_DIR_MAP`（clean_s2→clean, clean_s3→clean），无需额外数据准备
- 训练数据复用 `clean/train.jsonl`（5000 samples），仅 seed 不同
- wandb 未配置，已用 `WANDB_MODE=disabled` 绕过

---
