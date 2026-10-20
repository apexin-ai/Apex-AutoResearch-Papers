# analysis negative taxonomy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_negative-taxonomy_20260524T141759_result.json`
- **Structured JSON:** [`c614d4124da3134a837b.json`](../../sessions/c6/c614d4124da3134a837b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件：`artifacts/negative_results_taxonomy.md`

35 个 negative 实验分为 8 类：
- **TCN 跨环境/剂量失败**（10）— 仅 Walker σ=0.2 部分 seeds 有效，Cheetah/PickCube 全失败
- **SGS 干预失败**（5）— 梯度阻断路线全面否定（Full-SGS 0/3 可靠）
- **Dual-critic 跨环境失败**（5）— Cheetah 双 critic 无差异化，Walker 暴露 non-CIVO collapse
- **dt>1 本身退化**（5）— temporal subsampling 自身带来 40-70% 性能损失
- **CIVO 复现/表征**（4）— 确认 CIVO 随机性（30-50% seeds 发生）
- **Event-gate 机制失败**（3）— 核心提案 v2-v4 持续失败，催生 CIVO 研究转向
- **RAVE 失败**（2）— 值裁剪未触及根因
- **Frozen dt_emb 失败**（1）— gradient starvation

跨类别关键 pattern：干预层级递进失败链（梯度→表征→值→架构），环境依赖性是系统性障碍，且 exp_038 暴露了 CIVO 以外的退化机制。

---
