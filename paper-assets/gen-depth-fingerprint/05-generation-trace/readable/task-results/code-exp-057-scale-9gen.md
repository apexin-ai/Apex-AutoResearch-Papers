# code exp 057 scale 9gen

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_057_scale_9gen_20260520T070611_result.json`
- **Structured JSON:** [`4b61a74a31715114ffc6.json`](../../sessions/4b/4b61a74a31715114ffc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Data validation passed. Here's the summary:

## 状态

**Feature extraction: 不需要.** qwen3-8b 的 7-feature 已在 `features_all_models.csv` 中（4497 行），8-gen LOGO 评估已完成（qwen3-8b macro_f1=0.7009）。

## 9-gen LOGO 准备就绪

| 来源 | Generator | 行数 | Depths |
|------|-----------|------|--------|
| CSV (6 gen) | pythia-2.8b, pythia-1b, olmo-2-1b, qwen3-0.6b, qwen3-1.7b, qwen3-8b | 27,529 | 0-4 |
| JSONL | llama-3.2-3b | 4,680 | 0-4 |
| JSONL | mistral-7b-v0.3 | 4,849 | 0-4 |
| JSONL (新) | **gemma-2-2b** | 1,061 | 0-4 |
| **合计** | **9 generators** | **38,119** | |

## 执行命令

```bash
cd /root/gen-depth-fingerprint && python3 eval_9gen_logo.py
```

- **GPU**: 不需要（XGBoost CPU 评估）
- **预估时间**: 2-3 分钟
- **输出**: `results/9gen_logo_results.json`
- **脚本位置**: `/root/gen-depth-fingerprint/eval_9gen_logo.py`

vs 8-gen 基线比较: 自动从 `results/8gen_logo_results.json` 读取并计算 delta。

等审批后执行。

---
