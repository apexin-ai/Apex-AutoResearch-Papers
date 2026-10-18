# audit appendix

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_appendix_20260525T194500_result.json`
- **Structured JSON:** [`28a221c2dc817d82aa8a.json`](../../sessions/28/28a221c2dc817d82aa8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/audit_appendix.md` 并注册。

**核心发现**：~220 个数值中 ~180 个与 registry 匹配，发现 7 处不一致：

**需优先处理（2 项）**：
- **Pythia seed42 baseline**：论文 78.70% vs registry 78.2%，导致 Δ 从 +0.14pp 变为 +0.64pp
- **Min-K% d1-d3 BalAcc**：论文 40.4% vs registry 37.24%，差 3.16pp

**需确认（3 项）**：
- GPT-2 XL seed42 CI 边界偏移 0.11pp
- RF d2 recall 附录内部矛盾（.596 vs 59.2%）
- Pythia self-ref 四舍五入偏差（78.6% vs 78.54%）

**非错误但需注意（1 项）**：
- Curation PoC 表 dz vs d 系统性差异——论文正确标注 dz，registry 存的是 d，两者是不同指标

---
