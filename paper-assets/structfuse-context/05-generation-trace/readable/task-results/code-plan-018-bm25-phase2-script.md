# code plan 018 bm25 phase2 script

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_018_bm25_phase2_script_20260514T175227_result.json`
- **Structured JSON:** [`299a1dca5299c3ae0bef.json`](../../sessions/29/299a1dca5299c3ae0bef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报结果：

---

### 已完成

**1. 代码修改**（支持 bm25 策略）
- `training/train.py` L586: `choices` 添加 `"bm25"`
- `training/hard_negative_mining.py` `build_miner()`: 添加 `"bm25": RandomMiner`（BM25 negatives 已预挖掘在数据文件中，不需要动态挖掘）

**2. 创建的脚本**
- `/root/structfuse/scripts/run_m2_full_bm25_qwen.sh` — Qwen2.5-Coder-3B
- `/root/structfuse/scripts/run_m2_full_bm25_starcoder.sh` — StarCoder2-3B（**模型尚未下载**）

**3. 与现有脚本的差异**
- 数据路径: `train_bm25_s{seed}.jsonl` / `val_bm25_s{seed}.jsonl`
- 输出路径: `full_m2_outputs/bm25_s{seed}/`（Qwen）、`full_m2_outputs/bm25_starcoder_s{seed}/`（StarCoder）
- Epoch 配置: s42=3 epochs（无 early stopping），s43/s44=2 epochs + patience=2（现有脚本统一用 2 epochs + patience=3）
- 其他参数完全一致: batch=8, lr=2e-5, lora_r=16, proj_dim=256, temp=0.07, num_neg=7, max_seq=2048, eval_steps=500

**4. dry-run 验证**
- `bash -n` 语法检查: 两个脚本均通过
- `parse_args` 参数解析: bm25 策略正确识别
- `build_miner("bm25")`: 正常实例化为 RandomMiner
- 数据文件: 3 seeds × ~11.3K samples，路径均存在

**5. 预估单 seed 训练时间**
- 数据量与 random/embedding/dataflow 一致（~11K samples）
- s42（3 epochs）: 预估 ~2-3 小时
- s43/s44（2 epochs）: 预估 ~1.5-2 小时
- Qwen 全部 3 seeds 串行: ~5-8 小时

**6. 注意事项**
- StarCoder2-3B 模型不在服务器上（`/root/autodl-tmp/structfuse/models/` 只有 Qwen），脚本会检测并报错提示下载
- Qwen 脚本可直接启动: `nohup bash /root/structfuse/scripts/run_m2_full_bm25_qwen.sh 0 > /root/autodl-tmp/structfuse/full_m2_outputs/bm25_qwen_schedule.log 2>&1 &`

---
