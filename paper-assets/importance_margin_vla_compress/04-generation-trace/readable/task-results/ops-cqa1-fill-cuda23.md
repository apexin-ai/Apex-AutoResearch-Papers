# ops cqa1 fill cuda23

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-fill-cuda23_20260521T050200_result.json`
- **Structured JSON:** [`929d4b23a10c31a1e678.json`](../../sessions/92/929d4b23a10c31a1e678.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常。汇总：

---

## 已完成实验结果

### X-VLA random k=0.5 Object seed42
- **Overall SR: 70.6% (353/500)**，95% Wilson CI: [66.5%, 74.4%]
- Per-task:

| Task | Description | SR |
|------|-------------|-----|
| 0 | alphabet soup | 96% (48/50) |
| 1 | cream cheese | 46% (23/50) |
| 2 | salad dressing | 98% (49/50) |
| 3 | bbq sauce | 80% (40/50) |
| 4 | ketchup | 100% (50/50) |
| 5 | tomato sauce | 76% (38/50) |
| 6 | butter | 2% (1/50) |
| 7 | milk | 82% (41/50) |
| 8 | chocolate pudding | 26% (13/50) |
| 9 | orange juice | 100% (50/50) |

### X-VLA random k=0.85 Object seed42
- **Overall SR: 63.6% (318/500)**，95% Wilson CI: [59.3%, 67.7%]
- Per-task:

| Task | Description | SR |
|------|-------------|-----|
| 0 | alphabet soup | 100% (50/50) |
| 1 | cream cheese | 10% (5/50) |
| 2 | salad dressing | 100% (50/50) |
| 3 | bbq sauce | 94% (47/50) |
| 4 | ketchup | 24% (12/50) |
| 5 | tomato sauce | 92% (46/50) |
| 6 | butter | 0% (0/50) |
| 7 | milk | 94% (47/50) |
| 8 | chocolate pudding | 22% (11/50) |
| 9 | orange juice | 100% (50/50) |

## 新实验已启动

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| cuda:2 | X-VLA random k=0.3 Object seed42 | 60480 (子进程60485) | 运行中，已开始 eval |
| cuda:3 | X-VLA random k=0.5 Object seed43 | 61780 (子进程61785) | 运行中，已开始 eval |

nvidia-smi 确认 cuda:2 和 cuda:3 各占用 ~4.5GB 显存，实验正常推进。注意 cuda:0 上之前的进程已结束（释放了显存），cuda:1 仍有一个在跑。

---
