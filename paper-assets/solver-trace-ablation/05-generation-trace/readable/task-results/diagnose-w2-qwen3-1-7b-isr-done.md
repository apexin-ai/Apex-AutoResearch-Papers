# diagnose w2 qwen3 1 7b isr done

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w2-qwen3-1_7b-isr-done_20260516T114633_result.json`
- **Structured JSON:** [`31d33a2025fc1f5c759f.json`](../../sessions/31/31d33a2025fc1f5c759f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能之前已删）。任务完成。

---

## 汇报

**训练状态**：500/500 步正常完成，耗时 35 分 53 秒。

**⚠️ 诊断：训练后期 mode collapse**
- 从 ~step 463 开始：loss=0, grad_norm=0, entropy→0, reward_std=0, completions length 稳定在 66 token
- 模型输出坍缩为几乎完全相同的固定证明模板
- 这是 GRPO 在小模型上低 K（K=4）+ 低 batch 的典型坍缩模式

**Eval 结果（proofwriter_fol_100.jsonl）**：

| Metric | Value |
|--------|-------|
| Prove Rate | **93%** |
| Mean ISR | 0.2625 ± 0.0752 |
| Median ISR | 0.2857 |
| H7 | 0 |
| H1 | 0 |
| H8 | 0 |
| Genuine | **93/93 (100%)** |
| Content-independent | 93/93 (100%) |

**解读**：高 prove rate + 几乎恒定 ISR=0.286 + 100% content-independent = 模型学会了一个**通用证明模板**（大概率是将所有前提作为 7 个 clause、去掉 2 个的固定 pattern → 2/7≈0.286）。没有 H7/H8 hacking，但这不是 genuine reasoning——是 mode collapse 后的退化表现。ISR 信号被模板化了。

---
