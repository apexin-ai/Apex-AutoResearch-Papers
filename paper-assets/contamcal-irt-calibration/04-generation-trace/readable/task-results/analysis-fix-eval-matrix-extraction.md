# analysis fix eval matrix extraction

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fix-eval-matrix-extraction_20260515T122746_result.json`
- **Structured JSON:** [`340d13cd4f2e99ee971f.json`](../../sessions/34/340d13cd4f2e99ee971f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复成功。arc_challenge 和 humaneval 列现在都有数据了。

## 结果汇报

### 覆盖情况（排除 deprecated）

| Benchmark | N_aligned | N_irt |
|-----------|-----------|-------|
| MMLU | 36 | 45 |
| GSM8K | 36 | 46 |
| ARC_challenge | 36 | 45 |
| HumanEval | 36 | 46 |

### Bug 根因

旧脚本 CSV 列名用 `arc`，但 JSON 字段名是 `arc_challenge`；humaneval 的指标键是 `pass@1` 而非 `accuracy`，两个都没匹配上导致全空。

### Deprecated configs（6 个）

| Config | 原因 |
|--------|------|
| `Qwen2.5-1.5B_base_pretrained` | base_pretrained 参考基线 |
| `Qwen2.5-3B_d000_s42_v3_aligned` | D018 LoRA 超参损伤 (GSM8K=0.1198) |
| `Qwen2.5-3B_d000_v1_s123_DEPRECATED` | 目录名标记 DEPRECATED |
| `Qwen2.5-3B_d000_v1_s42_aligned_DEPRECATED` | 目录名标记 DEPRECATED |
| `Qwen2.5-3B_d005_v1_s42_aligned_DEPRECATED` | 目录名标记 DEPRECATED |
| `Qwen2.5-3B_d100_v1_s42_aligned_DEPRECATED` | 目录名标记 DEPRECATED |

### 空目录（9 个，无 eval_results.json）

| 目录 | 状态 |
|------|------|
| `Qwen2.5-0.5B_base_pretrained` | 空 |
| `Qwen2.5-0.5B_base_pretrained_aligned` | 空 |
| `Qwen2.5-0.5B_d000_s42_para` | 空 |
| `Qwen2.5-0.5B_raw` | 空 |
| `Qwen2.5-1.5B_d005_s123_aligned` | 空 |
| `Qwen2.5-1.5B_d025_s123_aligned` | 空 |
| `Qwen2.5-3B_d000_s123_aligned` | 空 |
| `Qwen2.5-3B_d000_v3_s42_aligned` | 空 |
| `Qwen2.5-3B_d005_s42_aligned` | 空 |

CSV 已写入 `/root/autodl-tmp/exp001/eval_summary_matrix.csv`，52 行，脚本保存在 `/root/contamcal-irt-calibration/scripts/gen_eval_matrix.py`。

---
