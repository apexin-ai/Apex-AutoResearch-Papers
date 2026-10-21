# analysis cross alpha fdr contradiction fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_alpha_fdr_contradiction_fix_20260515T111824_result.json`
- **Structured JSON:** [`2e7ce3e9b1fadb485870.json`](../../sessions/2e/2e7ce3e9b1fadb485870.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成。

## 总结

### P0 调查结论
**v4 正确（1 robust pair），d027 错误（0）。** token_entropy→distinct_1 在 α=0.25 有 4/5 methods pass（naive, diff_xcorr, threshold, TY; permG FDR-fail）。d027 初稿手动总结时误判"所有严格方法归零"。

### 修改清单

**d027_report.md** — Cross-Alpha Consensus Extension section:
- α=0.25 robust pair 数从 0 改为 1
- 添加修正注释说明错误原因
- 标注 C001 caveat：该 pair 依赖 TY（去掉 TY 则 3/5 不达标）
- 叙事从"binary threshold"改为"near-binary threshold with caveat"
- 新增 Granger Raw vs FDR 小节（10/32→1/32）

**cross_alpha_fdr_4point.md**:
- 添加 Claim 3 素材（Granger FDR fragility vs consensus robustness）
- **修正 §4 三个表的 permG/TY 列数据互换 bug**（原始报告中 v4 内部方法顺序 [TY,permG] 与表头 [permG,TY] 不一致）
- 修正 §7 items 2-3：permG 受 FDR 影响最大（非 TY），TY 影响中等
- 添加 raw vs FDR 标注要求和 C001 caveat

### 额外发现
在修正 P0 时发现 §4 sig rates 表的 permG/TY 列长期互换，影响了 §7 叙事中对两种方法 FDR 敏感度的描述。已一并修正。

---
