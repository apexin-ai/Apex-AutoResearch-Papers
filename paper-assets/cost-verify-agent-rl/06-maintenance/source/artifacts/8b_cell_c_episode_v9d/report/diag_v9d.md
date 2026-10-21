# 诊断报告：8b_cell_c_episode_v9d

## 错误类型
**torch.save 序列化错误**（磁盘空间不足导致 zip 文件写入失败）

## 关键事实

- **训练本身成功运行了 5 步**（step 0–4），success rate: 40.6% → 62.5% → ... → 81.25%
- 崩溃发生在 **step 4 结束后保存 checkpoint (global_step_5)** 时，不是训练过程中
- v9c 的 prompt overflow 问题已修复（`max_prompt_length: 15360` 生效），这是**新问题**

## 完整 Traceback

```
File "/root/cost-verify-agent-rl/RAGEN/ragen/trainer/agent_trainer.py", line 1113, in _save_checkpoint
    self.actor_rollout_wg.save_checkpoint(actor_local_path, actor_remote_path, self.global_steps, ...)

ray::WorkerDict.actor_rollout_save_checkpoint() (pid=286421)
  File "/root/cost-verify-agent-rl/RAGEN/verl/verl/workers/fsdp_workers.py", line 1043, in save_checkpoint
    self.checkpoint_manager.save_checkpoint(...)
  File "/root/cost-verify-agent-rl/RAGEN/verl/verl/utils/checkpoint/fsdp_checkpoint_manager.py", line 244, in save_checkpoint
    torch.save(optimizer_state_dict, optim_path)
  File "torch/serialization.py", line 976, in save
    with _open_zipfile_writer(f) as opened_zipfile:
  File "torch/serialization.py", line 808, in __exit__
    self.file_like.write_end_of_file()
RuntimeError: [enforce fail at inline_container.cc:668] . unexpected pos 1647515200 vs 1647515088
```

4 个 worker 全部在保存 optimizer state dict 时失败，同一错误。

## 根因分析

### 直接原因
`torch.save` 使用 zip 格式写 optimizer state dict 时，zip 文件内部位置计数器 (1647515200) 与实际文件位置 (1647515088) 不一致（差 112 字节），导致写入终止。

### 根本原因：磁盘空间不足
- 数据盘 `/root/autodl-tmp`：250GB 总量，**当前已用 228GB (91%)**
- **checkpoints 目录占 174GB**：
  - `scienceworld_sft`: 108GB
  - `8b-cell-c-v9/global_step_5`: 37GB（本次部分写入）
  - `qwen3_8b_sft_v1`: 31GB
- 本次 checkpoint 写入前可用空间约 60GB，4 个 model shard (4×7.7GB=30.8GB) 成功写入后仅剩约 28GB
- 4 个 worker 同时写 optimizer shard 到同一 RAID (`/dev/md0`)，在 RAID 接近满时触发写入异常
- rank_1 的 optim 文件被截断：**990MB**（其他 rank 均为 1.6GB）

### 为什么不是 v9c 的问题
v9c 的 prompt overflow 已通过 `max_prompt_length: 15360` 修复。v9d 完整运行了 5 步训练+rollout，从未触发 prompt 溢出。

## Checkpoint 文件状态

```
global_step_5/actor/
  model_world_size_4_rank_0.pt   7.7G  ✓
  model_world_size_4_rank_1.pt   7.7G  ✓
  model_world_size_4_rank_2.pt   7.7G  ✓
  model_world_size_4_rank_3.pt   7.7G  ✓
  optim_world_size_4_rank_0.pt   1.6G  ✓（但可能已损坏）
  optim_world_size_4_rank_1.pt   990M  ✗ 截断
  optim_world_size_4_rank_2.pt   1.6G  ✓（但可能已损坏）
  optim_world_size_4_rank_3.pt   1.6G  ✓（但可能已损坏）
```

## 修复建议

### 方案 A：清磁盘 + 重跑（推荐）
1. 删除不再需要的旧 checkpoint（释放 ~139GB）：
   ```bash
   rm -rf /root/autodl-tmp/checkpoints/scienceworld_sft/     # 108GB
   rm -rf /root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/      # 31GB
   rm -rf /root/autodl-tmp/checkpoints/8b-cell-c-v9/          # 37GB（已损坏）
   ```
2. 从头重跑 v9d（或 v9e）

### 方案 B：跳过 optimizer 保存（如果不需要断点续训）
在 config 中将 checkpoint 只保存 model：
```yaml
actor_rollout_ref:
  actor:
    checkpoint:
      save_contents: ['model']
```
每个 checkpoint 从 ~37GB 降至 ~31GB，减少磁盘压力。

### 方案 C：增大保存间隔
当前 `save_freq: 5`，可改为 `save_freq: 10` 或 `save_freq: 15`，减少 checkpoint 次数。

### 综合推荐
**A + B + C 组合**：先清磁盘，然后 `save_contents: ['model']` + `save_freq: 10`，确保 30 步训练期间磁盘充足。每个 checkpoint ~31GB × max_keep 5 = 155GB，清理后有 ~190GB 可用，足够。
