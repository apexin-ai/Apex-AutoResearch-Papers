# analysis v3 status check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v3_status_check_20260524T004015_result.json`
- **Structured JSON:** [`75230a3064ff75537bc2.json`](../../sessions/75/75230a3064ff75537bc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：**failed**

**失败原因**：`lm_eval` 加载 GSM8K 数据集时，HuggingFace Hub HTTP 客户端异常关闭。

```
RuntimeError: Cannot send a request, as the client has been closed.
```

调用链：`benchmark_eval.py:run_lm_eval_tasks` → `lm_eval.simple_evaluate` → `datasets.load_dataset("openai/gsm8k")` → `hf_hub_download` → httpx client 已关闭。

日志中也显示了第一次网络错误：
```
'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/main/README.md
Retrying in 1s [Retry 1/5].
```

**时间线**：
- 启动：2026-05-24 03:52:48 CST
- 失败：2026-05-24 03:54:30 CST（运行约 2 分钟）
- 模型加载成功（579 weights，~11秒），TEAL predictor mask 计算完成
- 在尝试从 HuggingFace 下载 GSM8K 数据集时因网络问题失败

**GPU 状态**：两块 GPU 空闲（0% utilization, 0 MiB used），无进程在跑。

**结果文件**：无。`results/` 下没有 `*s123*gsm8k*` 相关文件。

**根因**：服务器网络无法访问 huggingface.co。可能需要 `source /etc/network_turbo` 或预先缓存 GSM8K 数据集到本地。

---
