# analysis grpo qwen math 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_qwen_math_25_20260516T154652_result.json`
- **Structured JSON:** [`c02b50b46f821ddf9ea2.json`](../../sessions/c0/c02b50b46f821ddf9ea2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 分析结论：两个实验均为 NEGATIVE

### 核心发现：25% 反而比 20% 好（反直觉）

| 指标 | RASP 20% → 25% | Standard 20% → 25% |
|------|----------------|---------------------|
| reward | 0.061 → **0.206** (3.4x) | 0.044 → **0.182** (4.1x) |
| frac_zero_std | 0.675 → **0.350** | 0.850 → **0.325** |
| collapse | permanent → **no collapse** | permanent → **KL explosions but no reward collapse** |

### 为什么判 NEGATIVE

1. **C3 被推翻**：25% sparsity 的 collapse 比 20% 更轻而非更重
2. **RASP vs Standard 方向跨模型不一致**：DeepSeek 上 RASP 更差，Qwen Math 上 Standard 更差
3. **Standard 25% 出现新失败模式**：3 次灾难性 KL 爆炸（peak 7.9e15），但 DAPO clipping 保护了 reward 不崩溃

### Registry 更新

- `grpo_rasp_25_qwen_math`: conclusion 从 success → **negative**，补充完整 10 步 metrics 和跨稀疏度对比
- `grpo_standard_25_qwen_math`: conclusion 保持 **negative**，更新完整 metrics 和 notes

分析报告已注册为 artifact: `analysis_grpo_qwen_math_25.md`

---
