# code dev set lp alignment gating

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dev_set_lp_alignment_gating_20260519T051829_result.json`
- **Structured JSON:** [`a9c5e85ed7d60f5e081a.json`](../../sessions/a9/a9c5e85ed7d60f5e081a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。**三个数据集的 dev set routing 与 test set routing 完全一致。**

## 结果汇总

| Dataset | Dev adj ρ | Dev routing | Test adj ρ | Test routing | 一致 | 推理时间 |
|---------|-----------|-------------|------------|--------------|------|---------|
| SciERC | 0.167 | greedy | 0.158 | greedy | YES | 160.1s |
| CoNLL | 0.065 | greedy | 0.166 | greedy | YES | 34.6s |
| FewNERD | 0.516 | LP | 0.468 | LP | YES | 46.1s |

**关键发现：**
- **三个数据集 routing decision 完全一致**（threshold=0.3）
- SciERC/CoNLL 在 dev set 和 test set 上都低于 0.3 → greedy
- FewNERD 在 dev set 和 test set 上都远高于 0.3 → LP selection
- Dev set probe 可以安全替代 test set probe，消除 test-set leakage
- 总推理时间: ~240s (SciERC 因 275 instances 较慢，CoNLL/FewNERD 各 50 instances 很快)

**输出文件：**
- `output/dev_set_lp_probe/dev_vs_test_routing.json` — 对比结果
- `output/dev_set_lp_probe/scierc_dev_samples.jsonl` — SciERC dev samples (275 instances)
- `output/dev_set_lp_probe/conll2003_dev_samples.jsonl` — CoNLL dev samples (50 instances)
- `output/dev_set_lp_probe/fewnerd_dev_samples.jsonl` — FewNERD dev samples (50 instances)

---
