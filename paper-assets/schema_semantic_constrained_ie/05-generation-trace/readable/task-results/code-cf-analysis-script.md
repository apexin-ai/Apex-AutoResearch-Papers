# code cf analysis script

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cf_analysis_script_20260515T133441_result.json`
- **Structured JSON:** [`46750334985080dc4e29.json`](../../sessions/46/46750334985080dc4e29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**产出：**

1. `/root/schema_semantic_constrained_ie/analyze_cf_fallback.py` — 502 行完整脚本

2. **Smoke test 结果**（用 `phase2_scierc_full_s1_v2.jsonl` 模拟 CF fallback 输入）：
   - Checker 调用成功：`DR=0.93% CF=9.90% R-F1=8.36% E-F1=30.98%`（与 baseline 完全一致，因为用的同一份数据）
   - 对比表格生成正确，ΔDR/ΔCF=0（符合预期）
   - 缺失文件正确跳过并报 warning
   - Fallback stats 报 "not found yet"（正确）
   - Violation budget 计算正确

3. **输出文件全部生成**：
   - `dr_vs_cf_pareto.pdf` (21KB) + `.png` (61KB)
   - `comparison_table.md`
   - `violation_budget.md`
   - `violation_report_cf_fb_qwen_scierc.json`

4. 临时 symlink 已清理。

**脚本功能**：5 个模块——checker 调用 → 对比表格 → Pareto 散点图 → fallback 触发率 → violation budget。DocRED 的 F1 通过 `compute_f1_from_jsonl` 从 JSONL 直接计算（DocRED checker 不输出 F1）。CF fallback 实验完成后，直接 `python3 analyze_cf_fallback.py` 即可。

---
