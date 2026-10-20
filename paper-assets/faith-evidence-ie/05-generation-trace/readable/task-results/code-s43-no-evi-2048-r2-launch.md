# code s43 no evi 2048 r2 launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_s43-no-evi-2048-r2-launch_20260520T222855_result.json`
- **Structured JSON:** [`e10669e92600c5e3b6c8.json`](../../sessions/e1/e10669e92600c5e3b6c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**发现：s43 no-evidence 2048 eval 已在运行。**

PID 58422 已于 06:29:45 启动，cuda:1 占用 18870 MiB。无需重复提交。

与你要求的参数对比：

| 参数 | 你要求的 | PID 58422 实际 |
|------|---------|---------------|
| timeout | 21600s (6h) | 无 timeout（更好，不会超时） |
| output_dir | `_r2/` | 原目录 `eval_llama_sft_s43_no_evidence_2048/` |
| quantize | 默认 True (4-bit) | `--no-quantize` (FP16) |
| 模块路径 | `eval.inference` | `freige.eval.inference` |

**注意**：`--no-quantize` 是和之前 s42/s44 eval 的主要差异——之前用 4-bit，这次用 FP16。可能影响结果的可比性。

我的提交失败（conda 环境下 `python` 不在 PATH），且 `>` 重定向覆盖了 PID 58422 的 log 文件。eval 进程本身不受影响，完成后结果会写入 `metrics.json` 和 `predictions.json`。

参考 s42 耗时 ~3h28m（带 quantize），PID 58422 预计在 ~10:00 左右完成。

需要我注册 registry 吗？还是要 kill 58422 重新用 4-bit quantize 提交以保持和 s42/s44 一致？

---
