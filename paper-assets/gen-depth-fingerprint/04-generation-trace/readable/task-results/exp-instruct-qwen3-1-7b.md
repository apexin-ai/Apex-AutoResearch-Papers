# exp instruct qwen3 1 7b

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_instruct-qwen3-1_7b_20260518T030649_result.json`
- **Structured JSON:** [`5359a5383bff117bd93a.json`](../../sessions/53/5359a5383bff117bd93a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。汇报结果：

## exp_052 结果：Qwen3-1.7B Instruct vs Base

### Within-model 5-fold CV

| Metric | Instruct | Base | Delta |
|--------|----------|------|-------|
| **Binary F1** (gen-1 vs gen-2+) | **0.8753** [0.8667, 0.8837] | 0.8614 [0.8511, 0.8710] | **+0.014** |
| **3-class F1** (gen-0/1/2+) | 0.7324 [0.7195, 0.7450] | **0.7690** [0.7563, 0.7821] | **-0.037** |

### Per-class 3-class F1
| Class | Instruct | Base |
|-------|----------|------|
| gen-0 | 0.894 | 0.884 |
| gen-1 | **0.438** | 0.579 |
| gen-2+ | 0.866 | 0.845 |

### LOGO 跨模型泛化（已有结果）
- Instruct held-out: binary F1 = 0.658, 3-class F1 = 0.543
- Base held-out: binary F1 = 0.821, 3-class F1 = 0.802

### 关键发现

1. **Within-model binary F1 instruct 略优于 base**（0.875 vs 0.861），深度信号本身并未减弱
2. **3-class F1 instruct 更差**，瓶颈在 gen-1（0.438 vs 0.579）：chat template 包装导致 gen-0→gen-1 跳跃加大，gen-1 被频繁误分类
3. **Spearman ρ 方向反转**：instruct 的 lexical diversity 随深度递增（ρ > 0），base 则递减（ρ < 0）。这解释了 LOGO 跨模型泛化大幅下降（0.658 vs 0.821）——在 base models 上训练的分类器对 instruct 的反向 drift 方向无法适应
4. 参考 F1=0.709 的对比：within-model binary F1（0.875）远超此值；LOGO binary F1（0.658）低于此值。差异来源是评估设置不同

---
