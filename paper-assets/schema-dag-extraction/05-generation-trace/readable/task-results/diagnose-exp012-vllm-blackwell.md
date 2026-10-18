# diagnose exp012 vllm blackwell

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp012_vllm_blackwell_20260515T171340_result.json`
- **Structured JSON:** [`f0c541f006dc88f936d8.json`](../../sessions/f0/f0c541f006dc88f936d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Step 3b 也完全通过！** Structured JSON output 正常：

```json
[{"text": "John", "type": "person"}, {"text": "Google", "type": "organization"}]
```

---

## 诊断结论

**vLLM + LLaMA-3.1-8B 在 Blackwell SM120 上完全可用。** 三项测试全部通过：
1. 最小化测试 ✅
2. Chat template ✅  
3. Structured JSON output (guided decoding) ✅

**SIGKILL 的真正原因不是兼容性问题，而是 GPU 显存被占用**：

exp012_llama_8b.log 显示启动时 GPU 只剩 7.01 GiB / 94.97 GiB（88GB 被其他进程占了），vLLM 要求 85.48 GiB (90% utilization) 分配失败 → `ValueError`。

另外，**cgroup 内存限制 = 120GB**（`free -h` 显示的 1TB 是宿主机），当前已用 ~100GB（主要是 page cache）。这可能在某些场景下导致 CPU 端 OOM 被 SIGKILL。

### 可行配置（已验证）

```bash
# 确保 GPU 无残留进程
nvidia-smi  # 确认 0MiB 占用

# 运行实验
FLASHINFER_DISABLE_VERSION_CHECK=1 python3 src/run_experiment.py \
  --mode exp1 \
  --dataset fewnerd \
  --prompt_version v2 \
  --model_path /root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --gpu_memory_utilization 0.85 \
  --max_model_len 4096 \
  --enforce_eager \
  ...其他参数
```

### 建议修复

1. **运行前必须检查 GPU 占用**：在 `run_exp012_llama_8b.sh` 开头加 `nvidia-smi` 检查，确认 GPU 空闲
2. **降低 gpu_memory_utilization**: 从 0.90 降到 0.85，留更多余量
3. **脚本中 exp1 和 exp2 串行时**，确保 exp1 的 vLLM 进程完全退出后再启动 exp2（Python 进程退出后 GPU 显存应自动释放，但建议加 `sleep 5` 或检查 `nvidia-smi`）
4. **注意模型路径**：脚本用的是 `Meta-Llama-3___1-8B-Instruct`（下划线），实际目录同时存在 `Meta-Llama-3.1-8B-Instruct`（点号），两者都有效但要保持一致

---
