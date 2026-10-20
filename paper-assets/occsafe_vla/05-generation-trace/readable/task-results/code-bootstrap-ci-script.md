# code bootstrap ci script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap_ci_script_20260523T060243_result.json`
- **Structured JSON:** [`4b5dadcec9e72ea1221a.json`](../../sessions/4b/4b5dadcec9e72ea1221a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是汇总：

## 任务 1：Bootstrap CI 脚本

**文件：** `westd-34685:/root/occsafe_vla/analysis/bootstrap_ci.py`

用法：
```bash
python3 bootstrap_ci.py --config bootstrap_config.json --output bootstrap_results.json
```

**运行结果（B=10000, hierarchical bootstrap, 95% percentile CI）：**

| Condition | Seeds | TSR | CAR | CAR 95% CI |
|-----------|-------|-----|-----|------------|
| Vanilla | 3 | 0.907±0.009 | 0.780±0.012 | [0.759, 0.801] |
| Full OCC | 3 | 0.894±0.050 | **0.797±0.032** | [0.776, 0.817] |
| Detach OCC | 3 | 0.812±0.163 | 0.746±0.002 | [0.723, 0.768] |
| Random OCC | 3 | 0.869±0.029 | 0.789±0.031 | [0.767, 0.809] |
| Depth | 4 | 0.888±0.042 | 0.780±0.039 | [0.762, 0.797] |
| Cutoff | 2 | 0.915±0.004 | 0.783±0.021 | [0.757, 0.808] |

**显著 pairwise 差异（CI 不包含 0）：** Detach OCC 显著差于其他所有条件（CAR 最低）。Full OCC vs Vanilla 的 ΔCAR=+0.017 不显著但方向正确。

## 任务 2：Eval 数据清单

**文件：** `westd-34685:/root/occsafe_vla/analysis/eval_data_manifest.json`

已找到全部 50r eval 数据：
- **Vanilla**: 3 seeds ✓ (westd-34685)
- **Full OCC**: 3 seeds ✓ (westd-34685, s1 用 occ_s1_fresh)
- **Detach OCC**: 3 seeds ✓ (westd-10894 → 已拷贝到 westd-34685)
- **Random OCC**: 3 seeds ✓ (westd-10894 → 已拷贝到 westd-34685)
- **Depth**: 4 seeds ✓ (s0/s1 westd-34685, s2/s3 westd-10894 → 已拷贝)
- **Cutoff**: 2 seeds（s2 eval 待完成）

westd-10894 的 8 个 eval JSON 已重建到 `westd-34685:/root/occsafe_vla/analysis/eval_data_from_10894/`。

---
