# analysis figure data gaps

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_figure-data-gaps_20260516T215817_result.json`
- **Structured JSON:** [`422168a8a8b67af86e31.json`](../../sessions/42/422168a8a8b67af86e31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已保存：

**1. `gradient_decomposition_008d.json`**
从 checkpoint 直接测量（50 batches, GPU 上 forward+backward）：
- **008d @ 55K**: obs=39.5%, reward=24.8%, kl=34.8%, cont=0.9%
- **009e @ 112K** (同配置延长): obs=32.0%, reward=36.0%, kl=31.3%, cont=0.7%
- **018v2 @ 112K** (反事实): obs=38.4%, reward=33.9%, kl=26.2%, cont=1.4%
- 对比：018v2 实际训练时 SGS 生效，dt_emb 只接收 KL=100%

与先前分析（gen_figures.py 中 55K: 25.8/23.5/50.7, 105K: 93/0/7）有差异，已在 JSON 中标注。定性结论一致：obs 梯度是 dt_emb 的主要驱动力之一，SGS 将其完全阻断。

**2. `rssm_fidelity_data.json`**
从 metrics.jsonl 提取（已验证每个数值）：
- 105K 对比：baseline obs_loss=0.452 < 009e=0.682 < 008f=0.699 < 018v2=0.718
- reward_loss 各条件差异不大（~0.57-0.60）
- dyn_loss: gated 变体（5.4-5.7）显著高于 baseline（3.8）
- 包含完整 trajectory 数据供作图

---
