# analysis exp 084 085 status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-084-085-status-check_20260519T230800_result.json`
- **Structured JSON:** [`59f4539bcb654ee3af88.json`](../../sessions/59/59f4539bcb654ee3af88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已**完成**，CRON 误判。结果如下：

## exp-084 (Debate × LogiQA s123)

| 指标 | 值 |
|------|-----|
| n | 27 |
| debate_accuracy | **18.52%** |
| sc_accuracy | 44.44% |
| delta | **-25.93%** (debate 大幅劣于 SC) |
| wall_time | 1851.7s (~30.9 min) |
| fallback_count | 1 |

## exp-085 (Contrastive × LogiQA s123)

| 指标 | 值 |
|------|-----|
| n | 52 |
| contrastive_accuracy | **53.85%** |
| sc_accuracy | 50.00% |
| delta | **+3.85%** (contrastive 略优于 SC) |
| wall_time | 1770.5s (~29.5 min) |
| degenerate_count | 9 (17.3%) |

## 注意事项

1. **样本量异常**：exp-084 只跑了 27 题，exp-085 跑了 52 题，都远低于预期的 200 题。需要检查是 dry-run 模式还是数据集截断。
2. **exp-084 结果很差**：debate 准确率仅 18.52%，远低于 SC baseline 的 44.44%，delta=-25.93%。
3. **vLLM 状态**：因 ssh_read_only 不支持管道，未能检查 vLLM 进程；但两个实验都正常跑完并产出结果，说明 vLLM 在实验期间是正常的。

---
