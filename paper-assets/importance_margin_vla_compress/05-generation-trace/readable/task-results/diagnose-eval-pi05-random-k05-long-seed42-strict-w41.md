# diagnose eval pi05 random k05 long seed42 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k05_long_seed42_strict_w41_20260527T091256_result.json`
- **Structured JSON:** [`ffb1b01bdf4b05bb39c5.json`](../../sessions/ff/ffb1b01bdf4b05bb39c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程检查被限制了，不过从日志和 GPU 状态已经能得出完整结论。

## 诊断结果

### 失败根因：网络不可达

实验在模型加载完成后、构建预处理器时崩溃。`AutoTokenizer.from_pretrained("google/paligemma-3b-pt-224")` 试图从 HuggingFace Hub 下载 tokenizer，但网络不通。

### 关键错误信息

```
httpcore.ConnectError: [Errno 101] Network is unreachable

ValueError: Failed to instantiate processor step 'tokenizer_processor' with config: 
{'tokenizer_name': 'google/paligemma-3b-pt-224'}. Error: [Errno 101] Network is unreachable
EXIT_CODE=1
```

根本原因是 AutoDL 实例未执行 `source /etc/network_turbo` 启用代理，或者代理本身不可用，导致无法连接 HuggingFace Hub。此外，tokenizer 未提前缓存到本地。

### GPU1 当前状态

**空闲。** GPU0 和 GPU1 均空闲（1MiB 显存占用，0% 利用率）。GPU2 和 GPU3 被其他 python 进程占用（各 ~10GB）。

### 建议

**不需要重跑。** 理由：
1. 这是 westd-41074 上的 backup 实验，主实验 PID 118726 仍在 cqa1 上运行
2. 此外，约束 C003 明确禁止在 westd-41074 上部署 Long suite 实验（运行时间 >6h 会被 timeout kill）
3. 如果确实需要重跑，应在启动脚本中先 `source /etc/network_turbo` 并确保 paligemma tokenizer 已缓存到本地（`HF_HOME=/root/autodl-tmp/.hf_cache`）

---
