# analysis v3 status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v3-status-check_20260515T185626_result.json`
- **Structured JSON:** [`2fae566e79080ff2fb3e.json`](../../sessions/2f/2fae566e79080ff2fb3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v2 实验状态（⚠️ 无 v3 实验）

**不存在 v3 实验。** 服务器上没有任何 v3 相关文件。运行中的进程（PID 129992）输出到 `aime30_v2.json`。

**进程状态**: 仍在运行，已运行 3h04m，`--resume` 模式
```
python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 10240 --math-data data/aime2024_subset.json --output results/aime30_v2.json --no-proofwriter --resume
```

**进度**: 已完成 **20/30** 题（aime2024_II_01~II_15 + I_01~I_05），剩余 10 题

**预估剩余时间**: 平均 ~535s/题 × 10 = ~89 分钟 ≈ **1.5 小时**

---

### 当前结果（20 题）

| 指标 | SICA | SC@K=12 |
|------|------|---------|
| Accuracy | **14/20 (70%)** | **14/20 (70%)** |

两种方法在已完成的 20 题上结果完全一致。

### 逐题对比

| # | Problem | GT | SICA | SC | SC Votes | Raw→Unique→Sat/Excl | 备注 |
|---|---------|-----|------|-----|----------|---------------------|------|
| 0 | II_01 | 73 | 73 ✓ | 73 ✓ | **12**/12 | 56→33→28/5 | |
| 1 | II_02 | 236 | ✗ | ✗ | **0**/12 | 0→0→0/0 | 截断：无约束提取 |
| 2 | II_03 | 45 | 45 ✓ | 45 ✓ | **11**/12 | 51→18→18/0 | |
| 3 | II_04 | 33 | 33 ✓ | 33 ✓ | **12**/12 | 20→5→4/1 | |
| 4 | II_05 | 80 | 80 ✓ | 80 ✓ | **1**/12 | 47→42→2/40 | ⚠️ 极低共识但正确；95%约束被排除 |
| 5 | II_06 | 55 | 55 ✓ | 55 ✓ | **12**/12 | 13→0→0/0 | 约束全部去重为0 |
| 6 | II_07 | 699 | 699 ✓ | 699 ✓ | **1**/12 | 72→1→1/0 | ⚠️ 极低共识但正确；72→1去重 |
| 7 | II_08 | 127 | ✗ | ✗ | **0**/12 | 26→6→4/2 | 截断 |
| 8 | II_09 | 902 | ✗ | ✗ | **0**/12 | 35→14→14/0 | 截断 |
| 9 | II_10 | 468 | 468 ✓ | 468 ✓ | **7**/12 | 70→30→9/21 | ⚠️ 低共识 |
| 10 | II_11 | 601 | ✗ | ✗ | **0**/12 | 60→12→0/12 | 截断：约束全被排除 |
| 11 | II_12 | 23 | 23 ✓ | 23 ✓ | **8**/12 | 49→8→0/8 | |
| 12 | II_13 | 321 | 321 ✓ | 321 ✓ | **10**/12 | 27→16→0/16 | |
| 13 | II_14 | 211 | ✗ | ✗ | **0**/12 | 100→33→33/0 | 截断：有约束但无答案 |
| 14 | II_15 | 315 | ✗ | ✗ | **0**/12 | 22→11→11/0 | 截断 |
| 15 | I_01 | 204 | 204 ✓ | 204 ✓ | **12**/12 | 59→15→14/1 | |
| 16 | I_02 | 25 | 25 ✓ | 25 ✓ | **11**/12 | 64→11→0/11 | |
| 17 | I_03 | 809 | 809 ✓ | 809 ✓ | **12**/12 | 8→0→0/0 | |
| 18 | I_04 | 116 | 116 ✓ | 116 ✓ | **12**/12 | 33→16→16/0 | |
| 19 | I_05 | 104 | 104 ✓ | 104 ✓ | **4**/12 | 35→19→17/2 | ⚠️ 低共识但正确 |

### 低共识题（SC < 8/12）

| Problem | SC Votes | 正确? | 特征 |
|---------|----------|-------|------|
| II_05 | 1/12 | ✓ | 42 unique 约束中 40 被排除，SICA 依靠仅 2 条约束选对 |
| II_07 | 1/12 | ✓ | 72 raw 约束去重后仅剩 1 条 |
| II_10 | 7/12 | ✓ | 30 unique 中 21 被排除 |
| I_05 | 4/12 | ✓ | 正常约束分布 |

### 截断/失败题（0 votes，无答案）

共 **6 题**（II_02, II_08, II_09, II_11, II_14, II_15），全部 SICA 和 SC 同时失败。

- II_02: 零约束提取，trace 生成完全失败
- II_11: 有 60 raw 约束但 unique 12 条全被排除
- II_14: 有 100 raw→33 unique→33 satisfied，约束正常但无法产出答案（可能 candidate 为空）
- 其余题约束数正常但答案为空

### 关键观察

1. **SICA = SC**：在已完成 20 题上两者准确率完全一致，SICA 没有提供额外增益
2. **失败模式统一**：6 题截断全是两种方法同时失败，说明瓶颈在 trace 质量而非聚合方法
3. **低共识不等于错误**：4 题 SC votes ≤ 7 但全部正确，说明 SICA 在低共识场景可能更稳健（待验证）
4. **约束排除率高**：II_05 排除 40/42，II_10 排除 21/30，MaxSAT 大量排除约束

---
