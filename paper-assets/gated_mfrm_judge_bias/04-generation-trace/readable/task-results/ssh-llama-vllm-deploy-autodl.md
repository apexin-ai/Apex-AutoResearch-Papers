# ssh llama vllm deploy autodl

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama_vllm_deploy_autodl_20260523T234632_result.json`
- **Structured JSON:** [`3a207ebd9a9e1ebf92d7.json`](../../sessions/3a/3a207ebd9a9e1ebf92d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### LLaMA 下载状态：**进行中，未完成**

| 项目 | 状态 |
|------|------|
| 总文件数 | 17（含 9 个 safetensors 分片） |
| 已完成 safetensors | 3/9（001, 004, 007），约 14GB |
| 未完成 safetensors | 6 个（.incomplete 状态） |
| 总目录大小 | 28GB（含缓存中的部分下载） |
| 下载进度 | 5/17 files (29%) |
| 下载进程 | PID 480645，活跃中 |
| 问题 | HF 下载遇到超时（`The read operation timed out`），正在自动重试 |

### 后续步骤无法执行

根据指令，safetensors 文件不完整，**vLLM 部署、config 创建、collect.py 启动均暂停**。

### 建议

AutoDL 通过代理下载 HuggingFace 大文件极慢（~200KB/s），当前下载可能还需 1-2 小时。可以考虑：

1. **等待当前下载完成** — huggingface_hub 有自动重试机制，会继续跑
2. **切换 ModelScope** — 如果该模型在 ModelScope 有镜像，国内 CDN 会快很多（但 `casperhansen/Llama-3.3-70B-Instruct-AWQ` 是第三方量化版本，ModelScope 不一定有）
3. **下载完成后重新执行本流程** — 所有后续步骤（Step 2-6）可一次性跑完

---
