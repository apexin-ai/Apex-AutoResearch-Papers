# verify stale running experiments

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_stale_running_experiments_20260521T151254_result.json`
- **Structured JSON:** [`4197e2b9d3d2501435eb.json`](../../sessions/41/4197e2b9d3d2501435eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个实验已完成，PID 均已终止。汇总如下：

---

```
exp_id: eval_llama_rsft_s42_no_evi_2048
pid_alive: false
has_results: true
metrics:
  ign_f1: 0.5559
  f1: 0.5703
  truncated: 140/985
  format_ok: 984/985
  n_docs: 985
  no_evidence: true
  inference_time: 15710s (4h22m)
log_tail: EXIT_CODE=0
conclusion: success
```

```
exp_id: d140_4b_sft_s42_with_evi_2048
pid_alive: false
has_results: true
metrics:
  ign_f1: 0.3946
  f1: 0.4033
  evi_f1(DREEAM): 0.3129
  evi_f1(TP): 0.7906
  truncated: 243/985
  format_ok: 983/985
  n_docs: 985
  no_evidence: false
  inference_time: 8887s (2h28m)
log_tail: EXIT_CODE=129
conclusion: success (EXIT_CODE=129 = SIGHUP, 但 metrics 和 predictions 均已写入完成)
```

```
exp_id: d140_8b_sft_s42_no_evi_2048_fix
pid_alive: false
has_results: true
metrics:
  ign_f1: 0.5019
  f1: 0.5227
  truncated: 260/985
  format_ok: 985/985
  n_docs: 985
  no_evidence: true
  inference_time: 10900s (3h02m)
log_tail: EXIT_CODE=0
conclusion: success
```

```
exp_id: d140_1_7b_sft_s42_no_evi_2048_fix
pid_alive: false
has_results: true
metrics:
  ign_f1: 0.4233
  f1: 0.4436
  truncated: 507/985
  format_ok: 971/985
  n_docs: 985
  no_evidence: true
  inference_time: 7438s (2h04m)
log_tail: EXIT_CODE=0
conclusion: success
```

```
exp_id: d140_4b_sft_s42_no_evi_2048_fix
pid_alive: false
has_results: true
metrics:
  ign_f1: 0.4016
  f1: 0.4095
  truncated: 178/985
  format_ok: 983/985
  n_docs: 985
  no_evidence: true
  inference_time: 7606s (2h07m)
log_tail: EXIT_CODE=0
conclusion: success
```

---

**汇总排名（按 Ign-F1）：**

| # | 实验 | 模型 | Evidence | Ign-F1 | F1 | Truncated | Format OK |
|---|------|------|----------|--------|-----|-----------|-----------|
| 1 | eval_llama_rsft_s42_no_evi_2048 | Llama-3.1-8B (RSFT) | no | **0.5559** | 0.5703 | 140 | 984/985 |
| 2 | d140_8b_sft_s42_no_evi_2048_fix | Qwen3-8B (SFT) | no | **0.5019** | 0.5227 | 260 | 985/985 |
| 3 | d140_1_7b_sft_s42_no_evi_2048_fix | Qwen3-1.7B (SFT) | no | **0.4233** | 0.4436 | 507 | 971/985 |
| 4 | d140_4b_sft_s42_no_evi_2048_fix | Qwen3-4B (SFT) | no | **0.4016** | 0.4095 | 178 | 983/985 |
| 5 | d140_4b_sft_s42_with_evi_2048 | Qwen3-4B (SFT) | yes | **0.3946** | 0.4033 | 243 | 983/985 |

所有 5 个实验均已正常完成，registry 可标记为 COMPLETED。注意 1.7B 模型 truncated 率极高（507/985=51.5%），说明 2048 max_new_tokens 对该模型严重不足。

---
