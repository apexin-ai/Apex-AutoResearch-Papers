# code cleanup awq residual

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cleanup-awq-residual_20260515T170600_result.json`
- **Structured JSON:** [`e6c18ab668d41643441a.json`](../../sessions/e6/e6c18ab668d41643441a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有找到 AWQ 残留文件。磁盘现状如下：

**磁盘使用：213GB / 250GB（85%），38GB 可用**

数据盘大文件分布：

| 路径 | 大小 | 说明 |
|------|------|------|
| `.hf_cache/llama-3.3-70b-instruct-fp8` | **68GB** | Llama-3.3-70B FP8 模型缓存 |
| `output_seed0/` | 92GB | 实验输出 |
| `.hf_cache/qwen3-32b-fp8` | 32GB | Qwen3-32B（保护） |
| `models/llama-3.1-8b-instruct` | 15GB | LLaMA-8B（保护） |
| `output_v7/` | 6.3GB | 实验输出 |

AWQ-INT4 模型文件不存在（可能之前已清理，或下载失败未留残留）。

最大可释放空间是 **`llama-3.3-70b-instruct-fp8`（68GB）** — 不在保护列表上，且 exp012 用的是 8B 模型。是否删除？

---
