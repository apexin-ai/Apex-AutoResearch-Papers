# code aligned eval scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_aligned-eval-scripts_20260514T080412_result.json`
- **Structured JSON:** [`3439151911a5b7d7c827.json`](../../sessions/34/3439151911a5b7d7c827.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建：`/root/contamcal-irt-calibration/exp001/run_aligned_eval_05B.sh`

内容要点：
- 3 个 dosage（d000/d005/d100），每个跑 original + paraphrase（由 MODE 参数控制）
- AutoDL 环境配置齐全（network_turbo、conda、HF_HOME、SSL 证书）
- `--mc-format aligned` 显式指定
- adapter 不存在时跳过并警告
- `shift` 后 `"$@"` 透传额外参数（如 `--batch-size 4`）
- 输出目录带 `_aligned` / `_para_aligned` 后缀

用法：`CUDA_VISIBLE_DEVICES=2 bash run_aligned_eval_05B.sh both --batch-size 4`

---
