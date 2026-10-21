# research scienceworld registry history

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scienceworld_registry_history_20260522T033549_result.json`
- **Structured JSON:** [`5d353f862b098bf29c5e.json`](../../sessions/5d/5d353f862b098bf29c5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ScienceWorld 实验汇总报告

---

### 1. 实验时间线

| exp_id | 创建时间 | 状态 | 结论 | 说明 |
|--------|---------|------|------|------|
| `scienceworld_sft` | 05-19 14:35 | DONE | **success** | 1.7B SFT 训练，448 steps，train_loss 0.003 |
| `scienceworld_sft_eval` | 05-19 18:11 | DONE | killed | 首次 eval，中途 killed |
| `scienceworld_sft_eval_v2` | 05-19 18:50 | DONE | **success** | SFT baseline: **30.1% success, avg_score 20.9** |
| `scienceworld_info_loss_full` | 05-20 14:21 | DONE | failed | westd 上 info loss 实验，失败 |
| `sw_info_loss_full_v2` | 05-20 14:34 | DONE | failed | 同上重试，再次失败 |
| `scienceworld_info_loss_h2` | 05-20 14:21 | DONE | killed | h=2 info loss 实验，killed |
| `sw_info_loss_bjb1` | 05-20 16:38 | DONE | **success** | **info loss 结果: full=34.8% vs h2=4.5%, delta=30.3pp** |
| `scienceworld_grpo_cell_a` | 05-20 11:24 | DONE | **negative** | **Cell A collapse 确认: 15步全程 0% success, score→-100** |
| `scienceworld_grpo_cell_c` | 05-20 11:24 | DONE | **failed** | Cell C v1: Java IPC 通信异常，step 1 后崩溃 |
| `scienceworld_grpo_cell_c_v2` | 05-20 15:41 | DONE | **failed** | Cell C v2: 磁盘满(99%)，Ray object spilling 阻塞，stall 1h50m |
| `scienceworld_grpo_cell_c_v3` | 05-20 18:23 | DONE | **negative** | Cell C v3: **3步后止损，0% success, action_valid=9.4%, collapse** |

---

### 2. 每次失败的具体原因

**Cell C v1 (Java crash)**
- failure_reason: `ScienceWorld Java environment communication error: Exception while sending command`
- 仅完成 1/15 steps，step 1 score=5.44, action_valid=0.44
- Root cause: ScienceWorld 底层 Java IPC 通信不稳定

**Cell C v2 (磁盘满)**
- 在 step 2 stall，磁盘使用率 99%
- Ray object spilling 被阻塞，GPU utilization 0% 持续 1h50min
- 花费 5.41 GPU-hours 后 killed

**Cell C v3 (训练崩溃/止损)**
- 不是基础设施故障，而是**训练本身 collapse**
- step 1→3: score 2.71→0.96, reward 0.5→0.153, action_valid=9.4%
- 128 trajectories 全零 reward（reward saturation）
- D109 判定：满足止损条件（success=0%, action_valid<20%），趋势持续恶化，释放 GPU

**Cell A (负面结果，非"失败")**
- 15步全程 0% success，final_score -100.0（比 ALFWorld 更极端）
- entropy 上升 + KL 崩塌，模式与 ALFWorld Cell A 一致
- 这是**预期结果**，用于跨环境验证 step-independent collapse

---

### 3. SFT Baseline 结果

- **整体**: 540/1796 episodes 成功，**success rate 30.1%，avg_score 20.9**
- **高分任务**: lifespan-longest-lived 90.3%, find-non-living-thing 77.3%, find-living-thing 65.3%
- **零分任务**: boil 0%, chemistry-mix 0%, freeze 0%, grow-plant 0%, identify-life-stages 0%
- **Info loss**: full context 34.8% vs h=2 window 4.5%，delta 30.3pp（某些任务从 100%→0%）

---

### 4. 实验设计和超参数

**SFT 训练**:
- model: Qwen3-1.7B, data: 3592 train / 1796 val, lr: 5e-6, epochs: 2, batch: 16, max_length: 16384, FSDP2

**Cell A (step-independent GRPO)**:
- steps: 15, context_window_mode: step_independent, history_length: 2
- env_groups: 16, group_size: 8, ppo_mini_batch_size: 8, lr: 1e-6, n_gpus: 2
- server: westd, gpu: cuda:0,1

**Cell C (episode-level GRPO)**:
- steps: 15, context_window_mode: full
- env_groups: 16, group_size: 8, ppo_mini_batch_size: 8, lr: 1e-6, n_gpus: 2
- server: westd, gpu: cuda:2,3
- seed: 10000（v2/v3）

---

### 5. 基于失败历史的 GRPO 配置建议

Cell C 三次失败暴露三个独立问题：

1. **Java IPC 不稳定** → 需要 JVM 加固（`JAVA_TOOL_OPTIONS=-Xmx4g`、超时重试、进程隔离）。v2 已做但未解决根本问题。考虑在 ScienceWorld env wrapper 层加 try/retry + env reset 逻辑。

2. **磁盘空间** → v2 因 99% 磁盘满导致 Ray spilling 失败。训练前必须确保 ≥50GB 可用空间，设置 `RAY_object_spilling_config` 指向数据盘。

3. **Reward saturation / 任务太难** → 这是最根本的问题。128 trajectories 全零 reward 意味着模型在 GRPO group 内无任何成功样本，advantage 全为零，训练信号消失。SFT baseline 仅 30.1%（ALFWorld SFT 是 ~50-80%），大量任务类型 success=0%。

**配置方向建议**：
- **过滤训练任务**：排除 SFT success=0% 的任务类型（boil, chemistry-mix, freeze, grow-plant 等），只用 SFT 有基础能力的任务（find-*, lifespan-*, test-conductivity 等）
- **增大 group_size**：从 8 提到 16-32，增加组内至少有 1 个成功样本的概率
- **增大 env_groups**：增加每步训练样本量
- **提高 lr**：当前 1e-6 可能过低，可尝试 5e-6（与 SFT 一致）
- **考虑 curriculum**：先从高成功率任务开始，逐步引入难任务
- **JVM 稳定性**：每个 episode 后强制 env.reset()，通信超时设 30s，失败后重建 Java 进程而非整个训练崩溃

---
