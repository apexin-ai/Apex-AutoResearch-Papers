# analysis exp1 isr b03 s44 r2 retry

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp1-isr-b03-s44-r2-retry_20260515T001926_result.json`
- **Structured JSON:** [`18a8175b375b2c4a8533.json`](../../sessions/18/18a8175b375b2c4a8533.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是 3 个实验的 eval 指标汇总：

## Eval 结果表

| Experiment | PR | ISR* | H7% | H1% | Non-hacking% | n_proved |
|---|---|---|---|---|---|---|
| **exp1-isr-b03-s44-r2** (ISR, seed 44) | **98%** | **0.742** | **100% (98/98)** | 0% | **0% (0/98)** | 98 |
| **exp1-isr-b03-s43** (ISR, seed 43) | 91% | 0.283 | 2.2% (2/91) | 74.7% (68/91) | 23.1% (21/91) | 91 |
| **exp1-random-b03-s43** (Random, seed 43) | 79% | 0.221 | 0% (0/79) | 75.9% (60/79) | 24.1% (19/79) | 79 |

\*ISR = proved-only mean ISR (eval_sta.py 统一评估)

## 关键发现

**seed 44 完全崩塌为 Goodhart 退化解**：100% H7 hacking — 所有 98 个 proved 样本都是 single premise = conclusion。ISR 看似很高 (0.742)，但完全是因为单前提 ≈ 结论，不存在真正的推理。

**seed 43 更温和**：H7 仅 2.2%，但 H1 高达 74.7%（结论嵌入多前提中）。真正的 non-hacking 占 23.1%。

**Random baseline (seed 43)**：0% H7，H1 与 ISR seed 43 相当 (75.9%)，non-hacking 24.1%。ISR reward 并没有在 seed 43 上比 random 产生明显优势。

**跨 seed 方差极大**：同一 ISR β=0.3 配置，seed 44 → 100% H7 退化，seed 43 → 仅 2.2% H7，表明 ISR reward 的训练不稳定。

## 状态
- exp1-isr-b03-s44-r2: DONE ✓
- exp1-isr-b03-s43: DONE (eval_metrics 已更新) ✓
- exp1-random-b03-s43: DONE (使用之前的 eval 数据 + 新 classify_h7) ✓
- 磁盘: 67G/250G (27%)，无 optimizer.pt 需清理
- **exp1-random-b03-s43 checkpoint 已被删除，无法重新 eval**（使用了之前保存的 eval 结果）

---
