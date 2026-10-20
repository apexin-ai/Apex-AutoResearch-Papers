# infra gpu status check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260514T162806_result.json`
- **Structured JSON:** [`01ce11a5dd59ccbeebaf.json`](../../sessions/01/01ce11a5dd59ccbeebaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报：westd-22162 GPU 状态

### GPU 进程分布

| GPU | PID | 实验 | 显存 | 运行时长 | 进度 |
|-----|-----|------|------|----------|------|
| **cuda:0** | 130124 | c2_n500_deepseek (importance, s015) | 30,062 MiB | 2h47m | **301/500 (60%)** |
| **cuda:1** | 130263 | c2_n500_deepseek (random, s015) | 33,910 MiB | 2h47m | **321/500 (64%)** |
| **cuda:2** | 131864 | c2_qw_n500 (importance, s015) | 30,752 MiB | 2h36m | **236/500 (47%)** |
| **cuda:2** | 146382 | c3_llama (importance, s025) | 22,288 MiB | 9m | **15/50 (30%)** |
| **cuda:3** | 132002 | c2_qw_n500 (random, s015) | 31,364 MiB | 2h36m | **241/500 (48%)** |
| **cuda:3** | 146132 | c3_llama (random, s025) | 22,446 MiB | 10m | **16/50 (32%)** |

### 关键发现

**1. GPU 冲突确认：cuda:2,3 上两个实验同时运行**
- c2_qw_n500 占 ~31 GB/GPU，c3_llama 占 ~22 GB/GPU，合计 ~53 GB/97 GB
- 显存尚未溢出，GPU 利用率 89-92%，两者目前都在正常推进
- 但共享 GPU 会互相拖慢速度

**2. 重复进程已死**
- PID 132389, 132392（c2_qw_n500 重复进程）：已不存在
- PID 138408, 138410（c3_llama 原始子进程）：已不存在

**3. c3_llama 进程树重建**
- 原始 wrapper PID 138393 仍存活，通过 138398 → 138402/138403 派生了新 python 进程 146382/146132
- c3_llama 已完成 s015 和 s020 两轮，当前在跑 s025（第 3 轮）

**4. c2_qw_n500 的 full log 异常**
- `c2_qw_n500_gpu2_full.log` 和 `c2_qw_n500_gpu3_full.log` 停留在 22:00（2.5 小时前），只记录到加载模型和第 1 个 problem，之后无更新。实际进度写在 `n500_qw_imp_s015.log` / `n500_qw_rand_s015.log`

### 各实验状态总结

| 实验 | GPU | 状态 | 进度 | 预估剩余 |
|------|-----|------|------|----------|
| c2_n500_deepseek | cuda:0,1 | 正常运行 | 60-64% | ~1.5-2h |
| c2_qw_n500 | cuda:2,3 | 运行中（被拖慢） | 47-48% | ~2.5-3h |
| c3_llama (s025) | cuda:2,3 | 运行中（与上者冲突） | 30-32% | ~20min |

### 建议行动
c3_llama s025 轮只剩 ~35 个 problem（n=50），大约 20 分钟内完成。如果 c3_llama 后续没有更多轮次，冲突会自然解除。如果还有后续轮次（s030 等），需要决定是否暂停或迁移。

---
