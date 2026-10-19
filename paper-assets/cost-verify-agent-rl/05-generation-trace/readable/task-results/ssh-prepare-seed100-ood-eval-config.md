# ssh prepare seed100 ood eval config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare_seed100_ood_eval_config_20260522T195455_result.json`
- **Structured JSON:** [`f9a96051458a5869678f.json`](../../sessions/f9/f9a96051458a5869678f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

---

## Eval Config

**文件**: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_seed100_step5_ood_eval.yaml`

已修复添加 `actor_rollout_ref.model.enable_response_mask: false`。所有关键参数已验证：
- `seed.val: 321` ✓
- `enable_response_mask: false`（顶层 + 嵌套层）✓
- 134 OOD tasks (`AlfworldSG_OOD`) ✓
- `trainer.val_only: True` ✓
- `rollout.val_kwargs.temperature: 0.4` ✓
- `model_path: qwen_exp029_seed100_step5_hf` ✓（HF 转换尚未完成，symlink 不存在）
- OmegaConf 语法验证通过 ✓

---

## Seed100 训练 — Healthy (高方差)

| Step | Train Success | Pass@8 | Resp Len (mean) | KL Loss |
|------|-------------|--------|-----------------|---------|
| 0 (init val) | — | — | — | — |
| 1 | 19.5% | 75.0% | 10,635 | 0.0008 |
| 2 | 16.4% | — | — | — |
| 3 | 28.1% | 68.8% | 10,838 | 0.0088 |
| 4 | **9.4%** | — | — | — |
| 5 | 24.2% | 81.3% | 11,335 | 0.0125 |

- **Init val → Final val**: 6.25% → **18.75%** (3x 提升)
- Step 4 有异常低谷（9.4%），step 5 恢复到 24.2%，属 batch 方差
- KL 平稳上升 0.0008 → 0.0125，response length 稳定 ~10.6-11.3k
- **判定: Healthy**，未 collapse

---

## Seed200 v3 — Alive, Step 2/5

- 进程 129823: **存活**
- 当前进度: **40% (2/5)**
- Step 1 指标: train success 18.0%, pass@8 68.8%, resp_len/mean 11,462
- 预计还需 ~1 小时完成

---
