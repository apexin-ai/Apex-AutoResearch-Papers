# check llama ss startup

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llama_ss_startup_20260524T071947_result.json`
- **Structured JSON:** [`84207cfb67a4037fe72d.json`](../../sessions/84/84207cfb67a4037fe72d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Llama SS training 已在运行。** 状态：

- **GPU**: RTX PRO 6000 Blackwell (97GB), 98% 利用率, 86GB 显存占用
- **训练进度**: Step 100 / 3000, Epoch 0
- **指标**: L_NTP=1.609, L_GAR=0.237, Gate mean=0.818, SS ratio 尚在 warmup（0.004）
- **配置**: LoRA + ThreadGate, SS max_ratio=0.3, 8x gradient accumulation

**Gradient conflict 分析已完成**，结果在 `/root/turn_residual_gating/results/p2_llama_gradient_conflict/gradient_conflict_analysis.json`：
- 整体 cos_sim mean ≈ 0.0045（近正交），conflict fraction = 53.1%（17/32 层负余弦）
- NTP 梯度量级远大于 GAR（median ratio ~26x），符合预期
- Layer 27 冲突最强（cos_sim = -0.149），Layer 31 几乎无交互（ratio >1000x）

一切正常运行中，无需干预。

---
