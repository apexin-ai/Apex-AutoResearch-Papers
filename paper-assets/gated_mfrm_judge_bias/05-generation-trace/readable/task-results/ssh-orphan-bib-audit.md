# ssh orphan bib audit

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_orphan_bib_audit_20260524T073745_result.json`
- **Structured JSON:** [`7899c32d1389f7224796.json`](../../sessions/78/7899c32d1389f7224796.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 entry 全部已被引用，审计完成。

---

**Entry 1: `sanmartin2016`**
- **Bib 内容**: San Martín (2016), "Identification of Item Response Theory Models", Handbook of IRT Vol.2, CRC Press
- **引用状态**: 已引用 at appendix.tex:57 (`\citet[Chapter~5]{sanmartin2016}`)
- **method.tex identifiability 讨论**: method.tex §3.3 (lines 53-82) 大量讨论 identifiability，但呈现的是本文自己的 Propositions/Theorem，proof 推迟到 Appendix。Appendix 证明中引用 San Martín 的已有 MFRM identifiability 结果，引用位置正确。method.tex 无需重复引用。
- **决定**: 保留（已引用，位置正确）
- **执行结果**: 无需修改

**Entry 2: `talts2018sbc`**
- **Bib 内容**: Talts et al. (2018), "Validating Bayesian Inference Algorithms with Simulation-Based Calibration", arXiv:1804.06788
- **引用状态**: 已引用 at limitations.tex:3 (`\citealp{talts2018sbc}`)
- **上下文**: 讨论 CI coverage 的 posterior overconfidence 时引用 SBC，提出 SBC-based recalibration 作为未来方向
- **决定**: 保留（已引用，位置正确）
- **执行结果**: 无需修改

**Entry 3: `vehtari2017loo`**
- **Bib 内容**: Vehtari, Gelman & Gabry (2017), "Practical Bayesian Model Evaluation Using LOO-CV and WAIC", Statistics and Computing 27(5)
- **引用状态**: 已引用 at experiments.tex:48 (`\citealp{vehtari2017loo}`)
- **上下文**: 报告 LOO cross-validation 结果（ΔELPD = -55.7, SE = 9.4）时引用
- **决定**: 保留（已引用，位置正确）
- **执行结果**: 无需修改

**结论**: 3 个 entry 均非 orphan，全部在论文中被正确引用。无需修改，无需编译验证。

---
