# diag exp 14b inference scierc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_14b_inference_scierc_20260520T145131_result.json`
- **Structured JSON:** [`2bdb6f96cda97a2e5c0d.json`](../../sessions/2b/2bdb6f96cda97a2e5c0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**三个 inference 都没有失败，实际情况是 registry 状态不同步。**

### 各实验实际状态

| 实验 | GPU | 实际状态 | Registry 状态 | 详情 |
|------|-----|---------|--------------|------|
| **scierc** | GPU 3 (空闲) | ✅ **已完成全部 5 个 N** | DONE(failed) ❌ | 22:38 完成，日志 "ALL SciERC DONE" |
| **conll** | GPU 1 (98%) | 🔄 **运行中，n4 进度 77%** (10629/13812) | PREPARING ❌ | n1、n2 已完成，正在跑 n4 |
| **fewnerd** | GPU 0 (99%) | 🔄 **运行中，n1 进度 35%** (13029/37648) | PREPARING ❌ | PID 201001，已跑 ~26 分钟 |

### 根本原因

**没有任何实际失败。** 问题出在实验 registry 没有正确记录 spec（command/server/pid），导致 cron reconcile 误判：
- scierc 正常完成后进程退出 → cron 找不到进程 → 标记为 failed
- conll/fewnerd 进程一直在跑 → 但 registry 无 spec 信息 → 保持 PREPARING

### 关键数据点

- **磁盘空间**: 127G 可用，充足
- **Checkpoint**: `qwen25-14b-fewnerd-merged-final` 存在且正在使用
- **SciERC 结果质量极差**: greedy_f1=0.004, 99% samples F1=0, verdict=FAIL（模型只在 FewNERD 上微调，不能泛化到 SciERC 的 schema）
- **预计完成时间**: CoNLL n4 快完了（~2min），之后还有 n8、n16；FewNERD n1 还需 ~45 分钟，之后 n2-n16 会更久

### 需要做的

1. **修正 registry 状态** — scierc 标记为 DONE(success)，conll/fewnerd 标记为 RUNNING 并填入正确的 PID/server
2. **不需要重跑** — 三个实验都在正常工作
3. **SciERC 质量问题需要后续关注** — 14B 模型在非训练域数据集上 F1 接近 0，可能需要 domain-specific 微调或检查 prompt/schema 是否正确

---
