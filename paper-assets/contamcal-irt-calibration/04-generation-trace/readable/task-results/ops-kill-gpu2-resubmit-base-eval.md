# ops kill gpu2 resubmit base eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-gpu2-resubmit-base-eval_20260515T113004_result.json`
- **Structured JSON:** [`b801de0a926b0726291e.json`](../../sessions/b8/b801de0a926b0726291e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**结果汇总：**
- GPU 2 死进程 PID 530893/548811 已 kill，显存已释放
- `exp_008_base_pretrained_eval` 已标记 DONE/failed
- `exp_008_base_pretrained_eval_v2` 已创建并提交到 GPU 2
  - PID: **553256**，tmux session: `exp008v2`
  - GPU 2 当前 1311 MiB 已分配，模型正在加载中
  - CUDA_VISIBLE_DEVICES=2 已显式设置（C004 合规）
  - 无 --adapter-path（base pretrained 评估）

---
