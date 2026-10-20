# ops gpu check and submit 3B d000 s42 eval v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-and-submit-3B-d000-s42-eval-v3_20260515T063950_result.json`
- **Structured JSON:** [`088f7cfa05e4e38313e5.json`](../../sessions/08/088f7cfa05e4e38313e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已在 GPU 5 上启动成功。

## GPU 占用汇总

| GPU | 显存占用 | PID | 状态 |
|-----|---------|-----|------|
| 0 | 3695MiB / 24564MiB | 513900 (python) | 占用 |
| 1 | 13583MiB / 24564MiB | 492660 | 占用 |
| 2 | 8985MiB / 24564MiB | 506625 | 占用 |
| 3 | 8985MiB / 24564MiB | 503791 | 占用 |
| 4 | 8985MiB / 24564MiB | 513826 | 占用 |
| 5 | 6791MiB / 24564MiB | **516729** (新提交) | **exp_001_eval_3B_d000_s42_v3** |

## 提交结果

- **状态**: 成功
- **GPU**: cuda:5（CUDA_VISIBLE_DEVICES=5）
- **PID**: 516729
- **显存**: 6782MiB
- **tmux session**: `exp_001_eval_3B_d000_s42_v3`
- **日志**: `/root/autodl-tmp/exp001/eval_results/exp_001_eval_3B_d000_s42_v3.log`

注：上一个 Worker 报告 GPU 5 被 exp008 占用，但现在已释放。6 张 GPU 现已全部在用。

---
