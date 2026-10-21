# code exp012 llama direction

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp012-llama-direction_20260520T035716_result.json`
- **Structured JSON:** [`3c3d7b3c2ee774a352e8.json`](../../sessions/3c/3c3d7b3c2ee774a352e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本部署成功，`--help` 和 `import` 验证均通过。

## 总结

**脚本** `run_exp012_llama_direction.py` 已写入 `/root/contrastive_entrain_calib/training/`（488 行），功能：

1. **加载数据** — 读取 `calibration_v2_1_expanded.jsonl`（181 pairs, 362 samples, 5 domains）
2. **提取 hidden states** — Llama-3-8B-Instruct 前向传播，`apply_chat_template` + `add_generation_prompt=True`，取 last-token position 的 L16-L31 层输出
3. **计算 d_syc** — `mean(invalid_pressure) - mean(valid_correction)`，L2 归一化
4. **5-fold stratified CV AUROC** — 按 domain 分层，每 fold 独立计算 d_syc
5. **Style-controlled AUROC** — pair 内比较（concordance），控制问题内容
6. **保存结果** — `directions.pt`、`activations.pt`、`evaluation_report.json`

**Llama-3-8B-Instruct 模型状态**：**未下载**。服务器只有 Qwen3-8B (`/root/autodl-tmp/modelscope_cache/Qwen/Qwen3-8B`)。需要下载模型后才能运行。建议用 ModelScope（AutoDL 下 HF 下载极慢）：

```bash
source /etc/network_turbo
pip install modelscope
python -c "from modelscope import snapshot_download; snapshot_download('LLM-Research/Meta-Llama-3-8B-Instruct', cache_dir='/root/autodl-tmp/models')"
```

模型约 16GB (bfloat16)，下载后用 `--model-path /root/autodl-tmp/models/Meta-Llama-3-8B-Instruct` 运行。RTX 5090 32GB 单卡够用。

---
