# train plan017 mlm control

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan017-mlm-control_20260518T050320_result.json`
- **Structured JSON:** [`d4e48b82dee33b4bbb3d.json`](../../sessions/d4/d4e48b82dee33b4bbb3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器 westd-33183 持续无法连接（port 33183 on 36.103.198.204 不可达）。这个中断已持续较长时间。

**已完成的工作：**

1. **两个脚本已成功写入服务器**（在连接断开前完成）：
   - `src/train_deberta_mlm.py` — Stage 1 MLM 训练（DebertaV2ForMaskedLM, 15% masking, 4 epochs, lr=2e-5）
   - `src/plan_017_dd_eval.py` — Stage 2+3: 加载 MLM encoder → 提取 CLS embeddings → 训练 BiGRU → 评估 DD OOD (K=1,2,3,5,full) + IID

2. **MLM 训练已用 nohup 启动**（PID 198446, CUDA_VISIBLE_DEVICES=1），但无法确认是否成功运行（连接在启动后立即断开）

**恢复连接后需要做的：**

1. 检查训练日志：`cat logs/plan_017_mlm_train.log`
2. 如果 MLM 训练失败或未启动，重新运行：
   ```bash
   cd /root/persuasion_turn_jailbreak_detect
   source /root/miniconda3/bin/activate
   CUDA_VISIBLE_DEVICES=1 python src/train_deberta_mlm.py 2>&1 | tee logs/plan_017_mlm_train.log
   ```
3. MLM 训练完成后，运行评估：
   ```bash
   CUDA_VISIBLE_DEVICES=1 python src/plan_017_dd_eval.py 2>&1 | tee logs/plan_017_dd_eval.log
   ```
4. 结果将保存到 `results/plan_017_mlm_control.json`

---
