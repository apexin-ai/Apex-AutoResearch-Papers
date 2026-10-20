# paper n500 number fix comprehensive

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_n500_number_fix_comprehensive_20260516T043514_result.json`
- **Structured JSON:** [`3f100ae61bc9ee6884fd.json`](../../sessions/3f/3f100ae61bc9ee6884fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终结论

论文**已经完成了所有 n=50 → n=500 数字替换**。所有任务项的当前状态：

### 全部已完成 ✅

| 项目 | 验证 |
|------|------|
| A. DS s030: 14.59→8.48 | 主文全部用 8.48；14.59 仅在 appendix profiling subset 表（正确标注） |
| B. DS 中间值: 1.48→1.21, 7.16→3.99 | 同上 |
| C. QW 四值: 0.07, 0.31, 1.07, 3.16 | Table 2 + Table 3 ✅ |
| D. d_z 值 | 旧值(0.44/0.80/0.28/1.02) **不在任何 .tex 文件中**；论文改用 within-importance d_z=0.94/0.92 (n=500 数据) |
| E. n=50→n=500 | methodology 用 "500 problems"，表 caption 用 n=496/475 |
| F. 37×→22× | results.tex "$22{\times}$ amplification" ✅ |
| G. Table 1 | 0.39 & 1.21 & 3.99 & 8.48 ✅ |
| H. Table 2 + G ratios | 完整 n=496/475 数据 + Appendix V G表含 bootstrap CI |
| I. Permutation test | 保留 n=49 profiling subset，正确标注，主文改用 n=496 Wilcoxon |

### 服务器数据验证

SSH 到 `westd-22162` 确认 `/root/autodl-tmp/pacs/analysis_output/n500_full_statistics.md` 中的数值与论文一致：
- DS: 0.3907, 1.2149, 3.9857, 8.4813 ✅
- QW: 0.0659, 0.3073, 1.0745, 3.1550 ✅
- Within-importance d_z: DS -0.944, QW -0.923（论文报告 0.94/0.92）✅

### 唯一微小 inconsistency

`conclusion.tex` 写 "DeepSeek, $n{=}500$"，而其他地方用有效样本量 $n{=}496$。这是简化写法（500=总问题数），不算错误，但如果要严格统一可改为 $n{=}496$。

**无需执行任何编辑。** 论文在本次任务之前已经被完整更新。

---
