# fix kill 181997 urgent

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_181997_urgent_20260516T053546_result.json`
- **Structured JSON:** [`112b84848fdaed55e22b.json`](../../sessions/11/112b84848fdaed55e22b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Step 1: Kill 181997
**KILLED_OK** ✓

### Step 2: 181491 状态
- **存活**，已运行 20m49s
- 当前进度：**19/804**（ProofWriter D5），ETA ~919 min（~15.3h），avg 70.1s/prob
- 输出文件：`sica_expanded_14b.json` = 73,319 bytes，type=dict，keys=`['summary', 'results']`

### Step 3: 根因分析
排查了所有自动重启机制，**全部为空**：
- crontab: 无
- systemd: 无
- supervisor: 无
- tmux sessions: 无
- 守护/wrapper 脚本: 无

**根因：181997 是一次重复的 `submit_training_job` 调用**，不是自动重启。进程树显示当前只有一条链：

```
181486 (bash wrapper, PPID=1) → 181490 (timeout 72000) → 181491 (python run_full_mvp.py)
```

这是 agent-ml-research 框架的标准 job wrapper。181997 大概率是另一个 agent 会话或重试逻辑发起的第二次提交。`/tmp/agent-ml-exit/` 中没有 `sica_expanded_14b.exit`，说明当前 wrapper 从未退出过——不存在"退出后被重启"的情况。

### Step 4: 无需禁用
没有自动重启机制，无需操作。

### Step 5: 最终确认
- 只有 181491 一个 python 进程在跑 SICA
- vLLM 健康：**Qwen2.5-14B-Instruct** 正常服务

---
