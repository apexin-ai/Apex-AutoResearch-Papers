# ops pi05 precompute check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pi05-precompute-check_20260524T054606_result.json`
- **Structured JSON:** [`cd08ce558f61b5eed575.json`](../../sessions/cd/cd08ce558f61b5eed575.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 π0.5 precompute 状态汇报

### 进程存活
- **object (pid=113456)**: 运行中，ELAPSED 1d 09:27
- **goal (pid=114159)**: 运行中，ELAPSED 1d 09:26
- **long (pid=114507)**: 运行中，ELAPSED 1d 09:25
- **spatial**: **没死，是完成了** ✅ — 不需要重启

### Spatial 完成证据
`/root/autodl-tmp/crm_cache_pi05_2048/spatial/` 已生成最终 merge 输出（precompute 流水线终点）：
- `obs_features.pt` (494 MB) — 2026-05-24 13:32:50 创建
- `k_samples.pt` (72 MB) — 同一时刻
- `expert_actions.pt` (7 MB) — 同一时刻

外加 partial_s0_0_500 → partial_s0_60000_60250 完整覆盖 60250 个样本（spatial benchmark 数据量比 object/goal/long 小，所以最先跑完）。

reconcile_crons 的 "miss 3/5" 是 **false alarm**：cron 周期检测预期进程仍在跑，但 spatial 因数据量小已早于其它三个 benchmark 完成并正常退出。

### Cache 数据量
| benchmark | size | partial files | merge files | status |
|-----------|------|---------------|-------------|--------|
| spatial   | 1.1G | s0_0 → s0_60000_60250 (~120) | ✅ 全部 | **完成** |
| object    | 582M | s0_0 → s0_63500_64000 (~128) | ❌ | 运行中 |
| goal      | 550M | s0_0 → s0_60000_60500 (~121) | ❌ | 运行中 |
| long      | 563M | s0_0 → s0_61500_62000 (~124) | ❌ | 运行中 |

### GPU/磁盘
- GPU 0 (object): 9.8 GB / 24 GB, 27%
- GPU 1 (spatial): 0 MiB（已释放，符合完成状态）
- GPU 2 (goal): 9.8 GB / 24 GB, 24%
- GPU 3 (long): 9.8 GB / 24 GB, 23%
- 磁盘 `/root/autodl-tmp`: 196G / 250G 已用（**79%**），剩余 55G — 够其它三个跑完，但收尾时要警惕

### 建议
- **不要重启 spatial** — 已完成，merge 文件齐全
- 在 cron 配置里删除 spatial 这条监控，否则会一直 miss
- object/goal/long 按当前 1.87 s/sample 估算还需 ~几小时即可完成

---
