# diag d134 4b random b01 s48

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_d134-4b-random-b01-s48_20260518T200431_result.json`
- **Structured JSON:** [`7a705fe6374d2b264271.json`](../../sessions/7a/7a705fe6374d2b264271.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 结论：实验成功完成，cron 误判为失败

**失败原因：假阳性。** 训练使用了 `--no_wandb`，cron 检测逻辑依赖 W&B metrics 或 sentinel 文件判断进程存活。进程正常退出后，cron 看到 "process dead + no W&B" → 自动标记为 failed。

### 实际运行情况

| 阶段 | 状态 | 详情 |
|------|------|------|
| 训练 | 500/500 步完成 | 耗时 1h30m，final reward: prove_rate=0.5855, mean_isr=0.0994 |
| Eval | 完成 | 93/100 proved (93%), ISR=0.0625 |
| Classify | 完成 | genuine_rate=4.3%, h1_strict=80.6%, h8=15.1% |

### 环境状态

- **磁盘**：41G/250G 已用 (17%)，充裕
- **safetensors 文件**：不在输出目录中（可能被 pipeline 清理或保存在别处）
- **残留进程**：无法通过 read-only 检查，但训练日志显示正常退出（"Done."）

### 建议

1. 在 registry 中将 d134-4b-random-b01-s48 的状态从 failed 修正为 success
2. eval 和 classify 结果已生成，数据可直接使用
3. 如果需要 checkpoint 用于后续分析，确认 safetensors 是否被 pipeline 删除——如果是，需要记录这个行为；如果需要权重则需重训

---
