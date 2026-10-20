# paper consistency audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_consistency_audit_20260516T002041_result.json`
- **Structured JSON:** [`29455c46afb19d142cc9.json`](../../sessions/29/29455c46afb19d142cc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/paper_consistency_audit.md`。

**关键发现：**

**❌ 1 个严重问题** — Table 1 (tab:drift_summary) 的 α=1.0 行，4-seed mean±std 与 registry 数据不一致：
- ECE drift: 论文写 +3862±158，实际 +3780±30（mean 偏 82，std 偏 5 倍）
- Distinct-1: 论文 −25.3，实际 −27.8（偏 2.5 个百分点）
- Distinct-2: 论文 −29.7，实际 −34.0（偏 4.3 个百分点）
- Perplexity std: 论文 ±320，实际 ±45（偏 7 倍）
- 其余 4 行（单 seed）全部精确匹配，问题仅出在聚合计算

**⚠️ 2 个中等问题** — Discussion 称 GPT-2m 结果 "not yet available"，但 registry 已有完整结果（Tier 3 consensus 复现）；α=0.25/0.50 已有部分 multi-seed 数据可纳入

**✅ 40+ 个数字验证通过** — 所有方法消融率、κ 值、Granger p 值、sig 计数、FPR/FNR、实验参数均与 registry 一致

---
