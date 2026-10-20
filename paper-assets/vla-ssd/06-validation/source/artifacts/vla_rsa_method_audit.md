# VLA RSA 方法审计报告

## 1. 脚本方法分类表

| 脚本 | 配对方式 | Action Distance | 时序处理 | 汇总方式 | Token | 方法 |
|------|----------|----------------|----------|----------|-------|------|
| `rsa_analysis.py` | cross-task global (~4950 pairs) | cosine | 3-phase temporal binning 均值 | global single | last_preaction | **A** |
| `rsa_image_mean.py` | cross-task global (~4950 pairs) | cosine | 3-phase temporal binning 均值 | global single | image_mean | **A** |
| `rsa_no_instruction.py` | cross-task global (~4950 pairs) | cosine | 3-phase temporal binning 均值 | global single | last_preaction | **A** |
| `rsa_instruction_control.py` | cross-task global (~4950 pairs) | cosine | 3-phase temporal binning 均值 | global single | last_preaction | **A** |
| `rsa_siglip_only.py` | **within-task** (~45 pairs/task) | **euclidean** | **全轨迹** (N_SAMPLE=20) | **per-task mean** | last_preaction | **B** |

### 方法差异详解

**方法 A** (rsa_analysis.py 家族):
- 10 tasks × 10 demos = 100 trajectories → C(100,2) = 4950 pairs
- 跨任务配对：不同任务的 demo 也会配对
- Action dissimilarity: `scipy.spatial.distance.cosine` (frame-wise cosine distance 均值)
- 时序: 3 个 temporal bin (early/mid/late), 每个 bin 独立计算 RSA, 最终取 3-phase 均值
- 单一全局 dissimilarity matrix

**方法 B** (rsa_siglip_only.py):
- 每个 task 内部 C(n,2) ≈ 45 pairs, 10 个 task 分别计算再平均
- 仅任务内配对：只比较同一任务的不同 demo
- Action dissimilarity: `np.linalg.norm(a - b)` (L2 euclidean distance)
- 时序: 全轨迹 subsample 到 20 帧, 无 temporal binning
- Per-task RSA → bootstrap mean

## 2. RSA 数字方法归属表

### 方法 A 数字

| 数字 | 来源脚本 | 实验 |
|------|----------|------|
| VLA trained with-inst peak RSA = **0.4876** | rsa_analysis.py → `rsa_results.json` | lg_rsa_analysis |
| VLA untrained with-inst peak RSA = **0.4846** | rsa_analysis.py → `rsa_results.json` | lg_rsa_analysis |
| VLA image_mean trained = **0.5014** | rsa_image_mean.py → `rsa_image_mean.json` | p0_image_mean_rsa_verify |
| VLA image_mean untrained = **0.4847** | rsa_image_mean.py → `rsa_image_mean.json` | p0_image_mean_rsa_verify |
| VLA trained no-inst peak RSA = **0.489** | rsa_no_instruction.py → `rsa_no_instruction.json` | d027_trained_no_inst_rsa |
| VLA untrained no-inst peak RSA = **0.4802** | rsa_no_instruction.py → `rsa_no_instruction.json` | d021_instruction_ablation |
| Instruction control: normal=**0.4888**, empty=**0.4723**, random=**0.4835**, shuffled=**0.4832** | rsa_instruction_control.py | plan_008 |
| DINO = **0.388** | rsa_analysis.py (作为 anchor) | lg_rsa_analysis |

### 方法 B 数字

| 数字 | 来源脚本 | 实验 |
|------|----------|------|
| SigLIP+Projector RSA = **0.615** | rsa_siglip_only.py → `rsa_siglip_only.json` | d027_siglip_only_rsa |

## 3. 无效的跨方法比较

### 🔴 论文关键风险：SigLIP+Projector vs VLA RSA 不可比较

**Claim 2 ("LLM degrades action-relevant structure from 0.615 to 0.488") 基于无效比较。**

- SigLIP+Projector RSA = 0.615 → **方法 B** (within-task, euclidean, 全轨迹)
- VLA trained RSA = 0.4876 → **方法 A** (cross-task, cosine, 3-phase)

两个数字之间的差异 (0.615 − 0.488 = 0.127) **无法归因于 LLM 的影响**，因为至少 3 个方法论差异同时存在：

1. **配对方式偏差**: within-task 配对天然产生更高的 RSA，因为同一任务的 demo 在 action space 和 representation space 中更相似，correlation 更容易出现
2. **距离度量差异**: euclidean vs cosine distance 对 Spearman 相关的影响未知
3. **时序处理差异**: 全轨迹 vs 3-phase binning 聚合方式不同

### 其他潜在无效比较

以下跨方法比较在代码中存在但同样无效：

- `rsa_image_mean.py` 硬编码了 `"siglip_projector": 0.6153`（方法B）与自己的方法A结果做比较
- `rsa_siglip_only.py` 的 `"comparison"` 字典混合了方法A数字 (0.4876, 0.4846, 0.4802, 0.388) 和自己的方法B结果

### 方法 A 内部比较（有效）

以下比较在方法 A 内部，方法一致，是有效的：
- trained (0.4876) vs untrained (0.4846) — 有效
- with-inst (0.4846) vs no-inst (0.4802) — 有效
- instruction control 各条件对比 — 有效
- VLA vs DINO (0.388) — 有效（DINO 也用方法 A）
- last_preaction (0.4876) vs image_mean (0.5014) — 有效（同方法A，不同 token）

## 4. 修复建议

要使 SigLIP+Projector RSA 与 VLA RSA 可比较，需要二选一：

**选项 1**: 用方法 A 重算 SigLIP+Projector RSA（cross-task global + cosine + 3-phase）
**选项 2**: 用方法 B 重算所有 VLA RSA（within-task + euclidean + 全轨迹）

推荐选项 1，因为方法 A 覆盖更多脚本，重算成本最低。
