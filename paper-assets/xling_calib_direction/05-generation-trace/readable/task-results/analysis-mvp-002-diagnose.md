# analysis mvp 002 diagnose

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_002_diagnose_20260520T185417_result.json`
- **Structured JSON:** [`a13025334cd900aa840b.json`](../../sessions/a1/a13025334cd900aa840b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**mvp_002 进程正常退出（EXIT_CODE=0），但结果无效——是脚本 bug，不是崩溃。**

### 根因：层配置不一致

`run_mvp_002.sh` 中三个步骤的层配置不匹配：

| 步骤 | 实际使用的层 | 结果 |
|------|-------------|------|
| `extract_activations.py` | `--layers 2,6,10,14,18,22,26` ✅ | 42 个激活文件全部正确生成 |
| `train_probe.py` | 默认 `0,4,8,12,16,20,24,28,31` ❌ | 找不到 `layer0_en.pt` 等文件，全部 SKIP |
| `transfer_eval.py` | 默认 `0,4,8,12,16,20,24,28,31` ❌ | 无 probe 可用，全部 SKIP |

### 修复

在 `run_mvp_002.sh` 中给 `train_probe.py` 和 `transfer_eval.py` 加 `--layers 2,6,10,14,18,22,26`：

```bash
python train_probe.py \
  --activations_dir ./activations_mvp002 \
  --output_dir ./probes_mvp002 \
  --layers 2,6,10,14,18,22,26          # <-- 缺这行

python transfer_eval.py \
  --activations_dir ./activations_mvp002 \
  --probes_dir ./probes_mvp002 \
  --output_dir ./results_mvp002 \
  --layers 2,6,10,14,18,22,26          # <-- 缺这行
```

### 恢复

激活文件（~8GB，42个文件）完好，重跑时**只需从 probe 训练开始**，无需重新提取激活，节省约 1.5 小时 GPU 时间。

Registry 已更新为 `DONE/failed`。

---
