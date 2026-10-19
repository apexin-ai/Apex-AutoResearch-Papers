# experiment m1 extraction launch

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_m1_extraction_launch_20260512T204013_result.json`
- **Structured JSON:** [`d432fa027e1c81602a46.json`](../../sessions/d4/d432fa027e1c81602a46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

M1 全量 CodeQL 提取已成功启动。

**汇报：**

| 项目 | 详情 |
|------|------|
| **启动命令** | `nohup bash scripts/run_m1_extraction.sh > /tmp/m1_extraction.log 2>&1 &` |
| **PID** | 577864 |
| **磁盘** | 83GB 可用（52% 使用） |
| **实例数** | 50,869 Python-only instances，131 unique (repo, commit) groups |
| **Workers** | 8 CPU 并行 |
| **时间估算** | ~54h（脚本自估，可能偏保守） |
| **日志** | `/tmp/m1_extraction.log` |
| **输出** | `/root/autodl-tmp/structfuse/m1_extraction/` |

**修复的关键问题：**
- **根因**：脚本原指向 `swe_smith_metadata.jsonl`（未修复版，`buggy_function` 和 `base_commit` 为空），导致 CodeQL 外部谓词匹配不到任何函数。改用 `swe_smith_metadata_fixed.jsonl` 后 CodeQL 正常返回结果。
- 添加了 `source /etc/network_turbo` + SSL 证书环境变量（AutoDL GitHub 访问）。

**已知问题：**
- `pdfminer/pdfminer` clone 失败（exit 128，可能是 repo 不存在/已改名），会 fallback 到 skip_log。
- GPU 未占用（纯 CPU 任务），cuda:4 可用。

后续可用 `tail -30 /tmp/m1_extraction.log` 轮询进度。

---
