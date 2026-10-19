# setup k4 eval prep 41718

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_k4_eval_prep_41718_20260522T145014_result.json`
- **Structured JSON:** [`4b4d23d804f4f96f4cbe.json`](../../sessions/4b/4b4d23d804f4f96f4cbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 项目 | 状态 |
|------|------|
| eval 脚本 | `eval_k4_s123_half2.sh` (cuda:0) + `eval_k4_s456_half2.sh` (cuda:1) 已创建并 chmod +x |
| checkpoint 目录 | `checkpoints/perlayer_kl_k4_{s123,s456}/` 已创建 |
| sync 脚本 | `sync_k4_checkpoints.sh` 已创建（但见下方问题） |
| GPU | 两卡均空闲 (0% / 0MiB) |
| 模型 + 代码 | 均已就位 |

**修正了用户脚本中的参数问题**：
- `analyze_perlayer_sparsity.py` 实际参数是 `--predictor_path`/`--model_path`/`--calibration_samples`/`--device`（非 `--checkpoint`/`--calib_samples`）
- s456 脚本改为 `--gpu 1` / `--device cuda:1`

**SSH 连通性问题**：westd-41718 无法直连 westd-34887（hostname 无法解析，无 SSH config）。`sync_k4_checkpoints.sh` 原样无法工作。

**checkpoint 同步替代方案**：训练完成后，我通过 MCP 工具从 westd-34887 下载 checkpoint 再上传到 westd-41718（管理节点中转），或从 westd-34887 端 scp 推送到 westd-41718（需要在 34887 上配 41718 的地址）。你倾向哪种？

---
