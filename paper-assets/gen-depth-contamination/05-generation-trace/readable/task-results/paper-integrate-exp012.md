# paper integrate exp012

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_integrate_exp012_20260516T001041_result.json`
- **Structured JSON:** [`161a36ef0f53255c4d45.json`](../../sessions/16/161a36ef0f53255c4d45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Consistent — no changes needed there. Introduction (line 11) and related_work are also already consistent.

---

修改摘要：

**experiments_c1.tex** (Section 5.6 Binary Detector Confidence and Depth):
- 修正 6-class accuracy 范围：`0.119→0.127`（匹配 registry: olmo=0.127）
- 添加 per-generator 6-class accuracy 明细：Qwen-rw 0.199, Qwen-cont 0.183, Pythia 0.130, OLMo 0.127
- 添加 per-generator Spearman ρ 分层描述：Pythia/OLMo ~0.45, Qwen-cont ≤0.39, Qwen-rw 0.08-0.12（sign reversed）
- 强化 Spearman nuance："driven almost entirely by the human–synthetic boundary...do not monotonically track generational depth"
- K* 标注改为 `$\Kempirical^{\text{binary}} \leq 1$` 与 OBD 的 `$\Kempirical = 2$` 明确对比
- 引用新增 appendix 表 `\ref{tab:s9_binary_spearman}`

**discussion.tex** (Section 5.3 Why Graduated Filtering Fails):
- 新增一句：binary K*≤1 从 binary detector 自身角度解释了为什么 graduated→binary 收敛——binary detector 只能感知 human/synthetic 边界，任何基于其 confidence 的 depth-graduated 策略本质上就是 binary filtering

**appendix.tex**:
- 新增 Table S9 (`tab:s9_binary_spearman`)：exp-012 完整 Spearman ρ per generator × per metric（log-PPL ref, log-PPL observer, PPL ratio）+ 6-class accuracy + K* 对比

**未修改的文件**（已验证一致性）：
- `introduction.tex` line 11 已正确引用 `\ref{sec:binary_confidence}`
- `related_work.tex` DivEye/Binoculars 论述与 exp-012 结果不矛盾
- `discussion.tex` lines 23-25 的现有 binary confidence 段落数字与 registry 一致

---
