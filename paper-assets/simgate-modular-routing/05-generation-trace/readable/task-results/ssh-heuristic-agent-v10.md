# ssh heuristic agent v10

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_heuristic-agent-v10_20260518T053735_result.json`
- **Structured JSON:** [`33b239855471dc3787dc.json`](../../sessions/33/33b239855471dc3787dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

最终结果汇总。

---

## v10 结果

### v10 核心修改（vs v9）

| 改动 | 说明 |
|------|------|
| **恢复紧急 sleep** | energy ≤ 1 且 monster > 3 tiles → sleep; energy ≤ 2 且 monster > 5 tiles → sleep |
| **条件性 flee** | 有剑+hp≥5: 仅逃 2+ within 3 tiles; 有剑+hp<5: 逃 any within 4; 无剑: 逃 any within 5 |
| **主动清怪** | 有剑+hp≥6+单个 zombie within 2 tiles+无附近其他 monster → 攻击 |
| **放宽常规 sleep** | energy ≤ 3 且 monster > 5 tiles → sleep |
| **Sapling farming** | food ≤ 5 时收集 sapling (DO on grass); 有 sapling 时种植; 空闲时机会性收集/种植 |

### 5 Episode 结果（seed=42）

| Agent | Ep0 | Ep1 | Ep2 | Ep3 | Ep4 | **Avg** | Avg Achieve |
|-------|-----|-----|-----|-----|-----|---------|-------------|
| **v10** | 495 | 226 | 475 | 501 | 188 | **377** | **8.4** |
| v9 baseline | 220 | 179 | 481 | 653 | 203 | 347 | 6.2 |
| Random | 180 | 40 | 135 | 254 | 148 | **151** | **2.4** |

### 20 Episode 结果（seed=100）

| 指标 | v10 | v9 baseline |
|------|-----|-------------|
| Avg steps | **328** | 286 |
| Avg achievements | **7.2** | 5.8 |
| Max steps | 772 | 760 |
| Min steps | 204 | 180 |

### v10 vs Random 优势
- 存活步数 **2.5x**（377 vs 151）
- 成就数 **3.5x**（8.4 vs 2.4）
- v10 每局解锁: collect_drink, collect_sapling, collect_wood, defeat_zombie, eat_cow, make_wood_sword, place_plant, place_table (8/5 episodes)

### Death Rate
- **100% death rate**（未达到 <80% 目标）
- 死因分布: ~60% monster 集群伤害（-7hp 单步），~40% 饥饿（food=0 后缓慢失血）

### 迭代过程

| 版本 | 改动 | Avg Steps (seed=100) | 结果 |
|------|------|---------------------|------|
| v10 | 紧急sleep+条件flee+清怪 | 286 | 基线 |
| v10.1 | 更激进flee (3+ within 5) | 209 | **退步** |
| v10.4 | +sapling farming | **326** | **最佳** |
| v10.5 | +cluster flee (3+ within 4) | 295 | 略退 |
| v10.6 | +aggressive hunting (4 tiles) | 218 | **大退** |
| v10.7 | +danger-aware movement | 225 | **退步** |

### 剩余瓶颈
1. **Monster 集群伤害**：走进 3+ monster 时受 7hp 单步伤害。更激进的 flee 反而降低存活（减少进食/喝水时间）。danger-aware movement 也帮倒忙
2. **食物上限**：地图 32 cows 有限，sapling farming 有帮助但不够撑到 1000 步
3. 要突破 100% death rate 可能需要**根本性策略变化**（如石墙庇护所、更高级武器/盔甲）

---
