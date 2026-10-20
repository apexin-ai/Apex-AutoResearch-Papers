# infra prep exp017 dryrun

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_prep_exp017_dryrun_20260513T020807_result.json`
- **Structured JSON:** [`2d50ca613cdd7bd4d176.json`](../../sessions/2d/2d50ca613cdd7bd4d176.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕，汇总结果：

## 检查结果

| 检查项 | 状态 | 详情 |
|--------|------|------|
| 模型路径 | ✅ | `model.safetensors` (2.9G) + tokenizer + config 完整 |
| run_pipeline.py | ✅ | 存在，支持 `continuation` mode（L181, L630-631） |
| data_exp017_qwen_cont/ | ✅ 无冲突 | 目录不存在，pipeline 会自动创建 |
| results_exp017_qwen_cont/ | ✅ 无冲突 | 目录不存在，pipeline 会自动创建 |
| Python 环境 | ✅ | torch=2.10.0+cu128, transformers=4.57.6, CUDA=True, 1 GPU |

**所有前置条件满足。** 提交命令：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation"
```

exp-002 完成后可直接用此命令通过 `ssh_execute` 提交。

---
