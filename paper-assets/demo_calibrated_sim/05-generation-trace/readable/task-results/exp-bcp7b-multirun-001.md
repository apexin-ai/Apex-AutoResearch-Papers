# exp bcp7b multirun 001

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_bcp7b-multirun-001_20260513T154104_result.json`
- **Structured JSON:** [`fa3f3842d700351412bb.json`](../../sessions/fa/fa3f3842d700351412bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功提交并启动，vLLM 正在加载模型。

**执行摘要：**
- 杀掉了空闲的 14B vLLM server（GPU 2/3），释放 GPU 2
- 创建 `/root/democalib/run_bcp7b_multirun.sh`：启动 7B vLLM → 运行 3 轮 BCP eval（每轮 6 variants × 20 tasks）→ 聚合结果
- 通过 `submit_training_job` 提交到 cuda:2，exp_id=`bcp7b-multirun-001`，timeout 6h
- Registry 已更新：status=RUNNING, parent=mvp-004, hypothesis 已填写
- 日志：`~/runs/demo_calibrated_sim/bcp7b-multirun-001.log`
- 结果目录：`/root/democalib/results/bcp7b_multirun/`

注意：`run_mvp_experiment.py` 没有 seed 参数，tau-bench 的随机性来自 LLM 采样本身，3 次独立运行即可产生不同结果。

---
