# ops cqa1 cleanup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-cleanup_20260520T123821_result.json`
- **Structured JSON:** [`40ec279858ff26ae6962.json`](../../sessions/40/40ec279858ff26ae6962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

**命令1** `kill -9 858906 2>/dev/null; echo "PID killed"`
```
PID killed
```

**命令2** `nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader`
```
866924, GPU-7ee85176-9244-062b-6f11-e7ff7d06c9ae, 4046 MiB
868193, GPU-a2a15ad4-2e8d-72f9-62e5-cd246f7fc5d0, 4521 MiB
894197, GPU-c242dd9c-f3b7-fad5-77f0-5017abd1a6cf, 4046 MiB
```

**命令3** `ls -la /root/autodl-tmp/xvla_pruning_results/seed43/ 2>/dev/null | tail -5`
```
(空输出——目录不存在或为空)
```

---
