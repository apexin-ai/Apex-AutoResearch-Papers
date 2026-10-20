# diagnose bf16 qw imp failures

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bf16_qw_imp_failures_20260514T070415_result.json`
- **Structured JSON:** [`c0a17ca9a6ff25b1072f.json`](../../sessions/c0/c0a17ca9a6ff25b1072f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**根因：模型未下载。** `/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct` 目录不存在。

三个实验传入 `--model_path checkpoints/Qwen2.5-7B-Instruct`，但服务器上只有：
- `Qwen2.5-7B`（base 模型）
- `DeepSeek-R1-Distill-Qwen-7B`（symlink）

transformers 找不到本地目录后回退 HuggingFace Hub，绝对路径不是合法 repo_id → `HFValidationError` → 立即 crash。

**修复二选一：**

| 方案 | 操作 | 适用场景 |
|------|------|----------|
| A | 下载 Qwen2.5-7B-Instruct（ModelScope CDN，~10min） | 实验需要 Instruct 模型 |
| B | 改 `--model_path` 为 `checkpoints/Qwen2.5-7B` | base 模型即可 |

需要我执行哪个方案？

---
