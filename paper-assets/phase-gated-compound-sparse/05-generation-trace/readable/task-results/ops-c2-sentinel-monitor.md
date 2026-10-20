# ops c2 sentinel monitor

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c2_sentinel_monitor_20260514T192458_result.json`
- **Structured JSON:** [`3e2f35d588b5ab9a6590.json`](../../sessions/3e/3e2f35d588b5ab9a6590.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## 1. GPU 状态

| GPU | 型号 | 利用率 | 显存占用 |
|-----|------|--------|---------|
| 0 | RTX PRO 6000 Blackwell | 77% | 23.7 / 97.9 GB |
| 1 | RTX PRO 6000 Blackwell | 79% | 24.2 / 97.9 GB |
| 2 | RTX PRO 6000 Blackwell | 77% | 25.1 / 97.9 GB |
| 3 | RTX PRO 6000 Blackwell | 76% | 25.7 / 97.9 GB |

4 卡全部在用，GPU 利用率 76-79%。

## 2. Condition 完成状态

每个 GPU 跑 4 个 condition（s015→s020→s025→s030），通过 shell 脚本串行执行。

| GPU | Track | s015 | s020 | s025 | s030 |
|-----|-------|------|------|------|------|
| 0 | ds_imp | **DONE** | 113/500 🔄 | pending | pending |
| 1 | ds_rand | **DONE** | 160/500 🔄 | pending | pending |
| 2 | qw_imp | **DONE** | 61/500 🔄 | pending | pending |
| 3 | qw_rand | **DONE** | 40/500 🔄 | pending | pending |

**进度 4/16 conditions 完成，4/16 运行中，8/16 等待。**

进程详情：
| PID | GPU | 当前任务 | 启动时间 | 运行时长 |
|-----|-----|---------|---------|---------|
| 156554 | 0 | ds_imp_s020 | 02:31 | 57 min |
| 154305 | 1 | ds_rand_s020 | 02:05 | 83 min |
| 159269 | 2 | qw_imp_s020 | 03:02 | 26 min |
| 159794 | 3 | qw_rand_s020 | 03:11 | 17 min |

## 3. ETA 估算

s015 历史耗时：DeepSeek ~4.5h/condition，Qwen ~5.2h/condition（含首次冷启动）。
当前 s020 速率：DeepSeek ~0.51 min/problem ≈ 4.2h/condition，Qwen ~0.43 min/problem ≈ 3.6h/condition。

取保守值 ~4.5h/condition（DeepSeek）和 ~4h/condition（Qwen，s015 冷启动开销不再重复）：

| Track | s020 完成 | s025 完成 | s030 完成 |
|-------|----------|----------|----------|
| ds_imp | ~06:45 | ~11:15 | ~15:45 |
| ds_rand | ~06:25 | ~10:55 | ~15:25 |
| qw_imp | ~07:00 | ~11:00 | ~15:00 |
| qw_rand | ~07:10 | ~11:10 | ~15:10 |

**预计全部完成：5月15日 ~15:45 CST（约12小时后）。**

## 4. Sentinel 脚本

- `check_completion.sh` — 检查 16 个 condition 目录的 `profiling_results.json`，达标时创建 `DONE_DEEPSEEK` / `DONE_QWEN` / `DONE_ALL_N500`
- crontab 不可用（AutoDL 无 cron），改用 `check_completion_loop.sh` nohup 后台循环，每 10 分钟检查一次，全部完成后自动退出
- PID: 162290，日志：`/root/autodl-tmp/pacs/completion_check.log`

## 5. Results 目录结构

```
/root/autodl-tmp/pacs/results/
├── c4_attention_entropy/
│   ├── c4_entropy_results.json  (1.7MB, May 14 16:26)
│   └── run.log
├── c4_attention_entropy_qwen/
│   └── c4_entropy_results.json  (1.5MB, May 14 17:05)
└── rebootstrap_analysis/
    ├── rebootstrap_analysis.py
    └── rebootstrap_results.json
```

n500 profiling 结果不在 `results/` 下，而是直接在项目根目录的 `profiling_output_n500_bf16_{ds|qw}_{imp|rand}_s{015..030}/profiling_results.json`。

---
