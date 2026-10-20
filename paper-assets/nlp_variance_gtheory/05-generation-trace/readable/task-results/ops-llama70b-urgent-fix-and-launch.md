# ops llama70b urgent fix and launch

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama70b_urgent_fix_and_launch_20260523T152243_result.json`
- **Structured JSON:** [`76b3e8becb8676e3091f.json`](../../sessions/76/76b3e8becb8676e3091f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有找到 `submit_training_job` 工具。按用户指示，不自行启动，将命令写在报告中。

---

## 报告

### 1. Kill 结果
| PID | 状态 | 说明 |
|-----|------|------|
| 313232 | ✅ KILLED | 多余下载进程 |
| 318664 | ✅ KILLED | 多余下载进程 |
| 188816 | ✅ KILLED | 无关遗留进程 |
| 318453 | ✅ 存活 | 保留的下载进程（带 ignore_file_pattern），运行 4h22m 后完成全部下载 |

### 2. Safetensors 分片
**30/30 完成。** Kill 多余进程后带宽集中，shard 27 在 Step 1 完成后几乎立即下载完毕。

### 3. 磁盘清理
- 删除 `original/` (.pth 文件) + `._____temp/`
- **释放 ~132GB**（276G → 144G used，207G available）
- 模型目录大小：128G（30 个 safetensors）

### 4. Symlink 验证
```
/root/autodl-tmp/models/Llama-3.1-70B-Instruct -> /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-70B-Instruct
```
- 30/30 safetensors 可通过 symlink 访问 ✓

### 5. 推理脚本验证
- 路径：`/root/nlp_variance_gtheory/scripts/exp_llama70b/run_llama70b_inference.py`
- `MODEL_PATH = "/root/autodl-tmp/models/Llama-3.1-70B-Instruct"` ✓
- `TENSOR_PARALLEL = 4` ✓
- `config.json`: model_type=llama, hidden=8192, layers=80 ✓
- 5 benchmarks × 288 conditions × 200 items = 288,000 evaluations

### 6. 启动命令（供 submit_training_job 提交）
```
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/nlp_variance_gtheory && python scripts/exp_llama70b/run_llama70b_inference.py
```

### 7. 失败项
无。所有步骤均成功。

---
