# code verify alfworld score

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-alfworld-score_20260514T055837_result.json`
- **Structured JSON:** [`8c3fbc3f44271cd3c91b.json`](../../sessions/8c/8c3fbc3f44271cd3c91b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完毕。以下是报告。

---

## ALFWorld Score 粒度调研报告

### 1. ALFWorld score 是否可用

**不可用作连续奖励。** 

- RAGEN `env.py:137` 的 `request_infos` 未请求 `score=True`，但这**不是主要问题**
- 即使添加 `score=True`（实测已验证），返回的 score 仍然是 **纯二值 0/1**
- 根源在 TextWorld PDDL env (`pddl.py:170`):
  ```python
  self.state["score"] = 1 if self.state["won"] else 0
  ```
- TextWorld 的 `intermediate_reward` 机制仅在 `tw.py`（标准 TextWorld env）中实现，ALFWorld 用的是 `PddlEnv`，**不支持 intermediate_reward**

### 2. Score 粒度：所有 6 种任务类型均为 0/1

实测 walkthrough 全程执行结果：

| 任务类型 | walkthrough 步数 | score 序列 |
|----------|-----------------|------------|
| pick_and_place | 4 | [0,0,0,**1**] |
| look_at_obj_in_light | 4 | [0,0,0,**1**] |
| pick_clean_then_place | 6 | [0,0,0,0,0,**1**] |
| pick_heat_then_place | 6 | [0,0,0,0,0,**1**] |
| pick_cool_then_place | 7 | [0,0,0,0,0,0,**1**] |
| pick_two_obj | 8 | [0,0,0,0,0,0,0,**1**] |

**结论：ALFWorld 没有原生的连续进度信号。** PDDL goal 是一个 conjunction，所有 goal predicates 必须同时满足才算 won。

### 3. RAGEN 当前 reward function 完整逻辑

**env 层** (`ragen/env/alfworld/env.py:194-195`):
```python
reward = self.config.score * float(won)  # 10.0 * (0 or 1) = 0 或 10
```

**es_manager 层** (`ragen/llm_agent/es_manager.py:184-208`):
- 每个 turn 内多个 action 的 reward 累加：`acc_reward += reward`
- 存入 `status.rewards` 列表

**ctx_manager 层** (`ragen/llm_agent/ctx_manager.py`):
- `get_masks_and_scores()` 将 env rewards 转为 `rm_scores` tensor
- 支持 turn-level（`use_turn_scores=True`）和 episode-level 两种模式

**B-IAVR 层** (`ragen/biavr/reward.py`):
- 在 env reward 之上叠加 verify 成本/奖励：`r = -lambda_cost + alpha * 1[action_changed]`
- 注入到 history 的每个 turn：`turn['reward'] += biavr_reward`

**总公式（每 turn）**：`reward = 10.0 * won + biavr_reward(verify, changed)`

### 4. 接入连续 score 的改动建议

**A1 方案（直接用 ALFWorld score）不可行**——score 本身就是 0/1，和 won 等价。

**替代方案 A1'：基于 walkthrough 进度的 reward shaping**

需改动 2 个文件：

**(a) `ragen/env/alfworld/env.py`**
- `reset()` 中保存 `self.walkthrough = game_data['walkthrough']`，`self.walkthrough_idx = 0`
- `step()` 中：如果 agent 的 action 匹配 walkthrough 的下一步，`walkthrough_idx += 1`
- 计算 `progress = walkthrough_idx / len(walkthrough)`
- 在 `info` dict 中返回 `info['progress'] = progress`

**(b) `ragen/env/alfworld/env.py` 的 reward 计算**
```python
# 替换 reward = self.config.score * float(won) 为：
progress = self.walkthrough_idx / len(self.walkthrough)
reward = self.config.score * progress  # 0 到 10 的连续值
```

**替代方案 A1''：基于 PDDL facts 的子目标进度**

可行但复杂度更高：
- 需要 `request_infos.facts=True`（已验证 PddlEnv 支持）
- 需要解析 PDDL goal 结构，识别动态 vs 静态 predicates
- 需要处理 existential quantification 的变量绑定问题

### 5. 风险评估

| 风险 | 严重度 | 说明 |
|------|--------|------|
| **walkthrough 方案鼓励模仿而非探索** | **高** | 只奖励匹配 expert trajectory 的 action，抑制 agent 发现新策略。GRPO 可能 collapse 到模仿 walkthrough |
| **局部最优** | **中** | agent 可能学会执行前几步（拿物品）拿到部分 reward 但不完成整体任务（放到目标位置） |
| **walkthrough 匹配脆弱** | **中** | agent action 可能语义等价但文本不同（如 "go to table 1" vs "go to diningtable 1"），需要 fuzzy matching |
| **facts-based 方案实现复杂** | **低** | 需要大量自定义代码，但逻辑正确性更好 |
| **reward scale 变化影响 GRPO 训练稳定性** | **中** | 从 {0,10} 变为 [0,10] 连续值，需要调整 GRPO 的 advantage normalization |

**核心结论：D008 的前提假设不成立——ALFWorld 没有原生连续 score。** 如果要实现连续奖励，需要自行设计 reward shaping，但引入的风险（尤其是鼓励模仿/局部最优）需要仔细权衡。建议优先考虑其他缓解稀疏奖励的方案（如 curriculum learning、更小的 group size、或 B-IAVR 参数调优）。

---
