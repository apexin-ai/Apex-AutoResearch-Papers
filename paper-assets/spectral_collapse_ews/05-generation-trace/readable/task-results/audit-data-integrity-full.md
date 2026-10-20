# audit data integrity full

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-integrity-full_20260523T102939_result.json`
- **Structured JSON:** [`9a35fbefeaa51b22c961.json`](../../sessions/9a/9a35fbefeaa51b22c961.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/_project/report/data_audit_report.md`。

**结论：无实质性数据错误。** 所有数值均可追溯到服务器原始实验输出。

发现的问题：

| 类别 | 数量 | 严重程度 |
|------|------|----------|
| Table 1 (30 cells) | 0 | — |
| Table 2 (8 indicators) | 0 (caption 措辞不精确) | 📝 |
| Table 3 (20 cells) | 3 个末位小数舍入差异 | ⚠️ 极微 |
| Figure 1 (55 values) | 0 | — |
| Figure 2 (~100 values) | 0 | — |
| 正文引用数字 (~30 claims) | 1 处内部不一致 | ⚠️ 修辞 |

具体问题：
1. **Table 3 三处舍入**：r=0.3 PPL (13.35 vs 13.34)、r=0.5 SLV (2571.7 vs 2571.6)、r=0.5 PPL (15.12 vs 15.11)，均在末位 ±0.1 内
2. **§3.5 文本不一致**：同一个量（r=0 Gen0→1 SLV 变化）在两段分别写成 "+97" 和 "+98"，三种子均值为 +96
3. **Table 2 caption**：Rel Δ 公式写的是 |v₁₀−v₀|/|v₀|（Gen0→10），但 SLV 和 RankMe 实际用的是 peak→Gen10 计算（11.8% vs Gen0→10 的 7.9%）

---
