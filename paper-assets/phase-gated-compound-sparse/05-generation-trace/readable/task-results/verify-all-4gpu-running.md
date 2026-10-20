# verify all 4gpu running

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_all-4gpu-running_20260514T022000_result.json`
- **Structured JSON:** [`26f87c5f6fa5a3259ded.json`](../../sessions/26/26f87c5f6fa5a3259ded.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常运行。

## 状态汇总

| GPU | 实验 | PID | Memory | Util | 进度 | Masking |
|-----|------|-----|--------|------|------|---------|
| cuda:0 | mvp_v5_fixed_s020_r2 | 51024 | 30829 MiB | 74% | **16/50** | importance |
| cuda:1 | mvp_v5_fixed_s030_r2 | 51161 | 30829 MiB | 78% | **16/50** | importance |
| cuda:2 | mvp_v5_random_s015 | 51961 | 18971 MiB | 88% | **3/50** | random |
| cuda:3 | mvp_v5_random_s025 | 52103 | 18971 MiB | 96% | **3/50** | random |

## 关键确认

- **NaN skip 生效**: importance 实验日志中有 `Skipped 1 NaN attention layers: [27]`，layer 27 被正确跳过
- **4 个 tmux session 均存在**: mvp_v5_fixed_s020_r2, mvp_v5_fixed_s030_r2, mvp_v5_random_s015, mvp_v5_random_s025
- **无异常**: 所有实验正常推进，phase boundary 检测正常工作
- importance 实验启动更早 (10:12)，random 实验稍晚 (10:19)，进度差符合预期

---
