# fix sync diagnosis kappa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sync-diagnosis-kappa_20260524T072901_result.json`
- **Structured JSON:** [`56afa633b23d809e4306.json`](../../sessions/56/56afa633b23d809e4306.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No duplicate label warnings. All changes compiled cleanly.

---

**修改汇总**

#### 1. tab:independence 表格（L66-81）
- Qwen3 FOLIO: κ 0.77→**0.79**, K_eff 1.26→**1.24**
- Qwen2.5-14B FOLIO: K_eff 1.30→**1.31**（κ 0.74 不变）
- Mistral-7B FOLIO: κ 0.50→**0.46**, K_eff 1.84→**1.98**
- Mistral-7B (s123): κ 0.49→**0.46**, K_eff 1.88→**1.99**
- Mistral-7B (s456): κ 0.51→**0.46**, K_eff 1.82→**1.99**
- Mistral-7B (s789): κ 0.41→**0.45**, K_eff 2.17→**2.03**
- Mistral-7B (multi-T): κ 0.48→**0.43**, K_eff 1.91→**2.11**
- Mistral-7B PW-D5: κ 0.21→**0.19**, K_eff 3.62→**3.94**
- 行序重排：T=0.5 移至 T=0.3 之后、LogiQA 之前；T=1.0 移至 LogiQA 之后；s456 移至 s123 之后（与 appendix.tex 一致）

#### 2. L51 prose
`0.21 to 0.82` → **`0.19 to 0.82`**, `3.62` → **`3.94`**

#### 3. L95 prose
`$\kappa = 0.41$` → **`$\kappa = 0.46$`**

#### 4. Cross-model kappa table 分析结论
**不需要修改。** `kappa_generalization` 表 (diagnosis.tex L152) 明确显示 Mistral-7B SC 行使用 **K=10**（不是 K=12），因此 κ=0.44, K_eff=2.02, SC=56.86 是该 K 值下的正确数据。appendix.tex cross-model table (L739) 的值与此一致，均为 K=10 数据。L726 prose "Mistral-7B ($\kappa = 0.44$)" 和 L138 prose "SC ($\kappa = 0.44$)" 引用的也是 K=10 值，无需修改。

> 注：Qwen2.5-14B FOLIO 的 K_eff 在 tab:independence (1.31) 与 cross-model/kappa_generalization (1.32) 之间有 0.01 的差异，属于 K=12 下的计算舍入差，不影响结论。

---
