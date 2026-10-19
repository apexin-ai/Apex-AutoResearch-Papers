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

**决策**: 第一轮**只跑标称 4 suites** (~5-8h) — 拿到核心数 vs std baseline。理由：abstract 阶段只需 "ACIB-S 不损害标称 + scorer 分化有效" 这一条 claim 的证据。

### 1.3 GPU 分工
| GPU | 任务 | ETA |
|-----|------|-----|
| cuda:0 | seed1 eval: spatial + object (1000 ep) | 2.5-4h |
| cuda:1 | seed1 eval: goal + libero_10 (1000 ep) | 2.5-4h |

### 1.4 同时启动 seed2 重训
seed2 在 eval 完成后从 cuda:1 启动训练（~11h）。**前置**: 修复 acib_policy.py stop_grad 硬编码 bug (D023)，确保 `weights.detach()` 受 `--stop_grad_task` flag 控制。

**C001 合规**: 启动前 `ps aux | grep acib_v5_div_reg_seed2` 确认无残留进程。

### 1.5 Pass 判定（决定后续是否继续）
- 标称回退 < 2% (4 suites 全部满足)
- scorer_std 在 final ckpt 推理时仍 > 0.05（验证训练态保留到推理）

**Fail-safe**: 若 seed1 eval 严重回退，立即用 `checkpoint_15000` 重测一次；仍 fail 则停掉 seed2，进入 v6 设计而非继续刷参数。

---

## 2. ACIB-H 实验 [P0]

### 2.1 训练配置
基于 v5_div_reg 唯一改动 `mode=hard, top_k_ratio=0.8`，其余全部继承。Straight-through estimator 已实现。

| 参数 | 值 | 备注 |
|------|-----|------|
| mode | hard | straight-through estimator |
| top_k_ratio | 0.8 | 保留 ~51/64 tokens |
| hidden_dim | 64 | 同 v5_div_reg |
| α | 0.01 | 同 v5_div_reg |
| β | 0.01, warmup 1000 步 | 同 v5_div_reg |
| diversity_lambda | 0.1 | 同 v5_div_reg |
| stop_grad_task | False | 同 v5_div_reg |

### 2.2 训练 + eval 流程
| 阶段 | GPU | 时间 |
|------|-----|------|
| ACIB-H 训练 | cuda:0 (seed1 eval 完成后) | ~11h |
| ACIB-H eval (4 suites 标称) | 2× GPU 并行 | ~5-8h |

单 seed 即可（abstract 阶段）。

### 2.3 与 ACIB-S 对比
对比指标（论文 Table）:
- Per-suite SR (标称)
- Δ vs std baseline
- 推理时 scorer logit 分布 (soft) vs gate ratio (hard)
- 推理时 wall-clock

**假设**: 64-token regime 下 soft 优于 hard（信息已压缩到极限，hard discretization 损失大）。若结果反向，论文 framing 调整为 "hard 在 token 维度更稀疏时退化更明显"。

---

## 3. 消融实验优先级 [P1]

所有消融基于 v5_div_reg 配置，单 seed=42。

| 顺序 | 实验 | 配置改动 | 目的 | GPU-h |
|------|------|----------|------|-------|
| **A1** | **No-div** | `diversity_lambda=0` | 复现 v4_agg_kl collapse，证明 diversity reg 关键 | **0h 训练** — 直接引用 v4 已有 scorer_std=0.009 数据 + eval v4 ckpt (3-4h) |
| **A2** | **VIB-only** | `α=0` (去 consistency) | 证明 consistency loss 必要 | 11h train + 3-4h eval (单 suite) |
| **A3** | **Consistency-only** | `β=0` (去 IB) | 证明 IB constraint 必要 | 11h train + 3-4h eval (单 suite) |
| ~~A4~~ | ~~No-ent~~ | ~~`lambda_ent=0`~~ | v5_div_reg 用 diversity 非 entropy → **跳过** | --- |

**A1 复用 v4 数据，省 11h。** 消融 eval 只跑 **libero_spatial** (最便宜，区分度够)，paper 阶段再扩全 suite。

**消融 GPU 预算: A1=4h, A2=15h, A3=15h, 共 ~34h**。

---

## 4. ACIB-S on smolvla_libero_plus [P0, 互补性核心]

### 4.1 战略价值
**论文最关键实验** — 直接支撑 "ACIB 与 data-aug 正交互补" 的 framing。审稿人必问。

### 4.2 配置
| 参数 | 值 |
|------|-----|
| model_id | `lerobot/smolvla_libero_plus` (替代 smolvla_libero) |
| 其他 | 完全同 v5_div_reg |
| seed | 42 (abstract 阶段单 seed) |

### 4.3 评测 2×2 对照矩阵
| Model | ACIB | spatial | object | goal |
|-------|------|---------|--------|------|
| std | ✗ | 66.0% | 67.8% | 76.4% |
| std | ACIB-S | (§1 eval) | (§1 eval) | (§1 eval) |
| plus | ✗ | 81.6% | 88.8% | 87.8% |
| plus | ACIB-S | **本实验** | **本实验** | **本实验** |

**互补性 claim 成立条件**: 最后一行在 ≥2 suites 较 plus-only 提升（即使 +1-2%）。

### 4.4 GPU: ~11h train + ~6h eval = 17h

---

## 5. 时间线

### Gantt (每格 ~12h)

```
Day  cuda:0                              cuda:1
─────────────────────────────────────────────────────────────────────
0    [eval v5_div_reg seed1 sp+obj]      [eval v5_div_reg seed1 g+l10]
0.5  [train ACIB-H k=0.8]               [train v5_div_reg seed2]
1    [.....train.....]                   [.....train.....]
2    [eval ACIB-H 4 suites]             [eval v5_div_reg seed2 4 suites]
2.5  [train ACIB-S on plus]             [train Ablation A2 VIB-only]
3    [.....train.....]                   [.....train.....]
4    [eval ACIB-S on plus]              [eval A2 spatial]
4.5  [Ablation A1 eval (v4 ckpt)]       [train Ablation A3 Cons-only]
5                                        [.....train.....]
5.5  [token-importance figures]          [eval A3 spatial]
6    [结果汇总 + paper tables]           [paper tables]
7-9  [论文写作 + 补跑 / 补 seed]         [论文写作]
10   ★ CoRL ABSTRACT DEADLINE (5/26)
─────────────────────────────────────────────────────────────────────
11   [ACIB-H k=0.7 optional]            [extra seed for top result]
12   [eval + paper polish]              [eval + paper polish]
13   ★ CoRL PAPER DEADLINE (5/29)
```

### GPU-hour 预算

| 实验 | GPU-h | 优先级 |
|------|-------|--------|
| v5_div_reg seed1 eval (4 suites) | 5-8 | P0 |
| v5_div_reg seed2 retrain + eval | 16-19 | P0 |
| ACIB-H k=0.8 train + eval | 16-19 | P0 |
| ACIB-S on smolvla_libero_plus train + eval | 16-19 | P0 |
| Ablation A1 No-div (reuse v4) eval only | 3-4 | P1 |
| Ablation A2 VIB-only train + eval (1 suite) | 14-16 | P1 |
| Ablation A3 Consistency-only train + eval (1 suite) | 14-16 | P1 |
| Token importance 可视化 | 1-2 | P2 |
| **核心合计 (P0+P1)** | **85-103** | |
| **2 GPU 并行 wall-clock** | **~5-6 天** | |
| **Buffer 到 5/26** | **~4-5 天** | |

---

## 6. Abstract Deadline (5/26) 最低要求

| # | 实验 | 支撑 claim | 当前状态 |
|---|------|-----------|---------|
| 1 | v5_div_reg seed1+2 标称 eval | ACIB-S 有效 + 不退步 | seed1 训练中 |
| 2 | ACIB-S on smolvla_libero_plus eval | 与 data-aug 互补 | 待启动 |
| 3 | ACIB-H k=0.8 eval | Soft vs hard 对比 | 待启动 |
| 4 | Ablation A1 No-div (v4 ckpt eval) | diversity reg 必要性 | v4 数据已有 |
| 5 | Token importance 可视化 | 可解释性 | 待生成 |

**如果时间紧张可砍**: A2/A3 消融 → 降级到 paper 阶段。

---

## 7. Fallback & 失败应对

| 失败场景 | 应对 |
|---------|------|
| v5_div_reg seed1 标称回退 > 2% | 用 checkpoint_15000 重 eval；仍 fail → v6 设计，暂停所有后续 |
| seed2 复现失败 | 单 seed 投 abstract，paper 补 |
| ACIB-H 显著差于 ACIB-S | 论文 framing: "soft is necessary in compact regime"，作为 finding |
| ACIB-S on plus 无提升 | 重大风险 — 改 framing 为 "ACIB 在无 data-aug 场景下有效，低数据资源替代方案"；abstract 措辞弱化互补性 |
| GPU 掉盘 / 进程冲突 | C001 严格执行；`/root/autodl-tmp/` 磁盘 >90% 立即清旧 ckpt |

---

## 8. 优先级总结 (TL;DR)

**Must-do (按执行顺序)**:
1. **v5_div_reg seed1 标称 eval** (5-8h) — gate decision
2. **ACIB-H k=0.8** train + eval (~18h) — soft vs hard
3. **v5_div_reg seed2** retrain + eval (~18h) — 可信度
4. **ACIB-S on smolvla_libero_plus** train + eval (~18h) — 核心 claim
5. **Ablation A1 No-div** eval only (3-4h) — 便宜且关键
6. **Ablation A2 VIB-only** (~15h)
7. **Ablation A3 Consistency-only** (~15h)

**Nice-to-have (abstract 后)**:
- ACIB-H k=0.7 sweep
- Token importance maps (不耗 GPU，从 ckpt 提取)
- 额外 seeds (>2)

**严禁现在做**:
- k 全 sweep (0.6/0.7/0.8/0.9)
- FTM-SmolVLA baseline 复现
- 多 seed (>2)
- 数据效率分析
