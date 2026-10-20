# infra 7b pipeline env prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_7b-pipeline-env-prep_20260519T204404_result.json`
- **Structured JSON:** [`ab35bd617029d89e4b08.json`](../../sessions/ab/ab35bd617029d89e4b08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 环境准备完成

| 项目 | 状态 |
|------|------|
| 脚本部署 | ✅ 3 个脚本已部署到 `/root/autodl-tmp/struct_self_consist_ie/code/pipeline/` |
| 依赖包 | ✅ scipy 1.17.1, numpy 2.2.6, stdlib OK |
| 输出目录 | ✅ `/root/autodl-tmp/struct_self_consist_ie/output/7b_ft_signals/` 已创建 |
| Dry-run | ✅ 3 个脚本 `--help` 均正常 |

### 7B 当前输出文件

- `wnut17/qwen25_7b_n8_seed42/samples.jsonl`
- `wnut17/qwen25_7b_n8_seed123/samples.jsonl`
- `wnut17/qwen25_7b_n8_seed456/samples.jsonl`
- `fewnerd_7b/` — 空目录（实验尚未产出）

### 处理命令模板

7B 完成后 copy-paste 运行：

```bash
# 假设 7B FT 输出在标准目录结构下（含 scierc/conll2003/fewnerd 子目录）
INPUT=/root/autodl-tmp/struct_self_consist_ie/output/<7b_ft_dir>
OUTPUT=/root/autodl-tmp/struct_self_consist_ie/output/7b_ft_signals
PIPELINE=/root/autodl-tmp/struct_self_consist_ie/code/pipeline

# Step 1: 计算信号
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python $PIPELINE/compute_signals.py --input-dir $INPUT --output-dir $OUTPUT --model-size 7 --regime ft

# Step 2: 格式化 scaling curve 数据
python $PIPELINE/format_for_scaling.py --report $OUTPUT/full_signal_report.json --model-size 7 --regime ft

# Step 3: Bootstrap 显著性检验
python $PIPELINE/bootstrap_construction.py --input-dir $INPUT --output-dir $OUTPUT
```

---
