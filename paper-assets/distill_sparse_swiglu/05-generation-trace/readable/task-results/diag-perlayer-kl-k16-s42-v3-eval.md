# diag perlayer kl k16 s42 v3 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_perlayer_kl_k16_s42_v3_eval_20260523T045110_result.json`
- **Structured JSON:** [`f5f9a08924ab20328e16.json`](../../sessions/f5/f5f9a08924ab20328e16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断报告

### 失败原因
**网络不可达导致 HuggingFace 数据集下载失败。**

```
'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/allenai/ai2_arc/resolve/main/README.md
RuntimeError: Cannot send a request, as the client has been closed.
```

lm-eval 在加载 `arc_challenge` 任务时尝试从 HuggingFace 下载数据集元数据。即使数据集已缓存在 `/root/autodl-tmp/.hf_cache/datasets/allenai___ai2_arc/`，lm-eval 仍然会先尝试 HEAD 请求检查更新。网络不通（可能未执行 `source /etc/network_turbo`）导致请求失败，重试 1 次后 httpx client 被关闭，抛出 RuntimeError。

### 已完成的 metrics
- **WikiText-2 PPL = 8.6737**（15.9s 内完成）
- 模型加载、mask 计算均正常（model-level sparsity = 0.297）

### 失败的 task
`arc_challenge`（lm-eval 的第一个任务，还没开始跑就挂了）

### K=4 对比
K=4 downstream eval 成功完成了全部 7 个任务，数据集已缓存。区别在于那次运行时网络是通的。

### 修复方案

**方案 A（推荐）：** 重跑时加 `HF_DATASETS_OFFLINE=1`，强制 lm-eval 只用本地缓存，不发网络请求：
```bash
HF_DATASETS_OFFLINE=1 WANDB_MODE=disabled python -u src/benchmark_eval.py --exp_id perlayer_kl_k16_s42_v3_eval --checkpoint checkpoints/perlayer_kl_k16_s42_v3/predictor_perlayer_kl_k4.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa --seq_len 2048 --gpu 0
```

**方案 B：** 运行前先 `source /etc/network_turbo` 开启代理。

**方案 C：** 只跑 lm-eval 部分（PPL 已拿到），跳过 wikitext2：
```bash
HF_DATASETS_OFFLINE=1 WANDB_MODE=disabled python -u src/benchmark_eval.py --exp_id perlayer_kl_k16_s42_v3_eval --checkpoint checkpoints/perlayer_kl_k16_s42_v3/predictor_perlayer_kl_k4.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa --seq_len 2048 --gpu 0
```

方案 A 最稳，因为所有数据集都已缓存（K=4 eval 时下载过了）。

---
