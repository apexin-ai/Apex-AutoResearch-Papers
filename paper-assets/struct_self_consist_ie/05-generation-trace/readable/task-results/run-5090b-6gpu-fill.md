# run 5090b 6gpu fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_5090b_6gpu_fill_20260521T030850_result.json`
- **Structured JSON:** [`20c0e15899268ed87f64.json`](../../sessions/20/20c0e15899268ed87f64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个实验已启动并产出推理日志，registry 已更新。

**5090-b**（4 卡，tmux）:

| GPU | Exp ID | Dataset | T | Seed | 进度 |
|-----|--------|---------|---|------|------|
| cuda:0 | exp_fewnerd_t05_s456 | FewNERD | 0.5 | 456 | rendering prompts |
| cuda:1 | exp_fewnerd_t12_s456 | FewNERD | 1.2 | 456 | rendering prompts |
| cuda:2 | exp_scierc_t05_s123 | SciERC | 0.5 | 123 | 80% processed (3680/4408) |
| cuda:3 | exp_scierc_t12_s123 | SciERC | 1.2 | 123 | 78% processed (3456/4408) |

**5090-c**（2 卡，nohup）:

| GPU | Exp ID | Dataset | T | Seed | N | 进度 |
|-----|--------|---------|---|------|---|------|
| cuda:1 | exp_scierc_t08_s123 | SciERC | 0.8 | 123 | 8 | 5% processed |
| cuda:3 | exp_conll_n16_s42 | CoNLL | 1.0 | 42 | 16 | 8% processed (4416/55248) |

注意：
- FewNERD 模型实际名是 `qwen3-8b-fewnerd-exp021-merged`（非任务描述中的 `qwen3-8b-fewnerd-merged`）
- SciERC 模型是 `qwen3-8b-scierc-merged-v2`
- SciERC 只有 551 实例（×8 samples = 4408 prompts），所以 5090-b 上的两个 SciERC 实验即将完成
- CoNLL N=16 有 3453 实例 × 16 = 55248 prompts，预计耗时较长

---
