# code exp 002 bugfix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-002-bugfix_20260514T062645_result.json`
- **Structured JSON:** [`53fd90a4efb71607ad6a.json`](../../sessions/53/53fd90a4efb71607ad6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

| 测试 | 结果 | 状态 |
|------|------|------|
| Test1: checkpoint 自动检测 base model | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B` | OK |
| Test1: checkpoint 自动检测 adapter | `...Qwen2.5-0.5B_d005_s42/lora_adapter` | OK |
| Test2: model_id 提取（之前返回 `lora_adapter`） | `Qwen2.5-0.5B_d005_s42` | OK (已修复) |
| Test3: adapter 路径解析到 lora_adapter 子目录 | `.../lora_adapter` | OK |
| Test4: 无 adapter 时 model_id | `Qwen2.5-0.5B` | OK |
| Test5: 不同 dosage 的 model_id | `d000_s42`, `d025_s42`, `d100_s42` | OK |

**修复总结：**

- **Bug 1 (Dosage 命名)**: `extract_model_id()` 现在优先从 adapter 路径提取 model_id，并处理了 `lora_adapter` 子目录名的边界情况（向上取 parent），输出文件不再互相覆盖
- **Bug 2 (Adapter 加载)**: 三个文件都添加了 `resolve_adapter_path()` 自动查找 `lora_adapter/` 子目录；`compute_signals.py` 还添加了 `resolve_model_paths()` 自动从 `train_config.json` 提取 base model 路径

已部署到远程 `cqa1-21977` 的文件：`compute_signals.py`、`signal_minkpp.py`、`signal_selfcritique.py`。

---
