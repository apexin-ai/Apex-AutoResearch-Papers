# paper theory section fixes

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_theory_section_fixes_20260517T185407_result.json`
- **Structured JSON:** [`003d4b7dc03d8c8a5914.json`](../../sessions/00/003d4b7dc03d8c8a5914.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修改完成报告

### 修改 1：AUC 数值（两个文件）

**文件 A**: `artifacts/_project/paper/theory_draft.tex` line 110
| 项 | 旧值 | 新值 |
|---|---|---|
| AUC(d₁,d₂) | ≈ 0.93 | = 0.922 |
| AUC(d₂,d₃) | ≈ 0.85 | = 0.802 |
| AUC(d₃,d₄) | ≈ 0.77 | = 0.712 |
| AUC(d₄,d₅) | ≈ 0.68 | = 0.653 |

**文件 B**: `paper/theory_section_draft.md` line 28 + line 59
- §5.1 (line 28): 0.93→0.922, 0.86→0.802, 0.77→0.712
- §5.2 (line 59): 0.93→0.922, 0.86→0.802, 0.77→0.712, 0.68→0.653

### 修改 2：γ 值与空间明确化

| 文件 | 旧值 | 新值 |
|---|---|---|
| `_project/paper/theory_draft.tex` L110 | γ ≈ 0.80 | γ ≈ 0.75 in KL-divergence space |
| `paper/theory_section_draft.md` L59 | γ ≈ 0.85 in feature space | γ ≈ 0.75 in KL-divergence space |

两处均补充了: "This corresponds to an observed AUC decay ratio of approximately 0.87 between successive depth pairs, connected through Pinsker's inequality (nonlinear mapping)."

### 确认：d3v4 range

Registry 三模型数据完整：
- Pythia: 0.784, OLMo: 0.765, GPT-2 XL: 0.750
- **[0.750, 0.784] 正确，保持不变**

注意：同处 d4v5 range 写 [0.681, 0.694]，但实际 registry 上限为 0.684（OLMo），0.694 偏高。任务未要求修正此值。

### Shi et al. (2025) venue

**确认正确**：NeurIPS 2025 Spotlight。`paper/theory_section_draft.md` line 110 已正确标注。

### 未完成

`post_to_reviewer` 工具不在当前可用工具列表中，无法自动提交审查。需手动触发 reviewer 审查流程。

---
