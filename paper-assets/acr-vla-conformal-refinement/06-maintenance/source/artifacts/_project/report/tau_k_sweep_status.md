# τ-sweep + K-sweep + K=5 状态收割

**收割时间**：2026-05-25 ~04:15

## Part A: bjb1-32546

### GPU 与进程状态
- **6×GPU 全部空闲**（0% util，1MB used / 24564MB）
- 无 python 实验进程（仅 jupyter-lab + tensorboard 守护）
- 无 tmux 会话
- **结论**：τ-sweep + K-sweep 已全部完成，机器现在 idle

### τ-sweep（Spatial, seed=42, n_rollouts=20, norm=0.2）

| τ    | SR     | trigger_rate | crm_applied_steps / total | mean_unc | 状态 |
|------|--------|--------------|---------------------------|----------|------|
| 0.10 | 79.0%  | 75.2%        | 21937 / 29185             | 0.1845   | done |
| 0.15 | **80.5%** | 40.7%     | 11539 / 28385             | 0.1852   | done |
| 0.20 | **81.0%** | 26.6%     | 7498 / 28162              | 0.1876   | done |
| 0.25 | 79.5%  | 19.6%        | 5610 / 28550              | 0.1857   | done |
| 0.30 | 80.5%  | 16.7%        | 4764 / 28467              | 0.1922   | done |

**JSON 路径**：`logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau{0.1,0.15,0.2,0.25,0.3}_seed42.json`

**观察**：
- SR 在 τ=0.20 达峰（81.0%），与 τ=0.25 / 0.30 几乎打平（80.5% 上下）
- 触发率随 τ 单调下降（75% → 17%），SR 却基本平稳 → 高触发率下 CRM 修正并未带来额外增益
- τ=0.10 触发率 75% 但 SR 只有 79%，反而是最低的 → 过度修正
- "ramekin" 任务在所有 τ 下都 0/20 → 与 τ 无关的系统性失败

### K-sweep（Spatial, seed=42, n_rollouts=20）

| K    | 模式                         | seed | SR    | 状态 |
|------|------------------------------|------|-------|------|
| 1    | adaptive_conformal_crm (τ=0.25) | 42   | 79.5% | done（与 τ=0.25 同一 JSON） |
| 2    | vla_only mean baseline        | 46   | 80.0% | done（注意：mean 基线非 conformal） |
| 5    | adaptive_conformal_crm (τ=0.25) | 42   | —     | **running on bjb2-40593** |

**注意**：
- K=1 实际复用了 τ=0.25 单样本结果（log 文件 `eval-adaptive-k1-spatial-s42.log` 写入了同名 JSON）
- K=2 的可用文件是 `eval_spatial_k2mean_seed46.json`（seed 46，vla_only mean），**没有 seed 42 且非 conformal CRM 版本** → 不能直接和 K=1/K=5 比较
- 若要正式 K-sweep 对比，建议在 bjb1 补跑 K=2 adaptive_conformal_crm seed=42

---

## Part B: bjb2-40593（K=5 实验）

### GPU 与进程状态
- **GPU 0** 占用：27% util，2769MB used
- 运行中：tmux session `k5-spatial-s42`，PID 289696
- 启动时间：2026-05-25 00:57:46（已运行 ~3h13m，CPU time 904m）

### 命令
```bash
CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py \
  --mode adaptive_conformal_crm \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt \
  --conformal_threshold 0.25 --benchmark spatial --seed 42 \
  --n_rollouts 20 --max_correction_norm 0.2 --K 5
```

### 当前进度（7 任务 done + 第 8 任务进行中）

| # | 任务                                | 状态        | SR        |
|---|-------------------------------------|-------------|-----------|
| 1 | between_plate_and_ramekin           | done        | 19/20 95% |
| 2 | next_to_ramekin                     | done        | 18/20 90% |
| 3 | from_table_center                   | done        | 20/20 100%|
| 4 | on_the_cookie_box                   | done        | 20/20 100%|
| 5 | in_the_top_drawer_of_wooden_cabinet | done        | 13/20 65% |
| 6 | on_the_ramekin                      | done        | 0/20 0%   |
| 7 | next_to_the_cookie_box              | done        | 19/20 95% |
| 8 | on_the_stove                        | rollout 15/20 (11/15) | — |
| 9 | next_to_the_plate                   | pending     | —         |
| 10| on_the_wooden_cabinet               | pending     | —         |

**当前累计**：109/140 已完成（77.9%）
**ETA**：约 50-60 分钟（按 ~24 min/任务 + 当前任务剩 5 rollouts × 2.4 任务量推算）

---

## Part C: 空闲资源汇总

| 服务器       | 空闲 GPU | 显存可用 / 卡 | 备注 |
|--------------|----------|---------------|------|
| bjb1-32546   | 6×       | 24GB          | 完全空闲，可立即接新任务 |
| bjb2-40593   | 0×       | 24GB          | GPU 0 跑 K=5，~1h 后释放 |

## Part D: 建议下一步

1. **bjb1 立即可用**：6 张 GPU 全空，可以补 K=2 adaptive_conformal_crm seed=42 的缺口，以及多 seed 重复以做 error bar
2. **K=5 结果出来后**：写完 K∈{1,2,5} 对比表，再判断是否需要 K=10 / K=20
3. **τ 最优值**：当前数据支持 τ=0.20 作为最优（SR 81.0%，触发率 26.6% 兼顾效率），可作为主结果汇报
