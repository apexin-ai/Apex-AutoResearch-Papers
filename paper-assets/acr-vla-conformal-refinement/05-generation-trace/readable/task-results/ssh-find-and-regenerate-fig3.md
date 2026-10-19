# ssh find and regenerate fig3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_find-and-regenerate-fig3_20260520T063731_result.json`
- **Structured JSON:** [`65a1755377204e0933a3.json`](../../sessions/65/65a1755377204e0933a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇报：**

| 项目 | 内容 |
|------|------|
| **脚本路径** | `artifacts/figures/paper/gen_fig3_kvalue.py` |
| **修改内容** | VLA-only baseline: 11.6%→**10.9%**; K=5 mean: 16.25→**16.0** (n=4→7); K=10 mean: 17.57→**16.8** (n=7→6); 所有文本标注同步更新 |
| **新图表** | `artifacts/figures/paper/fig3_kvalue.pdf` / `.png` |
| **artifact ID** | `art_20260520_465226` |

注意：`stds` 保留了旧值（K=5: 2.22, K=10: 2.57），因为任务未提供新的标准差。如果有新的 per-seed 数据，需要更新。JSON 数据文件 `k_value_curve_data.json` 也仍是旧数据，需要同步更新。

---
