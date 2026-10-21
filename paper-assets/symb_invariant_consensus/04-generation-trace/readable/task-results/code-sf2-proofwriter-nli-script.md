# code sf2 proofwriter nli script

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sf2-proofwriter-nli-script_20260520T134627_result.json`
- **Structured JSON:** [`f53d0a4e6d393d06a9b1.json`](../../sessions/f5/f53d0a4e6d393d06a9b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。结果摘要：

**Dry-run 输出 (3题)**：
- DeBERTa standalone: 66.67% (2/3)
- SC baseline: 33.33% (1/3)
- NLI label mapping: ENTAILMENT→True, CONTRADICTION→False, NEUTRAL→Unknown
- 推理时间: 0.8s/3题
- 所有模块（complementarity、combo、McNemar、SICA agreement、JSON 保存）均正常运行

**完整运行预估**：
- 3题用时 0.8s（含模型加载），纯推理约 0.25s/题
- 600题估计：模型加载 ~5s + 推理 ~150s = **约 2.5-3 分钟** (CPU)
- 如果有 GPU 可用会更快（<1 min）

**修复记录**：`scipy.stats.binom_test` 在新版 scipy 中已更名为 `binomtest`，已修复。

脚本位置：`/root/symb_invariant_consensus/direction_r_deberta_proofwriter.py`，完整运行命令：
```bash
cd /root/symb_invariant_consensus && python3 direction_r_deberta_proofwriter.py
```

---
