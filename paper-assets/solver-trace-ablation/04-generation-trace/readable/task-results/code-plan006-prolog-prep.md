# code plan006 prolog prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-prolog-prep_20260514T023650_result.json`
- **Structured JSON:** [`8392a7bc1c48f6715c76.json`](../../sessions/83/8392a7bc1c48f6715c76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report 写完。核心结论：

**Prolog STA 代码管线已完整可用**（solver、reward、训练脚本集成、configs、5/5 测试通过）。

**两个 blocker**：
1. **Config data_path 指向不存在的文件** `proofwriter_prolog_500.jsonl`。修复：改指向 `train_500_seed42.jsonl`（5min，符合 C001）。训练时模型从自然语言生成 Prolog，不需要 ground-truth Prolog annotation。
2. **eval_sta.py 不支持 Prolog**（~80 行改动，1-2h）。训练不阻塞，eval 前必须修。

Report 已保存到 `artifacts/plan006_readiness.md`。

---
