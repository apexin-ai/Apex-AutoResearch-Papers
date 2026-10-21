# π0.5 Spatial CRM 训练缓存路径诊断

**Server**: bjb1-18228  **Date**: 2026-05-22 05:30 (Asia/Shanghai)

## 结论：问题已自动修复，无需人工干预

原报告 `FileNotFoundError: No precomputed cache at /root/autodl-tmp/crm_cache_pi05/spatial` 是**历史快照**。Spatial precompute 已在 03:23 完成，training 已重启并稳定运行。

## 实际目录结构

```
/root/autodl-tmp/crm_cache_pi05/
├── object/    1.3G   (上次修改 05-22 02:52)
└── spatial/   1006M  (上次修改 05-22 03:23)
```

**Spatial cache 关键文件**：
- `manifest.json` — `{"benchmark":"spatial","n_samples":60250,"K":10,"obs_dim":2048,"action_dim":6,"h_eff":5}`
- `obs_features.pt` (494 MB)
- `k_samples.pt` (72 MB)
- `expert_actions.pt` (7.2 MB)
- 99 个 `partial_s0..s6_*.pt` shards（已完成合并基础）

路径**完全正确**，训练脚本传入 `--cache_dir /root/autodl-tmp/crm_cache_pi05/` + `--benchmark spatial` → 命中 `crm_cache_pi05/spatial/`。

## Spatial Training 当前状态（运行中）

进程：`python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_pi05/ --output_dir /root/autodl-tmp/checkpoints/crm_pi05_full/spatial/ --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 2048`（tmux: `crm-train-pi05-spatial-full`，CUDA_VISIBLE_DEVICES=1）

启动时间：03:09:45  日志最后写入：05:30:08

| Epoch | train_loss | val_loss | 备注 |
|-------|-----------|----------|------|
| 1     | 0.018011  | 0.009994 | best |
| 2     | 0.017181  | 0.009440 | best |
| 15    | 0.013772  | 0.007799 | best |
| 16    | 0.013585  | 0.007745 | best (latest) |
| 17    | running   | -        | batch 450/1695 |

`[train] Loading cache (spatial): 60250 samples, K=10, obs_dim=2048` ✅

## Object Training 当前状态（PID 800111，运行中）

进程已运行 3h 07min。CUDA_VISIBLE_DEVICES=0。

| Epoch | train_loss | val_loss | 备注 |
|-------|-----------|----------|------|
| 21    | 0.008590  | 0.004751 | - |
| 22    | 0.008599  | 0.004617 | best (latest) |
| 23    | running   | -        | batch 300/1950 |

两者均健康收敛，loss 持续下降。

## 时间线还原

1. **~02:21** crm-train-pi05-object-full.log 创建，object training 启动
2. **02:52** object cache 最后写入完成
3. **03:09:45** crm-train-pi05-spatial-full.log 创建（首次启动，触发 FileNotFoundError——此时 spatial precompute 还未跑完最后一个 shard）
4. **~02:17–03:23** spatial precompute shard6 跑完（见 precompute-pi05-spatial-shard6.log，EXIT_CODE=0，耗时 16112s）
5. **03:23** spatial cache 目录最后写入完成（合并/写 manifest）
6. **03:23 后** spatial training 被重启（pipeline-auto 或人工），从 epoch 1 跑起，目前 epoch 17

## 建议的修复命令

**无需修复**。如果未来再遇到类似问题，排查清单：

```bash
# 1. 验证 cache manifest 存在且 n_samples 合理
cat /root/autodl-tmp/crm_cache_pi05/<benchmark>/manifest.json

# 2. 检查 partial shards 数量
ls /root/autodl-tmp/crm_cache_pi05/<benchmark>/partial_s*.pt | wc -l

# 3. 验证 precompute 是否真的退出成功
grep "EXIT_CODE" /root/runs/acr-vla-conformal-refinement/precompute-pi05-<benchmark>-shard*.log

# 4. 启动前等待 precompute EXIT_CODE=0
```

更深一层的根因：pipeline 在 spatial precompute 未完成时就触发了 spatial training。如果这是 crm-pipeline-auto.log 调度的，需要在 pipeline orchestrator 中加 precompute 完成依赖检查（监控 EXIT_CODE=0 或 manifest.json 存在），而不是按固定时序触发。
