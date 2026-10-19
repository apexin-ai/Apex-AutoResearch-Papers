# bjb1-18228 关键实验状态核查 (UTC 2026-05-24 19:27)

## 摘要

| 实验 | 状态 | 关键结论 |
|------|------|---------|
| train-crm-pi05-unified-3suite-r2 | **RUNNING** | epoch 24/50, best val_loss=0.004856 (epoch 23), ETA ~10h |
| eval-supp-spatial-vla-only-s42 | **DONE → registry updated** | SR=80.0% (160/200) |
| eval-supp-obj-vla-only-s50 | **DONE → registry updated** | SR=74.0% (148/200) |
| precompute-pi05-long-2048-r2 | **RUNNING** | PID 114507 存活 (已跑 2d 14h), 已写 175+ partial 文件 |
| precompute-pi05-object-2048-r2 | **COMPLETE** | obs_features.pt + k_samples.pt + expert_actions.pt 已生成 (2026-05-24 17:54) |

## GPU 占用 (4×RTX 4090 24GB)

| GPU | Util | Mem | 进程 |
|-----|------|-----|------|
| 0   | 10%  | 580 MiB  | π0.5 CRM 训练 (cached features → 显存极低) |
| 1   | 0%   | 0 MiB    | **空闲** |
| 2   | 0%   | 0 MiB    | **空闲** |
| 3   | 23%  | 9883 MiB | Long precompute (pi05 inference) |

→ **cuda:1 / cuda:2 完全空闲，可立即部署新作业。**

---

## 1. π0.5 CRM 训练 (最高优先级)

- **exp_id**: `train-crm-pi05-unified-3suite-r2`
- **PID 326310** (bash wrapper) 存活, **PID 326315** (python) 99% CPU 运行中
- **GPU**: cuda:0 (CUDA_VISIBLE_DEVICES=0)
- **数据**: 194,485 samples (object 72507 + spatial 60250 + goal 61728), K=10, obs_dim=2048
- **模型**: CRM 615,966 参数
- **进度** (来自 `/root/runs/.../train-crm-pi05-unified-3suite-r2.log`):
  - 已跑 **24/50 epochs**, 已耗时 **8h45m**
  - 每 epoch ~22 min (684 batches × 256 batch_size)
  - **best val_loss = 0.004856 @ epoch 23**, lr 现在 5.6e-4 (cosine 衰减)
  - 训练 loss 从 0.0146 → 0.0085 (稳定下降)
- **checkpoint dir**: `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/`
  - 已保存 epoch19/20/21/22/23 + `crm_best.pt` (2.4MB, 更新于 03:04)
- **预计完成**: 剩余 26 epochs × 22min ≈ **9.5h** → ETA 2026-05-25 ~13:00 UTC
- **timeout 限制**: 43200s = 12h；wrapper 启动于 ~18:35 UTC，timeout 截止约 06:35 UTC（**风险：可能在 epoch 35±2 时被 timeout 中断**）

⚠️ **建议**: 若需要训完 50 epoch，需在 timeout 触发前用 wrapper 显式延长或允许 resume；当前 `crm_best.pt` 已可作为可用 checkpoint。

---

## 2. eval-supp-spatial-vla-only-s42

- **已完成**, 退出日志 `logs/eval-supp-spatial-vla-only-s42.log` 显示 `Overall success rate (vla_only): 80.0% (160/200)`
- JSON: `logs/eval_spatial_vla_only_seed42.json` (mtime 05-25 02:20)
- 10 tasks × 20 rollouts, **最差任务**: `pick_up_the_black_bowl_on_the_ramekin` 0/20 (=0%)
- 其余 9 个任务 SR 在 0.7–1.0 之间
- **Registry 已更新**: PREPARING → QUEUED → RUNNING → DONE (conclusion=success)，metrics 已填，wall_clock=11293.8s

## 3. eval-supp-obj-vla-only-s50

- **已完成**, `Overall success rate (vla_only): 74.0% (148/200)`
- JSON: `logs/eval_object_vla_only_seed50.json` (mtime 05-25 02:44)
- 最差任务: butter 0.60, cream_cheese 0.60, milk/chocolate_pudding/soup 各 0.70
- 最好: bbq_sauce 0.95, orange_juice 0.85
- **Registry 已更新**: DONE, conclusion=success, wall_clock=11298.0s

---

## 4. Precompute 状态

### precompute-pi05-long-2048-r2  (RUNNING)
- PID **114507** 存活, 已运行 **2d 14h**, GPU 3 占 9.9GB
- cache dir: `/root/autodl-tmp/crm_cache_pi05_2048/long/` (790 MB)
- 当前最大 partial: `partial_s0_86500_87000.pt` (mtime 03:16 UTC，5min 前还在写)
- 未见 `obs_features.pt` / `k_samples.pt` 等合并文件 → 还没收尾

### precompute-pi05-object-2048-r2  (COMPLETE，无进程)
- cache dir: `/root/autodl-tmp/crm_cache_pi05_2048/object/` (1.3 GB)
- 最后 partial: `partial_s0_72500_72507.pt` (说明源 demos = 72,507 帧)
- **`obs_features.pt` + `k_samples.pt` + `expert_actions.pt` 已生成** → 完成
- 注: object cache 实际被 CRM 训练 (#1) 正在使用 (72507 samples 与训练日志匹配)

---

## 待办建议

1. ⚠️ **CRM 训练 timeout 风险**: 12h timeout 在 26 剩余 epoch 完成前到达。若需完整 50 epoch，需 (a) 提前 resume 准备，或 (b) 接受 `crm_best.pt` (epoch 23) 作为 final ckpt。
2. ✅ **cuda:1 / cuda:2 空闲**: 可立即部署其他 supp eval（如 8-seed 补全队列、pi05 ReconVLA cross-arch eval、tau sweep 等仍在 PREPARING 的实验）。
3. ⚠️ **Long precompute** 不阻塞训练（在 GPU 3，独立），但若需要 long benchmark 加入 CRM 训练数据集，需等其收尾合并。
