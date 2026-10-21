# analysis p7 dedup investigation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p7-dedup-investigation_20260515T173157_result.json`
- **Structured JSON:** [`e4ec62bf91a980c54d3d.json`](../../sessions/e4/e4ec62bf91a980c54d3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### P7 (aime2024_II_07) 去重异常：72 raw → 1 unique

**Root Cause: parse 失败率 97.2%，不是 dedup 逻辑 bug。**

| 假说 | 结论 |
|------|------|
| solver timeout 误判 UNSAT | **排除** — timeout 返回 `unknown`，代码正确只在 `unsat` 时判等价 |
| 变量名冲突导致 trivial equivalence | **排除** — 同名同 sort 的 Z3 变量共享是正确行为 |
| Int/Real 类型不匹配 | **次要问题** — `N%7==0` 用 `Int('N')`，`N>=1000` 用 `Real('N')`，不会 false-merge 但阻止 MAX-SAT 关联 |
| LLM 输出不可 parse 的 z3_formula | **主因** — 72 个中仅 2 个成功 parse，其余含数组索引/字符串操作/Python 推导式等 |

**数据**：
- 实际 P7: 72 extracted → 2 parsed (2.8%) → 2 等价 → 1 unique (weight=2)
- 合成测试: 规范 Z3 公式 parse rate 79%，说明 parser 本身尚可
- dedup 仅耗时 0.022s，与只处理 2 个约束一致

**修复方向**：
1. extraction prompt 强化对模运算/数位题的引导
2. parser 增加 `mod` 关键字 → `%` 转换
3. 统一 Int/Real sort（检测到模运算时全用 Int）

诊断脚本在服务器 `/root/symb_invariant_consensus/diagnose_p7_dedup.py`，报告已追加到 memory.md。

---
