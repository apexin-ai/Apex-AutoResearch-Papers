# code wild data calibration 003

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wild_data_calibration_003_20260516T013319_result.json`
- **Structured JSON:** [`fd1d79ed1a9c9051c67e.json`](../../sessions/fd/fd1d79ed1a9c9051c67e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 和 artifact 已更新。

**结果摘要：**

| Dataset | N | d0% | FPR% | Source |
|---------|--:|----:|-----:|--------|
| WikiText-103 | 546 | 100.00 | 0.00 | v1 ref |
| C4 | 5,000 | 79.80 | 20.20 | v1 ref |
| **FineWeb** | **5,000** | **80.54** | **19.46** | **v3** |

**关键发现：**
- FineWeb FPR=19.46%，与 C4 FPR=20.20% 仅差 0.74pp，跨数据集高度一致
- 所有误分类均为 d1（无 d2/d3 false positives），误分类程度温和
- P(d0) 分布：FineWeb 0.7987 vs C4 类似
- 确认 web-crawl 文本 ~20% FPR 是由模板/SEO 内容驱动的通用现象，非特定数据集伪影
- 编辑质量文本（WikiText）FPR 稳定在 0%

**技术要点：**
- v2 失败原因：HF streaming 在 AutoDL 代理下挂死
- v3 解决方案：用 `hf-mirror.com` 下载 FineWeb parquet（2GB/114s），本地离线读取
- RedPajama 文件路径 404，仅 FineWeb 成功
- 全流程 87 秒（含特征提取 77s on cuda:1）

---
