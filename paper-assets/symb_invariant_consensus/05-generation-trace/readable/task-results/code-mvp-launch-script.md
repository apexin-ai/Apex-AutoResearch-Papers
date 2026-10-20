# code mvp launch script

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-launch-script_20260515T110631_result.json`
- **Structured JSON:** [`7022ad00aeb132e3334e.json`](../../sessions/70/7022ad00aeb132e3334e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出汇总：

**服务器文件**（westd-32608:/root/symb_invariant_consensus/）：
- `run_full_mvp.py` — 60 题完整 MVP 实验脚本
- `launch_mvp.sh` — 一键启动脚本

**功能**：
- 合并加载 50 MATH-500 + 10 ProofWriter（共 60 题）
- SICA pipeline（K=12）+ SC baseline 对比
- `is_equiv` 等价判定（math_verify → sympy → numeric fallback）
- 断点续传：`--resume` 自动跳过已完成题目
- 每题实时打印进度、约束统计、MaxSAT 结果
- ETA 估算（基于滑动平均耗时）
- 每题完成后自动保存 checkpoint 到 `results/mvp_full_results.json`
- 输出指标：总体 accuracy、按数据集分（MATH/ProofWriter）、按难度分（Level 1-5）

**验证结果**：
- Python 语法 OK
- Import OK（所有依赖可解析）
- Shell 语法 OK
- Mock 模式 60 题端到端通过
- Resume 功能正常（检测已完成题目并跳过）

**启动方式**：Smoke test 通过后，执行 `bash launch_mvp.sh`（或 `bash launch_mvp.sh --resume` 断点续传）。

---
