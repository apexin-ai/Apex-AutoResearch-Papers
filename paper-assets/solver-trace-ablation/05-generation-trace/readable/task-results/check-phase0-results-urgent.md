# check phase0 results urgent

**solver trace ablation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase0_results_urgent_20260513T094715_result.json`
- **Structured JSON:** [`811cd213e37060d41c57.json`](../../sessions/81/811cd213e37060d41c57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 0 v2 状态：**卡在 Step 3，未产出结果**

### 进度

| Step | 状态 | 详情 |
|------|------|------|
| Step 1 (checkpoint) | ✅ | `checkpoint/` 目录已创建 |
| Step 2 (generation) | ✅ | 5000/5000 samples 生成完毕，`synthetic.jsonl` 15MB |
| Step 3 (scoring) | ❌ 卡死 | 加载 `stella_en_1.5B_v5` embedding 模型时 HF 连接超时 |
| Step 4 (correlation) | ⏳ | 未到达 |

### 错误信息

Step 3 在 17:06:12 开始 scoring，试图从 HuggingFace 下载 `NovaSearch/stella_en_1.5B_v5` 模型文件，反复 `ReadTimeoutError`：

```
HTTPSConnectionPool(host='huggingface.co', port=443): Read timed out. (read timeout=10)
```

最后一条日志停在 **17:08:22**，Retry 3/5。之后日志无更新——进程大概率已在重试耗尽后崩溃。

### GPU
- cuda:0: 0% util, 79GB/98GB used
- cuda:1: 0% util, 83GB/98GB used

显存被占但 GPU 空闲，模型加载到显存后卡在网络 I/O。

### 缺失的输出文件
`correlation_matrix.json`、`summary.json`、`scored_samples.jsonl`、`*.png` 均不存在。

### 根因
典型 AutoDL 网络问题。运行前未执行 `source /etc/network_turbo` 启用代理加速，导致 HuggingFace API 超时。需要：
1. Kill 当前进程
2. 设置 `source /etc/network_turbo` + `HF_HUB_DISABLE_XET=1` + SSL 证书环境变量
3. 或者先用 ModelScope 把 stella 模型下载到本地再离线加载
4. 重跑 Step 3

**不更新 registry**（无输出结果）。需要你确认下一步操作。

---
