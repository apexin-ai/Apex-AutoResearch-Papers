# analysis attention decomposition and pertask r2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_attention_decomposition_and_pertask_r2_20260518T171404_result.json`
- **Structured JSON:** [`01ed9c5b3d0ad6497157.json`](../../sessions/01/01ed9c5b3d0ad6497157.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

B2 + B3 完成。结果总结：

### B2: Attention Decomposition

**Trained model L1 (5 samples averaged):**

| Group | Instruction | Vision | BOS sink |
|-------|------------|--------|----------|
| Instr-dominant 24 heads | **62.4%** | 18.8% | 18.8% |
| Control 8 heads | **44.9%** | 27.1% | 28.0% |
| Delta | **+17.5pp** | -8.3pp | -9.2pp |

**Training effect:** 训练前两组 instruction attention 几乎相同 (~11-12%)，训练后 instruction-dominant heads 的 instruction attention 增幅（+50.9pp）远大于 control heads（+32.6pp）。分类名副其实。

### B3: Per-task R² Distribution

- **5-demo baseline:** L1 mean=0.256, std=0.070, range=[0.186, 0.385]；L13 mean=0.524, std=0.113, range=[0.386, 0.734]
- **50-demo ablation (all24 vs baseline):** L1 all 10/10 tasks positive (mean +0.0586)，L8 8/10 positive，L13 only 5/10 positive
- **Task variability:** CV 约 0.17-0.28（取决于层），说明 R² 跨任务差异显著
- 最高 R² task: "turn on the stove"，最低: "open the middle drawer"

输出文件：
- `/root/autodl-tmp/vla-ssd/results/attention_decomposition.json`
- `/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json`

Registry: `attention_decomposition` -> DONE (success)

---
