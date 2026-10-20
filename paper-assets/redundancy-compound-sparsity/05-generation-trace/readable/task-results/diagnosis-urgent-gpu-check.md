# diagnosis urgent gpu check

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_urgent-gpu-check_20260512T040550_result.json`
- **Structured JSON:** [`218be557c169f64e1823.json`](../../sessions/21/218be557c169f64e1823.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. GPU 状态
- **RTX 5090** (32GB), Driver 580.105.08, CUDA 13.0
- 显存占用：15841 MiB / 32607 MiB
- GPU 利用率：0%（采样瞬时值）
- 占用进程：python PID 24638（confound-ctrl-001 的子进程）

### 2. kv-bench-002
- **PID 22623 已结束**
- 结果文件存在，实验已完成（356s），结果摘要：

| Policy | Budget | PPL | Ratio | Evictions |
|--------|--------|-----|-------|-----------|
| FullCache | 100% | 7.73 | 1.000 | 0 |
| CARC-KV | 30% | 7.74 | 1.002 | 409 |
| H2O | 30% | 7.70 | 0.997 | 409 |
| StreamingLLM | 30% | 7.75 | 1.003 | 409 |
| CARC-KV/H2O/StreamingLLM | 50%/70% | 7.73 | 1.000 | 0 |

### 3. confound-ctrl-001
- **PID 24628 存活**，正在运行
- 模型已加载（DeepSeek-R1-Distill-Llama-8B，占用 ~15.5GB 显存）
- **问题**：HuggingFace 网络不通（`Errno 101: Network is unreachable`），MATH-500 和 competition_math 两个数据集的在线检查都失败了。但脚本似乎越过了重试（可能用了本地缓存），最后一行日志是 `generation flags` 警告
- 日志仅 25 行，未见推理进度输出。可能原因：(a) 正在推理但输出缓冲未刷新 (b) 卡在某处等待

### 4. 模型下载
- DeepSeek-R1-Distill-Llama-8B: **15G** ✓
- Qwen2-7B-Instruct: **15G** ✓

### 5. 注意事项
- 服务器 SSH 账户是 **root** 而非 sonny（项目配置需更新）
- confound-ctrl-001 启动时未执行 `source /etc/network_turbo`，导致 HuggingFace 不可达。如果脚本依赖在线下载数据集而非本地缓存，后续可能会出错
- 建议观察 confound-ctrl-001 日志增长情况，如果几分钟内无新输出，可能需要 kill 后修复网络问题重新提交

---
