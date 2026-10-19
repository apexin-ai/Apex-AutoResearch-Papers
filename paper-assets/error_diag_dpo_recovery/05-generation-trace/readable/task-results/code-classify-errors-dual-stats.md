# code classify errors dual stats

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_classify_errors_dual_stats_20260512T174428_result.json`
- **Structured JSON:** [`fef0d7d8708106aef9fb.json`](../../sessions/fe/fef0d7d8708106aef9fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改总结：

**代码差异**（`src/classify_errors.py`，424→542行）：
1. **L28-29**：新增 `import random` 和 `from statistics import mean, median, stdev`
2. **L299-305**：`_rule_based_error_type(correction_span)` — 基于 correction_span 的规则分类器（≤3→action, ≤6→verification, 7+→planning），用于 dry_run 模式测试统计管道
3. **L308-393**：`run_dual_analysis(records, output_dir)` — 核心函数：
   - Version A：全量 Kruskal-Wallis
   - Version B：按 `game_file` 去重（seed=42），保守版
   - 打印对比表 + 写 `p1_analysis.json`
   - 样本数 <3 时跳过检验并打印警告
4. **L484-495**：dry_run 路径调用（用规则分类器）
5. **L528-537**：full 分类路径调用（用 LLM 实际结果）

**Dry-run 结果**：
- 34条匹配轨迹，全部 correction_span≥6，规则分类器分为 verification(N=5) 和 planning(N=29)
- Version A/B 完全一致（本数据集34条轨迹的 game_file 无重复）
- Kruskal-Wallis: H=12.8224, p=0.000343
- JSON 已写入 `/tmp/p1_analysis.json`

---
