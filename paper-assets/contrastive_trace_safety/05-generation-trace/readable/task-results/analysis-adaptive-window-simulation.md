# analysis adaptive window simulation

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_adaptive_window_simulation_20260517T052256_result.json`
- **Structured JSON:** [`a568c7c2239fbf72719b.json`](../../sessions/a5/a568c7c2239fbf72719b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

**结论：POSITIVE，但改进幅度有限。**

Two-stage (W_screen=3, W_confirm=15, k=1) 实现了对 single-stage Pareto frontier 的技术性 domination：
- 相同 coverage (0.7692) 下 precision 提升 +1.3pp（对比 W=15）
- 相同 precision (0.7222) 下 coverage 提升 +5.1pp（对比 W=20）

**关键限制：**
1. 测试集小（n=55），1-5pp 的差异在噪声范围内
2. 所有方法的 benign FPR 极高（93-100%），因为 probe 仅在 jailbreak traces 上训练，无法区分 benign 与 pre-CP 状态
3. 未能 dominate 最高 coverage 点 W=1（cov=0.8462）
4. 最优配置 k=1，Stage 2 实质是大窗口 probe 的单步确认，非真正的连续步确认

**建议**：Two-stage 作为 methodological contribution 较弱（改进在噪声范围内）。适合作为 "practical deployment strategy" 在 discussion 中提及，而非核心方法贡献。

产出已保存至：
- `artifacts/exp_pathC_two_stage/results.json`
- `artifacts/exp_pathC_two_stage/pareto_comparison.pdf`
- `artifacts/exp_pathC_two_stage_summary.md`
- `src/experiments/exp_pathC_two_stage_sim.py`

---
