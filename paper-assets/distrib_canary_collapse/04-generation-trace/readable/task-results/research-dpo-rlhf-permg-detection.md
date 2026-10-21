# research dpo rlhf permg detection

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dpo_rlhf_permg_detection_20260521T053545_result.json`
- **Structured JSON:** [`cee3c8851f35d1941b83.json`](../../sessions/ce/cee3c8851f35d1941b83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 artifact 已注册。总结：

## 结果

**可行性：确认可行，公开 checkpoints 充足。**

### 最佳候选

| 排名 | 模型 | 参数量 | 阶段数 | CPU 可行 |
|------|------|--------|--------|----------|
| 1 | **OLMo-2-0425-1B** | 1B | 4 (Base→SFT→DPO→Instruct) | 是 |
| 2 | **SmolLM3-3B** | 3B | 4 (Midtrain→SFT→APO→LC) | int8 量化后可行 |
| 3 | Tulu-3-8B | 8B | 3 (SFT→DPO→RLVR) | 需 GPU |

OLMo-2-1B 是首选：Apache-2.0、4 个对齐阶段分别有独立 HF repo、RLVR 阶段还有 per-20-step checkpoints、1B 参数 CPU 可推理。

### 文献支撑

DPO/RLHF 导致 diversity collapse 已是共识：
- Kirk et al. (ICLR 2024): RLHF 显著降低多样性，across-input mode collapse
- Karouzos et al. (2026): 用 OLMo 追踪 collapse 发生在哪个阶段（SFT 或 DPO，取决于数据）
- Guo et al. (DivPO): 证明标准 DPO 目标函数本身允许退化最优解（所有概率集中到一个 response）
- Tomihari (2026): NTK 分析证明 entropy 在 RL post-training 中单调下降

### 实验方案

- WikiText-103 test 前 200 句作为 eval set
- 对 OLMo-2-1B 的 4 个阶段各生成 5 个 continuation（T=1.0）
- 计算 token_entropy、distinct-1/2/3、ECE、perplexity、self-BLEU
- 对 4-stage 序列跑 PermG cross-correlation 检测 entropy→distinct lead-lag
- CPU 预估：200 prompts × 4 stages ≈ 14-20 小时；GPU 则 2-4 小时

### Falsifiable prediction

> If DPO compresses the output distribution before lexical diversity visibly declines, PermG should detect a significant entropy → distinct-n lead at the DPO stage, with cross-correlation peak at negative lag.

### 产出文件

- `artifacts/dpo_application/dpo_permg_detection.json` — 完整搜索结果 + 可行性评估 + 实验方案 + 文献综述
- `artifacts/dpo_application/paper_snippet_dpo_generalizability.tex` — 论文 Discussion 段落（2 段英文，含 falsifiable prediction）

---
