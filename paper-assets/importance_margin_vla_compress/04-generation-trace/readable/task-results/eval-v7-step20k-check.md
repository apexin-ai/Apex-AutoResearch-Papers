# eval v7 step20k check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v7-step20k-check_20260515T191127_result.json`
- **Structured JSON:** [`fbdaf601a7153bdf809b.json`](../../sessions/fb/fbdaf601a7153bdf809b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## v7 Step 20K Intermediate Eval 报告

### 训练趋势 (Step 16000→20000)
- **Loss**: 在 0.002–0.088 范围内正常波动，无持续上升趋势
- **Grad norm**: 最大 27.18 (step 20000)，远低于 50 的警戒线
- **LR**: 4.86e-5 → 2.84e-5，cosine decay 正常
- **Speed**: 稳定 3.2 sps
- **结论: 训练健康，无退化迹象**

### GPU 状态
- GPU 0: 2.4GB / 96GB used (RTX PRO 6000 Black)
- GPU 1: 2.5GB / 96GB used
- Eval 在 GPU 0 上成功与训练并行运行

### Step 20K Eval vs Step 8K 对比

| 指标 | 条件 | Step 8K | Step 20K | 变化 |
|------|------|---------|----------|------|
| **action_loss** | clean | 0.0303 | **0.0107** | **-65%** |
| **action_loss** | eps=0.01 | 0.0199 | **0.0120** | **-40%** |
| **action_loss** | eps=0.05 | 0.0563 | **0.0340** | **-40%** |
| **margin_mean** | clean | 0.540 | **1.074** | **+99%** |
| **margin_mean** | eps=0.01 | 0.612 | **1.008** | **+65%** |
| preservation | eps=0.01 | 0.952 | 0.913 | -4% |
| preservation | eps=0.05 | 0.718 | 0.617 | -14% |
| kendall_tau | eps=0.01 | 0.868 | 0.770 | -11% |
| kendall_tau | eps=0.05 | 0.466 | 0.141 | -70% |
| lipschitz_emp | — | 0.145 | 0.266 | +83% |

### 分析

**正面信号**:
- Action loss 全面大幅下降（核心任务指标）
- Margin 近乎翻倍，importance 区分度更强
- Clean 条件下 preservation/kendall 保持 1.0

**需关注**:
- 高 eps 下 preservation_rate 和 kendall_tau 下降，尤其 eps=0.05 的 kendall 从 0.47 降到 0.14
- Empirical Lipschitz 从 0.145 升到 0.266，模型对扰动更敏感
- 但注意：此次 eval 用 max_batches=10（8K 用 50），方差更大

**解读**: 模型学到了更强的 importance 区分（高 margin），但同时对输入扰动更敏感（高 Lipschitz）。核心任务性能（action_loss）持续改善，**后半程无退化**。高 eps 下的 robustness 下降可能部分是 eval 样本量差异导致，建议训练结束后用 max_batches=100 做完整评估确认。

**结论: v7 训练可安全继续到 30K。** 结果已保存至 `results/eval_imm_v7_step020000_quick.json`。

---
