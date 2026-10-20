# diagnose d140 4b sft s42 with evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d140_4b_sft_s42_with_evi_2048_20260521T113420_result.json`
- **Structured JSON:** [`fec10c9fe1fd31ed48c7.json`](../../sessions/fe/fec10c9fe1fd31ed48c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验已成功完成，无需重跑。**

EXIT_CODE=129 (SIGHUP) 发生在所有工作完成**之后**。日志显示：

- 推理 247/247 batch 全部完成（985 个 doc）
- metrics.json 和 predictions.json 均已写入 `/root/autodl-tmp/eval_results/d140_4b_sft_s42_with_evi_2048/`
- SIGHUP 是 tmux/终端断连导致的信号，发生在结果写入之后

**结果摘要：**

| 指标 | 值 |
|------|-----|
| F1 | 0.4033 |
| Ign-F1 | 0.3946 |
| Evi-F1 (DREEAM) | 0.3129 |
| Evi-F1 (TP) | 0.7906 |
| EDCR | 0.7262 |
| Format OK | 983/985 (99.8%) |
| Truncated | 243/985 |

**GPU 当前状态：** cuda:3 已释放（0 MiB），进程已正常退出。

---
