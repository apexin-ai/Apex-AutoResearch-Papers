# ops db sweep collect and eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_db-sweep-collect-and-eval_20260516T215608_result.json`
- **Structured JSON:** [`15cd54888722a0d8ec22.json`](../../sessions/15/15cd54888722a0d8ec22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## d_b Sweep 完整结果

| d_b | Final Loss | per_token PPL | teal_global PPL | Sparsity | Predictor Params |
|-----|:---:|:---:|:---:|:---:|:---:|
| 64  | 0.361 | 10.158 | **12.076** | 0.500 | ~38M |
| 128 | ~0.30 | 9.218 | **11.963** | 0.500 | ~76M |
| 256 | 0.270 | 8.586 | **12.105** | 0.500 | ~151M |
| 512 | 0.224 | 7.933 | **12.315** | 0.500 | ~302M |

---

## 状态报告

1. **训练完成情况**：三个 d_b (64/256/512) 均完成 1000/1000 steps
2. **冗余进程**：无（GPU 空闲，无重复进程）
3. **teal_global eval**：全部完成并保存到 `results/benchmark/db_sweep_{64,256,512}_teal/`

## 关键发现

**per_token PPL 随 d_b 单调递减**（更大 predictor → 更好 token 级预测），但 **teal_global PPL 不受益于更大 d_b**，反而轻微恶化：

- per_token: 10.16 → 9.22 → 8.59 → 7.93（d_b↑ → PPL↓）
- teal_global: 12.08 → **11.96** → 12.11 → 12.32（d_b=128 最优）

**解释**：teal_global 将 per-token predictions 在 calibration 样本上平均为静态 mask，抹杀了 token-level granularity。更大的 predictor 过度拟合 token 级模式，这些模式在 averaging 时相互抵消。

**结论**：d_b=128 是最优选择——在 static mask 场景下效果最好，同时保持合理的参数开销（76M/32层 = 2.37M/layer）。增大 predictor 的收益仅体现在 per-token dynamic 模式下。

---
