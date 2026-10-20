# infra diagnose occ s2 exit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_diagnose_occ_s2_exit_20260521T043634_result.json`
- **Structured JSON:** [`3411562164c0187ab26b.json`](../../sessions/34/3411562164c0187ab26b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```
occ_s2 退出原因: 异常退出 — 磁盘满 (No space left on device)
最终 step: 45000（在保存 45000_chkpt 时 merged_vla.save_pretrained() 写 safetensors 失败）
50000_chkpt: 不存在
错误信息: safetensors_rust.SafetensorError: I/O error: No space left on device (os error 28)
eval 已触发: 否

occ_s0 状态: 也异常退出（同一原因 — 保存 45000_chkpt 时磁盘满）
occ_s0 最终 checkpoint: 45000_chkpt（同样无 50000_chkpt）

occ_s1 (PID 58802): 也已退出（大概率同一原因）
```

**磁盘状态**: `/root/autodl-tmp` 350G 已用 350G (100%)，其中 checkpoints 占 329G（occ_s0=119G, occ_s1=90G, occ_s2=121G）。

三个训练都在 step 45000 保存 checkpoint 时因磁盘满而崩溃。需要清理旧 checkpoint 腾出空间后从 45000 恢复训练。每个实验有 9 个 checkpoint（5000, 7500, 30000-45000 每 2500 步），删除早期的即可释放空间。

---
