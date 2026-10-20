# ssh death taxonomy 245eps

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_death-taxonomy-245eps_20260518T092635_result.json`
- **Structured JSON:** [`f3cfd95218fa6bc1554d.json`](../../sessions/f3/f3cfd95218fa6bc1554d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果：

## 分析结果

**数据源**: `results/plan_c/` 过滤至 `baseline_245eps/` 匹配（245 episodes, 11 tasks, seed=42）

### 死亡统计
| 策略 | 死亡数 | 总数 | 死亡率 |
|---|---|---|---|
| Internal (LLM) | **105** | 245 | **42.9%** |
| Deterministic | 40 | 245 | 16.3% |

### Fatal Action 分类
**100% (105/105) 的致命动作都是 `focus on [X]`** — 与 prescreening 数据一致，结论更强（样本更大）。

### Focus-on 目标分布
Top 3: `workshop` (20.0%), `inventory` (17.1%), `kitchen` (10.5%)

### Per-task 死亡率
- 0% 死亡率: `find-non-living-thing`（两种策略都是 0%）
- 最高死亡率: `lifespan-longest-lived` (56.0% internal vs 16.0% det)
- 10 个 task 的 internal 死亡率在 45-56% 之间

### 生成文件
| 文件 | 大小 |
|---|---|
| `death_action_distribution.pdf/.png` | 36KB / 144KB |
| `death_action_timeline.pdf/.png` | 27KB / 124KB |
| `death_action_comparison.pdf/.png` | 36KB / 125KB |
| `death_failure_taxonomy_245eps.md` | 报告 |

所有文件已覆盖到 `docs/paper/figures/`，报告在 `artifacts/`。关键检查点：Internal death count = 105 (42.9% × 245) ✓，不是旧版的 73。

---
