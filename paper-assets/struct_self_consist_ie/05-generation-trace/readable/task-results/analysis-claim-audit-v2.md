# analysis claim audit v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_claim_audit_v2_20260519T064159_result.json`
- **Structured JSON:** [`e920e9868a076eed0f3e.json`](../../sessions/e9/e920e9868a076eed0f3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。47 条定量 claim，38 条验证通过。关键发现：

**HIGH（必须修）：**

| ID | 问题 | 位置 | 修复 |
|---|---|---|---|
| INC-01 | **"ρ up to 0.50" 无支撑** — 所有配置最大 ρ ≈ 0.48（LLaMA CoNLL N=16 SJ），N=8 主表最大 0.451 | abstract, intro×2, conclusion, fig_overview caption（共 5 处） | 改为 "ρ up to 0.48" 或 "ρ up to 0.45"（仅 N=8） |
| UPD-01 | **Few-NERD N=16 LP "+0.52pp" 无来源** — 引用 Appendix app:n_scaling，但该节只有 SciERC 数据；registry exp_027 显示 5K 子集 +1.88pp，与 0.52pp 不一致 | experiments.tex:143 | 补充 Few-NERD N=16 全测试集数据到附录，或更正数值 |

**MEDIUM：**

| ID | 问题 | 修复 |
|---|---|---|
| INC-04 | fig_selection_gap caption 说 "ρ up to 0.36"，但 SciERC VC ρ=.379 | 检查图是否包含 VC；如包含则改为 "up to 0.38" |
| INC-05 | Discussion T=1.2 用 mean ρ=0.225，但其他地方用 median（Table within_rho） | 统一为 median（0.315）或标注 "mean" |
| UPD-02 | Few-NERD N=16 construction "+1.32pp" 同样引用 app:n_scaling 但该节无此数据 | 补充数据到附录 |

**LOW：** oracle headroom 13.0 vs 13.1pp 取整不一致；SciERC greedy F1 枚举缺 .646；FK dependence range −0.4%~−4.0% 在附录中无对应数据。

报告已写入 `artifacts/claim_audit_v2.json`。

---
