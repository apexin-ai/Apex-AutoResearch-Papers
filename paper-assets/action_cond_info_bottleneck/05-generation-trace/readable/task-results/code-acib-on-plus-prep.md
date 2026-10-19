# code acib on plus prep

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acib-on-plus-prep_20260516T151753_result.json`
- **Structured JSON:** [`a8b8e2ab301bd0e0ae67.json`](../../sessions/a8/a8b8e2ab301bd0e0ae67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。汇报：

### 结果

1. **smolvla_libero_plus 可用** — 已在本地缓存 `/root/autodl-tmp/.hf_cache/models--lerobot--smolvla_libero_plus`，无需下载

2. **hidden_size 一致，scorer 兼容** — 两个模型均为：
   - 总参数: 450,169,185
   - 可训练参数: 100,004,001
   - Scorer input_dim: 1920
   
   两者都基于 `SmolVLM2-500M-Video-Instruct`，架构完全相同。唯一差异是 plus 版本的 `empty_cameras=2`（data-aug），不影响 scorer。

3. **启动脚本已创建** — `/root/acib/scripts/run_acib_on_plus.sh`，参数与 v7 seed1 一致，仅 `--model_id` 改为 `lerobot/smolvla_libero_plus`，`--output_dir` 改为 `/root/autodl-tmp/acib_v7_on_plus`

4. **Dry-run 通过** — CPU 模式加载 smolvla_libero_plus + ACIB scorer 成功，无报错

5. **无需修改代码** — `--model_id` 直接切换即可，`train_acib.py` 的 `from_pretrained` 和 `load_normalization_stats` 都能正确处理 plus 模型

---
