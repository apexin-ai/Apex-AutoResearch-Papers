# research track d te robustness

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_track-d-te-robustness_20260522T043828_result.json`
- **Structured JSON:** [`fbcaf7805c337db3e146.json`](../../sessions/fb/fbcaf7805c337db3e146.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**Original 复现成功**: sync-dip 4/6 显著, 正对照 0/6 — 与原结果一致

**去趋势 (一阶差分)**: sync-dip **0/6** 显著 — 全部显著性消失。原始 TE 信号是共享单调下降趋势的 artifact，不是真正的非线性信息传递。m=2 ordinal patterns 只编码升/降，被共享趋势主导。

**m=3**: 0/6 显著 — 方向一致，但 T=10-20 下有效序列太短（8-18 个 pattern），统计功效不足也是原因之一。

**High surrogates (2000)**: 4/6 显著 — 与 500 surrogates 完全一致，p 值已充分解析。

**结论**: Symbolic TE 的 sync-dip 显著性不鲁棒，经不起去趋势检验。建议论文中不以此为非线性因果证据，而将负面去趋势结果重新定位为「确认 sync-dip 耦合是线性共享趋势驱动」的诊断证据，反而加强 PermG 解释框架。

产出文件：
- 远程: `artifacts/transfer_entropy_robustness.{py,json,pdf,png}`
- 本地: `artifacts/alpha_c_theory/te_robustness_summary.txt`

---
