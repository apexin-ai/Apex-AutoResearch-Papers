# research seed2 checkpoint5000 verify

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_seed2-checkpoint5000-verify_20260516T052838_result.json`
- **Structured JSON:** [`aa4c65f7cd087b92be52.json`](../../sessions/aa/aa4c65f7cd087b92be52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Seed2 checkpoint-5000 分析完成，MVP PASS。**

核心结果：

| 指标 | seed1 | seed2 | 差异 |
|------|-------|-------|------|
| BC | 0.937 | 0.933 | −0.004 |
| scorer_std | 0.440 | 0.438 | −0.002 |
| within-sample ratio | 22.59× | 23.02× | +0.43 |
| frac(w<0.2) | 41.4% | 40.5% | −0.9pp |
| frac(w>0.8) | 49.2% | 49.2% | 0 |

两个 seed 所有指标差异 < 1%，独立收敛到几乎相同的 bimodal 分布。diversity_lambda=0.1 下 scorer 行为稳健，不依赖随机初始化。

报告已写入 `artifacts/scorer_analysis_seed2_step5000.md` 并注册（art_20260516_868ff5）。

---
