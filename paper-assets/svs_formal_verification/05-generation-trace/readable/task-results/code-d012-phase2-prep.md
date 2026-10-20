# code d012 phase2 prep

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d012_phase2_prep_20260514T153326_result.json`
- **Structured JSON:** [`fc861c99e1a190b4bc1c.json`](../../sessions/fc/fc861c99e1a190b4bc1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**Entailment check 已完整集成到主管线，无需额外代码修改。**

代码审查的完整调用链路：

```
run_mvp.py
  ├─ formalizer.formalize_batch(premises)       # 前提 → FOL
  └─ scorer.select_answer(premises_fol=...)
       ├─ z3_checker.check_entailment()          # 逐 claim: premises ∧ prior ∧ ¬claim → UNSAT?
       │    └─ sandbox.check_entailment()        # 子进程 Z3 执行
       ├─ score_chain(ic_entail, fc_score)       # 0.5*ic_entail + 0.5*fc_score
       └─ evaluate_and_judge() → cv.ic_entail    # P2 Cohen's d 判定
```

**与 v3 独立脚本的差异**（设计选择，非 bug）：
- v3 合并分母 `entailed/total_claims`；主管线分离为 `entailed/formalized` + `fc_score=formalized/total`，更干净
- v3 额外计算 `ic_consist`（per-claim 一致性）；主管线省略——entailed 必然 consistent
- 旧 `check_internal_consistency()` 仍被调用但结果不参与评分，保留用于 ablation

**无阻塞问题。** Phase 1（PID 54002）完成后可直接用 `run_mvp.py` 跑正式实验。

设计文档已写入 `artifacts/d012_phase2_integration_design.md`，memory.md 已更新。

---
