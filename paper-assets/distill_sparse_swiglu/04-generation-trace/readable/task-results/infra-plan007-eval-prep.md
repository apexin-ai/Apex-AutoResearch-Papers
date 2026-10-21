# infra plan007 eval prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan007_eval_prep_20260515T221330_result.json`
- **Structured JSON:** [`becd7e445a8478bd53d4.json`](../../sessions/be/becd7e445a8478bd53d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇总结果：

---

## Plan_007 评估基础设施检查报告

### 1. 基础设施状态

| 项目 | 状态 |
|------|------|
| lm-eval-harness | ✅ v0.4.12 已安装 |
| eval_benchmark.py | ✅ 640 行，已集成 lm-eval + PPL |
| 目标 benchmarks | ✅ arc_challenge, winogrande, mmlu, gsm8k, humaneval 全部可用 |
| 数据集缓存 | ✅ ARC, WinoGrande, MMLU, GSM8K 均已缓存于 HF_HOME |
| GPU | ✅ 2× RTX PRO 6000 Blackwell 98GB；cuda:0 空闲，cuda:1 占用 54GB |

### 2. 已完成的评估

已有结果**仅 WikiText-2 PPL**（consolidated/results.json），无 C4 PPL，无 downstream benchmarks。lm-eval downstream 之前因 `HF_DATASETS_OFFLINE=1` 失败。

### 3. 需要修复的问题

| 问题 | 修复方案 | 代码量 |
|------|---------|--------|
| `eval_benchmark.py` 设置了 `HF_DATASETS_OFFLINE=1` 导致 lm-eval 无法加载 | 运行时传 `HF_DATASETS_OFFLINE=0 TRANSFORMERS_OFFLINE=0`，或删除 setdefault 那两行 | 1 行 |
| 缺少 multi-seed conditions | CONDITIONS 字典添加 kl_s123, kl_s456, bce_s123, bce_s456 | ~20 行 |
| 缺少 HumanEval | LM_EVAL_TASKS 加 `("humaneval", 0)` | 1 行 |
| C4 PPL 未运行 | 已支持，只需 `--tasks all` 且不 skip | 0 行 |

**总计新增/修改: ~25 行。Integration 方案已就绪**——`eval_benchmark.py` 的模式是正确的：加载 base model → patch MLP forward → 用 `HFLM(pretrained=patched_model)` 包装给 lm-eval → 评估 → unpatch。无需写自定义 model wrapper。

### 4. Checkpoints 可用性

| 条件 | 可用 seeds | Checkpoints |
|------|-----------|-------------|
| KL (v2) | s42, s123, s456 | ✅ 3 seeds（任务说 5-seed，但仅有 3） |
| BCE | s42, s123, s456 | ✅ 3 seeds |
| BCE+comp | s42 | ✅ |
| STE | s42 | ✅ |
| SPON | s42 | ✅ |
| TEAL/WINA/R-Sparse | N/A (training-free) | ✅ |
| Dense | N/A | ✅ |

**总计 13 个条件** × 6 benchmarks (WikiText-2 PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K) + HumanEval

### 5. GPU·h 估算

8B bf16 模型在 RTX PRO 6000 Blackwell 上：

| Benchmark | 估计时间/条件 | 13 条件总计 |
|-----------|-------------|-------------|
| WikiText-2 + C4 PPL | ~1 min | ~13 min |
| ARC-c (25-shot) | ~6 min | ~78 min |
| WinoGrande (5-shot) | ~4 min | ~52 min |
| MMLU (5-shot, 14k 题) | ~50 min | **~650 min** |
| GSM8K (5-shot) | ~12 min | ~156 min |
| HumanEval (0-shot) | ~8 min | ~104 min |
| **合计** | **~81 min** | **~1053 min ≈ 17.5 GPU·h** |

两块 GPU 并行 → **~9h 墙钟时间**。MMLU 占总量的 62%，是瓶颈。

### 6. 建议执行计划

**Phase 1** (~15 min): 全条件 × PPL only → 立刻拿到 PPL 表格
```
GPU0: --condition all --tasks ppl --gpu 0
```

**Phase 2** (~4h, 双 GPU 并行): 全条件 × ARC-c + WinoGrande + GSM8K + HumanEval
```
GPU0: 7 条件 (dense, kl×3, bce×3) --tasks arc_challenge,winogrande,gsm8k,humaneval --gpu 0
GPU1: 6 条件 (bce_comp, ste, spon, teal, wina, rsparse) --tasks ... --gpu 1
```

**Phase 3** (~5h, 双 GPU 并行): 全条件 × MMLU（最耗时）
```
GPU0: 7 条件 --tasks mmlu --gpu 0
GPU1: 6 条件 --tasks mmlu --gpu 1
```

**总墙钟时间: ~9-10h**，可在 DDL 前充裕完成。

---

下一步需要我修改 `eval_benchmark.py`（加 multi-seed conditions + HumanEval + 修复 offline 模式）并启动 Phase 1 吗？

---
