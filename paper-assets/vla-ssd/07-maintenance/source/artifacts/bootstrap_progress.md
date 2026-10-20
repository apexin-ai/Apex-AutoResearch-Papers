# Clustered Bootstrap Progress Report

**检查时间**: 2026-05-23 ~07:02 CST (batch 启动于 04:20 CST, 已运行 ~2h40m)

## cuda:0 — OpenVLA(8) + NORA(4) = 12 conditions

**进度: 8/12 done, 当前跑 #9 (nora/goal/trained)**

| # | Condition | 开始 | 完成 | 耗时 |
|---|-----------|------|------|------|
| 1 | openvla/goal/trained | 04:20 | 04:37 | 17min |
| 2 | openvla/goal/untrained | 04:37 | 05:02 | 24min |
| 3 | openvla/spatial/trained | 05:02 | 05:19 | 18min |
| 4 | openvla/spatial/untrained | 05:20 | 05:37 | 17min |
| 5 | openvla/object/trained | 05:37 | 06:00 | 24min |
| 6 | openvla/object/untrained | 06:00 | 06:25 | 24min |
| 7 | openvla/long/trained | 06:25 | 06:42 | 17min |
| 8 | openvla/long/untrained | 06:42 | 07:00 | 18min |
| 9 | nora/goal/trained | 07:00 | ... | extraction ~50% (2400/5000) |
| 10-12 | nora remaining 3 | — | — | — |

**ETA**: OpenVLA avg ~20min/condition. NORA 还剩 ~3.5 conditions → **~70min → ~08:15 CST**

## cuda:1 — TracVLA = 8 conditions

**进度: 3/8 done, 当前跑 #4 (tracvla/spatial/untrained, fitting 阶段)**

| # | Condition | 开始 | 完成 | 耗时 |
|---|-----------|------|------|------|
| 1 | tracvla/goal/trained | 04:20 | 04:47 | 27min |
| 2 | tracvla/goal/untrained | 04:47 | 05:48 | 61min |
| 3 | tracvla/spatial/trained | 05:48 | 06:14 | 26min |
| 4 | tracvla/spatial/untrained | 06:14 | ... | extraction done (2336s), now fitting RidgeCV |
| 5-8 | object + long (trained/untrained) | — | — | — |

**注意**: TracVLA untrained 比 trained 慢很多（goal: 61min vs 27min），可能因为 untrained 模型表征方差大导致 extraction 更慢。

**ETA**: trained ~27min, untrained ~50min avg. 还剩 ~4.5 conditions → **~150min → ~09:30 CST**

## 已生成结果文件

### bootstrap_r2/ (当前运行产出)
- `openvla_goal/trained.json` + `untrained.json` ✅
- `openvla_spatial/trained.json` + `untrained.json` ✅
- `openvla_object/trained.json` + `untrained.json` ✅
- `openvla_long/trained.json` + `untrained.json` ✅
- `tracvla_goal/trained.json` + `untrained.json` ✅
- `tracvla_spatial/trained.json` (untrained in progress)

### clustered_bootstrap/ (旧目录，仅1个文件)
- `openvla_goal/trained.json` (May 23 04:19, 在当前 batch 之前生成)
- `openvla_long/` — 空
- `tracvla_long/` — 空

## 异常/警告
- **无错误**。日志中只有 transformers 版本 deprecation warnings（预期行为）。
- TracVLA untrained conditions 耗时是 trained 的 2x，cuda:1 是瓶颈。
- cuda:0 预计 ~08:15 完成，cuda:1 预计 ~09:30 完成。**整体预计 09:30 CST 全部完成。**
