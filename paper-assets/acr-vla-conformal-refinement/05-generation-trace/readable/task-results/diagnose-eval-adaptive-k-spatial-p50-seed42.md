# diagnose eval adaptive k spatial p50 seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-adaptive-k-spatial-p50-seed42_20260520T103105_result.json`
- **Structured JSON:** [`b1a3a3c4b29843146c2d.json`](../../sessions/b1/b1a3a3c4b29843146c2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：UNKNOWN — 实验在服务器上零痕迹

诊断结果汇总：

| 检查项 | 结果 |
|--------|------|
| Run log (`/root/runs/*spatial*p50*seed42*`) | **不存在** |
| Output JSON (`eval_adaptive_k_spatial_p50_seed42.json`) | **不存在** |
| Exit file (`/tmp/agent-ml-exit/*spatial*p50*seed42*`) | **不存在** |
| Tmux session | **不存在**（只有 `spatial-p25-seed43`） |
| 进程 PID 681823 | **已死** |
| OOM kill (journalctl -k, 12小时) | **无** |
| 系统重启 | **无**（上次重启 2025-06-13） |
| Bash history | **无相关记录** |
| GPU0 状态 | 空闲（2 MiB），无进程 |

**分析**：该实验在 bjb1-32546 上没有留下任何框架管理痕迹（无 run log、无 exit file、无 tmux），说明它是在 agent-ml 框架之外直接启动的。由于 `evaluate.py` 只在全部完成后写 output JSON，进程中途死亡则什么都不会留下。

**最可能死因**：与 PID 675831 相同 — 被 deploy worker 或其他外部进程 kill。排除 OOM（内核无记录）和系统重启。

**注意**：同服务器上所有 spatial adaptive-k 实验都是 seed43（p25/p50/p75），seed42 从未成功产出结果。需要重新启动。

---
