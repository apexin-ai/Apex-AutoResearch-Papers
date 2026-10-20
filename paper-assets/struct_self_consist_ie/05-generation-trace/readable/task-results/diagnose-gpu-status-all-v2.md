# diagnose gpu status all v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_status_all_v2_20260521T031918_result.json`
- **Structured JSON:** [`566267b5ec0b4316bbc9.json`](../../sessions/56/566267b5ec0b4316bbc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/report_gpu_status_20260521.md`。

**关键发现：**

### autodl-5090
- 4 GPU 全满载，**32B FewNERD 推理已完成 92%**（34513/37648），预计 3-5 分钟内结束。输出目录已创建但尚未写入结果。

### autodl-5090-b
- **无 GPU 冲突**。旧 PIDs 全部退出，新 PIDs 305836/305838 (cuda:2,3) 也已退出。仅 GPU 0/1 各跑一个 FewNERD 温度实验（t=0.5 和 t=1.2，进度 5%，约 1.5-2h 剩余）。**GPU 2/3 空闲可调度。**
- 已完成：SciERC T=0.5 s123 和 T=1.2 s123，均 verdict=MARGINAL。

### autodl-5090-c
- **SciERC T=0.8 s123 (PID 269240) 已完成**，GPU 1 空闲。结果：rho_SJ_F1=0.382（三个温度中最高），verdict=MARGINAL。
- 14B (cuda:0)、7B N=16 (cuda:2)、CoNLL N=16 (cuda:3) 仍在跑。probe_groupkfold 在 CPU 上跑，scierc 处理到 300/551。
- **GPU 1 空闲可调度。**

### 空闲资源
- 5090: 即将全部释放 4 GPU
- 5090-b: GPU 2, 3 空闲
- 5090-c: GPU 1 空闲

---
