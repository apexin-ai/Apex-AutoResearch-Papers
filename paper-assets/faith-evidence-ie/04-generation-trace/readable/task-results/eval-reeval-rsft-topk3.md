# eval reeval rsft topk3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_reeval_rsft_topk3_20260515T220115_result.json`
- **Structured JSON:** [`6c093a6f1620ca469b48.json`](../../sessions/6c/6c093a6f1620ca469b48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 `--gpu` 参数，使用 `device_map="auto"`，由 `CUDA_VISIBLE_DEVICES` 控制（submit_training_job 自动设置）。

**C001 约束阻止提交：GPU 3 显存占用 31134 MiB >> 2GB。** 所有 4 张卡都在跑任务，没有空闲卡。

GPU 3 上两个 eval 进程：
- PID 261622: `rsft_s44` eval，已跑 4h24m
- PID 262080: `dpo_ced_1ep_fixed` eval，已跑 2h55m

其他准备工作已完成：
- Checkpoint 确认：`/root/autodl-tmp/rsft_topk3_output/`（有 adapter_model.safetensors）
- 模块路径：`python -m freige.eval.inference`（不是 `freige/inference.py`）
- 完整命令已就绪，等 GPU 空闲即可提交

需要等 GPU 3 的两个 eval 跑完，或你决定 kill 其中一个/换卡。要怎么处理？

---
