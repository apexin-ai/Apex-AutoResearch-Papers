# diagnose fulllayer action probe status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_fulllayer_action_probe_status_20260516T044354_result.json`
- **Structured JSON:** [`a88445008a5d7994c9f3.json`](../../sessions/a8/a88445008a5d7994c9f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：DONE** — 进程已正常完成。

| 项目 | 状态 |
|------|------|
| PID 700649 | 已退出（不在进程表中） |
| 退出码 | `EXIT_CODE=0`（成功） |
| 运行时长 | 19.5 分钟 |
| GPU | 两块 GPU 均已释放（0 MiB / 0% 利用率） |
| 结果文件 | `/root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json`（120KB，写入时间 12:10） |

### 实验结果摘要

**Trained model probing（33层，L0-L32）：**
- `image_mean` peak: **L8, R²=0.6553**
- `last_preaction` peak: **L13, R²=0.6779**

**Untrained model probing：**
- `image_mean` peak: **L0, R²=0.6403**
- `last_preaction` peak: **L32, R²=0.6093**

**Bootstrap 对比（全部显著）：**
- trained(L8) vs untrained(L0) image_mean: delta=+0.0149, p=0.006
- trained(L13) vs untrained(L32) last_preaction: delta=+0.0686, p<0.0001
- same-layer(L8) image_mean trained vs untrained: delta=+0.1229, p<0.0001
- same-layer(L13) last_preaction trained vs untrained: delta=+1.0071, p<0.0001

---
