# ops lm eval dataset precache

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_lm_eval_dataset_precache_20260515T220904_result.json`
- **Structured JSON:** [`49ed4a728de362446463.json`](../../sessions/49/49ed4a728de362446463.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部离线验证通过。汇总报告：

## 数据集缓存状态

| 数据集 | 状态 | 样本数 |
|--------|------|--------|
| WikiText-2 (test) | ✅ 已缓存（之前就有） | 4,358 |
| WikiText-103 (train+test) | ✅ 已缓存（之前就有） | - |
| ARC-Challenge (test) | ✅ 新缓存 | 1,172 |
| ARC-Easy (test) | ✅ 新缓存 | 2,376 |
| WinoGrande (val) | ✅ 新缓存 | 1,267 |
| MMLU - cais/mmlu (全部 57 科目) | ✅ 新缓存 | 14,042 |
| GSM8K (test) | ✅ 新缓存 | 1,319 |
| C4 (validation, streaming) | ❌ 无法预缓存 | - |

### C4 说明
`allenai/c4` streaming 模式初始化在此网络环境下持续超时（尝试了 HF 直连和 hf-mirror 均失败）。hub 元数据已缓存在 `/root/autodl-tmp/.hf_cache/hub/datasets--allenai--c4/`。项目 `evaluate.py` 已提供 `--skip_c4` 选项可绕过。运行 C4 PPL eval 时需要保证网络畅通。

### lm-eval 数据源确认
- lm-eval 0.4.12 的 `mmlu` task 使用 `cais/mmlu`（不是 `hails/mmlu_no_train`）
- `arc_challenge` → `allenai/ai2_arc` ARC-Challenge
- `winogrande` → `allenai/winogrande` winogrande_xl
- `gsm8k` → `openai/gsm8k` main

所有数据集均已通过 `TRANSFORMERS_OFFLINE=1` 离线加载验证。

---
