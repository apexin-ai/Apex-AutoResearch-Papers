# audit sign test d061

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_sign-test-d061_20260522T203355_result.json`
- **Structured JSON:** [`9729bfe353f58d9b2107.json`](../../sessions/97/9729bfe353f58d9b2107.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整结果：

---

## 产出 1: 完整条件列表（当前 Table 1, D061 已校正）

| # | Model | Domain | n | SC (%) | SICA (%) | Δ (pp) | Sign |
|---|-------|--------|---|--------|----------|--------|------|
| 1 | Mistral-7B | PW-D5 | 600 | 39.33 | 36.50 | −2.83 | − |
| 2 | Mistral-7B | LogiQA | 200 | 50.00 | 51.50 | +1.50 | + |
| 3 | Mistral-7B | FOLIO (s123) | 204 | 54.41 | 57.35 | +2.94 | + |
| 4 | Mistral-7B³ˢ | FOLIO | 204 | 56.53 | 56.70 | +0.16 | + |
| 5 | Mistral-7B | FOLIO (s456) | 204 | 55.88 | 55.88 | 0.00 | **tie** |
| 6 | Mistral-7B | FOLIO (s789) | 204 | 59.31 | 56.86 | −2.45 | − |
| 7 | LLaMA-3.1-8B | FOLIO | 204 | 66.18 | 61.76 | −4.41 | − |
| 8 | LLaMA-3.1-8B | StrategyQA | 200 | 72.00 | 74.00 | +2.00 | + |
| 9 | Qwen2.5-14B | FOLIO ICL | 199 | 74.37 | 74.87 | +0.50 | + |
| 10 | Qwen2.5-14B | PW-D5 | 600 | 74.00 | 71.50 | −2.50 | − |
| 11 | Qwen2.5-14B⁴ˢ | FOLIO | 204 | 75.49 | 74.51 | −0.98 | − |
| 12 | Qwen2.5-7B | FOLIO | 204 | 75.98 | 76.47 | +0.49 | + |
| 13 | Qwen2.5-14B | LogiQA | 200 | 79.00 | 78.00 | −1.00 | − |
| 14 | Qwen3-14B | FOLIO | 204 | 84.80 | 84.31 | −0.49 | − |
| 15 | Qwen3-14B | PW-D5 | 600 | 85.83 | 85.67 | −0.17 | − |
| 16 | Qwen3-14B (think) | FOLIO | 204 | 86.27 | 86.76 | +0.49 | + |

## 产出 2: Sign test 结果

| 指标 | 论文当前值 | 正确值 |
|------|-----------|--------|
| n+ | 5 | **7** |
| n− | 10 | **8** |
| n0 (tie) | 0 | **1** (s456, Δ=0.00) |
| n (non-tie) | 15 | **15** |
| p-value | 0.30 | **1.00** |

## 产出 3: "sixteen" 是否仍正确

**是。** 当前 Table 1 有 16 个非退化条件，"sixteen non-degenerate conditions" 正确。但 `diagnosis.tex`（未被 main.tex 引用）写的是 "fifteen"，是旧版文件。

## 产出 4: 差异溯源

sign test 从 5+/10− 变为 7+/8− 有两个原因：

**原因 A — D061 tiebreaking 导致 2 个 sign 变化（对老条件集）：**
- Qwen3-14B PW: Δ +0.67 → −0.17 （**+ 翻转为 −**，SC 从 85.00 升至 85.83）
- Mistral s456: Δ −0.49 → 0.00 （**− 翻转为 tie**，SC 从 56.37 降至 55.88）

如果仅 D061 修正（不改条件集）：5+ → 4+, 10− → 10−, +1 tie → 4+/10−/1tie (n=14), p=0.18

**原因 B — 条件集本身大幅变更（更大的影响）：**

移除的条件（全 −，共 5 个 −）：gpt-4o FOLIO, LLaMA PW-600, LLaMA LogiQA×2, Mistral ICL-oracle

移除的条件（1 个 +）：Qwen3 FOLIO-154

新增的条件：Mistral 3s-aggregate (+), s789 (−), StrategyQA (+), Qwen2.5-7B (+), Qwen3 FOLIO (−), Qwen3 thinking (+), ICL (+)

净效果：移除了 5 个 − 和 1 个 +，新增了 4 个 + 和 2 个 −，分布从 negative-skewed 变为几乎对称。

**结论的方向性不变但强度变了：** p 从 0.30（弱 negative 趋势）变为 1.00（完美 null）。"no significant directional bias" 的结论被**加强**而非削弱。但 abstract 和 experiments.tex 的具体数值 "5+/10−, p = 0.30" 需要更新为 **7+/8−, p = 1.00**。

---
