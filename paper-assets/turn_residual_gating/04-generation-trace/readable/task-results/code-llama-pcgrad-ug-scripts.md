# code llama pcgrad ug scripts

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_pcgrad_ug_scripts_20260522T233436_result.json`
- **Structured JSON:** [`7820ecfa297b9a8c3971.json`](../../sessions/78/7820ecfa297b9a8c3971.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本已创建，语法检查通过，所有路径验证正确。

### 产出

| 脚本 | 路径 | 训练命令 | 预估时间 |
|------|------|---------|---------|
| **PCGrad** | `scripts/d048_llama_pcgrad.sh` | `train_phase2_v9_pcgrad.py` + Llama + threadgate | ~3h |
| **UG** | `scripts/d048_llama_ug.sh` | `train_phase2.py` + Llama + `--gate-type uniform` | ~2.5h |
| **5-way Eval** | `scripts/d048_llama_eval_all.sh` | TF(`eval_phase2_gar.py`) + AR(`eval_attention_steering.py --mode gen`) + Bootstrap CI | ~2-3h |

### 超参统一（D048 协议）
- lr=2e-4, batch_size=1, grad_accum=8, max_seq_len=2048, epochs=3, seed=42
- gar-target=0.5, init-bias=1.5, gate-lr-multiplier=10（与现有 Llama TG/LO 一致）

### Checkpoint 路径
- TG: `runs/phase2_llama_tg_s42/epoch_2` ✓ 存在
- LO: `runs/phase2_llama_lora_only_s42/epoch_2` ✓ 存在
- UG: `runs/phase2_llama_ug_s42/epoch_2` — 训练后生成
- PCGrad: `runs/phase2_llama_pcgrad_s42/epoch_2` — 训练后生成

### Eval 脚本特点
- `set +e` 避免单个条件失败中断全部
- 自动跳过缺失 checkpoint 的条件（先训完 UG/PCGrad 再跑 eval）
- Bootstrap CI 取 `curve[2:]`，1000 次重采样，输出到 `results/d048_llama_eval/bootstrap_ci.json`

---
