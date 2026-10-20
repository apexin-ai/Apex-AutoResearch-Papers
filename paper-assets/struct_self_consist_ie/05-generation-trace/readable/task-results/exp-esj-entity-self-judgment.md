# exp esj entity self judgment

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_esj_entity_self_judgment_20260520T160012_result.json`
- **Structured JSON:** [`553af5cd4f3acf1b9461.json`](../../sessions/55/553af5cd4f3acf1b9461.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：所有 4 块 GPU 被 Qwen2.5-32B FewNERD QLoRA 训练占用。**

- 进度：32800 / 41180 steps (79.65%)
- 预估剩余：~7h48m
- 是 4-GPU 分布式训练，无法释放单块 GPU

**需要注意的差异：**
- 任务说 "Qwen2.5-7B-Instruct FewNERD-FT merged checkpoint"，但服务器上没有该模型
- 实际可用的 FewNERD FT 模型是 **Qwen3-8B + qwen3-8b-fewnerd-5epoch-lora**（base 在 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`）
- 脚本已按实际情况适配：加载 base + LoRA → merge → forward pass

**ESJ 脚本已就绪**，上传到了 `/root/autodl-tmp/struct_self_consist_ie/code/run_esj.py`。

当 GPU 可用时，dry-run 命令：
```bash
CUDA_VISIBLE_DEVICES=1 python /root/autodl-tmp/struct_self_consist_ie/code/run_esj.py \
  --base_model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --adapter_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-5epoch-lora \
  --data_path /root/autodl-tmp/struct_self_consist_ie/output/exp_028_fewnerd_5epoch/samples.jsonl \
  --output_dir /root/autodl-tmp/struct_self_consist_ie/results/esj_fewnerd \
  --max_instances 100 --batch_size 16
```

等训练结束后提交全量？还是要我终止当前训练释放 GPU？

---
