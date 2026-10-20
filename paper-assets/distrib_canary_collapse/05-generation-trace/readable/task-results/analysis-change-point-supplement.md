# analysis change point supplement

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_change_point_supplement_20260518T142018_result.json`
- **Structured JSON:** [`f37007f9f808e0fb2b20.json`](../../sessions/f3/f37007f9f808e0fb2b20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。输出文件清单：

**新增文件：**
- `cp_results_a000_s42.json`, `cp_results_a000_s43.json`, `cp_results_a000_s44.json`
- `cp_results_a025_s43.json`, `cp_results_a025_s44.json`
- `cp_summary_a000.json`, `cp_summary_a025.json`
- `cp_report_a000.md`, `cp_report_a025.md`

**更新文件：**
- `cp_summary.json` — 全条件综合摘要（含 FPR、data availability、multiple comparisons note）
- `cp_report.md` — 综合报告（含所有 4 个 alpha 条件的断点表 + FPR + cross-condition timing + 方法学说明）

---

**关键发现：**

| Condition | Sig tests | Rate | canary→downstream gap |
|-----------|-----------|------|-----------------------|
| α=0.00 (null) | 12/18 | 66.7% | **-2.25 gen (downstream FIRST)** |
| α=0.25 | 8/12 | 66.7% | 0.0 gen |
| α=0.75 | 14/18 | 77.8% | **+2.25 gen (canary FIRST)** |
| α=1.00 | 5/6 | 83.3% | **+1.0 gen (canary FIRST)** |

**null control FPR = 66.7%**：distinct_1/2/3 在 α=0.00 下全部 3/3 seeds 显著（gen 2），说明这些指标在纯迭代训练中本身就有单调漂移，change-point 显著性无法区分 treatment vs control。

但**时序排列是可区分的**：null 下 downstream (gen 2) 先于 canary (gen 4-8)，treatment 下反转为 canary (gen 1) 先于 downstream (gen 3-5)。这支持"canary lead time"的叙事，但论文中必须诚实报告高 FPR，并强调推断依据是跨指标时序排列而非单个显著性检验。

α=1.0 只有 s42 一个 seed（服务器上无 s43/s44/s45 数据）。α=0.25 缺 s42。均已在 `cp_summary.json` 的 `data_availability` 中标注。

---
