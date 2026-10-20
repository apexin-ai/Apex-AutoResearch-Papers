# code exp e qwen3 3shot prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-e-qwen3-3shot-prep_20260519T030100_result.json`
- **Structured JSON:** [`ab2fd1ee92f98e2f1ffe.json`](../../sessions/ab/ab2fd1ee92f98e2f1ffe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，数据加载正常（9784 test instances）。

## 总结

### 脚本兼容性
`eval_3shot_baseline.py` 已完全支持 Qwen3-8B，只需换 `--model_name_or_path`。已做一处修改：

**新增 `--disable_thinking` 参数**（L208-214, L332）：Qwen3-8B 默认启用 thinking mode，会在回答前输出 `&lt;think>...&lt;/think>`，`max_new_tokens=8` 不够用。修改后对 Qwen3 模型自动传 `enable_thinking=False` 给 chat template，跳过 thinking 直接输出 PASS/FAIL。

### Qwen3-8B 模型路径
`/root/autodl-tmp/models/Qwen/Qwen3-8B/`（5 个 safetensors 分片 + tokenizer 完整）

### 完整运行命令（待 GPU 释放）
```bash
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=&lt;GPU_ID> HF_HUB_OFFLINE=1 \
nohup /root/miniconda3/bin/python eval_3shot_baseline.py \
  --model_name_or_path /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --data_dir data/swebench_full \
  --device cuda:0 \
  --max_seq_length 4096 \
  --output_dir artifacts/eval_3shot_qwen3_8b \
  > ~/runs/exec-sim-repair-verifier/qwen3-8b-3shot-baseline.log 2>&1 &
```

### 预估运行时间
Qwen3-8B (~8B params) vs DeepSeek-coder-6.7B (~6.7B)：参数量大约 20%，但 5090 上推理很快。9784 samples，预估 **2-3 小时**（取决于 GPU 型号和 prompt 长度分布）。

### GPU 状态
4 个 GPU 全部在用，无法立即启动。需要等其中一个任务完成后再提交。

---
