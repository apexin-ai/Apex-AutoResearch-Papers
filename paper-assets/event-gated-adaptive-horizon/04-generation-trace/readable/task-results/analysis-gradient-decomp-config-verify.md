# analysis gradient decomp config verify

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient-decomp-config-verify_20260516T222731_result.json`
- **Structured JSON:** [`17211f2d7c6cc37fae17.json`](../../sessions/17/17211f2d7c6cc37fae17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结结果：

---

## 梯度分解修正测量结果

### 配置对比

| 参数 | 错误配置（旧脚本） | 正确配置（008d 训练） |
|------|-------------------|---------------------|
| gate_fixed_dt | 0 | **2** |
| gate_subsample_max_dt | 8 | **2** |
| dt 范围 | 1-8（随机） | 1-2��log-uniform） |

### 核心发现

**008d at 55K（正确配置）：obs=16.3%, reward=49.0%, KL=34.7%**
**009e at 112K（正确配置）：obs=21.5%, reward=38.1%, KL=40.4%**

论文 claim "obs 93%, reward 0%, KL 7%" **在任何配置下均无法复现**：
- 正确配置：reward 主导（38-49%），obs 最低（16-22%）
- 错误配置：KL 主导（49-53%），obs/reward 相当（22-28%）

### 93% 来源
是 `artifacts/gradient_evolution_018v2.json` 中一个手写 note，声称 "008d at 105K: obs=93%"。但没有 105K checkpoint（008d 到 55K 就停了，009e 续到 112K），也没有任何保存的测量数据支持此数字。

### 对论文的影响
"obs decoder 主导 dt_emb 梯度" 的叙事需要修改。实际情况是 **reward 和 KL 合计贡献 75-85%** 梯度，obs 反而最小。这改变了 SGS（stop-gradient from decoder to dt_emb）的理论解释。

---
