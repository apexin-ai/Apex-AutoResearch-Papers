# code training dynamics plot

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_training_dynamics_plot_20260519T114500_result.json`
- **Structured JSON:** [`8029d8e6dcf5f1b2521b.json`](../../sessions/80/8029d8e6dcf5f1b2521b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本执行成功。输出文件：

| 文件 | 大小 |
|------|------|
| `results/v7_training_dynamics.pdf` | 39.5 KB |
| `results/v7_training_dynamics.png` | 318.8 KB |
| `results/v7_training_dynamics_parsed.json` | 124.9 KB |

解析数据：480 条 loss 行、61 条 GATE 记录（去重后）、31 条 GATE-PROFILE 记录。

脚本位于 `/root/turn_residual_gating/plot_training_dynamics.py`，五个 panel 分别展示 L_NTP、L_GAR（含三阶段标注）、Gate mean±std、Gate min/max、L_DIV，gs75 和 gs144 处有红/蓝垂直虚线标注 Phase A/B/C。

---
