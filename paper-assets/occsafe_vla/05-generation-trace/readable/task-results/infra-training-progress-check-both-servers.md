# infra training progress check both servers

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_training_progress_check_both_servers_20260520T181116_result.json`
- **Structured JSON:** [`049d2e1bbba7207b5cac.json`](../../sessions/04/049d2e1bbba7207b5cac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 训练进度 ===
westd-10894 (vanilla):
  s0: step ~32634/50005, 1.09 it/s, elapsed 8:49h, ETA ~4.4h
  s1: step ~32355/50005, 1.08 it/s, elapsed 8:51h, ETA ~4.5h
  s2: step ~5901/50005, 1.07 it/s, elapsed 1:32h, ETA ~11.5h ⚠️ 已重启（原训练+resume均崩溃）

westd-34685 (occ):
  s0: step ~6064/50005, 1.09 it/s, elapsed 1:36h, ETA ~11.2h  [OCC] step=6000 occ_loss=0.0118 action_loss=0.1328
  s1: step ~6018/50005, 1.09 it/s, elapsed 1:35h, ETA ~11.2h  [OCC] step=6000 occ_loss=0.0138 action_loss=0.1279
  s2: step ~6004/50005, 1.09 it/s, elapsed 1:35h, ETA ~11.2h  [OCC] step=6000 occ_loss=0.0115 action_loss=0.1689

=== GPU ===
westd-10894 (4x 96GB):
  GPU0: 63007/97887 MiB, 99%  (vanilla_s0)
  GPU1: 62237/97887 MiB, 99%  (vanilla_s1)
  GPU2: 63031/97887 MiB, 99%  (vanilla_s2 重启中)
  GPU3: 16778/97887 MiB,  1%  (空闲)

westd-34685 (4x 96GB):
  GPU0: 62203/97887 MiB, 91%  (occ_s0)
  GPU1: 62203/97887 MiB, 45%  (occ_s1)
  GPU2: 62209/97887 MiB, 99%  (occ_s2)
  GPU3:     0/97887 MiB, 100% (异常：无显存占用但utilization=100%)

=== 磁盘 ===
westd-10894: 126G/250G (51%)
westd-34685: 111G/350G (32%)

=== Checkpoints ===
westd-10894 (vanilla):
  s0: latest, 25000_chkpt, 30000_chkpt
  s1: latest, 25000_chkpt, 30000_chkpt
  s2: latest, 25000_chkpt, 30000_chkpt (旧run遗留；新run尚无checkpoint)

westd-34685 (occ):
  s0: latest, 2500_chkpt, 5000_chkpt
  s1: latest, 2500_chkpt, 5000_chkpt
  s2: latest, 2500_chkpt, 5000_chkpt
```

**注意事项：**
- vanilla_s2 原始训练和 resume 均崩溃（exitcode 1），已从头重启，当前 step ~5901，比 s0/s1 落后约 27000 步
- westd-34685 GPU3 状态异常（0 MiB 显存占用但 utilization 显示 100%），不影响训练但值得留意

---
