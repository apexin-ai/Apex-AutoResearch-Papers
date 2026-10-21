# ops prompted gen verify

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prompted-gen-verify_20260518T034636_result.json`
- **Structured JSON:** [`436364e27cd71179961c.json`](../../sessions/43/436364e27cd71179961c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 核查结论

**69.5% 是真实的，存在于结果文件中。实验完整运行成功，未 crash。**

### 证据

**结果文件** — `/root/autodl-tmp/recursive_gen_depth_est/results/prompted_generation/summary.json`：
```json
{
  "four_class_accuracy": 0.6952,
  "accuracy_ci_95": [0.689, 0.7015],
  "fold_accuracies": [0.6885, 0.707, 0.6987, 0.6943, 0.6877],
  "baseline_bos_seeded_acc": 0.833,
  "delta_vs_baseline_pp": -13.78,
  "elapsed_hours": 5.14
}
```

**日志** — `/root/autodl-tmp/recursive_gen_depth_est/logs/prompted_gen_gpt2xl_001.log` 确认全部 3 个阶段完成：
- Phase 1: d0-d3 各生成 5000 samples（50 prompts × 100 samples）
- Phase 2: 20000 条特征提取完成
- Phase 3: 5-fold CV 完成，最终输出 `RESULT: 0.6952 [0.689, 0.7015]`

**数据完整** — `data/prompted_gen/` 含 depth_0~3.jsonl（各 ~11-13MB）、features.jsonl（13.7MB）、prompts.json；checkpoints 含 lora_depth_0/1/2。

### Registry "failed" vs ROADMAP "69.5%" 的矛盾

实验**技术上完全成功**（代码跑完、数据完整、结果写入）。Registry 标 "failed" 是**实验目标层面的判断**：prompted generation 的 4-class accuracy (69.5%) 相比 BOS-seeded baseline (83.3%) 下降了 13.8pp，说明 topic prompt 引入的分布变化削弱了 depth signal。

ROADMAP 的描述 "69.5% (signal attenuated but present)" 是准确的——信号存在但减弱。这不是 crash 或无效输出，而是一个有意义的负面结果（ecological validity 实验发现了 signal degradation）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "four_class_accuracy": 0.6952,
    "accuracy_ci_95": [
      0.689,
      0.7015
    ],
    "fold_accuracies": [
      0.6885,
      0.707,
      0.6987,
      0.6943,
      0.6877
    ],
    "baseline_bos_seeded_acc": 0.833,
    "delta_vs_baseline_pp": -13.78,
    "elapsed_hours": 5.14
  }
}
```

</details>

---
