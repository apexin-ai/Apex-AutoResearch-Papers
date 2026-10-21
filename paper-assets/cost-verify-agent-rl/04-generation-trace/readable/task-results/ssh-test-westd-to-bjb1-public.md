# ssh test westd to bjb1 public

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_test_westd_to_bjb1_public_20260523T042923_result.json`
- **Structured JSON:** [`3862cc37dfb1df901a2d.json`](../../sessions/38/3862cc37dfb1df901a2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**测试结果：公网直连成功。**

| 项目 | 值 |
|------|-----|
| bjb1 公网地址 | `connect.bjb1.seetacloud.com` |
| bjb1 端口 | `17606` |
| westd → bjb1 连通性 | 成功（0.96s） |
| 认证方式 | SSH 密钥（无密码） |

westd 上可直接用以下命令连接 bjb1：
```bash
ssh -p 17606 root@connect.bjb1.seetacloud.com
```

数据迁移可基于此通道使用 `scp -P 17606` 或 `rsync -e "ssh -p 17606"` 进行。

---
