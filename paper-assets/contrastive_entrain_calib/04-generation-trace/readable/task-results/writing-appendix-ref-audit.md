# writing appendix ref audit

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_appendix-ref-audit_20260525T090637_result.json`
- **Structured JSON:** [`c23eb45557767f769339.json`](../../sessions/c2/c23eb45557767f769339.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
(a) 附录盘点
- App §1: [app:training] [训练细节] 包含 reward weight 选择、response truncation 验证、hyperparameters 表(tab:hyperparams)、early termination criterion、GRPO reward variants 配置
- App §1 Table: [tab:hyperparams] [超参表格] GRPO variants 与 ACT 的训练超参对比（LR、batch、LoRA config 等）
- App §2: [app:taxonomy] [失败分类] probe-trained model 的 5 类 stubbornness 失败模式（deliberation traps 28.7%、sycophantic stubbornness 24.3%、acknowledge-but-maintain 23.8%、genuine-accept-missed 18.8%、refute/ignore 4.5%）

(b) 引用状态
- [app:training]: ✅ 已有合格引用 at framework.tex:28 "(Appendix~\ref{app:training})" — weight 选择方法
- [app:training]: ✅ 已有合格引用 at framework.tex:55 "full hyperparameters are reported in Appendix~\ref{app:training}"
- [app:training]: ❌ early termination sub-content 无直接引用 → 已添加引用 at discussion.tex:55 "termination criterion in Appendix~\ref{app:training}"
- [app:training]: ❌ truncation 验证 sub-content 无直接引用 → 已添加引用 at cosine_failure.tex:32 "we verify that no evaluation response reaches the 256-token limit (Appendix~\ref{app:training})"
- [tab:hyperparams]: ✅ 在 app:training 节内，由 framework.tex:55 覆盖（"full hyperparameters"），无需单独引用
- [app:taxonomy]: ✅ 已有合格引用 at probe_trap.tex:17 "Full taxonomy in Appendix~\ref{app:taxonomy}"

(c) 删除建议
- 无
```

---
