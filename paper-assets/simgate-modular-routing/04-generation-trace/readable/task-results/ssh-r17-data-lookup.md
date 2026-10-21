# ssh r17 data lookup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_r17-data-lookup_20260519T113613_result.json`
- **Structured JSON:** [`f4dea4057c33da741f02.json`](../../sessions/f4/f4dea4057c33da741f02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是汇总：

---

## Q1: 72B 实验 Deterministic 细节

**来源**: `westb-13313:/root/autodl-tmp/simgate-modular-routing/results/backbone_72b/`

### 1. 72B 是否有独立 deterministic episodes？

**是**。72B 收集了独立的 det episodes，没有复用 7B 数据。
- `collection_meta.json` 显示 `"reused_episodes": 0`
- 每个 episode 的 `episodes.jsonl` 包含完整的 `always_internal` 和 `always_deterministic` 配对轨迹
- 覆盖 **9 个 tasks**（缺少 lifespan-longest-lived-then-shortest-lived 和 measure-melting-point-unknown-substance）
- lifespan-longest-lived 只有 15 episodes，其余 8 个 tasks 各 20 episodes
- **总计 175 episodes**

### 2. 72B Det death rate

| Metric | Value |
|--------|-------|
| Int death rate | **33.7%** (59/175) |
| Det death rate | **2.9%** (5/175) |
| δ (death rate differential) | **30.9%** |

### 3. 72B Δ_nd

**Δ_nd = +3.50**（113 个 both-survive episodes）

几乎全部来自 find-non-living-thing（该 task 0 deaths，但 det 在 score comparison 上大幅领先 +20.0）。其余 8 个 task 的 Δ_nd 全部为 0.0（both-survive 时 int 和 det 得分完全相同）。

### 4. 72B DAF

| Metric | Value |
|--------|-------|
| DAF (aggregate) | **89.6%** |
| DAF (task-weighted, 9 tasks) | **89.0%** |

Per-task DAF: 8/9 tasks = 100%，find-non-living-thing = 0%（无 death，纯 score gap）

### 5. 72B Label distribution

- det-preferred: **66**, no-preference: **104**, internal-preferred: **5**
- Signal sources: death_asymmetry: **60**, tied_alive: **102**, both_dead: **2**, score_comparison: **11**

---

## Q3: Reflexion N=3 Δ_nd

**来源**: westb + westd 的 `reflexion_dose_response/` + `plan_c/` 数据

对比 Reflexion N=k 最终得分 vs plan_c 中相同 task+variation 的 det baseline（183 matched episodes）：

| Condition | Death rate (ref) | Death rate (det) | Δ_full | Δ_nd | n_nd | DAF |
|-----------|-----------------|-----------------|--------|------|------|-----|
| N=1 (baseline) | 51.9% | 20.2% | 33.20 | **-0.48** | 87 | 101.5% |
| N=2 | 43.7% | 20.2% | 24.46 | **-0.08** | 97 | 100.3% |
| **N=3** | **37.2%** | **20.2%** | **17.33** | **-0.47** | **103** | **102.7%** |
| N=4 | 39.9% | 20.2% | 18.24 | -3.20 | 101 | 117.5% |
| N=5 | 38.3% | 20.2% | 17.61 | -1.08 | 105 | 106.1% |

**Reflexion N=3 Δ_nd = -0.47**（103 个 both-alive episodes）。负值说明在 non-death episodes 中，Reflexion 得分略高于 det baseline。DAF > 100% 说明 death avoidance 完全解释了 det 优势（非 death 场景 reflexion 反而更好）。

关键发现：Reflexion N=3 把 death rate 从 51.9%（N=1）降到 37.2%，但 Δ_nd 保持接近 0，说明 Reflexion 的增益几乎全部来自 death reduction。

---

## Q4: DAF 95% CI 方法

**来源**: `westb-13313:/root/autodl-tmp/simgate-modular-routing/src/death_decomposition.py` + `paper/method.tex`

DAF CI [81.6%, 98.8%] 使用的是 **episode-level bootstrap**：

- **B = 10,000** resamples, seed = 42
- 每次 resample 从 N=245 episodes 中**有放回抽取** N 个 episodes
- 对每个 resample 重新计算 Δ_full、Δ_nd 和 DAF = 1 - Δ_nd/Δ_full
- 取 percentile-based 95% CI（2.5th 和 97.5th percentile）
- 论文原文: *"Episode-level bootstrap resampling (B=10,000 resamples)... each resample draws N=245 episodes with replacement, recomputes Δ_full, Δ_nd, and DAF"*

**不是** cluster/task-level bootstrap。代码中也有 task-weighted DAF CI（lines 425-436），那是 resample tasks 的方式，但论文主文报告的 [81.6%, 98.8%] 是 episode-level 的。

代码位置: `death_decomposition.py` lines 355-378（aggregate DAF bootstrap CI 计算）

---
