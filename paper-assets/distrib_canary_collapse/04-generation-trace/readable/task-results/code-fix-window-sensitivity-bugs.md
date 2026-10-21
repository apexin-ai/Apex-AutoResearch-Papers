# code fix window sensitivity bugs

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_window_sensitivity_bugs_20260516T001053_result.json`
- **Structured JSON:** [`c923434143d0c8e534dc.json`](../../sessions/c9/c923434143d0c8e534dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修复内容**：
1. **Off-by-one** (line 193): `[:T]` → `[:T+1]`，T=10 现在取 11 个数据点 (gen_0–gen_10)
2. **TY 实现统一**: 删除本地 `toda_yamamoto` / `toda_yamamoto_v2`（79 行），改为从 `method_ablation.py` 导入canonical实现（ADF d_max + fixed p=1 + F-test）

**关键变化**：
- 旧 TY 在 T=10 返回 `p=nan`（0/6 sig），因 VAR `test_causality` 在短序列上静默失败
- 修复后 T=10 TY = **4/6 sig**（TE→d1/d2/d3 全 4/4，ECE→d1 3/4）

**验证通过**：T=10 TY 结果与 ty_audit Method A 11-point 表格一致（TE 4/4，ECE→d1 3/4）

**4/5 consensus 结论不受影响**：所有 6 对在 T=5–10 全窗口均保持 robust（≥4/5 methods），因 NX/DX/TH/PG 四法已足够。

报告已写入 `artifacts/window_sensitivity_t11/window_sensitivity_fixed.md`。

---
