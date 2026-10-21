# ssh 5090 full sweep and fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090_full_sweep_and_fill_20260521T141630_result.json`
- **Structured JSON:** [`ae1c429a1a73d3832ebd.json`](../../sessions/ae/ae1c429a1a73d3832ebd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 GPUs active — models loading on GPUs 1 and 2 (16GB loaded, still completing). Here's the full report:

---

## Phase 1: 实验状态

| exp_id | GPU | Status | Key Metrics |
|--------|-----|--------|-------------|
| exp_fewnerd_n16_s42_v2 | cuda:0 | **RUNNING (84%)** | ~40min 剩余, 505K/602K prompts |
| exp_conll_n16_s456 | cuda:1 (完成) | **DONE** | greedy=0.9072, oracle=0.9545, ρ_SJ_cond=0.451, PASS |
| exp_conll_mf4v2_s123_rerun | cuda:2 (完成) | **DONE** | greedy=0.9072, oracle=0.9526, ρ_SJ_cond=0.414, degen=60.3%, PASS |
| exp_conll_mf4v2_s456_rerun | cuda:3 (完成) | **DONE** | greedy=0.9068, oracle=0.9429, ρ_SJ_cond=0.454, degen=60.4%, PASS |
| scierc_mf4v2_seed42 | - (完成) | DONE | greedy=0.6651, oracle=0.7815, MARGINAL |
| scierc_mf4v2_seed123 | - (完成) | DONE | greedy=0.6633, oracle=0.7777, MARGINAL |
| scierc_mf4v2_seed456 | - (完成) | DONE | greedy=0.6631, oracle=0.7732, MARGINAL |
| scierc_n16_s456 | - (完成) | DONE | greedy=0.6639, oracle=0.8063, MARGINAL |
| exp_fewnerd_mf4v2_s42/s123 | - | **FAILED** | tokenizer vocab_file=None (进程早死, 无输出) |

## Phase 2: v4 重算 (α_crit = greedy_f1 / 2)

公式已修正: `acrit(pi_mv)` → `g_f1 / 2`

CoNLL s42 的 `samples.jsonl` 不在 autodl-5090 上（在 5090-c），已跳过。

| Dataset | Seed | greedy | mv_strict | mv_incl | oracle | Δ_SC strict | Δ_SC incl | δ(degen) | α_crit |
|---------|------|--------|-----------|---------|--------|-------------|-----------|----------|--------|
| CoNLL | 123 | 0.9119 | 0.9123 | 0.9151 | 0.9542 | +0.04pp | +0.32pp | 60.3% | **0.4560** |
| CoNLL | 456 | 0.9116 | 0.9121 | 0.9133 | 0.9502 | +0.04pp | +0.17pp | 60.4% | **0.4558** |

α_crit_eff (adjusted for degeneracy): s123=1.148, s456=1.153

## Phase 3: GPU 填满

| GPU | New Experiment | PID | Model | ETA |
|-----|---------------|-----|-------|-----|
| cuda:0 | exp_fewnerd_n16_s42_v2 (继续) | 32117 | qwen3-8b-fewnerd-exp021 | ~40min |
| cuda:1 | **exp_fewnerd_mf4v2_s42_v3** | 48809 | qwen3-8b-fewnerd-exp021 | ~3.5h |
| cuda:2 | **exp_fewnerd_mf4v2_s123_v3** | 48951 | qwen3-8b-fewnerd-exp021 | ~3.5h |
| cuda:3 | **exp_e2_pretrained_fewnerd_s456** | 47630 | Qwen2.5-7B-Instruct | ~5.6h |

4/4 GPUs active. FewNERD MF4v2 s42/s123 首次失败因 tokenizer 路径不含 nested dir，已用正确路径 `checkpoints/qwen3-8b-fewnerd-exp021-merged/qwen3-8b-fewnerd-exp021-merged` 重提交。

---
