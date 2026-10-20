# paper figure fig5 dt amplification fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig5_dt_amplification_fix_20260515T102339_result.json`
- **Structured JSON:** [`62b58851ea7e6bbf4aeb.json`](../../sessions/62/62b58851ea7e6bbf4aeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修正摘要：

**Diff 总结：**
| 项目 | 旧值 | 新值 |
|------|------|------|
| Baseline (dt=1) | 915.67 (@105K) | **968.67** ±2.45 (@505K, 2-seed mean) |
| y 轴标签 | "Peak Eval Return" | **"Best Eval Return"** |
| dt=2 降幅 | -47% | **-50%** |
| dt=4 降幅 | -81% | **-82%** |
| N 标注 | 无 | **x 轴标签含 N=2/N=1** |
| 误差棒 | 无 | **baseline 有误差棒 (std=2.45)** |

**清理：** 旧 `fig5_rssm_fidelity.*` 本地和服务器均已删除。

**产出：** `artifacts/figures/paper/fig5_dt_amplification.pdf` + `.png`（已注册 art_20260515_72d849）。

---
