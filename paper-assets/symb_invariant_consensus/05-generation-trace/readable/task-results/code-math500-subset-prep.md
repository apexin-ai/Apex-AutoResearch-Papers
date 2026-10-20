# code math500 subset prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_math500-subset-prep_20260515T183555_result.json`
- **Structured JSON:** [`cf090b9ec5f38e756133.json`](../../sessions/cf/cf090b9ec5f38e756133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。汇报：

### 1. math500_subset.json 状态
- **已存在**，50 题，格式正确
- 字段：`id, problem, solution, answer, level`
- Level 分布：Level 1-5 各 10 道（分层抽样，seed=42）
- 生成脚本 `data/prepare_data.py` 从 `HuggingFaceH4/MATH-500` 加载

### 2. AIME 重叠检查
- AIME 2024 子集 30 题，MATH-500 子集 50 题，**零重叠**

### 3. 新增文件
- **`data/__init__.py`** — 使 `data/` 可作为 Python 包导入
- **`data/math500_loader.py`** — `load_math500_subset(path, levels, max_problems)` 接口，自动为每条记录补 `dataset="math"`，兼容 `run_full_mvp.py` 输入格式
- **`eval_math500.py`** — MATH-only 评估脚本，复用 run_full_mvp.py 核心逻辑（pipeline、SC baseline、is_equiv），支持 `--n-problems`, `--k`, `--temperature`, `--levels`, `--resume`, `--save-intermediates`

### 4. 后续步骤
- v3 实验完成后，运行 `python eval_math500.py --mode vllm --k 12 --temperature 0.7 --save-intermediates`
- 如需仅跑难题子集：`--levels 4 5`

---
