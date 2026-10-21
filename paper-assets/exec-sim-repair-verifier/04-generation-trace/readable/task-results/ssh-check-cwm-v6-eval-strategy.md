# ssh check cwm v6 eval strategy

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-cwm-v6-eval-strategy_20260512T201322_result.json`
- **Structured JSON:** [`baa3e6ff4e2b4d8ca5f2.json`](../../sessions/ba/baa3e6ff4e2b4d8ca5f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. eval_strategy / save_strategy 对比

```python
# train_repo_cwm.py 的 TrainingArguments (非 dryrun 模式)
"eval_strategy": "steps",
"save_strategy": "steps",
"save_steps": 500,
# eval_steps: 未显式设置 → 默认跟随 logging_steps = 50
```

**策略匹配**，都是 `"steps"`。不存在 CLS 脚本那种 eval="epoch" + save="steps" 导致 Trainer 静默覆盖的 bug。

### 2. Checkpoint 目录为空 — 但原因不是 bug

```
/root/autodl-tmp/checkpoints_repo_cwm_v6/  →  空（仅 . 和 ..）
```

**这是预期行为。** 实际训练进度远低于表面看到的：

- `tail` 看到的 `3691/9335` 是**正在运行的 eval 进度条**（9335 个 eval 样本），不是训练进度
- 训练的真实进度：**约 step 200 / 6633**（仅 ~3%）
- `save_steps=500`，第一个 checkpoint 还没到

日志中的 eval 记录：
- step 100: eval_loss=0.6099（耗时 752s）
- step 150: eval_loss=0.4333（耗时 752s）

### 3. 严重性能问题

`eval_steps` 未显式设置，默认跟随 `logging_steps=50`。每次 eval 耗时 **~12.5 分钟**（9335 eval 样本）。

| 指标 | 值 |
|------|-----|
| 训练总步数 | 6633 |
| eval 频率 | 每 50 步 |
| eval 次数 | ~133 次 |
| 每次 eval 耗时 | ~12.5 min |
| eval 总耗时 | **~27.7 小时** |
| 训练总耗时 | ~14.7 小时 |
| 预估总时间 | **~42 小时** |
| 训练占比 | ~35%（65% 时间在 eval） |

进程运行 56 分钟，实际只训练了 ~200 步（3%）。

### 4. 结论

- **无 CLS 同款 bug**，eval_strategy 和 save_strategy 都是 "steps"，checkpoint 不会被静默跳过
- **checkpoint 为空是因为还没到 step 500**，不是全损风险
- **但有严重效率问题**：eval 每 50 步触发一次（应该和 save_steps 一样设 500），导致训练时间从 ~15h 膨胀到 ~42h，约 65% 的 GPU 时间浪费在 eval 上
- PID 84887 正在运行，未做任何修改

---
