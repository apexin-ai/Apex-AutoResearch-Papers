# diagnose full harvest and status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full-harvest-and-status_20260521T003933_result.json`
- **Structured JSON:** [`57ced5efd7dc3f320b44.json`](../../sessions/57/57ced5efd7dc3f320b44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。以下是完整状态报告：

---

## GPU 状态

| GPU | PID | 状态 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| cuda:0 | 53413 | 运行 3h48m | 32503 MiB | 83% |
| cuda:1 | 58417 | 运行 2h10m | 18879 MiB | 91% |
| cuda:2 | — | **空闲** | 0 MiB | 0% |
| cuda:3 | — | **空闲** | 0 MiB | 0% |

## 已完成实验

### plan017_14b_rsft_no_evidence_eval
- **ign_f1: 0.5432**
- f1: 0.5536
- format_ok: 953/985 (96.8%)
- truncated: 106/985
- predictions: 15333
- 结论: **success** — registry 已更新 DONE

### eval_llama_sft_s42_with_evidence_2048
- **ign_f1: 0.5649**
- f1: 0.5767
- evi_f1(DREEAM): 0.4510, evi_f1(TP): 0.8030, EDCR: 0.6428
- format_ok: 976/985 (99.1%)
- truncated: 147/985
- predictions: 20302
- 结论: **success** — registry 已更新 DONE

## LLaMA s42 with-evi 2048 Control 分析

| 指标 | @1024 | @2048 | delta |
|------|-------|-------|-------|
| ign_f1 | 0.5384 | **0.5649** | **+2.65pp** |
| f1 | — | 0.5767 | — |
| format_ok | — | 976/985 | — |
| truncated | — | 147/985 | — |

**假设被拒绝。** 预期 delta < 1pp，实际 +2.65pp。with-evidence 模型对 token budget **敏感**——1024 的截断也在伤害 with-evi 性能。这意味着 no-evi@2048 vs with-evi@1024 的 evidence tax 比较方法学有偏差，需要在 matched token budget (都用 2048) 下重新计算 evidence tax。

## 14B RSFT Evidence Tax（待完成）

with-evidence eval (PID 53413) 仍在 GPU 0 运行（3h48m），无法计算 fair evidence tax。no-evi 的 ign_f1=0.5432（对比 SFT baseline 0.5507 下降了 0.75pp，值得关注）。

## s43 2048 r2 进度

- 133/247 batches (54%)，elapsed ~2h10m
- 速率 ~50-65s/batch，预计剩余 ~1h45m
- GPU 1 正常使用中（18879 MiB, 91%）
- ⚠️ log 开头有 `timeout: failed to run command 'python': No such file or directory` 错误，但实际推理正在正常执行（可能是 tmux 残留输出）

## 空闲 GPU

- **cuda:2** — 可用
- **cuda:3** — 可用

---
