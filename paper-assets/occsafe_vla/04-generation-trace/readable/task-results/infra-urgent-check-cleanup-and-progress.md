# infra urgent check cleanup and progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent_check_cleanup_and_progress_20260521T000726_result.json`
- **Structured JSON:** [`59e5261f295d79ab272a.json`](../../sessions/59/59e5261f295d79ab272a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685

- **清理脚本: 有 — 已 kill (PID 32353)**
  - `/root/autodl-tmp/cleanup_loop.sh` 每 20 分钟调用 `cleanup_checkpoints.sh`，对 occ_s0/s1/s2 目录仅保留 2 个 `*_chkpt`，删除其余
  - **排序 bug**：`sort -t'-' -k2 -n` 无法按 step 正确排序，实际保留的是最小 step (5000, 7500) 而非最新的
  - cleanup.log 确认：已系统性删除所有三个 seed 的 10000→27500 checkpoints（最后一次 07:56 CST 删了 27500_chkpt，正是 occ_s1 crash 的直接原因）
- **occ_s0: step ~28293/50005 (57%), ETA ~5.5h**
  - checkpoint 仅剩 5000_chkpt + 7500_chkpt（10k-27.5k 全被删）
  - 7500_chkpt 文件完整 (~15GB safetensors + heads)
- **occ_s2: step ~28315/50005 (57%), ETA ~5.5h**
  - checkpoint 仅剩 5000_chkpt + 7500_chkpt（同上）
  - 7500_chkpt 文件完整

## westd-10894

- **vanilla_s2: 训练中 step ~13487/50005 (27%), ETA ~9.3h (~17:48 CST)**
  - 前一轮 run 到 45000 后 crash (exitcode 1)，当前从 step 0 重跑
  - 50000_chkpt 不存在；旧 run checkpoint 留存: 30000, 35000, 40000, 45000
- **auto-eval: 已触发，进行中**
  - monitor_and_eval.sh 运行中 (PID 226828)
  - 正在评估 vanilla_s1 step 45000 (Task 2/10 in progress)
  - vanilla_s1 final (50k) 已完成: **TSR=0.935, CAR=0.765**
- **s0 intermediate eval: 7 个 JSON 结果已生成**
  - vanilla_s0: final, midtrain_20r (35k), step35000
  - vanilla_s1: final, midtrain, step35000, step40000
- **cleanup 进程: 无**

---

**关键风险已解除**：westd-34685 的 cleanup_loop 已 kill。但损失已造成 — occ_s0/s2 丢失了 10k-27.5k 的全部 intermediate checkpoints，仅剩 5000+7500。训练本身仍在正常推进，后续 checkpoint (30000, 32500, ...) 会正常保存。

**vanilla_s2 异常**：不是接近完成而是重跑中 (step 13487)，前一轮 crash 后从头开始。旧 45000 checkpoint 可用但缺 50000。

---
