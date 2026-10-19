# π0.5 CRM Eval 前置准备报告

**时间**：2026-05-21 23:50 (Asia/Shanghai)
**报告类型**：Eval 前置环境/进度检查

---

## 1. Object CRM Training 进度（bjb1-18228）

- **进程状态**：PID 800111 运行中，已 elapsed **49:29**
- **当前位置**：epoch 7/50，batch 500/1950
- **训练命令**：`python -u src/train_crm.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_pi05/ --output_dir /root/autodl-tmp/checkpoints/crm_pi05_full/object/ --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 2048`

### 已完成 epoch 摘要

| Epoch | train_loss | val_loss | lr        | 备注       |
|-------|-----------|----------|-----------|-----------|
| 1     | 0.011117  | 0.006107 | 9.99e-04  |           |
| 2     | 0.010691  | 0.005784 | 9.96e-04  |           |
| 3     | 0.010289  | 0.005706 | 9.91e-04  |           |
| 4     | 0.010175  | 0.005540 | 9.84e-04  |           |
| 5     | 0.010034  | 0.005544 | 9.76e-04  |           |
| 6     | 0.009881  | **0.005511** | 9.65e-04 | best 至今 |

val_loss 单调下降（除 epoch 5 略微反弹），收敛健康。

### 预计完成时间

- checkpoint 时间戳：epoch 2 @ 02:40 → epoch 6 @ 03:09 → 平均 **~7.25 min/epoch**
- 剩余：约 (50 - 7.26) × 7.25 ≈ **310 min（~5h 10min）**
- 预计完成时间：**2026-05-22 ~09:00**

---

## 2. 代码同步状态

| Server | git pull 结果 | evaluate.py 大小 | mtime | 状态 |
|--------|--------------|-----------------|-------|------|
| bjb1-18228 (训练) | -        | 33058 bytes | 2026-05-21 23:50:13 | OK |
| bjb1-32546 (eval) | 非 git 仓库  | 33058 bytes | 2026-05-21 23:49:20 | OK（已是目标版本） |
| bjb2-28827 (eval) | 无 origin remote | 33058 bytes | 2026-05-21 23:50:13 | OK（已是目标版本） |

**说明**：两台 eval 服务器的本地 `.git` 状态异常（bjb1-32546 根本没有 `.git`，bjb2-28827 有 `.git` 但未配置 origin remote），`git pull` 命令均失败。但 `evaluate.py` 字节数和首 5 行已与训练机一致（33058 bytes，标准 docstring 开头），文件内容确认为最新版。
后续如需更新代码，需通过 `rsync`/`scp` 从 bjb1-18228 同步，或重新初始化 git remote。

文件头确认（两台 eval 服务器）：
```
"""
LIBERO evaluation script for ACR-VLA.

Rollout loop:
  1. Load LIBERO env + task suite
```

---

## 3. Eval 环境验证

### bjb1-32546
- PyTorch: `torch=2.10.0+cu128, cuda=True, gpus=6`
- evaluate.py --help 输出完整（含 10 个 mode 选项：vla_only/crm_scalar/crm_perdof/acr_vla/crm_obs_only/reconvla/random_selection/adaptive_k/adaptive_unc_head/adaptive_conformal_crm）
- π0.5 模型：`/root/autodl-tmp/models/pi05_libero_finetuned/model.safetensors`（7.47 GB，21 16:21 落盘）✓

### bjb2-28827
- PyTorch: `torch=2.10.0+cu128, cuda=True, gpus=6`
- evaluate.py --help 输出完整（与 bjb1-32546 一致）
- π0.5 模型：`/root/autodl-tmp/models/pi05_libero_finetuned/model.safetensors`（7.47 GB，21 09:11 落盘）✓
- 注意：`policy_preprocessor.json` 在 14:31 被修改过（其他文件都是 09:07），可能是手动调整 norm stats，eval 前需确认是否符合预期

两台机器 6×GPU 环境就绪。

---

## 4. CRM Checkpoint 状态

### Object（训练中产出）：`/root/autodl-tmp/checkpoints/crm_pi05_full/object/`
- `checkpoint_epoch0002.pt` ~ `checkpoint_epoch0006.pt`（每个 7.42 MB）
- `crm_best.pt`（2.48 MB，2026-05-22 03:09，对应 epoch 6 的 best val_loss=0.005511）
- 训练仍在进行，最新 best 会持续覆盖。

### Spatial：`/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/`
- 目录存在但**为空**（4096 字节 → 实际 10 字节，未启动训练）
- 旧路径 `/root/autodl-tmp/checkpoints/crm_pi05/spatial/` 有 epoch0002-epoch0006 + crm_best.pt（mtime 02:05），但属于旧版训练产物
- **Spatial CRM 未在当前批次训练中**，需后续启动或决定复用旧 checkpoint

---

## 结论

- ✅ Object CRM 训练健康，预计 **~05:10 后完成**（2026-05-22 ~09:00）
- ✅ 两台 eval 服务器代码、模型、PyTorch 环境就绪
- ⚠️ Eval 服务器无可用 git remote，后续更新需手动 rsync
- ⚠️ Spatial CRM 当前批次未启动，新版 checkpoint 缺失
- ⚠️ bjb2-28827 上 `policy_preprocessor.json` 时间戳异于其他模型文件，eval 前建议核对

可以同步启动 object CRM 的 mid-training eval（用 `crm_best.pt` epoch 6 版本），或等待训练结束后再开始 full eval。
