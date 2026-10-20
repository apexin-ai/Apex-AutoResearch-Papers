# ops vllm cleanup 068 070

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_vllm-cleanup-068-070_20260519T133154_result.json`
- **Structured JSON:** [`b14a93d00a2f4571eb3f.json`](../../sessions/b1/b14a93d00a2f4571eb3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇总如下：

### westd-16639 (exp-068 清理)

| GPU | 清理前 | 清理后 |
|-----|--------|--------|
| cuda:0 | PID 152729, 88255MiB, 96% (exp-064) | 不变 |
| **cuda:1** | **PID 142896, 88287MiB, 0%** (exp-068) | **0MiB, 已释放** |
| cuda:2 | PID 151829, 88263MiB, 97% (exp-069) | 不变 |
| cuda:3 | PID 76474, 88263MiB, 97% (exp-048) | 不变 |

### westd-25068 (exp-070 清理)

| GPU | 清理前 | 清理后 |
|-----|--------|--------|
| cuda:0 | PID 190753, 88301MiB, 97% (exp-065) | 不变 |
| cuda:1 | PID 211709, 88099MiB, 0% | 不变 (未在清理范围) |
| **cuda:2** | **PID 211015, 88301MiB, 0%** (exp-070) | **0MiB, 已释放** |
| cuda:3 | PID 192666, 88115MiB, 96% (exp-062) | 不变 |

---

**注意**: westd-25068 的 **cuda:1** 上仍有一个 0% 利用率的 vLLM 进程 (PID 211709)，对应 tmux session `exp069_vllm`。这个不在本次清理范围内，但看起来也是空闲残留，是否需要一并清理？

---
