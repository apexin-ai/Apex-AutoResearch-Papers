# crm-train-pi05-spatial-v2 诊断报告

**日期**：2026-05-22
**服务器**：bjb1-18228
**结论（一句话）**：**报告的"v2 反复崩溃 / spatial-full FileNotFoundError"两条都与服务器实况不符。** v2 实验在服务器上根本不存在；spatial-full 已经训练完成（成功）。

---

## 1. 根因（root cause）

### 1.1 `crm-train-pi05-spatial-v2` 不存在
```
$ find /root -maxdepth 5 -name "*spatial-v2*"
(空)
```
- `/root/runs/acr-vla-conformal-refinement/` 下没有 `crm-train-pi05-spatial-v2.log`
- 没有 v2 相关的 checkpoint 目录
- GPU 全空闲（`No running processes found`），不存在"反复崩溃"的活动进程
- **可能性**：跟踪面板里的"v2 失败 5 次"是状态记录错误（重命名、stale entry，或与另一台服务器混淆）

### 1.2 `crm-train-pi05-spatial-full` 实际已成功
`tail -200 /root/runs/acr-vla-conformal-refinement/crm-train-pi05-spatial-full.log`：
```
Epoch 50/50  train_loss=0.010603  val_loss=0.006139  lr=0.00e+00

[train] Done. Best val_loss=0.006138
[train] Checkpoints at /root/autodl-tmp/checkpoints/crm_pi05_full/spatial/
EXIT_CODE=0
```
- 完成时间：May 22 09:09
- 最佳 val_loss = **0.006138**（与 object 的 0.004018 在同一量级，正常）
- Checkpoint `crm_best.pt` (2.5MB) + `checkpoint_epoch00{46-50}.pt` 全部落盘

启动 args 显示 cache 路径已经从老的 `/root/autodl-tmp/crm_cache/` 切换到新的 `/root/autodl-tmp/crm_cache_pi05/`：
```
'cache_dir': '/root/autodl-tmp/crm_cache_pi05/', 'benchmark': ['spatial'],
'input_mode': 'full', 'K': 10, 'obs_dim': 2048
```

### 1.3 "spatial FileNotFoundError" 是过期信息
Cache 现在存在并完整：
```
/root/autodl-tmp/crm_cache_pi05/spatial/
  manifest.json     {"benchmark": "spatial", "n_samples": 60250, "K": 10, "obs_dim": 2048, "action_dim": 6, "h_eff": 5}
  obs_features.pt   493MB
  k_samples.pt      72MB
  expert_actions.pt 7.2MB
  partial_s{0..6}_*.pt  (precompute 分片，已合并)
```
- 早期失败信息里截断的路径 `/root/autodl-tmp/crm_c...` 极可能是 `crm_cache/`（旧目录，下面 spatial 子目录是空的，stale legacy）。precompute 流水线把数据写到了 `crm_cache_pi05/`，**与训练脚本读取的路径一致**，所以训练能正常起来。
- 旧目录 `/root/autodl-tmp/crm_cache/spatial/`（空，May 14 创建）建议清理掉以免再误导。

---

## 2. 日志关键原文

**spatial-full 收尾段**：
```
Epoch 48/50  train_loss=0.010569  val_loss=0.006139  lr=3.94e-06
  → New best val_loss: 0.006139
Epoch 49/50  train_loss=0.010566  val_loss=0.006138  lr=9.87e-07
  → New best val_loss: 0.006138
Epoch 50/50  train_loss=0.010603  val_loss=0.006139  lr=0.00e+00
[train] Done. Best val_loss=0.006138
EXIT_CODE=0
```

**spatial-full 启动段**：
```
[train] Loading cache (spatial): 60250 samples, K=10, obs_dim=2048
[train] Total: 60250 samples from 1 benchmark(s)
[train] CRM parameters: 615,966
[train] Norm stats set: mean [-29.4758, 14.9303], std [0.0039, 6.8695]
```

**资源状态**：
- 4× RTX 4090 (24GB)，全空闲，温度 28–29°C
- 系统盘 30G，使用 53% (15G 可用)
- 数据盘 250G，使用 65% (89G 可用)

---

## 3. 修复建议

按优先级：

### 3.1 立即：更新追踪状态
v2 不需要修复，因为它**根本没跑过**。建议：
- 检查任务调度系统（roadmap / runs 表）里 `crm-train-pi05-spatial-v2` 的来源
- 将 `crm-train-pi05-spatial-full` 状态标记为 **completed**（best_val_loss=0.006138，checkpoint 在 `/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt`）

### 3.2 后续：下游可以直接评估
```bash
ls /root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt
# 直接喂给 eval 脚本即可，无需重训
```

### 3.3 清理：删除空的 stale cache 目录
```bash
rm -rf /root/autodl-tmp/crm_cache/spatial   # 空目录，截断 FileNotFoundError 的元凶
```
（保留 `crm_cache_pi05/` 不动）

### 3.4 如果确实想跑一个 v2（变体实验）
确认变体目的（不同 K、不同 obs_dim、不同 aug 配置？）后再启动，复用现有 cache：
```bash
cd /root/acr-vla-conformal-refinement
nohup python src/train_crm.py \
  --benchmark spatial \
  --cache_dir /root/autodl-tmp/crm_cache_pi05/ \
  --output_dir /root/autodl-tmp/checkpoints/crm_pi05_v2/spatial/ \
  --epochs 50 --batch_size 32 --lr 1e-3 --K 10 \
  > /root/runs/acr-vla-conformal-refinement/crm-train-pi05-spatial-v2.log 2>&1 &
```

---

## 4. 是否需要重新 precompute spatial features

**不需要。** Spatial cache 完整且与训练脚本期望的格式一致（60250 samples，K=10，obs_dim=2048，所有 partial shards 已合并为 obs_features.pt / k_samples.pt / expert_actions.pt），spatial-full 训练成功就是证据。

---

## 5. 给请求方的提示

如果"v2 死了 5 次"这条信息确有出处（dashboard / 监控日志），请提供来源，可能是：
- 跨服务器混淆（v2 实际在另一台机器上跑？项目默认服务器是 bjb2-40593，但任务指向 bjb1-18228）
- 监控误把 spatial-full 的中间进程退出/重启误标为 v2 的失败
- 旧的 v1 / v2-obs-only / v2-perdof / v2-scalar-unc（5月14日那批 5KB 左右的失败日志）被误识别为新的 v2
