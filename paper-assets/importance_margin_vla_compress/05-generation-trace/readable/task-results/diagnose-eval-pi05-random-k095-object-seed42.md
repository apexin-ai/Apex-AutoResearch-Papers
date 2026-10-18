# diagnose eval pi05 random k095 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k095_object_seed42_20260521T200615_result.json`
- **Structured JSON:** [`852d15162720382d35f6.json`](../../sessions/85/852d15162720382d35f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**失败根因**：服务器无外网访问，`AutoTokenizer.from_pretrained("google/paligemma-3b-pt-224")` 调用 HuggingFace Hub API 时触发 `[Errno 101] Network is unreachable`。

**关键事实**：
- 模型加载成功（4143.4M params，pruning 配置正确：random, keep 243/256），9 分钟主要花在模型加载 + 网络重试
- 崩溃在 evaluation 开始前，**无任何 episode 结果**
- GPU 0 已释放，可立即重跑

**修复**：重跑前先 `source /etc/network_turbo` 启用网络代理，或预缓存 tokenizer 到本地路径。诊断报告已写入 `worker_outputs/diagnose_eval_pi05_random_k095.md`。

---
