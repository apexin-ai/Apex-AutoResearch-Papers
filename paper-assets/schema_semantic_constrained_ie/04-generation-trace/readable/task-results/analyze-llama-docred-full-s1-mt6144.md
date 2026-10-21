# analyze llama docred full s1 mt6144

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_llama_docred_full_s1_mt6144_20260515T150034_result.json`
- **Structured JSON:** [`3fd84fefc9c062ef7927.json`](../../sessions/3f/3fd84fefc9c062ef7927.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 关键发现

**vs unconstrained_mt6144 基线**（核心结论）：
- DR: 26.18% → **2.57%**，相对下降 **−90.2%**（与 mt4096 的 −90.2% 完全一致）
- RV / ET: 全部清零
- R-F1: 5.95 → **6.25%**，**+0.30pp**（mt4096 是 +0.29pp，几乎相同）
- E-F1: 55.67 → 55.04%，−0.63pp

**vs full_s1 (mt4096)**（mt6144 vs mt4096 增量）：
- DR Δ +0.02pp，R-F1 Δ −0.02pp，E-F1 Δ +0.03pp，parse-fail 91→90 — **全部在噪声范围内**
- mt6144 并未带来任何可测量的改进；90 个 parse failure 都是 ~102s 单样本超时（非 token 预算瓶颈）

**Fallback 统计**：grammar-first fallback 触发 67911 次（约每 emitted triple 4 次），说明 grammar∩semantic 经常为空、fallback 路径被大量使用。

**CF 注意**：此实验混淆了 CF fallback 代码 + mt6144 两个变量；CF 12.13% (vs mt4096 12.02%) 看起来 fallback 代码并未压低 CF，但不能在此独立归因，需要 mt4096+fallback 的对照。

## 产出
- `artifacts/llama_docred_full_s1_mt6144/report/analysis.md` 已写入并注册（art_20260515_702ab3）
- Registry: status → **DONE**, conclusion → **success**, metrics 完整登记

## 对论文的影响
论文继续以 mt4096 结果为主，mt6144 在附录里作为 max-tokens 鲁棒性检查；不需要重算 bootstrap CI（Δ ≤ 0.03pp）。

---
