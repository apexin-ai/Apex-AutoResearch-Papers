# RSA 方法论审计报告

**日期**: 2026-05-16  
**审计对象**: `rsa_analysis.py` (DINO RSA=0.388) vs `rsa_clip.py` (CLIP RSA)  
**结论**: **两个脚本存在 2 个关键方法学差异，直接影响数值可比性。**

---

## 1. 0.388 的精确来源

- **结果文件**: `/root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json`
- **生成脚本**: `/root/vla-ssd/rsa_analysis.py` (输出路径 `OUT_DIR / "rsa_results{args.feat_suffix}.json"`)
- **文件时间戳**: rsa_results.json Modify 2026-05-16 04:04:16; rsa_analysis.py Modify 2026-05-16 05:33:34
- **计算方式**: DINO per-phase RSA = {early: 0.4909, mid: 0.4132, late: 0.2601}, **取三个 phase 的均值** → mean(0.4909, 0.4132, 0.2601) = **0.3881 ≈ 0.388**

---

## 2. 逐项对比

### 2.1 RDM 构建方式（配对范围）— ⚠️ 关键差异

| 维度 | `rsa_analysis.py` | `rsa_clip.py` |
|------|-------------------|---------------|
| 配对范围 | **跨任务全局配对** — 所有 (task, demo_id) pairs | **仅任务内配对** — 每个 task 内 `itertools.combinations` |
| 样本数 | 10 tasks × 10 demos = 100 demos → ~4950 pairs | 每个 task ~10 demos → ~45 pairs/task |
| 汇总方式 | 单一全局 RDM/ADM → 单一 Spearman | 每 task 独立 RSA → **mean across 10 tasks** |

**`rsa_analysis.py` 关键代码** (line 247-258):
```python
# 全局 common_keys = set of (task, demo_id) tuples across ALL tasks
sorted_keys = sorted(common_keys_base)  # ~100 entries
adm_cache[phase] = build_dissimilarity_matrix(act_common, sorted_keys, phase)
dino_rdm_cache[phase] = build_dissimilarity_matrix(dino_common, sorted_keys, phase)
dino_rsa_cache[phase] = compute_rsa(dino_rdm_cache[phase], adm_cache[phase])
```

**`rsa_clip.py` 关键代码** (line 72-81):
```python
def compute_rsa(feats, actions):
    common = sorted(set(feats.keys()) & set(actions.keys()))  # within ONE task
    pairs = list(itertools.combinations(common, 2))
    rep_dists = [mean_cosine_distance(feats[a], feats[b]) for a, b in pairs]
    act_dists = [mean_action_distance(actions[a], actions[b]) for a, b in pairs]
    rsa, _ = spearmanr(rep_dists, act_dists)
    return float(rsa)
```

**影响**: 
- 跨任务配对混入了"不同任务本身就有不同 action 和不同视觉特征"的信号，这是 task-level confound。
- 任务内配对更纯净地衡量"同一任务内，demo 间的表征相似度是否预测 action 相似度"。
- **两种方式测量的是不同的东西**，数值不可直接比较。

### 2.2 Action 距离度量 — ⚠️ 关键差异

| 维度 | `rsa_analysis.py` | `rsa_clip.py` |
|------|-------------------|---------------|
| 度量 | **Cosine distance** (`scipy.spatial.distance.cosine`) | **Euclidean distance** (`np.linalg.norm(a-b)`) |
| 作用于 | 7-dim action vector | 7-dim action vector |

**`rsa_analysis.py`** — action dissimilarity 通过 `build_dissimilarity_matrix()` 构建，内部调用 `compute_mean_cosine_distance()`:
```python
def compute_mean_cosine_distance(feat_a, feat_b, n_sample=20):
    L = min(len(feat_a), len(feat_b), n_sample)
    a = subsample_to_length(feat_a, L)
    b = subsample_to_length(feat_b, L)
    dists = []
    for i in range(L):
        na = np.linalg.norm(a[i])
        nb = np.linalg.norm(b[i])
        if na < 1e-8 or nb < 1e-8:
            dists.append(1.0)
        else:
            dists.append(cosine_dist(a[i], b[i]))
    return float(np.mean(dists))
```

**`rsa_clip.py`** — action dissimilarity 用专门的 `mean_action_distance()`:
```python
def mean_action_distance(act_a, act_b):
    a = subsample_to_length(act_a, N_SAMPLE)
    b = subsample_to_length(act_b, N_SAMPLE)
    n = min(len(a), len(b))
    return float(np.mean([np.linalg.norm(a[i] - b[i]) for i in range(n)]))
```

**影响**:
- Cosine distance 衡量方向差异，忽略幅度；Euclidean 衡量绝对差异。
- 7-dim action 向量（含位移 + 旋转 + gripper）各维度量纲不同，cosine distance 会被大幅度维度主导方向。
- **对 RSA 排序的影响取决于 action 分布**，但两者产生的 dissimilarity 排序可能显著不同。

### 2.3 表征距离度量 — ✅ 一致

| 维度 | `rsa_analysis.py` | `rsa_clip.py` |
|------|-------------------|---------------|
| 度量 | Cosine distance (`scipy.spatial.distance.cosine`) | Cosine distance (`scipy.spatial.distance.cosine`) |
| 零向量保护 | 有 (norm < 1e-8 → return 1.0) | 无 |

两者都用 cosine distance 计算表征相似度。零向量保护差异在实践中影响不大（CLIP/DINO 特征极少为零向量）。

### 2.4 时序处理 — ⚠️ 中等差异

| 维度 | `rsa_analysis.py` | `rsa_clip.py` |
|------|-------------------|---------------|
| 时序分 bin | 3-phase: early [0, 0.33), mid [0.33, 0.67), late [0.67, 1.0] | **无** — 全轨迹 |
| 子采样 | `min(len_a, len_b, 20)` | 各自 subsample 到 20，再 `min(len_a, len_b)` |
| 汇总 | 3 个 phase RSA 取均值 | 直接一个 RSA |

**影响**: 
- `rsa_analysis.py` 的 DINO RSA 0.388 = mean(0.4909, 0.4132, 0.2601)，late phase 拉低了均值。
- 如果 `rsa_clip.py` 也做 temporal binning，CLIP 的 RSA 在 early/mid phase 可能更高。

### 2.5 采样策略 — ✅ 基本一致

| 维度 | `rsa_analysis.py` | `rsa_clip.py` |
|------|-------------------|---------------|
| N_SAMPLE | 20 (default, 函数参数) | 20 (全局常量) |
| 采样方式 | 均匀子采样 `np.linspace(0, T-1, target_len, dtype=int)` | 相同 |
| 随机种子 | bootstrap 用 rng seed=42 | `np.random.seed(42)` |
| Demo 数量 | 10 per task (default `--n_demos 10`) | 所有可用 demo |

### 2.6 相关性计算 — ✅ 一致

| 维度 | `rsa_analysis.py` | `rsa_clip.py` |
|------|-------------------|---------------|
| 方法 | Spearman rank correlation | Spearman rank correlation |
| 函数 | `scipy.stats.spearmanr` | `scipy.stats.spearmanr` |
| 输入 | 矩阵上三角 (`np.triu_indices_from(rdm, k=1)`) | flat list from `itertools.combinations` |
| Fisher z-transform | 无 | 无 |

两种取上三角的方式数学等价。

### 2.7 Action 向量定义 — ✅ 一致

| 维度 | `rsa_analysis.py` | `rsa_clip.py` |
|------|-------------------|---------------|
| 维度 | 7-dim (从 hdf5 读取 `actions`, shape=(T, 7)) | 7-dim (同) |
| 来源 | `data/demo_X/actions` in `{task}_demo.hdf5` | 同 |
| 时间对齐 | a_t (每帧对应的 action) | 同 |

---

## 3. 差异汇总

| # | 差异项 | 严重程度 | 影响方向 |
|---|--------|----------|----------|
| 1 | **配对范围**: 跨任务全局 vs 任务内 | 🔴 关键 | 跨任务配对引入 task-level confound，可能抬高或压低 RSA |
| 2 | **Action 距离**: cosine vs euclidean | 🔴 关键 | 改变 pair 间 dissimilarity 排序，直接影响 Spearman |
| 3 | **时序分 bin**: 3-phase 均值 vs 全轨迹 | 🟡 中等 | late phase 低值拉低了 DINO 0.388 的均值 |
| 4 | **零向量保护**: 有 vs 无 | 🟢 次要 | 实践中影响极小 |

---

## 4. 结论

**DINO RSA=0.388 与 CLIP RSA=0.5572 不可直接比较。** 两个数字在以下两个根本方面使用了不同方法：

1. **配对范围不同**: `rsa_analysis.py` 计算所有 demo 对的全局 RDM（含跨任务对），`rsa_clip.py` 只在每个 task 内计算再平均。前者混入了跨任务差异信号。
2. **Action 距离不同**: `rsa_analysis.py` 用 cosine distance 衡量 action 差异，`rsa_clip.py` 用 euclidean distance。7-dim 异构 action 向量上两者行为差异大。

**要使两个数值可比，需要统一方法论后重新计算。** 建议以 `rsa_clip.py` 的 within-task + euclidean action distance 为标准（更干净），对 DINO 特征重跑。

---

## 5. 关联脚本清单

| 脚本 | 路径 | 方法学派系 |
|------|------|-----------|
| rsa_analysis.py | `/root/vla-ssd/rsa_analysis.py` | 跨任务全局 + cosine action |
| rsa_analysis_no_inst.py | `/root/vla-ssd/rsa_analysis_no_inst.py` | 同上 (无 instruction 变体) |
| rsa_clip.py | `/root/vla-ssd/scripts/rsa_clip.py` | 任务内 + euclidean action |
| rsa_siglip_only.py | `/root/vla-ssd/scripts/rsa_siglip_only.py` | 任务内 + euclidean action |
| rsa_instruction_control.py | `/root/vla-ssd/scripts/rsa_instruction_control.py` | (待审计) |
| rsa_image_mean.py | `/root/vla-ssd/rsa_image_mean.py` | (待审计) |
| rsa_no_instruction.py | `/root/vla-ssd/rsa_no_instruction.py` | (待审计) |
