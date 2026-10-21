# code d112 eval bf16 submit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d112_eval_bf16_submit_20260519T130122_result.json`
- **Structured JSON:** [`edf4dd7f4ab7c1600d43.json`](../../sessions/ed/edf4dd7f4ab7c1600d43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常运行：模型加载完成，SFT adapter 已合并，RSFT LoRA adapter 已加载，998 文档 / 12275 gold triples 准备就绪，推理已开始（0/247 batches）。

完成总结：

- **Symlinks 已创建**：`rsft_output_4b_sft_s44_bf16/adapter_config.json` → `checkpoint-567/adapter_config.json`
- **Eval 已提交**：`d112_rsft_s44_eval_bf16`，PID 693522，**cuda:2**（cuda:0 仍被训练进程占用 27GB，不满足 C001，改用 cuda:2）
- **Registry 已更新**：
  - `d112_rsft_s44_train_bf16` → DONE/success，checkpoint_path 已设置
  - `d112_rsft_s44_eval_bf16` → PREPARING，hypothesis 和 parent 已设置
- **Eval 预计 ~2h**（247 batches）

---
