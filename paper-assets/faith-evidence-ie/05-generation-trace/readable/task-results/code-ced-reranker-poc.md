# code ced reranker poc

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ced_reranker_poc_20260515T093913_result.json`
- **Structured JSON:** [`7568ee06ff7b18a24fd5.json`](../../sessions/75/7568ee06ff7b18a24fd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完全成功。结果：

```
  Strategy               rel_f1   evi_f1     EDCR     prec   recall   ign_f1  preds
  Greedy baseline        0.4267   0.7500   0.6970   0.3137   0.6667   0.4267     51
  Random (N=8)           0.5600   0.7037   0.6042   0.5385   0.5833   0.5600     26
  CED reranker           0.5333   0.7077   0.7356   0.4444   0.6667   0.5333     41
  Oracle (upper)         0.9091   0.7368   0.0345   1.0000   0.8333   0.9091     25
  CED vs Greedy: Δrel_f1=+0.1067
  Oracle headroom: Δrel_f1=+0.4824
```

**报告：**

- **脚本路径**：`/root/autodl-tmp/freige/eval/ced_reranker.py`
- **功能验证**：2 docs dry-run 通过，全流程正常（sampled gen → greedy gen → CED scoring → eval → results.json + console summary）
- **已有 full run (PID 178055)**：旧版脚本在 GPU 0 上跑全部 985 docs，已完成 ~30%（294/985），预估 ~4h 后完成。旧版的 `generations.jsonl` 格式兼容新脚本，可直接 resume
- **速度估算**（单卡 RTX 5090）：
  - Sampled generation (N=8): ~20s/doc → 50 docs ≈ 17min，985 docs ≈ 5.5h
  - Greedy generation: ~6s/doc → 50 docs ≈ 5min
  - CED scoring: ~3s/doc → 50 docs ≈ 2.5min
  - **50 docs 总计 ≈ 25 min 单卡**
- **GPU 需求**：1 张卡足够（Qwen3-4B bf16 ≈ 8GB，deberta-base ≈ 0.5GB）。多卡可通过 `CUDA_VISIBLE_DEVICES` 隔离
- **NLI 模型**：使用已缓存的 `cross-encoder/nli-deberta-v3-base`（任务指定的 `deberta-v3-large-zeroshot-v2.0` 服务器上不存在）
- **注意**：greedy 生成时 transformers 会打 warning（`top_p, top_k` not valid for greedy），不影响结果

---
