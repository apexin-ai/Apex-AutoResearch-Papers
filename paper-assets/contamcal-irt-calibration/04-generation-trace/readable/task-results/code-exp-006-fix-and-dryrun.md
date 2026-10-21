# code exp 006 fix and dryrun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_006_fix_and_dryrun_20260514T151631_result.json`
- **Structured JSON:** [`e43acf835130257b5663.json`](../../sessions/e4/e43acf835130257b5663.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果

### 修改内容
代码已有 `--model-scale`、`--data-seed`、`--aligned-only` 过滤。修改了 `--dry-run` 行为：现在只打印数据加载摘要并 return，**不启动 Stan fitting**。

### Dry-run 输出
```
[DRY-RUN] Model scale: 0.5B, Seed: 42
[DRY-RUN] Aligned only: True
[DRY-RUN] Loading directories:
  - Qwen2.5-0.5B_d000_s42_aligned (dosage=0, seed=42)
  - Qwen2.5-0.5B_d005_s42_aligned (dosage=5, seed=42)
[DRY-RUN] Total models: 2
[DRY-RUN] Dosages: [0, 5]
[DRY-RUN] mmlu: 2 valid models x 14042 items
[DRY-RUN] gsm8k: 2 valid models x 1319 items
[DRY-RUN] arc_challenge: 2 valid models x 1172 items
[DRY-RUN] humaneval: 2 valid models x 164 items
[DRY-RUN] Stan model: 4pl_gamma -> contam_irt_4pl_simple.stan
[DRY-RUN] Exposure file: None (oracle dosage)
```

### 数据缺口
**只有 2/4 个 dosage 点可用，缺少 d025 和 d100 的 aligned eval：**

| 目录 | 状态 |
|------|------|
| `Qwen2.5-0.5B_d000_s42_aligned` | eval_results.json ✓ |
| `Qwen2.5-0.5B_d005_s42_aligned` | eval_results.json ✓ |
| `Qwen2.5-0.5B_d025_s42_aligned` | **空目录** |
| `Qwen2.5-0.5B_d100_s42_aligned` | **空目录** |

非 aligned 的 `d100_s42` 有 eval_results.json，但 aligned 格式的 d025 和 d100 还没跑完。

2 个模型 × 14042 items 做 IRT fitting 没有意义（至少需要 3-4 个 dosage 点才能拟合 dose-response curve）。需要先补齐 d025 和 d100 的 aligned eval 再跑 exp-006。

---
