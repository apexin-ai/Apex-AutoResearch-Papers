# analysis transfer entropy

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_transfer_entropy_20260518T140339_result.json`
- **Structured JSON:** [`af1cc23db3975ed8b415.json`](../../sessions/af/af1cc23db3975ed8b415.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析全部完成。结果总结：

## 结果

**12 个 run × 8 pairs × 双向 = 192 个 TE 测试，BH FDR 校正后 0 个显著。**

关键发现：

| 现象 | 解读 |
|------|------|
| 所有 TE p-values > 0.05（多数 > 0.5） | T=11 下 binning TE 根本没有足够的统计功效 |
| ECE 在 a100_s42 上 TE=0.0 | 单调序列 → 分 bin 后转移完全确定性，无法检测额外信息流 |
| token_entropy pairs 方向性反转（reverse > forward） | 估计噪声主导，无法可靠判断因果方向 |
| 与 Permutation Granger 一致率 46/88 = 52.3% | 接近随机水平，TE 和 Granger 在此处结论无关联 |

**这本身是有价值的方法敏感性证据**：非参数 TE 在 T=11 的极短时间序列上不具备检测因果方向的能力，支持了项目选择参数化 Granger 方法的合理性。

### 产出文件

`/root/autodl-tmp/distrib_canary_collapse/artifacts/transfer_entropy_analysis/`:
- 12 个 `te_results_*.json`（每个 run 的详细结果）
- `te_summary.json`（跨 run 汇总）
- `te_vs_granger_comparison.md`（与 Permutation Granger 对比表）

---
