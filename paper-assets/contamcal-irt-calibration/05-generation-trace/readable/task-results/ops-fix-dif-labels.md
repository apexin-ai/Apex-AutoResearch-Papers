# ops fix dif labels

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-dif-labels_20260523T092229_result.json`
- **Structured JSON:** [`7d960788750f70a02109.json`](../../sessions/7d/7d960788750f70a02109.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改摘要：

| 文件 | 修改内容 |
|------|---------|
| `analysis/compare_dif_models.py` | docstring、model keys (`uniform_dif`/`nonuniform_dif`)、`compute_ppp` 分支、列标题、比较打印全部交换 |
| `analysis/dif_comparison/results.json` | `"nonuniform"` → `"uniform_dif"`，`"uniform"` → `"nonuniform_dif"` |
| `stan_models/contam_irt_2pl_gamma_uniform.stan` | 注释 "UNIFORM DIF variant" → "NON-UNIFORM DIF variant" |
| `stan_models/contam_irt_2pl_gamma.stan` | 无需改（注释仅描述公式，未标注 DIF 类型） |
| 本地 `dif_model_comparison.md` | 所有列标题、解读文字中的 uniform/non-uniform 交换 |

数值结果未变，仅标签修正。

---
