# code plan017 and eval prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan017-and-eval-prep_20260514T023636_result.json`
- **Structured JSON:** [`09615a8644e8fe24fa26.json`](../../sessions/09/09615a8644e8fe24fa26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

### 产出总结

**1. plan017 config**
- 路径: `configs/grpo_additive_random.yaml`
- 关键参数: `reward_mode: additive_random`, `beta: 0.3`, `data_path: data/train_500_seed42.jsonl` (C001 合规)
- 奖励公式: `r = r_exec * (1 + 0.3 * random[0,1])`，与 plan002 `additive_bonus` 结构完全对称，random 替代 ISR

**2. train_grpo.py 修改**
- 在 `make_reward_fn` 中添加 `additive_random` 分支（line ~196）：调用 `_full_fn` 获取 execution reward，乘以 `(1 + beta * random)`
- 在 argparse choices 列表中添加 `additive_random`
- 随机数使用 `_random.Random(stats["total"])` 确保可复现

**3. eval_downstream.py 修改**
- 新增 `scipy.stats.spearmanr` — ISR 与 NLI 正确性秩相关
- 新增 `scipy.stats.mannwhitneyu` — Q4 vs Q1 ISR 分组 accuracy 显著性
- 新增 `bootstrap_bon_ci()` — Best-of-N ISR-best vs random 的 95% CI（1000 次 bootstrap）
- 统计结果写入 summary JSON 并在终端打印

**4. eval_cross_solver.py**
- 路径: `scripts/eval_cross_solver.py`（~150 行）
- 读取 eval_downstream.py 输出 JSON → 对有 premises+conclusion 的 formalization 调 Z3 prove → 与 Prover9 结果比较
- 输出: 四分类 agreement (both_proved/both_unproved/p9_only/z3_only)，按 ISR bucket (high/mid/low/no_isr) 分组统计
- 支持多 worker 并行

**注意事项**
- 现有 `grpo_random_reward.yaml` 使用了 `data_path: data/proofwriter_fol_500.jsonl`，违反 C001。plan017 已修正为 `train_500_seed42.jsonl`
- 现有 `random_reward` 模式用的是 weighted combo `r = w_exec * 1.0 + w_sta * random`，结构不同于 additive bonus。plan017 的 `additive_random` 使用乘法结构 `r_exec * (1 + β * random)` 与 plan002 完全对称，是正确的对照

---
