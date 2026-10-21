# code prep next batch

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-next-batch_20260517T135248_result.json`
- **Structured JSON:** [`ce15990d4ea005e3eb69.json`](../../sessions/ce/ce15990d4ea005e3eb69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已完全就位，验证结果：

**exp-012 GSM8K (`scripts/run_exp012_gsm8k.sh`)**:
- 语法 OK
- 数据: `data/gsm8k_200.json` (130KB, 200题) 已存在
- 入口: `scripts/run_gsm8k_pilot.py --n-problems 30` (取前30题)
- 模型: Qwen2.5-14B-Instruct 已在 `/root/autodl-tmp/models/`
- 输出: `results/exp012_gsm8k/`
- 参数: K=12, T=0.7, seed=42

**exp-004 Qwen-7B (`scripts/run_exp004_qwen7b.sh`)**:
- 语法 OK
- 数据: `proofwriter_30.json` + `folio_30.json` 已存在
- 入口: `run_full_mvp.py`，`--math-data data/empty.json`（跳过 MATH 题）
- 模型: **Qwen2.5-7B-Instruct 未下载** — 脚本已含自动下载逻辑（modelscope `snapshot_download`），首次运行时自动拉取 (~14GB，约10-15分钟)
- 输出: `results/exp004_qwen7b/`
- 参数: K=12, T=0.7, max-model-len=8192, seed=42

**结论**: 两个脚本已完整准备好，语法正确，数据文件就位。GPU 空出后可直接顺序执行：
```bash
bash scripts/run_exp012_gsm8k.sh   # ~1h (14B 已在本地)
bash scripts/run_exp004_qwen7b.sh  # ~2h (含首次模型下载)
```

唯一注意：exp-004 的 7B 模型需要首次下载。如果想提前下载以节省 GPU 占用时间，可以现在就运行模型下载（不需要 GPU）。是否现在预下载 7B 模型？

---
