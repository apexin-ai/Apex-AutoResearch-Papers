# ops cpu prep plan005 bootstrap

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cpu-prep-plan005-bootstrap_20260515T181542_result.json`
- **Structured JSON:** [`0af86700db28ea58c9ce.json`](../../sessions/0a/0af86700db28ea58c9ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 检查报告

### 1. plan_005 `analyze_stratified.py` — PREPARING，待 Phase 1 eval 数据

| 项目 | 状态 |
|------|------|
| 脚本存在 | `/root/structfuse/scripts/analyze_stratified.py` (17KB, May 15 13:08) |
| --dry-run | 已通过，产出 `stratified_results_dryrun.json/csv` |
| 参数 | `--results-dir`, `--index-file`, `--strategies`, `--encoder`, `--seeds`, `--pool-size`, `--output-dir`(required), `--dry-run`, `--bootstrap-iter` |
| stratification_index.json | 存在 (19MB) |
| per_query 实际数据 | **不存在** — 目录中只有 `per_query_dryrun_*` 文件，缺少 `per_query_qwen_*` 真实 eval 结果 |

**缺什么才能正式跑**：需要先执行 `evaluate_stratified.py`（Phase 1）生成真实 per_query 数据。完整流程已封装在 `run_plan005_s43.sh` 中，Phase 1 做 eval，Phase 2 自动调 analyze_stratified.py。

### 2. D055 `bootstrap_paired_test.py` — READY

| 项目 | 状态 |
|------|------|
| 脚本存在 | `/root/structfuse/scripts/bootstrap_paired_test.py` (11KB, May 15 23:06) |
| strict=False 修复 | **已应用** — L67 adapter-only 路径 `strict=False` + unexpected_keys/missing_keys 校验；L76 full-model 路径同样 `strict=False` |
| adapter 检测 | `_is_adapter_only()` 函数检查 adapter_config.json 或 model.pt < 500MB |
| random_s43 checkpoint | 6.2GB (full-model) |
| embedding_distance_s43 checkpoint | 33MB (adapter-only，会走 strict=False 路径) |
| val_random_s43.jsonl | 331MB |
| base model (Qwen2.5-Coder-3B) | 存在 |
| contrastive_model.py | 存在 |
| argparse / --dry-run | **无**，所有路径硬编码为常量 |

**就绪状态**：所有输入依赖齐全，可直接运行。

### 3. 正式执行命令模板

**plan_005 全流程**（Phase 1 eval + Phase 2 analysis，约 30-60 min）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
nohup bash /root/structfuse/scripts/run_plan005_s43.sh > /tmp/plan005_s43.log 2>&1 &
echo $!
# 轮询: tail -20 /tmp/plan005_s43.log
```

**D055 bootstrap 单独运行**（约 10-20 min）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
nohup python /root/structfuse/scripts/bootstrap_paired_test.py > /tmp/bootstrap_s43.log 2>&1 &
echo $!
# 轮询: tail -20 /tmp/bootstrap_s43.log
# 产出: /root/structfuse/results/bootstrap_s43_paired.json
```

---
