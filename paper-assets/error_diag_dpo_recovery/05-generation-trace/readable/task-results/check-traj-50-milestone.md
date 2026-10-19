# check traj 50 milestone

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_traj-50-milestone_20260512T131441_result.json`
- **Structured JSON:** [`c87e49c0fcf837b78579.json`](../../sessions/c8/c87e49c0fcf837b78579.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**轨迹收集进度报告：**

| 项目 | 状态 |
|------|------|
| **总轨迹数** | 48 条（part0: 24, part1: 24） |
| **进度** | 各 24/500，约 4.8% |
| **traj_p0** | 存活，screen + python 进程均在 |
| **traj_p1** | 存活，screen + python 进程均在 |
| **速度** | 每条约 70-95 秒，预计每分片 ~500×80s ≈ 11 小时完成 |
| **成功率** | 目前 0/24（两个分片均无成功轨迹） |

**GPU 状态：**

| GPU | 显存占用 | 利用率 | 备注 |
|-----|---------|--------|------|
| 0 | 7763 MiB | 35% | traj_p0（CUDA_VISIBLE_DEVICES=0） |
| 1 | 7763 MiB | 41% | traj_p1（CUDA_VISIBLE_DEVICES=1） |
| 2 | 22099 MiB | 100% | 其他项目（structfuse 训练） |
| 3 | 0 MiB | 0% | 空闲 |
| 4 | 8159 MiB | 100% | 其他项目 |
| 5 | 18736 MiB | 100% | 其他项目 |

**注意**：24 条轨迹成功率 0%，全部 reward=False。可能需要关注模型在 ALFWorld 上的表现是否符合预期——如果 Qwen3-8B zero-shot 本身在这些任务上成功率极低，后续收集到的轨迹可能全是失败轨迹。

---
