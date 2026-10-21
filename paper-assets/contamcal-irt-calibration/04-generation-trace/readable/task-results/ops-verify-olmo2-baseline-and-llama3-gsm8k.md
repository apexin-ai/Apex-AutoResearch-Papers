# ops verify olmo2 baseline and llama3 gsm8k

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-olmo2-baseline-and-llama3-gsm8k_20260521T135923_result.json`
- **Structured JSON:** [`9c74e95e2c0f1f6c0191.json`](../../sessions/9c/9c74e95e2c0f1f6c0191.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 均在 GPU 0/1/2 上正常运行（各 ~18.6GB 显存）。

---

## 汇报

### Task 1: OLMo-2 d000 MMLU 基线核实

| Seed | Accuracy | 来源路径 |
|------|----------|----------|
| **s42** | **58.60%** (8229/14042) | `eval_results_cross_family/olmo2_d000_s42_westd/eval_results.json` |
| **s0** | **55.34%** (7771/14042) | `results/mmlu_eval/olmo2/d000_s0/eval_results.json` |

**结论：需修改。** 论文用 53.8% 但磁盘上唯一的 s42 MMLU 结果是 **58.60%**，差距 4.8pp。s0=55.34% 也不匹配。两份 eval JSON 都未记录 adapter_path 字段，无法从文件本身确认是 base model 还是 adapter eval。没有找到产出 53.8% 的 eval 文件——论文数值来源不明，建议追溯。

### Task 2: LLaMA-3 GSM8K eval

3 个 eval 已启动，均在 GPU 上加载模型并开始 GSM8K 评估：

| Dosage | GPU | PID | 状态 |
|--------|-----|-----|------|
| d000 | 0 | 528870 | running, loading dataset |
| d025 | 1 | 529276 | running, evaluating gsm8k |
| d100 | 2 | 529683 | running, evaluating gsm8k |

evaluate.py=37775 bytes ✓，3 个 adapter 均 lora_alpha=32 ✓。日志位于 `/tmp/eval_llama3_d{000,025,100}_gsm8k.log`。

---
