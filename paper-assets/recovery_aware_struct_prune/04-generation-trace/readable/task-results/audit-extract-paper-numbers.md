# audit extract paper numbers

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_extract-paper-numbers_20260525T194435_result.json`
- **Structured JSON:** [`6ea15626dd681dd09e77.json`](../../sessions/6e/6ea15626dd681dd09e77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/audit_paper_numbers.md` 并注册（art_20260525_7984c8）。

## 关键发现

**HIGH（必须修复）**
1. **gen_fig1_dose_response.py 与 Table 3 数据不一致**：α=0.5 (64.52/65.05 vs 60.73/61.18，差约4 pp)、α=3.0 (64.06/64.59 vs 64.14/63.46，GRPO 差 1.13 pp)、α=4.0 SFT 微差。caption "|Δ|≤1.14 pp" 在两份数据上都恰好成立（因 α=2.0），所以读者表面看不出矛盾，但底层数据源不统一。

**MEDIUM**
2. **"20% MLP channel sparsity" 术语不准确**：200/784 = 25.5% MLP groups, 1.46B/7.62B = 19.2% total params, 无一为 20%。
3. **App:122 "α SFT 范围 ~8 pp"** vs 实际 27.8-21.6 = 6.2 pp。

**LOW**
4. tab_math500 caption 用 "4.62 pp"，正文用 "4.6 pp"（同一数字两种舍入）。
5. App:374 "$\varepsilon$=2 pp 约为 4× cross-seed σ" 推导不清（2/0.19=10.5×）。
6. App:308 RASP KL "<0.001" 实际有点超 0.001（max=0.001119）。
7. App:109 "rises from 0.354 to 0.308" 方向矛盾（实为下降）。
8. App:210 Standard 范围上界 60.20% vs TOST 反推 60.28%（差 0.08）。

**Orphan / 文件管理**
- `gen_fig2_reward_accuracy.py` 是 orphan，含与现行数据不一致的硬编码值。
- `gen_fig1_framework.py` 输出 `fig1_framework.pdf` 而论文引用 `fig1_method_framework.pdf`；脚本含 "+2.2pp advantage" 等论文文本不再使用的文案。

**整体保真度**: 验证 39 项派生计算，36 项正确（含 mean |Δ|=0.54 准确为 0.5425，4.4× 准确为 4.37，5.5× 准确为 5.50 等所有 headline 数字）。绝大多数表格-正文-脚本数据高度一致。

---
