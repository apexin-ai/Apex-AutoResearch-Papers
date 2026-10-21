# code fix sgs diagnostic bug

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_sgs_diagnostic_bug_20260515T143724_result.json`
- **Structured JSON:** [`ec7d4bcbad67cf54b0aa.json`](../../sessions/ec/ec7d4bcbad67cf54b0aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复完成

**Diff**：删除了 models.py L388-417（30行 SGS 诊断块），包含：
- `# SGS diagnostics` 注释
- 每 1000 步的 `torch.autograd.grad` 诊断（计算 `dt_emb_reward_grad_norm` / `dt_emb_decoder_grad_norm`）
- 每 5000 步的 `dt_emb_weight_norm` / `dt_emb_weight_diff_dt1_dt2` 记录

**SGS 核心机制（L338-355 的 gradient hook）未修改。**

**验证结果**：
- 修复后文件大小：34,558 bytes
- Dry-run（`--reward_dt_emb_detach True`）成功运行到 step 5000+，metrics 正常产出，无崩溃
- 仅有 gym deprecation warning 和 GradScaler deprecation warning（均无关）

**结论：models.py 已修复，exp_016 可以安全启动。**

---
