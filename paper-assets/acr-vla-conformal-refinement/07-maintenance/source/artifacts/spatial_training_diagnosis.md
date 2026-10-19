# crm-train-pi05-spatial-full 诊断报告

诊断时间：2026-05-22 03:10（服务器：bjb1-18228）

## 结论一句话

**Spatial 训练启动后 3 秒就因 cache 不完整而崩溃，目前未在跑。** Object 训练正常（cuda:0, PID 800111, epoch 7）。Spatial 预计算只完成 7/10 个 shard，没有 merge 步骤，缺 `manifest.json`。

## 1. 进程状态：未启动（崩溃即退）

`nvidia-smi`：cuda:1 完全空闲（0 MiB, 0% util）；只有 cuda:0 上的 object 训练（PID 800111）在跑。

`ps aux`：没有任何 spatial 相关 Python 进程；ROADMAP 记录的 PID 795051 已不存在；老的启动器 bash（PID 800105）只启了 object 一个，没有 spatial 启动指令。

`tmux ls`：无 tmux 会话。

## 2. 日志证据：FileNotFoundError

`/root/runs/acr-vla-conformal-refinement/crm-train-pi05-spatial-full.log` 显示 spatial 训练在 **2026-05-22 03:09:45 启动**，**3 秒后 03:09:48 崩溃**：

```
[train_crm] args: {'benchmark': ['spatial'], 'cache_dir': '/root/autodl-tmp/crm_cache_pi05/', ...}
[train_crm] device: cuda
Traceback (most recent call last):
  File "/root/acr-vla-conformal-refinement/src/train_crm.py", line 329, in train
FileNotFoundError: No precomputed cache at /root/autodl-tmp/crm_cache_pi05/spatial.
              Run with --precompute first, or use --auto.
EXIT_CODE=1
```

`train_crm.py:325-331` 的检查逻辑：训练前必须存在 `cache_dir/<benchmark>/manifest.json`。spatial 目录里没有这个文件。

## 3. Checkpoint 状态：空目录

`/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/` 存在但完全为空（由 object 启动脚本 02:21 的 `mkdir -p` 顺手创建）。**未产生任何 checkpoint。**

## 4. 预计算数据：不完整（缺 3/10 shard 且未 merge）

对比 object（可用）vs spatial（不可用）的 `/root/autodl-tmp/crm_cache_pi05/`：

| 项 | object（✅ 可用） | spatial（❌ 不可用） |
|---|---|---|
| `manifest.json` | 有 | **缺失** |
| `obs_features.pt`（merge 后） | 有 | **缺失** |
| `k_samples.pt`（merge 后） | 有 | **缺失** |
| `expert_actions.pt`（merge 后） | 有 | **缺失** |
| partial shards | s0~s9 全 | **只有 s0~s6** |
| s6 最后一个 partial | n/a | `partial_s6_8500_8607.pt`（02:17 完成） |

Spatial 只跑了 7/10 个 shard 的预计算，且没有触发最后的 merge 步骤。

## 5. 未启动的真正原因

回看 02:21 的启动器 bash 命令（PID 800105），里面只有 object 的 nohup 启动，**根本没有 spatial 的启动指令**。说明当时的 submit 调用要么只提交了 object，要么 spatial 的提交被跳过了（可能因为预计算未完成所以前置检查失败）。

而 spatial 日志在 03:09:45 创建——这次启动是**另一次独立尝试**（很可能是 submit_training_job 把 PREPARING 状态转成实际启动时），但此时预计算仍未完整 + 未 merge，于是立即崩溃。

## 6. 建议的下一步

按顺序执行：

1. **补完 spatial 预计算**：先跑剩余 3 个 shard
   ```bash
   for s in 7 8 9; do
     nohup python -u src/train_crm.py --precompute --benchmark spatial \
       --cache_dir /root/autodl-tmp/crm_cache_pi05/ --model pi05 \
       --num_shards 10 --shard_id $s --precompute_batch_size 4 \
       > /root/runs/acr-vla-conformal-refinement/precompute-pi05-spatial-shard${s}.log 2>&1 &
   done
   ```
   注意 cuda:0 上 object 训练只用 ~548 MiB，cuda:1 完全空闲，可在 cuda:1 上跑 precompute。

2. **预计算完成后触发 merge**：再以 `--num_shards 10 --shard_id 0` 或类似方式让脚本走 merge 分支，产出 `manifest.json` + `obs_features.pt` + `k_samples.pt` + `expert_actions.pt`。（需要看脚本 merge 触发条件——目前看下来当 `--num_shards>1` 时会自动合并所有 shard）

3. **重新启动 spatial 训练**：
   ```bash
   nohup env CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial \
     --cache_dir /root/autodl-tmp/crm_cache_pi05/ \
     --output_dir /root/autodl-tmp/checkpoints/crm_pi05_full/spatial/ \
     --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 2048 \
     > /root/runs/acr-vla-conformal-refinement/crm-train-pi05-spatial-full.log 2>&1 &
   ```

4. **更新 registry / ROADMAP**：把 PREPARING 状态改成 FAILED（崩溃原因记下），等预计算补完后再切回 RUNNING。把过时的 PID 795051 清掉。

5. **修 submit_training_job 的前置检查**：理想情况下，提交训练前应该检查 cache 完整性（`manifest.json` 是否存在），否则不应该把 job 状态置为 PREPARING/RUNNING，而应该直接拒绝。
