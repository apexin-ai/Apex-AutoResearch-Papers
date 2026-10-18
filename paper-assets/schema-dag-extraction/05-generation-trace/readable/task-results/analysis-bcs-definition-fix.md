# analysis bcs definition fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bcs_definition_fix_20260516T043644_result.json`
- **Structured JSON:** [`acf55c501247c77b667f.json`](../../sessions/ac/acf55c501247c77b667f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## 执行结果

### Step 1: 代码修复 ✓
- `src/compute_bcs.py`: `compute_bcs` 改为 MEAN，旧版保留为 `compute_bcs_max` (deprecated)
- `src/run_docred.py`: `compute_bcs` 改为 MEAN
- 原文件备份为 `.bak`

### Step 2: BCS 重算 ✓
| 组 | 旧 BCS (MAX) | 新 BCS (MEAN) |
|---|---|---|
| 16rel (n=100) | [0.653, 0.900], mean=0.826 | [0.479, 0.705], mean=0.579 |
| 80rel (n=25) | [0.646, 0.823], mean=0.720 | [0.509, 0.598], mean=0.548 |
| 80pool_16sub (n=100) | 已是 MEAN ✓ | mean=0.557 |

### Step 3: 统计分析（MEAN BCS）

**回归：**
| 组 | slope | 95% CI | r | p |
|---|---|---|---|---|
| 16rel | **-0.509** | [-0.686, -0.336] | -0.467 | 9.6e-7 |
| 80pool_16sub | **-0.401** | [-0.701, -0.069] | -0.221 | 0.027 |
| 80rel | +0.221 | [-1.303, +1.695] | +0.064 | 0.76 |

**Permutation test (slopes):**
- 16rel vs 80pool_16sub: p=0.598 (n.s. — slopes 方向一致)
- 16rel vs 80rel: p=0.027 *

**Quartile Δ(high−low BCS):**
- 16rel: **-5.31pp** CI[-7.44, -3.19] (显著)
- 80pool_16sub: -3.92pp CI[-8.17, +0.38]
- 80rel: -1.04pp CI[-10.12, +8.04]

**Practical magnitude (16-rel):** IQR=0.057, 对应 acc gap = **-2.89pp** CI[-4.30, -1.71]

### Step 4: 产出 ✓
- 服务器: `/root/schema-dag-extraction/artifacts/bcs_fix/bcs_fix_results.json`
- 本地: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/bcs_fix/bcs_fix_results.json`

核心结论不变：BCS-accuracy 负相关在 16-rel 和 80pool_16sub 中显著。修改后 |r| 有所降低（因为 MEAN 压缩了 BCS 方差），但 slope 绝对值反而增大，方向一致。

---
