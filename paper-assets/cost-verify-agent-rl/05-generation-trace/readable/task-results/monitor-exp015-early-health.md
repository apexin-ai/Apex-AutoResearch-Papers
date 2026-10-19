# monitor exp015 early health

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp015-early-health_20260514T125820_result.json`
- **Structured JSON:** [`7dde0aa42fdeef33c567.json`](../../sessions/7d/7dde0aa42fdeef33c567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp015 早期健康检查报告

### 状态总结

| 项目 | 状态 |
|------|------|
| **进程** | 存活 (PID 334692, 运行 ~6 分钟, 状态 Ss+) |
| **GPU 0** | 50% 利用率, 41717/97887 MiB (43%) |
| **GPU 1** | 100% 利用率, 41721/97887 MiB (43%) |
| **日志行数** | 1629 行 |
| **当前阶段** | 刚进入训练循环 — "Training Progress: 0/30" |
| **错误/OOM** | 无 |

### 已完成

- Ray 启动成功，Worker (338194, 338195) 和 TaskRunner (337970) 正常
- Qwen3 1.72B 模型加载成功 (safetensors, 1/1 shard)
- FSDP 初始化完成 (bfloat16)
- 数据处理完成: 训练集 8810 条, 验证集 494 条
- 配置确认: LR=1e-7, kl_loss_coef=0.1, grad_clip=1.0, total_steps=30

### 待确认

- **val→train 过渡尚未发生** — 训练进度条刚出现在 0/30，第一个 step（含 validation rollout）正在执行中
- 目前无 reward/loss metrics 输出

### 建议

训练刚进入第一步，validation rollout 可能需要 5-10 分钟。建议 **5 分钟后再次检查** 日志尾部，确认：
1. val metrics 是否输出
2. val→train 过渡是否成功（这是 exp013e 崩溃点）
3. 第一步 training metrics

---
