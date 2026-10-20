# paper figures generation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figures-generation_20260515T230013_result.json`
- **Structured JSON:** [`145cdc586f11ae543076.json`](../../sessions/14/145cdc586f11ae543076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个图表全部生成并注册完成：

| 图表 | 文件 | 放置位置 |
|------|------|----------|
| Fig 1: Task Reformulation | `fig1_reformulation.{pdf,png}` | Introduction |
| Fig 2: Gap Amplification | `fig2_gap_amplification.{pdf,png}` | Experiments |
| Fig 3: Oracle Stratified | `fig3_oracle_stratified.{pdf,png}` | Experiments |

- Fig 1: CLS/CWM/TRAJ 三条 pipeline 对比，CWM 失败模式（token exhaustion、53-67% unparseable）红字标注
- Fig 2: broken axis 展示 gap 从 1.24pp → 2.43pp → 25.59pp 的急剧增长，含误差线和 p 值
- Fig 3: 双轴图，block advantage 柱 + instance % 线，标注 T=2 贡献 55.3% 总 advantage

---
