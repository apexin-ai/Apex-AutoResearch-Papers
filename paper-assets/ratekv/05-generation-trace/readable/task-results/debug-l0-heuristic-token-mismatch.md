# debug l0 heuristic token mismatch

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_l0_heuristic_token_mismatch_20260514T063920_result.json`
- **Structured JSON:** [`99317326ff9440cc46d2.json`](../../sessions/99/99317326ff9440cc46d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

### Bug 根因

`run_l0_heuristic_corrected.py` 中 MCKP PPL 是**硬编码的参考值**（从之前的实验复制），不是在脚本中实际 eval 的。

具体问题：
- Qwen 硬编码 `mckp_ppl: 9.569`，但这个值来源不明（exp_e_hires 实际为 10.9131）
- 硬编码值与 plan_015 的 eval 条件不同，导致 MCKP 9.569 < baseline 9.8106（量化不可能优于 baseline）

你提到的 "288937 tokens" 实际是 **Llama-3.1-8B 的 token count**（不同 tokenizer 产生不同 token 数），不是 MCKP 条件的异常。Qwen 所有条件均为 298938 tokens，Llama 均为 288937 tokens，Mistral 均为 331726 tokens。

### 修复方案

写了 `rerun_mckp_eval.py`，对三个模型实际跑 MCKP allocation（从 hires profiling 结果加载），使用与其他条件完全相同的 `evaluate_perplexity` 函数。

### 附加问题

主实验在 Mistral L0-random seed=1 处崩了（tmux session 消失，结果文件未生成）。写了 `rerun_mistral_remaining.py` 补跑剩余条件。

### 最终结果（budget=0.25, bf16, WikiText-2 test）

```
Model                    BF16    Unif4     MCKP         L0rand    Naive
----------------------------------------------------------------------
Qwen2.5-7B              9.811   15.445   10.913  11.691±0.422   12.230
Llama-3.1-8B            8.092    8.469    8.450  10.479±1.033    9.941
Mistral-7B-v0.3         7.035    7.131    7.323   7.560±0.087    7.481
```

所有 MCKP > baseline ✓。Token count 同模型内一致 ✓。结果已保存至 `/root/ratekv/l0_heuristic_corrected_results.json`，registry 已更新。

---
