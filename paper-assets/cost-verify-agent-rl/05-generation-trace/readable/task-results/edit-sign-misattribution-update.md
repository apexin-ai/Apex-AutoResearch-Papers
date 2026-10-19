# edit sign misattribution update

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_edit_sign_misattribution_update_20260517T062644_result.json`
- **Structured JSON:** [`84151bb523002757b194.json`](../../sessions/84/84151bb523002757b194.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改完成。汇总：

---

### 更改汇总

**文件 1: `failure_unification_table.md`** — 5 处更新：

| 位置 | 原表述 | 新表述 |
|------|--------|--------|
| Summary (L5) | "Credit Assignment Decay: γ-attenuated credit ... undifferentiated failure" | "Advantage Sign Misattribution: advantage SIGN determined by episode outcome, not window-local action quality..." |
| Summary (L5) | "structural credit assignment decay (γ^k attenuation + undifferentiated failure signal)" | "structural advantage sign misattribution (direction error from episode-level outcome + γ^k magnitude attenuation)" |
| exp013f Key Evidence (L11) | "failed episodes distribute identical negative advantage across all windows" | "failed episodes assign incorrect advantage SIGN to all windows (good actions penalized, bad actions reinforced based on episode outcome rather than action quality)" |
| exp026 Root Cause (L13) | 旧的 Credit Assignment Decay 描述 | "Advantage sign misattribution: advantage SIGN determined by episode outcome..." |
| Community value (L28) + Scope (L35) | "Credit Assignment Decay" | "Advantage Sign Misattribution" with sign error explanation |

**文件 2: `credit_assignment_analysis.py`** — 完整重写：
- Docstring 改为 "Advantage Sign Misattribution Analysis"
- Fig A 注释明确标注 magnitude decay 是次要机制，sign misattribution 才是根本问题
- 新增 `plot_sign_misattribution()` 占位函数（四象限可视化）

**文件 3: `why_step_independent.md`** — 1 处更新：
- Section 5 (L95): 在 "all steps get the same reward" 后插入 sign misattribution 解释，替代原来的 "making within-group normalization collapse"

---
