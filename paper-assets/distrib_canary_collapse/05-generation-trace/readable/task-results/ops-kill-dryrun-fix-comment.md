# ops kill dryrun fix comment

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-dryrun-fix-comment_20260514T220351_result.json`
- **Structured JSON:** [`2beccc0a4b8a282388f4.json`](../../sessions/2b/2beccc0a4b8a282388f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Summary

1. **进程 kill**: PID 57123 和 57471 已成功终止（SIGTERM 即可，无需 force kill）。`ps` 确认进程不存在。

2. **VRAM**: cuda:0 和 cuda:1 各占 ~14.4GB，均为 a000_s42 实验进程（PID 46721, 53074）。dry-run 进程的 VRAM 已释放——之前 dry-run 和 a000_s42 共享 GPU，kill 后剩余占用即为 a000_s42 本身。

3. **注释修复**: `method_ablation.py:301` 已从 `partial eta-squared = F/(F+df_resid)` 改为 `Cohen's f² = F/df_resid`，与代码实际实现 `f2_val = F / df` 一致。

---
