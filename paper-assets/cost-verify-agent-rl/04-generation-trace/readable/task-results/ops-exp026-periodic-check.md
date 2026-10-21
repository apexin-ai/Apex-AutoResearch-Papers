# ops exp026 periodic check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_periodic_check_20260515T121232_result.json`
- **Structured JSON:** [`2a792abab20b036dc313.json`](../../sessions/2a/2a792abab20b036dc313.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp026 状态报告

### 进程: ✅ 运行中
- **主进程** PID 778562: `python train.py --config-name _alfworld_exp026_step_independent_grpo`
- **Rollout workers** PID 782015/782016: `ray::WorkerDict.actor_rollout_generate_sequences` (CPU 87.6%)
- **TaskRunner** PID 781795, 多个 ray::IDLE workers
- **tmux session** `exp026` 存在

### 训练进度: Step 2/150 (1%)
- Step 0→1: 38 min, Step 1→2: ~43 min
- 速度: ~2444s/step (~40 min/step)
- **预计总时长: ~100 小时**（当前已运行 ~1.7h）
- 当前正在执行 step 2 的 rollout 生成

### Step 0 验证指标 (16 episodes, baseline)
| 指标 | 值 |
|------|-----|
| **success** | **6.25%** (1/16) |
| pass@1 | 6.25% |
| action_is_valid | 63.1% |
| action_is_effective | 87.9% |
| num_actions | 42.4 |
| reward/mean@775 | 0.323 |
| response_length | 114.7 |

### GPU: ✅ 双卡活跃
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 66% | 48.5G / 95.6G (50.7%) |
| 1 | 65% | 48.5G / 95.6G (50.7%) |

### 磁盘: ✅ 充足
`/root/autodl-tmp`: 137G/250G (55%), 剩余 114G

### W&B: 已禁用 (WANDB_MODE=disabled)

### 异常/警告
- ⚠️ 部分序列超过 max_prompt_length 4096: 观察到 4195/4364/4367/4733 tokens（truncation 警告）
- 大量 "Skipping non-numeric metric 'anchor_obs'" 警告（无害）
- 无 NaN、无 entropy 归零、无 GPU 骤降 → 🟢

### 早停评估
- Step 0 success = 6.25%：这是训练前 baseline，符合预期。尚需等到 step 10 才能做首次早停判定。

---
