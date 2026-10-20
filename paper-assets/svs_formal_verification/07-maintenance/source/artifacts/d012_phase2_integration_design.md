# D012 Phase 2: Entailment Check 集成设计文档

## 核心发现：集成已基本完成

代码审查发现，claim-level entailment check **已经集成到主管线**。以下是完整的调用链路：

```
run_mvp.py
  → formalizer.formalize_batch(premise_claims)  # 前提形式化
  → scorer.select_answer(..., premises_fol=premises_fol)
    → z3_checker.check_entailment(claims_fol, premises_fol, vocab)
      → sandbox.check_entailment(context, vocab, premises, conclusion, timeout)
        → Z3 worker: premises ∧ prior_claims ∧ ¬claim → UNSAT = entailed
    → scorer.score_chain(ic_entail, fc_score)
      → ic_weight * ic_entail + fc_weight * fc_score
  → evaluate_and_judge() uses cv.ic_entail for P2 Cohen's d
```

## 各文件现状

### z3_sandbox.py (line 187-228)
`check_entailment` worker handler 已实现：
- 解析 premises、prior claims、conclusion
- `solver.add(premises + prior_claims + Not(conclusion))`
- UNSAT → entails, SAT → not_entails, unknown → not_entails

### z3_checker.py (line 149-190)
`Z3Checker.check_entailment()` 已实现：
- 逐 claim 顺序检查：`premises ∧ claim_0 ∧ ... ∧ claim_{i-1} ⊢ claim_i`
- 返回 `(ic_entail, entailed_count, total_checked, details)`
- `ic_entail = entailed / len(claims_fol)` （仅计 formalized claims）

### scoring.py
- `score_chain()`: 已用 `ic_entail`，不用旧 `ic_score`
- `select_answer()`: 已调用 `z3_checker.check_entailment()`
- 旧 `check_internal_consistency()` 仍被调用但结果仅存储，不参与评分

### run_mvp.py (line 117-126)
- 已对 premises 做 formalization
- 已传递 `premises_fol` 给 scorer

### evaluate_and_judge() (line 214+)
- P2 判定已用 `cv.ic_entail`（不是旧 ic_score）

### types.py
- `ChainVerification` 已有 `ic_entail`, `entailment_details`, `claims_fol`, `premises_fol` 字段

## v3 独立脚本 vs 主管线的差异

| 维度 | entailment_rescore_v3.py | 主管线 | 评估 |
|------|-------------------------|--------|------|
| ic_entail 分母 | `total_claims`（含未 formalize） | `len(formalized)` | 管线更干净：entailment quality 和 formalization coverage 分离 |
| fc_score | 无，合并在 ic_entail 里 | `formalized/total`，独立权重 | 管线设计更好 |
| ic_consist | 有：`premises ∧ claim → SAT` | 无 | 非必需——entailed 必然 consistent |
| scoring | 无（只计算指标） | `ic_weight * ic_entail + fc_weight * fc_score` | ✅ |
| CCLC | 无 | 跨链 SAT 检查 | ✅ |

## 剩余优化点（非阻塞）

### 1. 移除冗余 IC 计算（低优先级）
`scoring.py:select_answer()` 仍调用 `z3_checker.check_internal_consistency()`，结果 `ic_score/ic_sat/mcs_size` 存入 ChainVerification 但不参与评分。可移除以减少 Z3 调用，但保留有利于 ablation 对比（old IC vs entailment IC）。

**建议：Phase 1 实验完成后再决定是否移除。**

### 2. CCLC 仍用旧 SAT 逻辑
`cross_chain.py` 的 `check_cross_chain_compatibility()` 调用 `check_internal_consistency(merged, vocab)` 做跨链一致性检查。语义上这是对的——CCLC 检查的是"不同链的 claims 是否互相矛盾"，SAT check 是正确的方法。不需要改为 entailment。

### 3. 潜在的权重调优
当前 `ic_weight=0.5, fc_weight=0.5, cclc_lambda=0.3`。Phase 1 结果出来后可能需要根据 entailment rate 分布调整权重。

## 阻塞问题

**无。** 主管线代码已具备运行 entailment-based IC scoring 的全部功能。Phase 1 完成后可直接用 `run_mvp.py` 跑正式实验。

## 验证计划

Phase 1（PID 54002）完成后：
1. 对比 v3 独立脚本的 ic_entail 和主管线的 ic_entail 计算结果，确认一致性
2. 用 `run_mvp.py --config config_entailment.yaml` 跑完整 50 问题实验
3. 检查 P2 Cohen's d 是否为正（correct chains 的 ic_entail > incorrect chains）
