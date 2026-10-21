# analysis 30pct retention deploy

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_30pct_retention_deploy_20260517T071611_result.json`
- **Structured JSON:** [`a99977426515eb173e07.json`](../../sessions/a9/a99977426515eb173e07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果与原始假设**不同**：

## 30% Global Top-k Per-Layer Retention 结果

| 区域 | 层范围 | 平均 Retention | vs Uniform 70% |
|------|--------|---------------|-----------------|
| Early | L0-7 | **77.1%** | +7.1% |
| Middle | L8-23 | **76.4%** | +6.4% |
| Knowledge | L12-20 | **79.7%** | +9.7% |
| **Late** | **L24-31** | **50.1%** | **-19.9%** |

### 5 个 Starved 层（全在尾部）

| Layer | Retention | 状态 |
|-------|-----------|------|
| L27 | 49.3% | STARVED |
| L28 | 40.4% | STARVED |
| L29 | 46.0% | STARVED |
| L30 | 36.6% | STARVED |
| L31 | **28.4%** | **CRITICAL** |

### 关键发现

原假设"中间层知识层被饿死"**不成立**。实际上：

1. **被饿死的是尾部层 L27-31**，而非 knowledge layers。Global allocation 反而给了 knowledge layers 更多 neurons（79.7% > uniform 70%）。

2. **原因**：尾部层激活分布极度长尾。L31 的 std/mean = 1.89，max = 9.89（是 mean 的 56 倍）。Mean-normalization 后，少数高分 neuron 在全局竞争中"虹吸"了预算，但该层大多数 neuron 被淘汰。

3. **对 MMLU 的影响**：尾部层负责最终 token logit 形成。L31 只保留 28.4% neurons，直接破坏了输出分布的精度，解释了 MMLU 25.27%（global）vs 38.61%（TEAL）的差距。TEAL 的 per-layer uniform 保障每层至少 70%，避免了这种尾部崩溃。

这一发现需要调整论文中关于 global allocation 失败机制的叙述：问题不是"饿死知识层"，而是**尾部层长尾分布导致的 budget 虹吸效应**。

---
