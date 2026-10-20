# exp medium external seed123 chain cuda1

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_medium_external_seed123_chain_cuda1_20260514T020008_result.json`
- **Structured JSON:** [`cb57b3616da224bda5cd.json`](../../sessions/cb/cb57b3616da224bda5cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇报：

### 1. cuda:1 当前状态
- **medium_external_seed42**：Generation 6/7（第7代，共8代），正在训练阶段
- 从 06:56 开始，已运行约 3 小时，每代约 26 分钟
- 预计 seed42 还剩 ~45 分钟完成（gen 6 剩余 + gen 7）

### 2. Chain 方式
采用**方法 C（tmux send-keys）**。chain_cuda1.sh 完成后（seed42 → medium_random50），seed123 命令自动执行。

执行链顺序：
1. medium_external_seed42 ← 当前运行中，~45min 完成
2. medium_random50 ← chain_cuda1.sh 中已有，预计 ~3.5h
3. **medium_external_seed123** ← 已排队（send-keys）

### 3. 预计启动时间
- seed42 完成：~10:45 CST
- medium_random50 完成：~14:15 CST
- **seed123 预计启动：~14:15 CST（约 4 小时后）**

已创建脚本 `run_medium_external_seed123.sh`（seed=123, 输出到 `results_medium_external_seed123/`），日志写入 `/root/autodl-tmp/div_cal_verify/medium_external_seed123.log`。

---
