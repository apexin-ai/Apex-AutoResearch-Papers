# code cuda2 scierc epoch dgs

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cuda2_scierc_epoch_dgs_20260518T191406_result.json`
- **Structured JSON:** [`87aac2afad3455347e32.json`](../../sessions/87/87aac2afad3455347e32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。汇总：

**Task 1: SciERC 3ep/10ep DGS 分析** ✅
**Task 2: Qwen rank=8 DGS 分析** ✅

| 设置 | 退化率 | Greedy | DGS | DGS-Greedy | Oracle Headroom |
|------|--------|--------|-----|------------|-----------------|
| 3-epoch | 6.4% | 0.6501 | 0.6383 | **-1.18pp** n.s. | 14.97pp |
| 5-epoch | 17.8% | 0.6439 | 0.6513 | **+0.74pp** n.s. | 13.19pp |
| 10-epoch | 47.8% | 0.6467 | 0.6567 | **+0.99pp** sig | 8.64pp |
| rank=8 | 7.2% | 0.6397 | 0.6350 | **-0.47pp** n.s. | 16.01pp |

关键结论：
1. **退化率与 epoch 严格单调**: 3ep(6.4%) < 5ep(17.8%) < 10ep(47.8%)
2. **DGS 增益依赖退化率**: 低退化率(3ep/rank8)时 DGS ≈ LP-all，而 LP 选择本身 underperform greedy → DGS 无效；中高退化率时 gating 机制才有意义
3. **10ep 是唯一 DGS 显著正向的设置**（CI 完全在零以上），但代价是 oracle headroom 压缩到 8.64pp
4. **rank8 与 3ep 表现相似**：低退化、高 headroom，但 LP 信号弱

**Task 3**: ROADMAP 剩余 P0 任务主要是论文写作和 LLaMA FewNERD 训练（63%，~6h 剩余）。cuda:2 当前无可执行的分析任务。

---
