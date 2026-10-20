# audit deepseek eval systematic

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_deepseek_eval_systematic_20260516T021339_result.json`
- **Structured JSON:** [`342fd362d4e2bddfdc8b.json`](../../sessions/34/342fd362d4e2bddfdc8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。现在汇总所有发现。

---

## 全面审计结果

### 核心结论：Base model 混用**不可能发生**

DeepSeek-Coder-6.7B (`hidden=4096, intermediate=11008`) 与 Qwen2.5-Coder-7B (`hidden=3584, intermediate=18944`) 维度完全不兼容。LoRA adapter shape 不匹配（如 `down_proj.lora_A: [16, 11008]` vs `[16, 18944]`），`PeftModel.from_pretrained` 会直接报错。**不可能**将 DeepSeek LoRA 加载到 Qwen base model 上。

所有 registry submit 命令均显式传了 `--model_path` 指向正确的 DeepSeek 模型。所有 8 个 checkpoint 的 `adapter_config.json` 的 `base_model_name_or_path` 均指向 DeepSeek。

### 汇总表

| 实验 ID | registry acc | eval_results.json acc | predictions.jsonl acc | adapter base_model | 是否正确 |
|---|---|---|---|---|---|
| deepseek_vota_seed42 | **0.8445** | 0.1597 ❌ | 0.8445 ✅ | DeepSeek ✅ | registry 正确，eval_results.json 是旧值 |
| deepseek_no_trace_seed42 | **0.7336** | 0.7336 ✅ | 0.7336 ✅ | DeepSeek ✅ | ✅ 全部一致 |
| deepseek_exception_only_seed42 | **0.9933** | 0.9933 ✅ | 0.9933 ✅ | DeepSeek ✅ | ✅ 全部一致 |
| deepseek_full_trace_seed42 | INVALIDATED | 0.2849 (all fail) | 0.1059 (garbage) | DeepSeek ✅ | ✅ 已标记失败，LoRA 训练因 label 截断失败 |
| deepseek_exception_only_seed123 | **0.9109** | 0.9109 ✅ | 0.9109 ✅ | DeepSeek ✅ | ✅ 全部一致 |
| deepseek_exception_only_seed456 | **0.9933** | 0.9933 ✅ | 0.9933 ✅ | DeepSeek ✅ | ✅ 全部一致 |
| deepseek_full_trace_seed42_v3 | **0.7916** | 0.2849 ❌ | 0.7916 ✅ | DeepSeek ✅ | registry 正确，eval_results.json 是错误 eval 的旧值 |

### 不一致条目详解

**1. deepseek_vota_seed42 — eval_results.json = 0.1597（应为 0.8445）**
- 根因：evaluate.py v2 默认 `max_length=2048`，DeepSeek tokenizer 效率低，91.7% 样本超限被截断 → 模型产生垃圾输出
- confirmatory eval 用 `max_length=16384`（不截断）→ 0.8445，与训练日志原始 eval 一致
- **eval_results.json 未被更新**，仍为 0.1597；正确值在 `eval_results_confirmatory.json`

**2. deepseek_full_trace_seed42_v3 — eval_results.json = 0.2849（应为 0.7916）**
- 根因：`run_missing_predictions.sh` 用 `--max_length 16384` 评估了 max_length=2048 训练的模型 → OOD 输入 → 全部预测 "fail"
- 后续 `eval_results_maxlen2048.json` 用正确的 `--max_length 2048` → 0.7916
- **eval_results.json 未被更新**，仍为 0.2849；正确值在 `eval_results_maxlen2048.json`
- predictions.jsonl 已更新为 maxlen2048 运行的结果（0.7916），registry UNRELIABLE 标记现在过时

### 需要修复的问题

1. **`deepseek_vota/final/eval_results.json`** 应覆写为 `eval_results_confirmatory.json` 的内容（0.8445）
2. **`deepseek_full_trace_seed42_v3/final/eval_results.json`** 应覆写为 `eval_results_maxlen2048.json` 的内容（0.7916）
3. **Registry v3 notes** 中的 `UNRELIABLE_PREDICTIONS` 标记应更新——predictions.jsonl 已在 May 16 10:17 被 maxlen2048 运行覆写，现在是可靠的
4. **evaluate.py** 不保存 `model_path` 到 eval_results.json，建议添加（防止未来审计困难）

### 系统性风险

- **evaluate.py `--model_path` 默认 Qwen**：当前因维度不兼容不会导致错误结果（会 crash），但如果未来添加维度兼容的模型可能产生静默错误
- **evaluate.py 不记录 max_length 到输出 JSON**：导致无法从结果文件反推使用了什么参数

---
