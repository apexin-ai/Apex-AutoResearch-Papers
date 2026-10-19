# π0.5 CRM Precompute Status Check — 2026-05-21 16:43 UTC

## 概览
- **总 shard 数**: 17 (Object 10 + Spatial 7)
- **当前运行中**: 16 train_crm 进程
- **已完成 shard 输出文件 (merged)**: 0 (没有任何 obs_features.pt / k_samples.pt / expert_actions.pt / manifest.json)
- **pipeline-auto 状态**: ⚠️ **运行中但远程轮询逻辑坏了**（详见末尾）

## bjb1-32546 — Object shards 1-9 (6 GPU)

进程: 9 个 train_crm 进程在跑（s1-r2, s2-r2, s3-r2, s4-r2, s5-fix, s6-r2, s7-fix, s8-fix, s9-fix），目录有 255 个 partial 文件。

| Shard | 状态 | 进度 (samples/7251) | 备注 |
|-------|------|---------|------|
| s1-r2 | 运行 | 3800 (52%) | ETA ~2.1h |
| s2-r2 | 运行 | 4400 (61%) | ETA ~1.5h |
| s3-r2 | 运行 | 4300 (59%) | ETA ~1.6h |
| s4-r2 | 运行 | 4000 (55%) | ETA ~1.9h |
| s5 | s5-r2 Terminated EC=143 → s5-fix 接管 4700 (65%), ETA ~1.4h |
| s6-r2 | 运行 | 4700 (65%) | ETA ~1.4h (s6-fix Terminated EC=143 但 r2 在跑) |
| s7 | s7-r2 (bjb1-18228) Terminated EC=143 → s7-fix 接管 (本机) 4700 (65%), ETA ~1.4h |
| s8 | s8-r2 (bjb1-18228) Terminated EC=143 → s8-fix 接管 (本机) 4800 (66%), ETA ~1.3h |
| s9 | s9-r2 (bjb1-18228) Terminated EC=143 → s9-fix 接管 (本机) 4700 (65%), ETA ~1.4h |

## bjb2-40593 — Object shard 0 (1 GPU)

- **正确运行的进程**: PID 872656, 138% CPU, 368 min runtime
- **实际活跃日志**: `/root/precompute_pi05_shard0.log`（**不是** `~/runs/.../precompute-pi05-shard0.log`，那个是旧 attempt）
- **进度**: 4600/7251 (63%), 3.35s/sample, ETA ~2.5h（比其他 shard 慢约 1.7×）
- **失败 attempts**:
  - `precompute-pi05-obj-s0-r2.log`: CUDA OOM EXIT_CODE=1（GPU 23.5GB 显存被其他进程占满了，留 4MB）
  - `precompute-pi05-shard0.log` (~/runs/): Terminated EXIT_CODE=129 (SIGHUP)
- **当前显存**: 9839/24564 MiB 健康
- **partials**: 48 个 partial_s0_*.pt 文件

## bjb2-28827 — Spatial shard 0-5 (6 GPU)

进程: 6 个 train_crm 进程全部健康运行。

| Shard | 进度 (samples/8607) | 速度 | ETA |
|-------|---------|------|-----|
| s0 | 4600 (53%) | 2.27s/sample | ~2.5h |
| s1 | 4600 (53%) | 2.26s/sample | ~2.5h |
| s2 | 4600 (53%) | 2.23s/sample | ~2.5h |
| s3 | 4500 (52%) | 2.28s/sample | ~2.6h |
| s4 | 4700 (55%) | 2.21s/sample | ~2.4h |
| s5 | 4500 (52%) | 2.31s/sample | ~2.6h |

## bjb1-18228 — Spatial shard 6 + pipeline-auto + (旧 Object s7-9)

- **Spatial shard 6**: 运行中, 5500/8607 (64%), 1.88s/sample, **ETA ~1.6h**（进度最快）
- **Object s7/s8/s9-r2**: **全部 Terminated EC=143** ——已迁移到 bjb1-32546 上的 -fix 进程
- **存储 (rsync target)**: object/ 217 partials, spatial/ 11 partials, 无 merged 文件

## pipeline-auto 关键问题 ⚠️

```
[pipeline] Fri May 22 00:37:33 CST 2026: precompute processes remaining: bjb1-32546=0 bjb2-40593=0 bjb2-28827=0 local=4 total=4
[pipeline] Fri May 22 00:42:34 CST 2026: precompute processes remaining: bjb1-32546=0 bjb2-40593=0 bjb2-28827=0 local=4 total=4
```

- 进程**存活**（log 在按 5 分钟间隔更新到 00:42）
- **但 SSH 远程进程探测全部返回 0**——bjb1-32546 实际 9 个进程, bjb2-40593 1 个, bjb2-28827 6 个, 都被识别成 0
- `local=4` 反映本机 spatial shard6 的进程树（tmux+bash+timeout+python = 4 个）
- **风险**: 当 spatial shard6 完成后, local=0, remote=0 (假) → total=0 → 触发**早 merge**, 而其他 16 个 shard 还没完
- **必须修**: 检查 pipeline 脚本里的 ssh 探测命令（可能 ssh 鉴权失败、远程命令 quoting 问题、或 server 名称不匹配）

## 总结

| 类别 | 数量 |
|------|------|
| 运行中 shard 进程 | 16 (Object 10 + Spatial 7) |
| 失败/已 terminated 但已迁移的旧 attempt | 7 (s0-r2 OOM, s0-shard0 SIGHUP, s5-r2, s6-fix, s7-r2, s8-r2, s9-r2 全是 SIGTERM) |
| 完成的 shard | 0 |
| Merged 输出文件 | 0 |
| Object partials (bjb1-32546 源) | 255 |
| Object partials (bjb1-18228 rsync 目标) | 217 (落后源 ~38) |
| Spatial partials (bjb1-18228) | 11 |

**预计完成时间**: 最慢的是 bjb2-40593 obj s0 (~2.5h) 和 bjb2-28827 spatial s0-s5 (~2.5h), 再加 rsync 同步时间, 预计 **2.5-3h 内全部 shard 完成**。

**立即行动项**:
1. 修复 pipeline-auto 的远程 SSH 探测逻辑，否则有早 merge 风险
2. 确认 bjb1-18228 → bjb1-32546 的 partial 文件 rsync 在跑（255 vs 217 差 38 个）
3. bjb2-40593 shard0 实际日志路径是 `/root/precompute_pi05_shard0.log`，需要同步到 bjb1-18228 merge 目录
