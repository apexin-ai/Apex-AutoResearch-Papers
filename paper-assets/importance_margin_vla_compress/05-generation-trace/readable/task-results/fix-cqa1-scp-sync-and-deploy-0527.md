# fix cqa1 scp sync and deploy 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_scp_sync_and_deploy_0527_20260527T014752_result.json`
- **Structured JSON:** [`d5f8ba153414e072be69.json`](../../sessions/d5/d5f8ba153414e072be69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 已完成
1. **代码同步** — `eval_openvla_l2norm_libero.py` 已通过 raw base64 分 4 块从 westd-41074 同步到 cqa1-33015（425 行，MD5 verified）
2. **transformers 降级** — cqa1 已从 5.5.3 降至 4.40.1，prismatic import 验证通过

### cqa1-33015 GPU 状态

| GPU | 实验 | PID | 状态 | Registry ID |
|-----|------|-----|------|-------------|
| 0 | Random k=0.95 Goal (50 ep) | 896333 | **RUNNING** ✅ | `eval_openvla_random_k095_goal_seed42_v2` |
| 1 | L2norm k=0.95 Object (20 ep) | 898055 | **RUNNING** ✅ | `eval_openvla_l2norm_k095_object_seed42` |
| 2 | — | — | 空闲 | — |
| 3 | Attn k=0.5 Goal (50 ep) | 897100 | **RUNNING** (预存) | `eval_openvla_attn_k05_goal_seed42_v3` |

### 阻塞
- **L2norm k=0.95 Long** — cqa1 上没有 `openvla-libero-10` / `openvla-7b-finetuned-libero-10` 模型，无法运行。仅有 object/spatial/goal 三个模型。需要从其他服务器下载模型，或改在有模型的 westd 服务器上跑。

### 注意
- 脚本参数名是 `--mode random_prune/l2norm_prune` 和 `--k_ratio`，不是 `--pruning_method` 和 `--keep_ratio`
- GPU 0 的 Goal 实验由 submit_training_job 系统自动重启，跑 50 episodes（用户指定 20），功能等价

---
