# ssh launch a1 lora obj

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch_a1_lora_obj_20260521T044133_result.json`
- **Structured JSON:** [`7f1ff49fe6ee67ae20d6.json`](../../sessions/7f/7f1ff49fe6ee67ae20d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

| 项目 | 结果 |
|------|------|
| **Python PID** | **292258** |
| **GPU** | cuda:2（GPU-8ec4...），16873 MiB / 97887 MiB |
| **训练状态** | 正常推进，step 45+，~3.9s/it，loss ~0.18-0.27 |
| **exp_name** | `a1_lora_object_pudding_seed0` |
| **tmux session** | `a1_lora_obj` |

**参数验证**：日志中没有出现 LoRA/SDF 参数量打印（`logging.info` 输出未捕获到 tee 文件）。但代码确认 `inject_lora_pi0` 在第 134 行被调用，SDF decoder 和 EE extractor 在 110-111 行初始化。

**注意事项**：
1. 首次启动时 `CUDA_VISIBLE_DEVICES=2` 被脚本第 305 行的 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)` 覆盖（默认 `--gpu 3`），导致跑到 cuda:3 上与 PID 281629 冲突。**已杀掉并用 `--gpu 2` 重新启动**。
2. cuda:2 显存 16873 MiB 低于 cuda:1/cuda:3 的 baseline_lora（23893 MiB），可能是 A1 变体配置差异（如 batch_size 未显式指定，可能用了不同默认值）。

---
