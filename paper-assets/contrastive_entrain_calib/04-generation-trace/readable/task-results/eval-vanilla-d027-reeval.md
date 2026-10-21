# eval vanilla d027 reeval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_vanilla-d027-reeval_20260520T093205_result.json`
- **Structured JSON:** [`3045ccfba11546ef1f12.json`](../../sessions/30/3045ccfba11546ef1f12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### Part A: Vanilla Baseline D027 Re-eval
- **已提交** @ westd-28034 GPU 0，PID `234327`，tmux session `vanilla-d027-reeval`
- Registry: `vanilla-d027-reeval` (PREPARING → RUNNING)
- 命令省略 `--lora_path`（脚本默认 None，直接跑 base model）
- 日志: `~/runs/contrastive_entrain_calib/vanilla-d027-reeval.log`
- 预计耗时 ~30min（参考 exp-004 ckpt-8000 eval 用时 1663s）

### Part B: exp-004 ACT Checkpoint Trajectory

| Checkpoint | ToF | NoF | SYCONScore | vs Vanilla |
|------------|-----|-----|------------|------------|
| Vanilla* | 0.1105 | 0.9227 | 0.1974 | — |
| ckpt-500 | 0.0939 | 0.8895 | 0.1699 | -2.8pp |
| ckpt-2000 | 0.1492 | 0.8785 | 0.2550 | +5.8pp |
| ckpt-8000 | 0.1823 | 0.8674 | 0.3013 | **+10.4pp** |

*Vanilla 数值来自 eval_pipeline.py，D027 unified preset re-eval 进行中，数字可能更新。

趋势：SYCONScore 单调递增，ckpt-2000 起超越 vanilla。每 +1pp ToF 仅损失 ~0.77pp NoF，trade-off 可控。已写入 memory.md 顶部。

---
