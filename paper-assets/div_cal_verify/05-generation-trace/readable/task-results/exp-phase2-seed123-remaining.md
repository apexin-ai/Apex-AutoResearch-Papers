# exp phase2 seed123 remaining

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phase2_seed123_remaining_20260513T100409_result.json`
- **Structured JSON:** [`a02b8be421ff639ba146.json`](../../sessions/a0/a02b8be421ff639ba146.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认：

- **tmux session**: `phase2_seed123_remaining` 已创建
- **进程 PID**: 197481（`run_mvp.py --method uncurated`，正在 cuda:1 上运行，CPU 占用 71.8%，模型加载中）
- **脚本**: `run_seed123_remaining.sh 1`，顺序执行 uncurated → RGDS，共 2×8=16 代
- **日志**: `/root/autodl-tmp/div_cal_verify/phase2_seed123_remaining.log`
- **Registry**: `phase2_seed123_remaining` 已注册为 RUNNING

**双卡并行状态**:
| GPU | 实验 | PID | 方法 |
|-----|------|-----|------|
| cuda:0 | phase2_ext_seed123 | 180473 | external_only seed=123, Gen 4/7 |
| cuda:1 | phase2_seed123_remaining | 197481 | uncurated seed=123 (刚启动) → 后接 RGDS |

**预计时长**: 参考 seed=42 的 phase2_3method_selfit，每方法 8 代约 6-8 小时，两方法顺序跑约 12-16 小时。

---
