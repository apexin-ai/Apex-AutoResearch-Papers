# research paper n500 update audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_n500_update_audit_20260514T204335_result.json`
- **Structured JSON:** [`2dd48a8853e4695f747f.json`](../../sessions/2d/2dd48a8853e4695f747f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清单已产出至 `artifacts/n500_update_checklist.md`。

## 汇总

**更新点总数**：70 个（去重后），82 处引用（含跨 section 重复）

**按 section 分布**：
- Results (§5)：**26 处**（最密集——4 张表 + 1 张图 + 所有定量声明）
- Appendix (moved content)：14 处
- Abstract：8 处
- Discussion/Conclusion：12 处
- 其余 section：12 处

**图表需重新生成**：5 张（fig1_dose_response, fig3_crossover, fig4_bootstrap, fig5_crossmodel + 确认是否有额外 hero figure）

**硬约束合规**：
- D054 (median only) ✅
- D015 (emergent interaction framing) ✅
- D056 (C5b→future work) ✅
- D060 (LLaMA→suggests) ✅，但 results.tex:77 "The qualitative pattern replicates" 建议软化
- **D059 违规 ⚠️ 6 处**：abstract/results/discussion/appendix 中有 imp-vs-rand d_z 和 random d_z，需全部替换为 Wilcoxon p + median_diff。Table 3 (llama-cross-arch) 需要结构重构

**高风险点**：
1. Qwen s015 显著性——D061 显示 n=500 已显著，风险解除
2. Random PASS/FAIL 模式可能因 n=500 功效提升而变化
3. LLaMA 是否跑 n=500（决定 §5.5 全部数据是否更新）
4. Table 3 重构（D059 违规修复涉及整段叙事）
5. Crossover pattern 稳定性
6. C4 entropy 分析是否基于 n=500 重跑（影响 §6 + appendix 2 张表）

---
