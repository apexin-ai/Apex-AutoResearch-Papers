# code nohup check extract round2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nohup_check_extract_round2_20260522T103513_result.json`
- **Structured JSON:** [`0df88c56edd1f33e22d6.json`](../../sessions/0d/0df88c56edd1f33e22d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

**进程状态**: `compute_all_tasks.py` 已结束（不再运行），未找到 nohup.out 日志。

**5 个新完成的配置**（已保存到 `artifacts/plan011_new_cms_round2.json`）：

| 配置 | K | Accuracy | n |
|------|---|----------|---|
| humaid/deepseek_zero-shot | 10 | 0.6760 | 1500 |
| vast/deepseek_zero-shot | 3 | 0.5040 | 1500 |
| vast/llama4_few-shot-3 | 3 | 0.5007 | 1500 |
| vast/qwen2.5-7b_few-shot-3 | 3 | 0.4613 | 1500 |
| vast/qwen2.5-7b_few-shot-5 | 3 | 0.4647 | 1500 |

**未完成的配置**（有 jsonl 但无 npz，或 jsonl 为空/不完整）：
- civil_comments: deepseek_few-shot-3 (665B), deepseek_zero-shot (0B), llama4_* (全0B), qwen3_few-shot-3/5/zero-shot (有 jsonl 无 npz)
- humaid: deepseek_few-shot-3/5 (有 jsonl 无 npz), llama4_few-shot-3/5 (有 jsonl 无 npz), qwen3_few-shot-3 (有 jsonl 无 npz), qwen3_few-shot-5 (0B)
- vast: llama4_few-shot-5 (280KB 不完整), qwen2.5-7b_zero-shot (有 jsonl 无 npz), qwen3_few-shot-3/5 (0B)

进程似乎在处理到部分配置时就终止了，大量 CC 和部分 VAST/HumAID 配置未生成 npz。

---
