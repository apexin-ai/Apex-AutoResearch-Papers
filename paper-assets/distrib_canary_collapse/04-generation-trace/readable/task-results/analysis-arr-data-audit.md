# analysis arr data audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_arr_data_audit_20260524T042855_result.json`
- **Structured JSON:** [`517d0d4472cdd928d686.json`](../../sessions/51/517d0d4472cdd928d686.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。112 个数字已检查，结果保存至 `artifacts/_project/arr_final_audit_20260524.md`。

**关键发现：**

**❌ 2 个错误（必须修复）：**
1. **conclusion.tex "13 of 15" vs discussion.tex "Five of fifteen do not confirm"** — 13/15 confirm 与 10/15 confirm 直接矛盾。conclusion 的 13/15（仅计 PermG ≥6/8）和 experiments 的 11/15（cascade+PermG 组合标准）各自合理，但 discussion 的 "Five" 与两者都不一致。
2. **"Five" vs "four" non-confirming** — experiments.tex 列举了 4 个 failure modes，discussion 说 5 个，第 5 个无法追溯。

**⚠️ 15 个需人工确认（非错误但无法端到端追溯）：**
- introduction "3/5 saturated predictions" 无 artifact 来源
- Fisher 18/32 的 α-level/seed 组成未完全记录
- discussion "s43 reverse 6/6 at α≥0.60" 仅 T=10 成立，缺 T 限定
- Table 1 非 PermG 行的处理管线不在 artifacts 中

**✅ 核心数字全部一致：** α_c=0.483、MAE=0.037、15/15 CI、14/15 cascade、64% intervention、Fisher p=3.45e-11、Table 17 全部 16 格。

---
