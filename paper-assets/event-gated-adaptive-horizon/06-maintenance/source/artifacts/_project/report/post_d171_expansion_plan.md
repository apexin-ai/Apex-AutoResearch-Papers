# Post-D171 Environment Expansion Plan

> 目标：扩展 CIVO 验证的环境覆盖，解决 Reviewer "scope 太窄" (Significance 2.5/4) 问题
> 状态：Draft — 待 Director 审批后执行
> 日期：2026-05-28

## 1. 当前覆盖

| 环境 | DoF | Configs Tested | CIVO? | Seeds |
|------|-----|---------------|-------|-------|
| Walker Walk | 6 | baseline, 008d, 008a, 008f, frozen, SGS×3, wide dual-critic | ✅ 2/3 onset | 36+ |
| Cheetah Run | 6 | baseline, 008d, 008a, 008f, frozen | ✅ 3/4 onset | 20+ |
| Hopper Hop | 4 | baseline, trained, frozen, no_dt_emb | ❌ severe learning delay, NOT CIVO | 8 |

**问题**：仅 2 个 CIVO-positive 环境，均为 6-DoF 单脊柱构型。Reviewer 合理质疑泛化性。

## 2. 候选环境（优先级排序）

### Tier 1: 高优先级

**A. Humanoid Walk** (`dmc_humanoid_walk`)
- DoF: 21 actuators, ~67-dim obs
- 理由：最高 DoF 的 DMC locomotion 环境。如果 CIVO 出现 → 强烈支持 "multi-joint locomotion" claim
- 风险：105K 步可能不够 baseline 收敛，需 200K 步
- 备选：若 walk 不收敛，降级到 `humanoid_stand`（更简单，收敛快）

**B. Quadruped Walk** (`dmc_quadruped_walk`)
- DoF: 12 actuators, ~78-dim obs
- 理由：四足形态，与 Walker/Cheetah（双足/单脊柱）形态完全不同
- 风险：中等，DreamerV3 在 quadruped 上表现较好

### Tier 2: 负面对照

**C. Finger Turn Hard** (`dmc_finger_turn_hard`)
- DoF: 2 actuators, ~12-dim obs
- 理由：非 locomotion 的 manipulation 任务。预期 CIVO **不出现**
- 如果 CIVO 不出现 → 支持 "locomotion 特异性" claim
- 如果 CIVO 出现 → 挑战 locomotion 假设，但科学上有价值

### 已排除

- **Cartpole Swingup** (1 DoF)：之前计划过 (plan_035-037) 但取消。太简单，作为负面对照信息量不够
- **Swimmer** (5-13 DoF)：无重力/无接触动力学，与 CIVO 假设关联弱
- **Ant**：非标准 DMC 环境，需额外代码适配

## 3. 实验矩阵

### Phase 1: CIVO 检测（必做）

每个环境 4 runs：

| Config | 描述 | Seeds | 步数 |
|--------|------|-------|------|
| Baseline | 无 gate (dt=1) | 0, 1 | 200K |
| 008d (CIVO trigger) | trained dt_emb + gate + subsample ON + dt=2 + H=8 | 0, 1 | 200K |

**判定标准**：
- Baseline 必须在 200K 内 converge（eval_return 稳定上升且达到合理水平）
- 008d 是否出现 NVE > 2.0×（同时检查 value_mean 趋势 + civo/alert）
- 如果 baseline 不 converge → 该环境不适合 105K/200K 时间窗口，需要 Director 决策

### Phase 2: 因果控制（仅在 Phase 1 检测到 CIVO 时执行）

| Config | 描述 | Seeds | 步数 |
|--------|------|-------|------|
| 008f (no dt_emb) | gate_dt_embed_dim=0 + subsample ON + dt=2 + H=8 | 0 | 200K |
| Frozen dt_emb | dt_emb_freeze=True + subsample ON + dt=2 + H=8 | 0 | 200K |

### Phase 3: 干预效果（可选，最强证据级别）

| Config | 描述 | Seeds | 步数 |
|--------|------|-------|------|
| 008a (value suppression) | trained dt_emb + subsample OFF + dt=2 + H=15 | 0 | 200K |
| Wide dual-critic | min+capacity dual critic | 0 | 200K |

## 4. GPU 时间估算

### 从 registry 推算（RTX PRO 6000 Blackwell, 105K 步）

| 环境 | 样本数 | GPU-h 中位数 | 范围 |
|------|--------|-------------|------|
| Walker Walk | 8 | 3.2 | 2.99-4.46 |
| Cheetah Run | 7 | 2.85 | 2.25-3.24 |
| Hopper Hop | 3 | 3.14 | 3.02-3.42 |

**平均 ~3.1 GPU-h / 105K run**

### 新环境预估（200K 步 ≈ 2× 现有）

DreamerV3 dmc_proprio 训练时间主要由 RSSM+MLP 训练循环决定（train_ratio=512），与 obs dim 关系较弱（仅影响 encoder/decoder 第一/最后一层）。MuJoCo sim 复杂度是次要因素。

| 环境 | 预估 GPU-h (200K) | 理由 |
|------|-------------------|------|
| Humanoid Walk | ~6.5 | 2× 平均值，sim 稍慢 |
| Quadruped Walk | ~6.5 | 2× 平均值，sim 稍慢 |
| Finger Turn Hard | ~6.0 | 2× 平均值，sim 很快 |

### 总量估算

| 阶段 | 环境数 | Runs | GPU-h |
|------|--------|------|-------|
| Phase 1 | 3 | 12 | ~76 |
| Phase 2 | 0-3 | 0-6 | 0-39 |
| Phase 3 | 0-3 | 0-6 | 0-39 |
| **Total** | **3** | **12-24** | **76-154** |

### Wall Time（2× RTX PRO 6000 并行）

- Phase 1 only: 12 runs ÷ 2 GPU = 6 batches × ~6.5h = **~39h (1.6 天)**
- Phase 1+2: 18 runs ÷ 2 = 9 batches × ~6.5h = **~58h (2.4 天)**
- Full (Phase 1+2+3): 24 runs ÷ 2 = 12 batches × ~6.5h = **~78h (3.3 天)**

## 5. 命令模板

### 通用 wrapper（westd-51268）

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID={EGL_ID} && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio {EXPERIMENT_ARGS}"
```

### Humanoid Walk

```bash
# Phase 1: Baseline (seed 0)
--task dmc_humanoid_walk --logdir logdir/exp_humanoid_baseline_s0 --steps 200000 --seed 0 --compile False --device cuda:0

# Phase 1: Baseline (seed 1)
--task dmc_humanoid_walk --logdir logdir/exp_humanoid_baseline_s1 --steps 200000 --seed 1 --compile False --device cuda:0

# Phase 1: 008d CIVO trigger (seed 0)
--task dmc_humanoid_walk --logdir logdir/exp_humanoid_008d_s0 --steps 200000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8

# Phase 1: 008d CIVO trigger (seed 1)
--task dmc_humanoid_walk --logdir logdir/exp_humanoid_008d_s1 --steps 200000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8

# Phase 2: 008f no dt_emb (seed 0)
--task dmc_humanoid_walk --logdir logdir/exp_humanoid_008f_s0 --steps 200000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0

# Phase 2: Frozen dt_emb (seed 0)
--task dmc_humanoid_walk --logdir logdir/exp_humanoid_frozen_s0 --steps 200000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True
```

### Quadruped Walk

```bash
# Phase 1: Baseline (seed 0)
--task dmc_quadruped_walk --logdir logdir/exp_quadruped_baseline_s0 --steps 200000 --seed 0 --compile False --device cuda:0

# Phase 1: Baseline (seed 1)
--task dmc_quadruped_walk --logdir logdir/exp_quadruped_baseline_s1 --steps 200000 --seed 1 --compile False --device cuda:0

# Phase 1: 008d CIVO trigger (seed 0)
--task dmc_quadruped_walk --logdir logdir/exp_quadruped_008d_s0 --steps 200000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8

# Phase 1: 008d CIVO trigger (seed 1)
--task dmc_quadruped_walk --logdir logdir/exp_quadruped_008d_s1 --steps 200000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8

# Phase 2: 008f no dt_emb (seed 0)
--task dmc_quadruped_walk --logdir logdir/exp_quadruped_008f_s0 --steps 200000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0

# Phase 2: Frozen dt_emb (seed 0)
--task dmc_quadruped_walk --logdir logdir/exp_quadruped_frozen_s0 --steps 200000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True
```

### Finger Turn Hard

```bash
# Phase 1: Baseline (seed 0)
--task dmc_finger_turn_hard --logdir logdir/exp_finger_baseline_s0 --steps 200000 --seed 0 --compile False --device cuda:0

# Phase 1: Baseline (seed 1)
--task dmc_finger_turn_hard --logdir logdir/exp_finger_baseline_s1 --steps 200000 --seed 1 --compile False --device cuda:0

# Phase 1: 008d CIVO trigger (seed 0)
--task dmc_finger_turn_hard --logdir logdir/exp_finger_008d_s0 --steps 200000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8

# Phase 1: 008d CIVO trigger (seed 1)
--task dmc_finger_turn_hard --logdir logdir/exp_finger_008d_s1 --steps 200000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8

# Phase 2: 008f no dt_emb (seed 0)
--task dmc_finger_turn_hard --logdir logdir/exp_finger_008f_s0 --steps 200000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0

# Phase 2: Frozen dt_emb (seed 0)
--task dmc_finger_turn_hard --logdir logdir/exp_finger_frozen_s0 --steps 200000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True
```

## 6. 执行策略

### 并行调度（2 GPU）

**Batch 1**: humanoid_baseline_s0 (cuda:0) + humanoid_008d_s0 (cuda:1)
**Batch 2**: humanoid_baseline_s1 (cuda:0) + humanoid_008d_s1 (cuda:1)
**Batch 3**: quadruped_baseline_s0 (cuda:0) + quadruped_008d_s0 (cuda:1)
**Batch 4**: quadruped_baseline_s1 (cuda:0) + quadruped_008d_s1 (cuda:1)
**Batch 5**: finger_baseline_s0 (cuda:0) + finger_008d_s0 (cuda:1)
**Batch 6**: finger_baseline_s1 (cuda:0) + finger_008d_s1 (cuda:1)

Phase 2 batches conditional on Phase 1 results per environment.

### Gating 决策点

每个环境 Phase 1 完成后立即分析：
1. Baseline 是否收敛？（eval_return 趋势稳定）
   - 不收敛 → 不适合当前步数设定，汇报 Director
2. 008d 是否 NVE > 2.0×？
   - 是 → 启动该环境的 Phase 2
   - 否 → 记录为 negative（类似 Hopper），分析原因

### 风险与缓解

| 风险 | 概率 | 缓解 |
|------|------|------|
| Humanoid baseline 在 200K 不收敛 | 中 | 降级到 humanoid_stand，或延长到 400K |
| 新环境 MuJoCo EGL segfault | 低 | 参考 008d s6/s7 失败经验，尝试 osmesa backend |
| 008d 在所有新环境均无 CIVO | 中 | 科学上有价值（确定边界条件），论文可用"locomotion DoF threshold"叙事 |
| westd-51268 EGL driver 不兼容新环境 | 低 | 先跑 dry-run 1000 步验证环境可用 |

## 7. 论文影响预估

### 最佳情况：Humanoid + Quadruped 都出现 CIVO
- CIVO 从 2 → 4 个环境，涵盖 6-21 DoF
- "multi-joint locomotion" claim 极大加强
- Significance 有望从 2.5 → 3.0+
- Finger 负面对照确认 locomotion 特异性

### 中等情况：仅 1 个新环境出现 CIVO
- 3 个 CIVO-positive 环境（比当前 2 个改善）
- 不出 CIVO 的环境与 Hopper 一起作为边界分析

### 最差情况：新环境均无 CIVO
- CIVO 保持 2 环境
- 但增加了系统性的边界分析（Hopper + Humanoid + Quadruped + Finger 均无）
- 重新定义 scope："6-DoF single-spine locomotion specific"
- 科学贡献仍然成立（精确界定了失败条件）
