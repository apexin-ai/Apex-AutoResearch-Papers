# deploy westd 41074 pi05 batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-41074-pi05-batch_20260524T012049_result.json`
- **Structured JSON:** [`de7a4df247f04bdf906e.json`](../../sessions/de/de7a4df247f04bdf906e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常运行，模型加载成功，pruning 配置正确。

## 部署汇总

| GPU | 实验 ID | tmux session | PID | 状态 |
|-----|---------|-------------|-----|------|
| 0 | `eval_pi05_random_k095_goal_seed43` | eval_pi05_random_k095_goal_seed43 | 335825 | Random k=0.95, keep 243/256 tokens, Goal seed43 |
| 1 | `eval_pi05_l2norm_k07_goal_seed43` | eval_pi05_l2norm_k07_goal_seed43 | 336074 | L2norm k=0.7, keep 179/256 tokens, Goal seed43 |
| 2 | `eval_pi05_l2norm_k05_long_seed43` | eval_pi05_l2norm_k05_long_seed43 | 336428 | L2norm k=0.5, keep 128/256 tokens, Long seed43 |
| 3 | `eval_pi05_random_k085_goal_seed43` | eval_pi05_random_k085_goal_seed43 | 318964 | **已在运行**（Task 2/10 进行中） |

**注意事项**：
- 任务描述中的参数名有误：脚本实际使用 `--prune_mode`（非 `--mode`）、`--keep_ratio`（非 `--k_ratio`）、`libero_10`（非 `libero_long`）
- GPU 0 和 GPU 2 的实验是重跑（已有历史结果 SR=81.6% 和 54.0%），registry 状态卡在 DEPLOYED（状态机不允许 DONE→RUNNING 直接转换）

---
