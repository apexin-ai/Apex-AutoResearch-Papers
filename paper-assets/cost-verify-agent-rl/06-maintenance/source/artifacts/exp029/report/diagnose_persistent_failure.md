# exp029_episode_level_seed2 持续失败诊断报告

**日期**: 2026-05-19  
**服务器**: bjb1-17606 (2× RTX PRO 6000 96GB)  
**最新 run**: exp029_seed2_resume_step15_fixA (W&B: msklzze2)

---

## 1. 错误时间线：4 次运行，3 种不同错误

| # | 日志文件 | 时间 | 错误类型 | 失败位置 |
|---|---------|------|---------|---------|
| 1 | `exp029_episode_level_seed2.log` | May 18 15:41 | **CUDA OOM** | `loss.backward()` step 1 |
| 2 | `exp029_seed2_100step.log` | May 18 22:59 | **磁盘 I/O 错误** | `torch.save(optimizer_state_dict)` at step 25 |
| 3 | `exp029_seed2_resume_step15.log` | May 18 23:19 | **FSDP 设备不匹配** | `actor_rollout_update_actor` (resume 阶段) |
| 4 | `exp029_seed2_resume_step15_fixA.log` | May 19 01:26 | **磁盘 I/O 错误** | `torch.save(optimizer_state_dict)` at step 25 |

---

## 2. 最新运行 (#4) 的真正错误

**不是 OOM。训练本身完全正常。**

训练从 step 15 成功运行到 step 24（约 10 个 step，每步 ~10-16 分钟），在 step 25 尝试保存 checkpoint 时崩溃：

```
fsdp_checkpoint_manager.py:244, in save_checkpoint
    torch.save(optimizer_state_dict, optim_path)

RuntimeError: [enforce fail at inline_container.cc:668] . unexpected pos 5372236096 vs 5372235992
RuntimeError: basic_ios::clear: iostream error
```

这是 **`torch.save` 在写入大文件时磁盘空间不足**的经典错误。`inline_container.cc:668` 的 `unexpected pos` 发生在 zipfile writer 写到一半时磁盘满了。

### 证据：训练正常运行的指标 (step 24)

- `train/AlfworldSG/success`: 37.5% (pass@8: 68.75%)
- `actor/pg_loss`: 正常
- `actor/grad_norm`: 4.57 (正常范围)
- `response_length/mean`: 10490
- GPU 未 OOM，正常完成了 forward/backward/update

---

## 3. 根因：磁盘空间耗尽

### 磁盘状况

```
/dev/md0  250G  227G  24G  91%  /root/autodl-tmp
```

### Checkpoint 空间占用

| 目录 | 大小 | 说明 |
|------|------|------|
| exp029-seed2/ | **100G** | 5 个 checkpoint (step 5/10/15/20/25) |
| hsweep-h2/ | 41G | 历史实验 |
| exp021_ragen_sft_v4/ | 23G | SFT 基础模型 (不能删) |
| exp029/ (seed1) | 21G | seed1 checkpoint |
| **总 checkpoints/** | **183G** | |

### 为什么每个 checkpoint 这么大

- 配置 `save_contents: ['model', 'optimizer', 'extra']` 保存完整 FSDP state
- 每个 checkpoint: model (~9G/rank × 2) + optimizer state (~1.5G/rank × 2) = ~21G
- `max_actor_ckpt_to_keep: 10`，但只有 5 个 checkpoint，所以没有自动清理触发

### 失败机制

1. 训练运行到 step 25，触发 `save_freq: 5` 保存 checkpoint
2. 先保存 model 部分: 18G 写入 `global_step_25/actor/` (成功)
3. 再保存 optimizer state dict: 需要 ~3-5G，此时磁盘剩余 < 6G
4. `torch.save` 写到一半磁盘满 -> `inline_container.cc` 报错
5. 两个 FSDP worker 同时写失败 -> Ray task error 级联

---

## 4. 其他两次错误的分析

### Run #1: CUDA OOM (已修复)

原始配置 (ppo_max_token_len=65536, 无 gradient_checkpointing) 导致的 GPU 内存不足。通过降低 token len 到 16384 + 启用 gradient_checkpointing **已修复**。最新运行证明训练可以正常跑 10+ step。

### Run #3: FSDP 设备不匹配

```
RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!
```

发生在 `actor_rollout_update_actor`。原因：step 15 的 checkpoint 是在 `optimizer_offload: true` 下保存的（optimizer state 在 CPU），但 resume 时 config 改为 `optimizer_offload: false`，FSDP 加载时 state dict 设备不匹配。

---

## 5. 推荐修复方案

### 方案 A: 清理磁盘 + 继续在 bjb1 跑 (最快)

1. **删除不需要的 checkpoint** 释放空间:
   ```bash
   # 删除 exp029-seed2 的旧 checkpoint (保留 step 20 用于 resume)
   rm -rf /root/autodl-tmp/checkpoints/exp029-seed2/global_step_5
   rm -rf /root/autodl-tmp/checkpoints/exp029-seed2/global_step_10
   rm -rf /root/autodl-tmp/checkpoints/exp029-seed2/global_step_15
   rm -rf /root/autodl-tmp/checkpoints/exp029-seed2/global_step_25  # 不完整，已损坏
   # 释放 ~63G
   
   # 如果 hsweep-h2 不再需要:
   rm -rf /root/autodl-tmp/checkpoints/hsweep-h2/  # 释放 41G
   ```
2. **减少 checkpoint 保存内容**:
   - 改 `save_contents: ['model', 'extra']` (不保存 optimizer state)
   - 或改 `max_actor_ckpt_to_keep: 3` 自动清理旧的
3. **从 step 20 resume** (latest_checkpointed_iteration=20)

### 方案 B: 转到 westd-47453 (更稳妥)

westd-47453 有 4× RTX PRO 6000，如果磁盘空间更大，可以避免此问题。但需要先确认磁盘空间和环境就绪。

### 方案 C: 只保存 model，跳过 optimizer (最小改动)

修改 `save_contents` 从 `['model', 'optimizer', 'extra']` 改为 `['model', 'extra']`。每个 checkpoint 从 ~21G 降到 ~18G。但这意味着 resume 时 optimizer state 从头初始化，对于 constant lr + 短训练影响不大。

---

## 6. 结论

**exp029_seed2 的 OOM 问题早已解决。** 最近 3 次失败中有 2 次是磁盘空间不足，1 次是 FSDP resume 设备不匹配。核心问题是 250G 磁盘被 183G checkpoint 占满，`torch.save` 写不完就崩溃。

训练本身表现正常: 10 个 step 顺利完成，success rate 从初始水平上升到 37.5%，梯度和 loss 均正常。

**建议优先执行方案 A**：删除旧 checkpoint 释放 ~60-100G 空间，同时调整 `max_actor_ckpt_to_keep: 3`，然后从 step 20 resume。
