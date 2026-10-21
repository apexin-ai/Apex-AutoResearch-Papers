# diagnose training metrics anomaly

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_training-metrics-anomaly_20260514T200818_result.json`
- **Structured JSON:** [`3d899c6b0f297fd81d70.json`](../../sessions/3d/3d899c6b0f297fd81d70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。以下是报告。

---

## 排查结论：**误报——两个进程完全独立，指标不同**

### 进程验证

| 项目 | CWM 8B (PID 266816) | CLS 8B (PID 266449) |
|------|---------------------|---------------------|
| GPU | GPU 2, 30724MiB | GPU 3, 30904MiB |
| 脚本 | `train_repo_cwm.py` | `train_repo_verifier.py` |
| 种子 | 42 | 123 |
| Stdout fd | `→ repo-level-cwm-8b-conda-v2.log` | `→ repo-level-cls-8b-seed123-conda-v3.log` |
| 当前 step | ~2000 (epoch 0.90) | ~3728 (epoch 1.67) |
| 最新 loss | 0.1796 | 0.3805 |
| 最新 checkpoint | checkpoint-1900 (03:48) | checkpoint-3600 (03:51) |

### 脚本差异确认
- **CWM**: 预测执行输出（generation），目标字段 = `execution_output`
- **CLS**: 分类 pass/fail，目标字段 = `label` → LABEL_MAP {1:"pass", 0:"fail"}
- 不同的 system prompt、不同的 user prompt、不同的 save_steps (100 vs 200)

### 关于 "loss=0.2144 at step 3576" 的追溯
- `loss=0.2144` **仅出现在 CLS v3 日志中**（step ~3550 处，epoch 1.61）
- CWM 当前只到 step ~2000，**不可能有 step 3576 的指标**
- 所有历史日志（旧 CWM/CLS）中也未找到这个值

### 根因
**观察错误**，不是日志混写或配置错误。可能的原因：
1. 查看时误读了同一个 CLS 的 tmux 输出（CLS tmux session `repo-level-cls-8b-seed123-conda-v3` 当前已不存在）
2. CWM v3 日志显示曾有人试图用 `train_repo_verifier.py --task cwm` 启动，但参数不识别直接报错退出，未实际运行

### 结论
**无需干预。** 两个进程在不同 GPU 上独立训练不同任务，指标完全不同，checkpoint 目录独立。训练正常进行中。

---
