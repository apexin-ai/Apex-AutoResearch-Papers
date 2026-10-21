# code exception only nomarker data prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exception_only_nomarker_data_prep_20260516T143057_result.json`
- **Structured JSON:** [`e725cb5052d428cb8fa0.json`](../../sessions/e7/e725cb5052d428cb8fa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**数据已生成并验证通过：**

| | Train | Test | Total |
|---|---|---|---|
| 样本数 | 4720 | 1190 | 5910 |
| Pass | 3107 | 851 | 3958 |
| Fail | 1613 | 339 | 1952 |
| 含标记(修改前) | 3099 | 843 | 3942 |
| 含标记(修改后) | 0 | 0 | 0 |

**Before/After 对比：**
- Before: `Execution trace:\n[No exception data in trace]\n`
- After: `Execution trace:\n\n` （标记行被完全移除，trace 段为空）

**产出文件：**
- 脚本: `/root/trace-verdict-study/data/nomarker/prepare_nomarker_data.py`
- 数据: `/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_{train,test}.jsonl`

训练/评估代码已支持 `--condition exception_only_nomarker`，可直接启动 SFT。

---
