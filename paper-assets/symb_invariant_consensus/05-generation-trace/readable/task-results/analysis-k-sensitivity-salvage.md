# analysis k sensitivity salvage

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k-sensitivity-salvage_20260517T025706_result.json`
- **Structured JSON:** [`4252e5b30273cebffb36.json`](../../sessions/42/4252e5b30273cebffb36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存。以下是汇总结果：

## K-Sensitivity 实验结果 (sica_k_sensitivity_14b)

**状态**: 实验完整完成。日志末尾有 `K_ABLATION_DONE` 标记，SIGHUP 在完成后才到达。

**结果文件**: `/root/symb_invariant_consensus/results/k_ablation/k{6,8,11,12,16,20}_results.json`（全部 6 个文件完整）

### 汇总表

| K | SICA acc | SC acc | Gap (pp) | Unique constraints | Wall time |
|---|---------|--------|----------|-------------------|-----------|
| 6 | 73.3% | 73.3% | **0.0** | 1127 | 35 min |
| 8 | 73.3% | 75.0% | **-1.7** | 1193 | 42 min |
| 11 | 73.3% | 73.3% | **0.0** | 1312 | 57 min |
| 12 | 70.0% | 75.0% | **-5.0** | 1319 | 59 min |
| 16 | 71.7% | 75.0% | **-3.3** | 1353 | 77 min |
| 20 | 70.0% | 73.3% | **-3.3** | 1415 | 97 min |

### 结论

**Negative result，与 D029 记录一致。** SICA 在所有 K 值下均 <= SC，gap 在 0 到 -5pp 之间。

关键发现：
1. **SICA 不随 K 增大而提升**，反而略微下降（73.3% → 70.0%）
2. **约束饱和**：unique constraints 从 1127 增长到 1415（仅 +25%），尽管 total constraints 增长了 3.5x。更多 traces 产出的主要是冗余约束
3. **成本线性增长**：wall time 从 35min 到 97min，但准确率没有回报
4. **Conclusion**: 增加 K 不能帮助 SICA 超越 SC。假设"更多推理路径 → 更丰富约束集 → MaxSAT 聚合更强"被证伪

---
