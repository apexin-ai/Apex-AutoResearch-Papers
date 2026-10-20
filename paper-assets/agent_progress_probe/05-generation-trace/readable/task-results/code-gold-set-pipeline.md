# code gold set pipeline

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gold-set-pipeline_20260514T191223_result.json`
- **Structured JSON:** [`889d507cd9c20158dcbe.json`](../../sessions/88/889d507cd9c20158dcbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 产出总结

### 脚本：`evaluate_gold_set.py`（640行）
- 位置：`/root/autodl-tmp/agent_progress_probe/evaluate_gold_set.py`
- 评估 6 个模型：MV Labels, GRU Probe, Structural RF, Structural GB, TWV Labels, TWV Probe
- 支持 `--gold_csv` 和 `--dry_run` 两种模式
- 输出 `results.json` + `report.md`
- 容错：模型/数据缺失时跳过并 warn

### Dry-run 结果（cuda:1, 48.9s）

| Model | Macro-F1 | F1(stag) | Accuracy |
|---|---|---|---|
| MV Labels | 1.0000 | 1.0000 | 1.0000 |
| GRU Probe | 0.9612 | 0.9521 | 0.9633 |
| Structural RF | 0.9994 | 0.9992 | 0.9994 |
| Structural GB | 0.9991 | 0.9989 | 0.9992 |
| TWV Labels | 0.9469 | 0.9322 | 0.9510 |
| TWV Probe | 0.9441 | 0.9289 | 0.9482 |

- MV=1.0 符合预期（pseudo gold 本身就是 MV conf>=2）
- Structural RF/GB 接近 1.0（过拟合 MV 标签的结构特征）
- GRU Probe 和 TWV 的差异将在真实 gold labels 下显现

### 使用方式
```bash
# 标注完成后：
python evaluate_gold_set.py --gold_csv gold_labels.csv --output_dir gold_results --device cuda:1
```

---
