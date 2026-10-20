# ops scaleup collect launch

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scaleup-collect-launch_20260516T054714_result.json`
- **Structured JSON:** [`fff9250bbf2be2603ac3.json`](../../sessions/ff/fff9250bbf2be2603ac3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## 报告

### 1. Scale-up 数据收集：已成功运行

收集进程（PID 238209）已在运行，是之前 nohup 启动成功的（不是失败）。当前状态：

- **已收集成功轨迹**：4 条（刚启动约 2 分钟）
- **排除的失败 stub**：714 条（上次遗留）
- **采样计划**：2809 games，实际运行 2260 episodes（4 workers 并行）
- **初始成功率**：前 10 条尝试中 4 条成功 → **~40% 成功率**（初始值，随难度分布会变化）
- **overshoot factor**：3.0×（进程已启动，未修改）

**注意**：overshoot factor 当前是 3.0 而非要求的 1.5。因进程已在运行，若需修改需 kill 后重启。当前 3.0× 意味着采样 2809 games（目标 1000 成功），按 40% 成功率估算约可获得 ~900 条，稍有不足但接近目标。是否需要杀掉重启用 1.5×？（1.5× 只采样 1500，按 40% 成功率只能得 ~600 条，反而不够）

### 2. TaxEI-RP 训练进度

| Seed | Step | Total | 剩余时间 | Loss | Epoch |
|------|------|-------|----------|------|-------|
| s42 | 5030 | 5415 | ~16 min | 0.225 | 2.79 |
| s0 | 4940 | 5415 | ~20 min | 0.278 | 2.74 |
| s123 | 5030 | 5415 | ~16 min | 0.264 | 2.79 |
| s1 | 5000 | 5415 | ~17 min | 0.221 | 2.77 |

**4 个训练任务都在 epoch 3 尾声，全部将在 ~20 分钟内完成。** 所有进程运行了约 3.5 小时，状态健康。

### 3. 异常

无异常。API 可达（进程成功获取 completions），训练正常收敛。唯一注意点是 overshoot factor 3.0 vs 要求的 1.5，但 3.0 在当前成功率下实际上更合理——建议保持不动。

---
