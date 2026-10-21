# research cls home progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cls-home-progress-check_20260512T185916_result.json`
- **Structured JSON:** [`2d717fe3a199cc96982f.json`](../../sessions/2d/2d717fe3a199cc96982f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。汇总如下：

---

## 训练进度报告

### 1. 当前训练状态
| 指标 | 值 |
|------|-----|
| 当前 step | **862 / 6633** (13%) |
| 速度 | ~7.1 s/it |
| 已运行 | 1h42m |
| 剩余 steps | 5771 |
| 预计剩余时间 | **~11.4h** |
| 预计完成时间 | **2026-05-12 ~23:24** |
| 进程 PID 2840844 | 运行中 (elapsed 1h45m) |

### 2. GPU 利用率
| GPU利用率 | 显存使用 | 显存总量 |
|-----------|----------|----------|
| 77% | 19,465 MiB | 32,607 MiB (60%) |

### 3. Checkpoint 保存情况
**目录为空** — 这是正常的。训练脚本 `save_strategy="epoch"`，不是 `save_steps`。每 epoch ~2211 步才保存一次，当前才 862 步，第一个 checkpoint 预计在 step ~2211 时出现（约 2.7h 后）。`save_total_limit=2`，最终只保留 2 个 checkpoint + best。

handoff 提到的 "save_steps=50 已生效" 是**不准确的**，脚本中没有 `save_steps` 参数。

### 4. Eval 脚本就绪状态
**没有** `eval_repo_*.py`。可用的 eval 脚本：
- `eval_verifier.py` — 对应 cls 模型，最可能适用
- `eval_traj_verifier.py` — trajectory 模型
- `eval_cwm_baseline.py` — CWM baseline
- `eval_precision_recall.py` / `eval_majority_voting.py` — 分析工具

repo-level cls 训练完后，大概率需要基于 `eval_verifier.py` 写一个 `eval_repo_verifier.py`，或直接用 `eval_verifier.py` 并指向新 checkpoint。

### 5. cls8b-eval-seed123 差异说明
服务器上**不存在** `eval_cls8b_seed123` 相关文件。现有 seed123 eval 结果：
- `eval_seed123.json`: accuracy **89.52**, fail F1 **89.40**, pass F1 89.64
- `eval_cls_seed123_with_preds.json`: 与上面完全相同
- `eval_traj_seed123.json`: accuracy 85.47（trajectory 模型，不同任务）

仅有的 cls8b eval 是 `eval_cls8b_seed456.json`（accuracy 88.31）。

handoff 提到的三个值 89.52 / 89.40 / 89.37 中：
- 89.52 = overall accuracy
- 89.40 = fail-class F1
- 89.37 在所有 JSON 文件中**未找到**，可能是记忆偏差或来自 wandb/其他来源

---
