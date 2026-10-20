# ops gpu check recovery eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-recovery-eval_20260514T181820_result.json`
- **Structured JSON:** [`f4c0624dc26ae7fb1778.json`](../../sessions/f4/f4c0624dc26ae7fb1778.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 seed=42 checkpoint 已就绪。现在汇总状态。

---

## GPU 状态报告

| GPU | 实验 | 进度 | Loss | 剩余时间 |
|-----|------|------|------|----------|
| cuda:0 | v4-vanilla-seed0 | 1005/1635 (61%) | 0.407 | **~22 min** |
| cuda:1 | v4-taxei-seed0 | 1095/3387 (32%) | 0.367 | ~1h 15m |
| cuda:2 | v4-random-seed0 | 1090/3387 (32%) | 0.434 | ~1h 15m |
| cuda:3 | v4-vanilla-seed7 | 559/1635 (34%) | 0.449 | **~39 min** |

**4 块 GPU 全部在训练，当前无空闲 GPU。**

### v4-vanilla-seed0 / seed7 状态
- 都仍在训练中（非已完成）。Registry 显示 cron 未找到可能是因为 cron 监控脚本断了，但进程还在跑。
- seed0 已过 epoch 1 checkpoint（checkpoint-545 已保存），当前 epoch 1.84
- seed7 刚到 epoch 1.0

### Recovery Eval 准备情况
- 脚本 `run_injected_eval.sh` 就绪
- seed=42 的 3 个 final checkpoint 全部存在：
  - taxei: `checkpoint-3387`
  - random: `checkpoint-3387`
  - vanilla: `checkpoint-1635`
- `eval/injected_eval.py` 就绪

### 计划
GPU 0 将最先释放（~22 min），然后 GPU 3（~39 min）。Recovery eval 脚本默认 3 个 variant 分别占 GPU 0/1/2 并行跑，但 GPU 1/2 要 1h15m 后才空。

**两个方案：**
1. **等 GPU 0 空闲后逐个跑**：先在 GPU 0 跑 taxei eval，GPU 3 空闲后跑 vanilla eval，最后 GPU 1 或 2 空闲跑 random eval
2. **等 ~1h15m 所有 GPU 空闲后用 `all` 模式 3 个并行跑**

方案 1 更快拿到前两个结果。需要我设置监控、在 GPU 空闲时自动启动吗？

---
