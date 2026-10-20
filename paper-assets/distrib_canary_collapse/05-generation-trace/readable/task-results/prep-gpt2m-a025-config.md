# prep gpt2m a025 config

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_gpt2m-a025-config_20260515T120322_result.json`
- **Structured JSON:** [`7c788b79d34381467887.json`](../../sessions/7c/7c788b79d34381467887.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已读取两个实验的完整配置。`gen_wiki_gpt2m_a025_s42` 仍为 QUEUED，可直接使用。

基于 `gen_wiki_gpt2m_a100_s42_v2` 的命令模板，修改 `synthetic_ratio` 和 `output_dir`，完整提交配置如下：

---

**提交配置：gen_wiki_gpt2m_a025_s42**

```
exp_id: gen_wiki_gpt2m_a025_s42
gpu_ids: ["cuda:0"]
timeout_hours: 12
server: westd-19828
account: root

command:
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a025_s42"
```

与 v2 参考的差异：
| 参数 | v2 (α=1.0) | 本次 (α=0.25) |
|------|-----------|--------------|
| `--synthetic_ratio` | 1.0 | 0.25 |
| `--output_dir` | `results/gen_wiki_gpt2m_a100_s42` | `results/gen_wiki_gpt2m_a025_s42` |
| `mkdir -p` | `results/gen_wiki_gpt2m_a100_s42` | `results/gen_wiki_gpt2m_a025_s42` |

其余参数（model_name 本地路径、TRANSFORMERS_OFFLINE=1、conda 激活、batch_size=32、seed=42）完全一致。

**注意**：`gen_wiki_gpt2m_a100_s42_v2` 实际以 EXIT_CODE=1 失败（18 秒即退出）。如果根本原因未修复，本次提交可能遇到同样问题。建议提交前先确认 v2 的失败日志。

---
