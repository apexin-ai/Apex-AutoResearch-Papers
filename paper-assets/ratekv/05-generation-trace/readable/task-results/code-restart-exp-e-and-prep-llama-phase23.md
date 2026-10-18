# code restart exp e and prep llama phase23

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_restart_exp_e_and_prep_llama_phase23_20260514T015725_result.json`
- **Structured JSON:** [`536f3a38e76b235e7539.json`](../../sessions/53/536f3a38e76b235e7539.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**exp_e Phase 2+3** 已在 cuda:1 上运行（tmux session `exp_e_phase23`）：
- Phase 2 solver 已完成：bit dist `{8: 4, 2: 8, 4: 100}`，memory ratio 0.2500
- Phase 3 模型已加载，正在跑 WikiText-2 PPL eval（baseline → MCKP → uniform 三组）
- 日志：`/root/ratekv/exp_e_phase23.log`
- 结果将保存到 `exp_e_hires_results.json`

**run_llama_phase23.py** 已写好部署到服务器，未启动。等 Llama profiling 完成后用：
```bash
tmux new-session -d -s llama_phase23 "CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_OFFLINE=1 python run_llama_phase23.py 2>&1 | tee llama_phase23.log"
```

---
