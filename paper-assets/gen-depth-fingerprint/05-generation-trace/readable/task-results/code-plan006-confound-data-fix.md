# code plan006 confound data fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-confound-data-fix_20260516T021050_result.json`
- **Structured JSON:** [`d6eebaa2640578399696.json`](../../sessions/d6/d6eebaa2640578399696.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。**新旧对比**：

| 指标 | 旧（污染，9666条） | 新（clean rp=1.0，4912条） | 变化 |
|------|------|------|------|
| n_records | 9666 | **4912** | 去掉 4754 条 rp=1.3 污染 |
| 3-class F1 | 0.680 | **0.742** | **+0.062 ↑** |
| Binary F1 | 0.539 | **0.671** | **+0.132 ↑** |
| entropy_mean rho | **+0.394** | **−0.533** | **方向反转！** |
| Depth retention (d4/d0) | — | 0.970 | — |

**关键发现**：

1. **entropy_mean Spearman rho 从 +0.394 翻转为 −0.533**。这证实了 feature reversal 完全是 rp=1.3 confound 导致的 artifact。去掉污染后，paraphrase 的 entropy 方向与 continuation (rho=−0.675) 一致——都是负相关（深度越深，entropy 越低），符合理论预期。

2. **分类性能大幅提升**：3-class F1 从 0.68 → 0.742，binary F1 从 0.539 → 0.671。rp=1.3 数据引入的 confound 不仅搞乱了特征方向，还严重拖累了分类器。

3. **Paraphrase vs Continuation 对比**：
   - 3-class F1：para 0.742 vs cont 0.788（差距 −0.045，比之前 −0.11 缩小很多）
   - Cross-transfer：para→cont 0.770, cont→para 0.743（跨域泛化良好）
   - 结论仍为 "similar"——paraphrastic chains 保留了与 continuation 相当的 depth signal

污染文件已移至 `/root/gen-depth-fingerprint/data/pythia-2.8b-paraphrase_backup/`，新结果保存在 `/root/gen-depth-fingerprint/results/plan006_paraphrastic_comparison.json`。

---
