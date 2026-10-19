# exp029_episode_level 诊断报告 (attempt 4)

**时间**: 2026-05-16
**W&B run**: 6d4oml60 (exp029-alfworld-episode-level)

## 退出原因: CUDA OOM

崩溃点: `dp_actor.py:468` → `loss.backward()`

```
torch.OutOfMemoryError: CUDA out of memory.
Tried to allocate 9.27 GiB.
GPU 0 total: 94.97 GiB
  - 训练进程 (pid 889859): 55.41 GiB
  - Ray worker (pid 895287): 35.66 GiB
  - 空闲: 3.87 GiB
```

**根因**: GPU 0 上同时运行了训练进程和一个 Ray worker（可能是 ref model），两个进程合计占用 91 GiB。backward pass 需要额外 9.27 GiB 用于梯度计算，空间不足。

## 最后完成的训练步骤

**Step 1** (唯一完成的 step)
- 耗时: 1808.6s (~30min)
- response_length/mean: 12689, max: 16381
- total_tokens: 1,624,217
- train/AlfworldSG/success: 17.97%
- train/AlfworldSG/pass@8: 56.25%
- update_actor 耗时: 412.3s

崩溃发生在 **Step 2 的 update_actor 阶段**。

## Checkpoint 状态

**无可恢复 checkpoint**。`/root/autodl-tmp/` 下不存在 exp029 相关的 checkpoint 目录。仅有 exp019b 和 exp021 的旧 checkpoint。

## 当前服务器状态

- PID 889859 (主进程): 已死
- PID 895287 (Ray worker): 已死
- **残留进程**: PID 899940, 899941 (`ray::WorkerDict.ref_init_model`)，各占 ~7GB RSS + 1360 MiB GPU，已运行 ~1min，状态 SNl (stopped)
- 磁盘: /root/autodl-tmp 78% (57GB free) — 正常
- GPU: 当前基本空闲 (各 3 MiB used)

## 内存分析

训练配置:
- `ppo_max_token_len_per_gpu: 65536`
- `ppo_mini_batch_size: 32`, `micro_batch_size_per_gpu: 1`
- `context_window_mode: full`, `response_length: 16384`
- `batch_size: 128`, `env_groups: 16 × group_size: 8`
- FSDP on 2× RTX PRO 6000 (95GB each)
- `optimizer_offload: False`, `param_offload: False`

Step 1 侥幸通过，Step 2 backward pass 需要的峰值内存略高（可能因 response length 分布变化），导致 OOM。margin 非常小 (差 5.4 GiB = 9.27 - 3.87)。

## 修复建议

重启前必须:
1. **清理残留 Ray 进程**: `ray stop --force` 或 `kill -9 899940 899941`

降低显存峰值（任选一或多个）:
2. **启用 optimizer offload**: `optimizer_offload: True` — 将 Adam 状态卸载到 CPU，可节省 ~6-10 GiB/GPU
3. **降低 ppo_max_token_len_per_gpu**: 65536 → 49152 或 32768
4. **设置 PYTORCH_ALLOC_CONF=expandable_segments:True** — 减少碎片化
5. **启用 gradient checkpointing** (如未启用): 用计算换内存

推荐方案: **选项 2 + 4** 组合。optimizer offload 的性能损失较小（增加 ~10% 训练时间），但可释放足够内存覆盖 backward pass 峰值。expandable_segments 是零成本优化。

由于无 checkpoint，必须从头重训。
