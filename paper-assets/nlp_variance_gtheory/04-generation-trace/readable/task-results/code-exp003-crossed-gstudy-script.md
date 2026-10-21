# code exp003 crossed gstudy script

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp003_crossed_gstudy_script_20260522T070830_result.json`
- **Structured JSON:** [`e29fe45b980d41292514.json`](../../sessions/e2/e29fe45b980d41292514.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成汇报

### Part 1: 脚本

`scripts/exp003_scale_crossed_gstudy.py` 已写入服务器。

**2-model 测试结果（3B + 7B，115,200 records）**:

| 指标 | 值 | 说明 |
|------|-----|------|
| Pct sum | 100.00% | ✓ |
| D-study | 单调递增 | ✓ (0.236 → 0.861) |
| G_item | 0.712 | ✓ 合理范围 |

Top variance components:
- item_id: 43.53%
- model:item_id: 31.74%
- residual: 15.93%
- item_related total: 83.28%

代码验证通过。72B 数据到手后运行 `python scripts/exp003_scale_crossed_gstudy.py`（不加 `--test`）即可。

### Part 2: 72B 下载进度

| 指标 | 状态 |
|------|------|
| 进程 | PID 229326 运行中 |
| Watchdog | PID 232345 运行中 |
| 已完成 | 7/37 safetensors (model-00001~00007) |
| 进行中 | 8 个文件并行下载 (model-00008~00015) |
| 已下载 | ~26GB 完成 + ~14GB 部分 ≈ 40GB / ~133GB |
| 进度 | **~30%** |
| 速度 | ~400KB/s × 8 streams ≈ 3.2 MB/s |
| 预估剩余 | **~7-8 小时** |
| 磁盘 | 122GB 可用（足够，133-40=93GB 需下载）|

---
