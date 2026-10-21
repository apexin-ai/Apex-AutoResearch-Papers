# check exp029 immediate

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_immediate_20260516T153029_result.json`
- **Structured JSON:** [`301d6e6a9239c8f33937.json`](../../sessions/30/301d6e6a9239c8f33937.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029_episode_level 状态汇报

### 进程状态: ALIVE
| 进程 | PID | 运行时间 | RSS |
|------|-----|---------|-----|
| 主进程 | 872859 | 4min 34s | 2 MB (coordinator) |
| TaskRunner | 876099 | 4min 18s | ~2.1 GB |

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 37,987 MiB / 48GB | 98% |
| cuda:1 | 38,857 MiB / 48GB | 98% |

### 当前阶段: `val_before_train` (初始验证)

训练尚未开始。当前进度：
1. 模型加载完成 (Qwen3 from `qwen3_exp021_ragen_sft_v4`)
2. FSDP 2-GPU 初始化完成
3. W&B 连接成功 → run `7hz8rhxg` ("exp029-alfworld-episode-level")
4. 数据加载完成 (train: 8810, val: 494)
5. **正在执行 val_before_train**：ALFWorld 环境交互中（日志末尾大量 `anchor_obs` warnings，时间戳 23:31:06，说明正在跑 32 个 val episodes）

### 关键配置
- env: AlfworldSG (episode-level)
- train groups: 16×8=128 episodes/step
- val groups: 32×1=32 episodes
- total_training_steps: 100
- lr: 1e-6 (constant), entropy_coeff: 0.001, kl_loss_coef: 0.01
- valid_action_bonus: 0.15, success_gated_bonus: True

### Metrics
暂无训练 metrics，val_before_train 尚未完成。预计 val 完成后会输出 baseline success_rate，然后进入 step 0 rollout。

---
