# analysis eval status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-status-check_20260514T190309_result.json`
- **Structured JSON:** [`7db1e4c912f677ef44dc.json`](../../sessions/7d/7db1e4c912f677ef44dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `artifacts/eval_status_check.md`。

**关键发现：**

1. **5 个 PID 全部存活**，4 张 GPU 满载，**cuda:2 未空闲**（正在跑 ckpt-10，92% 即将完成）

2. **唯一已完成的结果是 checkpoint-50**，指标很差：
   - F1=0.1563（SFT baseline 0.4057，下降 61%）
   - Evi-F1=0.5643（baseline 0.7979，下降 29%）
   - EDCR=0.8858（baseline 0.7118，提升 24%）
   - GRPO 训练在 step 50 严重损害了关系抽取能力，只换来 distractor citation 的改善

3. **近期将出结果**：ckpt-60（~33min）、step-100（~30min）、step-90（~53min）

4. **multi batch_eval 还需 ~6 小时**完成剩余 checkpoints（20,30,40,70,80）

5. **两个早期任务失败**（last, ckpt90），原因是 `No module named freige.eval.batch_eval`，已被后续正确的任务替代

6. **Step 90 状态**：PID 83207 在 GPU 1 上运行中（35%），约 53 分钟后出结果

---
