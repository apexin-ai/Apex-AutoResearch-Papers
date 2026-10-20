# paper method section

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_method-section_20260515T221813_result.json`
- **Structured JSON:** [`3fbd7997d467c47425d5.json`](../../sessions/3f/3fbd7997d467c47425d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section 已提交，14/14 claims 全部有 provenance 追踪。

输出文件：
- LaTeX: `docs/paper/method.tex`
- Provenance: `paper_provenance.yaml` (v1)

结构：4 小节 (~2.5 页)
- **3.1 Problem Setup**: 加权公式 w=(1-q)^b，与 Drayson 共享；差异化：adaptive per-batch vs validation grid search
- **3.2 Dual-Constraint Framework**: α_eff + ESS 定义，Proposition 1 (单调性 + 证明骨架 via covariance)，b_τ/b_ESS 约束，b* 三 regime 定义，40.1% α_eff binding 实证 (b*=1.67 vs ESS-only 4.15)
- **3.3 Algorithm**: Algorithm 1 伪代码 (bisection)，loss reweighting vs SIR 对比，O(B log(b_max/ε)) 复杂度分析
- **3.4 Hyperparameters**: τ sweep 6 点 ([0.5,0.8] safe range, 0.8 default)，n_min 分析 (n_min=1 退化确认，n_min≥B 退化为 uniform)

所有定量数字均标注 exp_id，无 "significantly"/"consistently" 等未支撑强度词。

---
