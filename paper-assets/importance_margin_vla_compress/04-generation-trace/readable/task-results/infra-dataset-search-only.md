# infra dataset search only

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_dataset-search-only_20260515T134144_result.json`
- **Structured JSON:** [`60151d8424a273fb15f9.json`](../../sessions/60/60151d8424a273fb15f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两次搜索都没返回结果。libero 搜索为空，lerobot author 下也没匹配到数据集。

stdout/stderr 原样输出：

```
设置成功
注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证
---
```

libero 相关数据集搜索为空，lerobot 作者下的 top 20 数据集也为空。可能原因：该版本 `huggingface_hub` 的 `list_datasets` API 行为有差异，或代理环境下 API 请求未正确返回数据。

---
