# audit paper number consistency

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper-number-consistency_20260521T092353_result.json`
- **Structured JSON:** [`2d30609308ee4a36014b.json`](../../sessions/2d/2d30609308ee4a36014b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。~180 个数字已交叉验证，结果写入 `artifacts/paper_number_audit.md`。

**必须修复的 3 个高严重度问题：**

1. **experiments.tex L60: "13–26pp" 应为 "19–26pp"** — 全文其他位置（abstract、intro、conclusion）都写 19–26pp，唯独这里写了 13。13 无任何数据来源支持。

2. **TOST p 值不一致** — 同一个 ±2pp TOST 检验，sensitivity table 写 0.0087，Holm table 写 0.0071，正文写 0.007。三处应该是同一个数。

3. **Table 2 TRAJ 4B 数值与 registry 不符** — Table 2 写 s42=85.27, s123=86.72；registry 存的是 s42=85.66, s123=85.47。差距 0.39–1.25pp，不是四舍五入能解释的。需要查来源。

**中等严重度 2 个：**
- Table 3 DeepSeek 0-shot 写 48.50，appendix 同一个数写 48.54（registry 也是 48.54）
- CLS 8B s123 function-level: Table 2 写 89.40，registry 记录 89.37

**低严重度 3 个 + 清晰度警告 2 个** 详见报告。其余 ~167 个数字全部验证通过。

---
