# exp-010-mistral-v2 失败诊断

## 一句话总结

v2 进程在启动瞬间被外部 SIGTERM 杀死（GPU 被其他实验占用），且即使成功启动也会因 vLLM max_model_len=4096 bug 而全部 400 失败。

---

## 详细分析

### v2 直接死因：外部 SIGTERM（资源冲突）

- 日志内容仅 `Terminated\nEXIT_CODE=143\n`（25 字节），无任何脚本输出
- EXIT_CODE=143 = 128+15 = SIGTERM
- 时间线：
  - 12:47 pilot-constraint-filtering 启动（Qwen2.5-14B，port 8000）
  - 13:30 exp-018-arc 启动（复用同一 vLLM 实例，port 8000）
  - **13:51 exp-010-mistral-v2 被提交** → 立即被 kill
- 结论：GPU 已被 Qwen2.5-14B 占据，v2 需要加载 Mistral-7B 到同一 GPU，job 管理系统检测到冲突后立即发 SIGTERM

### v1 根因：vLLM max_model_len 被忽略

- 脚本传 `--max-model-len 8192`，但 vLLM 实际使用 4096
- 证据：`/tmp/vllm_exp010.log` 中 non-default args 显示 `'max_model_len': 4096`
- 请求 max_tokens=4096，导致 input_tokens + 4096 > 4096 → 所有请求 400
- 可能原因：
  - vLLM 0.20.2 + `vllm.entrypoints.openai.api_server`（旧入口）对 `--max-model-len` 参数处理异常
  - 或 GPU 内存不足时 vLLM 自动降到 4096（但 7B 模型 + 90% 利用率在 A6000 上应该够 8192）

### v1 结果（参考）

- 路径：`/root/symb_invariant_consensus/results/exp010_mistral/exp010_results.json`
- 处理了 26/60 个问题（全是 ProofWriter，FOLIO 未跑到）
- 准确率：SICA=0%, SC=0%（因为所有 trace 生成都 400 失败）
- **完全不可用**

---

## 部分结果可用性

**不可用。** v1 的 26 条结果全部是空壳（0 constraints, 0 votes, 0 answers）。v2 无任何结果。

---

## 是否值得重跑 & 修复建议

**值得重跑**，但需修复两个问题：

### 1. 确保 GPU 独占

- 提交前确认无其他 vLLM/模型占用 GPU
- 或使用不同 port 且 GPU memory 足够承载两个模型（不太现实，7B+14B）

### 2. 修复 max_model_len 问题

方案 A（推荐）：降低 max_tokens
```
--max-tokens 2048  # 而非 4096，确保 input+output < 4096
```

方案 B：强制 vLLM 使用 8192
```bash
# 使用新入口 vllm.serve（而非 vllm.entrypoints.openai.api_server）
python -m vllm.serve "$MODEL" --max-model-len 8192 ...
```

方案 C：修改模型 config
```bash
# 在 config.json 中设 "max_position_embeddings": 8192
# 然后 --max-model-len 8192 应该能生效
```

### 推荐方案

使用方案 A（`--max-tokens 2048`）最安全：
- Mistral-7B 对 ProofWriter/FOLIO 的推理链通常 < 1500 tokens
- 避免依赖 vLLM 对 max_model_len 的处理逻辑
- 同时在脚本中使用 `python -m vllm.serve`（新入口）并显式 `--max-model-len 8192`

### 重跑命令模板

```bash
# 确认 GPU 空闲
nvidia-smi

# 启动 vLLM（使用新入口）
python -m vllm.serve /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 \
  --port 8000 \
  --max-model-len 8192 \
  --gpu-memory-utilization 0.90 \
  --dtype auto

# 运行实验（max_tokens 降为 2048）
python3 run_full_mvp.py \
  --mode vllm --k 12 --temperature 0.7 \
  --max-tokens 2048 \
  --api-base "http://localhost:8000/v1" \
  --math-data data/empty.json \
  --pw-data data/proofwriter_30.json \
  --folio-data data/folio_30.json \
  --output results/exp010_mistral/exp010_v3_results.json \
  --save-intermediates --seed 42
```
