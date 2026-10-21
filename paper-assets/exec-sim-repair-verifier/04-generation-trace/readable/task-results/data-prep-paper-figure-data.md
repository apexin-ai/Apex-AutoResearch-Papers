# data prep paper figure data

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data-prep_paper-figure-data_20260515T132727_result.json`
- **Structured JSON:** [`c71168dee403a5870150.json`](../../sessions/c7/c71168dee403a5870150.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个文件已生成并注册：

| 文件 | artifact ID | 内容 |
|------|-------------|------|
| `relaxed_matching_results.csv` | art_20260515_1557c9 | CLS vs CWM strict/normalized/enhanced matching 对比，含 parse rate 和 upper bound |
| `tost_multi_margin.csv` | art_20260515_9242c9 | TOST ±1/2/3pp 三档 margin，p=0.0104@±2pp 确认等价 |
| `mutation_type_accuracy.csv` | art_20260515_e363ac | 5 种 mutation type × 4 个 checkpoint 的 accuracy，含 val/test 分布比例 |
| `multi_seed_test_curves.json` | art_20260515_693d9b | 8B/4B × s42/seed123 完整 test/val curves + CWM baseline + seq2048 ablation + majority baseline |

数据来源：registry 的 125 个实验 metrics、memory.md 锁定数字、artifacts/ 已有分析报告（relaxed_matching_analysis.txt、tost_multi_margin_results.txt、mutation_type_analysis_w3w8_c1.md）交叉验证。

---
