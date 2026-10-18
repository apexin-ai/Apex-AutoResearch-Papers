# code wild data calibration 005

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wild_data_calibration_005_20260516T045705_result.json`
- **Structured JSON:** [`97a55d7db4793f0899a9.json`](../../sessions/97/97a55d7db4793f0899a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**wild_data_calibration_005 完成。**

## 结果汇总

| Dataset | FPR | d0% | N |
|---------|-----|-----|---|
| WikiText | 0.0% | 100.0% | 546 |
| OpenWebText | 0.9% | 99.1% | 5000 |
| **RedPajama V2** | **15.3%** | **84.7%** | **5000** |
| FineWeb | 19.46% | 80.54% | 5000 |
| C4 | 20.2% | 79.8% | 5000 |

RedPajama FPR=15.3%，与 C4 (20.2%) 和 FineWeb (19.46%) 在同一量级（差 -4.9pp / -4.16pp），进一步确认 FPR 的跨数据集一致性。

web-crawled 数据集（C4、FineWeb、RedPajama）FPR 在 15-20% 范围内集中，而高质量筛选数据集（WikiText、OpenWebText）FPR 接近 0%。这个分层模式跨 5 个数据集一致。

产出文件在 `results/wild_data_calibration_005/`，已注册 artifact。

---
