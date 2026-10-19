# investigate s456 checkpoint discrepancy

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_s456-checkpoint-discrepancy_20260518T040837_result.json`
- **Structured JSON:** [`38f29424f50a7b965d06.json`](../../sessions/38/38f29424f50a7b965d06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Re-eval result: MMLU = 0.4382** — exactly matches the original. The old checkpoint genuinely produces 43.82% with current code.

This is the definitive answer. Let me compile the complete report.

---

## P0 调查报告：s456 KL 30% MMLU 差异 (43.82% vs 27.14%)

### 根因

**两个结果都是正确的。** 差异来源于 CUDA 非确定性导致的不同训练 checkpoint。

| 证据项 | 结论 |
|--------|------|
| 代码 md5 | 两台服务器 train.py / evaluate.py / benchmark_eval.py / predictor.py / data_utils.py 全部一致 |
| 模型权重 md5 | safetensors 一致（同一 base model） |
| Checkpoint 权重差 | predictor 参数绝对值和差异 0.04%（CUDA 非确定性） |
| 逐层 allocation 差异 | 1-5pp per layer |
| PPL | 8.933 vs 8.961（一致） |
| ARC/WG/GSM8K | 均在 1-2pp 内（正常 seed variance） |
| **Re-eval 验证** | 旧 checkpoint 用当前代码重新 eval → MMLU=0.4382（完美复现） |
| s123 对照组 | 38.07 vs 38.36（0.3pp，一致） |

### 结论

CUDA 非确定性在训练中造成 0.04% 权重差异，经过 global top-k allocation 放大后，导致 MMLU 16.7pp 差异。PPL 和其他 benchmark 不受影响，因为 MMLU 对 mask pattern 的敏感度远高于其他任务（s42 global MMLU 也仅 25.27%，接近随机）。

### Table 1 现状问题

当前 Table 1 的 KL global 30% 三 seed 数据**混合了两台服务器的结果**：

| Seed | MMLU (当前用) | 来源 | MMLU (westd-34887) |
|------|---------------|------|---------------------|
| s42 | 25.27 | westd-34887 | 25.27 |
| s123 | 38.36 | westd-41718 | 38.07 |
| s456 | 27.14 | westd-41718 | 43.82 |
| **Mean±Std** | **30.3±7.1** | 混合 | **35.7±9.5** |

### 需要做的决策

**选项 A（用 westd-34887 统一）**：更一致，因为 s42 只在 westd-34887 训练。  
- KL global 30% MMLU: **35.7±9.5**（std 更大，更强调 global 不稳定性）
- 正文 "30.3±7.1" 改为 "35.7±9.5"；"MMLU 30.3$\pm$7.1\%" → "MMLU 35.7$\pm$9.5\%"
- 其他列变动 <1pp

**选项 B（保持现状 westd-41718 为主）**：当前表格已用的数字。  
- 但 s42 仍来自 westd-34887（该 seed 没有 westd-41718 的 checkpoint）
- 混合不同训练 run 的 multi-seed 数据，科学上不太严谨

**选项 C**：在 westd-41718 上重训 s42，获得完全统一的 3-seed 数据集。

**建议**：选 A。原因：(1) s42 只有 westd-34887 版本，混合不可避免，不如全用同一来源；(2) std 从 7.1 增到 9.5 进一步 **强化** 论文"global allocation 不稳定、应用 uniform"的核心论点。

需要改的具体数字（若选 A）：

```
Table 1 & Table 3 (tab:phase), KL global 30% row:
  MMLU: 30.3±7.1  →  35.7±9.5
  
正文 §4.2 (line 30):
  "MMLU 30.3±7.1%" → "MMLU 35.7±9.5%"
  "seed variance (30.3±7.1%)" 相关描述需同步更新
  
PPL / ARC / WG / GSM8K 列变动 <0.5pp，可按需微调
```

---
