# check analysis pipeline readiness

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_analysis_pipeline_readiness_20260515T014857_result.json`
- **Structured JSON:** [`96d7e0d7d0f287ec21b0.json`](../../sessions/96/96d7e0d7d0f287ec21b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整审查完成。以下是分析结论。

---

## 分析代码审查结果

**主脚本**: `/root/autodl-tmp/pacs/analyze_n500_unified.py` (676 行)

### 各项检查

| 要求 | 状态 | 说明 |
|------|------|------|
| median（非 mean） | ✅ | `np.median(diffs)` + `bootstrap_median_ci` 均用 median |
| Bootstrap B=10000 | ✅ | `B_BOOT = 10000` |
| d_z within-importance only | ✅ | `within_dz_importance` 仅对 imp pairs 计算 d_z；rand 和 imp-vs-rand 仅报 Wilcoxon + median_diff |
| 输出格式 | ✅ | aggregate table, per-condition breakdown, Cohen's d table, CSV/JSON/LaTeX |

### 一个差异点

任务要求"paired permutation test"，但脚本用的是 **Wilcoxon signed-rank test** (`scipy.stats.wilcoxon`)。Permutation test 仅用于 dose-response 单调性检验。n=500 时两者结论基本一致，但方法论上不同。如果论文要求严格用 permutation test，需要修改 `analyze_condition` 中的检验方法。

---

## Dry-run 结果（s015 + s020，共 8 conditions，各 n=500）

### DeepSeek
| Condition | Median II (low−high) | 95% CI | p_bonf |
|-----------|---------------------|--------|--------|
| imp_s015 | +0.3907 | [0.3496, 0.4431] | <0.0001 |
| imp_s020 | +1.2149 | [1.1072, 1.3365] | <0.0001 |
| rand_s015 | +0.0139 | [−0.0167, 0.0389] | 1.0000 |
| rand_s020 | +0.0315 | [−0.0112, 0.0767] | 1.0000 |

Within-imp d_z: s015 vs s020 = **−0.468** [−0.528, −0.415] (small)

### Qwen
| Condition | Median II (low−high) | 95% CI | p_bonf |
|-----------|---------------------|--------|--------|
| imp_s015 | +0.0659 | [0.0492, 0.0925] | <0.0001 |
| imp_s020 | +0.3073 | [0.2612, 0.3564] | <0.0001 |
| rand_s015 | −0.0111 | [−0.0390, 0.0124] | 1.0000 |
| rand_s020 | +0.0153 | [−0.0145, 0.0684] | 1.0000 |

Within-imp d_z: s015 vs s020 = **−0.509** [−0.608, −0.422] (medium)

**对比 n=50**: DeepSeek s015 Δ=0.32→0.39, s020 Δ=1.15→1.21，方向一致、幅度接近，n=500 CI 显著收窄。

---

## 数据就绪状态

- s015: ✅ 4/4 conditions (profiling_results.json 存在)
- s020: ✅ 4/4 conditions
- s025: ⏳ 目录已创建但无 profiling_results.json（实验进行中）
- s030: ❌ 目录不存在

---

## 全量分析一键命令

数据到齐后：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/pacs && \
python3 analyze_n500_unified.py --csv --latex
```

输出写入 `analysis_output/n500_unified.json` + `.csv`，LaTeX 表格打到 stdout。

---
