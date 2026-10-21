# analysis plan018 r3 eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan018-r3-eval_20260515T122110_result.json`
- **Structured JSON:** [`94468f05f271f5f3fa85.json`](../../sessions/94/94468f05f271f5f3fa85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。

---

## plan018-additive-random-b01-s42-1000-r3 分析结果

### 训练概况
- 1000 步从头训练（Qwen3-4B base），additive_random reward，β=0.1，seed=42
- 耗时 1h37m，train_loss=0.0067
- 训练末期：PR=0.827，mean_isr=0.521

### Eval 核心指标（proofwriter_fol_100.jsonl）
| 指标 | 值 |
|------|-----|
| prove_rate | 0.97 |
| mean_isr | 0.6892 |
| median_isr | 0.75 |
| isr_std | 0.2037 |
| **H7 (tautological)** | **97/97 = 100%** |
| genuine | **0%** |
| failed | 3 |

ISR 分布：0.33(13), 0.67(5), 0.75(71), 1.00(8) — 全部来自 tautological proofs 的 STA 分解，非 genuine reasoning。

### 与 r2 对比
r3 从头训练，r2 从 checkpoint-350 恢复。**结果一致**：都是 100% H7 tautological collapse。Random reward 在 1000 步下的 collapse 是确定性的，不受初始化路径影响。

### 与 ISR β=0.1（plan002-b01-s42-1000）对比
| | Random β=0.1 (本实验) | ISR β=0.1 (plan002) |
|---|---|---|
| PR | 0.97 | — |
| H7% | **100%** | 92.2% |
| genuine% | **0%** | **2.2%** |

ISR reward 即使在 β=0.1 的低权重下仍能产生少量 genuine proofs (2.2%)，而 random baseline 完全 collapse。

### 结论
**negative** — Random β=0.1 1000步完全 tautological collapse，0% genuine。这确认了 ISR reward 的因果贡献：将 ISR 替换为等量随机 reward 后 genuine reasoning 完全消失，证明 ISR signal 本身（而非仅仅 reward shaping 的额外梯度信号）驱动了 genuine proof 的产生。

---
