# research magnitude crossover novelty

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_magnitude-crossover-novelty_20260514T022857_result.json`
- **Structured JSON:** [`85dee70a9c1eebdfb32c.json`](../../sessions/85/85dee70a9c1eebdfb32c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，写入 `artifacts/magnitude_crossover_novelty_check.md`。

**新颖性：中-高。** 核心结论：

1. **无直接竞争**：没有论文报告过 importance vs. random eviction 在不同 reasoning phase 的性能排序反转，也没有论文将 head pruning + KV eviction 作为 compound sparsity 整体研究。

2. **部分被覆盖的机制**：DefensiveKV (ICLR'26) 已证明 importance stability 的脆弱性；NACL (ACL'24) 已展示 random eviction 的 diversity benefit。这两篇解释了 crossover 的部分机制，但都没发现 phase-conditional 的方向反转。

3. **最大风险**：项目自身 v3 数据显示所有 phase 的 II 均 super-additive 且 CI 重叠，且 phase segmentation 已被证伪为 unimodal。crossover 发现需要更强的统计验证和更好的 phase 定义。

4. **推荐 framing**：不要用离散 phase，改用 output entropy 作为连续 conditioning variable，将 finding 包装为 **"Strategy Sensitivity Amplification under Compound Sparsity"**——compound setting 将 eviction strategy 选择的影响指数级放大。这个 framing 直接对接 ICLR'25 Interplay paper 的非正交性理论框架。

---
