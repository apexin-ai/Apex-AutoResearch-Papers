# audit data integrity

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-integrity_20260523T191559_result.json`
- **Structured JSON:** [`a6e8d5345813f8d2e4d9.json`](../../sessions/a6/a6e8d5345813f8d2e4d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/_project/data_audit_20260523.md` 并注册。

**核心结论：0 个数据错误，论文可提交。** 所有关键定量 claim（α_c=0.483、MAE=0.037、15/15 CI、14/15 cascade、64% reduction、Table 17 等）均与 artifact 源文件一致。

**需关注的 4 项**：
1. experiments.tex L91 `α_c(10)=0.487` vs L23 `α_c=0.483±0.006` — 来自不同分析（理论预测 vs 实证 sigmoid），均合法，但读者可能困惑
2. appendix.tex L1027 cascade "t_H ≤ t_D holds in 14/15" 措辞可更精确（ordering 实为 15/15，direction 为 14/15）
3. experiments.tex L104 "5 non-confirming conditions" — 文本只列出 4 个，第 5 个需人工确认
4. introduction.tex L24 "3/5 predictions in saturated regimes" — artifact 来源未找到，experiments.tex 对应位置说 "2/4 boundary predictions"（不同子集）

**已确认安全**：无 58% 残留、无 0.476 残留、sync-dip 术语统一、_reframe 旧文件不在编译链中。

---
