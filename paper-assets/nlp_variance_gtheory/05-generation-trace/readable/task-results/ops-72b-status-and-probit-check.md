# ops 72b status and probit check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_72b_status_and_probit_check_20260522T153321_result.json`
- **Structured JSON:** [`405a8b271786009e82e8.json`](../../sessions/40/405a8b271786009e82e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 72B 下载状态

- **36/37 shards**，最后一个 shard (`model-00037-of-00037.safetensors`) 下载中：**85% (2.73G/3.22G)**，速度 ~570KB/s
- **ETA: ~15 分钟**（约 500MB 剩余）
- 下载进程活跃：PID 229326
- Watchdog 活跃：两个实例（inline PID 249737 + script PID 255069），下载完成后会自动启动 TP=4 推理
- 推理尚未开始（等下载完成）

### 2. Probit Simulation 数据：**可用**

服务器上有两个 simulation 结果文件，均使用 probit latent model（`y = 1{μ + latent > 0}`），100 replications：

| 文件 | 设计 | Spearman ρ (excl. residual) | Top-1 正确率 | Top-5 正确率 |
|------|------|---------------------------|-------------|-------------|
| `simulation_binary_recovery.json` | 432 cond/item | 0.708 (0.685–0.734) | 100% | 72% |
| `binary_simulation_recovery_matched.json` | 1296 cond/item | **0.732** (0.716–0.751) | 100% | **79%** |

**Matched design（更密设计）的 bias/RMSE 更优：**

| Accuracy (p) | Mean \|bias\| (base) | Mean \|bias\| (matched) | ρ (base) | ρ (matched) |
|-------------|--------------------|-----------------------|----------|-------------|
| 0.5 | 0.361 | **0.299** | 0.714 | **0.741** |
| 0.6 | 0.342 | **0.279** | 0.714 | **0.731** |
| 0.7 | 0.415 | **0.340** | 0.703 | **0.731** |
| 0.8 | 0.404 | **0.368** | 0.702 | **0.724** |

核心结论：Henderson Type-I 在 binary 数据上 residual 会膨胀（吸收 Bernoulli 方差），但**系统性方差分量的排序稳健恢复**——item_id 在 100% 的 replications 中被正确识别为最大 systematic source。Recovery 随 n_items 增大而改善，对 p ∈ [0.5, 0.8] 稳健。

---
