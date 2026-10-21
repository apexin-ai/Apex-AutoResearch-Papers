# gpu exp 059 cross qwen3 extractor

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-059-cross-qwen3-extractor_20260519T063728_result.json`
- **Structured JSON:** [`b3122a483c0bbefd96be.json`](../../sessions/b3/b3122a483c0bbefd96be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量运行正在进行中，API 调用正常。

**当前状态总结：**

| 项目 | 状态 |
|------|------|
| vLLM Qwen3-14B | 运行中，端口 8000，cuda:0 |
| 代码修改 | `APIBasedLLM` 添加 `extra_body` 支持；`cross_model_extract.py` 添加 `--qwen3-nothink` flag |
| Dry-run (n=3) | 通过：3 题全部正常，extraction + scoring pipeline OK |
| 全量运行 (n=204) | 已启动，tmux session `exp059_run`，预计 ~2.3h |
| 实验注册 | exp-059-cross-qwen3-extractor, status=RUNNING |
| exp-033 baseline | SICA=59.31%, SC=54.41%, n=204 |

**监控命令：**
- 进度: `grep -c "Cross-model:" /root/symb_invariant_consensus/logs/exp059_run.log`
- 尾部: `tail -5 /root/symb_invariant_consensus/logs/exp059_run.log`
- 完成标志: `grep "EXP059_FINISHED" /root/symb_invariant_consensus/logs/exp059_run.log`

实验完成后需要：读取 summary 中的 SC%, SICA%, Δ(pp)，与 exp-033 对比，更新 registry 为 DONE。

---
