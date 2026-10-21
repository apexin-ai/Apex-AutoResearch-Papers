# ops fix 19828 14b model

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-19828-14b-model_20260522T070352_result.json`
- **Structured JSON:** [`090485e2fca7791cc76b.json`](../../sessions/09/090485e2fca7791cc76b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地路径完全可用。GPTNeoXForCausalLM, 1415M 参数。

**汇报**：

| 项目 | 结果 |
|------|------|
| **失败原因** | HF 缓存 `models--EleutherAI--pythia-1.4b-deduped` 条目损坏（只有 `.no_exist` marker + `refs/main`，无实际模型文件）。`from_pretrained` 在线下载尝试失败（AutoDL 网络代理不稳定），导致 `OSError: model-00001-of-00002.safetensors not found` |
| **模型下载** | 通过 ModelScope CDN 成功下载到 `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped/`（~14 min，含 safetensors + pytorch_model.bin 共 ~8GB）|
| **离线验证** | `from_pretrained('/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped')` 离线加载成功：1415M params, GPTNeoXForCausalLM |
| **HF 缓存兼容** | symlink hack 不起作用——HF hub 缓存需要 blob-based 结构。**重启实验时需用 `--model_name /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped`** 代替 `EleutherAI/pythia-1.4b-deduped` |
| **磁盘** | 19828 数据盘 250G，用 106G→~114G（下载后），剩余 ~136G，可用于 1.4B 实验 |

**重启命令需修改**：`--model_name` 从 `EleutherAI/pythia-1.4b-deduped` 改为 `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped`。

---
