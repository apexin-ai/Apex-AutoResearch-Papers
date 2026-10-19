# research paper research

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-research_20260514T031618_result.json`
- **Structured JSON:** [`5fc1f41f2980d63574c2.json`](../../sessions/5f/5fc1f41f2980d63574c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已更新。总结如下：

## 扫描结果

**新增 15 篇论文**（31 → 46 篇），覆盖 4 个搜索方向：

### 竞争者（2 篇，需重点关注）
- **SC-VLA** (2602.21633) — 在线 action refinement via sparse world imagination + residual RL，9% 成功率提升。与 ACR-VLA 同属 inference-time correction，但用 RL 而非统计方法
- **VLA-Pilot** (2511.14178) — Plug-and-play inference-time policy steering，用 MLLM 做 verifier + evolutionary diffusion 做 action optimizer。同属 zero-shot inference-time 方法，但无统计保证

### CP + 机器人 / 多维 CP（6 篇）
- **Fan & Sesia 2025** — 坐标级标准化做多维 CP，与我们的 per-DOF 方法论直接相关
- **OTCP** (Klein et al.) — 最优传输做多维 CP scoring
- **LCP** (2509.21955) — 可学习 nonconformity function 用于机器人规划
- **CLAPS** (2512.10294) — Lie 群上的 conformalized action prediction sets
- **LUCCa** (2409.08249) — 状态-动作空间的局部 conformal 校准
- **CRC-CBF** (2603.10392) — Conformal risk control + CBF 用于 HRI 安全

### VLA 不确定性量化（3 篇）
- **Zollo & Zemel 2025** — 首个 VLA 置信度校准研究（prompt ensembles + Platt scaling）
- **Tang et al. 2026** — "Averaging Trap" 问题，max-pooling 捕捉关键时刻不确定性
- **Valle et al. 2025** — 8 个不确定性指标 + 5 个质量指标的 VLA 评估框架

### VLA 架构 / 训练（4 篇）
- **ACoT-VLA** (CVPR 2026) — Action chain-of-thought，LIBERO-Plus 84.1%
- **AFIL** (2605.08434) — 失败轨迹作为负向引导
- **SafeDiffCon** (ICML 2025) — CP + 扩散模型安全控制
- **DiffusionVLA** (ICML 2025) — 自回归推理 + 扩散策略

### 直接竞争者分析
**未发现做 per-DOF conformal + VLA 的工作。** 最近的是 ReconVLA（已收录），它用 CQR 做 scalar action-level uncertainty，而非我们的 per-DOF 分解。SC-VLA 和 VLA-Pilot 做 inference-time correction 但不用 conformal prediction。**ACR-VLA 的 per-DOF conformal statistics 创新点仍然成立。**

---
