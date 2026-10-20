# ssh fewnerd freeform mv recompute and pt n16 fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewnerd_freeform_mv_recompute_and_pt_n16_fix_20260522T145749_result.json`
- **Structured JSON:** [`e4e8cda60a4d287a7d1c.json`](../../sessions/e4/e4e8cda60a4d287a7d1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both tasks complete.

---

## Task 1: FewNERD Freeform MV/LP/Degeneracy Results

```
FewNERD N=8 T=1.0 seed=42:
                    Constrained    Free-form     Δ
greedy_f1              0.7911       0.7913      +0.00 pp
mv_strict_f1           0.7585       0.7586      +0.00 pp
mv_Δ (pp)               -3.27        -3.26      +0.01 pp
lp_f1                  0.7918       0.7922      +0.00 pp
lp_Δ (pp)               +0.07        +0.09      +0.02 pp
degeneracy_rate          9.1%         9.1%       -0.0 pp
```

**Key finding**: Freeform and constrained are virtually identical on FewNERD. All deltas are <0.02pp. Degeneracy rate is the same 9.1%. This contrasts with CoNLL where freeform showed larger differences — FewNERD's fine-grained entity types apparently constrain the output space enough that removing schema constraints has no effect.

Gold-filtered instances: 32,565 / 37,648.

---

## Task 2: PT N=16 Crash Diagnosis

**Partial data**: 27,110 / 37,648 lines (72%) — confirmed.

**Root cause**: `sampling.py:675` — `f.write(json.dumps(inst, ensure_ascii=False))` with `open(path, "w", encoding="utf-8")`. vLLM occasionally produces token strings containing lone Unicode surrogates (`\ud800`–`\udfff`), which `ensure_ascii=False` passes through but UTF-8 encoding rejects.

**Fix applied**: Line 673 changed from:
```python
with open(path, "w", encoding="utf-8") as f:
```
to:
```python
with open(path, "w", encoding="utf-8", errors="replace") as f:
```

This replaces unencodable surrogates with `�` during write. Backup at `sampling.py.bak`.

**GPU availability**: cuda:0, cuda:1, cuda:2 all free (0 MiB). cuda:3 in use (29785 MiB, 83% util). Ready for rerun on any of GPUs 0–2 when you decide.

---
