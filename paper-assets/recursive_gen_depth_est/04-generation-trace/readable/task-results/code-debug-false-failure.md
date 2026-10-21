# code debug false failure

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_debug_false_failure_20260514T182414_result.json`
- **Structured JSON:** [`b9e132948c90adf2b011.json`](../../sessions/b9/b9e132948c90adf2b011.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

9 个本地脚本全部修改完毕。

---

## 总结

### 根因

`cross_model_olmo_002` 被误标 failed 的原因是 **worker 绕过了 `submit_training_job` MCP tool**（ToolSearch 没找到该工具），用 raw `ssh_execute` 创建了不含 sentinel trap 的 tmux session。进程正常完成后：
- 无 sentinel 文件 `/tmp/agent-ml-exit/cross_model_olmo_002.exit`
- 无 W&B run
- Cron handler 连续 5 次检测到 "process dead, no sentinel, no W&B" → auto-resolve as failed

### 已完成的修复

**Pipeline 脚本（服务器 + 本地，10 + 9 个文件）**：
- 在 `set -e` 后添加 EXIT trap，通过 `AML_EXP_ID` 环境变量写 sentinel
- 移除旧的错误 sentinel 代码（`touch logs/pipeline_*.done`）
- 语法验证通过，端到端测试确认 sentinel 格式正确

### 使用方式

当 worker 用 `ssh_execute` 提交时，需在 tmux 命令中传入环境变量：
```bash
tmux new-session -d -s {exp_id} 'AML_EXP_ID={exp_id} bash scripts/run_pipeline_xxx.sh ...'
```

### 框架侧问题（需人工确认）

`submit_training_job` MCP tool 在 `mcp_server.py:124` 已注册为 `@mcp.tool()`，但 worker 的 ToolSearch 未找到它。可能是 worker session 的 MCP tool 列表配置问题，建议检查：
- `/home/ubuntu/agent-ml-research/core/mcp_server.py` 中 tool 注册是否被条件过滤
- Worker session 创建时的 MCP 连接配置

---
