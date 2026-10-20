# code cwm baseline scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm-baseline-scripts_20260511T210816_result.json`
- **Structured JSON:** [`deee9400482157329235.json`](../../sessions/de/deee9400482157329235.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本全部验证通过：

| 脚本 | `--help` | 状态 |
|------|----------|------|
| `build_cwm_data.py` | `--input_dir`, `--output_dir`, `--timeout` | OK |
| `train_cwm_baseline.py` | 与 `train_verifier.py` 完全一致的超参数接口 | OK |
| `eval_cwm_baseline.py` | `--data_dir`, `--checkpoint_dir`, `--max_new_tokens` | OK |

**关键设计对齐点**：
- **Loss masking**: `tokenize_example` 用 `apply_chat_template` 分别生成 prompt-only 和 full (prompt+target) 的 token IDs，prompt 部分 labels 设为 -100，只在 assistant 回复部分计算 loss
- **LoRA/训练配置**: rank=16, alpha=32, target_modules, bs=2, grad_accum=16, lr=2e-4, epochs=3 — 与 `train_verifier.py` 完全一致
- **Prompt 格式**: system="code execution simulator", user 问 "What is the execution result?", target 是 "PASS: ..." 或 "FAIL: {ErrorType}: {msg}"
- **评估**: 分类指标完全复用 `eval_verifier.py` 格式，额外增加 exact match rate、per-error-type breakdown、生成长度统计

---
