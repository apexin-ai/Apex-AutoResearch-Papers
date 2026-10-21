# eval check gradient postsft and fill westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check_gradient_postsft_and_fill_westb_20260517T112307_result.json`
- **Structured JSON:** [`e288148683b0e3d27636.json`](../../sessions/e2/e288148683b0e3d27636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. eval_gradient_postsft 结果

| 指标 | 值 |
|---|---|
| **GSM8K Accuracy** | **61.5% ± 3.4%** (123/200) |
| EOS rate | 99.5% |
| Avg response length | 167 tokens |
| 结论 | **success** |

Hypothesis 验证：Pre-SFT 25.5% → Post-SFT **61.5%**。Gradient scoring 经 SFT 恢复后与 RASP (~61%) **持平**，而非预期的更弱。这说明 gradient scoring 造成的损伤是可逆的，SFT 可以充分恢复。

Registry 已更新为 DONE/success。

### 2. westb GPU 状态

| GPU | 进程 | 占用 | 用途 |
|---|---|---|---|
| cuda:0 | PID 704557 | 50.4GB / 97.9GB, 52% util | `sft_recovery.py` — random pruned model SFT |
| cuda:1 | PID 707938 | 12.6GB / 97.9GB, 80% util | `eval_gsm8k.py` — random pruned model post-prune eval |

**两张 GPU 均被占用**，正在跑 scoring ablation（random method 阶段）。当前不可用于新实验。

### 3. scoring ablation 代码

- **`run_scoring_ablation.sh`** 和 **`run_scoring_ablation_continue.sh`** 已存在，覆盖 4 个 method: `magnitude`, `gradient`, `random`, `cka_only`
- **`prune.py`** 的 `--mode` 参数支持 7 种 scoring: `standard`, `rasp`, `rasp-rlvr`, `magnitude`, `gradient`, `random`, `cka_only`
- `magnitude` scoring ablation 已包含在现有脚本流程中（正在运行），**不需要额外准备代码**

如果需要跑额外的 magnitude ablation 实验（不同 sparsity 或参数），需要等当前 scoring ablation 完成后释放 GPU。

---
