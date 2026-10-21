# docs onset rate update d167

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_docs_onset-rate-update-d167_20260527T112543_result.json`
- **Structured JSON:** [`10218d283d74ea1cd6e8.json`](../../sessions/10/10218d283d74ea1cd6e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。变更汇总：

**paper_framing.md** (8 处修改):
- C2 header: Walker 3/3→2/3, 6/7→5/7, Fisher p<0.0001→p<0.001
- Walker onset 列表: 3/3→2/3, exp_009b 从 onset seed 改为 "sub-threshold perturbation under τ=2.0"
- 阈值行: 删除旧 "4/4 perfect classification", onset rate 86%→71%, 标注 009b sub-threshold
- 证据表: D032 行重标为 "sub-threshold perturbation", 2.05x@25K 标注 "pre-35K false positive"
- 阈值分离力行: 2/2→1/2, 删除 "4/4 perfect classification"
- Strength 段: Walker 3/3→2/3, 6/7→5/7, Fisher p→<0.001, 86%→71%
- Story Arc: Walker 3/3→2/3
- R6 + Experiment Coverage: 同步更新所有数字

**ROADMAP.md** (1 处):
- C2 里程碑: 6/7(86%) p<0.0001 → 5/7(71%) p<0.001, 标注 D167

---
