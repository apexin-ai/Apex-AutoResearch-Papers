# ops disk check post restart

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-check-post-restart_20260521T193733_result.json`
- **Structured JSON:** [`0f1c24fd2baf5591b250.json`](../../sessions/0f/0f1c24fd2baf5591b250.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
17855: 61% used, 138G available — OK
19828: 96% used,  11G available — WARNING ⚠️
```

**19828 可清理目录**（按大小排序）：

| 目录 | 大小 | 说明 |
|------|------|------|
| `generalize/` | 69G | 最大，清理收益最高 |
| `alpha_sweep/` | 39G | |
| `scale/` | 11G | |
| `gen_opt13b_wiki_a100_s43_fp32/` | 9.9G | |
| `phase_diagram/` | 9.4G | |
| `scale_check/` | 5.4G | |
| `intervention/` | 9.3G | |
| `ablation/` | 3.2G | |
| `gen_wiki_gpt2m_a100_s43/` | 2.8G | |

19828 仅 11G 可用，远低于 30G 底线。清理 `generalize/` 或 `alpha_sweep/` 中已完成的实验可快速释放空间。需要指定清理哪些目录？

---
