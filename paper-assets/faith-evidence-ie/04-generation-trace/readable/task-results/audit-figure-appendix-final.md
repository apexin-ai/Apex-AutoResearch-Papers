# audit figure appendix final

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_figure-appendix-final_20260523T191633_result.json`
- **Structured JSON:** [`abd2c88639843db6f2aa.json`](../../sessions/ab/abd2c88639843db6f2aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心结论：

**14项验证通过** — fig_evidence_tax 全部5组 tax/error/n_seeds、fig_spectrum 全部6个数据点、Cohen's d 4个值、95% CI 8个区间、ablation 均值、RSFT Gain、LLaMA per-seed、error analysis 百分比等全部与源表一致。

**2处不一致需修复：**

1. **1.7B 方差压缩倍数**：experiments.tex 写 "31×"，appendix tab:variance_ci 写 "32.6×"。原因是主文用 rounded std (2.79/0.09=31) 计算，appendix 用 unrounded std 计算。建议统一为 appendix 的 32.6× 或改主文为 "~33×"。

2. **4-seed Ign-F1 std**：appendix 文字写 0.49，但从表中显示的 per-seed 值 (44.23, 45.12, 45.11, 44.16) 计算得 sample std=0.53 / population std=0.46，均不等于 0.49。可能是 per-seed 值在表中被四舍五入导致。严重性低，该值未被其他地方引用。

**1处待确认：**
- **Evi-F1 -7.7pp**（sentence-level CED filtering）在 analysis.tex 和 limitations.tex 中一致引用，但无对应的 appendix 表格提供原始数据。若 reviewer 追问来源，需补充或指向具体实验。

---
