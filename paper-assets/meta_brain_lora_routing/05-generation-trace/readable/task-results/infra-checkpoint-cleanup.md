# infra checkpoint cleanup

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_checkpoint-cleanup_20260515T121133_result.json`
- **Structured JSON:** [`fb44af409c18385a5b32.json`](../../sessions/fb/fb44af409c18385a5b32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

### 结果

1. **杀掉的进程**: PID 2711, 3126, 3208, 6393 已杀（部分可能已提前退出）
2. **PID 7014 状态**: ModelScope 下载进程，运行至完成后正常退出
3. **最终下载方式**: 由 PID 7014 (ModelScope `snapshot_download`) 续传完成，无需重新下载
4. **model.safetensors 最终大小**: **14G**（符合预期范围）
5. **checkpoint 目录完整文件列表** (`/root/autodl-tmp/checkpoints/pi0_base/`):

| 文件 | 大小 |
|------|------|
| `.gitattributes` | 1.5K |
| `README.md` | 4.6K |
| `config.json` | 1.9K |
| `model.safetensors` | 14G |
| `policy_postprocessor.json` | 448B |
| `policy_preprocessor.json` | 1012B |

文件通过硬链接放置（link count=2），不额外占用磁盘。当前无残留下载进程（huggingface/wget/curl/modelscope 均无）。注意有一个 `pip install lerobot` 正在后台运行（PID 6580），这是 git clone lerobot 仓库，非下载 checkpoint。

---
