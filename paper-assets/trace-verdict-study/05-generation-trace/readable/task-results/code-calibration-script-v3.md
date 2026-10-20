# code calibration script v3

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_calibration_script_v3_20260515T144638_result.json`
- **Structured JSON:** [`980a4d1dd8fe65f119b7.json`](../../sessions/98/980a4d1dd8fe65f119b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并通过语法检查：`/root/trace-verdict-study/scripts/calibration_deepseek.sh`

要点：
- 4 个 DeepSeek 条件逐个跑，`--condition` 用基础名（vota/no_trace 等）以匹配测试数据文件，`--checkpoint_dir` 和 `--model_path` 指向 DeepSeek 路径
- checkpoint 不存在时自动跳过（适配 exception_only/full_trace 尚未完成的情况）
- 输出统一到 `/root/autodl-tmp/trace-verdict-study-checkpoints/calibration_deepseek/`，文件名带 `deepseek_` 前缀
- 用法：`bash scripts/calibration_deepseek.sh --gpu 0`

---
