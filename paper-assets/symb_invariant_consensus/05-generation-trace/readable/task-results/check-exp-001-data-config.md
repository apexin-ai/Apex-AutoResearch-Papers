# check exp 001 data config

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp-001-data-config_20260516T084325_result.json`
- **Structured JSON:** [`b641b80e2c6299d76158.json`](../../sessions/b6/b641b80e2c6299d76158.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 实际总题数配置：**804**

启动命令（无 `--resume`，全新运行）：
```
python run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 \
  --math-data /tmp/empty_math.json \
  --pw-data data/proofwriter_full.json \
  --folio-data data/folio_full.json \
  --output results/sica_expanded_14b.json --save-intermediates --seed 42
```

数据文件：
- `/tmp/empty_math.json` → `[]`（0 题）
- `data/proofwriter_full.json` → **600 题**（全部 D5-OWA）
- `data/folio_full.json` → **204 题**

Registry 记录的 804 题是正确的。

### 2. 当前进度：**195/804 完成，全部是 ProofWriter**

- `problem_idx` 0 → 194，共 195 条结果
- 全部 dataset="proofwriter"，level="D5"
- **不包含任何 D012 legacy 数据**——grep "folio" 在结果文件中返回 0 匹配，所有 problem_id 格式均为 `ProofWriter_*-OWA-D5-*`
- 启动时未使用 `--resume`，结果文件创建于 `2026-05-16 13:16:01`（全新）

Reviewer 之前看到的 "162 条 PW 结果" 是更早时间点的快照（problem_idx 0-161），目前已推进到 195 条。

### 3. FOLIO 部分何时开始

脚本加载顺序：MATH → PW → FOLIO（顺序拼接）。FOLIO 从 **problem_idx 600** 开始（即 PW 600 题全部跑完之后）。

### 4. ETA

- 已完成 195 题，总耗时 12,456s → **~64s/题**
- 剩余 609 题 × 64s ≈ **38,976s ≈ 10.8 小时**
- 预计 FOLIO 开始时间：还需跑完 405 题 PW ≈ 7.2h（约明天凌晨 ~00:00）
- 预计全部完成：约明天上午 ~03:30（+0800）

### 关于 "加载 140 题" 的疑问

Reviewer 看到的 "loaded 140 (70 PW + 70 FOLIO)" **不是** exp-001 的日志。exp-001 启动时应输出 "Loaded 600 ProofWriter problems" + "Loaded 204 FOLIO problems" + "Total: 804 problems"。那条 140 题的日志可能来自之前的 `sica_d012_14b` 或其他小规模测试 run。

---
