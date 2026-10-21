# RAGEN ALFWorld Dry-Run 验证报告

**日期**: 2026-05-14
**服务器**: bjb1-17606 (2x RTX PRO 6000 Blackwell, 94GB)
**环境**: Python 3.12.3, PyTorch 2.10.0+cu128, vLLM 0.18.1, verl 0.6.1, RAGEN 0.1
**模型**: Qwen3-1.7B
**配置**: 2 GRPO steps, 2 env_groups x 4 group_size, max_turn=10, response_length=512

## 结论: PASS

训练流水线完整跑通，vLLM 0.18.1 与 RAGEN 完全兼容。

---

## 1. vLLM 0.18.1 兼容性

**状态: 完全兼容**

尽管 RAGEN 原始依赖声明 `vllm==0.8.2`，实测 vLLM 0.18.1 在以下阶段均无报错：
- vLLM rollout engine 初始化（enforce_eager 模式）
- 多轮 token 生成（`actor_rollout_generate_sequences`）
- Log probability 计算（`actor_rollout_compute_log_prob`）
- 模型权重在 FSDP 与 vLLM 之间同步
- 验证阶段的推理

**无需降版本、无需 monkey-patch。**

## 2. 训练流水线完整性

**状态: GRPO rollout -> reward -> update 全流程完成**

Pipeline 各阶段均正常执行：

| 阶段 | 耗时(s) | 占比 |
|------|---------|------|
| gen (vLLM rollout) | 52.64 | 53.4% |
| old_log_prob | 0.68 | 0.7% |
| ref_log_prob | 0.63 | 0.6% |
| advantage | <0.01 | ~0% |
| update_actor | 2.92 | 3.0% |
| eval/testing | 41.77 | 42.4% |
| **total per step** | **98.64** | **100%** |

- Algorithm: GRPO (critic disabled, advantage from group reward normalization)
- Loss aggregation: seq-mean-token-mean
- Actor gradient norm: 4.29
- pg_loss: ~0 (expected at training start)

## 3. 速率

| 指标 | 值 |
|------|-----|
| Step 1 (含初始化) | 228.98s |
| Step 2 (稳态) | 98.64s |
| 稳态 step/h | ~36.5 |
| 总训练时间 (2 steps) | 220.33s |
| Token throughput | 157.5 tokens/s |
| GPU 显存峰值 | ~38.5 GB / 94 GB (rollout 阶段) |

## 4. ALFWorld 环境交互

**状态: 环境加载和交互正常**

- 训练集: 8810 games, 验证集: 494 games
- Agent 能产生 action 并收到 reward（format penalty）

### 训练指标 (Step 2)

| 指标 | 值 | 说明 |
|------|-----|------|
| success | 0.0 | 未训练模型不会完成任务 |
| manager_invalid_action | 96.25% | 大部分 action 格式错误 |
| action_is_valid | 3.75% | 少量正确格式的 action |
| score/mean | -0.9625 | format_penalty=-0.1 累积 |
| score/max | -0.7 | 最好的 sample 有 3 个有效 action |
| avg response_length | 3884 tokens | 多轮交互累积 |

### 验证指标

| 指标 | 值 |
|------|-----|
| success | 0.0 |
| manager_invalid_action | 100% |
| reward/mean | -1.0 |
| response_length | 2757 tokens |

## 5. 修复记录

### 5.1 flash_attn 缺失 (已修复)

- **问题**: `ragen/workers/actor/dp_actor.py:24` 和 `ragen/workers/critic/dp_critic.py:24` 在模块级 import `flash_attn`，flash_attn 未安装导致启动崩溃
- **修复**: 改为 try/except lazy import，`use_remove_padding=False` 时不需要 flash_attn
- **影响**: 2 个文件各改 1 行

### 5.2 ALFWORLD_DATA 环境变量

- **问题**: ALFWorld 数据在 `/root/autodl-tmp/alfworld/`，需设置 `ALFWORLD_DATA`
- **修复**: 启动命令添加 `ALFWORLD_DATA=/root/autodl-tmp/alfworld`

## 6. 完整运行命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/cost-verify-agent-rl/RAGEN
ALFWORLD_DATA=/root/autodl-tmp/alfworld CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_dryrun
```

## 7. 关键时间线

- 02:14:44 训练启动
- 02:15:35 vLLM engine 初始化完成
- 02:18:32 Step 1 rollout + update 完成 (228.98s)
- 02:20:11 Step 2 rollout + update 完成 (98.64s)
- 02:20:53 Validation 完成 (41.77s)
- 02:21:07 训练结束，总计 327.62s
