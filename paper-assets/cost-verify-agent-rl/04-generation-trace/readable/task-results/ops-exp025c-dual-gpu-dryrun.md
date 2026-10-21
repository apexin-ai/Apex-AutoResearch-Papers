# ops exp025c dual gpu dryrun

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp025c_dual_gpu_dryrun_20260515T081352_result.json`
- **Structured JSON:** [`cf57a4efdc2a6489d3af.json`](../../sessions/cf/cf57a4efdc2a6489d3af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Ray 已停止（74/75 进程）。现在汇报结果。

---

## 结果报告

```
PID peak: 5505 / 20480 (27%)
PID baseline: 711
PID samples (内置监控, 每10秒):
  t=0s:    714
  t=10s:   5504  (Ray workers 启动后)
  t=20s~8min: 5504 ±1 (完全稳定，无波动)

Status: Ray 资源调度卡死（非 PID 崩溃，非 EAGAIN）
```

### 关键发现

**PID 完全安全** — 峰值仅 5505/20480 (27%)，从未接近上限。线程压缩 env vars 有效。

**但进程卡死在 Ray 调度**，从未推进到模型加载/训练阶段：
```
Warning: resource request cannot be scheduled: {'CPU': 2.0, 'GPU': 2.0}
Warning: resource request cannot be scheduled: {'CPU': 0.1}
All cluster resources being claimed by actors.
```

**原因**：`ray_init.num_cpus=8` 太少。Ray 启动了 112 个 Python worker 进程（预启动 + TaskRunner），占满了 8 个 CPU slot，导致 colocated worker（需要 2 CPU + 2 GPU）和 env worker（需要 0.1 CPU）无法被调度。

### ⚠️ 重要 caveat

本次 dry run **未能到达模型加载和 vLLM 推理阶段**，所以 5505 只是 Ray 初始化的 PID 数量。实际训练时 vLLM + FSDP 会增加更多线程，但基于 exp025c（单 GPU）成功经验 + 本次 27% 的基线，预计双 GPU 总 PID 仍有很大余量。

### 下一步建议

增大 `ray_init.num_cpus`（比如 16 或更高），或确认服务器实际 CPU 核数后设为匹配值，解决 Ray 调度问题后才能看到完整训练阶段的 PID 数据。

---
