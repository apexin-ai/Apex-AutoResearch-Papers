# ops westd41074 gpu1 pi05 l2norm k07 seed43 and collect

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-gpu1-pi05-l2norm-k07-seed43-and-collect_20260521T125933_result.json`
- **Structured JSON:** [`72673e096448c5c830ed.json`](../../sessions/72/72673e096448c5c830ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## π0.5 L2norm V-shape 验证数据

| keep_ratio | seed42 | seed43 |
|------------|--------|--------|
| k=0.7 | 55.0% | **57.8%** |
| k=0.5 | 33.4% | 运行中（PID 206999, GPU0） |
| k=0.3 | 51.0% | **55.4%** |

**k=0.7 seed43 = 57.8%**，在 50-60% 范围内，与 seed42 的 55.0% 一致。V-shape 两端（k=0.7, k=0.3）在两个 seed 下均表现稳定（55-58%）。

等 k=0.5 seed43 完成后，如果也在 30-35% 范围（valley），V-shape 确认为系统性现象。

### k=0.7 seed43 per-task
| Task | SR |
|------|-----|
| alphabet_soup | 46% |
| cream_cheese | 96% |
| salad_dressing | 80% |
| bbq_sauce | 80% |
| ketchup | 26% |
| tomato_sauce | 100% |
| butter | 30% |
| milk | 4% |
| chocolate_pudding | 70% |
| orange_juice | 46% |

k=0.5 seed43（PID 206999）仍在 GPU0 运行，已运行 ~1.5h。

---
