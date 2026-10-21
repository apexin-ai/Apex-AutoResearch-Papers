# code vota loop only prep and train

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_vota_loop_only_prep_and_train_20260515T075656_result.json`
- **Structured JSON:** [`f60b276f76e50dc4e54f.json`](../../sessions/f6/f60b276f76e50dc4e54f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正在加载模型，启动正常。

### 结果

| 项目 | 状态 |
|------|------|
| **数据** | 就绪。train=4720, test=1190, `input`/`output` 格式（与 exception_only 一致） |
| **cuda:0** | 空闲，训练已成功提交 |
| **训练** | PID 82362，模型加载中，带 `--gradient_checkpointing` |
| **Registry** | `vota_loop_only_seed42` 已注册，关联 plan_003 |
| **预计时长** | 参照 exception_only 同规模数据，约 2-3 小时训练 + eval |

训练完成后会自动运行 `eval/evaluate.py`。

---
