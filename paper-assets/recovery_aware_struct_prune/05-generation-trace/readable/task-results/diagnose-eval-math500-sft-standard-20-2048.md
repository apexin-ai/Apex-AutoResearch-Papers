# diagnose eval math500 sft standard 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_standard_20_2048_20260518T225058_result.json`
- **Structured JSON:** [`228169abb5f318e16579.json`](../../sessions/22/228169abb5f318e16579.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，所有证据已收集。

## 诊断报告

### 根因：**进程未在 tmux 中运行，SSH 会话断开后被 SIGHUP 杀死**

### 关键证据

1. **日志无错误信息**：日志在 problem 10/500 处干净截断（06:37），无 Traceback、OOM、CUDA error。进程被外部信号杀死。

2. **无 tmux 会话保护**：当前服务器上 4 个存活的实验**全部在 tmux 中运行**：
   - `eval_math500_dense_2048` → GPU 0 (PID 32469)
   - `eval_math500_v2` → GPU 1 (PID 22049)
   - `rasp_grpo_eval` → GPU 3 (PID 21100)
   - `sft_standard_20_retrain_westd` → GPU 2 (PID 34346)
   
   唯独失败的 `eval_math500_sft_standard_20` **没有对应的 tmux 会话**。

3. **资源充足，排除 OOM/磁盘**：
   - GPU 2: RTX PRO 6000 97GB，模型仅 ~12GB，显存充足
   - 系统内存：1TB 中仅用 31GB
   - 磁盘：/root/autodl-tmp 71GB 可用
   - dmesg 无权限，但系统资源指标全部正常

4. **时间线还原**：
   - 06:18 — eval 启动，加载模型
   - 06:21 — 数据集加载完成，开始评测（~95s/problem）
   - 06:37 — 完成 10/500 后进程死亡（日志停止）
   - 06:40 — SFT retrain 在 **tmux 中** 启动于 cuda:2（填补空出的 GPU）

5. **脚本无超时机制**：`eval_math500.py` 无 timeout/signal 处理代码。

### 已完成的部分结果

- 10/500 problems 已处理
- 无中间 accuracy 记录（脚本只在完成所有 500 题后输出 accuracy）
- 无 JSON 输出文件（结果只在全部完成后写入）
- 平均每题 ~95s，预计全部 500 题需 ~13 小时

### 修复建议

重新运行时**必须使用 tmux**：

```bash
tmux new-session -d -s eval_sft_standard_20_2048 \
  "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
   cd /root/recovery_aware_struct_prune && \
   CUDA_VISIBLE_DEVICES=2 python src/eval_math500.py \
     --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20 \
     --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_standard_20_2048.json \
     --max_new_tokens 2048 \
     2>&1 | tee /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_standard_20_2048.log"
```

注意：cuda:2 当前正在运行 SFT retrain（PID 34346, 51GB VRAM），需等其完成后再启动 eval。

---
