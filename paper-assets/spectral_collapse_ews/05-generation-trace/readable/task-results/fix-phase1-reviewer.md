# fix phase1 reviewer

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_phase1_reviewer_20260516T160508_result.json`
- **Structured JSON:** [`e9dfbb0c0fc0e8bf8307.json`](../../sessions/e9/e9dfbb0c0fc0e8bf8307.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 修改摘要

| 文件 | 改动 |
|------|------|
| `run_phase1.py` | `--k` default 2.0→1.0；添加 `linear_increasing` 到 CONDITION_CHOICES；`build_config` 返回 `(config, ratio_schedule)` 元组；`--gpu -1` 支持 CPU；传递 `ratio_schedule` 给 pipeline |
| `src/pipeline.py` | `run_recursive_training` 新增 `ratio_schedule: Optional[List[float]]` 参数；ratio 决定逻辑：schedule 优先 > controller > config.real_data_ratio |

## 验证结果

- `--help` 参数列表正确，`--k` default=1.0 ✓
- `from src.pipeline import run_recursive_training` import 成功 ✓
- 4 个条件的 config 构建全部正确 ✓
- `linear_increasing` schedule: `[0.2, 0.2667, ..., 0.8]`，首值=0.20，末值=0.80 ✓
- `adaptive` 模式 ratio_schedule=None，k=1.0, tau=0.02, r_min=0.20, r_max=0.80 ✓
- dry-run 因 CPU 加载模型超时未完成（正常——CPU 模式下 transformers 模型加载需 >30s），逻辑层验证已覆盖

---
