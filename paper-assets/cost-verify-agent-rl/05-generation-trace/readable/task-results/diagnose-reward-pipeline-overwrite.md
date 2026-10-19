# diagnose reward pipeline overwrite

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_reward-pipeline-overwrite_20260514T151646_result.json`
- **Structured JSON:** [`20c4eaf41f3dd9c26ca4.json`](../../sessions/20/20c4eaf41f3dd9c26ca4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部代码链追踪完成。以下是诊断结论。

---

## 诊断结论

### 1. agent_trainer.py 中是否存在 overwrite？

**存在赋值，但不是"覆盖"。**

- **Line 759**: `reward_tensor, reward_extra_infos_dict = compute_reward(batch, self.reward_fn)`
- **Line 779**: `batch.batch["token_level_scores"] = reward_tensor`

但 `token_level_scores` 在 line 779 之前**不存在于 batch 中**。ctx_manager 的 `_build_dataproto` 构造的 batch keys 为：`input_ids, attention_mask, position_ids, responses, loss_mask, rm_scores, original_rm_scores`。**没有 token_level_scores。** 这是首次赋值，不是覆盖。

### 2. self.reward_fn 返回什么？

`self.reward_fn` = **DummyRewardManager**（train.py 硬编码，config 中的选择逻辑被注释掉了）。

DummyRewardManager.__call__ 逻辑：

```python
if 'rm_scores' in data.batch.keys():    # ← 条件为 TRUE
    return data.batch['rm_scores']       # ← 直接返回 env reward
```

ctx_manager 的 `_build_dataproto` 已将 env reward 存为 `rm_scores`，所以 DummyRewardManager **直接透传 rm_scores**，从不走 fallback path（`non_tensor_batch['reward']`）。

### 3. 结论：FALSE ALARM（误报）

完整 reward 链路：

```
alfworld env.step()
  → reward = config.score * float(won)   # 10.0 if won, 0.0 if not
    → es_manager turn history['reward']
      → ctx_manager._extract_history() → scores list
        → get_masks_and_scores() → score_tensor[:, -1] = sum(turn_rewards)
          → _normalize_score_tensor() → identity (no-op for exp016)
            → batch.batch["rm_scores"] = score_tensor
              → DummyRewardManager: return rm_scores (透传)
                → agent_trainer:779: batch.batch["token_level_scores"] = reward_tensor
                  → token_level_rewards → advantage computation
```

**没有独立计算的 Path B 去覆盖 Path A。** "Path B"（DummyRewardManager）读的就是 Path A 的输出（rm_scores），原封不动返回。

### 4. exp016 reward=0 的真正原因

**模型没有完成任何 alfworld 任务。** Alfworld env 的 reward 是稀疏的：`reward = 10.0 * float(won)`，只有完整通关才有非零 reward。如果模型在所有 episode 中都失败，reward 就是全零——这不是管道 bug，而是模型性能问题。

exp013f 有 reward_mean=2.6-4.39，说明部分 episode 通关了，同一条管道正常传递了非零 reward。

### 5. 潜在风险（非当前 bug，但值得注意）

DummyRewardManager 的 fallback path（当 `rm_scores` 不在 batch 中时）会读 `non_tensor_batch['reward']`，但 ctx_manager 的 `_build_dataproto` **从未设置这个 key**（non_tensor 只有 `env_ids, group_ids, messages_list`）。如果未来某个 ctx_manager 模式不设置 rm_scores，fallback path 会 KeyError 崩溃。当前所有模式都设置了 rm_scores，所以不会触发。

---
