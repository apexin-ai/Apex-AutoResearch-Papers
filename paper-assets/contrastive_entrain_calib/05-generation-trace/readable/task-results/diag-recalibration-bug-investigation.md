# diag recalibration bug investigation

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_recalibration-bug-investigation_20260519T113046_result.json`
- **Structured JSON:** [`192a3827d1c4ff8428a0.json`](../../sessions/19/192a3827d1c4ff8428a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整报告。

---

## 调查报告：Recalibration 机制 Bug

### 1. `_reward_step` 递增粒度

**每个 TRL optimizer step 递增 1 次（非 micro-batch 级别）。**

`_reward_step` 在 `_DCRewardCallable.__call__`（line 192）中递增。该 callable 被 TRL GRPOTrainer 每个 training step 调用一次。

证据：log 中 `reward/r1_mean` 出现 772 次 + 前 10 步特殊格式 ≈ 782 次 reward 计算，TRL 从 step 500 resume 到 1273 = 773 步。基本吻合（差异来自 tail 截断时训练仍在继续）。

### 2. Recalibration 实际触发次数

**只触发了 1 次**，在 `_reward_step=500`（对应 TRL step ~1000）：

```
18:04:30 [RECALIB step 500] Starting direction recalibration...
18:04:30 [RECALIB step 500] Loaded 362 calibration records
18:04:39 [RECALIB step 500] cosine_sim=0.6695, auroc=0.8152, direction_norm=79.1360
```

下一次 recalibration 将在 `_reward_step=1000`（TRL step ~1500）时触发。当前 TRL step 1273，还没到。

### 3. Bug 确认及根因

**确认有 bug。**

根因：**`_reward_step` 在 checkpoint resume 时不会恢复，硬编码重置为 0。**

调用链：

1. `run_exp002v2_dcgrpo_cosine.py` line 最后：`trainer.train(resume_from_checkpoint="checkpoint-500")` 从 TRL step 500 恢复
2. HF Trainer 正确恢复了 `state.global_step=500`（进度条从 `501/8000` 开始）
3. 但 `DCGRPOTrainer.__init__` line 282：`self._reward_step: int = 0` 不是 Trainer state 的一部分，没有持久化逻辑（grep `save_state`/`load_state`/`state_dict` 均无匹配）
4. 结果：`_reward_step` 从 0 重新开始，与 TRL global_step 有 500 的偏移
5. 用户设置 `recalibration_interval=500`，期望 TRL step 500、1000、1500 触发
6. 实际：resume 后 `_reward_step=500` 对应 TRL step 1000 才触发第一次，`_reward_step=1000` 对应 TRL step 1500 才触发第二次

**对 exp-002v3 的影响**：如果 exp-002v3 从头训练（不 resume），bug 不会出现。但一旦中途 resume，recalibration 计数会重置偏移。

### 4. 修复建议

**方案 A（推荐，最小改动）**：用 Trainer 的 `global_step` 替代 `_reward_step` 做 recalibration 判断。

`dcgrpo_trainer.py` lines 192-198，改为：

```python
t._reward_step += 1

# Use Trainer's global_step for recalibration check (survives resume)
recalib_check = t.state.global_step + 1  # +1: global_step hasn't incremented yet for current step
if (t._recalibration_interval > 0
        and recalib_check > 0
        and recalib_check % t._recalibration_interval == 0):
    t.recalibrate_direction(recalib_check)
```

`t.state.global_step` 由 HF Trainer 管理，resume 时正确恢复。`+1` 是因为 reward 计算在 optimizer step 之前执行，此时 `global_step` 还是上一步的值。

**方案 B**：在 resume 时同步 `_reward_step`。在 trainer 初始化后、训练循环开始前，检测 resume 并设置 `_reward_step = self.state.global_step`。需要 hook 进 HF Trainer 的 resume 流程，改动更大。

**对当前 exp-002v2-recalib 的影响**：step 1000 的 recalibration 延迟到 TRL step 1500 才触发（延迟 ~500 步 / ~2.5 小时）。不会导致训练失败，但 recalibration 频率低于预期。

---
