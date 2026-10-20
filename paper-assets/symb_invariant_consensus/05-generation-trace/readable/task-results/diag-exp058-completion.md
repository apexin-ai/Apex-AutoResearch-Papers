# diag exp058 completion

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp058-completion_20260519T043723_result.json`
- **Structured JSON:** [`e37d3beceeda14f5d4c7.json`](../../sessions/e3/e37d3beceeda14f5d4c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-058 处理完毕。

**exp-058 T=0.5 结果：**
| 指标 | 值 |
|---|---|
| SC accuracy | 57.84% (118/204) |
| SICA accuracy | 57.35% (117/204) |
| delta | **-0.49pp** |
| McNemar | b=3, c=2, p=1.0000 (不显著) |
| 完成度 | 204/204 |

**完整 T sensitivity 曲线 (Mistral-7B, FOLIO-204, k=12)：**

| T | delta (pp) | 方向 |
|---|---|---|
| 0.3 | -0.49 | 微负 |
| **0.5** | **-0.49** | **微负** |
| 0.7 | +4.90 | 正（最佳） |
| 1.0 | +0.49 | 微正 |

T=0.5 和 T=0.3 的 delta 完全相同（-0.49pp），discordant pairs 极少（b=3, c=2），说明低温下 SC 和 SICA 行为几乎一致。SICA 的优势集中在 T=0.7，符合「需要足够多样性才能让约束聚合发挥作用」的预期。

Registry 已更新为 DONE (negative)，cron 已删除。

---
