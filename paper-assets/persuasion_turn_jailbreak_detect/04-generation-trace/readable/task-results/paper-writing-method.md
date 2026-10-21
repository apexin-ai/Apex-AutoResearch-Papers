# paper writing method

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260518T041906_result.json`
- **Structured JSON:** [`38a653398e9ca47262f3.json`](../../sessions/38/38a653398e9ca47262f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`method.tex` 已写入 `paper/method.tex` 并注册。

结构概要：
- **Problem Formulation**: 定义 $C = \{u_1, a_1, \ldots\}$，binary classification over user turn prefixes，解释为何只用 user turns
- **Stage 1**: DeBERTa-v3-base + multi-task (8-class strategy + binary intent)，loss $L = L_{\text{intent}} + \lambda \cdot L_{\text{strategy}}$，完整 8-class taxonomy 列表，Qwen3-8B annotation + ablation validation
- **Stage 2**: mean pooling $\bar{h} = \frac{1}{K}\sum h_i$ + 2-layer MLP，frozen encoder weights
- **Design Rationale**: 4 个 paragraph 分别回答 why persuasion fine-tuning / why mean pooling / why 8-class / why vanilla baseline

与 experiments.tex 一致性已验证：$\lambda=1.0$、mean pooling、DeBERTa-v3-base、seed/epoch 等细节留给 Experiments。无 em-dash、无 -ing phrase endings、无过度分段。

---
