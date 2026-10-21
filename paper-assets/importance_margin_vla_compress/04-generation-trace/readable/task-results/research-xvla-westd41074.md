# research xvla westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_xvla_westd41074_20260520T035434_result.json`
- **Structured JSON:** [`84a3865133687c432648.json`](../../sessions/84/84a3865133687c432648.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。汇报结果：

---

## X-VLA Token Importance 分析结果

**模型**: X-VLA-0.9B (lerobot/xvla-libero)，Linear projection connector  
**数据**: LIBERO-Object 100帧, 10 tasks  
**服务器**: westd-41074:cuda:1

### 核心发现

**Pruning curve 几乎完全平坦** — 这是目前测过最可压缩的 VLA 模型：

| Retention k | Normalized Loss |
|-------------|----------------|
| 0.30 (保留30%) | **1.0014** (+0.14%) |
| 0.50 | 1.0003 |
| 0.70 | 1.0000 |
| 1.00 | 1.0000 |

丢弃 70% 的 vision tokens 仅导致 0.14% 的 loss 增加。

**Entropy ratio**: 0.6138（中高），浅层集中（L1=0.34）→ 深层均匀（L22=0.79）

### 跨模型对比

| 模型 | Connector | k=0.3 Norm Loss | 压缩行为 |
|------|-----------|-----------------|----------|
| SmolVLA | Pixel-shuffle | Cliff-edge | 不可压缩 |
| OpenVLA | 2-layer MLP | ~1.15 (+15%) | 渐进退化 |
| **X-VLA** | **Linear proj** | **1.0014 (+0.14%)** | **几乎无损** |

### 解读

Linear projection connector 保留了 DaViT 输出的原始冗余结构——大部分信息集中在少数 token，L2 norm 即可轻松识别。相比之下，MLP projector 通过非线性变换重新分配了信息，使 token 间差异更大、更难压缩。

**这是 connector 架构论文的关键数据点**，直接支持 "connector 架构决定 token 可压缩性" 的核心论点。

已完成：memory.md 更新、registry 注册（analysis_xvla_token_importance, DONE/success）、artifact 注册（xvla_attention_entropy_perlayer.json）。

---
