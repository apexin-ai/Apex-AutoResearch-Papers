# diagnose phase diagram t25 a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase_diagram_t25_a050_s42_fp32_20260521T192551_result.json`
- **Structured JSON:** [`bf127cf195ffcc6ea397.json`](../../sessions/bf/bf127cf195ffcc6ea397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**失败原因**：磁盘满（350G/350G，100%）。gen_14 训练完成（5000/5000 steps）但 `model.save_pretrained()` 写 safetensors 时 `No space left on device`。

**进度**：14/25 generations 完成（gen_0~gen_13 全部数据完整可用），gen_14 checkpoint 截断损坏（293MB vs 正常 1.6GB）。

**重试前需要**：
1. 释放磁盘空间（phase_diagram 目录占 36GB，剩余 11 gen checkpoint 还需 ~17.6GB）
2. 删除 gen_14 损坏数据
3. 补上 HF_HOME 三件套

报告已保存到 `artifacts/phase_diagram_t25_a050_s42_fp32/failure_diagnosis.md`。

---
