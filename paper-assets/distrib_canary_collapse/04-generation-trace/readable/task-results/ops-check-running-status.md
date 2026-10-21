# ops check running status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-status_20260514T234526_result.json`
- **Structured JSON:** [`c5e2cc1e32ab4b4af88b.json`](../../sessions/c5/c5e2cc1e32ab4b4af88b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU
| GPU | 利用率 | 显存占用 | 进程 |
|-----|--------|----------|------|
| 0 | 62% | 7,453 / 97,887 MiB | plan_006_s42 (PID 68373) |
| 1 | 50% | 14,391 / 97,887 MiB | alpha_sweep_a025_s42_v3 (PID 53074) |

### tmux sessions (从 ps 输出推断)
- `plan_006_s42` — 启动于 07:41
- `alpha_sweep_a025_s42_v3` — 启动于 05:04
- `alpha_sweep_a000_s42` — 启动于 03:01，无 GPU 进程，已结束

### plan_006_s42（20 gen × 10000 steps, ratio=1.0, wikitext103）
- **进度：0/20 gen**（刚启动 ~4 分钟，仍在 Generation 0 baseline 阶段）
- 输出目录仅有 config.json，尚无 metrics.json
- 日志 118 行，全部为 padding warning，**无 error**

### alpha_sweep_a025_s42_v3（10 gen × 5000 steps, ratio=0.25, wikitext103_5k）
- **进度：7/10 gen 完成**，正在训练 gen 7
- 已完成各代 train_loss 趋势（递减）：3.044 → 2.766 → 2.622 → 2.499 → 2.383 → 2.341
- 日志 2703 行，**无 error**
- 已运行 ~2h41m，预计还需 ~15-20 分钟完成剩余 3 gen

---
