# code fix bugs and rerun both

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_bugs_and_rerun_both_20260521T211425_result.json`
- **Structured JSON:** [`ec5f8a15e18b93303e11.json`](../../sessions/ec/ec5f8a15e18b93303e11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有实验完成。汇总结果：

---

## Bootstrap 非对称性结果

| 模型 | ZH→EN bal_acc | EN→ZH bal_acc | Observed diff | Bootstrap mean | 95% CI | CI 排除 0 |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Llama 3.1** | 0.7132 (L15) | 0.5956 (L5) | +0.1176 | +0.1182 | [0.0429, 0.1957] | **Yes** |
| **Qwen 3** | 0.7321 (L18) | 0.6726 (L23) | +0.0595 | +0.0580 | [-0.0367, 0.1481] | No |

**结论**：Llama 的 ZH→EN 显著优于 EN→ZH（CI 排除 0），Qwen 的不对称性不显著。

---

## MLP vs Linear Probe 对比

| 模型 | 方向 | Linear bal_acc | MLP bal_acc | 差值 | 结论 |
|------|------|:---:|:---:|:---:|------|
| **Llama** | EN→EN | 0.7757 (L28) | **0.8051** (L16) | +0.0294 | MLP 提升，best layer 前移 |
| **Llama** | ZH→ZH | 0.7206 (L13) | **0.7463** (L7) | +0.0257 | MLP 提升 |
| **Llama** | EN→ZH | 0.5956 (L5) | **0.6875** (L18) | +0.0919 | MLP 大幅提升，best layer 后移 |
| **Llama** | ZH→EN | 0.7132 (L15) | **0.7500** (L15) | +0.0368 | MLP 提升，best layer 不变 |
| **Qwen** | EN→EN | 0.7500 (L24) | **0.7738** (L14) | +0.0238 | MLP 提升，best layer 前移 |
| **Qwen** | ZH→ZH | 0.7262 (L14) | **0.7500** (L2) | +0.0238 | MLP 提升，best layer 大幅前移 |
| **Qwen** | EN→ZH | 0.6726 (L23) | **0.6964** (L22) | +0.0238 | MLP 小幅提升 |
| **Qwen** | ZH→EN | 0.7321 (L18) | **0.7381** (L8) | +0.0060 | MLP 微弱提升，best layer 前移 |

**核心发现**：
1. MLP 在所有方向均优于 Linear，提升 +0.6~+9.2 pp
2. 跨语言方向提升最大：Llama EN→ZH 从 0.5956→0.6875（+9.2 pp），说明非线性特征确实有帮助
3. MLP 的 best layer 普遍前移，提示非线性探针能在更浅层提取信息

---
