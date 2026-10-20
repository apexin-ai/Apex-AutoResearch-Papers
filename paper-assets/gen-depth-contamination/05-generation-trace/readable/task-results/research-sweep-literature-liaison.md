# research sweep literature liaison

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sweep_literature_liaison_20260520T182547_result.json`
- **Structured JSON:** [`e7e695fdf8dbbf718e3e.json`](../../sessions/e7/e7e695fdf8dbbf718e3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**报告已注册** → `artifacts/exp_contamination_rate_sweep/report/contamination_rate_sweep_literature_analysis.md`

**核心发现：**

1. **Dose-response 一致**：Du et al. (2025) 的 20-30% 阈值和 Dohmatob et al. (ICLR 2025) 的理论结果都预测了我们观察到的 "污染越高，binary filtering 收益越大" 模式。没有论文做过我们这样的系统性 contamination rate × filtering strategy 矩阵。

2. **Graduated ≈ no_filter 是新发现**：没有论文直接比较过 binary vs depth-graduated filtering。现有 weighting 文献 (He et al. golden ratio, Kuo et al. ICLR 2025) 的 weighting 都在 real/synthetic 二元轴上，不在 depth 轴上。我们的 graduated 失败可以被 K\*=2 自洽解释：depth≥1 特征已收敛，depth-graduated weights 是在 noise 上加权。

3. **100% binary 不可用**：这是 trivial 的边界条件，Amin et al. 的 β>0 最低要求隐含了这一点，不构成新贡献。

4. **新增 5 篇论文到 literature_map.yaml**：Du et al., He et al., Bakshi & Chakraborty, Nait Saada et al., Zhu et al.

---
