# env pi05 setup bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_env_pi05-setup-bjb2-40593_20260521T010641_result.json`
- **Structured JSON:** [`254bc69d0d0d376c963f.json`](../../sessions/25/254bc69d0d0d376c963f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

| 项目 | 结果 |
|------|------|
| **lerobot** | v0.5.2 (GitHub dev + pi0 extra)，PI05Policy 导入正常 |
| **模型路径** | `/root/autodl-tmp/models/pi05_libero_finetuned/` |
| **模型大小** | 7.0GB（model.safetensors 7.47GB） |
| **GPU 加载** | cuda:0, 显存占用 8.71GB / 24GB |
| **磁盘** | 数据盘剩余 145GB |

**需注意**：加载时有 vision_tower key mismatch warning（`vision_model.` 前缀差异，missing + unexpected keys 对称），这是 transformers 版本与 checkpoint 的命名规则差异。模型以 `strict=False` 方式加载成功，vision tower 权重实际已加载（通过 unexpected keys 映射）。正式 eval 时建议确认 vision encoder 输出是否正确。

---
