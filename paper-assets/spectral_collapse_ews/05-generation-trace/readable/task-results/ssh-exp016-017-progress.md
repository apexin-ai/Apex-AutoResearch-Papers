# ssh exp016 017 progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp016-017-progress_20260522T073202_result.json`
- **Structured JSON:** [`c6814ec5c39e1f4a7b75.json`](../../sessions/c6/c6814ec5c39e1f4a7b75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整汇总如下：

---

## 1. 进程存活

| 实验 | PID | 状态 | 运行时间 |
|------|-----|------|---------|
| exp_016 | 614614 | **ALIVE** | 08:16:15 |
| exp_017 | 648360 | **ALIVE** | 01:14:16 |

## 2. GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| 0 | 93% | 25017 MiB |
| 1 | 94% | 19045 MiB |

## 3. exp_016 checkpoint 进度 (r=0.3, seed44)

```
gen_0, gen_1, gen_2, gen_3, gen_4
```

## 4. exp_017 checkpoint 进度 (r=0.2, seed43)

- `fixed_mix_r02_seed43/`: **gen_0** (仅1个)
- `fixed_mix_r020_seed43/`: 不存在

## 5. exp_016 日志最后 30 行

正在做 gen_4 的 sample generation 阶段：
```
Generated 12160/35000 samples
Generated 12480/35000 samples
Generated 12800/35000 samples
```
（大量 right-padding 警告，可忽略）

## 6. exp_017 日志最后 30 行

正在做 sample generation 阶段（目标更大 40000）：
```
Generated 26240/40000 samples
Generated 26560/40000 samples
Generated 26880/40000 samples
```

## 7. Results JSON 进度

| 实验 | 文件 | generations 数 |
|------|------|---------------|
| exp_016 | `phase1_fixed_mix_r03_seed44_results.json` | 5 (gen 0–4)，当前正在跑 gen_4 的 sample generation |
| exp_017 | `phase1_fixed_mix_r025_seed43_results.json` | 11 (gen 0–10) |
| exp_017 | `phase1_fixed_mix_r025_seed43_summary.json` | 存在 |
| exp_017 (r=0.2) | 无匹配文件 | — |

**注意**：exp_017 的 results JSON 匹配到的是 `r025_seed43`（r=0.25）而非 `r02_seed43`（r=0.2）。exp_017 的 PID 进程（运行 1h14m）可能是刚启动的 r=0.2 任务，checkpoint 只有 gen_0，暂无 results JSON 输出。而 `r025_seed43` 的 11 代结果可能来自之前的运行。

---
