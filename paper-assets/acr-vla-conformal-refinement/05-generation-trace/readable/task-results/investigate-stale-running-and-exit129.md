# investigate stale running and exit129

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_stale-running-and-exit129_20260517T191702_result.json`
- **Structured JSON:** [`205ba087d73c348cab5d.json`](../../sessions/20/205ba087d73c348cab5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。汇报如下：

---

## 检查 1: 原始 multiscale PID 状态

- **bjb2-28827 PID 455518**: ✅ 存活（python子进程 PID 455520, CPU 569%）。当前进度：已完成 4/10 tasks（alphabet_soup 0%, cream_cheese 0%, salad_dressing 10%, bbq_sauce 20%），正在跑第 5 个 task (ketchup)。无 JSON 输出（未完成）。
- **bjb1-32546 PID 503178**: ✅ 存活（python子进程 PID 503180, CPU 363%）。seed43 当前进度：已完成 3/10 tasks（alphabet_soup 0%, cream_cheese 0%, salad_dressing 20%），正在跑 bbq_sauce。无 JSON。
- **bjb1-32546 PID 504682**: ✅ 存活（python子进程 PID 504684, CPU 373%）。seed44 当前进度：已完成 3/10 tasks（alphabet_soup 0%, cream_cheese 0%, salad_dressing 20%），正在跑 bbq_sauce。无 JSON。

## 检查 2: K sweep 状态 (bjb1-18228)

- **k5**: 运行中 PID=713405 (GPU 0, CPU 183%)，无 JSON 输出（未完成）
- **k20**: 运行中 PID=713480 (GPU 2, CPU 131%)，无 JSON 输出（未完成）
- 额外发现：还有 2 个 multiscale 实验在此服务器运行（seed43 PID 702904 GPU 1, seed44 PID 703107 GPU 3），使用 `crm_k1_best.pt` checkpoint（非 multiscale checkpoint）

## 检查 3: EXIT_CODE=129 实验结果

- **eval-perdof-object-norm02-seed45-r2**: 
  - bjb2-28827 有 **原始实验** `eval_object_perdof_norm02_seed45.json` 已完成：**SR=9.0%**（20 rollouts，10 tasks）
  - r2 版本（bjb1-18228）只有日志显示刚启动（"10 tasks loaded"），无 JSON，无进程存活
  - 但 bjb2-28827 上 **新的重试** 正在运行：PID 389051 (perdof seed46) 和 PID 404983 (perdof seed47)

- **eval-obs-only-object-norm005-seed43-r3**: 
  - 无 JSON 结果文件
  - bjb1-32546 上 **r2 版本正在运行**：PID 433500 (CPU 138%)，已跑了 ~600 分钟
  - 之前的 r1 日志只到了 task 1 就中断了

- **eval-obs-only-object-norm01-seed47**: 
  - 无 JSON 结果文件
  - bjb2-28827 上 **正在运行**：PID 448782 (CPU 160%, GPU 1)，已跑了 ~118 分钟，当前在 task 5 (ketchup)
  - 这是 agent-ml cron 管理的实验，仍在正常执行中

## 检查 4: Checkpoint 对比

| 文件 | 服务器 | 大小 | 时间 |
|------|--------|------|------|
| `crm_k1_best.pt` | bjb2-28827 | 1,347,854 bytes | May 18 02:13 |
| `crm_k1_best.pt` | bjb1-32546 | 1,347,854 bytes | May 17 23:16 |
| `crm_k1_best_multiscale.pt` | bjb1-32546 | 1,347,854 bytes | May 18 02:30 |

**判断：三个文件大小完全相同（1,347,854 bytes）。`crm_k1_best_multiscale.pt` 和 `crm_k1_best.pt` 极可能是相同模型的拷贝（仅时间戳不同）。**

## 检查 5: GPU 占用

**bjb2-28827** (6x GPU, 24564 MiB each):
```
GPU 0: 19%, 3772/24564 MiB  ← multiscale seed42
GPU 1: 17%, 5664/24564 MiB  ← obs_only norm01 seed47
GPU 2: 17%, 3804/24564 MiB  ← perdof seed47 (旧)
GPU 3: 18%, 5664/24564 MiB  ← obs_only norm01 seed46
GPU 4: 19%, 3342/24564 MiB  ← perdof seed46 (旧)
GPU 5: 17%, 5664/24564 MiB  ← perdof seed43 r3
```

**bjb1-32546** (6x GPU, 24564 MiB each):
```
GPU 0: 19%, 3343/24564 MiB  ← norm005 seed43 r2
GPU 1: 99%, 7109/24564 MiB  ← multiscale seed43
GPU 2: 22%, 2876/24564 MiB  ← (低占用，可能是旧实验)
GPU 3: 22%, 2876/24564 MiB
GPU 4: 86%, 5711/24564 MiB  ← multiscale seed44
GPU 5: 22%, 3343/24564 MiB
```

**bjb1-18228** (4x GPU, 24564 MiB each):
```
GPU 0: 23%, 5664/24564 MiB  ← k5 sweep
GPU 1: 19%, 4236/24564 MiB  ← multiscale seed43 (crm_k1_best.pt)
GPU 2: 21%, 5664/24564 MiB  ← k20 sweep
GPU 3:  0%, 4213/24564 MiB  ← multiscale seed44 (crm_k1_best.pt)
```

---

**总结要点：**
1. 所有 multiscale 和 K sweep 实验均在正常运行中，预计还需数小时完成
2. EXIT_CODE=129 的实验中，perdof seed45 原始版已有结果(SR=9%)；norm005 seed43 和 norm01 seed47 已被重启并正在运行
3. `crm_k1_best_multiscale.pt` 与 `crm_k1_best.pt` 大小一致，bjb1-18228 上的 multiscale 实验实际使用的是 `crm_k1_best.pt`（非 multiscale 版本），这可能是配置问题

---
