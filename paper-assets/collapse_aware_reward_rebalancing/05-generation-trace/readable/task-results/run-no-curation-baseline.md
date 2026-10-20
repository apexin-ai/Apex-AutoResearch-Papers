# run no curation baseline

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_no-curation-baseline_20260516T122505_result.json`
- **Structured JSON:** [`dda6c0e288a82735dcb5.json`](../../sessions/dd/dda6c0e288a82735dcb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**No-curation baseline 已成功启动在 cuda:1 上。**

总结：
- **脚本**: `/root/autodl-tmp/carr/run_baseline.py`
- **PID**: 501406 (python3 主进程)
- **tmux session**: `baseline`
- **日志**: `/root/autodl-tmp/carr/outputs/baseline_no_curation.log`
- **状态**: Generation 0/2 进行中，已生成 16/2000 prompts

关键参数与 Quick Probe 一致：seed=42, 2000 train + 200 eval prompts, K=4 candidates, 3 代。区别仅在 curation 策略为 `no_curation`（随机选 1-of-4）。

---
