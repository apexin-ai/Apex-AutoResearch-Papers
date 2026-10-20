# eval adaptive fix seed123 456 ood downstream

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_adaptive_fix_seed123_456_ood_downstream_20260520T090319_result.json`
- **Structured JSON:** [`648380af4f4805038d7a.json`](../../sessions/64/648380af4f4805038d7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：`adaptive_fix_seed123` 和 `adaptive_fix_seed456` 的 checkpoint 不存在。**

搜索了整个 `/root/` 目录，包含 "adaptive" 且带 seed123/456 的 final checkpoint 只有：

| 实验名 | 路径 | 备注 |
|--------|------|------|
| `adaptive_ood_seed123` | `/root/autodl-tmp/.../adaptive_ood_seed123/final/` | τ=0.8 n_min=2，但 registry conclusion=negative |
| `adaptive_ood_seed456` | `/root/autodl-tmp/.../adaptive_ood_seed456/final/` | τ=0.8 n_min=2，但 registry conclusion=negative |
| `adaptive_1_7b_seed123` | `/root/autodl-tmp/.../adaptive_1_7b_seed123/final/` | 1.7B 模型，不是 0.6B |
| `adaptive_rho06_tau07_seed123` | `/root/autodl-tmp/.../adaptive_rho06_tau07_seed123/final/` | ρ=0.6 τ=0.7 |
| `adaptive_rho06_tau07_seed456` | `/root/autodl-tmp/.../adaptive_rho06_tau07_seed456/final/` | ρ=0.6 τ=0.7 |

`adaptive_fix_seed42` 是唯一做过 n_min fix (3→2) 的实验。seed123 和 seed456 从未用 n_min=2 训练过，或训练产物已丢失（可能在之前退役的 westd-30476 上）。

**最接近的替代品**是 `adaptive_ood_seed123/456`（同为 τ=0.8 n_min=2 retrain），但 registry 标记 conclusion=negative（in-dist PPL 不达标）。是否用这两个 checkpoint 补跑 OOD + downstream，还是需要先重新训练 adaptive_fix 版本？

---
