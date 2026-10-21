# analysis exp 078 cheetah 008d s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_078_cheetah_008d_s0_20260525T143708_result.json`
- **Structured JSON:** [`49e04ef0951d44f43984.json`](../../sessions/49/49e04ef0951d44f43984.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析完成：exp_078_cheetah_008d_s0

### 核心结论：**SUCCESS** — CIVO 在 Cheetah 上成功触发

初始描述 "NVE=0.3" 具有误导性——那只是 105K 终点值。完整时间序列：

| Step | eval_return | ve_ratio | NVE |
|------|-------------|----------|-----|
| 35K | **213.7** (peak) | 0.11 | 1.24 |
| 45K | 148.9 | 0.30 | **1.70** ← onset |
| 55K | 64.5 | 0.91 | **3.66** |
| 65K | 36.8 | 1.72 | **3.55** |
| 75K | 26.1 | 2.32 | **4.10** ← peak |
| 85K | 26.7 | 2.02 | **2.74** |
| 95K | 32.5 | 1.37 | **2.26** |
| 105K | 119.5 | 0.29 | 0.48 ← self-corrected |

- **NVE>1.5 持续 5 个检查点**（45K-95K，50K steps），峰值 4.10x@75K
- CIVO alert 在 55K 和 65K 触发
- 自我修正至 105K（NVE=0.48），eval 从 26.7 恢复至 119.5
- 最终 eval 仅为 baseline 的 **26.7%**（119.5 vs 448.1）
- 分类：**onset_self_correcting**（与 Walker 009b 模式一致）

### 对论文 claims 的影响

**C2 强化**：Cheetah CIVO onset 与 Walker 在相同 step（45K）发生，跨环境一致性显著。CIVO onset 现在是 **9/9 deterministic**（8 Walker + 1 Cheetah）given trained dt_emb。

**关键差异**：Cheetah CIVO 更强（NVE 4.10 vs Walker 009b 的 1.62）但仍自我修正，而 Walker 在类似 NVE 水平（s4: 4.62, s5: 4.72）会 collapse。环境动力学影响 collapse/self-correction outcome。

### Registry & Artifact

- Registry: DONE (success), 含完整 NVE trajectory
- 报告: `artifacts/exp_078_cheetah_008d_s0/report/analysis_exp_078.md`

---
