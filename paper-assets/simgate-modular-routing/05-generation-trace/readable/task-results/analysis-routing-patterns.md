# analysis routing patterns

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_routing-patterns_20260515T114910_result.json`
- **Structured JSON:** [`4fbebd10368a73cdfa2d.json`](../../sessions/4f/4fbebd10368a73cdfa2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 PDF 和分析脚本均已就绪。

---

## 产出

### 文件
- `results/routing-patterns/routing_heatmap.pdf` (30KB)
- `results/routing-patterns/death_timing.pdf` (16KB)
- `results/routing-patterns/episode_length_comparison.pdf` (20KB)
- `scripts/analyze_routing_patterns.py`

### 分析 Summary

**Routing Pattern（245 episodes, 11 tasks）**

| 指标 | 值 |
|---|---|
| Det-preferred | 86 (35.1%) |
| Internal-preferred | 9 (3.7%) |
| No-preference | 150 (61.2%) |
| **Det/(Det+Int)** | **90.5%** |

- 6 个 task（Find-Animal, Life-Stage-1/2, Freeze, Melting-Pt, Incline）Det/(Det+Int) = **100%**，无一 episode 偏好 internal
- 5 个 task 有 internal-preferred episodes，最多的是 Find-NL（4/40=10%）和 Chem-Mix（2/20=10%）

**Death Timing**

| | Internal | Deterministic |
|---|---|---|
| 总 death 数 | 105 | 40 |
| Mean death step | **18.6** | **21.9** |
| Early (1-10) | 3.8% | 0.0% |
| **Mid (11-20)** | **69.5%** | 30.0% |
| Late (21-30) | 26.7% | **70.0%** |

**关键 insight**: Internal model 的 death 集中在 mid-game（steps 11-20, 69.5%），而 deterministic model 的 death 集中在 late-game（steps 21-30, 70.0%）。Internal model 平均早 3.3 步死亡。这说明 internal model 在中期阶段更容易做出致命错误决策。

**Episode Length**

- Internal 平均 episode 长度在所有 task 上都 ≤ deterministic（因为 death 导致提前终止）
- Find-NL 是唯一例外（两者均为 30.0，该 task 无 death）
- 差距最大的是 Life-Stage-1（+5.7 步）和 Lifespan-L（+5.2 步）

**Death-conditioned routing**: Internal 死亡的 105 个 episode 中 66.7% 被标记为 det-preferred；无 death 的 140 个 episode 中仅 11.4% 为 det-preferred。Death asymmetry 是 routing label 的主要驱动信号。

---
