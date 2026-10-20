# ssh gpu0 crash cleanup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu0-crash-cleanup_20260514T015135_result.json`
- **Structured JSON:** [`c6321a5fae13a9475197.json`](../../sessions/c6/c6321a5fae13a9475197.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理完成

**GPU 状态：**
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| GPU0 | 0 MiB / 32607 MiB | 0% |
| GPU1 | 0 MiB / 32607 MiB | 0% |

无任何 python/vllm/episode 残留进程。GPU0 已完全释放。

**已完成 episode 数据：**
| Task | Episodes |
|------|----------|
| find-animal | 20 |
| identify-life-stages-1 | 20 |
| lifespan-longest-lived-then-shortest-lived | 20 |
| lifespan-longest-lived | **15** |

`lifespan-longest-lived` 只完成 15 eps，重启时用 `--start_episode 15`。

**注意：** GPU1 当前也显示 0 MiB——如果 GPU1 的 find-non-living-thing 任务应该在跑，可能也需要检查。

---
