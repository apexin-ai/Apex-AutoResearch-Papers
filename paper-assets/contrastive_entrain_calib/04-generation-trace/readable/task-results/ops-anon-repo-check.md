# ops anon repo check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_anon-repo-check_20260523T161229_result.json`
- **Structured JSON:** [`5ba5646f6a2418a0026f.json`](../../sessions/5b/5ba5646f6a2418a0026f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕。以下是完整性检查汇总：

---

## 匿名仓库完整性检查报告

### 1. 代码完整性 ✅

| 目录/文件 | 状态 | 内容 |
|-----------|------|------|
| `training/` | ✅ 存在 | 17 个文件，覆盖 DCGRPO、R3-only、ACT、probe penalty、steering 等多组实验 |
| `eval/` | ✅ 存在 | 8 个文件，含 pipeline、unified preset、vanilla baseline、NLI utils、lm-eval |
| `data/` | ✅ 存在 | 4 个文件：train_split、eval_split、eval_held_out、calibration_v2_1_expanded |
| 配置文件 | ✅ 存在 | `requirements.txt`、`.gitignore`、多个 `.sh` 脚本 |
| 根目录工具脚本 | ✅ 存在 | extract_activations、compute_directions、evaluate_directions 等 |

总计 **46 files**，与 commit 记录一致。

### 2. README 检查 ⚠️ 有缺失

| 项目 | 状态 | 说明 |
|------|------|------|
| 项目描述 | ✅ | 有，描述了三阶段 pipeline |
| 环境依赖 | ✅ | 提到 Python 3.10+, CUDA 12.x, PyTorch 2.x, `pip install -r requirements.txt` |
| 训练使用说明 | ⚠️ **不足** | 没有具体的训练命令示例（如 `python training/run_exp003_r3only.py`） |
| 评估使用说明 | ⚠️ **不足** | 没有评估命令示例 |
| 数据格式说明 | ⚠️ **不足** | 仅提到 292 train / 70 held-out 的数量，缺少 JSONL 字段说明 |
| 复现步骤 | ❌ **缺失** | 没有 step-by-step 的复现流程 |

### 3. 敏感信息检查 ✅ 通过

- **作者身份**：所有文件均无姓名、邮箱、机构信息 ✅
- **API key / token**：未发现任何硬编码凭证 ✅
- **绝对路径**：所有路径均为相对路径（`./models/`、`./data/`） ✅
- **wandb 实体名**：未发现 wandb project/entity 配置 ✅
- **GitHub org 名**：使用 `anonymous-nlp-2026-2`，已匿名 ✅

### 4. 数据文件 ✅

- 训练数据（`train_split.jsonl`）、评估数据（`eval_split.jsonl`、`eval_held_out.jsonl`）和校准数据（`calibration_v2_1_expanded.jsonl`）均已包含在仓库中
- 数据格式为 JSONL，每条包含 `pair_id`、`condition`、`domain`、`ground_truth`、`turns` 等字段，无身份信息

---

### 建议修复项

**README 需补充以下内容**（草拟如下）：

```markdown
## Quick Start

### 1. Environment Setup
```bash
pip install -r requirements.txt
```

### 2. Direction Extraction
```bash
python extract_activations.py --model_path ./models/Qwen3-8B --data_path ./data/calibration_v2_1_expanded.jsonl
python compute_directions.py
```

### 3. Training
```bash
# ACT + SFT (main method)
python training/run_exp004s2_act.py

# GRPO + R3 reward
python training/run_exp003_r3only.py
```

### 4. Evaluation
```bash
bash eval/run_exp003_unified_eval.sh
# or run LM-Eval benchmarks
bash eval/run_lm_eval.sh
```

## Data Format

Each JSONL entry contains:
- `pair_id`: unique sample identifier
- `condition`: `valid_correction` or `invalid_pressure`
- `domain`: subject area (e.g., math)
- `ground_truth`: correct answer
- `turns`: multi-turn dialogue as `[{role, content}, ...]`
```

需要我把这段补充内容写入本地 README 并推送到仓库吗？

---
