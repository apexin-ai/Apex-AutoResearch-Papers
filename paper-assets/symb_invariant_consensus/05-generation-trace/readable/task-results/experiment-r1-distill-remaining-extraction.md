# experiment r1 distill remaining extraction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r1-distill-remaining-extraction_20260521T155008_result.json`
- **Structured JSON:** [`f489be19d50369cb767d.json`](../../sessions/f4/f489be19d50369cb767d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型目录缺少实际权重文件（只有 config/tokenizer，没有 safetensors shards）。

**汇报当前状态——与预期严重不符：**

1. **R1-Distill vLLM**: 已无运行进程，所有 4 GPU 占用 0 MiB，无需 kill
2. **R1-Distill 模型权重不完整**: `/root/autodl-tmp/models/DeepSeek-R1-Distill-Llama-8B/` 只有 config.json、tokenizer 等元数据，**缺少所有 .safetensors 权重文件**。之前的 vLLM 启动因此失败（`Cannot find any model weights`）
3. **R1-Distill 中间结果不存在**: `/root/symb_invariant_consensus/results/exp_r1_distill_8b_sica/` 目录**完全不存在**——没有 intermediates，没有 per_trace_constraints_v2。registry 显示此实验标记为 `failed`（"process dead 5× with no sentinel"）
4. **已有的 93 题 cross-extraction 指标**只记录在 registry.yaml 中（metrics 条目），实际文件数据已丢失

**结论**：无法直接"补提取 111 题"——R1-Distill SC traces 数据不存在。要完成这个实验需要：
1. 重新下载 R1-Distill 模型权重（~16GB）
2. 部署 R1-Distill vLLM，跑 204 题 SC traces 生成
3. 再部署 Mistral 做 cross-extraction

这比预期的工作量大得多。请确认是否继续，或者有其他优先级更高的任务？

另外注意：任务 Step 1 写的是 "SSH westd-16639"，但项目绑定服务器是 **westd-25068**。如果数据可能在 westd-16639 上，我可以去那边查。

---
