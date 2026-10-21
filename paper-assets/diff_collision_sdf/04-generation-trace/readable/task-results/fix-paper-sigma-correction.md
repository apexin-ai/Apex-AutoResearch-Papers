# fix paper sigma correction

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_paper_sigma_correction_20260527T170749_result.json`
- **Structured JSON:** [`4a5794d253310a7248a2.json`](../../sessions/4a/4a5794d253310a7248a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

旧数字全部清除，新数字全部到位。

---

## 修改清单

| 文件 | 行 | 旧值 | 新值 |
|------|-----|------|------|
| claim3.tex | 7 | `z=1.85, p≈0.032` | `z=1.76, p≈0.039` |
| claim3.tex | 33 | `σ=1.94, z=1.85, p≈0.032` | `σ=2.04, z=1.76, p≈0.039` |
| claim3.tex | 38 | `p≈0.032` | `p≈0.039` |
| abstract.tex | 7 | `p≈0.032` | `p≈0.039` |
| introduction.tex | 20 | `p≈0.032` | `p≈0.039` |
| discussion.tex | 12 | `p≈0.032` | `p≈0.039` |
| appendix.tex | 170 | `σ 1.94%`, `z=1.85`, `p≈0.032` | `σ 2.04% (Bessel-corrected)`, `z=1.76`, `p≈0.039 (approximate z-test)` |
| appendix.tex | 170 | `0.9σ` | `0.8σ` (因 σ 变大，z for λ=0.01 从 0.86 降到 0.81) |
| appendix.tex | 183 | `±1.94%`, `z=1.85, p≈0.032` | `±2.04%`, `z=1.76, p≈0.039` |
| appendix.tex | 172 | *(新增)* | permutation test 段落 |

## Permutation test 结果

- 8 个值: {57, 52.5, 55, 57, 54, 52.5, 58, 58.5}
- C(8,2) = 28 种组合
- 均值 ≥ 58.25 的组合: 仅 {58, 58.5}（均值 = 58.25），共 1 种
- **exact permutation p = 1/28 ≈ 0.036**
- 与 approximate z-test p ≈ 0.039 一致

## 验证

全文搜索确认 `docs/paper/` 下所有 .tex 文件中：旧值 (0.032, z=1.85, σ=1.94) 零匹配；新值 (0.039, z=1.76, σ=2.04) 全部到位，共 8 处。

---
