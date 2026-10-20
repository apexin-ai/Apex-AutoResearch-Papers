# ssh structure overlap analysis

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_structure_overlap_analysis_20260521T155828_result.json`
- **Structured JSON:** [`a8328557bbcaa7e70b86.json`](../../sessions/a8/a8328557bbcaa7e70b86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

原始 score 文件不可用于精确重建 `sft_cka_only_20` 和 `sft_standard_20` 的 group-level masks。但我已有完整的 per-layer 维度数据来计算 Jaccard bounds。让我编译最终分析。

---

## CKA-only 20% vs Standard 20% — Jaccard Overlap 分析

### 基本参数
- 原始 intermediate_size = 18944, group_size = 676, groups/layer = 28, 总 MLP groups = 784
- Attention: 两种方法都未剪枝（num_kv_heads 保持 4/layer）

### Per-layer MLP 剪枝对比

| Layer | Original | CKA-only | Standard | CKA removed | STD removed | 分析 |
|-------|----------|----------|----------|-------------|-------------|------|
| **0** | 18944 | 8128 | 8128 | **16** | **16** | 两者都重剪 |
| **1** | 18944 | 8128 | 8128 | **16** | **16** | 两者都重剪 |
| **2** | 18944 | 8128 | 8128 | **16** | **16** | 两者都重剪 |
| **3** | 18944 | 8128 | 8128 | **16** | **16** | 两者都重剪 |
| **4** | 18944 | 8128 | 8128 | **16** | **16** | 两者都重剪 |
| **5** | 18944 | 8128 | 8128 | **16** | **16** | 两者都重剪 |
| **6** | 18944 | 8128 | 18944 | **16** | 0 | CKA-only 独有 |
| **7** | 18944 | 18268 | 18944 | 1 | 0 | CKA-only 独有 |
| **8** | 18944 | 8128 | 18944 | **16** | 0 | CKA-only 独有 |
| **9** | 18944 | 8128 | 18944 | **16** | 0 | CKA-only 独有 |
| 10-15 | 18944 | 18944 | 18944 | 0 | 0 | 两者都保留 |
| **16** | 18944 | 18944 | 14212 | 0 | 7 | Standard 独有 |
| **17** | 18944 | 18944 | 16240 | 0 | 4 | Standard 独有 |
| **18** | 18944 | 18944 | 14212 | 0 | 7 | Standard 独有 |
| **19** | 18944 | 16240 | 8128 | 4 | **16** | 重叠 ≤ 4 |
| **20** | 18944 | 17592 | 17592 | 2 | 2 | 重叠 ≤ 2 |
| **21** | 18944 | 11508 | 13536 | 11 | 8 | 重叠 ≤ 8 |
| **22** | 18944 | 18944 | 16240 | 0 | 4 | Standard 独有 |
| **23** | 18944 | 13536 | 8128 | 8 | **16** | 重叠 ≤ 8 |
| **24** | 18944 | 9480 | 8128 | 14 | **16** | 重叠 2-14 |
| **25** | 18944 | 18944 | 8128 | 0 | **16** | Standard 独有 |
| **26** | 18944 | 18944 | 13536 | 0 | 8 | Standard 独有 |
| **27** | 18944 | 8128 | 18944 | **16** | 0 | CKA-only 独有 |

**总计**: CKA removed = 200, Standard removed = 200

### Jaccard 计算（bounds）

没有精确的 group index masks（原始 score 文件已删除，pruning_metadata.pt 未生成），只能从维度推断 **上下界**。

**Pruned set Jaccard:**
- 交集下界 = 6×4 + 2 = **26** (layers 0-5 各至少 max(0, 16+16-28)=4, layer 24 至少 max(0,14+16-28)=2)
- 交集上界 = 6×16 + 4+2+8+8+14 = **132** (layers 0-5 各至多 16, plus other overlapping layers)
- **Jaccard_pruned ∈ [26/374, 132/268] = [7.0%, 49.3%]**

**Retained set Jaccard:**
- **Jaccard_retained ∈ [410/758, 516/652] = [54.1%, 79.1%]**

### 核心发现：剪枝分布截然不同

| 区域 | CKA-only | Standard |
|------|----------|----------|
| 早期层 (0-9) | **重剪** (145 groups, 72.5%) | 仅剪 L0-5 (96 groups) |
| 中间层 (10-15) | 完全保留 | 完全保留 |
| 后期层 (16-27) | 集中在 L19-24, L27 (55 groups) | 广泛分布 L16-26 (104 groups) |

### 仅 CKA-only 剪枝的结构（Standard 保留）
- Layers 6, 7, 8, 9, 27: 共 65 groups
- CKA-only 认为这些层冗余（低 CKA 独特性），Standard importance 认为它们重要

### 仅 Standard 剪枝的结构（CKA-only 保留）
- Layers 16, 17, 18, 22, 25, 26 (完整): 共 46 groups
- Layer 19 中 Standard 多剪 12 groups, L23 多剪 8 groups, L25 全部 16 groups
- Standard 认为这些后期层的 importance 低，但 CKA 认为它们有独特表征

### 精度说明
以上 Jaccard 数值为 **bounds（非精确值）**。精确值需要 group-level pruning masks，但这些 masks 在原始 pruning 运行时未保存（`pruning_metadata.pt` 是后来添加的功能）。原始 importance scores 已不可用，无法重建。

---
