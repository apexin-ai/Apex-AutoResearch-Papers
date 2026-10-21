# ssh 5090c cuda1 check n16 metrics

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090c_cuda1_check_n16_metrics_20260521T112745_result.json`
- **Structured JSON:** [`57b5e6c40349c35d01f7.json`](../../sessions/57/57b5e6c40349c35d01f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕。

### FewNERD N=16 seed=456 结果
```
greedy_f1:  0.7883
mv_f1:      ⚠️ 不在 report.json 中（未计算）
oracle_f1:  0.9058
Δ_SC:       +11.74 pp (oracle - greedy)
degen:      ⚠️ 不在 report.json 中（未计算）
κ_Fleiss:   0.4552
ρ(SJ, F1):  0.285 (full, n=32565)
ρ(FK, F1):  0.233 (full, n=32565)
samples:    37648 ✓
verdict:    FAIL (single subtask MVP)
```

注：`signal_report.json` 不存在，`report.json` 中没有 `mv_f1` 和 `degeneracy_rate` 字段。如果需要这两个指标，需要后处理计算。

### 5090-c cuda:1 状态
**不是孤儿进程，是活跃实验。**

```
PID=311995  VLLM::EngineCore  30136MiB  运行 4min
  └─ 父进程 PID=311697
     python -u code/run_mvp_pilot.py \
       --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged \
       --dataset fewnerd --subtask ner \
       --n_samples 16 --seed 123 \
       --output_dir output/fewnerd_n16_s123/
```

这是 **fewnerd_n16_s123**（seed=123）实验，正在运行中，不是被取消的 worker 残留。

---
