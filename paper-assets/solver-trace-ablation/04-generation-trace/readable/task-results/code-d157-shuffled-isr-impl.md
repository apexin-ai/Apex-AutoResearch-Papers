# code d157 shuffled isr impl

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d157-shuffled-isr-impl_20260520T143537_result.json`
- **Structured JSON:** [`8b52226896ae131b7485.json`](../../sessions/8b/8b52226896ae131b7485.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU released, temp files cleaned. Here's the summary:

---

**Dry-run 通过。** 3 个 step 全部正常完成，reward 计算无报错。

### 代码改动 (train_grpo.py, 637→676 行)
1. `step_buf` 新增 `shuffle_n_proved`, `shuffle_identity` 字段
2. `reward_fn` 内新增 `_shuffle_buf` 和 `shuffled_isr` elif 分支 — 先收集所有 ISR 值（placeholder reward=0），再在 batch 内对 proved samples 做 `_random.Random(stats["total"]).shuffle()`
3. 循环后 post-process：proved>1 时 shuffle ISR 并重算 reward=exec*(1+β*shuffled_isr)，proved≤1 时记录 identity
4. `get_step_stats()` 输出和重置新增 shuffle 字段
5. argparse choices 新增 `shuffled_isr`
6. `LocalLogCallback` 打印 shuffle 统计

### 配置文件
`configs/grpo_shuffled_isr_b01.yaml` — 与 ISR β=0.1 配置一致，仅改 `reward_mode: shuffled_isr`

### Dry-run log (关键行)
```
step=1  reward=0.2700  prove=0.250  isr=0.200  beta_t=0.1000  shuffle_proved=2  shuffle_id=1
step=2  reward=0.0000  prove=0.000  isr=0.000  beta_t=0.1000  (no proved → no shuffle)
step=3  reward=0.5250  prove=0.500  isr=0.250  beta_t=0.1000  shuffle_proved=4  shuffle_id=1
```

---
