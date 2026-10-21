# recon openvla availability

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recon_openvla-availability_20260523T115331_result.json`
- **Structured JSON:** [`f132b070646be1993c57.json`](../../sessions/f1/f132b070646be1993c57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

### 服务器: westd-41074（4 GPU，~10-30min 释放）

| 项目 | 状态 |
|------|------|
| OpenVLA 模型 | `openvla-libero-object` (4/4 safetensors ✅)；`openvla-oft-libero-object-ms` (空目录 ❌) |
| 评估脚本 | 4个 ✅ (`eval_openvla_libero.py`, `l2norm`, `smart_compress`, `acis_prune`) |
| OpenVLA 代码库 | `openvla-repo` ✅, `openvla-oft-repo` ✅ |
| 磁盘 | 250G / **38G 可用** (86%) |
| **可否直接跑 E2** | **部分可以** — 只有 Object suite 模型，缺 Spatial/Goal/Long 模型。磁盘偏紧，再下载 3 个模型（~42GB）不够 |

---

### 服务器: westd-27271（2 GPU，~30min 释放）

| 项目 | 状态 |
|------|------|
| OpenVLA 模型 | **4 个 suite 全有** ✅：`openvla-libero-object` (4/4), `openvla-7b-finetuned-libero-spatial` (4/4), `openvla-7b-finetuned-libero-goal` (4/4), `openvla-7b-finetuned-libero-10` (4/4) |
| 评估脚本 | 3个 ✅ (`eval_openvla_libero.py`, `l2norm`, `smart_compress`)；缺 `eval_openvla_acis_prune.py` |
| OpenVLA 代码库 | `openvla-repo` ✅, `openvla_deps` ✅ |
| 磁盘 | 250G / **83G 可用** (67%) |
| **可否直接跑 E2** | **是，最佳选择** — 全部 4 个 suite 模型就绪，磁盘充裕。仅 2 GPU 但够用（eval 只需 1 GPU） |

---

### 服务器: westd-38929（4 GPU，~50min-3h 释放）

| 项目 | 状态 |
|------|------|
| OpenVLA 模型 | `openvla-libero-object` (4/4 ✅), `openvla-oft-libero-object` (4/4 ✅), `openvla-oft-libero-spatial` (4/4 ✅), `openvla-oft-libero-goal` (**2/4 ⚠️ 不完整**), `openvla-oft-libero-object-fresh` (2/4 ⚠️ 不完整) |
| 评估脚本 | 5个 ✅（最全，含 `liberoplus_smoke` 和 `acis_prune`） |
| OpenVLA 代码库 | `openvla-repo` ✅, `openvla_code` ✅, `openvla-oft-official` ✅, `openvla-oft-git` ✅ |
| 磁盘 | 250G / **52G 可用** (80%) |
| **可否直接跑 E2** | **部分可以** — Object + Spatial 的 OFT 模型完整，但 Goal 模型不完整（2/4），缺 Long/LIBERO-10 模型 |

---

### 结论

**westd-27271 是跑 E2 的最佳选择**：4 个 suite 的 fine-tuned 模型全部完整就绪，磁盘最充裕（83G 可用），评估脚本基本齐全（缺的 `acis_prune.py` 可从其他服务器复制）。虽然只有 2 GPU，但 eval 通常单 GPU 即可。

---
