# infra disk audit westd10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk_audit_westd10894_20260521T024322_result.json`
- **Structured JSON:** [`906e991cb7bd25b1d9a4.json`](../../sessions/90/906e991cb7bd25b1d9a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。汇总如下：

---

```
磁盘总况: 230G / 250G (92% used), 21G 可用

Checkpoint 目录 (总计 193G):

vanilla_s0 (60G):
  - 35000_chkpt: 15G  ✅ 保留
  - 40000_chkpt: 15G  🗑 可删
  - 45000_chkpt: 15G  🗑 可删
  - 50000_chkpt: 15G  ✅ 保留

vanilla_s1 (60G):
  - 35000_chkpt: 15G  ✅ 保留
  - 40000_chkpt: 15G  🗑 可删
  - 45000_chkpt: 15G  🗑 可删
  - 50000_chkpt: 15G  ✅ 保留

vanilla_s2 (75G):
  - 30000_chkpt: 15G  ⚠️ 额外checkpoint，不在策略范围内
  - 35000_chkpt: 15G  ✅ 保留
  - 40000_chkpt: 15G  🗑 可删
  - 45000_chkpt: 15G  🗑 可删
  - 50000_chkpt: 15G  ✅ 保留

occ_dryrun:  4K (空壳)
occ_dryrun2: 4K (空壳)

可清理项（按策略: 保留 50K+35K，删 40K+45K）:
  - vanilla_s0/...--40000_chkpt: 15G
  - vanilla_s0/...--45000_chkpt: 15G
  - vanilla_s1/...--40000_chkpt: 15G
  - vanilla_s1/...--45000_chkpt: 15G
  - vanilla_s2/...--40000_chkpt: 15G
  - vanilla_s2/...--45000_chkpt: 15G
  预计释放: ~90G

需要 Director 确认:
  - vanilla_s2/...--30000_chkpt (15G): 额外的30K checkpoint，是否也删？
  - occ_dryrun / occ_dryrun2: 空目录，是否清理？

其他大文件:
  - models:    15G
  - data:      2.0G
  - HF cache:  148K (可忽略)
  - occsafe_vla 代码: 211M
```

---
