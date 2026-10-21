# prep matrix completion readiness

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_matrix_completion_readiness_20260521T211223_result.json`
- **Structured JSON:** [`23964e77732a4825a8ae.json`](../../sessions/23/23964e77732a4825a8ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data gathered. Here's the report:

---

## 服务器就绪状态报告 — westd-19183 (2026-05-21)

### 基础设施
| 项目 | 状态 |
|------|------|
| **磁盘** | 82GB 可用 / 250GB (68% used) ✅ |
| **GPU** | 2× NVIDIA RTX PRO 6000 Blackwell (98GB) — 均已被占用 (~15GB VRAM each) |
| **残留进程** | 实验 1 & 2 **已在运行中** |

---

### 实验 1: openvla_long_cf_trained

**✅ 已在运行** — PID 579765, GPU 0, 启动于 05:09

- **脚本**: `libero_long_full_pipeline.py --only-counterfactual --conditions trained` ✅
- **模型**: `openvla-7b-oft-finetuned-libero-10` ✅ 存在
- **数据**: 使用 `libero_10`（不是独立的 libero_long 目录） ✅ 存在
- **unnorm_key bug**: ✅ 已修复 — 脚本第579行 merge `dataset_statistics.json` 到 `model.norm_stats`，日志确认 "Merged norm_stats key: libero_10_no_noops"
- **`--only-counterfactual`**: ✅ 仅跑 Phase 6（CF），跳过 Phase 1-5
- **已有 Phase 1-5 结果**: `results/libero_long/` 下有 action_r2_probing.json, l1_attention_profile.json, cross_instruction_classification.json, rsa_analysis.json ✅
- **进度**: CF condition "wrong" ~800/5000 samples

---

### 实验 2: openvla_long_untrained_v1

**✅ 已在运行** — PID 580172, GPU 1, 启动于 05:11

- **脚本**: `libero_long_full_pipeline.py --conditions untrained` ✅ (全流程 Phase 1-6)
- **模型**: `openvla-7b`（OXE pretrained, 未 OFT fine-tune） ✅ 存在
- **数据**: `libero_10` ✅
- **`--conditions`**: ✅ 支持 trained/untrained 分别运行（第528行 argparse）
- **进度**: Phase 1 representation extraction, task 3/10, ~1600/5000 samples

---

### 实验 3: cf_batch_missing_v1

**⚠️ 未启动 — 被 GPU 占用阻塞**

| 检查项 | 状态 |
|--------|------|
| **脚本** `counterfactual_batch.py` | ✅ 存在，支持 `--arch`/`--suite`/`--condition` 参数 |
| **方法选择** | ✅ untrained 自动用 `cosine_dist`（第792行），trained 用 `action_mse` + Cohen's d |
| **模型 phi3v-base** (TracVLA untrained) | ✅ `checkpoints/phi3v-base/` |
| **模型 openvla-7b** (OpenVLA untrained) | ✅ `checkpoints/openvla-7b/` |
| **数据 libero_spatial** | ✅ 存在 |
| **数据 libero_object** | ✅ 存在 |
| **tracvla_spatial/untrained CF 结果** | ❌ 缺失（有 r2/l1_attn/cross_instr，无 counterfactual） |
| **tracvla_object/untrained CF 结果** | ❌ 缺失（同上） |
| **libero_object_untrained CF 结果** | ❌ 缺失（同上） |

**启动命令**（需等 GPU 空闲）：
```bash
# GPU 0 (实验1完成后)
python scripts/counterfactual_batch.py --arch tracvla --suite spatial --condition untrained
python scripts/counterfactual_batch.py --arch tracvla --suite object --condition untrained
python scripts/counterfactual_batch.py --arch openvla --suite object --condition untrained
```

---

### 阻塞与风险

1. **GPU 全满**: 2 块 GPU 分别被实验 1、2 占用。实验 3 必须等至少一个完成。实验 1（CF-only）预计先完成（仅跑 Phase 6）。
2. **实验 1 结果路径**: pipeline 输出到 `results/libero_long/`（顶层），而 `counterfactual_batch.py` 映射到 `results/libero_long/trained/`。确认 CF 结果不会被错误写入或遗漏。
3. **磁盘**: 82GB 余量充足，无风险。

---
