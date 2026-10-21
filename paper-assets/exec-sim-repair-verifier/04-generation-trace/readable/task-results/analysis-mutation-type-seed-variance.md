# analysis mutation type seed variance

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mutation-type-seed-variance_20260515T122916_result.json`
- **Structured JSON:** [`4857f4ad1e9869e1be2e.json`](../../sessions/48/4857f4ad1e9869e1be2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Part 1 — 按 mutation type 拆解 (W3/W8)**

| 类型 | 8B s42 Acc | Test 占比 | Val 占比 | 难度排名 |
|------|-----------|-----------|---------|---------|
| gold | 94.09% | 47.4% | 45.2% | 最易 |
| return_value | 83.99% | 5.7% | 10.7% | |
| operator_swap | 82.72% | **34.3%** | 19.1% | |
| off_by_one | 71.04% | 1.9% | 10.0% | |
| boundary_removal | **41.47%** | 10.7% | 15.0% | 最难 |

- **operator_swap 从 19.1%→34.3% 并不是主要困难源**——模型处理得不错 (82.72%)
- **boundary_removal 最难** (41.47%，几乎随机)，错误模式是大量 FP (预测 pass 但实际 fail)
- **Test 分布比 val 更有利**：测试精度因分布偏移虚增 ~2-3pp
- **隐藏因素**：xarray (23.7% test, 0% val) 全部 label=pass，模型 100% 正确——这是平凡贡献

**Part 2 — 种子差异根因 (C1)**

- 4B s123 过拟合更快：val loss 从 step 200 的 0.08 急升到 step 800 的 0.15，step 1000 达 0.28
- Val-best (ckpt-800) 选在过拟合拐点
- 8B 代理分析显示：不同 seed 在 return_value 上差距最大 (17.62pp)，而非 operator_swap
- 4B val-best 的逐类型预测文件在离线 home 服务器上，无法完成最终确认

报告已注册为 artifact：`mutation_type_analysis_w3w8_c1.md`

---
