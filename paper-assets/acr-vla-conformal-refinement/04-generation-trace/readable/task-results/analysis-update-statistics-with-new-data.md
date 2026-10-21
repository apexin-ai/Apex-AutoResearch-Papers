# analysis update statistics with new data

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_update-statistics-with-new-data_20260520T060316_result.json`
- **Structured JSON:** [`f4b4d0748d1b7b5fce9d.json`](../../sessions/f4/f4b4d0748d1b7b5fce9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功，输出已保存到 `statistical_analysis_output_v2.txt`。

### 关键变化对比（v1 → v2）

| Comparison | 旧 p-value | 新 p-value | 变化 |
|---|---|---|---|
| **Long: CRM vs VLA** | 0.0276 * (n=6v7) | **0.0488 *** (n=7v11) | p 变大，但仍 *（VLA-Long 加入4个偏高的seed拉高了baseline mean：0.1414→0.1482） |
| **Goal: CRM vs VLA** | 0.5819 n.s. (n=6v5) | **0.8179 n.s.** (n=6v6) | 新seed49=0.65拉低VLA-Goal均值（0.694→0.687），差异更小，仍不显著 |
| **Spatial: CRM vs VLA** | p≈7e-6 *** | **p≈7e-6 ***（n=7v9）** | CRM加了0.36，mean微升0.3433→0.3457，显著性不变 |
| **Long CRM mean** | 0.1750 (n=6) | **0.1700 (n=7)** | seed50=0.14 拉低了 CRM-Long 均值 |
| **Adaptive-K all** | n=11 | **n=12** | p25加入0.15，整体mean 0.1409→0.1417 |

**核心影响**：Long 的 p-value 从 0.028 升至 0.049，刚好卡在 0.05 边缘——VLA-Long 新增的4个seed（0.15-0.17）偏高，缩小了 CRM-VLA 差距。MW-U 检验已不显著（p=0.061）。其余结论不变。

---
