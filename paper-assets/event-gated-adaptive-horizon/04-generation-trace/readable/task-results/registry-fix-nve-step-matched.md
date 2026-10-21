# registry fix nve step matched

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry_fix_nve_step_matched_20260524T085046_result.json`
- **Structured JSON:** [`d342b1b9742e87e9ef14.json`](../../sessions/d3/d342b1b9742e87e9ef14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验的 registry 已更新成功。汇总：

### s1 (exp_009e_008d_walker_s1)
- ve_ratio peak: **1.6663 @55K**
- Step-matched baseline: 0.4035 @55K
- **NVE peak: 4.13× @55K**（paper onset NVE @45K = 2.09×）
- Final NVE: 1.57× @105K
- 分类: **onset_collapse**

### s2 (exp_009b_008d_walker_s2)
- ve_ratio peak: **0.5703 @55K**
- Step-matched baseline: 0.331 @45K
- **NVE peak: 1.62× @45K**（25K 算术峰 2.04× 因 baseline<0.1 排除）
- Final NVE: 0.38× @105K（self-corrected，eval 268）
- 分类: **onset_self_correcting**

### s4 (exp_008d_civo_trigger_s4)
- ve_ratio peak: **3.0294 @105K**
- Step-matched baseline: 0.6564 @105K
- **NVE peak: 4.62× @105K**
- 分类: **onset_collapse**

所有 `backfill_error` 标注已清除，替换为正确的 step-matched NVE 值。

---
