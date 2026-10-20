# diagnose cuda3 and registry tail

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cuda3_and_registry_tail_20260521T194406_result.json`
- **Structured JSON:** [`237bc0ff3e70e7b32b76.json`](../../sessions/23/237bc0ff3e70e7b32b76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 状态
| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| 0 | 62% | 9.4G / 97.9G | 忙碌 (test_eval_4b_sft_s42) |
| 1 | 91% | 32.5G / 97.9G | 忙碌 (test_eval_14b_sft_s42) |
| 2 | 87% | 19.6G / 97.9G | 忙碌 (test_eval_8b_sft_s42) |
| 3 | 90% | 18.9G / 97.9G | 忙碌 (test_eval_llama_sft_s42) |

### 实验进程状态
| 实验 | PID | GPU | 运行时间 | 状态 |
|------|-----|-----|----------|------|
| test_eval_4b_sft_s42 | 126048 | cuda:0 | 1h08m | 存活 |
| test_eval_14b_sft_s42 | 125321 | cuda:1 | 1h11m | 存活 |
| test_eval_8b_sft_s42 | 125615 | cuda:2 | 1h11m | 存活 |
| test_eval_llama_sft_s42 | 130446 | cuda:3 | 3m35s | 存活 |

### test_eval_llama_sft_s42 详情
刚启动 3 分多钟，模型已加载完毕，正在推理中。日志显示已完成 8/500 文档，速度约 24-29s/it，输出目录暂为空（结果尚未写入）。按当前速度估计总耗时约 3-4 小时。

---
