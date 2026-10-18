# ssh exp004 maven launch

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp004-maven-launch_20260515T060057_result.json`
- **Structured JSON:** [`7859eeaf3c05dd72acd8.json`](../../sessions/78/7859eeaf3c05dd72acd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并验证成功。

---

**汇总：**

1. **命令全文**（exp1 + exp2 串行）：
   ```
   source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export CUDA_VISIBLE_DEVICES=0 && cd /root/schema-dag-extraction && 
   python3 src/run_experiment.py --dataset maven --mode exp1 --prompt_version v2 --eval_mode text_match --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ --max_samples 500 --embeddings_path artifacts/maven_type_embeddings_qwen3.pt --sim_matrix_path artifacts/maven_bcs_matrix_qwen3.pt --types_file configs/maven_event_types.json --output_dir artifacts/exp004 &&
   python3 src/run_experiment.py --dataset maven --mode exp2 ...（同上参数，mode=exp2）
   ```

2. **PID**: 224685 | tmux session: `exp004_maven_bcs`

3. **预估运行时间**：
   - exp1: 149 solo batches (count=1) + 6×5=30 random batches = ~179 batches × 500 samples。count=1 的 solo 推理快（短 prompt），大 count 的 prompt 长。预估 **3-5 小时**
   - exp2: 2 counts × 27 batches = 54 batches × 500 samples。预估 **2-3 小时**
   - 总计约 **5-8 小时**

4. **代码修改**：`src/run_experiment.py` — 在 batch config 构建前添加 dataset-specific count levels：
   - MAVEN: exp1=`[1,6,12,24,42,84,168]`, exp2=`[12,24]`
   - Few-NERD（不变）: exp1=`[1,2,6,12,22,44,66]`, exp2=`[6,12]`
   - 实际 active types = 149（500 samples 中只出现 149/168 种 event type）

---
