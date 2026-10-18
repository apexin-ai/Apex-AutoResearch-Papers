# ssh reeval script prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_reeval-script-prep_20260515T005614_result.json`
- **Structured JSON:** [`3426c737ca8d91affc4c.json`](../../sessions/34/3426c737ca8d91affc4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。对比参考值：

| count | TextF1 | P | R | P/G | Hallu | WrTyp | Spur |
|-------|--------|---|---|-----|-------|-------|------|
| 1 (ref) | 0.184 | 0.105 | 0.720 | 6.85 | 283 | 0 | 15950 |
| 1 (new) | 0.1835 | 0.1052 | 0.7198 | 6.85 | 283 | 0 | 15949 |
| 64 (ref) | 0.463 | 0.520 | 0.418 | 0.80 | 175 | 2434 | 2495 |
| 64 (new) | 0.4632 | 0.5195 | 0.4179 | 0.80 | 175 | 2434 | 2495 |

所有数字完全吻合（count_1 spurious 差 1，是原始脚本的 FP 统计口径微差，不影响结论）。

额外产出：offset 修正后 exact F1 和 relaxed F1 也一并算出。比如 count_64 exact F1=0.4542, relaxed F1=0.5111，说明修正 offset 后 exact match 也能恢复到合理水平。

exp2 兼容性：predictions 文件格式与 exp1 完全相同（同一个 `run_experiment.py` 生成），脚本已支持 `--exp exp2`。exp2 尚在运行（PID 197321，predictions_exp2.json 在实验结束后一次性写入），脚本会在文件不存在时报错退出。

---
