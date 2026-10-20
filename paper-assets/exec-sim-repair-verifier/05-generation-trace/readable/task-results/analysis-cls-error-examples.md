# analysis cls error examples

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls-error-examples_20260517T094017_result.json`
- **Structured JSON:** [`33341d2c299bd688db12.json`](../../sessions/33/33341d2c299bd688db12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成：`artifacts/qualitative_cls_error_examples.json`

收集了 3 个样本：

| ID | Model | Level | Error Type | Problem | Mutation | 错误原因 |
|---|---|---|---|---|---|---|
| FP-1 | Qwen3-4B | func | false positive | HumanEval/37 | off_by_one | slice step 2→1 改变了列表长度，但模型未追踪 zip+append 的传播效果 |
| FN-1 | Qwen3-4B | func | false negative | HumanEval/130 | original | Tribonacci 自引用递推式用了代数化简，模型无法验证数学等价性（该题贡献了 27/160 FN） |
| FP-2 | Qwen3-8B | repo | false positive | pytest-7490 | boundary_removal | `if True:` 替换了 guard condition，导致 None.reason 抛 AttributeError，但模型未追踪跨 concern 的 None 传播 |

---
