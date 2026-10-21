# diagnose exec only s45 1000step

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exec-only-s45-1000step_20260522T021328_result.json`
- **Structured JSON:** [`d987ca0498fb585be8db.json`](../../sessions/d9/d987ca0498fb585be8db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验 `exec-only-s45-1000step` 实际上已成功完成，cron 报告是误报。**

### 详情

| 项目 | 状态 |
|------|------|
| **训练进度** | 1000/1000 步全部完成，耗时 2h 15m 39s |
| **最终指标** | parse_rate=1.0, prove_rate=0.1495, mean_isr=0.0734 |
| **模型保存** | `/root/autodl-tmp/outputs/exec_only_s45_1000_k4/` — 模型文件完整（~7.5GB safetensors） |
| **checkpoint** | checkpoint-1000 存在 |
| **eval_sta** | 已运行，`eval_sta.json` 和 `classify.json` 已生成（10:07） |
| **磁盘** | 数据盘 4% 使用，无压力 |
| **GPU** | cuda:0 上仍有一个 python 进程 (PID 946257, 8560MiB)——可能是 eval 后残留 |

### 失败根因

**不是真正的失败。** 训练在 09:59:42 正常完成并输出 `INFO Done.`，但 cron 监控在进程退出后找不到 sentinel 文件或 W&B run，因此误判为 "process dead"。这是 cron 监控逻辑的假阳性。

### 建议

1. **无需重训**——模型和 eval 结果都已完整保存
2. 手动将 registry 状态更新为 `conclusion=success`
3. GPU 0 上的残留进程 (PID 946257) 需要确认是否可以清理（C007 约束）
4. 如果后续 exec-only 系列都走同一训练脚本，可考虑在训练完成后写一个 sentinel 文件（如 `touch $OUTPUT_DIR/.done`）避免 cron 误报

---
