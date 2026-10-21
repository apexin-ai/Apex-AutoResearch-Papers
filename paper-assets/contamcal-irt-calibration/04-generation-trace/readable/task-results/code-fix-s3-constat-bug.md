# code fix s3 constat bug

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-s3-constat-bug_20260515T232230_result.json`
- **Structured JSON:** [`629d12508efb30b67107.json`](../../sessions/62/629d12508efb30b67107.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

**根因**：`s3_constat.py` 用 `orig ∩ para` 交集作为 item 集合，但 paraphrase eval 只覆盖了部分 items（arc_challenge 697/1172, gsm8k 228/1319, mmlu 6596/14042），导致 s3 输出的向量长度远小于 s1/s2。

**修复**：改为以 original eval 的全部索引为基准。有 paraphrase 数据的 items 正常计算 accuracy gap；没有 paraphrase 数据的 items 输出 `score=0.0`（无 contamination 证据），metadata 中 `has_paraphrase=false` 标记。

**验证**：三个 benchmark dry-run 通过，item count 均与 s1/s2 一致（arc_challenge=1172, gsm8k=1319, mmlu=14042）。

**v7 状态**：PID 652247 在 GPU 2 上跑 d005_s123，当前 s4_selfcritique mmlu (7%)。v7 命令未传 `--original-eval-paths`/`--paraphrase-eval-paths`，s3 本就被跳过，不受影响，无需重启。

---
