# eval hellaswag intermediate

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_hellaswag_intermediate_20260516T100202_result.json`
- **Structured JSON:** [`7099f63c66810ba55328.json`](../../sessions/70/7099f63c66810ba55328.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

HellaSwag 数据就位。

## 汇报

**当前 checkpoint 可用情况：**
- `gen_0` — 已存在，已评估

**gen_0 HellaSwag 结果：**
- acc_norm = **0.4130**
- acc = 0.3450

**训练进度：**
- Phase 0 训练正在 GPU 0 上运行（95% 利用率，~19GB 显存），仍在 gen_1 阶段（生成 50k 合成样本 + 训练），尚无 gen_1 checkpoint 产出
- 配置：10 代，每代 50k 样本，Pythia-410M

**已部署的后台评估：**
- 监控脚本 `auto_eval_hellaswag.sh` 已在后台运行 (PID 14666)，在 cuda:1 上持续等待新 checkpoint 出现并自动评估
- 结果将写入 `results/hellaswag_genX/results.json`
- 日志：`results/auto_eval.log`

**趋势判断：** 目前只有 gen_0 基线（0.4130），无法判断趋势。随着后续 checkpoint 产出，监控脚本会自动评估。需要稍后回来查看结果。

---
