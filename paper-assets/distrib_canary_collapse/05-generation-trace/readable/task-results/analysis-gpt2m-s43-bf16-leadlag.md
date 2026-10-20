# analysis gpt2m s43 bf16 leadlag

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603_result.json`
- **Structured JSON:** [`3a8eb4e7df7cc99960a5.json`](../../sessions/3a/3a8eb4e7df7cc99960a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

## Table 7 Row: GPT-2-medium / Wiki (s43, bf16)

| | Naive | Diff. XCorr | Threshold | PermG (fwd) | PermG (rev) | TY | K≥4/5 | MMCT |
|---|---|---|---|---|---|---|---|---|
| **s43 bf16** | 8/8 | 7/8 | 8/8 | 1/8 | 0/8 | 0/8 | 1/8 | **6/8** |
| s42 fp32 | 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 5/8 | 6/8 | 8/8 |

**关键发现：**

1. **K≥4 共识从 6/8 暴跌到 1/8**（唯一通过的是 ece→perplexity，属于 spurious channel）
2. **MMCT 恢复到 6/8**，因为 FPR-inverse weighting 给予 naive+diff+thresh 三法共识足够权重
3. **根因是 fp32 vs bf16 混淆因子**：s42(fp32) entropy drift=-86.6%, s43(bf16) entropy drift=-16.6%。bf16 将 collapse 严重程度降低约 5 倍，PG/TY 在弱信号下失去检验力
4. 非 parametric 方法（naive, threshold）对信号强度不敏感，8/8 保持稳定
5. **不建议直接纳入 Table 7 作为 cross-seed 行**，因为 fp32/bf16 是实验条件差异而非 seed variance

数据已写入 registry（metrics 字段）并注册为 artifact。5method_leadlag.json 保存在 westd-17855 上。

---
