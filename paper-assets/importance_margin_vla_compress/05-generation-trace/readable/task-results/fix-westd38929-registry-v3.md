# fix westd38929 registry v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd38929_registry_v3_20260525T053412_result.json`
- **Structured JSON:** [`b643030a48e3f3c4c8db.json`](../../sessions/b6/b643030a48e3f3c4c8db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部修复完成。汇总：

## Registry 修复结果

| 实验 ID | PID | GPU | 利用率 | 进度 | Registry |
|---------|-----|-----|--------|------|----------|
| `eval_openvla_attn_k09_long_seed42_v3` | 2508 | cuda:0 | 82% | 40/50 ep, sr=22/40 (55%) | ✅ RUNNING |
| `eval_openvla_attn_k085_long_seed42_v3` | 2583 | cuda:1 | 62% | 40/50 ep, sr=26/40 (65%) | ✅ RUNNING |
| `eval_openvla_random_k09_long_seed42_v3` | 2763 | cuda:2 | 73% | 40/50 ep, sr=26/40 (65%) | ✅ RUNNING |
| `eval_openvla_l2norm_k09_long_seed42_v3` | 2944 | cuda:3 | 66% | 40/50 ep, sr=29/40 (72.5%) | ✅ RUNNING |

- 4 个 PID 全部存活，状态 `Rl+`（运行中），约 ~1.0 eps/min
- 4 张卡均在使用，GPU 利用率 62-82%，每张卡占用 ~16GB 显存
- 日志显示全部在正常推进（40/50 episodes），无 hang
- Registry 通过 DONE→PREPARING→QUEUED→RUNNING 三步转换成功恢复
- 预计剩余 ~10 分钟完成（10 episodes × ~1 ep/min）

---
