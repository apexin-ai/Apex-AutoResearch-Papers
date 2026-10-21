# diagnose full gpu status and harvest

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full-gpu-status-and-harvest_20260520T164923_result.json`
- **Structured JSON:** [`911bbab894e42990c6b5.json`](../../sessions/91/911bbab894e42990c6b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 状态:
- cuda:0: 92% util, 32.5/98GB — plan017_14b_rsft_generate_r4 — 225/474 pending (2782/3027 docs, 92%)
- cuda:1: 91% util, 18.9/98GB — eval_llama_sft_s43_no_evidence_r2 — 69/247 batches (28%), ETA ~1h
- cuda:2: 85% util, 18.9/98GB — eval_llama_sft_s44_no_evidence — 226/247 batches (91%), ETA ~12min
- cuda:3: 0% util, 空闲

已完成实验 metrics:
- eval_llama_rsft_s44_no_evidence: ign_f1=0.5550, f1=0.5674, edcr=0.6818, format_ok=984/985 (99.9%), truncated=178/985

Fair Comparison 结果 (RSFT s44):
                      ign_f1    P        R        pred     gold
  With-evidence(full): 0.5587   0.5574   0.5601   11781    12151
  No-evidence(full):   0.5550   0.5488   0.5614   11994    12151
  Fair tax:            -0.38pp  (fair subset: 984 docs)

  → 去掉 evidence 仅损失 0.38pp ign_f1，几乎无 evidence tax
  → no-evi recall 略高(+0.13pp) 但 precision 低(-0.86pp)，说明去掉 evidence 后模型倾向多预测

Rsync 状态:
- 主 autodl-tmp rsync: 仍在运行 (PID 5150)
- Qwen3-8B 4个 adapter rsync: 全部进行中 (PIDs 37381-37399)
  - bf16: 810M ✓ (adapter_model.safetensors 存在)
  - s43: 939M, s44: 939M, no_evidence: 939M

14B gen r4: 22256 lines ≈ 2782/3027 docs (92%), 剩余 ~245 docs, ETA ~1.2h
```

**待完成（预计按时间顺序）：**
1. ~12min: eval_llama_sft_s44_no_evidence 完成 → 可立即跑 SFT s44 fair comparison
2. ~1h: eval_llama_sft_s43_no_evidence_r2 完成 → 可跑 SFT s43 fair comparison
3. ~1.2h: 14B gen r4 完成 → 可开始 RSFT filtering + training

---
