# code w10 beam ablation launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_beam_ablation_launch_20260517T083216_result.json`
- **Structured JSON:** [`23d4d71ae525f4448829.json`](../../sessions/23/23d4d71ae525f4448829.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理正在进行中：k2 已处理 41 样本，k8 已处理 25 样本（k2 确实更快）。

---

## 报告

### 预检结果
1. **无冲突进程** — 无 `run_constrained` 或 `python.*extraction` 残留进程
2. **模型路径** — `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B` 存在（注意：任务给的路径少了两级子目录，已修正）
3. **violation_checker.py** — 确认是 SciERC 版本（文件在项目根目录而非 `evaluation/`）

### 实验状态

| 实验 | GPU | PID | 状态 | 进度 |
|---|---|---|---|---|
| w10_beam_ablation_k2 (num_beams=2) | cuda:0 | 429459 | RUNNING | 41/551 |
| w10_beam_ablation_k8 (num_beams=8) | cuda:1 | 429690 | RUNNING | 25/551 |

### 路径修正（与任务指令的差异）
- **data_path**: `data/scierc/test.json` → `data/processed_data/test.json`
- **constraints_path**: `data/scierc/ontology_constraints_scierc.json` → `ontology_constraints.json`
- **model_path**: `/root/autodl-tmp/models/Qwen3-8B-ms` → `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`

### 预估时长
基于 k=4 baseline（551 样本，平均 5.9s/样本，总计 54 分钟）：
- **k=2**: ~30-40 分钟（beam 宽度更小，生成更快）
- **k=8**: ~90-120 分钟（beam 宽度翻倍，计算量更大）

---
