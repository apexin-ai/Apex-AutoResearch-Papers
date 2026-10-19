# deploy fix bjb2 40593 obj adapt s45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_fix-bjb2-40593-obj-adapt-s45_20260523T175216_result.json`
- **Structured JSON:** [`9d44a65429174ccc6fde.json`](../../sessions/9d/9d44a65429174ccc6fde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

**1. Checkpoint SCP 结果**
- 从 bjb1-32546 经本地中转 scp 到 bjb2-40593 成功
- md5sum: `4161c6403b8eb268864b99dd986be784`（源/目标一致）
- 文件大小: 1,320,219 bytes

**2. 新进程状态**
- PID: 175263，tmux session: `eval-obj-adapt-s45-r2`
- GPU 0 占用 5898 MiB / 24564 MiB
- CRM checkpoint 已成功加载（327,198 params），10 个 LIBERO-Object tasks 已加载，正在运行 eval

**3. s46 checkpoint 状态**
- bjb2-28827 上 `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` 存在，1,320,219 bytes，正常

**4. Registry 更新**
- `eval-supp-obj-adapt-tau025-s45-r2` 已创建，status=RUNNING，parent=eval-supp-obj-adapt-tau025-s45

---
