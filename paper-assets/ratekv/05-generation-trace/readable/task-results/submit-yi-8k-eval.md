# submit yi 8k eval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_yi_8k_eval_20260516T053121_result.json`
- **Structured JSON:** [`41615c824244341fec07.json`](../../sessions/41/41615c824244341fec07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常，已开始 PPL 评估。

## 汇总

**服务器检查结果：**
| 项目 | 状态 |
|------|------|
| 脚本 `run_yi_longcontext_8k.py` | 本地直接上传（无 git remote） |
| Profile 文件（2-bit + 4/8-bit） | 已就绪 |
| Yi-1.5-9B 模型 | 已缓存 |
| WikiText-2 数据集 | 已缓存（离线可用） |

**提交结果：**
- experiment_id: `yi_8k_eval`
- GPU: `cuda:1`（物理 GPU 1）
- PID: `405564`
- Log: `~/runs/ratekv/yi_8k_eval.log`

**注意事项：**
- 首次尝试 GPU 0 因 llama 任务占用 73 GB 导致 OOM，已切到 GPU 1（mistral 仅占 41 GB，余量充足）
- GPU 1 同时跑 mistral multi-seed PPL，两个任务共享显存，若后续 mistral 内存用量增加可能出问题——建议关注日志
- token 序列长度警告（338838 > 4096）是正常的，WikiText-2 全文拼接后用 stride=8192 滑窗评估

---
