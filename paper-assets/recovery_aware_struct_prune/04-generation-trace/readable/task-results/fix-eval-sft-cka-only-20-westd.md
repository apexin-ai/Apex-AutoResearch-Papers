# fix eval sft cka only 20 westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_sft_cka_only_20_westd_20260517T190740_result.json`
- **Structured JSON:** [`cf9d03a433080c15e1ce.json`](../../sessions/cf/cf9d03a433080c15e1ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型已加载到 GPU（24GB VRAM），正在加载 GSM8K 数据集。eval 正常运行。

完成：
1. 诊断问题：westd 上 model.safetensors 损坏（370MB/12.3GB）
2. 清理空间：删除损坏文件 + 一个已完成的 alpha ablation pruned checkpoint（`pruned_alpha_0.0`，eval JSON 已保存）
3. 从 westb SCP 完整模型（12.3GB）到 westd
4. 验证 tokenizer + 模型加载成功
5. 提交 `eval_sft_cka_only_20_n1319` 到 westd cuda:0，registry 已更新为 RUNNING

---
