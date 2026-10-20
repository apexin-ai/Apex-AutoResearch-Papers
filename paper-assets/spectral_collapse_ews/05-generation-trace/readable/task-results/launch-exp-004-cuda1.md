# launch exp 004 cuda1

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_exp_004-cuda1_20260517T175518_result.json`
- **Structured JSON:** [`5138a9244f3dfdfca529.json`](../../sessions/51/5138a9244f3dfdfca529.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇总：

---

**路径冲突检查**：无冲突。`fixed_mix_seed42/` 路径不存在，与 exp_005 的 `adaptive_k20_seed42/` 完全独立。

**exp_004 状态**：
- PID: **135411**（实际 python 进程）/ tmux session PID: 135406
- 状态：正常运行，正在执行 Gen 0 评估（effective rank + perplexity）

**nvidia-smi (cuda:1)**：
| 进程 | PID | VRAM |
|------|-----|------|
| exp_005 (adaptive) | 116947 | 25,008 MiB |
| exp_004 (fixed_mix) | 135411 | 18,980 MiB |
| **合计** | | **43,988 MiB / 97,887 MiB (45%)** |

安全余量充足，无 OOM 风险。两个实验均正常运行。

---
