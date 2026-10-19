# ssh codeql fix and rerun

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_codeql_fix_and_rerun_20260513T194805_result.json`
- **Structured JSON:** [`6d8c66904503187d4a01.json`](../../sessions/6d/6d8c66904503187d4a01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### Step 1: CodeQL pack install
- **成功**。`codeql/python-all@7.1.0` 等 13 个依赖已安装
- 过程中修复了 AutoDL 代理 SSL 证书问题（导入了代理证书到 CodeQL Java truststore）

### Step 2: 端到端测试（seatgeek/thefuzz）
- **DB create**: 成功（22 modules，1.2s）
- **call_graph.ql**: 成功，13 条结果（与 all.jsonl 记录一致）
- **bounded_dataflow.ql**: 成功，有 dataflow 路径输出
- 测试文件已清理

### Step 3: M1 重提取已启动
- **tmux session**: `m1_reextract_v2`
- **日志路径**: `/root/runs/structfuse-context/m1_reextract_v2.log`
- **实例数**: 28,276 个待重跑，82 个 unique repo groups
- **Workers**: 4
- **磁盘**: 114GB 可用
- **预估耗时**: ~60h（4 workers）
- **状态确认**: CodeQL 查询正在工作——已开始产出 call_graph 结果（gruns/furl 82 entries, feedparser 51 entries, python-docx 43 entries）
- GPU 未受影响（M2 训练 sessions 仍在运行）

---
