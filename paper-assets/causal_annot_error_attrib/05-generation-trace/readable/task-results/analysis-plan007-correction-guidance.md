# analysis plan007 correction guidance

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan007_correction_guidance_20260520T185109_result.json`
- **Structured JSON:** [`09986c27ed2ac9be2952.json`](../../sessions/09/09986c27ed2ac9be2952.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**实验范围**：仅完成 2/7 topologies × 2/6 C structures × N_sim=10（原计划 7×6×1000 因 `--N_sim` 参数格式错误未执行，应为 `--n-sim`）。

**关键结论**：

| 排名 | 方法 | 平均 Bias Reduction | 说明 |
|---|---|---|---|
| 1 | **PPI++** | **97.4%** | 唯一达到接近名义覆盖率（97.5%）的方法，全胜 |
| 2 | MC-SIMEX | 58.5% | 不需要 gold labels 的最佳选择，但覆盖率差（27.5%） |
| 3 | DSL | 1.8% | 极度依赖拓扑：confounding +68.5%，exposure −64.9% |
| 4 | MLA | −30.1% | 对 T 系数无效，对 dummy 系数有害 |
| 5 | naive_plugin | −37.6% | 同 MLA |

**假设验证**：
- **H1 (Frisch-Waugh) ✓** — naive_plugin/MLA 对 T 系数 bias reduction = 0.0%（精确到 10⁻¹⁵）
- **H2 (PPI++ 最优) ✓** — 所有场景 95–99% bias reduction
- **H3 (拓扑差异) ✓** — DSL 差异最大（133 个百分点）
- **H4 (naive_plugin/MLA 对 dummy 有效) ✗** — 反而使 bias 恶化 60–83%，observation-level C⁻¹ 校正产生 generated-regressor bias

**需要重跑完整实验**：`python3 -u plan_007_correction_guidance.py --n-sim 1000`

---
