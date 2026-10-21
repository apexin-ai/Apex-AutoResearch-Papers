# research alfworld methodology

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_alfworld-methodology_20260515T154350_result.json`
- **Structured JSON:** [`b5a0118287a0a65609b2.json`](../../sessions/b5/b5a0118287a0a65609b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the structured output:

---

## ALFWorld 方法论补充材料

### 1. 模型

**Qwen2.5-7B-Instruct** (`/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct`)
- 推理引擎：vLLM，`gpu_memory_utilization=0.85`，`max_model_len=4096`
- 生成参数：`temperature=0.3`，`max_new_tokens=256`

### 2. "Deterministic" Modality 的精确定义

**与 ScienceWorld 语义完全不同。** ALFWorld 中 "deterministic" = LLM 在每一步接收环境提供的 **admissible actions list**（合法动作列表）。

代码 docstring 原文：
> The admissible actions list is the "deterministic computation" source: it constrains the LLM to valid simulator actions.

具体实现对比：

| 维度 | Internal mode | Deterministic mode |
|------|--------------|-------------------|
| 系统 prompt | "You do NOT have access to any action list" | "You MUST choose an action from the admissible actions list exactly as written" |
| 用户 prompt | 仅含 observation + history | 含 observation + history + **编号的 admissible actions 列表** |
| 动作解析 | `parse_action_free()` → 自由文本提取，再 `match_to_admissible()` 做 best-effort 匹配（exact → case-insensitive → substring） | `parse_action_constrained()` → 直接匹配 admissible list |
| 兜底 | 匹配失败时 fallback 到 `admissible[0]` | 同 |

关键点：Internal mode 生成的动作仍然需要 map 到 admissible action 才能执行（TextWorld 引擎限制），但 LLM **看不到**这个列表。差异完全在于信息可见性，不是模拟器模式的切换。

### 3. Labeling 流程（与 Algorithm 1 的异同）

**沿用 Algorithm 1 的 episode-level 比较逻辑**，标签定义完全一致：

```
if det_success and not internal_success → "det-preferred"
if internal_success and not det_success → "internal-preferred"
else → "no-preference"  (both succeed OR both fail)
```

**差异：**
- **成功判定**：ALFWorld 使用 TextWorld 的 `won` 布尔标志（任务是否完成），不存在 ScienceWorld 的 normalized score / death 概念
- **无 death 统计**：ALFWorld 没有 agent 死亡机制，失败 = 50 步内未完成任务
- **无部分分数**：score 只有 0.0（失败）和 1.0（成功），没有中间态

### 4. Episode 长度配置

- **max_steps = 50**（命令行默认值，实际运行使用此值）
- Split: `valid_seen`（来自 `json_2.1.1`）
- History window: 最近 10 步 (`last_k=10`)
- Random seed: 42
- 环境：TextWorld gym + `AlfredDemangler(shuffle=False)` + `AlfredInfos`

步数统计：
| | Mean | Median | Min | Max |
|---|---|---|---|---|
| Internal | 49.0 | 50.0 | 5 | 50 |
| Deterministic | 40.2 | 50.0 | 3 | 50 |

几乎所有 internal episodes 都跑满 50 步（3.0% 成功率极低）。

### 5. 关键统计

**总量**：135 games，6 task types

**Label 分布**：

| Label | Count | % |
|-------|-------|---|
| det-preferred | 35 | 25.9% |
| internal-preferred | 2 | 1.5% |
| no-preference | 98 | 72.6% |

**No-preference 细分**：both-succeed = 2，both-fail = **96**

**成功率**：Internal 4/135 (3.0%)，Deterministic 37/135 (27.4%)

**按 Task Type 细分**：

| Task Type | N | Internal SR | Det SR | det-pref | int-pref | no-pref |
|-----------|---|-------------|--------|----------|----------|---------|
| pick_and_place | 32 | 0.0% | 56.2% | 18 | 0 | 14 |
| pick_clean_then_place | 27 | 3.7% | 18.5% | 5 | 1 | 21 |
| pick_cool_then_place | 24 | 0.0% | 16.7% | 4 | 0 | 20 |
| pick_two_obj_and_place | 23 | 0.0% | 8.7% | 2 | 0 | 21 |
| pick_heat_then_place | 16 | 6.2% | 18.8% | 3 | 1 | 12 |
| look_at_obj_in_light | 13 | 15.4% | 38.5% | 3 | 0 | 10 |

**论文写作要点**：
- ALFWorld 的 deterministic modality 是 **admissible actions oracle**，不是 simulator mode——需要在补充材料中明确说明这个语义差异
- 标签分布严重偏向 det-preferred + both-fail，符合"外部知识源（admissible list）显著提升 7B 模型在交互式任务中的表现"的叙事
- `pick_and_place` 上 det 优势最大（56.2% vs 0.0%），因为动作空间约束对简单导航任务帮助最大

---
