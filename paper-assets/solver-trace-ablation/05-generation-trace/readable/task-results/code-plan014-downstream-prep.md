# code plan014 downstream prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan014-downstream-prep_20260514T031904_result.json`
- **Structured JSON:** [`5e9e5ded49668bb30cad.json`](../../sessions/5e/5e9e5ded49668bb30cad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Prover9 已安装。所有依赖就绪（除 CVC5）。

**总结：`eval_downstream.py` 和 `eval_cross_solver.py` 已存在且功能完整。**

两个脚本覆盖 plan014 的两个验证维度：

### Validation A: NLI accuracy (`eval_downstream.py`, 562行)
- 加载 checkpoint → 每个 sample 生成 K 个 FOL formalization
- 3-way NLI 分类 (true/false/unknown)，对比 gold label
- 全量 STA ISR 计算
- 按 ISR 分桶 (high/mid/low) 和四分位统计 accuracy
- Spearman ρ(ISR, correct) + Mann-Whitney U (Q4 vs Q1)
- Best-of-N 策略对比 (Oracle / ISR-best / Random / Prove-first)
- Bootstrap 95% CI

### Validation B: Cross-solver agreement (`eval_cross_solver.py`, 156行)
- 读取 eval_downstream.py 输出
- Z3 重新验证每个 formalization
- 统计 Prover9 ↔ Z3 agreement rate，按 ISR 分桶报告

### 依赖状态
| 依赖 | 状态 |
|------|------|
| Prover9 | ✅ /usr/local/bin/prover9 (2009-11A) |
| Z3 | ✅ 4.16.0 |
| scipy | ✅ 1.17.1 |
| CVC5 | ❌ 未安装（Z3 已足够覆盖 cross-solver 需求）|

### 运行方式
```bash
# Step 1: NLI validation (需要 GPU，约 30-60min for 100 samples × 8 generations)
python scripts/eval_downstream.py \
  --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42/checkpoint-xxx \
  --data_path data/test_held_out.jsonl \
  --output_path results/plan014_downstream.json \
  --num_generations 8 --workers 4

# Step 2: Cross-solver agreement (纯 CPU，约 5-10min)
python scripts/eval_cross_solver.py \
  --input_path results/plan014_downstream.json \
  --output_path results/plan014_cross_solver.json \
  --workers 4
```

### 预估运行时间
- eval_downstream.py: GPU 推理 ~20min (100 samples × 8 gens) + CPU solver ~10min → **~30min**
- eval_cross_solver.py: **~5min** (纯 CPU，Z3 通常比 Prover9 快)

### Kill criterion
Spearman ρ(ISR, downstream_accuracy) 在 `summary.statistical_tests.spearman.rho` 字段。ρ < 0.1 → ISR 不成立。

**代码就绪，无需额外编写。** 唯一缺失的是 CVC5（可选），Z3 已覆盖 cross-solver 验证需求。

---
