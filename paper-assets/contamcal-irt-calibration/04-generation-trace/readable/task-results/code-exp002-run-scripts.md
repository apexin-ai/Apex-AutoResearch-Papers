# code exp002 run scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002-run-scripts_20260514T075511_result.json`
- **Structured JSON:** [`09a980baac58ad0eb46d.json`](../../sessions/09/09a980baac58ad0eb46d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。总结：

**`/root/contamcal-irt-calibration/exp002/run_signals_05B.sh`** 已创建（chmod +x）。

与原模板的关键差异（基于实际 CLI 接口调整）：
- 参数名：`--model-path` + `--adapter-path` 代替模板中的 `--base-model`；`--ref-adapter-path` 分开传 d000 adapter
- **每 benchmark 单独调用**：`compute_signals.py` 要求 `--benchmark` 为必选参数（mmlu / gsm8k / arc_challenge），所以是 3 dosage × 3 benchmark = 9 次调用
- `aggregate_rrf.py` 用 `--signal-files`（接 merged JSON）+ `--model-name` + `--labels-file`，不是 `--signal-dirs`
- 自动检测 contamination labels（d005/d100 有，d000 没有）传给 RRF 做 AUC
- 加了 AutoDL 环境配置：`network_turbo`、`conda activate`、`HF_HOME`、SSL 证书
- 额外参数透传：`"$@"` 支持 `--dry-run`、`--max-items` 等

**d025 状态**：adapter 目录存在但为空（SFT 进行中），SFT 数据和 contamination labels 已就绪。完成后将 `d025` 加入 DOSAGE 循环即可。

---
