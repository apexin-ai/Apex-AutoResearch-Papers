# exp029_episode_level_seed2 诊断报告

**时间**: 2026-05-18 13:39 (crash) | **服务器**: bjb1-17606 | **W&B run**: vugdm2sw

## 失败根因：CUDA OOM during loss.backward()

训练在 step 1 的 actor policy update 阶段崩溃，具体位置：

```
File ".../dp_actor.py", line 468, in update_policy
    loss.backward()
torch.AcceleratorError: CUDA error: out of memory
```

OOM 发生在 `loss.backward()`，即前向传播成功计算了 loss，但反向传播时激活值内存不足。

## 关键证据

| 项目 | 状态 |
|------|------|
| 磁盘 | 51% (123G free) — 正常 |
| GPU 进程 | 已全部退出，0MiB 占用 |
| Ray 进程 | 已终止 |
| val_step0 | 完成，success=12.5%（与 seed 1 baseline 一致） |
| 训练 step 完成数 | 0（step 1 rollout 生成后，update_actor 时崩溃） |

## 与 seed 1 对比

| 配置项 | seed 1 (exp029_episode_level) | seed 2 |
|--------|-------------------------------|--------|
| CUDA_VISIBLE_DEVICES | 0,1 | 0,1 |
| model | qwen3_exp021_ragen_sft_v4 | 同 |
| ppo_mini_batch_size | 16 | 16 |
| ppo_micro_batch_size_per_gpu | 1 | 1 |
| ppo_max_token_len_per_gpu | 65536 | 65536 |
| optimizer_offload | True | True |
| entropy_checkpointing | False | False |
| train seed | 10000 | 43 |
| 训练结果 | 完成 16 steps 后 OOM 退出 | step 1 即 OOM |

**重要发现**：seed 1 也在最后一步（step 16）因 OOM/SYSTEM_ERROR 退出。说明这套配置的内存 headroom 本身就很小，seed 2 的随机种子导致 step 1 的 rollout 序列更长/更多 token，直接触发了 OOM。

seed 1 step 16 的 `response_length/max: 16372`，`response_length/min: 1248`，total tokens 1,367,910。不同 seed 的 rollout 数据量可能差异很大。

## 根因分析

1. 内存 headroom 不足：2x RTX PRO 6000 (98GB each) + FSDP + optimizer_offload=True，但 `entropy_checkpointing=False`，`ppo_max_token_len_per_gpu=65536`，激活值内存随 rollout 序列长度变化
2. seed 依赖的随机性：不同 seed 产生不同的 episode rollout，token 总量不同，导致 backward 时内存需求不同
3. seed 1 也在边缘运行：最终也 OOM 退出（虽然 step 16 的指标已记录完成）

## 建议方案

### 方案 A：直接重试（风险中等）
- 清理 Ray 残留进程后重启
- 可能成功（不同的 rollout 调度可能避开内存峰值），也可能再次 OOM
- 前置操作：`ray stop --force`

### 方案 B：降低 ppo_max_token_len_per_gpu（推荐）
- 将 `ppo_max_token_len_per_gpu` 从 65536 降至 49152 或 32768
- 这会 cap 单 GPU 的 actor update token 数，限制 backward 内存峰值
- 需要确认 seed 1 是否也用了此参数以保持实验可比性

### 方案 C：启用 entropy_checkpointing
- 将 `entropy_checkpointing: True`
- 用计算换内存，减少激活值存储
- 影响训练速度但不影响训练结果

### 方案 D：转移到 westd-47453（4x GPU）
- 4 张 RTX PRO 6000，FSDP 分摊到更多 GPU，每卡内存压力更小
- 根据 C006 白名单，westd-47453 cuda:0,1,2,3 全部可用

## 重启前置操作

无论选哪个方案，重启前需要：
1. `ray stop --force` 清理残留 Ray 集群
2. 确认 `nvidia-smi` 显示 0 进程
3. 确认 `/root/autodl-tmp` 磁盘充足（当前 123G，够用）
