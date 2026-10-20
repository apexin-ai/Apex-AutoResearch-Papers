# ssh status check

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_status-check_20260512T153523_result.json`
- **Structured JSON:** [`aad20a86363d3ea3b5fb.json`](../../sessions/aa/aad20a86363d3ea3b5fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果如下：

---

## 1. nvidia-smi

```
GPU 0: NVIDIA RTX PRO 6000 Black   56°C   P0   336W/600W   34198MiB / 97887MiB   100% 利用率
GPU 1: NVIDIA RTX PRO 6000 Black   53°C   P0   268W/600W   17101MiB / 97887MiB    71% 利用率
```

两块 GPU 都在工作，温度正常。

---

## 2. Python 进程列表

| PID | 启动时间 | CPU% | 命令 |
|-----|---------|------|------|
| **17369** | 23:02:07 | 100% | `python rerank_nli.py --model_path ./outputs/sft/merged --eval_file ./data/docred_dev.jsonl --nli_model_name .../nli-deberta-v3-large --output_file ./outputs/posthoc_nli/eval_results.json --output_dir ./outputs/posthoc_nli --no_use_flash_attention` |
| **17587** | 23:02:38 | 100% | `python evaluate.py --model_path ./outputs/sft/merged --eval_file ./data/docred_dev.jsonl --output_file ./outputs/sft/eval_results.json --no_use_flash_attention` |
| **17840** | 23:03:16 | 100% | `python evaluate.py` (同上，**重复实例**) |
| 10513 | 21:12:37 | 1.2% | `python -c "from huggingface_hub import snapshot_download..."` (HF 下载进程，疑似挂起) |
| 913 | 19:04:11 | 0% | jupyter-lab (系统服务) |
| 917 | 19:04:11 | 0% | tensorboard (系统服务) |

**注意：evaluate.py 有 2 个实例 (PID 17587 + 17840) 在跑，两个都在抢 GPU 0，可能互相争抢资源。**

---

## 3. PID 12569

**不存在（已清理）。**

---

## 4. eval_results.json (SFT)

**不存在。** evaluate.py 仍在运行中，尚未写出结果。

---

## 5. posthoc_nli 目录

**目录已创建，但为空（0 个文件）。** rerank_nli.py 仍在运行中，尚未写出结果。

---

## 6. sft_eval.log 最后 30 行

```
The tokenizer you are loading from './outputs/sft/merged' with an incorrect regex pattern...
`torch_dtype` is deprecated! Use `dtype` instead!
Loading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 172.67it/s]
The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k'].
```

模型已加载完成，正在推理阶段。日志内容较少说明刚启动不久。

---

## 7. outputs 目录 JSON 文件列表

```
outputs/sft/checkpoint-500/adapter_config.json          1.1KB   May 12 22:45
outputs/sft/checkpoint-500/tokenizer_config.json        5.4KB   May 12 22:45
outputs/sft/checkpoint-500/special_tokens_map.json      499B    May 12 22:45
outputs/sft/checkpoint-500/added_tokens.json            707B    May 12 22:45
outputs/sft/checkpoint-500/vocab.json                   2.7MB   May 12 22:45
outputs/sft/checkpoint-500/tokenizer.json               11MB    May 12 22:45
outputs/sft/checkpoint-500/trainer_state.json           15KB    May 12 22:45
outputs/sft/checkpoint-570/adapter_config.json          1.1KB   May 12 22:54
outputs/sft/checkpoint-570/tokenizer_config.json        5.4KB   May 12 22:54
outputs/sft/checkpoint-570/special_tokens_map.json      499B    May 12 22:54
outputs/sft/checkpoint-570/added_tokens.json            707B    May 12 22:54
outputs/sft/checkpoint-570/vocab.json                   2.7MB   May 12 22:54
outputs/sft/checkpoint-570/tokenizer.json               11MB    May 12 22:54
outputs/sft/checkpoint-570/trainer_state.json           18KB    May 12 22:54
outputs/sft/adapter/tokenizer_config.json               5.4KB   May 12 22:54
outputs/sft/adapter/special_tokens_map.json             499B    May 12 22:54
outputs/sft/adapter/added_tokens.json                   707B    May 12 22:54
outputs/sft/adapter/vocab.json                          2.7MB   May 12 22:54
outputs/sft/adapter/tokenizer.json                      11MB    May 12 22:54
outputs/sft/adapter/adapter_config.json                 1.1KB   May 12 22:54
outputs/sft/merged/config.json                          1.5KB   May 12 22:54
outputs/sft/merged/generation_config.json               188B    May 12 22:54
outputs/sft/merged/model.safetensors.index.json         33KB    May 12 22:55
outputs/sft/merged/tokenizer_config.json                5.4KB   May 12 22:55
outputs/sft/merged/special_tokens_map.json              499B    May 12 22:55
outputs/sft/merged/added_tokens.json                    707B    May 12 22:55
outputs/sft/merged/vocab.json                           2.7MB   May 12 22:55
outputs/sft/merged/tokenizer.json                       11MB    May 12 22:55
```

**无 eval_results.json**——两个评估任务均尚未完成。

---

## 关键发现

1. **evaluate.py 有重复实例**：PID 17587 和 17840 都在 GPU 0 上跑同一个 evaluate.py，会争抢显存和计算资源，建议 kill 其中一个。
2. **PID 10513 的 HF 下载进程**从 21:12 跑到现在（超过 2 小时），疑似挂起。
3. **PID 12569 已不存在。**
4. **两个评估任务都还在跑**，尚无输出文件。rerank_nli.py 在 GPU 1，evaluate.py 在 GPU 0（但有两个实例竞争）。

---
