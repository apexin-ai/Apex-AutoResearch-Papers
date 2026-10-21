# ssh exp017 018 progress

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp017_018_progress_20260523T100021_result.json`
- **Structured JSON:** [`9b08cd69c4872c8f0ec8.json`](../../sessions/9b/9b08cd69c4872c8f0ec8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-018 (cuda:2)

**进程**: 运行中，PID 345307，CPU 104%，已运行 ~67 分钟
**GPU**: 73566 MiB

**synthetic_n20.csv**: 15 行（含 header = 14 条数据）

最后 3 行：
```
5,joint_gmfrm,0.09608924324949444,0.968421052631579,0.3112602772509905,0.9606677809775076,1.0,1394.0,354.53775572776794
6,sequential,0.15524451261779593,0.9578947368421054,1.5833724721610172,0.5458551421325101,1.01,653.0,166.3316445350647
6,joint_gmfrm,0.0962666835812814,0.9578947368421054,1.0153660475447923,0.4960395816312468,1.01,1192.0,296.6363182067871
```

**日志**: exp-018.log 为空（输出 tee 到 `exp018/results/exp018.log`，不是 `/root/runs/` 路径）

---

## exp-017 (cuda:0)

**进程**: 运行中，PID 318082，CPU 103%，已运行 ~182 分钟
**GPU**: 73586 MiB

**coverage_simulation.csv**: 38 行（含 header = 37 条数据），进度 **38/800**

最后 3 行：
```
8,34,0.75,1.0,0.621182955801487,0.2871408015489578,1.0,3158.0,344.55604791641235
8,35,0.5,1.0,0.7726924493908882,0.29669101908802986,1.0,3435.0,340.1221022605896
8,36,0.625,1.0,0.6703061610460281,0.2709451653063297,1.0,2604.0,344.4957962036133
```

**日志尾部**:
```
[38/800] N=  8 seed= 37 | 10389s | ETA 264231s
```

**exp-017 预计剩余时间**: ~264231s ≈ **73.4 小时**。每步约 ~273s，800 步总计约 61 小时，已跑 2.9 小时完成 38 步。有 `num_chains=4` 串行警告（只有 1 个 GPU device，4 条链顺序执行）。

---
