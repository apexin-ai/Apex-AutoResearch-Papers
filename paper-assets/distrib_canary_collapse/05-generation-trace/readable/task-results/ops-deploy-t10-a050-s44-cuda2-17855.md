# ops deploy t10 a050 s44 cuda2 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-t10-a050-s44-cuda2-17855_20260523T081910_result.json`
- **Structured JSON:** [`ef1d79830544016933ce.json`](../../sessions/ef/ef1d79830544016933ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**blocker: westd-17855 磁盘仅剩 5.8G/350G (99%)。**

每个 14b T=10 实验 ~5.3G，部署 2 个 (a050_s44 + a060_s44) 需要 ~10.6G，C007 要求 2x 余量即 ≥21G。

GPU 2 和 3 空闲可用，但磁盘不够。

可选方案：
1. **清理已完成实验** — 服务器上有大量已完成的 14b 实验（例如 `t10_a045_s42_fp32_14b` 5.3G, `t10_a045_s43_fp32_14b` 11G, `t15_a045_s42_fp32_14b` 11G 等），如果数据已分析并注册，可以清理腾出空间
2. **部署到其他服务器** — 如果有其他磁盘充足的服务器
3. **一次只部署一个** — 5.8G 刚好够一个 5.3G 的实验，但不满足 C007 的 2x 余量要求

请指示如何处理。

---
