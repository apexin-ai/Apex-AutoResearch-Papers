# analysis exp 061 cartpole civo check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_061_cartpole_civo_check_20260525T031446_result.json`
- **Structured JSON:** [`64478a0ee23147234c1f.json`](../../sessions/64/64478a0ee23147234c1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 结果汇总

### 1. exp_061 — Cartpole CIVO Trigger：**已完成，NEGATIVE**

3 seeds 全部达 112K steps，进程已退出。

| Seed | eval_return | value_mean | ve_ratio peak | CIVO? |
|------|-------------|------------|---------------|-------|
| s0 | 211.1 | 9.23 | **0.058** | NO |
| s1 | 269.0 | 9.32 | **0.040** | NO |
| s2 | 228.9 | 9.46 | **0.043** | NO |

**ve_ratio 全部 < 0.06，远低于 1.5x 阈值。civo/alert 全为 0。Cartpole 不触发 CIVO。**

性能对比 baseline (exp_060): eval_return 下降 ~59%，但这是 dt=2 本身的时间分辨率损失，非 CIVO 机制——exp_062 control（无 dt_emb）显示相似幅度的下降。

### 2. exp_061 CIVO 分析核心结论

- CIVO **不是** DMC locomotion 通用现象，它在 Walker/Cheetah 触发但 Cartpole 不触发
- Cartpole 值函数始终校准（value_mean 远低于 eval_return），无过估
- 可能原因：Cartpole 动力学简单（1自由度），dt=2 的 RSSM fidelity gap 不够大触发 value 发散
- **论文定位建议**：CIVO scope 描述为 "multi-joint locomotion"，Cartpole 作为 negative control

### 3. exp_062 — Cartpole Control：**运行中**

| Seed | Step | eval_return | Status |
|------|------|-------------|--------|
| s0 | 112K | 230.4 | Done |
| s1 | 112K | 255.3 | Done |
| s2 | 108K | 248.8 | **Running** |

s2 还差 ~4K steps，预计 **1-2 小时内完成**。注册表已更新，分析 artifact 已注册 (`art_20260525_b27d24`)。

---
