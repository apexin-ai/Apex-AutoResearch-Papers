# ops kill pipeline auto setup monitor

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-pipeline-auto-setup-monitor_20260521T172634_result.json`
- **Structured JSON:** [`ca742c798a2dd910b326.json`](../../sessions/ca/ca742c798a2dd910b326.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pipeline-Auto Kill 结果
- **PID 790737 状态**：already dead（kill 返回 "No such process"，无任何 pipeline/auto/monitor 进程残留）
- **是否有 premature merge 发生**：**否**。bjb1-18228 上：
  - `object/` 目录为空（no partials, no merged）
  - `spatial/` 只有本地 s6 的 14 个 partial（正常）
  - 全集群无 `rsync` / `merge_*.pt` 文件
  - 无 cron / at job

## Precompute 进度

| 服务器 | Shard | 进度 | ETA |
|---|---|---|---|
| bjb1-18228 | spatial s6 | 7000/8607 (81%) | ~50 min |
| bjb2-28827 | spatial s0 | 5800/8608 (67%) | ~114 min |
| bjb2-28827 | spatial s1 | 5800/8607 (67%) | ~106 min |
| bjb2-28827 | spatial s2 | 5900/8607 (69%) | ~100 min |
| bjb2-28827 | spatial s3 | 5700/8607 (66%) | ~110 min |
| bjb2-28827 | spatial s4 | 5900/8607 (69%) | ~100 min |
| bjb2-28827 | spatial s5 | 5700/8607 (66%) | ~112 min |
| bjb2-40593 | object s0 | 5400/7251 (74%) | ~104 min |
| bjb1-32546 | object s1 | 5100/7251 (70%) | ~77 min |
| bjb1-32546 | object s2 | 5900/7251 (81%) | ~43 min |
| bjb1-32546 | object s3 | 5700/7251 (79%) | ~50 min |
| bjb1-32546 | object s4 | 5400/7251 (74%) | ~63 min |
| bjb1-32546 | object s5 | 6100/7251 (84%) | ~37 min |
| bjb1-32546 | object s6 | 6100/7251 (84%) | ~36 min |
| bjb1-32546 | object s7 | 6100/7250 (84%) | ~37 min |
| bjb1-32546 | object s8 | 6300/7250 (87%) | ~30 min |
| bjb1-32546 | object s9 | 6100/7250 (84%) | ~38 min |

全 17 个 shard 进程都在运行（核对 `shard_id` 集合 = {0..9} object + {0..6} spatial），无失败 / 无重启中。

## 建议
1. **必须手动 merge**。bjb1-18228 上只有本地 spatial s6，其它 16 个 shard 都在远端。等所有 shard 跑完后需要：
   - `rsync` object s0 partials：`bjb2-40593` → `bjb1-18228`
   - `rsync` object s1-s9 partials：`bjb1-32546` → `bjb1-18228`
   - `rsync` spatial s0-s5 partials：`bjb2-28827` → `bjb1-18228`
   - 再跑 merge 脚本
2. **预计全部完成时间**：~**2 小时**（瓶颈为 bjb2-28827 上的 spatial s0/s3/s5，约 110-114 min）。
3. **注意 chunk size 不一致**：s5/s7/s8/s9 用 `--save_every 100`（每个 shard ~73 个 partial），其余用默认 500（~15 个 partial）。merge 脚本若假设固定 chunk size 需要检查。
4. **磁盘充裕**：bjb1-32546 和 bjb2-28827 均为 51G/250G (21% 占用)，空间足够。

---
