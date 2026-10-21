# diag revkl 30 s42 boolq uniform

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_revkl_30_s42_boolq_uniform_20260522T031503_result.json`
- **Structured JSON:** [`c64bec2ab9ede3e1258f.json`](../../sessions/c6/c64bec2ab9ede3e1258f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断报告：`revkl_30_s42_boolq_uniform` 失败

### 错误信息

```
'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/aps/super_glue/resolve/.../super_glue.py
Retrying in 1s [Retry 1/5].
...
RuntimeError: Cannot send a request, as the client has been closed.
```

Traceback 路径：`lm_eval.simple_evaluate` → `task_manager.load` → `ConfigurableTask.__init__` → `download` → `datasets.load_dataset` → `hf_hub_download` → 网络请求失败。

### 根因

**westd-41718 无法访问外网（HuggingFace）。** `lm-eval-harness` 在加载 BoolQ 任务时需要从 HuggingFace 下载 `super_glue` 数据集，而 westd-41718 网络不可达（Errno 101）。重试 5 次后 httpx client 被关闭，抛出 `RuntimeError`。

westd-41718 上不存在 `super_glue` 数据集的本地缓存，而 **westd-34887 上有缓存**（`/root/autodl-tmp/.hf_cache/datasets/super_glue`）。

Checkpoint 文件、模型加载、mask 计算均正常（已成功打印 32 层 sparsity）。代码本身无问题。

### 修复方案

**方案 A（推荐）：从 westd-34887 同步数据集缓存到 westd-41718**

```bash
# 在 westd-41718 上
scp -r westd-34887:/root/autodl-tmp/.hf_cache/datasets/super_glue /root/autodl-tmp/.hf_cache/datasets/
```
然后设置 `HF_DATASETS_OFFLINE=1` 重跑，避免再次触发网络请求。

**方案 B：改在 westd-34887 上运行此评估**（该服务器有缓存且网络可达）。

**方案 C：在 westd-41718 上启用代理**（`source /etc/network_turbo`），然后重跑让它在线下载。

需要我执行修复吗？

---
