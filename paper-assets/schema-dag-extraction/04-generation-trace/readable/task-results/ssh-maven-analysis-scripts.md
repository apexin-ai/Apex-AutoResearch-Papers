# ssh maven analysis scripts

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_maven-analysis-scripts_20260515T062257_result.json`
- **Structured JSON:** [`dd1eec3abae4c64515ba.json`](../../sessions/dd/dd1eec3abae4c64515ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

**新增文件**: `src/analyze_maven_results.py`（服务器 + 本地同步）

**CLI 用法**:

```bash
# dry-run（mock data 验证逻辑）
python3 src/analyze_maven_results.py \
    --bcs_matrix artifacts/maven_bcs_matrix_qwen3.pt \
    --output results/maven_analysis_dryrun.json \
    --dry-run

# exp-004 跑完后的实际分析
python3 src/analyze_maven_results.py \
    --results_dir artifacts/exp004/ \
    --bcs_matrix artifacts/maven_bcs_matrix_qwen3.pt \
    --output results/maven_analysis.json
```

**dry-run 结果**（mock 数据，correlation 预期不显著）:

| Layer | 指标 | 值 |
|-------|------|----|
| L1 Pairwise | 780 pairs, Pearson r | -0.038 (p=0.29) |
| L1 Nonzero-only | n=552, Spearman ρ | -0.050 (p=0.24) |
| L2 Per-type | 40 types, Pearson r | -0.028 (p=0.86) |
| L2 Partial r | (控制 log-freq) | -0.029 (p=0.86) |
| L3 count_12 | n=25, r(F1,pctBCS) | -0.021 (p=0.92) |
| L3 count_24 | n=25, bcs_range=0.053 | -0.173 (p=0.41) |

三层分析逻辑均正确运行，输出格式符合规范。等 exp-004 (PID 224685) 结束后将 `--results_dir` 指向实际输出目录即可。

---
