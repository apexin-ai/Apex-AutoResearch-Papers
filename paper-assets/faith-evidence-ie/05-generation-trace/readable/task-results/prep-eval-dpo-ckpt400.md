# prep eval dpo ckpt400

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_eval_dpo_ckpt400_20260515T203353_result.json`
- **Structured JSON:** [`d8dfbd03762fe2d2029b.json`](../../sessions/d8/d8dfbd03762fe2d2029b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**Checkpoint-400**: 完整。`adapter_model.safetensors` 528MB，tokenizer、adapter_config 等全部存在。

**Plan_008 进度**: 1371/1509 步 (91%)，剩余 138 步，约 ~4.3s/step，预计 **~10 分钟完成**。cuda:3 占用 20093/32607 MiB。

**GPU 状态**: 4 卡全部占用：
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 15557/32607 MiB | 87% |
| 1 | 18793/32607 MiB | 86% |
| 2 | 16469/32607 MiB | 91% |
| 3 | 20093/32607 MiB | 85% |

**残留清理**: `eval_results/dpo_ced_ckpt400/` 目录为空或不存在，无需清理。

**Eval 命令就绪**，但有一个问题：命令未指定 `CUDA_VISIBLE_DEVICES`，之前 OOM 就是因为抢到了已被占用的 GPU。建议加上 `CUDA_VISIBLE_DEVICES=3`，等 plan_008 跑完（~10 分钟后）再提交：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output/checkpoint-400 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_ckpt400 --no-quantize"
```

等你确认 plan_008 完成后我再提交执行。

---
