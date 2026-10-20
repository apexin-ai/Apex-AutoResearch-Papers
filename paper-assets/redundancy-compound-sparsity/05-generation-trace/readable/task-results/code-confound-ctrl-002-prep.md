# code confound ctrl 002 prep

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_confound-ctrl-002-prep_20260512T024823_result.json`
- **Structured JSON:** [`d04ef1bdc9326df83d01.json`](../../sessions/d0/d04ef1bdc9326df83d01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：**

1. **模型下载** — 已用 nohup 后台启动 (PID=19552)，当前进度 ~5%，4 个分片并行下载中，速度 ~800KB/s。日志：`/tmp/qwen2_download.log`

2. **脚本** — `/home/sonny/redundancy-compound-sparsity/results/confound_ctrl/confound_ctrl_002.py` 已创建，语法检查通过。与 confound_ctrl_001.py 的差异：
   - `MODEL_PATH` → `/root/autodl-tmp/.ms_cache/Qwen/Qwen2-7B-Instruct`
   - `MAX_NEW_TOKENS` → 2048（指令模型回答短）
   - 实验名 `confound-ctrl-002`，输出 `confound_ctrl_002_results.json`
   - metadata 含 `hypothesis`、`compare_against`（DeepSeek-R1-Distill-Qwen-7B r=0.147 + Llama-3.1-8B-Instruct r=0.471）、`interpretation` 两种结果解读
   - 架构参数从 model.config 自动读取（预期 28 layers, 4 KV heads）

3. **未提交实验**（GPU 被占用）

下载速度较慢（~800KB/s），预计需要数小时完成。可稍后用 `tail -5 /tmp/qwen2_download.log` 轮询。

---
