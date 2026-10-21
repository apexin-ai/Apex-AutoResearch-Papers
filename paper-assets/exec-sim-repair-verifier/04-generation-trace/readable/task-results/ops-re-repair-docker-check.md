# ops re repair docker check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_re-repair-docker-check_20260517T040114_result.json`
- **Structured JSON:** [`12d545c23a094294fc72.json`](../../sessions/12/12d545c23a094294fc72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。

---

## Docker 可行性结论
**不可行** — `docker` 命令不存在（`command not found`）。swebench-harness 也未安装。无法在此服务器上进行 SWE-bench Docker 验证。

## SWE-bench 数据
**有** — 数据充足：
- HF cache: `datasets--princeton-nlp--SWE-bench_Verified` (arrow 格式)
- 项目目录 `/home/sonny/exec-sim-repair-verifier/data/swebench_full/`:
  - `swebench_test.jsonl`, `swebench_train.jsonl`, `swebench_val.jsonl`
  - `swebench_verified_meta.jsonl`
  - 4 种 mutation prediction 文件 (`boundary_removal`, `off_by_one`, `operator_swap`, `return_value`)
  - `predictions_gold.jsonl`
  - trajectory 文件 (`traj_*.jsonl`)

## 代码审计摘要

### prompt 结构
4 个 condition，信息差递增：
| Condition | 信息内容 |
|-----------|---------|
| `control` | 只有 Issue Description + Incorrect Patch，**无任何测试信息** |
| `random-diag` | 加入随机 50% pass/fail 标签的测试诊断（噪音 baseline） |
| `cls-diag` | 模拟分类器 ~84% 准确率（翻转 16% oracle 标签） |
| `oracle-diag` | 完美测试诊断（ground truth per-test pass/fail） |

所有 condition 共享 system prompt（要求输出 unified diff）和 base prompt（issue + mutation patch）。

### eval metric
**Diff similarity** — `difflib.SequenceMatcher.ratio()` 对比生成 diff 与 gold patch。统计：
- mean/median similarity
- best-of-K (per instance 取最高)
- win rate（条件 beat control 的 instance 占比）
- valid diff 比率

**无 Docker 执行验证**（文件 docstring 明确写 "No Docker verification"）。

### Docker eval 代码路径
**不存在。** `re_repair_eval.py` 文件不存在。当前只有 `re_repair_phase0.py` 使用 diff similarity 作为 proxy metric。

### 外部依赖
- `numpy`
- `transformers` (AutoModelForCausalLM, AutoTokenizer)
- `torch`
- 标准库: `difflib`, `json`, `re`, `argparse`, `logging`, `pathlib`, `collections`

## 磁盘
| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| `/root/autodl-tmp` | 250G | 184G | 67G | 74% |
| `/` (overlay) | 30G | 21G | 9.5G | 69% |

## Instruct 模型
**无 Qwen3-8B-Instruct。** 现有的是 base 模型：
- `/root/autodl-tmp/models/Qwen/Qwen3-8B`（5 个 safetensors shard，完整）
- `/root/autodl-tmp/models/Qwen/Qwen3-32B`

下载可行性：`hf` CLI 已安装，但 `hf whoami` 不可用（命令接口变化）。磁盘剩余 67G 足够存放 Qwen3-8B-Instruct（~16GB）。需要确认网络连通性和正确的 `hf` 子命令后可执行下载。

---
