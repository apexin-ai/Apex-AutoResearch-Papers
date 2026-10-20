# diagnose cwm v6 sigterm

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cwm-v6-sigterm_20260512T205350_result.json`
- **Structured JSON:** [`12510e6c980a611abf5e.json`](../../sessions/12/12510e6c980a611abf5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告写入 `artifacts/cwm_v6_diagnosis.md`。核心结论：

**SIGTERM 来源是 SeetaCloud 平台**，不是 OOM。tmux server 被宿主机/编排系统杀死，SIGTERM 级联到训练进程。cgroup 所有指标（memory/pids/cpu）均远未触及上限。

**但更严重的问题是 checkpoint 从未保存成功。** 6 次 CWM 训练、所有 checkpoint 目录全空。v1 跑到 step 694（理应有 6 个 checkpoint），目录仍然为空。这意味着即使训练不被 kill，checkpoint 保存逻辑本身就有 bug。

**建议优先级**：
1. 修 checkpoint 保存 bug（排查 Trainer 的 save_strategy/save_steps 是否实际生效）
2. 添加 SIGTERM handler 做 graceful shutdown 保存
3. 降低 save_steps 到 50
4. 解决上述问题后可继续在 seetacloud 训练（从零开始，无可用 checkpoint resume）

---
