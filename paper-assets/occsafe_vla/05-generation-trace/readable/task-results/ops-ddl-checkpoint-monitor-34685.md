# ops ddl checkpoint monitor 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ddl-checkpoint-monitor-34685_20260528T062936_result.json`
- **Structured JSON:** [`d852f64b7e4377bcec77.json`](../../sessions/d8/d852f64b7e4377bcec77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

---

## 状态汇总

### Checkpoint 进度

| 实验 | GPU | PID | 最新 chkpt | 时间 | 50000_chkpt |
|------|-----|-----|-----------|------|------------|
| detach_ln_v2_s3 | 3 | 56822 | 45000 | 13:15 UTC | 未生成 |
| full_occ_ln_v2_s3 | 2 | 56474 | 45000 | 13:15 UTC | 未生成 |
| detach_ln_v2_s2 | 0 | 47238 | 40000 | 14:16 UTC | 未生成 |
| full_occ_bn_v2_s2 | 1 | 62535 | — | — | （额外实验） |

### 时间估算
- **detach_ln_v2_s3 / full_occ_ln_v2_s3**: 5000 步 ≈ 1h22m（40k→45k 耗时），50000_chkpt 预计 **~14:37 UTC**（约 5-10 分钟内）
- **detach_ln_v2_s2**: 从 25k resume，15000 步耗时 ~4h06m，5000 步 ≈ 82min，50000 预计 **~17:00 UTC**

### 轮询脚本
- 3 个脚本全部存活（PID 69355/69356/69357，已运行 ~7.5 min）
- 路径修复已生效：两个 s3 脚本都检查 `$CHKPT_DIR/lora_adapter/adapter_config.json`
- 日志仅显示 "Polling started"，尚未触发 eval

### GPU 占用
4 张 GPU 全部占满（每张 ~62 GiB）。PID 62535 是 `full_occ_bn_v2_s2` 实验，在 GPU 1 上。

### 结论
- **无需手动干预**。两个 s3 实验的 50000_chkpt 将在 ~5-10 分钟内生成，轮询脚本正常工作，会自动 kill 训练 + 启动 eval。
- detach_ln_v2_s2 距离 50000 还较远（~2.5h），轮询脚本也在监控。
- 注意：eval 启动时需要 GPU，s3 的 eval 会在对应 GPU 上 kill 训练后运行，不冲突。

---
