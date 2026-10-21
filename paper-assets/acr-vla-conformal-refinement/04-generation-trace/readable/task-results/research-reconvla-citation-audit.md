# research reconvla citation audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reconvla-citation-audit_20260513T220502_result.json`
- **Structured JSON:** [`31c2612ad2048a39c630.json`](../../sessions/31/31c2612ad2048a39c630.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。结论明确。

---

## 调查结果

### 1. bib 条目实际指向的论文

`chen2026reconvla` 指向 **arXiv 2604.16677**（非用户提到的 2508.10333）：

| 字段 | 内容 |
|------|------|
| 标题 | ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework |
| 作者 | Lingling Chen, Zongyao Lyu, William J. Beksi (UT Arlington) |
| 实际方法 | 对 VLA action token 输出施加 **conformal prediction**，生成校准的不确定性估计，用于 failure detection |
| 提交日期 | 2026-04-17 |

**该论文完全不包含 "draw K samples, select closest to sample mean" 这一方法。**

### 2. arXiv 2508.10333（用户提到的 ID）

这是另一篇同名论文：*"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver"*，AAAI 2026 杰出论文，关于 **visual attention reconstruction via diffusion transformer**。与 action sampling 也完全无关。

### 3. "draw K samples → select closest to sample mean" 方法是否有出处

搜索了以下关键词组合，**未找到任何已发表论文描述这一具体方法**：
- "action sample selection" + "sample mean" + "Euclidean distance"
- "multiple action samples argmin mean distance"
- "sample consensus action selection"

最接近的已发表工作是 **RoboMonkey**（arXiv 2506.17811），但它使用 sampling + VLM verifier 而非 scalar Euclidean distance to mean。

---

## 结论：**引用造假确认**

我们论文中存在两层问题：

1. **方法归因造假**：我们在 `introduction.tex:14`、`related_work.tex:39`、`experiments.tex:49` 中将一个自造的 baseline 方法（"draw K samples, select closest to sample mean via scalar Euclidean distance"）归因给 Chen et al. 的 ReconVLA，但该论文根本不包含这个方法。

2. **讽刺的是**：真实的 ReconVLA (2604.16677) 实际上也在做 **conformal prediction for VLA**——和我们的 ACR-VLA 高度相关。我们把一个真正的竞品论文错误描述成了一个更弱的 strawman baseline。

涉及的文件位置：
- `introduction.tex` 第 14, 23 行
- `related_work.tex` 第 39, 43 行
- `experiments.tex` 第 49, 73, 80, 83, 84, 157, 195 行
- `references.bib` 第 57-64 行

**建议**：将 "ReconVLA" baseline 改名为描述性名称（如 "Sample-Mean Selection" 或 "Scalar-Distance Selection"），标注为我们自己构建的 baseline，移除对 chen2026reconvla 的虚假归因。同时需要重新审视如何在 related work 中正确讨论真实的 ReconVLA 论文。

Sources:
- [ReconVLA (2508.10333) - Reconstructive VLA](https://arxiv.org/abs/2508.10333)
- [ReconVLA (2604.16677) - Conformal Prediction VLA](https://arxiv.org/html/2604.16677v1)
- [RoboMonkey - Test-Time Scaling](https://arxiv.org/abs/2506.17811)
- [Diffusion Policy](https://arxiv.org/abs/2303.04137)

---
