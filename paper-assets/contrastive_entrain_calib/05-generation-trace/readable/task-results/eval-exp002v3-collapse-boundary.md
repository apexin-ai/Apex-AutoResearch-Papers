# eval exp002v3 collapse boundary

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp002v3-collapse-boundary_20260522T130255_result.json`
- **Structured JSON:** [`b845e57f0781bcf64efb.json`](../../sessions/b8/b845e57f0781bcf64efb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 全部正常启动，正在推理中。

**启动状态汇总：**

| tmux session | Checkpoint | GPU | 显存占用 | 状态 |
|---|---|---|---|---|
| `eval_002v3_ckpt1500` | checkpoint-1500 | GPU1 | 16.5 GB | 运行中，362 pairs |
| `eval_002v3_ckpt1000` | checkpoint-1000 | GPU2 | 15.0 GB | 运行中，362 pairs |
| `eval_002v3_ckpt500` | checkpoint-500 | GPU3 | 14.9 GB | 运行中，362 pairs |
| `exp-003-eval-s2-ckpt7500` | (exp-003 s2) | GPU0 | 16.9 GB | 之前已在运行 |

脚本：`eval_unified_preset.py`，base model = `Qwen3-8B`，data = `calibration_v2_1_expanded.jsonl` (362 pairs)。每个约 20 分钟完成。

已知 ckpt-2000 已坍塌 (SYCONScore=0.0, ToF=0.0, NoF=1.0)。这 3 个 checkpoint 的结果将定位 collapse 边界在 500-2000 步之间的具体位置。

---
