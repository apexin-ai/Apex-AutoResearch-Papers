# analysis plan001 data completeness check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan001-data-completeness-check_20260522T071204_result.json`
- **Structured JSON:** [`ac76eb46f2732cc54279.json`](../../sessions/ac/ac76eb46f2732cc54279.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整性检查完成。结果：

**数据覆盖率：100%** — 所有 72 个条件（6 models × 6 attacks × 2 datasets）均有数据，无需补跑。

### 数据分布

| 来源文件 | 内容 |
|---------|------|
| `results_step2v3_regression_*.json` | individual_asr + regression: prompt_injection, sycophancy, score_manipulation |
| `results_taxonomy_broadspectrum_*.json` | individual_asr + regression: verbosity_bias, position_bias, authority_bias |
| `results_step1_full_*.json` | pairwise MI: 15 pairs × 2 datasets (clean condition) |
| `_step2v3_checkpoint.json` | raw clean scores (6 models × 2 datasets × 300) + attacked scores (3 attacks) |
| `_taxonomy_checkpoint.json` | raw clean scores (同上) + attacked scores (3 taxonomy attacks) |

### Clean scores
6 个模型在 2 个 dataset 上的 clean individual scores（各 300 samples）完整存在于两个 checkpoint 文件中。

### 磁盘
- `/root/`: 15GB 可用 / 30GB
- `/root/autodl-tmp/`: 61GB 可用 / 250GB（模型占 172GB）

### 已创建目录
- `artifacts/results/plan001/`
- `artifacts/results/plan001/individual_scores/`
- `artifacts/results/plan001/mi_matrix/`
- `artifacts/results/plan001/panel_regression/`

报告写入 `/root/cert_manip_resist_eval/artifacts/results/plan001_data_completeness.json`。

---
