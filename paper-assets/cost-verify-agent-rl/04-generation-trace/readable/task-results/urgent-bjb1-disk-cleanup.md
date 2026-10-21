# urgent bjb1 disk cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_bjb1_disk_cleanup_20260521T163507_result.json`
- **Structured JSON:** [`f95ecb8acd0bd050324a.json`](../../sessions/f9/f95ecb8acd0bd050324a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志文件自 00:36:19 后没有任何新输出（文件大小不变）。进程还活着但实验已经卡死——初始化阶段被磁盘满中断后没有自动恢复。需要重新提交。

```
清理前: 9.6 GB 可用 (97% 占用)
已删除:
  - /root/autodl-tmp/checkpoints/exp029-seed3/     21 GB  (seed 3 已完成, 仅中间 step 5)
  - /root/autodl-tmp/checkpoints/exp029/            21 GB  (seed 1 已完成, OOD eval 已跑)
  - /root/autodl-tmp/checkpoints/exp029_hf/         3.8 GB (seed 1 HF 格式, 不再需要)
  - /root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/  31 GB  (旧版 SFT v1, 已被 exp021_ragen_sft_v4 取代)
清理后: 85 GB 可用 (67% 占用, 释放了 ~75 GB)

保留:
  - exp021_ragen_sft_v4/   23 GB  (SFT base model)
  - exp029-seed4/          21 GB  (global_step_15, 需做 OOD eval)
  - exp029-seed7-high-kl/  0 GB   (空目录)
  - scienceworld_sft/      7.6 GB

high_kl 实验: 进程存活但卡死，日志自 00:36 停止更新，需要 kill 后重新提交。
```

---
