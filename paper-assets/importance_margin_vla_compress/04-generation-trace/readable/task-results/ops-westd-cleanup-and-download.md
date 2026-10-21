# ops westd cleanup and download

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_cleanup_and_download_20260517T143021_result.json`
- **Structured JSON:** [`2dd3077a03bd78013bc5.json`](../../sessions/2d/2dd3077a03bd78013bc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。最终汇总：

---

## 磁盘清理 (Plan B)

| 清理项 | 释放空间 |
|--------|---------|
| HF cache (`datasets/parquet/`) | ~35G |
| `imm_anchor` (14 个 step 目录) | ~16.8G |
| `imm_anchor_v7_1` (14 个 step 目录) | ~16.8G |
| `baseline_v6_alpha16` (5 个 step 目录) | ~6G |
| **合计** | **~72G** |

**清理前**: 226G used / 25G free (91%)
**清理后**: 154G used / 97G free (62%)

保护目录未动：`libero_imm_twostage_fullft/`、`acis_stage1only_k05/`、所有 `eval_results/`。每个清理目录仅保留 `step_029999` + `latest` 符号链接。

---

## OpenVLA 下载

**模型** (`/root/autodl-tmp/openvla-libero-object/`): 15G, 16 个文件全部下载完成 (OK)
- 4 个 safetensors 分片: 4.6G + 4.7G + 4.7G + 251M
- config/tokenizer/其他配置文件: 11 个

**仓库** (`/root/autodl-tmp/openvla-repo/`): shallow clone 完成 (LFS skipped)

---

## 最终磁盘状态

```
/dev/md0   250G  168G  83G  67%  /root/autodl-tmp
```

---
