# diag inference bench full failure

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_inference_bench_full_failure_20260517T025620_result.json`
- **Structured JSON:** [`9dd77c8a317536c8db88.json`](../../sessions/9d/9dd77c8a317536c8db88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败原因：模型路径错误

脚本 `benchmark_inference_full.py` 第 17 行硬编码了错误路径：

```
"rasp_20": "/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20"
```

但该目录**不存在**。实际目录名是 `sft_rasp_20_westd`。

### 错误链

1. Dense 模型加载成功，完成了 dense 的 inference benchmark
2. 轮到 `rasp_20` 时，`AutoTokenizer.from_pretrained("/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20")` 发现本地路径不存在
3. transformers 回退为 HuggingFace Hub repo_id 解析，因路径含 `/` 报 `HFValidationError`
4. 脚本崩溃，无 JSON 输出

### 部分结果

无。`inference_bench_full.json` 不存在，说明脚本在写出结果前就崩溃了（dense 的结果也未保存）。

### 服务器上实际存在的 SFT 模型目录

| 脚本中可能的 key | 实际路径 |
|---|---|
| rasp_20 | `sft_rasp_20_westd` |
| standard_20 | `sft_standard_20_westd` |
| rasp_25 | `sft_rasp_25` |
| standard_25 | `sft_standard_25` |
| unpruned | `sft_unpruned_baseline` |
| qwen_math 系列 | `sft_qwen_math_rasp_20` / `sft_qwen_math_standard_20` / etc. |

### 修复建议

修改 `benchmark_inference_full.py` 第 17 行，将路径改为正确的目录名。需要核对脚本中所有模型路径配置是否都对应实际存在的目录（可能不止 `rasp_20` 一个有问题）。需要我直接修复脚本吗？

---
