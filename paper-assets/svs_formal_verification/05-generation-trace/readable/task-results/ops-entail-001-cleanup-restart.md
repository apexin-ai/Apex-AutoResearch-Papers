# ops entail 001 cleanup restart

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_entail_001_cleanup_restart_20260514T151137_result.json`
- **Structured JSON:** [`e576b5c657a6320c3baa.json`](../../sessions/e5/e576b5c657a6320c3baa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总报告：

---

## 执行结果

### 1. 进程清理
无活跃的 10q/entailment_rescore 进程需要清理（之前已被 kill 或自行终止）。

### 2. vLLM 状态（cuda:0+1）
- **模型**: DeepSeek-R1-Distill-Qwen-14B, TP=2, port 8001
- **GPU 占用**: cuda:0 31452MiB/32607MiB, cuda:1 31452MiB/32607MiB
- **GPU 利用率**: 0%（空闲，无推理请求）
- **API 响应**: 正常（`/v1/models` 返回 200）
- cuda:2+3 完全空闲（3MiB）

### 3. v3 rescorer
- **PID**: 76901（bash wrapper: 76896）
- **状态**: RUNNING，已匹配 50 个 problems，从 problem 1/50 开始处理
- **启动命令**: `cd /root/autodl-tmp/svs_formal_verification && nohup python entailment_rescore_v3.py > /root/outputs/entail_001_v3.log 2>&1 &`
- **日志**: `/root/outputs/entail_001_v3.log`
- **输出**: `/root/outputs/entailment_rescore_v3_results.json`
- **Checkpoint**: 每 2 个 problem 自动保存

### 4. 预计完成时间
之前 v3 跑了 ~7 分钟只处理了 problem 1/50 的部分 chain（被 kill 前未完成）。按每个 problem ~7-10 分钟估算，50 个 problem 约 **350-500 分钟（6-8 小时）**。因为使用远程 V3.2 API，网络延迟是瓶颈。

### 5. 注意事项
- 脚本没有内建 resume 逻辑——如果再次中断，需从头开始（但 checkpoint 文件中的部分结果可手动恢复）
- 此次匹配到 50 个 problems（上次 46 个），可能是 ProofWriter cache 更新了
- 不消耗本地 GPU 资源，全部走远程 DeepSeek V3.2 API

---
