# paper multi seed caption fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_multi-seed-caption-fix_20260524T123924_result.json`
- **Structured JSON:** [`44eaab536f90439b9e3c.json`](../../sessions/44/44eaab536f90439b9e3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 edits done. Here's the summary:

---

**修改 1 — Caption (L1407)**
- 旧：`three of four ProofWriter conditions show consistently negative Δ (...), while Qwen3-14B is the sole positive condition (+0.92 pp)`
- 新：明确列出三个负 Δ 模型（Mistral-7B, LLaMA-8B, Qwen2.5-14B），Qwen3-14B 描述为 "negligible mixed-sign Δ (+0.92 ± 1.14 pp, all n.s.)"，加 `§\ref{sec:discussion}` 引用（label 确认正确：`\label{sec:discussion}` 在 discussion.tex:2）

**修改 2 — 分析段落 (L1466)**
- 消除原有 "Qwen3-14B is the only condition" 与新增句的重复
- 插入："Qwen3-14B is the sole exception: its 4-seed mean Δ is slightly positive (+0.92 ± 1.14 pp, all n.s.), reflecting the capability-modulated pattern discussed in §discussion—models with SC baselines above 85% leave few correctable errors for SICA to exploit."

**修改 3 — 数据核实**

| 位置 | Qwen2.5-14B FOLIO SC | 状态 |
|------|---------------------|------|
| tab:multi-seed seed42 (appendix L1422) | **77.50** | ✓ 正确 |
| tab:multi-seed 4-seed mean (appendix L1427) | 75.01 | ✓ 正确 (= mean of 77.50, 74.51, 74.02, 74.02) |
| tab:main_results 4s aggregate (experiments L32) | 75.01 | ✓ 与 multi-seed 一致 |

**75.98 出现位置（Qwen2.5-14B 相关）：**

| 文件 | 行 | 表格/上下文 |
|------|-----|-----------|
| diagnosis.tex | 30 | 主诊断表 Type A |
| diagnosis.tex | 41 | Oracle upper bound |
| diagnosis.tex | 70 | tab:independence |
| diagnosis.tex | 158 | SC baseline 表 |
| appendix.tex | 442 | tab:remediation caption |
| appendix.tex | 643, 713-714, 737, 768 | 多个附录表 |
| appendix.tex | 1084, 1112, 1140 | K-sensitivity 表 |

75.98 同时被 Qwen2.5-**7B** (experiments.tex:33) 和 Qwen2.5-**14B** 使用。按 registry 信息（exp-041 SC=77.45%, 75.98 来自 exp-061 即 7B），Qwen2.5-14B 处的 75.98 可能有误，但涉及 ~15 处表格/图/caption，按"不要修改其他表格"约束未动。如需全面修正，建议单独处理。

**附带发现：** 分析段落中 Qwen2.5-14B ProofWriter `Δ=−1.63` 与 multi-seed 表中 mean `−1.71` 不一致（可能来自不同计算方式），未修改。

---
