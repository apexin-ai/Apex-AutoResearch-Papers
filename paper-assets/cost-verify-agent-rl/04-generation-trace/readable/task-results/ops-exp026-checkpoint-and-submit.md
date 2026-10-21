# ops exp026 checkpoint and submit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_checkpoint_and_submit_20260515T125816_result.json`
- **Structured JSON:** [`614e84b8025cc2ba86f7.json`](../../sessions/61/614e84b8025cc2ba86f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无法提交新任务 — 两块 GPU 都在跑 exp026。**

当前状态：
| 项 | 值 |
|---|---|
| tmux session | `exp026`，启动 18:38（今天） |
| 训练进度 | 3/150 步（2%），step 2 完成于 ~20:21 |
| GPU 占用 | cuda:0 + cuda:1 各 ~49GB/98GB VRAM |
| 每步耗时 | ~43 分钟 |
| Checkpoint | **空**（save_freq=25，尚未到第一个保存点）|
| 首次 val | step 5（test_freq=5），预计 ~1.5 小时后 |
| 首次 checkpoint | step 25，预计 ~16 小时后 |
| 训练完成 150 步 | 预计 ~4.5 天 |

**exp026 train metrics 重现了之前的正向信号**（这是重启后的新 run，指标一致）：
- step 1: success=21.88%, pass@16=1.0
- step 2: success=32.81%, pass@16=1.0, entropy=0.317（无 collapse）

**建议选项**：
1. **让它跑下去** — 等 step 5 val 结果（~1.5h），这是第一个 C003-compliant 验证点。train metrics 强正向，值得等
2. **Kill 后重提交单卡** — 杀掉当前 run，分拆成 cuda:0 训练 + cuda:1 eval（但无 checkpoint 可 eval，且丢失已跑 2 步进度）
3. **降低 save_freq** — 修改 config 重启，更频繁保存 checkpoint 以防再次中断

如何处理？

---
