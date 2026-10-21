# ops docker eval postmortem

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_docker-eval-postmortem_20260517T082557_result.json`
- **Structured JSON:** [`970c164380bd0f964b1c.json`](../../sessions/97/970c164380bd0f964b1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：Docker eval **失败**

**原因：Docker 未安装在该服务器上。**

`eval_re_repair.py` 依赖 `swebench.harness.run_evaluation`（需要 Docker 来创建容器运行测试），但 `seetacloud-westd-4x5090` 上没有 Docker。

### 当前状态

| 项目 | 状态 |
|------|------|
| PID 3610714 | 已退出（进程不存在） |
| Docker | **未安装**（`which docker` 返回空） |
| 输入数据 | 已生成：`/root/autodl-tmp/eval_results/re_repair_v2/re_repair_instances.jsonl`（9 instances） |
| eval 输出 | **不存在**（无 `eval_results.jsonl`，无 swebench logs） |
| Phase 0 (diff-sim) | 已完成（`/root/autodl-tmp/eval_results/re_repair_phase0/`，120 records） |

### 已完成的 Phase 0 结果（diff similarity，非 Docker）

| Condition | Mean Sim | Best-of-K Mean | Valid Diff |
|-----------|----------|----------------|-----------|
| control | 0.815 | 0.820 | 100% |
| cls-diag | 0.775 | 0.818 | 97% |
| oracle-diag | 0.773 | 0.809 | 100% |
| random-diag | 0.719 | 0.719 | 90% |

### 重启方案

Docker eval 无法在当前服务器上运行。选项：

1. **迁移到有 Docker 的服务器** — 需要一台支持 Docker 的机器（SWE-bench harness 要求 Docker + 大量磁盘空间缓存环境镜像）
2. **在当前服务器安装 Docker** — SeetaCloud 容器内通常无法运行 Docker-in-Docker
3. **放弃 Docker eval，改用 Phase 0 的 diff-similarity 指标** — 已有结果，但不是 resolve rate

需要你决定如何推进。

---
