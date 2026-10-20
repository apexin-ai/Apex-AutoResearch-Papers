# infra investigate vanilla s2 status

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_investigate_vanilla_s2_status_20260521T004423_result.json`
- **Structured JSON:** [`8d7c45cccf56fc73673b.json`](../../sessions/8d/8d7c45cccf56fc73673b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查结果汇总：

- **PID 225562**: 已死亡，进程正常退出
- **实际训练状态**: **已完成** — `train_resume2.log` 显示 "Max step 50005 reached! Stopping training..." 于 08:33:53 UTC May 21
- **50000_chkpt**: **存在**，08:34 UTC May 21 创建
- **checkpoint 列表**:
  - `30000_chkpt` (May 21 01:58)
  - `35000_chkpt` (May 21 04:40)
  - `40000_chkpt` (May 21 05:59)
  - `45000_chkpt` (May 21 07:16)
  - `50000_chkpt` (May 21 08:34)
- **auto-eval**: **未触发** — 无 `.launched_*` 或 `.done_*` 文件，无 monitor_and_eval 进程在运行
- **GPU 状态**: 全部空闲，无计算进程

**矛盾解释**: 另一个 Worker 看到 "从 step 0 重跑, step ~13487" 是因为 `train_resume2.log` 的 progress bar 使用**相对 step 计数**（从 resume 点 35000 开始计为 0）。实际是从 35000_chkpt resume 正常运行，relative step 15006 = absolute step 50006 ≥ 50005，正常完成。

**建议**: vanilla_s2 训练已成功完成，需要启动 auto-eval 评估 50000_chkpt。

---
