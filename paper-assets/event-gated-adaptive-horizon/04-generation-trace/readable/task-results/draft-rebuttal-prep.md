# draft rebuttal prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_draft_rebuttal-prep_20260524T030759_result.json`
- **Structured JSON:** [`5c01234b3ab27005f7d9.json`](../../sessions/5c/5c01234b3ab27005f7d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/rebuttal_prep.md`，包含 7 个 Q&A（覆盖指定的 5 个必须攻击面 + 2 个高概率附加攻击面）：

| # | 攻击面 | 核心应对 |
|---|--------|---------|
| Q1 | Frozen 只有 71% (5/7) | 重新定义指标：sustained CIVO 0/7 = 100%，2/7 transient 自修复反而强化诊断 |
| Q2 | Manipulation 0/5 | D146 ordering reversal（frozen 11.32 > trained 3.08）证伪 dt_emb 因果，定位为 scope boundary |
| Q3 | 仅 DreamerV3 | TAWM 对比锁定 MPC vs imagination 架构边界；gradient-causality dissociation 是通用方法论 |
| Q4 | 仅 2 个 locomotion 环境 | Walker moderate vs Cheetah extreme 是 severity continuum 设计，加 3 个 ManiSkill = 5 environments 总计 |
| Q5 | 无 head-to-head 干预对比 | 成功率差距太大（SGS 1/17, TCN 2/10, removal 5/5），paired comparison 无增量信息 |
| Q6 | NVE 1.5× 是否 arbitrary | Youden-optimal 1.53× 独立收敛，LOEO AUROC 0.981，承认 in-sample 作 limitation |
| Q7 | 样本量 n=2–4 太小 | Fisher p=0.003，132 实验总量；小 n 条件的 seed variance 作为不可靠证据报告而非正面结果 |

---
