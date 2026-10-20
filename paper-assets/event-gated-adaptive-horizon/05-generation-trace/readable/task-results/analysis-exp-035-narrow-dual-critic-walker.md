# analysis exp 035 narrow dual critic walker

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_035_narrow_dual_critic_walker_20260521T161055_result.json`
- **Structured JSON:** [`32db94d293b600e0c74d.json`](../../sessions/32/32db94d293b600e0c74d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_035 分析完成。Registry 已更新为 DONE (negative)，报告已注册。

## 结果摘要

**exp_035 结论：NEGATIVE — min operation alone 不能预防 CIVO，但能驱动强恢复**

| 指标 | 值 |
|------|-----|
| eval_peak / final | 697.8 (215K, 仍在上升) |
| eval_trough | 33.8 (85K, CIVO 崩溃) |
| NVE_peak | **2.75** (85K) — CIVO 触发 |
| NVE_final | 0.066 — 完全消退 |
| v1-v2 gap | **≈0.01** — 两个 critic 学到几乎相同的值 |
| CIVO 预防 | **否** |
| CIVO 恢复 | **是，强恢复** (33.8 → 697.8) |

## 2×2 Factorial 完整图景

|  | Single Critic | Dual Critic (min) |
|---|---|---|
| **~1.05M (normal)** | Baseline: CIVO → 崩溃无恢复 | **exp_035: CIVO (NVE 2.75) → 强恢复 697.8** |
| **~2.4M (wide)** | exp_033: CIVO (NVE 4.75) → 弱恢复 408 | exp_032: CIVO 预防 (NVE ≤1.1), eval 787.7 |

关键发现：
1. **完全预防 CIVO 需要 min + capacity 协同**（只有 exp_032 做到）
2. **min 是恢复的主导因素**：exp_035 (narrow dual, 697.8) > exp_033 (single wide, 408)，尽管参数更少
3. v1-v2 gap ≈ 0 说明窄 critic 缺乏容量形成多样化表征，min() 的悲观压力失效
4. 论文 framing 应从 "Synergistic Prevention" 改为 **"Complementary Defense-in-Depth"**：capacity 防 onset，min 保 recovery

---
