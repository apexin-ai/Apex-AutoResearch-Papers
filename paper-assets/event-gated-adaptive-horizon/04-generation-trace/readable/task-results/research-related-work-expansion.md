# research related work expansion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related-work-expansion_20260516T194613_result.json`
- **Structured JSON:** [`da05f6ee3885db2c8937.json`](../../sessions/da/da05f6ee3885db2c8937.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。新增 11 篇论文已写入 `artifacts/related_work_expansion.yaml` 并注册到 manifest。

**覆盖情况：**

| 方向 | 新增论文 | 说明 |
|------|---------|------|
| Plasticity loss | Abbas 2023 (CoLLAs), Dohare 2024 (Nature), Juliani 2024 (NeurIPS) | 从现象发现到系统研究 |
| Gradient conflict | PCGrad (NeurIPS'20), CAGrad (NeurIPS'21), GradNorm (ICML'18) | SGS 的理论基础链 |
| Value overestimation in MBRL | Luis 2024 (JMLR), Lai 2020 (ICML), Hutson 2024 (NeurIPS) | 分布式估计+双向模型+任务感知预测 |
| Temporal abstraction failures | Bacon 2017 (AAAI), Li 2024 (ICML) | option退化+理论分析skills何时有害 |

**注意：** TD3、HarmonyDream、PETS、MOPO 已在现有 literature_map 中（`fujimoto2018td3`, `ma2024harmonydream`, `chua2018pets`, `yu2020mopo`），无需重复添加，只需确保论文正文 related work 部分引用它们。

`hutson2024policyshaped` (relevance=5) 是最值得关注的 direct competitor——与 SGS 解决同一问题（MBRL 模型容量浪费），但用分割+对抗学习而非梯度停止。

---
