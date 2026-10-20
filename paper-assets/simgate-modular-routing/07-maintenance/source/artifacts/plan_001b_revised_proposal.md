# Plan-001b Final Proposal (D013)

**Date**: 2026-05-14
**Status**: 待 Director 审批
**Prerequisite**: 预筛 25/25 tasks 完成 ✅ | pipeline-format-fix 完成 ✅

---

## 1. 目的

收集全面 episode-level 数据用于：
- **plan-012**: Death decomposition 分析 (论文 Table 1 + Figure 1)
- **plan-005**: Routing pattern heatmap / diagnostic probe
- **plan-002**: Router SFT 训练（即使 ≈ always-det 也做，负面结果有价值）
- **plan-011**: Rule-based vs learned router 对比

## 2. Blocking Gates 状态

| Gate | 状态 | 说明 |
|------|------|------|
| pipeline-format-fix worker 完成 | ✅ | `label_episode()` → `classify_episode_labels()` 三标签，端到端验证通过 |
| dry-run 通过 | ✅ | prescreening episodes.jsonl → death_aware_labeling.py → 150 sft_triples |
| episodes.jsonl 格式确认 | ✅ | `{episode_idx, variation_idx, always_internal, always_deterministic}` |
| classify_episode() 三标签 | ✅ | `det-preferred` / `internal-preferred` / `no-preference` + `signal_source` |

## 3. 预筛结果总览（25/25 完成）

### Signal 分布

| Signal Type | Prescreening (25 tasks, 5eps each) | MVP (5 tasks, 20eps each) | Total Tasks |
|------------|-----------------------------------:|---------------------------:|------------:|
| death-dominated | 19 | 4 | **23** |
| genuine-det | 5 | 0 | **5** |
| internal-preferred | 1 | 0 | **1** |
| no-effect | 0 | 1 | **1** |

### Genuine-det Tasks（最高论文价值）

| Task | Δ(D-I) | I_d% | D_d% | Δ_nd | n_eps |
|------|-------:|-----:|-----:|-----:|------:|
| lifespan-longest-lived-then-shortest | +70.0 | 60% | 0% | +10.0 | 5 |
| find-animal | +66.6 | 60% | 0% | +4.2 | 5 |
| identify-life-stages-1 | +65.0 | 60% | 0% | +5.0 | 5 |
| lifespan-longest-lived | +50.0 | 60% | 20% | +12.5 | 5 |
| measure-melting-point-unknown | +26.6 | 60% | 40% | +9.83 | 5 |

这 5 个 task 在排除 death 后 det 仍显著优于 internal（Δ_nd > +3），证明 router 价值不限于 death detection。

### Internal-preferred Task

| Task | Δ(D-I) | I_d% | D_d% | Δ_nd |
|------|-------:|-----:|-----:|-----:|
| find-non-living-thing | -6.8 | 0% | 0% | -6.8 |

唯一一个 internal > det 的 task，0% death rate 双模式，label 多样性来源。

### 之前待定 3 Tasks 结果

| Task | Δ(D-I) | I_d% | D_d% | Δ_nd | Signal |
|------|-------:|-----:|-----:|-----:|--------|
| test-conductivity-of-unknown-substances | +40.0 | 60% | 20% | 0.0 | death-dominated |
| measure-melting-point-known-substance | +60.0 | 60% | 0% | -1.8 | death-dominated |
| use-thermometer | +40.0 | 60% | 20% | -0.75 | death-dominated |

三个均为 death-dominated，不影响 task selection。方案 A 确认为最终方案。

---

## 4. 三标签方案

| Label | 定义 | 预期占比 |
|-------|------|---------|
| det-preferred | int died + det alive，或 both alive det > int | ~38% |
| internal-preferred | det died + int alive，或 both alive int > det | ~1-2% |
| no-preference | both died，或 both alive tie | ~60% |

**Class imbalance 应对**: SFT 训练用 class-weighted loss（internal 样本权重 ×5）+ find-non-living-thing 扩大到 40 eps。

---

## 5. 最终 Task Selection（方案 A 确认）

**15 tasks = 5 genuine-det + 1 internal-pref + 5 death-dom (新采) + 4 MVP (复用)**

| # | Task | Source | Signal | Existing eps | New eps needed | Target |
|---|------|--------|--------|-------------:|---------------:|-------:|
| 1 | find-animal | prescreen | genuine-det | 5 | 15 | 20 |
| 2 | identify-life-stages-1 | prescreen | genuine-det | 5 | 15 | 20 |
| 3 | lifespan-longest-lived-then-shortest | prescreen | genuine-det | 5 | 15 | 20 |
| 4 | lifespan-longest-lived | prescreen | genuine-det | 5 | 15 | 20 |
| 5 | measure-melting-point-unknown | prescreen | genuine-det | 5 | 15 | 20 |
| 6 | **find-non-living-thing** | prescreen | **int-pref** | 5 | **35** | **40** |
| 7 | freeze | prescreen | death-dom | 5 | 15 | 20 |
| 8 | chemistry-mix | prescreen | death-dom | 5 | 15 | 20 |
| 9 | grow-fruit | prescreen | death-dom | 5 | 15 | 20 |
| 10 | inclined-plane-determine-angle | prescreen | death-dom | 5 | 15 | 20 |
| 11 | identify-life-stages-2 | prescreen | death-dom | 5 | 15 | 20 |
| 12 | boil | MVP | death-dom | **20** | **0** | 20 |
| 13 | melt | MVP | death-dom | **20** | **0** | 20 |
| 14 | change-the-state-of-matter-of | MVP | death-dom | **20** | **0** | 20 |
| 15 | chemistry-mix-paint-secondary-color | MVP | death-dom | **20** | **0** | 20 |

**排除**: grow-plant (no-effect), 其余 14 个 death-dominated prescreening tasks（已有足够 death-dom 样本）

| 合计 | 值 |
|------|---|
| 总 tasks | 15 |
| 现有 episodes | 135 (5×11 prescreen + 4×20 MVP) |
| 需新增 episodes | 185 (15×11 prescreen + 35 find-non-living extra) |
| 最终总 episodes | 320 |
| Signal 覆盖 | death-dom:9, genuine-det:5, int-pref:1 |

### find-non-living-thing 40 eps 方案可行性

- 0% death rate（双模式），所有 episode 都产生有效 training signal
- max_variations=300，40 episodes 仅消耗 13% variation 空间，无重复风险
- 预估 40 eps 产出 ~40 个 internal-preferred labels（占总训练集 ~12%）
- 配合 class-weighted loss，足以让 router 学到 internal-preferred 模式

---

## 6. GPU 时间估算

### 基准

从预筛日志推算：5 episodes × 2 modes ≈ 20 min → **4 min/episode-pair**

### 时间表

| 组别 | Tasks | New eps | Time (单卡) |
|------|------:|--------:|------------:|
| genuine-det (5 tasks × 15 eps) | 5 | 75 | 300 min |
| int-pref (find-non-living, 35 new eps) | 1 | 35 | 140 min |
| death-dom (5 tasks × 15 eps) | 5 | 75 | 300 min |
| MVP (reuse, 0 new) | 4 | 0 | 0 min |
| **合计** | **15** | **185** | **740 min ≈ 12.3h** |

### GPU 分配策略（双卡并行）

| GPU | 任务分配 | 预计时间 |
|-----|---------|---------|
| cuda:0 | genuine-det 5 tasks (75 eps) + death-dom 2 tasks (30 eps) = 105 eps | ~7h |
| cuda:1 | find-non-living-thing 35 eps + death-dom 3 tasks (45 eps) = 80 eps | ~5.3h |

**总挂钟时间**: ~7h（含启动/模型加载开销 ~30min）

---

## 7. 数据格式与复用

### 复用验证 ✅

Prescreening `episodes.jsonl` 与 `episode_level_collection.py` 输出格式一致（pipeline-format-fix 已确认）：
- 均存储 `always_internal` + `always_deterministic` paired episodes
- 含 step-level: `step`, `action`, `modality`, `score_before`, `score_after`
- `death_aware_labeling.py` 的 `classify_episode()` 可直接消费
- 三标签输出: `det-preferred` / `internal-preferred` / `no-preference` + `signal_source`

### 复用路径

```
--reuse_dirs results/prescreening,results/mvp,results/research
```

`scan_reuse_episodes()` 自动扫描已完成 episodes，`effective_start` 从已有数量续跑。

---

## 8. 提交命令

### GPU0
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/simgate-modular-routing

nohup python src/episode_level_collection.py \
  --task_types "find-animal,identify-life-stages-1,lifespan-longest-lived-then-shortest-lived,lifespan-longest-lived,measure-melting-point-unknown-substance,freeze,chemistry-mix" \
  --episodes 20 \
  --gpu_id 0 \
  --output_dir results/plan_c/ \
  --reuse_dirs results/prescreening,results/mvp,results/research \
  --seed 42 \
  > results/plan_c/gpu0_run.log 2>&1 &
```

### GPU1
```bash
nohup python src/episode_level_collection.py \
  --task_types "find-non-living-thing,grow-fruit,inclined-plane-determine-angle,identify-life-stages-2" \
  --episodes 20 \
  --gpu_id 1 \
  --output_dir results/plan_c/ \
  --reuse_dirs results/prescreening,results/mvp,results/research \
  --seed 42 \
  > results/plan_c/gpu1_run.log 2>&1 &
```

**find-non-living-thing 追加到 40 eps**:
```bash
nohup python src/episode_level_collection.py \
  --task_types "find-non-living-thing" \
  --episodes 40 \
  --start_episode 20 \
  --gpu_id 1 \
  --output_dir results/plan_c/ \
  --seed 43 \
  > results/plan_c/gpu1_fnlt_extra.log 2>&1 &
```

---

## 9. 预期产出

| 下游 Plan | 需要的数据 | 本次提供 |
|-----------|-----------|---------|
| plan-012 (death decomposition) | 15+ tasks × 20 eps 的 death rate + score 数据 | ✅ 15 tasks, 320 episodes |
| plan-005 (routing heatmap) | 多 task cross-domain episode 数据 | ✅ 5 domains covered |
| plan-002 (router SFT) | labeled step triples (context, int_action, det_action, label) | ✅ ~3200 steps |
| plan-011 (rule-based baseline) | task-level death keywords + episode outcomes | ✅ same data |

### 预期 label 分布（基于预筛 extrapolation）

| Label | 估算数量 | 占比 |
|-------|---------|-----|
| det-preferred | ~120 | ~38% |
| internal-preferred | ~15 (含 find-non-living ~40) | ~5% (upsampled → ~15%) |
| no-preference (discard/tie) | ~185 | ~58% |

---

## 10. 风险与缓解

| 风险 | 概率 | 影响 | 缓解 |
|------|------|------|------|
| genuine-det 在 20 eps 下不再显著 | 30% | 高 | 5 个 task 中只需 2-3 个存活即可 |
| internal labels 仍 < 5% | 60% | 中 | class-weighted loss + find-non-living 40 eps |
| vLLM OOM on 双卡并行 | 10% | 低 | 已验证 prescreening 双卡稳定运行 |
| 某些 task reuse 格式不兼容 | 5% | 低 | pipeline-format-fix 已验证兼容 |

---

## 11. Timeline

```
T+0h          预筛全部完成 ✅，pipeline-format-fix ✅，方案确认
T+0.5h        启动 plan_c 双卡并行
T+7h          数据采集完成
T+8h          运行 death_aware_labeling.py → labeled data
T+9h          统计 label 分布，确认是否满足 plan-002 需求
T+9h          → plan-012 death decomposition 分析
T+10h         → plan-002 router SFT 启动
```

**距 DDL (2026-05-25) 还剩 11 天，plan-001b 占 ~0.5 天。**
