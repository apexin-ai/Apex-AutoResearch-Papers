# analysis integrate plan031 032 results

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_integrate-plan031-032-results_20260514T142844_result.json`
- **Structured JSON:** [`5d274351a57340d2c4e9.json`](../../sessions/5d/5d274351a57340d2c4e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。memory.md 新增章节 "2026-05-14: Actor Entropy & Value Calibration 分析结果 (plan_031/032)"，关键发现：

1. **Value calibration 是最强诊断信号**：v/R ratio（eval_return 基准）> 1.5 在 late training 100% 区分 collapsed vs healthy。collapsed 的 008d 峰值 1.67，006 峰值 2.72；healthy 从未超过 1.0。
2. **Actor entropy 差异反直觉**：collapsed configs 在 15K 步时 entropy 下降更慢（仍为正值），而非更快。可用但非主要诊断指标。
3. **008f 极端保守**：v/R=0.20 despite 503 eval_return，与 dt_emb removal 导致 reward prediction 退化一致。
4. **Normalized v/e target 无区分力**：所有实验 late-stage 均收敛至 ~1.0，不可用于诊断。
5. **组合机制可用于论文**：delusional critic signature = 慢 entropy 收敛 + value 过高估计，构成完整因果链。

另发现服务器上还有 `analysis_rssm_prediction_quality.json`（RSSM prediction quality 分析），属不同 plan 产物，已在 memory 中注明。

---
