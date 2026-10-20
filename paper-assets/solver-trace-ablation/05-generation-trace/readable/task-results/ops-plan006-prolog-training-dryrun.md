# ops plan006 prolog training dryrun

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan006-prolog-training-dryrun_20260514T065808_result.json`
- **Structured JSON:** [`2b5ae27e9416e9e53f34.json`](../../sessions/2b/2b5ae27e9416e9e53f34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是完整分析报告。

---

## Phase 1: GPU 状态与实验进度

| GPU | 实验 | PID | 显存 | 进度 | 预估剩余 |
|-----|------|-----|------|------|----------|
| cuda:0 | plan018 (additive_random) | 377683 | 80355/97887 MiB | step 12/500 (2.4%) | ~81 min (~10s/step) |
| cuda:1 | plan016 (extended-1000) | 263273 | 80355/97887 MiB | step 532/1000 (53.2%) | ~47 min (~6s/step) |

**结论**：cuda:1 (plan016) 约 47 分钟后释放，优先用 cuda:1 跑 dry-run。

---

## Phase 2: Prolog 配置参数摘要

```yaml
# configs/grpo_prolog_exec_only.yaml
model_path: Qwen3-4B
data_path: data/train_500_seed42.jsonl   # C001 ✓
logic_type: prolog
reward_mode: execution_only
solver: prolog                           # swipl at /usr/bin/swipl ✓
K (num_generations): 8
per_device_batch_size: 4
gradient_accumulation_steps: 2           # effective batch = 8 prompts
max_completion_length: 512
learning_rate: 1.0e-6
exec_weight: 1.0 / sta_weight: 0.0
num_steps: 100
warmup: 未配置（TRL 默认 = 0）
```

---

## Phase 3: 冷启动风险评估

### Reward 路径分析

`execution_only` + `logic_type=prolog` 的 reward 路径：
1. `prolog_sta_reward()` 被调用，`execution_weight=1.0, sta_weight=0.0`
2. `parse_prolog_formalization(text)` 提取 clauses + query
3. `solver.prove(clauses, query)` → swipl 执行
4. **reward = 1.0 (proved) 或 0.0 (failed)**，纯二值信号，无部分奖励

当 prove 全部失败时：K=8 个 completion 全部 reward=0 → std=0 → GRPO advantage 全零 → **gradient=0, loss=0**（日志中表现为 `frac_reward_zero_std=1.0`）。

### FOL vs Prolog 初始 PR 对比

参考 plan018（FOL, additive_random）前 10 步的 prove_rate：
- 非零: steps 3,5,7,8,9,11,12 → **7/10 steps 有信号**
- 平均 PR ≈ 20%（per-sample）

Prolog 预期更低，原因：
- Prolog 语法更严格（小写 atoms, 大写 Variables, `.` 结尾）
- 解析器要求特定格式（`Facts/Rules:` section 或 `?-` query prefix）
- ProofWriter 数据集的 Prolog 形式化在预训练数据中罕见

**保守估计 Prolog 初始 PR ≈ 2-5%（per-sample）**

### 定量：K=8 时零梯度 batch 比例

P(batch 至少 1 个 proved) = 1 - (1-p)^K

| Per-sample PR | P(≥1 in K=8) | 零梯度 batch 比例 | 有效学习速率系数 |
|:---:|:---:|:---:|:---:|
| 2% | 15% | **85%** | ×0.15 |
| 5% | 34% | **66%** | ×0.34 |
| 10% | 57% | 43% | ×0.57 |
| 20% | 83% | 17% | ×0.83 |

**若初始 PR=2%**：每 step 4 个 prompt，期望仅 0.6 个有 ≥1 success → 极度稀疏梯度。100 步中有效步数仅 ~15 步。

**若初始 PR=5%**：期望 1.36 个 prompt 有信号 → 仍然很稀疏，但不至于完全停滞。100 步中有效步数 ~34 步。

### 死区风险

- 低 PR → 多数 batch 零梯度 → 无改进 → PR 不涨 → **正反馈死循环**
- 纯 binary reward（0/1）无部分奖励，格式正确但逻辑错误得不到任何信号
- 无 warmup，第一步就是全 LR=1e-6，偶发的非零梯度可能造成参数跳跃

**风险等级：中高**

---

## Phase 4: 对策方案（按优先级）

| 优先级 | 方案 | 效果 | 代价 |
|:---:|------|------|------|
| **P0** | 先用 base model 跑 inference-only eval（5-10 题 × K=8），测实际初始 PR 和 parse rate | 定量确认风险，避免盲跑 | CPU 可做，~2min |
| **P1** | K=16 | PR=5% 时有效 batch 从 34%→56%；PR=2% 时从 15%→28% | 每步耗时 ×2，显存可能增加 |
| **P2** | 添加 `warmup_ratio=0.1`（10 步） | 防止早期稀疏梯度造成参数跳跃 | 几乎无代价 |
| **P3** | 降 LR 至 5e-7 | 稀疏信号下减少单步更新幅度 | 可能需要更多 steps |
| **P4** | 格式奖励（parseable Prolog +0.1） | 提供部分信号，缓解全零问题 | 改变实验设计 |
| **P5** | 两阶段：SFT format → GRPO | 根本解决格式问题 | 大工程，需要标注数据 |

---

## Dry-run 命令（GPU 释放后执行）

```bash
# ===== plan006: Prolog 3-step dry-run =====
# 前置：确认 cuda:1 已释放 (plan016 完成)
export CUDA_VISIBLE_DEVICES=1
cd /root/solver-trace-ablation
python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --num_steps 3 \
  --output_dir /tmp/plan006_dryrun \
  --no_wandb
```

验证 checklist：
- [ ] 训练 loop 无报错（parse/solver/GRPO 全通）
- [ ] swipl 调用正常（无 "swipl not found"）
- [ ] 3 步 REWARD_LOG 正常输出
- [ ] 观察初始 prove_rate 和 parse_rate → 定量校准冷启动风险
- [ ] nvidia-smi 确认只占 cuda:1

---
