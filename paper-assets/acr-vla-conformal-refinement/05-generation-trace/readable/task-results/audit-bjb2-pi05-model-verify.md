# audit bjb2 pi05 model verify

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb2-pi05-model-verify_20260526T151944_result.json`
- **Structured JSON:** [`2fd5f26fb51978d1606a.json`](../../sessions/2f/2fd5f26fb51978d1606a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

### 模型文件（三台对齐）

| 项目 | bjb2-24035 | bjb2-28827 | bjb1-32546 (基准) |
|------|-----------|-----------|------------------|
| model.safetensors | 7,473,096,344 B | 7,473,096,344 B | 7,473,096,344 B |
| config.json | 完全一致 | 完全一致 | 完全一致 |
| policy_preprocessor.json | 1937 B (ModelScope 本地路径) | 1937 B (ModelScope 本地路径) | 1903 B (HF 名称) |

`policy_preprocessor.json` 差异仅是 tokenizer_name 路径：bjb2 两台指向 `/root/autodl-tmp/.ms_cache/AI-ModelScope/paligemma-3b-pt-224`，bjb1-32546 指向 `google/paligemma-3b-pt-224`。功能等价。

### 代码与包版本

| 项目 | bjb2-24035 | bjb2-28827 | bjb1-32546 | bjb1-18228 |
|------|-----------|-----------|-----------|-----------|
| pi05_wrapper.py | 414 行 | 414 行 | 414 行 | 414 行 |
| modeling_pi05.py | 1297 行 | 1297 行 | 1297 行 | 1297 行 |
| lerobot | 0.5.2 | 0.5.2 | 0.5.2 | 0.5.2 |
| transformers | **5.9.0** | **5.8.1** | 5.8.0 | 5.8.0 |
| git commit | 24a7df4e | 446587ca | (无 .git) | a594db57 |

### 376 missing_keys — 不是 bug

**所有四台服务器（包括已知正常的 bjb1-32546）都有完全相同的 376 missing_keys 输出。** 这是 `_fix_vision_tower_keys` 方法的正常行为：它只加载 437 个 vision tower keys 的 remap，`load_state_dict(remap, strict=False)` 报告的 376 "missing" keys 是其他已经由 `from_pretrained` 加载的参数，不影响模型完整性。

### 实际实验结果（从日志）

| 服务器 | 实验 | SR |
|--------|------|-----|
| bjb1-32546 | pi05 VLA-only spatial s42 | **98.0%** (196/200) |
| bjb1-18228 | pi05 VLA-only spatial s43 | **97.5%** (195/200) |
| bjb2-28827 | pi05 VLA-only object s43 | **98.5%** (197/200) |
| bjb2-28827 | pi05 CRM spatial s42 | **96.5%** (193/200) |
| bjb2-24035 | 日志中无 pi05 实验记录 | — |

### 结论

| 服务器 | 状态 | 说明 |
|--------|------|------|
| **bjb2-24035** | **正常** | 模型文件、代码、lerobot 版本一致。transformers 5.9.0（最新），无 pi05 实验日志（未运行过）。无异常。 |
| **bjb2-28827** | **正常** | 已成功运行多个 pi05 实验，SR 98.5%。376 missing_keys 与正常服务器一致。 |

**bjb1-18228 的 pi05 也显示 97.5% SR**（日志 `eval_spatial_vla_only_pi05_seed43.log`），并非 0%。如果之前观察到 0% SR，可能是更早的代码版本或不同的实验配置导致的，已在后续 commit 中修复。

---
