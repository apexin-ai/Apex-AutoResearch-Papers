# code dino rerun and verdict prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dino-rerun-and-verdict-prep_20260515T132655_result.json`
- **Structured JSON:** [`d7eb8e35e164dc7f7cab.json`](../../sessions/d7/d7eb8e35e164dc7f7cab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部字段齐全。结果汇总：

### DINO 重跑结果
- `per_task_mean_rho`: **0.9008**（远高于 registry 中的 0.554 — 说明之前的 0.554 可能是旧代码/不同数据的结果）
- `pooled_rho`: 0.9001
- `per_task_rho`: 10 个 task 全部在 0.84–0.93 范围
- 文件结构：`layer_0.json`, `summary.csv`, `summary.json` — 匹配 analyze_results.py 预期

### Verdict 命令（已验证格式正确）
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/vla-ssd

python scripts/analyze_results.py \
  --results_dirs "trained:/root/autodl-tmp/vla-ssd/results/trained/,untrained:/root/autodl-tmp/vla-ssd/results/untrained/,dinov2:/root/autodl-tmp/vla-ssd/results/dinov2/" \
  --output_dir /root/autodl-tmp/vla-ssd/results/analysis/ \
  --probe_type temporal_distance
```

`analyze_results.py` 通过 `extract_per_task_mean_rho()` 读取每层的 `per_task_rho` 字典并计算均值，`compute_judgment()` 用 DINO 的 `per_task_mean_rho` 作为 gate threshold。命令格式确认无误。

### Probe 训练进度
| Probe | 当前层 | 进度 | 备注 |
|-------|--------|------|------|
| mvp_probe_trained (GPU 0) | Layer 3 | 4/33 | rho=0.9539 @ Layer 2 |
| mvp_probe_untrained (GPU 1) | Layer 4 | 5/33 | rho=0.0000（预期行为） |

每层 ~30-40s，33 层预计各需 ~20min 左右完成。

### 注意
DINO `per_task_mean_rho` = 0.9008，与 CLAUDE.md 中提到的 `DINO_GATE_THRESHOLD = 0.554` 差异很大。`analyze_results.py` 中硬编码了 `DINO_GATE_THRESHOLD = 0.554`，但实际 DINO 跑出来 0.9008。如果 judgment 逻辑用这个 0.554 做 gate，VLA trained 的 rho 需要 >= 0.554 才 PASS — 这个条件应该容易满足。但 delta (VLA - DINO) 的 effect size 比较会基于实际 DINO 结果，DINO 这么高意味着 VLA 需要显著超过 0.9 才能显示 meaningful contribution。

---
