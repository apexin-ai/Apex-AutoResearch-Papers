# code exp24 calibration ece

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp24-calibration-ece_20260520T141925_result.json`
- **Structured JSON:** [`753c36678aff7752114b.json`](../../sessions/75/753c36678aff7752114b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp24 完成。结果：

| Variant | IID ECE | DD OOD ECE | AA OOD ECE |
|---------|---------|------------|------------|
| 9class  | ≈0.000  | 0.143±0.053 | 0.116±0.053 |
| vanilla | 0.009±0.007 | 0.669±0.004 | 0.504±0.066 |

9-class 在所有数据集上校准都显著优于 vanilla。OOD 场景差异尤其明显——vanilla 的 DD OOD ECE 高达 0.67（jailbreak 样本被高置信度误判为 benign），而 9-class 仅 0.14。

产出：
- `results/exp24_calibration_ece.json`（含 per-bin reliability diagram 数据）
- artifact 已注册，registry 已更新为 DONE

---
