# ssh d051 exit diagnosis

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d051-exit-diagnosis_20260517T052923_result.json`
- **Structured JSON:** [`e995fb46d483b065d52e.json`](../../sessions/e9/e995fb46d483b065d52e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**进程已正常完成**，tmux session 保留但脚本已退出到 shell prompt。

### 1. 退出原因
正常完成。日志最后显示 `Done. Output: .../d051_fewnerd_n25_s456` 并回到 shell。

### 2. Few-NERD s456 最终状态
所有 6 个 count levels 全部完成（count_2, count_6, count_12, count_22, count_44, count_66），每个 25 batches。

### 3. Few-NERD s456 完整 metrics

| Count Level | Mean Recall | Std |
|---|---|---|
| count_2 | 0.5528 | 0.1402 |
| count_6 | 0.4092 | 0.1197 |
| count_12 | 0.3051 | 0.1050 |
| count_22 | 0.2577 | 0.0922 |
| count_44 | 0.2898 | 0.1366 |
| count_66 | 0.4067 | 0.0016 |

### 4. Conclusion: **success**

所有 6 个 dataset×seed 组合（fewrel×{s42,s123,s456} + fewnerd×{s42,s123,s456}）均有 `count_curve_summary.json`，实验完整结束。

---
