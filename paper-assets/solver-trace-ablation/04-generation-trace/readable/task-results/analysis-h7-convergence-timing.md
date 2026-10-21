# analysis h7 convergence timing

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_h7-convergence-timing_20260515T185111_result.json`
- **Structured JSON:** [`fb664ea431b0f238a49d.json`](../../sessions/fb/fb664ea431b0f238a49d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/root/solver-trace-ablation/analysis/h7_convergence_timing.md`（215 行）。

## 核心发现

**数据限制**：没有 per-checkpoint taxonomy，没有 W&B 记录。所有时序分析基于 reward_log.jsonl 中的 step-level `isr_mean` 作为 H7 代理指标（H7→高ISR，H1→ISR≈0）。

**H7 收敛速度对比**：

| 条件 | ISR首次持续>0.5 的 step | 最终 H7% |
|------|------------------------|----------|
| ISR s43 | ~Step 200 | 100% @500 |
| ISR s42 | ~Step 450-500 | 16%→97% (500→1000) |
| Exec-only s43 | ~Step 450-500 | 100% @1000 |
| Random s42/s43 | **从未** | 0% / 38.3% |
| Exec-only s42/s44 | **从未** | 0% (H1 mode) |

**关键机制**：ISR reward 创造 H7 自放大正反馈环——ISR s43 从发现到饱和仅需 ~250 步（step 150→400），而 Exec-only s43 需要 ~350 步（step 150→500+）。Random 条件下 ISR 轨迹无上升趋势，即使 H7 存在（s43: 38.3%）也不被差异性强化。

**对叙事 A 的支撑度**：中等偏强。ISR reward 确实加速 H7 收敛，但 onset 时间有 seed 依赖性（s42 比 s43 慢 ~200 步）。如需更强论据，建议对现有 checkpoint 补做 per-100-step taxonomy eval。

---
