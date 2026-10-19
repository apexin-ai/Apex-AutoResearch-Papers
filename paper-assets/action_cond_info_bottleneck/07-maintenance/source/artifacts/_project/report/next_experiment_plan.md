# Next Experiment Plan — Post-v5_div_reg

> 生成时间: 2026-05-16  
> 目标会议: **CoRL 2026** — abstract 5/26 (T-10 天), paper 5/29 (T-13 天)  
> 硬件: 2× RTX PRO 6000 96GB @ westb-13953 (cuda:0, cuda:1)  
> 状态前提: `acib_v5_div_reg` (seed 1, seed=42) ETA 07:40 UTC 完成, `acib_v5_div_reg_seed2` 已 failed (EXIT_CODE=129, 需重启)

---

## 0. 核心 narrative 与实验映射

CoRL story 三句话：
1. **Problem**: 64-token compact visual regime 下，VLA 对视觉扰动脆弱；data-aug (smolvla_libero_plus) 是已知补救，但需要扰动池且不可解释。
2. **Method**: ACIB 用 action-conditioned token scorer + aggregate-rate IB + diversity regularizer，提供 IB-grounded 正则化 + 可解释 token importance maps。Soft (S) vs Hard (H) 双模式。
3. **Claim**: ACIB 与 data-aug **正交互补** — ACIB-S on top of smolvla_libero_plus 进一步提升鲁棒性；64-token regime 下 soft 优于 hard。

每个 claim 对应必做实验：
| Claim | 实验 | 优先级 |
|-------|------|--------|
| ACIB-S 能提升 vs std baseline | v5_div_reg eval (2 seeds) | P0 |
| 64-token 下 soft > hard | ACIB-H + ACIB-S 对比 | P0 |
| ACIB ⟂ data-aug | ACIB-S on smolvla_libero_plus | P0 |
| 每个 loss 组件都必要 | VIB-only / Consistency-only / No-div 消融 | P1 |
| Method 选择合理 | Soft-vs-Hard 分析、token importance maps | P2 |

---

## 1. v5_div_reg 完成后的 eval 计划 [P0, 立即执行]

### 1.1 Checkpoint 选择
- **首选**: `outputs/acib_v5_div_reg/checkpoint_final` (20k steps)
- **备份**: `checkpoint_15000` — 防止 final 出现训练末期退化
- 选择标准: 同时满足 `scorer_std > 0.05` 且 `task_loss` 不高于训练初期 1.5x
- 启动前必查: `ls /root/acib/outputs/acib_v5_div_reg/checkpoint*` 确认存在

### 1.2 评测矩阵
| Suite | Episodes/task | 总 ep | Baseline 对照 |
|-------|---------------|-------|---------------|
| libero_spatial | 50 | 500 | std=66.0% |
| libero_object | 50 | 500 | std=67.8% |
| libero_goal | 50 | 500 | std=76.4% |
| libero_10 | 50 | 500 | std=待补全 (失败需重跑) |
| **小计 (标称)** | | **2000** | |
| **LIBERO-Plus (4 视觉维度) 可选** | 50 | 8000 | std plus eval 仍在进行 |

**决策**: 第一轮**只跑标称 4 suites** (~5-8h) — 拿到核心数 vs std baseline；LIBERO-Plus 扰动放第二轮。理由：abstract 阶段只需 "ACIB-S 不损害标称 + ≥2 suites 显著提升" 这一条 claim 的证据。

### 1.3 GPU 分工
| GPU | 任务 | ETA |
|-----|------|-----|
| cuda:0 | seed1 eval: spatial + object (1000 ep) | 2.5-4h |
| cuda:1 | seed1 eval: goal + libero_10 (1000 ep) | 2.5-4h |

### 1.4 同时启动 seed2 重训（覆盖前一次 failed）
seed2 在 cuda:1 eval 完成后立即启动训练（~11h），seed1 eval 完成后 cuda:0 启动 ACIB-H 训练（见 §2）。

**C001 合规**: 启动前 `ps aux | grep acib_v5_div_reg_seed2` 确认无残留进程。

### 1.5 Pass 判定（决定后续是否继续）
- 标称回退 < 2% (4 suites 全部满足)
- ≥ 2/4 suites 较 std 提升 ≥ 5% abs，或全部至少不退步
- scorer_std 在 final ckpt 仍 > 0.05（验证训练态保留到推理）

**Fail-safe**: 若 seed1 eval 严重回退，立即用 `checkpoint_15000` 重测一次；仍 fail 则停掉 seed2 重启，进入 v6 设计而非继续刷参数。

---

## 2. ACIB-H 实验 [P0]

### 2.1 训练配置
基于 v5_div_reg 唯一改动 `mode=hard, top_k_ratio=0.8`，其余 (β=0.01, β_warmup=1000, α=0.01, diversity_lambda=0.1, aggregate-rate KL) 全部继承。Straight-through estimator 已实现，无需修改代码。

| 参数 | 值 | 备注 |
|------|-----|------|
| mode | hard | --- |
| top_k_ratio | 0.8 | 首选 k；与 64-token regime 匹配 (保留 ~51 tokens) |
| 其他 | 同 v5_div_reg | --- |

**k=0.7 作为后续 sweep**（如时间允许，§7）。先不做 k=0.6/0.9，时间不允许。

### 2.2 训练 + eval 流程
| 阶段 | GPU | 时间 |
|------|-----|------|
| ACIB-H @ k=0.8 训练 | cuda:0 (seed1 eval 完成后) | ~11h |
| ACIB-H eval (4 suites 标称) | 2× GPU 分 spatial/object vs goal/long | ~5-8h |

**总 ~16-19h on 1 GPU 等效。** 单 seed 即可（abstract 阶段），seed2 视时间补。

### 2.3 与 ACIB-S 对比计划
对比指标（表格化进论文 §4.2）:
- Per-suite SR (标称)
- Δ vs std baseline
- 推理时 scorer logit 分布 (soft) vs gate ratio (hard) — 验证 hard 真在裁剪
- 推理时 wall-clock（hard 理论上可加速，但 64 tokens 收益小）

**假设**: 64-token regime 下 soft 优于 hard（信息已压缩到极限，hard discretization 损失大）。若结果反向，论文 framing 调整为 "hard 在 token 维度更稀疏时退化更明显"。

---

## 3. 消融实验优先级 [P1]

所有消融均基于 v5_div_reg 配置，单 seed=42，单 suite=libero_spatial（节省 GPU），训练 + eval 共 ~14-16h/实验。

| 顺序 | 实验 | 配置改动 | 目的 | 时间 |
|------|------|----------|------|------|
| **A1** | **No-div** | `diversity_lambda=0` | 复现 v4_agg_kl 的 collapse，证明 diversity reg 是 anti-collapse 关键 | 跳过训练，直接引用 `acib_v4_agg_kl` 已 logged scorer_std=0.009 数据；只 eval 该 ckpt 比对 SR ⇒ **0 GPU-h 训练 + 3-4h eval** |
| **A2** | **VIB-only** | `α=0` (consistency 关闭) | 证明 consistency loss 对 perturbation robustness 必要 | 11h 训练 + 3-4h eval (单 suite) |
| **A3** | **Consistency-only** | `β=0` (整段, 不只是 warmup) | 证明 IB term 对 sparsity / token importance 必要 | 11h 训练 + 3-4h eval (单 suite) |
| A4 | No-ent | `lambda_ent=0` | 仅当当前 v5_div_reg 配置含 entropy 项时有意义；据 memory.md，v5_div_reg 用 diversity 而非 entropy → **跳过** | --- |

**A1 复用 v4 已有数据 + 仅一次 eval**，省 11h 训练。A2/A3 必跑，A4 跳过。

### 3.1 消融 eval 简化策略
消融只需 **libero_spatial 标称**（最便宜，区分度足够），不跑 LIBERO-Plus、不跑 4 suites。若 paper 要求覆盖更全，rebuttal 阶段再补。

**消融 GPU 预算: A1=4h, A2=15h, A3=15h, 共 34h on 1 GPU**。

---

## 4. ACIB-S on smolvla_libero_plus [P0, 互补性核心]

### 4.1 战略价值
这是**论文最关键的实验** — 直接支撑 "ACIB 不是 data-aug 替代而是正交互补" 的 framing。没有这个数据，paper 的 main claim 站不住脚。

### 4.2 配置
| 参数 | 值 |
|------|-----|
| `model_id` | `lerobot/smolvla_libero_plus` (替代 smolvla_libero) |
| 其他 | 完全同 v5_div_reg (aggregate KL + diversity reg, β=0.01, α=0.01) |
| seeds | 42 (单 seed for abstract) |

### 4.3 评测对照
| 模型 | Suite 平均 SR (预期/已知) |
|------|---------------------------|
| smolvla_libero (std) | spatial=66.0%, object=67.8%, goal=76.4% |
| smolvla_libero_plus | spatial=81.6%, object=88.8%, goal=87.8% (已有) |
| smolvla_libero + ACIB-S (v5_div_reg) | (来自 §1 eval) |
| **smolvla_libero_plus + ACIB-S** | **目标: 至少 +1-3% on perturbed; 标称不退** |

**互补性 claim 成立条件**: 4.3 表最后一行在 ≥ 2 suites 较 smolvla_libero_plus 进一步提升（即使只有 +1-2%）。

### 4.4 GPU 分工 + 时间
| 阶段 | GPU | 时间 |
|------|-----|------|
| 训练 (11h) | cuda:1 (从 §1.4 seed2 训练完后续接) | 11h |
| eval 4 suites 标称 + (可选) LIBERO-Plus 4 维 | 2× GPU 并发 | 5-8h (标称) + 16h (扰动) |

---

## 5. 时间线 (10 天到 abstract, 13 天到 paper)

### 时间轴（每格 ~12h，以 12h 为最小调度单位）

```
Day  cuda:0                              cuda:1
─────────────────────────────────────────────────────────────────────
0    [eval v5_div_reg seed1 sp+obj]      [eval v5_div_reg seed1 g+l10]
0.5  [train ACIB-H k=0.8]                [train v5_div_reg seed2]
1                                        
2    [.....train continues.....]         [.....train continues.....]
3    [eval ACIB-H 4 suites]              [eval v5_div_reg seed2 4 suites]
3.5  [train ACIB-S on plus]              [train Ablation A2 VIB-only]
4
5    [.....train continues.....]         [.....train continues.....]
6    [eval ACIB-S on plus 4 suites]      [eval A2 spatial]
6.5                                      [train Ablation A3 Cons-only]
7    [eval ACIB-S on plus + LIBERO-Plus] [.....train continues.....]
8                                        [eval A3 spatial]
8.5  [Ablation A1 eval (use v4 ckpt)]    [free → token-importance figs]
9    [results aggregation, paper draft]  [paper draft]
10   ★ CoRL ABSTRACT DEADLINE (5/26)
─────────────────────────────────────────────────────────────────────
11   [ACIB-H k=0.7 train] (optional)     [extra seed for top result]
12   [eval]                              [eval + paper polish]
13   ★ CoRL PAPER DEADLINE (5/29)
```

### 5.1 GPU-hour 预算
| 实验 | GPU-h |
|------|-------|
| §1 v5_div_reg seed1 eval (4 suites) | 5-8 |
| §1 v5_div_reg seed2 retrain + eval | 16-19 |
| §2 ACIB-H k=0.8 train + eval | 16-19 |
| §3.A1 No-div (reuse v4) eval only | 3-4 |
| §3.A2 VIB-only train + eval (1 suite) | 14-16 |
| §3.A3 Consistency-only train + eval (1 suite) | 14-16 |
| §4 ACIB-S on smolvla_libero_plus train + eval | 16-19 |
| Optional: LIBERO-Plus 扰动 eval for top 1-2 ckpts | 8-16 |
| Optional: ACIB-H k=0.7 | 16-19 |
| **核心预算 (P0+P1)** | **84-101 GPU-h** |
| **2 GPU 并发后 wall-clock** | **~5-6 天** |
| **Buffer 到 5/26** | **~4-5 天 (训练 reruns / 补 seeds / 调试)** |

预算充裕。瓶颈不在 GPU 而在**数据正确性**（C001 进程冲突、ckpt 损坏、eval 脚本 bug）。

---

## 6. 启动序列（具体命令草拟，供 worker 立即执行）

**触发条件**: `acib_v5_div_reg` 状态变为 DONE / scorer_std 健康。

```bash
# Step 1: ckpt 健康检查 (ssh_read_only)
ls -la /root/acib/outputs/acib_v5_div_reg/checkpoint_final/
tail -50 ~/runs/action_cond_info_bottleneck/acib_v5_div_reg.log | grep -E "scorer_std|task_loss"

# Step 2: C001 检查 — 两张 GPU 都要排查
ps aux | grep -E "eval_acib|train_acib" | grep -v grep

# Step 3: 双卡 eval v5_div_reg seed1 (并发)
# cuda:0: spatial + object
CUDA_VISIBLE_DEVICES=0 nohup python scripts/eval_acib.py \
  --ckpt /root/acib/outputs/acib_v5_div_reg/checkpoint_final \
  --suites libero_spatial,libero_object \
  --n_episodes 50 \
  --output_dir /root/acib/eval/v5_div_reg_seed1_gpu0 \
  > /root/acib/logs/eval_v5_div_reg_seed1_gpu0.log 2>&1 &

# cuda:1: goal + libero_10
CUDA_VISIBLE_DEVICES=1 nohup python scripts/eval_acib.py \
  --ckpt /root/acib/outputs/acib_v5_div_reg/checkpoint_final \
  --suites libero_goal,libero_10 \
  --n_episodes 50 \
  --output_dir /root/acib/eval/v5_div_reg_seed1_gpu1 \
  > /root/acib/logs/eval_v5_div_reg_seed1_gpu1.log 2>&1 &

# Step 4: eval 结束后无缝衔接（用 register_artifact 登记结果 + 启动下一阶段）
```

每次切换实验**必须**走 `ps aux | grep <output_dir>` 检查 + `kill` 旧进程 + 等待 PID 消失（C001 三犯不可有第四次）。

---

## 7. Fallback & 失败应对

| 失败场景 | 应对 |
|---------|------|
| v5_div_reg seed1 标称回退 > 2% | 用 checkpoint_15000 重 eval；仍 fail → 设计 v6 (降 β / 改 diversity_lambda)，**暂停** seed2/ACIB-H |
| v5_div_reg seed2 训练复现失败 | 单 seed 投 abstract，paper 阶段再补；abstract 文字标 "n=1 seed, multi-seed in progress" |
| ACIB-H 显著差于 ACIB-S | 论文 framing 改为 "soft is necessary in compact regime"，作为 finding 而非缺陷 |
| ACIB-S on plus 无提升 (互补性 fail) | 重大风险 — 改 framing 为 "ACIB 在无 data-aug 场景下与 data-aug 相当；为低数据资源场景的替代方案"；abstract 推迟到 paper deadline |
| GPU 卡死/掉盘 | C001 严格执行；磁盘 `/root/autodl-tmp/` 监控 > 90% 立即清理旧 ckpt |

---

## 8. 优先级总结（TL;DR）

**must-do 顺序**（按价值排序）:
1. **v5_div_reg seed1 标称 eval** (5-8h) — 决定整套方案是否走得通
2. **ACIB-S on smolvla_libero_plus** 训练 + eval (~18h) — 论文核心 claim
3. **v5_div_reg seed2 重训 + eval** (~18h) — 数据可信度
4. **ACIB-H k=0.8** 训练 + eval (~18h) — soft vs hard 对比
5. **消融 A1 (No-div, reuse v4)** (3-4h) — anti-collapse 论证，便宜
6. **消融 A2 VIB-only** (~15h) — α 必要性
7. **消融 A3 Consistency-only** (~15h) — β 必要性

**nice-to-have**（abstract 后到 paper 期间）:
- ACIB-H k=0.7 sweep
- ACIB-S on plus 加 LIBERO-Plus 扰动 eval
- Token importance maps 可视化（不耗 GPU，从已有 ckpt 提取）

**严禁现在做**:
- k 全 sweep (0.6/0.7/0.8/0.9)
- FTM-SmolVLA baseline 复现（abstract 后再说）
- 多 seed (>2) — 时间不允许，paper 阶段补
- 数据效率分析
