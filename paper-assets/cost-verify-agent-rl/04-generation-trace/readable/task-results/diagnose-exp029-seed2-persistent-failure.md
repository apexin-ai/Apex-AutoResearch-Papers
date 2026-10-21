# diagnose exp029 seed2 persistent failure

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029-seed2-persistent-failure_20260518T172904_result.json`
- **Structured JSON:** [`027f041355661ff5242f.json`](../../sessions/02/027f041355661ff5242f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心结论：

**exp029_seed2 的 OOM 问题早已修复。** 最近反复失败的真正原因是 **磁盘空间耗尽**（`/root/autodl-tmp` 250G 盘已用 227G，91%），不是 GPU 内存问题。

4 次运行的错误分类：
| 次数 | 错误 | 状态 |
|------|------|------|
| #1 | CUDA OOM (loss.backward) | 已通过降 token_len + gradient_checkpointing 修复 |
| #2 | 磁盘满 (torch.save checkpoint) | **根因** |
| #3 | FSDP resume 设备不匹配 (optimizer_offload 改动) | 次要问题 |
| #4 | 磁盘满 (torch.save checkpoint) | **同 #2** |

训练本身完全正常（step 15-24 成功运行，success rate 37.5%），在 step 25 保存 checkpoint 时 5 个旧 checkpoint 占 100G，磁盘写满崩溃。

**修复方案**：删除 `exp029-seed2` 的 step 5/10/15/25 旧 checkpoint（释放 ~63G），清理 `hsweep-h2`（释放 41G），设 `max_actor_ckpt_to_keep: 3`，从 step 20 resume。

报告已写入 artifacts。

---
