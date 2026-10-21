# fix cwm eval max tokens

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cwm-eval-max-tokens_20260517T161926_result.json`
- **Structured JSON:** [`a08b07793d7a6dc596d2.json`](../../sessions/a0/a08b07793d7a6dc596d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CWM eval 已成功重启，推理已开始（1/9784）。GPU1 占用 16GB，一切正常。

## 汇总

### 1. CWM eval max_new_tokens
- **实际值: 128** (已确认)
- 已终止旧进程，清理旧结果，以 **max_new_tokens=512** 重新启动
- 新进程 PID=662946，在 GPU1 (CUDA_VISIBLE_DEVICES=1) 上运行
- 每样本约 3-13s（token 数增加后会慢一些），9784 样本预估 **8-15 小时**完成

### 2. CLS-s123 unparseable 诊断
- 2796/9784 (28.6%) unparseable，**与 truncated 100% 重合**
- 原因：`max_seq_length=2048` 对部分样本不够，输入被截断后模型输出乱码续写（如 `", but replace it with a new one"`）而非 `pass`/`fail`
- 这不是 parser 过严，是 **输入截断导致模型行为退化**
- 修复方案：用更大的 `max_seq_length`（如 4096）重跑 cls-s123 eval，或对截断样本默认预测 majority class（pass）

---
