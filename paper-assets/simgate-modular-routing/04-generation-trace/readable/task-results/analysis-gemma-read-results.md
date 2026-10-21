# analysis gemma read results

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma-read-results_20260520T235201_result.json`
- **Structured JSON:** [`2a47c5b6112098804de5.json`](../../sessions/2a/2a47c5b6112098804de5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Found the bugs. Here are the complete results and critical issues.

---

## analysis.json 完整数据（11 tasks × 20 eps = 220 total）

### Per-task

| Task | N | int_DR | det_DR | ΔDR | det_pref | int_pref | no_pref |
|------|---|--------|--------|-----|----------|----------|---------|
| identify-life-stages-1 | 20 | 55.0% | 80.0% | -25.0pp | 7 | 0 | 12 |
| identify-life-stages-2 | 20 | 55.0% | 80.0% | -25.0pp | 5 | 0 | 15 |
| freeze | 20 | 60.0% | 80.0% | -20.0pp | 5 | 0 | 15 |
| grow-fruit | 20 | 40.0% | 60.0% | -20.0pp | 4 | 0 | 16 |
| measure-melting-point | 20 | 50.0% | 75.0% | -25.0pp | 7 | 0 | 13 |
| lifespan-longest-lived | 20 | 55.0% | 60.0% | -5.0pp | 4 | 0 | 15 |
| lifespan-LL-SL | 20 | 55.0% | 75.0% | -20.0pp | 7 | 0 | 13 |
| chemistry-mix | 20 | 45.0% | 55.0% | -10.0pp | 3 | 0 | 16 |
| inclined-plane | 20 | 55.0% | 85.0% | -30.0pp | 6 | 0 | 13 |
| find-animal | 20 | 35.0% | 60.0% | -25.0pp | 6 | 0 | 14 |
| find-non-living-thing | 20 | 60.0% | 25.0% | +35.0pp | 9 | 0 | 8 |

### Aggregate

- **N**: 220
- **Int DR**: 51.36%
- **Det DR**: 66.82%
- **ΔDR**: -15.45pp
- **Δ_full**: -25.0091
- **Δ_nd**: 0.24 (n_nd=25)
- **DAF**: 100.96%
- **mean_int_score**: -33.73
- **mean_det_score**: -8.72
- **Labels**: det_pref=63 (28.6%), int_pref=0 (0%), no_pref=150 (68.2%)

### Bootstrap 95% CI (B=10000, cluster K=11)

- **Int DR**: [46.82%, 55.45%]
- **Det DR**: [56.36%, 75.91%]
- **ΔDR**: [-23.64pp, -4.09pp]
- **DAF**: [98.34%, 103.41%]

### Cross-model table

| Model | Int DR | Det DR | ΔDR | DAF |
|-------|--------|--------|-----|-----|
| Qwen2.5-7B | 42.9% [36.7,49.0] | 16.3% [11.8,21.2] | +26.5pp [20.4,32.7] | 90.4% [81.3,99.1] |
| Llama-3.1-8B | 41.4% [35.0,47.7] | 11.4% [7.3,15.9] | +30.0pp [23.6,36.4] | 88.2% [80.2,95.1] |
| Gemma-2-9B | 51.4% [46.8,55.5] | 66.8% [56.4,75.9] | -15.5pp [-23.6,-4.1] | 101.0% [98.3,103.4] |

---

## 分析脚本有两个 bug，数据不可用于论文

### Bug 1: label 字符串不匹配

脚本用 `e["label"] == "int-preferred"` 匹配，但实际 label 值是 `"internal-preferred"`。导致 **int_pref 全部为 0**。

验证：ILS-1 raw data episode 5 明确 `label: "internal-preferred"`，但 analysis.json 报 int_pref=0。aggregate label 合计 63+0+150=213，缺 7 个 episode（正是被漏掉的 internal-preferred）。

### Bug 2: DR 定义是 score==0（零分率），不是 score==-100（实际死亡率）

脚本第 78-79 行：
```python
int_deaths = sum(1 for e in eps if e["internal_score"] == 0)
det_deaths = sum(1 for e in eps if e["deterministic_score"] == 0)
```

对比 ILS-1 raw data:
- **score=-100 的实际死亡**: internal 8/20=40%, det 2/20=10% → 与 Qwen/Llama 同向 (+30pp)
- **score=0 的零分率** (脚本用的): internal 11/20=55%, det 16/20=80% → 反向 (-25pp)

Gemma 大量 episode 的 internal 路由 score=-100（真死亡），这些不被当前 DR 统计捕获。

### 附加问题：find-non-living-thing 有 34 行

文件被追加了 14 行重复数据（episode 0-13 重跑）。当前 analysis.json 是在 20 行时生成的，但如果重跑脚本会加载全部 34 行。

### latex_table.tex（旧版本，7 tasks，用的是正确的死亡定义）

仅供参考，这个文件用 score=-100 作为 DR，只覆盖了 7 个 task（另4个标 missing），140 episodes aggregate: Int DR 38.6%, Det DR 13.6%, ΔDR +25.0pp, DAF 99.9% [99.5, 100.0]。

---

**结论**：analysis.json 数据因上述两个 bug **不能直接用于论文**。需要修复脚本（label 匹配 + DR 定义改为 score≤0 或 score==-100）后重跑。是否需要我现在修复并重跑？

---
