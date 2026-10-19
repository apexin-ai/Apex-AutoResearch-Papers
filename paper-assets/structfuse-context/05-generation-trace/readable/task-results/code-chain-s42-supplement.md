# code chain s42 supplement

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_chain_s42_supplement_20260514T152851_result.json`
- **Structured JSON:** [`6c0de32e48f2e297d7d0.json`](../../sessions/6c/6c0de32e48f2e297d7d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 watcher 已部署并正常运行。

## 汇报

### tmux sessions (6 个)
| Session | 状态 | GPU |
|---------|------|-----|
| `m2_qwen_s43` | 运行中 — random_s43 step 1000/2810 | cuda:0 |
| `m2_full_starcoder` | 运行中 — random_s42 step 3800/~4215 | cuda:1 |
| `m2_starcoder_s43` | 等待 s42 完成 → 启动 s43plus | cuda:1 |
| `qwen_s42_watcher` | 等待 PID 337267 (run_m2_full_qwen.sh) | - |
| `starcoder_s42_watcher` | 等待 PID 74122 + 309679 | - |
| `m1_reextract_v2` | CodeQL 提取 | CPU |

### 链式执行逻辑
- **cuda:0**: `run_m2_full_qwen.sh` (6 runs, s43+s44) → `qwen_s42_watcher` 检测完成 → `run_m2_s42_supplement.sh --encoder qwen --gpu cuda:0`
- **cuda:1**: `random_s42` → `run_m2_full_starcoder_s43plus.sh` (由 m2_starcoder_s43 触发) → `starcoder_s42_watcher` 检测完成 → `run_m2_s42_supplement.sh --encoder starcoder --gpu cuda:1`

### 预估时间线
- **StarCoder random_s42**: ~400 steps 剩余, 约 1-2 小时完成
- **StarCoder s43plus**: 6 runs × ~1400 steps × 2 epochs, 约 24-36 小时
- **Qwen s43+s44 队列**: 当前 run 1/6, 约 24-36 小时剩余
- **s42 supplement** (每个 encoder 2 runs × 3 epochs): 约 6-8 小时/encoder

---
