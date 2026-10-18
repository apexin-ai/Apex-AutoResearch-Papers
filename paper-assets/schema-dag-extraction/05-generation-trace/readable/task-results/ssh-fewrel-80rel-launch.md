# ssh fewrel 80rel launch

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-80rel-launch_20260515T125537_result.json`
- **Structured JSON:** [`83ba793e3f356ed92008.json`](../../sessions/83/83ba793e3f356ed92008.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 检查项 | 状态 |
|--------|------|
| **GPU 空闲** | **是** — 0% 利用率，0 MiB 已用 / 97887 MiB 总显存，无进程占用 |
| **16-rel exp2 完成** | **是** — eval_exp2.json (101KB) 和 predictions_exp2.json (26.7MB) 均已生成，无残留 tmux/进程 |
| **--use_all 参数** | **可用** — `--use_all`: Load both train+val splits (all 80 relations) |

### exp2 关键结果（16-rel / 8-way分类）

| Batch | Accuracy | BCS (相似度) |
|-------|----------|-------------|
| count_8_low_bcs | **88.9%** | 0.782 |
| count_8_high_bcs | **79.8%** | 0.892 |
| count_8_random_0 | **88.1%** | 0.847 |

- 低 BCS 批次（类间区分度高）准确率最高 88.9%
- 高 BCS 批次（类间容易混淆）准确率降至 79.8%，符合预期
- `military rank` 在两个批次中均达 100%；`main subject`（62.9%）、`mother`（59.7%）、`follows`（61.3%）是弱项

**GPU 已空闲，exp2 已完成，`--use_all` 参数就绪，可以启动 80-rel 实验。**

---
