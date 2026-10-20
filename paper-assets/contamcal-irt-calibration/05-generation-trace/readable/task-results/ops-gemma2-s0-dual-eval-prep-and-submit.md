# ops gemma2 s0 dual eval prep and submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gemma2-s0-dual-eval-prep-and-submit_20260520T202051_result.json`
- **Structured JSON:** [`c2adfb4770d77bc14de7.json`](../../sessions/c2/c2adfb4770d77bc14de7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重要发现：

**当前状态：**
- **d050 训练**：GPU 1 上运行中，进度 3342/3642 (92%)，约 12 分钟完成
- **d100 训练**：尚未开始。sweep 脚本在 d050 之后会自动启动 d100，d100 数据量最大（116k+ samples），预计还需 ~2.5-5 小时
- **已完成 checkpoint**: d000, d005, d025（均有 adapter 文件）
- **d050**: lora_adapter 目录存在但尚未写入文件（训练完成时才写）
- **d100**: 目录不存在

**sweep dosage 列表是 000/005/025/050/100**（不含 d075），与你预期的 d0/d025/d050/d075/d100 不完全一致。

**已有脚本：**
- MMLU s0 eval: `eval_gemma2_s0_mmlu.sh` — 已存在，但用 cuda:0
- ARC s0 eval: 不存在（只有 s123 版本）

由于 d100 训练还需数小时，eval 无法在短期内全部跑完所有 dosage。两个选项：

**A)** 现在准备好两个 eval 脚本（MMLU 改到 cuda:2，新建 ARC s0 版本 cuda:0），等全部训练完成后提交
**B)** 先对已有 checkpoint (d000/d005/d025) 跑 eval，d050/d100 完成后再补跑

你要哪个方案？

---
