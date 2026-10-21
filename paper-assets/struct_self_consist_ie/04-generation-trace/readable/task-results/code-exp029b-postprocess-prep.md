# code exp029b postprocess prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp029b_postprocess_prep_20260518T020017_result.json`
- **Structured JSON:** [`f0e525a8e2cdf1ac4453.json`](../../sessions/f0/f0e525a8e2cdf1ac4453.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有脚本已创建完成。训练进度 540/1170 (46%), 剩余约 31 分钟。

已创建的文件：

| 文件 | 说明 |
|------|------|
| `export_config_scierc_10epoch.yaml` | LlamaFactory merge 配置 |
| `scripts/exp_029b_postprocess/01_merge_lora.sh` | LoRA → merged model |
| `scripts/exp_029b_postprocess/02_inference.sh` | vLLM N=8 T=1.0 logprobs, `CUDA_VISIBLE_DEVICES=0` |
| `scripts/exp_029b_postprocess/03_analyze.py` | 分析脚本，动态从 `exp_029a analysis_results.json` 读取 3-epoch 和 5-epoch baseline |
| `scripts/exp_029b_postprocess/run_all.sh` | 串行执行 1→2→3 |

与 exp_029a 的关键差异：
- 路径全部从 `3epoch` → `10epoch`
- **baseline 不再硬编码** — 从 `exp_029a_scierc_3epoch/analysis_results.json` 动态加载 3-epoch 指标和内嵌的 5-epoch reference
- 对比表从 2 列扩展为 3 列（5-epoch / 3-epoch / 10-epoch），同时显示 vs 5ep 和 vs 3ep delta
- 结论逻辑改为检测单调性：10ep > 5ep > 3ep → CONFIRMED

训练完成后执行：
```bash
bash /root/autodl-tmp/struct_self_consist_ie/scripts/exp_029b_postprocess/run_all.sh
```

---
