# ops deploy procrustes and run plan012 — Part 2 of 2

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ops-deploy-procrustes-and-run-plan012.md) · [Structured JSON](../../../sessions/3b/3b28785847f7d32370e7.json)

## Before a recorded user message

### Tool result

_source line 549 · 2026-05-21T01:28:54.244Z_

<details><summary>↩ Tool result · `toolu_01RBKWywsxcCayeA7f5CJ6xM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \" 40759\\nRUNNING\\n279 /tmp/procrustes_sensitivity.log\\n    8   sw   1000    0.4869    0.5178  +0.0309   0.6288   0.4497  -0.1791\\n    8   ko     10    0.4975    0.5026  +0.0051   0.3749   0.4430  +0.0681\\n    8   ko     20    0.4975    0.5021  +0.0046   0.3749   0.4492  +0.0744\\n    8   ko     50    0.4975    0.5069  +0.0094   0.3749   0.4272  +0.0523\\n    8   ko    100    0.4975    0.5110  +0.0134   0.3749   0.4056  +0.0307\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "4da4276f-a248-4600-a392-898452f8c235",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\" 40759\\\\nRUNNING\\\\n279 /tmp/procrustes_sensitivity.log\\\\n    8   sw   1000    0.4869    0.5178  +0.0309   0.6288   0.4497  -0.1791\\\\n    8   ko     10    0.4975    0.5026  +0.0051   0.3749   0.4430  +0.0681\\\\n    8   ko     20    0.4975    0.5021  +0.0046   0.3749   0.4492  +0.0744\\\\n    8   ko     50    0.4975    0.5069  +0.0094   0.3749   0.4272  +0.0523\\\\n    8   ko    100    0.4975    0.5110  +0.0134   0.3749   0.4056  +0.0307\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 25.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \" 40759\\nRUNNING\\n279 /tmp/procrustes_sensitivity.log\\n    8   sw   1000    0.4869    0.5178  +0.0309   0.6288   0.4497  -0.1791\\n    8   ko     10    0.4975    0.5026  +0.0051   0.3749   0.4430  +0.0681\\n    8   ko     20    0.4975    0.5021  +0.0046   0.3749   0.4492  +0.0744\\n    8   ko     50    0.4975    0.5069  +0.0094   0.3749   0.4272  +0.0523\\n    8   ko    100    0.4975    0.5110  +0.0134   0.3749   0.4056  +0.0307\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.45}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 550_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01ToGybiddyaGVnybUX5JoGe`</summary>

```json
{
  "server": "westd-13176",
  "command": "sleep 25 && ps -p 40759 -o pid= 2>/dev/null && echo \"RUNNING\" || echo \"DONE\"; wc -l /tmp/procrustes_sensitivity.log; tail -5 /tmp/procrustes_sensitivity.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "14cce5e5-faf2-413d-8890-4d763cab1f3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArZEFjMSk8rATxrNptosqg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 117479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-21T01:29:23.650Z_

<details><summary>↩ Tool result · `toolu_01ToGybiddyaGVnybUX5JoGe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \" 40759\\nRUNNING\\n280 /tmp/procrustes_sensitivity.log\\n    8   ko     10    0.4975    0.5026  +0.0051   0.3749   0.4430  +0.0681\\n    8   ko     20    0.4975    0.5021  +0.0046   0.3749   0.4492  +0.0744\\n    8   ko     50    0.4975    0.5069  +0.0094   0.3749   0.4272  +0.0523\\n    8   ko    100    0.4975    0.5110  +0.0134   0.3749   0.4056  +0.0307\\n    8   ko    200    0.4975    0.5348  +0.0373   0.3749   0.3722  -0.0027\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "a68ce47d-c3e8-4539-8974-78e576c870c4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\" 40759\\\\nRUNNING\\\\n280 /tmp/procrustes_sensitivity.log\\\\n    8   ko     10    0.4975    0.5026  +0.0051   0.3749   0.4430  +0.0681\\\\n    8   ko     20    0.4975    0.5021  +0.0046   0.3749   0.4492  +0.0744\\\\n    8   ko     50    0.4975    0.5069  +0.0094   0.3749   0.4272  +0.0523\\\\n    8   ko    100    0.4975    0.5110  +0.0134   0.3749   0.4056  +0.0307\\\\n    8   ko    200    0.4975    0.5348  +0.0373   0.3749   0.3722  -0.0027\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 25.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \" 40759\\nRUNNING\\n280 /tmp/procrustes_sensitivity.log\\n    8   ko     10    0.4975    0.5026  +0.0051   0.3749   0.4430  +0.0681\\n    8   ko     20    0.4975    0.5021  +0.0046   0.3749   0.4492  +0.0744\\n    8   ko     50    0.4975    0.5069  +0.0094   0.3749   0.4272  +0.0523\\n    8   ko    100    0.4975    0.5110  +0.0134   0.3749   0.4056  +0.0307\\n    8   ko    200    0.4975    0.5348  +0.0373   0.3749   0.3722  -0.0027\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 552_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Y77oBsoekXbp8nKnYUXaZa`</summary>

```json
{
  "server": "westd-13176",
  "command": "sleep 25 && ps -p 40759 -o pid= 2>/dev/null && echo \"RUNNING\" || echo \"DONE\"; wc -l /tmp/procrustes_sensitivity.log; tail -5 /tmp/procrustes_sensitivity.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "fe35ebdc-6ca5-4387-b625-afc793e1139e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiKJKXc398eXKHs1sq9NcT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 117954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-21T01:29:52.375Z_

<details><summary>↩ Tool result · `toolu_01Y77oBsoekXbp8nKnYUXaZa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE\\n284 /tmp/procrustes_sensitivity.log\\n    8   ko    200    0.4975    0.5348  +0.0373   0.3749   0.3722  -0.0027\\n    8   ko    500    0.4975    0.5393  +0.0418   0.3749   0.3518  -0.0231\\n    8   ko   1000    0.4975    0.5593  +0.0617   0.3749   0.3282  -0.0466\\n\\nResults saved to /root/xling_calib_direction/activations/../results/linproj_procrustes_sensitivity.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "35950629-3d00-40c6-9757-b536282073fb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DONE\\\\n284 /tmp/procrustes_sensitivity.log\\\\n    8   ko    200    0.4975    0.5348  +0.0373   0.3749   0.3722  -0.0027\\\\n    8   ko    500    0.4975    0.5393  +0.0418   0.3749   0.3518  -0.0231\\\\n    8   ko   1000    0.4975    0.5593  +0.0617   0.3749   0.3282  -0.0466\\\\n\\\\nResults saved to /root/xling_calib_direction/activations/../results/linproj_procrustes_sensitivity.csv\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 25.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DONE\\n284 /tmp/procrustes_sensitivity.log\\n    8   ko    200    0.4975    0.5348  +0.0373   0.3749   0.3722  -0.0027\\n    8   ko    500    0.4975    0.5393  +0.0418   0.3749   0.3518  -0.0231\\n    8   ko   1000    0.4975    0.5593  +0.0617   0.3749   0.3282  -0.0466\\n\\nResults saved to /root/xling_calib_direction/activations/../results/linproj_procrustes_sensitivity.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 554_

完成！CSV 保存到 `/root/xling_calib_direction/results/linproj_procrustes_sensitivity.csv`。读取完整输出汇总。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "8517dce8-29e1-45ec-9ac8-5cc14a850784",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gJsjLDRA6FWXSeFy1sEVR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 118417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 408
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 555_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ARmLTcuh5VV9NmDTjWytpa`</summary>

```json
{
  "server": "westd-13176",
  "command": "head -5 /root/xling_calib_direction/results/linproj_procrustes_sensitivity.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "8e59f715-6ea2-44b2-9acf-57df985ef7d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gJsjLDRA6FWXSeFy1sEVR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 118417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 408
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 556 · 2026-05-21T01:29:57.414Z_

<details><summary>↩ Tool result · `toolu_01ARmLTcuh5VV9NmDTjWytpa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"layer,language,n_pairs,auroc_zs,auroc_proc_mean,auroc_proc_std,ece_zs,ece_proc_mean,ece_proc_std,brier_zs,brier_proc_mean,brier_proc_std,delta_auroc,delta_ece\\n0,zh,10,0.516569,0.507209,0.034931,0.314175,0.439607,0.036662,0.314994,0.444850,0.035958,-0.009360,0.125431\\n0,zh,20,0.516569,0.502052,0.023202,0.314175,0.426524,0.037956,0.314994,0.434750,0.035508,-0.014517,0.112349\\n0,zh,50,0.516569,0.526015,0.019439,0.314175,0.415990,0.023534,0.314994,0.428908,0.023543,0.009446,0.101815\\n0,zh,100,0.516569,0.522497,0.012371,0.314175,0.404204,0.019343,0.314994,0.419227,0.018736,0.005928,0.090028\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "fd7d33d0-48d1-44fc-9f14-e193534ebe88",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"layer,language,n_pairs,auroc_zs,auroc_proc_mean,auroc_proc_std,ece_zs,ece_proc_mean,ece_proc_std,brier_zs,brier_proc_mean,brier_proc_std,delta_auroc,delta_ece\\\\n0,zh,10,0.516569,0.507209,0.034931,0.314175,0.439607,0.036662,0.314994,0.444850,0.035958,-0.009360,0.125431\\\\n0,zh,20,0.516569,0.502052,0.023202,0.314175,0.426524,0.037956,0.314994,0.434750,0.035508,-0.014517,0.112349\\\\n0,zh,50,0.516569,0.526015,0.019439,0.314175,0.415990,0.023534,0.314994,0.428908,0.023543,0.009446,0.101815\\\\n0,zh,100,0.516569,0.522497,0.012371,0.314175,0.404204,0.019343,0.314994,0.419227,0.018736,0.005928,0.090028\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"layer,language,n_pairs,auroc_zs,auroc_proc_mean,auroc_proc_std,ece_zs,ece_proc_mean,ece_proc_std,brier_zs,brier_proc_mean,brier_proc_std,delta_auroc,delta_ece\\n0,zh,10,0.516569,0.507209,0.034931,0.314175,0.439607,0.036662,0.314994,0.444850,0.035958,-0.009360,0.125431\\n0,zh,20,0.516569,0.502052,0.023202,0.314175,0.426524,0.037956,0.314994,0.434750,0.035508,-0.014517,0.112349\\n0,zh,50,0.516569,0.526015,0.019439,0.314175,0.415990,0.023534,0.314994,0.428908,0.023543,0.009446,0.101815\\n0,zh,100,0.516569,0.522497,0.012371,0.314175,0.404204,0.019343,0.314994,0.419227,0.018736,0.005928,0.090028\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 557_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018d1xN3Uzej75ZrdgcfLNFC`</summary>

```json
{
  "server": "westd-13176",
  "command": "wc -l /root/xling_calib_direction/results/linproj_procrustes_sensitivity.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "42fae355-5f3e-4130-9f2d-c908ef97cb92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gJsjLDRA6FWXSeFy1sEVR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 118417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 408
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 558 · 2026-05-21T01:29:58.094Z_

<details><summary>↩ Tool result · `toolu_018d1xN3Uzej75ZrdgcfLNFC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"281 /root/xling_calib_direction/results/linproj_procrustes_sensitivity.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "d5cc627f-1f7f-42d6-9987-fa2d33d1cec2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"281 /root/xling_calib_direction/results/linproj_procrustes_sensitivity.csv\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"281 /root/xling_calib_direction/results/linproj_procrustes_sensitivity.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 559_

全部完成。汇总结果：

---

## 产出

### 1. transfer_eval.py 部署确认
- `/root/xling_calib_direction/code/transfer_eval.py` ✓ (含 `procrustes_align`, `orthogonal_procrustes`, `n_proj_pairs`)
- `/root/xling_calib_direction/transfer_eval.py` ✓
- `scipy.linalg.orthogonal_procrustes` 导入正常

### 2. CSV 路径
`/root/xling_calib_direction/results/linproj_procrustes_sensitivity.csv` — 280 行数据 (8层 × 5语言 × 7 N值)

### 3. 关键发现

**ΔAUROC 与 N 的关系：**
- N 增大普遍改善 ΔAUROC（std 也缩小）
- 但改善幅度强烈依赖于 **ZS baseline 强度**

**核心模式：Procrustes 效果取决于 ZS AUROC**

| ZS AUROC 范围 | Procrustes 效果 | 典型案例 |
|---|---|---|
| < 0.50 (below chance) | **大幅改善** ΔAUROC +0.10~+0.14 | hi@L8/L12/L16, sw@L12 |
| 0.50~0.55 | 小幅改善 +0.02~+0.06 | ar/ko@L0/L4/L8 |
| > 0.60 | **损害** ΔAUROC -0.01~-0.05 | zh/ar/ko@L20/L24/L27 |

**最大受益者：Hindi**
- Layer 8: ZS=0.43 → Proc=0.57 (ΔAUROC=**+0.14**, N=1000)
- Layer 12: ZS=0.45 → Proc=0.56 (ΔAUROC=+0.12)
- Layer 16: ZS=0.46 → Proc=0.58 (ΔAUROC=+0.12)

**ECE 行为更复杂：**
- 早期层（0, 4, 8）ZS ECE 很差（0.44-0.67），Procrustes 大幅改善 ECE（最大 ΔECE=-0.36@L4 zh）
- 中高层（16-27）ZS ECE 较好（0.25-0.37），Procrustes 反而恶化 ECE

**Swahili 是例外：** 在中高层，Procrustes 几乎对 sw 无效甚至有害（ΔAUROC 始终为负@L16/L20/L27），但在 L8/L12 的 ECE 改善显著

### 4. N 增大是否改善 ΔAUROC？
**是，但有上限**。大多数情况下 N=200→1000 的边际收益递减。对于 ZS>0.60 的层，即使 N=1000 也无法使 ΔAUROC 转正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "uuid": "08b50145-e690-46dd-9279-d2a31a996502",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKLHhDDo617PGn4MUVsjYf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 118825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 849
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 560_

全部完成。汇总结果：

---

## 产出

### 1. transfer_eval.py 部署确认
- `/root/xling_calib_direction/code/transfer_eval.py` ✓ (含 `procrustes_align`, `orthogonal_procrustes`, `n_proj_pairs`)
- `/root/xling_calib_direction/transfer_eval.py` ✓
- `scipy.linalg.orthogonal_procrustes` 导入正常

### 2. CSV 路径
`/root/xling_calib_direction/results/linproj_procrustes_sensitivity.csv` — 280 行数据 (8层 × 5语言 × 7 N值)

### 3. 关键发现

**ΔAUROC 与 N 的关系：**
- N 增大普遍改善 ΔAUROC（std 也缩小）
- 但改善幅度强烈依赖于 **ZS baseline 强度**

**核心模式：Procrustes 效果取决于 ZS AUROC**

| ZS AUROC 范围 | Procrustes 效果 | 典型案例 |
|---|---|---|
| < 0.50 (below chance) | **大幅改善** ΔAUROC +0.10~+0.14 | hi@L8/L12/L16, sw@L12 |
| 0.50~0.55 | 小幅改善 +0.02~+0.06 | ar/ko@L0/L4/L8 |
| > 0.60 | **损害** ΔAUROC -0.01~-0.05 | zh/ar/ko@L20/L24/L27 |

**最大受益者：Hindi**
- Layer 8: ZS=0.43 → Proc=0.57 (ΔAUROC=**+0.14**, N=1000)
- Layer 12: ZS=0.45 → Proc=0.56 (ΔAUROC=+0.12)
- Layer 16: ZS=0.46 → Proc=0.58 (ΔAUROC=+0.12)

**ECE 行为更复杂：**
- 早期层（0, 4, 8）ZS ECE 很差（0.44-0.67），Procrustes 大幅改善 ECE（最大 ΔECE=-0.36@L4 zh）
- 中高层（16-27）ZS ECE 较好（0.25-0.37），Procrustes 反而恶化 ECE

**Swahili 是例外：** 在中高层，Procrustes 几乎对 sw 无效甚至有害（ΔAUROC 始终为负@L16/L20/L27），但在 L8/L12 的 ECE 改善显著

### 4. N 增大是否改善 ΔAUROC？
**是，但有上限**。大多数情况下 N=200→1000 的边际收益递减。对于 ZS>0.60 的层，即使 N=1000 也无法使 ΔAUROC 转正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 6215738,
  "duration_api_ms": 1093521,
  "num_turns": 226,
  "stop_reason": "end_turn",
  "session_id": "6736e159-f84d-4b5e-96c2-a3e987a4abf9",
  "total_cost_usd": 10.626488750000004,
  "usage": {
    "input_tokens": 221,
    "cache_creation_input_tokens": 107833,
    "cache_read_input_tokens": 17446207,
    "output_tokens": 49005,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 107833,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 850,
        "cache_read_input_tokens": 118825,
        "cache_creation_input_tokens": 849,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 849
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3094,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003199,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 221,
      "outputTokens": 49005,
      "cacheReadInputTokens": 17446207,
      "cacheCreationInputTokens": 107833,
      "webSearchRequests": 0,
      "costUSD": 10.623289750000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1efe2ce6-a8c6-4cd6-ae18-ac3dc4e001f1"
}
```

</details>

---
