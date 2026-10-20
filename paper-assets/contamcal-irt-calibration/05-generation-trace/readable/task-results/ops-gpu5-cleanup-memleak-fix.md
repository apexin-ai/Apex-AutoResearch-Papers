# ops gpu5 cleanup memleak fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu5-cleanup-memleak-fix_20260516T054921_result.json`
- **Structured JSON:** [`bdfcd0fee72848667f4b.json`](../../sessions/bd/bdfcd0fee72848667f4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改已验证。汇总：

**GPU 5 状态**：
- PID 701549 (exp008, 0.5B-Instruct): 2766 MiB
- PID 707351 (exp002, 0.5B d005_s123): 1898 MiB
- 总计 4678 MiB / 24564 MiB — 0.5B 模型两进程合计应 < 3GB，确认有泄漏

**已修复 4 个文件**：

| 文件 | 修复内容 |
|------|---------|
| `exp002/signal_embedding.py:142` | FAISS search 后立即 `del index, train_embeddings, bench_embeddings` + gc + empty_cache |
| `exp002/signal_selfcritique.py:233` | return 前 `del model, tokenizer` + gc + empty_cache |
| `exp008/compute_signals_on_model.py:102,211` | `compute_all_signals` return 前清理 + benchmark 循环每轮清理 |
| `exp002/compute_signals.py:98` | signal 循环每轮清理 |

`signal_minkpp.py` 已有 `del target_model` / `del ref_model` + `empty_cache`，无需修改。

当前运行的进程不受影响（代码已在内存中），后续运行会自动释放中间变量显存。

---
