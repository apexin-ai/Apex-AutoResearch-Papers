# diag exp 068 status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-068-status-check_20260519T120102_result.json`
- **Structured JSON:** [`9ab1918fe8ebf22af6f0.json`](../../sessions/9a/9ab1918fe8ebf22af6f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**exp-068-qwen3-logiqa200 正在正常运行。**

| 项目 | 状态 |
|---|---|
| tmux sessions | `exp068_vllm` (19:08创建) + `exp068_run` (19:13创建) |
| vLLM | port 8001, CUDA_VISIBLE_DEVICES=1, PID 142896 |
| 进度 | **88/200 (44%)**, ETA ~62 min |
| 结果文件 | exp068_results.json (155KB), 88 intermediates |
| GPU 1 利用率 | 97% |

**westd-16639 GPU 占用情况（全部占满）：**
| GPU | 利用率 | vLLM PID | 显存 |
|---|---|---|---|
| cuda:0 | 0% (idle but loaded) | 149111 | 88254MiB/97887MiB |
| cuda:1 | 97% (**exp-068**) | 142896 | 88278MiB/97887MiB |
| cuda:2 | 96% | 125544 | 88246MiB/97887MiB |
| cuda:3 | 97% | 76474 | 88254MiB/97887MiB |

Registry 已更新：补充了 gpu/pid/tmux_session/port 字段，写入诊断 notes。无空闲 GPU。

---
