# ops llama4 arrival watcher

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama4-arrival-watcher_20260521T090124_result.json`
- **Structured JSON:** [`bea9d3f472c2dcea71a2.json`](../../sessions/be/bea9d3f472c2dcea71a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切就绪。汇报：

## 当前状态

| 项目 | 值 |
|------|-----|
| 下载进程 | PID 69801, 已运行 43 分钟 |
| 已完成 shard | 1/14 (model-00003, 4.7G) |
| 正在下载 | 8 个 (model-00001,02,04,05,06,07,08,09) |
| 未开始 | 5 个 (model-00010~00014) |
| 已下载总量 | 21G / ~65G |
| 下载速度 | 1-2.5 MB/s (多线程并发) |

## 已部署

1. **检查脚本**: `/root/xling_calib_direction/scripts/llama4_arrival_check.sh` — 手动运行可随时查状态
2. **后台守护**: `/root/xling_calib_direction/scripts/llama4_watch_daemon.sh` (PID 71779) — 每 5 分钟自动轮询，下载完成后自动执行 shard 验证 + config 解析
3. **日志**: `/tmp/llama4_watch.log` — 查看 daemon 输出；`/tmp/llama4_arrival.log` — 查看验证结果

按当前速度，预估还需 ~1.5-2 小时完成全部 14 shards。完成后 daemon 会自动验证并将结果写入日志。

---
