# ssh diagnose a1 sdf v3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_a1_sdf_v3_20260520T065156_result.json`
- **Structured JSON:** [`a9fc6b751e10067208bd.json`](../../sessions/a9/a9fc6b751e10067208bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不在当前 session，无需清除。

---

## 诊断结论

**`a1_sdf_spatial_bowl_s0_v3` 因磁盘满崩溃。**

| 项目 | 详情 |
|------|------|
| **退出原因** | `No space left on device (os error 28)` — 保存 step 6500 checkpoint 时磁盘写满 |
| **最终 step** | 6499/30000 (22%) |
| **最终 loss** | 0.2779, lr=2.31e-05 |
| **运行时长** | ~6h19m |
| **磁盘状态** | `/root/autodl-tmp` 350G **100% 已满**，仅剩 1.3M |
| **最后成功 checkpoint** | step 6000 (`/root/autodl-tmp/checkpoints/a1_sdf_spatial_bowl/a1_sdf_spatial_bowl_seed0/6000/`) |
| **失败 checkpoint** | `tmp_6500/`（不完整，应删除） |
| **已保存 checkpoints** | 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000 (共12个) |

**日志最后 20 行**（step 6489-6499 + traceback）：
```
Training:  22%|██▏ | 6489/30000 [..., loss=0.2597, lr=2.31e-05, step=6489]
Training:  22%|██▏ | 6490/30000 [..., loss=0.2044, lr=2.31e-05, step=6490]
Training:  22%|██▏ | 6491/30000 [..., loss=0.2549, lr=2.31e-05, step=6491]
Training:  22%|██▏ | 6492/30000 [..., loss=0.2554, lr=2.31e-05, step=6492]
Training:  22%|██▏ | 6493/30000 [..., loss=0.2492, lr=2.31e-05, step=6493]
Training:  22%|██▏ | 6494/30000 [..., loss=0.2580, lr=2.31e-05, step=6494]
Training:  22%|██▏ | 6495/30000 [..., loss=0.2512, lr=2.31e-05, step=6495]
Training:  22%|██▏ | 6496/30000 [..., loss=0.2618, lr=2.31e-05, step=6496]
Training:  22%|██▏ | 6497/30000 [..., loss=0.2727, lr=2.31e-05, step=6497]
Training:  22%|██▏ | 6498/30000 [..., loss=0.2476, lr=2.31e-05, step=6498]
Training:  22%|██▏ | 6499/30000 [..., loss=0.2779, lr=2.31e-05, step=6499]
Traceback: safetensors_rust.SafetensorError: I/O error: No space left on device (os error 28)
  at save_checkpoint → safetensors.torch.save_model → serialize_file
```

**恢复建议**：需清理磁盘空间后从 step 6000 checkpoint 恢复训练。12 个 checkpoint 占用大量空间，可考虑只保留最近 2-3 个。

---
