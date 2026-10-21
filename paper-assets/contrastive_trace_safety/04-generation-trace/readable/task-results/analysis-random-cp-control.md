# analysis random cp control

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random_cp_control_20260519T113501_result.json`
- **Structured JSON:** [`512801a597e983a04e19.json`](../../sessions/51/512801a597e983a04e19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果总结：

**Real-CP vs Random-CP 层选择对比 (OT-7B, 28 layers)**

| Metric | Real-CP 选择的层 | Random-CP 平均层 (±std) |
|--------|-----------------|----------------------|
| BA×crossing (CR-composite) | **L0** (0% depth) | 14.2 ± 9.2 (散布) |
| Precision | **L19** (70% depth) | 14.4 ± 8.0 (散布) |
| FPR | **L18** (67% depth) | 15.3 ± 8.7 (散布) |
| BA | L9 (33% depth) | 13.5 ± 7.6 (散布) |

**核心发现：**
- Real-CP 下 metric disagreement 模式清晰：CR-composite → 极浅层 (L0)，threshold-based → 深层 (L18-19)
- Random-CP 下所有 metric 层选择散布在全层范围（mean 13-15，std 8-9），**无系统性浅/深分裂**
- CR-composite 选浅层频率仅 30%（vs real-CP 100%）
- 所有 metric 表现趋同，**metric disagreement 不可复现**

这直接反驳 W4 的质疑：层选择 metric disagreement pattern 需要真实 CP 标注才出现，不是模型几何的 artifact。

输出文件：
- 服务器：`/root/autodl-tmp/contrastive_trace_safety/artifacts/random_cp_control/`
- 本地：`artifacts/random_cp_control/` (report.txt, random_cp_summary.json)
- 详细 per-repeat 数据：`random_cp_layer_selection.json`

---
