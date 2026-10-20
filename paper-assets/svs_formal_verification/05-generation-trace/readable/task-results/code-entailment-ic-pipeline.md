# code entailment ic pipeline

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_entailment_ic_pipeline_20260514T140435_result.json`
- **Structured JSON:** [`98c942bb20378a4f5199.json`](../../sessions/98/98c942bb20378a4f5199.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D012 完成。以下是总结：

---

### 1. 代码结构理解

| 文件 | 关键函数 |
|------|---------|
| `z3_checker.py` | `check_internal_consistency(claims, vocab, total_claims)` → `(is_sat, ic_score, mcs_size)` |
| `scoring.py` | `SVSScorer.select_answer(chains, chain_claims, vocab, z3_checker, cross_checker)` → `SVSResult` |
| `z3_sandbox.py` | `check_entailment(claim_fol_strs, vocab, premise_fols, conclusion_fol)` → `(entails, status)` |
| `run_mvp.py` | `run_pipeline(cfg)` — 加载数据→采样→分解→formalize→scorer→输出 |
| `loader.py` | `Problem.premises: list[str]` — ProofWriter context 按句拆分 |
| `autoformalize.py` | `formalize_batch(claims, vocab)` — 并行 LLM formalization |

### 2. 改动摘要（4 文件，+76 行）

- **`z3_checker.py`** (+41): 新增 `check_entailment(claims_fol, premises_fol, vocab)` — 逐 claim 调 sandbox 的 entailment check，累积 context
- **`types.py`** (+5): `ChainVerification` 新增 `ic_entail`, `entailment_details`, `claims_fol`, `premises_fol`, `claims_nl`
- **`scoring.py`** (+16): `select_answer()` 增加 `premises_fol` 参数，每条 chain 在 IC 后额外跑 entailment check，填充新字段
- **`run_mvp.py`** (+14): 在 vocab 提取后，用 `formalizer.formalize_batch()` formalize premises → `premises_fol`，传给 scorer

### 3. z3_sandbox 不需要扩展

sandbox 已有完整的 `check_entailment` worker + client：worker 构建 `solver.add(premises + prior_claims + ¬conclusion)`，检查 UNSAT=entails。新的 `Z3Checker.check_entailment()` 直接调它。

### 4. Premises 获取方式

`Problem.premises` 由 `loader.py` 从 ProofWriter 的 `theory`/`context` 字段按句号拆分得到。在 `run_mvp.py` 中构造 `AtomicClaim(chain_id=-1, ...)` 后调 `formalizer.formalize_batch()` 转为 FOL。

### 5. Dry-run 结果

测试用例：3 个 premises（`Green(cat)`, `Green→Big`, `Big→Round`），3 个 claims。

```
ic_entail=0.6667, entailed=2/3
  Big(cat)   -> entailed=True  (z3=entails)
  Round(cat) -> entailed=True  (z3=entails)  
  Cold(dog)  -> entailed=False (z3=not_entails)
```

输出 JSON 包含所有新字段：`ic_entail`, `entailment_details`, `claims_fol`, `premises_fol`, `claims_nl`。

### 6. Git commit

```
dcf5617 (feat/entailment-ic) feat: implement entailment-based IC (D012)
4ba8df3 (master) checkpoint: mvp_003 baseline code before D012 entailment modifications
```

PID 37622 (mvp_003) 仍在运行，未受影响。

---
