# research spectral collapse literature

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_spectral-collapse-literature_20260512T172025_result.json`
- **Structured JSON:** [`411a9cde0e39ba0e78eb.json`](../../sessions/41/411a9cde0e39ba0e78eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 artifacts 目录。由于 `save_project_file` 白名单不包含任意文件名，报告已直接保存到：

`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/literature_survey_spectral_collapse.md`

---

## 调研核心结论

**SIGMA (2026-01) 已经将谱分析（Gram 矩阵特征值谱）用于 LLM model collapse 检测。** 我们不能再 claim "首次将谱分析用于 collapse 检测"。

**但我们的 novelty 依然成立：**

| 现有工作 | 做了什么 | 没做什么（= 我们的空间） |
|---------|---------|----------------------|
| **SIGMA** | Gram 矩阵谱界量化 collapse | 无控制机制，未验证 leading indicator |
| **ERBP** | entropy-reservoir 理论框架 | reservoir 参数需先验设定，无在线调节 |
| **EntroPIC** | PI 控制稳定 RLHF 熵 | 控制 loss 系数而非数据比例，不用谱指标 |
| **DIDS** | FIM 驱动动态域采样 | 不针对 collapse，非 real/synthetic 二元 |

**我们的独特贡献 = SIGMA 的谱监控 + ERBP 的理论动机 + EntroPIC 的 PI 控制范式，首次组合成：谱有效秩 → PI 控制器 → 动态 real/synthetic 比例调节。**

**推荐的 paper framing 调整**：从 "spectral metrics detect collapse"（已被 SIGMA 占据）转向 **"from passive monitoring to active closed-loop control"**。

**最大风险**：如果 MVP 实验显示谱有效秩与 PPL 同步下降（无 leading indicator 特性），需 pivot 到 "higher-resolution indicator" framing。

---
