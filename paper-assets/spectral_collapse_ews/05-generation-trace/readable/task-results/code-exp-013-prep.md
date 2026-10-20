# code exp 013 prep

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_013_prep_20260520T074928_result.json`
- **Structured JSON:** [`8738cbf93e9ca937a8c8.json`](../../sessions/87/8738cbf93e9ca937a8c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 产出

**启动脚本** — `/root/spectral_collapse_ews/scripts/launch_pure_collapse_seed44.sh` 已更新，参数与 exp_010 一致：
- `--condition pure_collapse --seed 44 --generations 10 --signal log_det --tau 0.002 --k 0 --signal_mode per_gen`
- 支持 `bash launch_pure_collapse_seed44.sh 1` 指定 GPU

**Dry-run** — `--help` 解析通过，所有参数合法。

**Checkpoint 目录** — `pure_collapse_seed44/` 不存在，无覆盖风险。

**磁盘空间** — **严重不足**：`/root/autodl-tmp/` 250G 已用 237G，仅剩 **14G (5%)**。现有 checkpoints 占 120G。一组 pure_collapse 10-gen 实验（pythia-410m）预计需要 ~10-12G checkpoint 空间，14G 勉强够但很紧。建议启动前先清理已不需要的旧 checkpoint 或中间产物。

---
