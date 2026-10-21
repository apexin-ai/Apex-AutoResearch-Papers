# analysis sweep exec only s45 r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sweep-exec-only-s45-r2_20260516T092041_result.json`
- **Structured JSON:** [`f42ecc614276c07378b8.json`](../../sessions/f4/f42ecc614276c07378b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## sweep-exec-only-s45-r2 结果摘要

**训练**: 500/500 步正常完成，prove_rate=0.74, train_loss=0.027, 运行 54.7 分钟。

**Eval (proofwriter_fol_100)**:
- prove_rate = **99%** (99/100)
- mean_isr = 0.5012 ± 0.2055

**Hacking 分类**:
| 类别 | 数量 | 比例 |
|------|------|------|
| H7a (同义反复) | 93 | 93.9% |
| H1 (结论嵌入) | 5 | 5.1% |
| H8 (合取坍缩) | 1 | 1.0% |
| **Genuine** | **1** | **1.0%** |

**结论: success** — 典型的 exec-only 坍缩模式，93.9% H7a 单前提 P→P 证明。ISR=0.5 是 2 组件结构的伪影，genuine 仅 1%。与其他 seed 的 exec-only 结果一致，可纳入 5-seed sweep。

Registry 已更新 conclusion=success + metrics + checkpoint_path + log_path。状态保持 ANALYZING，由 Main Agent 决定推进。

---
