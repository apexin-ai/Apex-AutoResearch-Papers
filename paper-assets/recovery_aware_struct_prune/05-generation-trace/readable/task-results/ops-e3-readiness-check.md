# ops e3 readiness check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_e3_readiness_check_20260518T153606_result.json`
- **Structured JSON:** [`a80f17863e1e74dcbc13.json`](../../sessions/a8/a80f17863e1e74dcbc13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
| GPU | 进程 | 进度 | 预计剩余 |
|-----|------|------|----------|
| cuda:0 | 1.5B CKA-only GRPO (`train_grpo_v5.py`) | 85/100 | ~29 min |
| cuda:1 | 1.5B RASP GRPO (`train_grpo_v5.py`) | 38/100 | ~33 min |

两块 GPU 均满载（99% util），不可用于 E3。

## E3 代码
| 文件 | 状态 | 说明 |
|------|------|------|
| `compute_layer_cka.py` | 存在，完整 | 参数：`--model_a`(Dense) `--model_b`(pruned) `--output`(JSON) `--save_reprs_a`/`--load_reprs_a`(缓存Dense reprs) `--device` `--n_samples`(default 50) |
| `plot_cka_heatmap.py` | 存在，完整 | 参数：`--inputs`(多个JSON) `--labels` `--output`(PDF/PNG) |

## 模型可用性 (westb-23072)

| 模型 | post-SFT 路径 | post-prune 路径 | 存在？ |
|------|---------------|-----------------|--------|
| Dense | `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` | N/A | YES |
| CKA-only 20% | `sft_cka_only_20` | `pruned_cka_only_20` | YES / YES |
| Standard 20% | **缺失** | **缺失** | NO / NO |
| Random 20% | `sft_random_20` | `pruned_random_20` | YES / YES |
| RASP 20% | **缺失** | **缺失** | NO / NO |

注：westb 上有 `pruned_gradient_20` 和 `pruned_magnitude_20`，但没有 Standard 20% 和 RASP 20% 的 7B 版本（只有 1.5B 变体和 25% 版本）。

## 缺失模型 — westd-29022 上存在

| 模型 | westd-29022 post-SFT | westd-29022 post-prune |
|------|---------------------|----------------------|
| Standard 20% | `sft_standard_20_westd` | `pruned_standard_20` |
| RASP 20% | `sft_rasp_20_westd` | `pruned_rasp_20` |

需要从 westd-29022 SCP 到 westb-23072。

## 已有 CKA 数据 (westb)
- `results/cka_scores.pt` (May 14), `cka_per_layer.json` (May 15), `cka_heatmap.json` (May 15), `cka_heatmap.pdf` (May 15) — 旧版结果，可能不包含全部 5 个模型。

## E3 可以立即启动？
**NO**，阻塞原因：
1. **GPU 不可用** — cuda:0 和 cuda:1 均在跑 1.5B GRPO，预计 ~30-35 分钟后释放
2. **模型缺失** — Standard 20% 和 RASP 20% 的 7B pruned/SFT 模型需从 westd-29022 SCP 过来（每个 ~14GB，传输时间取决于带宽）
3. **决策点** — E3 用 post-SFT 还是 post-prune 模型？代码示例用的是 pruned 路径，但你的描述写的是 post-SFT (pre-GRPO)

---
