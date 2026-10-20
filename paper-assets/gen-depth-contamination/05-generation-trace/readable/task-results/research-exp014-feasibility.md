# research exp014 feasibility

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp014_feasibility_20260518T045543_result.json`
- **Structured JSON:** [`8bd89b555e09b86da26d.json`](../../sessions/8b/8bd89b555e09b86da26d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-014 可行性评估

### 实验概要
- **描述**: Common Crawl 2025/2026 snapshot 做 depth 预测，与 AlignScore + vocabulary richness 做 correlation
- **支撑 claim**: C1 (K* characterization)
- **优先级**: P2（最低）
- **依赖**: exp-005 (已完成)

### 资源现状

| 资源 | 状态 |
|------|------|
| 磁盘 | 212GB 空闲 ✅ |
| GPU | 4× 4090D 全部空闲 ✅ |
| 已缓存模型 | Pythia-1.4B, Qwen-7B ✅ |
| 已缓存数据 | C4, Wikipedia, arXiv ✅ |
| Common Crawl 网络 | **734 B/s — 基本不可用** ❌ |
| AlignScore | 未安装，需下载 ~1.7GB 模型 |

### 关键阻碍

1. **网络瓶颈（showstopper）**: 服务器到 Common Crawl CDN 下载速度 ~734 B/s。即使只下载 1GB 样本也需 ~16 天。HF 上没有原始 CC 2025/2026 snapshot 数据集。

2. **概念循环风险**: CC 野生数据没有 ground-truth depth 标签。实验只能证明 "模型预测的高 depth 文本质量更低"，reviewer 可以反驳这只是在检测低质量文本而非真实递归深度。验证力度有限。

3. **时间约束**: EMNLP ARR deadline **May 25（7 天后）**。paper_framing.md 的核心 claims 和 evidence 均未引用 exp-014。24 个实验全部完成，证据链已经很强（8 models × 3 domains × 4 decoding strategies + cross-model transfer + neural probe）。

### 判断: **不建议执行**

- **可行性**: 因网络问题，不可行（除非找到 CC 数据的国内镜像或替代来源）
- **必要性**: P2 + 不在 paper framing 中 + deadline 7 天 → 边际价值极低
- **建议**: 在论文 Future Work 中提及 naturalistic validation 方向，deadline 后有余力再做
- **不需要 Director 审批**（建议直接 skip）

---
