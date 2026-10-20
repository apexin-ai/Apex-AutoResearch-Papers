# audit conll oracle headroom p0

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_conll-oracle-headroom-p0_20260519T184346_result.json`
- **Structured JSON:** [`804956c1f2b4f8a5197d.json`](../../sessions/80/804956c1f2b4f8a5197d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是完整验证结果：

```
=== Qwen 8B FT CoNLL N=8 ===
(来源: exp002_conll2003 / exp_002_conll_n8_seed{123,456} report.json, 全集 3453 实例)

Seed 42:  greedy=0.9074  oracle=0.9468  headroom=3.94pp
Seed 123: greedy=0.9072  oracle=0.9524  headroom=4.53pp
Seed 456: greedy=0.9068  oracle=0.9434  headroom=3.66pp
3-seed mean: greedy=0.9071  oracle=0.9475  headroom=4.04pp

(来源: selection_f1_qwen_conll_n8.json, 过滤后 n=2756, 仅 seed 42)
Seed 42:  greedy=0.9079  oracle=0.9483  headroom=4.04pp

=== Qwen 8B FT CoNLL N=16 (对比用) ===
(来源: exp_002_conll_n16 / seed123 / seed456 report.json, 全集 3453)

Seed 42:  greedy=0.9075  oracle=0.9566  headroom=4.92pp
Seed 123: greedy=0.9068  oracle=0.9633  headroom=5.65pp
Seed 456: greedy=0.9074  oracle=0.9549  headroom=4.75pp
3-seed mean: greedy=0.9072  oracle=0.9583  headroom=5.11pp

=== Appendix cross_selection 表 Qwen/CoNLL (line 248) ===
论文写: Greedy=.908  Oracle=.957  → headroom=4.9pp
Matches raw data: NO

- Greedy=.908 正确（N=8 seed42 filtered: .9079 → 四舍五入 .908 ✓）
- Oracle=.957 错误！这是 N=16 seed 42 的值（.9566 → .957）
  N=8 正确值: seed42 filtered=.948, 3-seed full mean=.948
- 正确 headroom: .948 - .908 = 4.0pp（非 4.9pp）

=== LLaMA CoNLL N=8 ===
(来源: selection_f1_llama_conll_n8.json, n=2756)
greedy=0.9242  oracle=0.9426  headroom=1.84pp

论文写: Greedy=.924  Oracle=.943  → headroom=1.9pp
Matches raw data: YES ✓

(来源: exp_017_llama_conll_infer/report.json, N=8, 全集 3453)
greedy=0.9266  oracle=0.9443  headroom=1.77pp

=== LLaMA CoNLL N=16 (对比用) ===
(来源: exp_017_llama_conll_n16 / s123 / s456 report.json)
Seed 42:  greedy=0.9267  oracle=0.9487  headroom=2.20pp
Seed 123: greedy=0.9266  oracle=0.9497  headroom=2.31pp
Seed 456: greedy=0.9267  oracle=0.9488  headroom=2.21pp
3-seed mean: greedy=0.9267  oracle=0.9491  headroom=2.24pp

=== tab:scale_comparison (主论文, 可能是 Table 5) ===
论文写: CoNLL 8B FT  Greedy=.908  Hdr.≈5pp
这个 ≈5pp 大概率来自 .957-.908=4.9pp，同样基于错误的 N=16 oracle。
正确值: ≈4pp（.948-.908=4.0pp）

=== 结论 ===
1. 确认 BUG: appendix cross_selection 表 Qwen/CoNLL N=8 行的 Oracle=.957
   实为 N=16 seed42 值（.9566→.957），非 N=8。
   N=8 正确 Oracle ≈ .948（seed42 filtered）或 .948（3-seed full mean）。

2. 正确 headroom:
   - Qwen/CoNLL N=8: ~4.0pp（非论文中的 4.9pp）
   - LLaMA/CoNLL N=8: ~1.8pp（论文中 1.9pp 正确）

3. tab:scale_comparison 的 CoNLL Hdr.≈5 也可能受此影响，
   正确值约 ≈4pp。

4. 论文其他位置引用 "CoNLL's low oracle headroom (5.0~pp at N=8)"
   （appendix line 932）同样需要修正为 ~4.0pp。

5. Reviewer 怀疑 "Tab5 误用 LLaMA 数据" 不成立——
   Tab5 的 .908 greedy 和 ≈5pp headroom 确实是 Qwen 数据，
   但 oracle 误用了 N=16 而非 N=8。LLaMA CoNLL 的 headroom 仅 1.8pp，
   并未被混入主表。
```

---
