# benchmark inference speedup plan016

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_benchmark_inference_speedup_plan016_20260516T203051_result.json`
- **Structured JSON:** [`f62c3afc0b1bc8e14f03.json`](../../sessions/f6/f62c3afc0b1bc8e14f03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态汇总：**

- 脚本已就绪：`/root/recovery_aware_struct_prune/src/benchmark_inference.py`
- `datasets` 已安装
- 模型路径确认：
  - Dense: `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`（同架构 Qwen2, full-width intermediate_size=18944）
  - RASP 20%: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20`（per_layer_intermediate_size 非均匀）
  - Standard 20%: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20`（per_layer_intermediate_size 非均匀）

**阻塞**：cuda:1 被 GRPO 训练 (`grpo_rasp_rlvr_20`) 占用，进度 17/100，预计还需 ~9.5 小时（~7min/step × 83 steps）。westd-11672 全部 4 GPU 也都在跑任务。

**执行命令（GPU 空闲后）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && \
CUDA_VISIBLE_DEVICES=1 python src/benchmark_inference.py \
  --dense_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --rasp_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 \
  --standard_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 \
  --n_prompts 50 --max_new_tokens 512
```

**选项：**
1. 等 GRPO 训练完成后自动启动（我可以写一个等待脚本 nohup 挂后台）
2. 杀掉 GRPO 训练 (pid 635524) 立即腾出 cuda:1
3. 暂不执行，等你手动触发

怎么做？

---
