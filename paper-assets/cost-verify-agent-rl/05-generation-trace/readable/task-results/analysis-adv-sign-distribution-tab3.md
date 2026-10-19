# analysis adv sign distribution tab3

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_adv-sign-distribution-tab3_20260519T022133_result.json`
- **Structured JSON:** [`47821ed97943841bbeae.json`](../../sessions/47/47821ed97943841bbeae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

输出文件已写入：
- `artifacts/tab3_mechanism_verification.json`
- `artifacts/tab3_mechanism_verification_summary.md`

## 关键结果

| 指标 | 值 |
|------|-----|
| **P(correct sign \| per-sample)** | **52.07%** (近似随机 50%) |
| **P(correct sign \| group majority)** | **81.25%** (13/16 groups) |
| **P(correct dir \| episode-normalized)** | **88.67%** |
| **Sign agreement early (pos 0-5)** | 51.14% (n=2511) |
| **Sign agreement late (pos 10-15)** | 63.86% (n=83) |
| **Theoretical P(misattrib)** | **20.48%** (p=0.7126, h=2, K=8) |

数据来自 128 episodes（16 uid × 8 episodes），正好一个 training step 的完整数据。

**与理论值 19.1% 的对比**：用实际数据推导的 p=0.7126 代入公式 p(1-p) 得到 20.48%，与 19.1% 的差异来自 p 值不同（19.1% 对应 p≈0.75 或论文中使用的特定参数化）。方向完全一致。

**关键发现**：per-sample advantage sign 与 episode outcome 的一致性仅 52%，实证确认了 step-independent GRPO 中的 sign misattribution 现象。

---
