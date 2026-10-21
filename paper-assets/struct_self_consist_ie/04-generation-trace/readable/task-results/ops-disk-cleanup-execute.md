# ops disk cleanup execute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_execute_20260516T111546_result.json`
- **Structured JSON:** [`c310a589bb8422b74337.json`](../../sessions/c3/c310a589bb8422b74337.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Part 1: 磁盘清理

已删除 3 个目录：
- `checkpoints/qwen3-8b-scierc-merged/` (16GB)
- `checkpoints/qwen3-8b-scierc-merged-v2-ckpt400/` (16GB)
- `checkpoints/qwen3-8b-scierc-lora/` (1.7GB)

**释放 ~32GB**，磁盘从 91% (24G free) 降至 78% (56G free)。

### Part 2: 4B checkpoint 依赖验证

**结论：`qwen3-4b-conll2003-merged-ckpt4200` 不可安全删除。**

证据：
1. 存在两个 4B merged model：`qwen3-4b-conll2003-merged`（来自 ckpt-3800）和 `qwen3-4b-conll2003-merged-ckpt4200`（来自 ckpt-4200）
2. `exp_qwen3_4b_conll_scs_inference` (v1) 和 v2 的 greedy_f1 不同（0.9251 vs 0.9234），确认使用了不同模型
3. v2 实验被论文分析脚本广泛引用（`analyze_q4q5.py`, `selection_f1_4b.py`, `r8w3_sj_union_v2.py` 等）
4. `merge_4b_ckpt4200.py` 专门为生成该模型而编写，命名对应关系明确：v2 实验使用的是 ckpt4200 merged model

**备注**：即使误删，可从 `checkpoints/qwen3-4b-conll2003-lora/checkpoint-4200` 重新 merge 恢复（LoRA adapter 仍在）。但无需冒险，保留即可。

---
