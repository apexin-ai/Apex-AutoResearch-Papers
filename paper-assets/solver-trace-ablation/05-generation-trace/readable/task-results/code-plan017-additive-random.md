# code plan017 additive random

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan017-additive-random_20260514T031405_result.json`
- **Structured JSON:** [`db717941e079b6bb8bc8.json`](../../sessions/db/db717941e079b6bb8bc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**代码已就绪，无需新建脚本。** `train_grpo.py` 已内置 `additive_random` 模式，`grpo_additive_random.yaml` 配置也已存在。

**本次改动**：给 `step_buf` 增加了 `random_sum`/`random_n` 追踪，reward_log 现在显式输出 `random_mean` 字段，方便区分 random 值和 ISR。

**Dry-run 验证通过**：
- `reward_mode=additive_random`，公式 `r = r_exec * (1 + 0.3 * random_value)` 正确执行
- reward_log 同时记录 `isr_mean`（真实 ISR，未用于奖励）和 `random_mean`（实际用于奖励的随机值）
- Step 1: `random=0.391, isr=0.400, reward=0.589, prove_rate=0.500`
- Step 2: `random=0.492, isr=0.000, reward=0.000, prove_rate=0.000`（所有样本 execution 失败→reward=0，符合预期）

**启动命令**：
```bash
export CUDA_VISIBLE_DEVICES=&lt;N>
python scripts/train_grpo.py --config configs/grpo_additive_random.yaml
```

---
