# analyze eval pi05 l2norm k085 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k085_spatial_seed42_20260522T012829_result.json`
- **Structured JSON:** [`f411a6cf534d0503c3e3.json`](../../sessions/f4/f411a6cf534d0503c3e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验失败。原因是网络不可达——加载 tokenizer `google/paligemma-3b-pt-224` 时 `huggingface_hub` 尝试联网调用 `model_info()`，但 AutoDL 网络代理未启用，导致 `httpx.ConnectError: [Errno 101] Network is unreachable`。

```
RESULT_SUMMARY:
overall_sr: N/A
total_successes: N/A
total_episodes: N/A
log_path: /root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k085_spatial_seed42.log
result_json_path: N/A（未生成）
status: failed
notes: 网络不可达导致 tokenizer 加载失败。transformers 的 GemmaTokenizer 内部调用 huggingface_hub.model_info() 检查是否为 Mistral 模型，该调用需要网络。AutoDL 实例未启用 network_turbo 代理，或代理已过期。修复方案：(1) 启动前 source /etc/network_turbo；(2) 或设置 HF_HUB_OFFLINE=1 / TRANSFORMERS_OFFLINE=1 跳过联网检查（前提是 tokenizer 文件已缓存在本地）。
```

GPU0 当前空闲（0%, 1 MiB），可以重跑。GPU2/3 有其他任务在运行。

---
