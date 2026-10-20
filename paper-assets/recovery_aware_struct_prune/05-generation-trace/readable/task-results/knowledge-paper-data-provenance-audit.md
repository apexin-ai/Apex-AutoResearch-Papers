# knowledge paper data provenance audit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_paper_data_provenance_audit_20260523T104659_result.json`
- **Structured JSON:** [`81b09b7e100c76de535e.json`](../../sessions/81/81b09b7e100c76de535e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

溯源表已写入 `artifacts/data_provenance_audit.md` 并注册。

**覆盖范围**: 9 个表格文件 + experiments.tex/appendix.tex/abstract.tex/introduction.tex 中的内联数值 + 5 个 Figure 的数据来源。

**关键发现**:

1. **4 个论文数值无 registry 记录**:
   - MATH-500 Standard 25% GRPO = 12.8%
   - Qwen2.5-Math-7B CKA-only Post-Prune = 1.0% 和 Post-SFT = 51.50%
   - Qwen2.5-Math-7B Standard Post-Prune = 18.5%

2. **4 个微小数值差异** (均为四舍五入，≤0.01pp):
   - CKA seed456: 64.59% vs 64.58%
   - α=3.0 GRPO: 63.45% vs 63.46%
   - Extended training 两个 reward 值

3. **3 个 registry 记录 metrics 为空** (Random seed123、depth-first SFT/GRPO)

4. **30% cliff CKA-only**: paper=0% (N=100) vs registry=1.6% (N=500)，评估样本量不同

---
