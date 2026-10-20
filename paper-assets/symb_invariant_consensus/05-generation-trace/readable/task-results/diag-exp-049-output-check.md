# diag exp 049 output check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-049-output-check_20260518T211142_result.json`
- **Structured JSON:** [`bb18a409eadd240e95c3.json`](../../sessions/bb/bb18a409eadd240e95c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## exp-049 诊断结果

### 状态：**部署失败，确认无输出**

### 具体发现

| 项目 | 状态 |
|---|---|
| tmux session | 不存在（仅 exp032/exp033 在跑） |
| GPU 3 (cuda:3) | 完全空闲，0 MiB，无进程 |
| vLLM | **曾于 04:33 成功启动**（Mistral-7B, port 8003），现已死亡 |
| Pipeline | 从未运行（无 run_full_mvp/run_logiqa 进程） |
| 结果目录 | `exp049_mistral_logiqa200/` 存在但**完全为空** |
| 日志 | 无 pipeline 日志，vLLM 日志只有成功启动记录，无后续错误 |
| Run script | **不存在** — `scripts/` 中没有 `run_exp049.sh` |

### Root Cause

**部署不完整**。vLLM 被启动到 port 8003 并成功加载 Mistral-7B（`/tmp/vllm_exp049.log` 记录到 "Application startup complete"），但：

1. **没有对应的 run script** — `scripts/` 目录中最高编号是 exp038，不存在 exp049 脚本
2. **pipeline 从未启动** — 结果目录为空，无任何 `.log` 或 `.json` 文件
3. **vLLM 已死** — 进程 PID 29810/30018 不存在，可能因为没有 tmux session 保护而在 SSH 断开后被 SIGHUP 杀死，或被后续 exp038（也用 port 8003 + GPU 3）的部署冲突挤掉

**最可能的场景**：部署脚本未生成就尝试手动启动了 vLLM，pipeline 步骤遗漏，随后 vLLM 也因缺少 session 保护而死亡。

### 需要的修复

需要为 exp-049 创建完整的 run script（参照 `run_exp038.sh` 模板，改为 Mistral-7B + LogiQA-200），在 tmux session 中重新部署。GPU 3 和 port 8003 现在空闲，可以立即使用。是否需要我创建脚本并部署？

---
