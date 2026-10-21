# check exp003 d010 startup

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp003_d010_startup_20260517T063245_result.json`
- **Structured JSON:** [`53a1d75a21e24ea19d52.json`](../../sessions/53/53a1d75a21e24ea19d52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认通过：

| 检查项 | 状态 |
|--------|------|
| 进程 PID 88156 | **存活** (Ss+)，参数含 `--signal log_det --tau 0.005` |
| Controller 参数 | `signal=log_det, tau=0.005, k=1.0, r_min=0.2, r_max=0.8` ✓ |
| 模型加载 | 成功（`TRANSFORMERS_OFFLINE=1`，本地缓存） |
| 训练进度 | Gen 0 评估中（effective rank → perplexity → distinct-4） |
| GPU cuda:1 | PID 88161 占用 19034 MiB，利用率 93% |
| tmux session | `exp_003` 存在 |

训练已正常启动，正在执行 Gen 0 baseline 评估。

---
