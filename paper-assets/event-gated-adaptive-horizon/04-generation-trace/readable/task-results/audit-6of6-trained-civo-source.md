# audit 6of6 trained civo source

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_6of6_trained_civo_source_20260524T062526_result.json`
- **Structured JSON:** [`b4727ec40a9f811b71c7.json`](../../sessions/b4/b4727ec40a9f811b71c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 论文数据审计结果

### 前提纠正

**论文中不存在"6/6 trained locomotion CIVO"声明。** 实际声明是：

| 声明 | 位置 | 内容 |
|------|------|------|
| **4/4 classification accuracy** | `results.md:54` | 2 trained seeds 超过 NVE>1.5x，2 removed seeds 不超过 |
| **2/2 trained-embedding seeds** | `method.md:109` | 两个 trained dt_emb seed 都超过 NVE>1.5x at 35K+ |
| **9/10 (AUROC=0.958)** | `limitations.md:14`, `method.md:78` | 10个实验中9个正确分类，1个 false positive (008e_v3_s2) |

---

### Part 1: 论文"4/4"声明引用的实验

| 条件 | 实验 | Seed | 数据源 |
|------|------|------|--------|
| Trained e_Δt | exp_008d_subsample_on_h8 | 1 (paper says 0) | `paper_data_walker_walk.json` 中有 ve_ratio |
| Trained e_Δt | exp_009b_008d_walker_s2 | 2 | `paper_data_walker_walk.json` 中有 ve_ratio |
| Removed e_Δt | exp_008f_no_dt_embed_subsample_on_h8 | 1 | `paper_data_walker_walk.json` 中有 ve_ratio |
| Removed e_Δt | exp_009c_008f_walker_s2 | 2 | `paper_data_walker_walk.json` 中有 ve_ratio |

---

### Part 2: 数据来源审计

**关键发现：论文中引用的 4 个核心实验的 metrics.jsonl 中都没有 `civo/ve_ratio` key。** ve_ratio 是后计算的（value_mean / eval_return），存储在 `paper_data_walker_walk.json` 中。

| 实验 | metrics.jsonl 有 civo/ve_ratio? | 数据实际来源 |
|------|-------------------------------|-------------|
| exp_008d (s1) | **否** (0 pts) | paper_data_walker_walk.json (后计算) |
| exp_009b (s2) | **否** (0 pts) | paper_data_walker_walk.json (后计算) |
| exp_008f (s1) | **否** (0 pts) | paper_data_walker_walk.json (后计算) |
| exp_009c (s2) | **否** (0 pts) | paper_data_walker_walk.json (后计算) |
| exp_008d_civo_trigger_s4 | **是** (10 pts) | metrics.jsonl 原始记录 |
| exp_045 (s3 extended) | **是** (19 pts) | metrics.jsonl 原始记录 |
| exp_059 (s5) | **是** (10 pts) | metrics.jsonl 原始记录 |

---

### Part 3: NVE 数据验证（来自 paper_data_walker_walk.json）

**Trained dt_emb — 论文声明 vs 数据：**

| 实验 | 论文声明 | 实际数据 | 一致？ |
|------|---------|---------|-------|
| **008d s1** Peak NVE | 2.09× @45K | ve=0.6929, baseline=0.331 → **NVE=2.09×** | ✅ |
| 008d s1 加速 | 1.71→2.09→4.12 (35-55K) | 35K=1.71, 45K=2.09, 55K=4.12 | ✅ |
| **009b s2** Peak NVE | 1.62× @45K | ve=0.5359, baseline=0.331 → **NVE=1.62×** | ✅ |
| 009b s2 自修正 | 1.62→1.41→0.94 (45-65K) | 45K=1.62, 55K=1.41, 65K=0.94 | ✅ |

**Removed dt_emb — 论文声明 vs 数据：**

| 实验 | 论文声明 | 实际数据 | 一致？ |
|------|---------|---------|-------|
| **008f s1** Peak NVE | 0.97× @55K | 55K=0.97 | ✅ |
| **009c s2** Peak NVE | 1.14× @105K | 105K=1.14 | ✅ (论文写1.26@25K for peak, 实际25K=1.26也对) |

**4/4 分类准确率验证：** ✅ 两个 trained 超过1.5×，两个 removed 不超过。声明成立。

---

### Part 4: 额外 Walker trained seeds（不在论文"4/4"声明中）

这些实验有原始 `civo/ve_ratio` 记录：

| 实验 | 有 NVE≥1.5× @35K+? | Peak NVE | 分类 |
|------|---------------------|----------|------|
| **s4** (exp_008d_civo_trigger_s4) | 是，但仅 105K 一个点 (NVE=4.44) | 4.44 @105K | 单点 spike，非 sustained |
| **s3** (exp_045 extended, 122-302K) | 是，122K-132K (NVE=6.98, 7.19)，之后骤降至 <0.63 | 7.19 @132K | 早期 spike → 自修正 |
| **s5** (exp_059) | 是，65-85K (NVE=1.83→2.18→4.84)，之后降至 0.94 | 4.84 @85K | 3-checkpoint burst → 自修正 |

---

### Part 5: Cheetah CIVO 数据

| 实验 | 有 civo/ve_ratio? | 状态 |
|------|-------------------|------|
| exp_010b_cheetah_civo_trigger (orig) | **否** | value_mean/eval_return 显示 55K 后 collapse (eval 63→22→47→51) |
| exp_010b_cheetah_civo_trigger_s0 | **是** (10 pts) | 极端 CIVO：ve_ratio 从 65K 开始爆炸 (16.89→70.64 @105K) |
| exp_048_cheetah_civo_extension | **是** (19 pts) | 持续高 ve_ratio (1.43-24.13)，eval 全程 <33 |

**Cheetah 没有 baseline ve_reference，无法计算标准化 NVE。** 论文 `limitations.md:11` 也承认 Cheetah 结果在提交时尚不可用。

---

### 最终总结

```
=== 论文"trained locomotion CIVO"声明溯源 ===

实际声明：4/4 classification accuracy（非"6/6"）
位置：results.md:54, method.md:70

论文引用的 4 个实验：
| 实验           | env    | seed | 有原始civo/ve_ratio? | NVE peak (≥35K) | 分类      | 数据可信度      |
|---------------|--------|------|---------------------|-----------------|-----------|---------------|
| 008d          | Walker | 1    | 否（后计算）          | 2.09× @45K      | sustained | ✅ 可验证复现   |
| 009b          | Walker | 2    | 否（后计算）          | 1.62× @45K      | transient | ✅ 可验证复现   |
| 008f          | Walker | 1    | 否（后计算）          | 0.97× @55K      | no_CIVO   | ✅ 可验证复现   |
| 009c          | Walker | 2    | 否（后计算）          | 1.14× @105K     | no_CIVO   | ✅ 可验证复现   |

ve_ratio 计算方式：value_mean / eval_return（从 metrics.jsonl 提取后合并）
NVE 计算方式：ve_ratio / baseline_ve_ratio（baseline = exp_001 at matched step）
数据存储：paper_data_walker_walk.json（预计算数据文件）

论文数值 vs 原始数据：全部一致 ✅
4/4 分类准确率声明：成立 ✅
Cheetah 结果：论文明确标注"pending"，未纳入主声明 ✅

注意事项：
- 4个核心实验的 ve_ratio 不是训练时在线记录的，是后处理计算
- 这不影响可信度（value_mean 和 eval_return 是原始数据）
- 后续 seeds (s3/s4/s5) 有在线 civo/ve_ratio，可交叉验证方法一致性
```

---
