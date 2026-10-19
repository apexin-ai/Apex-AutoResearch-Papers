# diagnose exp 004 s2 failure

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-004-s2-failure_20260522T104107_result.json`
- **Structured JSON:** [`1027ae644b4b86242ff3.json`](../../sessions/10/1027ae644b4b86242ff3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/exp-004-s2-diagnosis.md`。

**结论**：根分区 30GB 100% 满，step 2500 保存 checkpoint 时 safetensors 写入失败 (`No space left on device`)。训练本身正常收敛。

**关键数据**：
- 最后完整 checkpoint: **checkpoint-2000**（682MB，文件完整）
- checkpoint-2500 不完整（402MB，截断），需删除
- GPU 1 当前空闲，可立即恢复

**恢复路径**：先把 outputs 目录迁移到数据盘（194GB 可用）做符号链接，删除损坏的 checkpoint-2500，然后从 checkpoint-2000 恢复训练。剩余 5500 步约 14 小时。

---
