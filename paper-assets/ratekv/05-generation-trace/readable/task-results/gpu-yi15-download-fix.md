# gpu yi15 download fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_yi15_download_fix_20260514T153307_result.json`
- **Structured JSON:** [`28ce0368562523ecbdd3.json`](../../sessions/28/28ce0368562523ecbdd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**现状总结：无需手动干预，系统会自动恢复。**

| 项目 | 状态 |
|------|------|
| **shard 002** | 已完成 (4.98 GB) |
| **shard 004** | 已完成 (2.78 GB) |
| **shard 001** | 下载中 75% (3.46G/4.59G)，ETA ~35 min |
| **shard 003** | 下载中 83% (3.84G/4.63G)，ETA ~24 min |
| **下载进程** | PID 228878，ModelScope，速度 ~580 kB/s |
| **wait 脚本** | PID 233159，每 60 秒轮询，当前检测到 2/4 shards |
| **模型路径** | `/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B` |

**自动恢复链**：
1. ModelScope 下载完成后会将 shard 001、003 从 `._____temp/` 移到最终目录
2. `wait_and_run_yi15_v2.sh` 检测到 4/4 shards 且文件大小稳定后，自动执行 `CUDA_VISIBLE_DEVICES=1 python -u run_yi15_full_pipeline.py --model /root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B --gpu cuda:0`
3. Pipeline 通过 `--model` 参数接收路径，无需修改脚本

预计 **~35 分钟后**下载完成，再等 ~2 分钟 wait 脚本确认稳定，pipeline 自动启动。

---
