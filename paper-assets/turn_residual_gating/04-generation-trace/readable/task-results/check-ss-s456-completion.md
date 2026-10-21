# check ss s456 completion

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ss_s456_completion_20260524T003601_result.json`
- **Structured JSON:** [`8a53df8b692f3a1851dd.json`](../../sessions/8a/8a53df8b692f3a1851dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## 状态汇总

### 1. SS s456 训练：**成功完成**
- PID 112418 已退出
- 3 个 epoch checkpoint 均已生成（`epoch_0`, `epoch_1`, `epoch_2`），`adapter_model.safetensors` (19.3MB) + `gate_params.pt` (3.3MB)
- 训练耗时 23515 秒（~6.5 小时），3000 步
- SS 使用统计：4747/16000 样本触发了 scheduled sampling，0 fallback

### 2. GPU chain 当前步骤：**Step 3/7 — SS s456 eval**
- PID 108997 (`gpu_chain_next.sh`) 运行中（7h12m）
- 已完成：Step 1 (SS s123 eval) → Step 2 (SS s456 训练) → **正在执行 Step 3**
- 当前 GPU 进程：PID 129280 `eval_attention_steering.py`（SS s456 AR eval，刚启动约1分钟）
- TF eval 已完成：`tf_ss_s456_ours/` 和 `tf_ss_s456_dongre/` 已生成
- AR eval 正在跑中（beta=0,3,5, N=50）
- GPU 占用：21GB / 98GB，利用率 66%

### 3. post_chain_queue.sh (PID 119240)：**等待中**
- 运行 4h02m，仍在等 gpu_chain 结束（每 60s 轮询一次）

### 4. 剩余 chain 步骤
Step 3 完成后还有 4 步：
- Step 4: Qwen-1.5B Phase 1 diagnostic
- Step 5: Qwen-1.5B TG training
- Step 6: Qwen-1.5B eval
- Step 7: MMLU eval (6 checkpoints)

一切正常运行，无需干预。

---
