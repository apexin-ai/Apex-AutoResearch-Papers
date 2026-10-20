# ops submit d000s42 d100 evals gpu2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_d000s42_d100_evals_gpu2_20260514T022723_result.json`
- **Structured JSON:** [`74fb9ea19370391bc83a.json`](../../sessions/74/74fb9ea19370391bc83a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 旧 tmux 清理
已清理。剩余 sessions: eval_15B_d000 (s42_v2, s123), eval_3B_d000 (s42, s123), sft_d100_15B_v2

## d000_s42_v2 提交
- PID: 263528
- GPU: cuda:2
- 启动确认: 是

## d100_v2 提交
- PID: 263784
- GPU: cuda:2
- 启动确认: 是

## 当前 GPU 状态
| GPU | 已用 | 空闲 |
|-----|------|------|
| 0 | 10055 MiB | 14027 MiB |
| 1 | 12620 MiB | 11462 MiB |
| **2** | **8827 MiB** | **15254 MiB** |
| 3 | 8957 MiB | 15125 MiB |
| 4 | 5829 MiB | 18253 MiB |
| 5 | 5829 MiB | 18253 MiB |

GPU 2 模型仍在加载中 (8.8GB used)，两个 0.5B eval 加载完成后预计 ~14.5GB，剩余充足。

---
