# audit table1 spatial provenance 20260525T015026 retry1 — Part 4 of 4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[← Part 3](part-003.md) · [Transcript overview](../audit-table1-spatial-provenance-20260525t015026-retry1.md) · [Structured JSON](../../../sessions/da/daa03b6813ade8e1cdfe.json)

## Before a recorded user message

### Tool result

_source line 112 · 2026-05-25T01:56:50.733Z_

<details><summary>↩ Tool result · `toolu_01Fb68ibY8UyZBzxxGnyJdCz`</summary>

```text
{
  "VLA-only (K=1)": {
    "per_task": {
      "between_plate_and_ramekin": 0.6,
      "next_to_ramekin": 1.0,
      "from_table_center": 0.0,
      "on_cookie_box": 0.2,
      "in_top_drawer": 0.0,
      "on_ramekin": 0.0,
      "next_to_cookie_box": 0.9,
      "on_stove": 0.0,
      "next_to_plate": 0.3,
      "on_wooden_cabinet": 0.0
    },
    "overall_sr": 0.3,
    "n_tasks": 10,
    "complete": true,
    "sources": {
      "between_plate_and_ramekin": "eval-spatial-v7-full",
      "next_to_ramekin": "eval-spatial-v7-full",
      "from_table_center": "eval-spatial-v7-full",
      "on_cookie_box": "eval-spatial-v7-full",
      "in_top_drawer": "eval-spatial-v7-full",
      "on_ramekin": "eval-spatial-v7-full",
      "next_to_cookie_box": "eval-spatial-v7-full",
      "on_stove": "eval-spatial-v7-full",
      "next_to_plate": "eval-spatial-v7-full",
      "on_wooden_cabinet": "eval-spatial-v7-full"
    }
  },
  "VLA-mean (K=10)": {
    "per_task": {
      "between_plate_and_ramekin": null,
      "next_to_ramekin": 0.7,
      "from_table_center": 1.0,
      "on_cookie_box": 0.0,
      "in_top_drawer": 0.3,
      "on_ramekin": 0.0,
      "next_to_cookie_box": 0.0,
      "on_stove": 0.8,
      "next_to_plate": 0.0,
      "on_wooden_cabinet": 0.1
    },
    "overall_sr": 0.3222222222222222,
    "n_tasks": 9,
    "complete": false,
    "sources": {
      "next_to_ramekin": "eval-vla-mean-spatial",
      "from_table_center": "eval-vla-mean-spatial",
      "on_cookie_box": "eval-vla-mean-spatial",
      "in_top_drawer": "eval-vla-mean-spatial",
      "on_ramekin": "eval-vla-mean-spatial",
      "next_to_cookie_box": "eval-vla-mean-spatial",
      "on_stove": "eval-vla-mean-spatial",
      "next_to_plate": "eval-vla-mean-spatial",
      "on_wooden_cabinet": "eval-vla-mean-spatial-t10"
    }
  },
  "ReconVLA argmin (K=10)": {
    "per_task": {
      "between_plate_and_ramekin": 0.6,
      "next_to_ramekin": 1.0,
      "from_table_center": 0.0,
      "on_cookie_box": 0.3,
      "in_top_drawer": 0.1,
      "on_ramekin": 0.1,
      "next_to_cookie_box": 0.9,
      "on_stove": 0.0,
      "next_to_plate": 0.4,
      "on_wooden_cabinet": 0.0
    },
    "overall_sr": 0.33999999999999997,
    "n_tasks": 10,
    "complete": true,
    "sources": {
      "between_plate_and_ramekin": "eval-reconvla-spatial-v3",
      "next_to_ramekin": "eval-reconvla-spatial-v3",
      "from_table_center": "eval-reconvla-spatial-v3",
      "on_cookie_box": "eval-reconvla-spatial-v3",
      "in_top_drawer": "eval-reconvla-spatial-v3",
      "on_ramekin": "eval-reconvla-spatial-v3",
      "next_to_cookie_box": "eval-reconvla-spatial-v3",
      "on_stove": "eval-reconvla-spatial-v3",
      "next_to_plate": "eval-reconvla-spatial-v3",
      "on_wooden_cabinet": "eval-reconvla-spatial-v3"
    }
  },
  "Argmin-only (K=10)": {
    "per_task": {
      "between_plate_and_ramekin": 0.6,
      "next_to_ramekin": 1.0,
      "from_table_center": 0.0,
      "on_cookie_box": 0.3,
      "in_top_drawer": 0.1,
      "on_ramekin": 0.1,
      "next_to_cookie_box": 0.9,
      "on_stove": 0.0,
      "next_to_plate": 0.3,
      "on_wooden_cabinet": 0.1
    },
    "overall_sr": 0.33999999999999997,
    "n_tasks": 10,
    "complete": true,
    "sources": {
      "between_plate_and_ramekin": "eval-argmin-only-spatial-r2",
      "next_to_ramekin": "eval-argmin-only-spatial-r2",
      "from_table_center": "eval-argmin-only-spatial-r2",
      "on_cookie_box": "eval-argmin-only-spatial-r2",
      "in_top_drawer": "eval-argmin-only-spatial-r2",
      "on_ramekin": "eval-argmin-only-spatial-r2",
      "next_to_cookie_box": "eval-argmin-only-spatial-r2",
      "on_stove": "eval-argmin-only-spatial-r2",
      "next_to_plate": "eval-argmin-only-spatial-r2",
      "on_wooden_cabinet": "eval-argmin-only-spatial-r2"
    }
  },
  "ACR per-DOF": {
    "per_task": {
      "between_plate_and_ramekin": 0.6,
      "next_to_ramekin": 1.0,
      "from_table_center": 0.1,
      "on_cookie_box": 0.4,
      "in_top_drawer": 0.0,
      "on_ramekin": 0.0,
      "next_to_cookie_box": 0.9,
      "on_stove": 0.1,
      "next_to_plate": 0.4,
      "on_wooden_cabinet": 0.0
    },
    "overall_sr": 0.35,
    "n_tasks": 10,
    "complete": true,
    "sources": {
      "between_plate_and_ramekin": "eval-acr-spatial-v4-small-r2",
      "next_to_ramekin": "eval-acr-spatial-v4-small-r2",
      "from_table_center": "eval-acr-spatial-v4-small-r2",
      "on_cookie_box": "eval-acr-spatial-v4-small-r2",
      "in_top_drawer": "eval-acr-spatial-v4-small-r2",
      "on_ramekin": "eval-acr-spatial-v4-small-r2",
      "next_to_cookie_box": "eval-acr-spatial-v4-small-r2",
      "on_stove": "eval-acr-spatial-v4-small-r2",
      "next_to_plate": "eval-acr-spatial-v4-small-r2",
      "on_wooden_cabinet": "eval-acr-spatial-v4-small-r2"
    }
  },
  "ACR obs-only": {
    "per_task": {
      "between_plate_and_ramekin": 0.9,
      "next_to_ramekin": 1.0,
      "from_table_center": 0.0,
      "on_cookie_box": 0.4,
      "in_top_drawer": 0.1,
      "on_ramekin": 0.0,
      "next_to_cookie_box": 0.9,
      "on_stove": 0.0,
      "next_to_plate": 0.2,
      "on_wooden_cabinet": 0.0
    },
    "overall_sr": 0.35,
    "n_tasks": 10,
    "complete": true,
    "sources": {
      "between_plate_and_ramekin": "eval-acr-spatial-v4-obs-only-r3",
      "next_to_ramekin": "eval-acr-spatial-v4-obs-only-r3",
      "from_table_center": "eval-acr-spatial-v4-obs-only-r3",
      "on_cookie_box": "eval-acr-spatial-v4-obs-only-r3",
      "in_top_drawer": "eval-acr-spatial-v4-obs-only-r3",
      "on_ramekin": "eval-acr-spatial-v4-obs-only-r3",
      "next_to_cookie_box": "eval-acr-spatial-v4-obs-only-r3",
      "on_stove": "eval-acr-spatial-v4-obs-only-r3",
      "next_to_plate": "eval-acr-spatial-v4-obs-only-r3",
      "on_wooden_cabinet": "eval-acr-spatial-v4-obs-only-r3"
    }
  },
  "ACR scalar": {
    "per_task": {
      "between_plate_and_ramekin": 0.6,
      "next_to_ramekin": 1.0,
      "from_table_center": 0.1,
      "on_cookie_box": 0.4,
      "in_top_drawer": 0.0,
      "on_ramekin": 0.0,
      "next_to_cookie_box": 0.9,
      "on_stove": 0.0,
      "next_to_plate": 0.1,
      "on_wooden_cabinet": 0.1
    },
    "overall_sr": 0.32,
    "n_tasks": 10,
    "complete": true,
    "sources": {
      "between_plate_and_ramekin": "eval-acr-spatial-v4-scalar-r2",
      "next_to_ramekin": "eval-acr-spatial-v4-scalar-r2",
      "from_table_center": "eval-acr-spatial-v4-scalar-r2",
      "on_cookie_box": "eval-acr-spatial-v4-scalar-r2",
      "in_top_drawer": "eval-acr-spatial-v4-scalar-r2",
      "on_ramekin": "eval-acr-spatial-v4-scalar-r2",
      "next_to_cookie_box": "eval-acr-spatial-v4-scalar-r2",
      "on_stove": "eval-acr-spatial-v4-scalar-r2",
      "next_to_plate": "eval-acr-spatial-v4-scalar-r2",
      "on_wooden_cabinet": "eval-acr-spatial-v4-scalar-r2"
    }
  },
  "ACR tiny (norm=0.05)": {
    "per_task": {
      "between_plate_and_ramekin": 0.7,
      "next_to_ramekin": 0.9,
      "from_table_center": 0.0,
      "on_cookie_box": 0.3,
      "in_top_drawer": 0.0,
      "on_ramekin": 0.0,
      "next_to_cookie_box": 0.9,
      "on_stove": null,
      "next_to_plate": null,
      "on_wooden_cabinet": null
    },
    "overall_sr": 0.39999999999999997,
    "n_tasks": 7,
    "complete": false,
    "sources": {
      "between_plate_and_ramekin": "eval-tiny-correction-spatial",
      "next_to_ramekin": "eval-tiny-correction-spatial",
      "from_table_center": "eval-tiny-correction-spatial",
      "on_cookie_box": "eval-tiny-correction-spatial",
      "in_top_drawer": "eval-tiny-correction-spatial",
      "on_ramekin": "eval-tiny-correction-spatial",
      "next_to_cookie_box": "eval-tiny-correction-spatial"
    }
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "uuid": "14048dd6-6968-4000-9b5d-c7e996e2321f",
  "tool_use_result": {
    "stdout": "{\n  \"VLA-only (K=1)\": {\n    \"per_task\": {\n      \"between_plate_and_ramekin\": 0.6,\n      \"next_to_ramekin\": 1.0,\n      \"from_table_center\": 0.0,\n      \"on_cookie_box\": 0.2,\n      \"in_top_drawer\": 0.0,\n      \"on_ramekin\": 0.0,\n      \"next_to_cookie_box\": 0.9,\n      \"on_stove\": 0.0,\n      \"next_to_plate\": 0.3,\n      \"on_wooden_cabinet\": 0.0\n    },\n    \"overall_sr\": 0.3,\n    \"n_tasks\": 10,\n    \"complete\": true,\n    \"sources\": {\n      \"between_plate_and_ramekin\": \"eval-spatial-v7-full\",\n      \"next_to_ramekin\": \"eval-spatial-v7-full\",\n      \"from_table_center\": \"eval-spatial-v7-full\",\n      \"on_cookie_box\": \"eval-spatial-v7-full\",\n      \"in_top_drawer\": \"eval-spatial-v7-full\",\n      \"on_ramekin\": \"eval-spatial-v7-full\",\n      \"next_to_cookie_box\": \"eval-spatial-v7-full\",\n      \"on_stove\": \"eval-spatial-v7-full\",\n      \"next_to_plate\": \"eval-spatial-v7-full\",\n      \"on_wooden_cabinet\": \"eval-spatial-v7-full\"\n    }\n  },\n  \"VLA-mean (K=10)\": {\n    \"per_task\": {\n      \"between_plate_and_ramekin\": null,\n      \"next_to_ramekin\": 0.7,\n      \"from_table_center\": 1.0,\n      \"on_cookie_box\": 0.0,\n      \"in_top_drawer\": 0.3,\n      \"on_ramekin\": 0.0,\n      \"next_to_cookie_box\": 0.0,\n      \"on_stove\": 0.8,\n      \"next_to_plate\": 0.0,\n      \"on_wooden_cabinet\": 0.1\n    },\n    \"overall_sr\": 0.3222222222222222,\n    \"n_tasks\": 9,\n    \"complete\": false,\n    \"sources\": {\n      \"next_to_ramekin\": \"eval-vla-mean-spatial\",\n      \"from_table_center\": \"eval-vla-mean-spatial\",\n      \"on_cookie_box\": \"eval-vla-mean-spatial\",\n      \"in_top_drawer\": \"eval-vla-mean-spatial\",\n      \"on_ramekin\": \"eval-vla-mean-spatial\",\n      \"next_to_cookie_box\": \"eval-vla-mean-spatial\",\n      \"on_stove\": \"eval-vla-mean-spatial\",\n      \"next_to_plate\": \"eval-vla-mean-spatial\",\n      \"on_wooden_cabinet\": \"eval-vla-mean-spatial-t10\"\n    }\n  },\n  \"ReconVLA argmin (K=10)\": {\n    \"per_task\": {\n      \"between_plate_and_ramekin\": 0.6,\n      \"next_to_ramekin\": 1.0,\n      \"from_table_center\": 0.0,\n      \"on_cookie_box\": 0.3,\n      \"in_top_drawer\": 0.1,\n      \"on_ramekin\": 0.1,\n      \"next_to_cookie_box\": 0.9,\n      \"on_stove\": 0.0,\n      \"next_to_plate\": 0.4,\n      \"on_wooden_cabinet\": 0.0\n    },\n    \"overall_sr\": 0.33999999999999997,\n    \"n_tasks\": 10,\n    \"complete\": true,\n    \"sources\": {\n      \"between_plate_and_ramekin\": \"eval-reconvla-spatial-v3\",\n      \"next_to_ramekin\": \"eval-reconvla-spatial-v3\",\n      \"from_table_center\": \"eval-reconvla-spatial-v3\",\n      \"on_cookie_box\": \"eval-reconvla-spatial-v3\",\n      \"in_top_drawer\": \"eval-reconvla-spatial-v3\",\n      \"on_ramekin\": \"eval-reconvla-spatial-v3\",\n      \"next_to_cookie_box\": \"eval-reconvla-spatial-v3\",\n      \"on_stove\": \"eval-reconvla-spatial-v3\",\n      \"next_to_plate\": \"eval-reconvla-spatial-v3\",\n      \"on_wooden_cabinet\": \"eval-reconvla-spatial-v3\"\n    }\n  },\n  \"Argmin-only (K=10)\": {\n    \"per_task\": {\n      \"between_plate_and_ramekin\": 0.6,\n      \"next_to_ramekin\": 1.0,\n      \"from_table_center\": 0.0,\n      \"on_cookie_box\": 0.3,\n      \"in_top_drawer\": 0.1,\n      \"on_ramekin\": 0.1,\n      \"next_to_cookie_box\": 0.9,\n      \"on_stove\": 0.0,\n      \"next_to_plate\": 0.3,\n      \"on_wooden_cabinet\": 0.1\n    },\n    \"overall_sr\": 0.33999999999999997,\n    \"n_tasks\": 10,\n    \"complete\": true,\n    \"sources\": {\n      \"between_plate_and_ramekin\": \"eval-argmin-only-spatial-r2\",\n      \"next_to_ramekin\": \"eval-argmin-only-spatial-r2\",\n      \"from_table_center\": \"eval-argmin-only-spatial-r2\",\n      \"on_cookie_box\": \"eval-argmin-only-spatial-r2\",\n      \"in_top_drawer\": \"eval-argmin-only-spatial-r2\",\n      \"on_ramekin\": \"eval-argmin-only-spatial-r2\",\n      \"next_to_cookie_box\": \"eval-argmin-only-spatial-r2\",\n      \"on_stove\": \"eval-argmin-only-spatial-r2\",\n      \"next_to_plate\": \"eval-argmin-only-spatial-r2\",\n      \"on_wooden_cabinet\": \"eval-argmin-only-spatial-r2\"\n    }\n  },\n  \"ACR per-DOF\": {\n    \"per_task\": {\n      \"between_plate_and_ramekin\": 0.6,\n      \"next_to_ramekin\": 1.0,\n      \"from_table_center\": 0.1,\n      \"on_cookie_box\": 0.4,\n      \"in_top_drawer\": 0.0,\n      \"on_ramekin\": 0.0,\n      \"next_to_cookie_box\": 0.9,\n      \"on_stove\": 0.1,\n      \"next_to_plate\": 0.4,\n      \"on_wooden_cabinet\": 0.0\n    },\n    \"overall_sr\": 0.35,\n    \"n_tasks\": 10,\n    \"complete\": true,\n    \"sources\": {\n      \"between_plate_and_ramekin\": \"eval-acr-spatial-v4-small-r2\",\n      \"next_to_ramekin\": \"eval-acr-spatial-v4-small-r2\",\n      \"from_table_center\": \"eval-acr-spatial-v4-small-r2\",\n      \"on_cookie_box\": \"eval-acr-spatial-v4-small-r2\",\n      \"in_top_drawer\": \"eval-acr-spatial-v4-small-r2\",\n      \"on_ramekin\": \"eval-acr-spatial-v4-small-r2\",\n      \"next_to_cookie_box\": \"eval-acr-spatial-v4-small-r2\",\n      \"on_stove\": \"eval-acr-spatial-v4-small-r2\",\n      \"next_to_plate\": \"eval-acr-spatial-v4-small-r2\",\n      \"on_wooden_cabinet\": \"eval-acr-spatial-v4-small-r2\"\n    }\n  },\n  \"ACR obs-only\": {\n    \"per_task\": {\n      \"between_plate_and_ramekin\": 0.9,\n      \"next_to_ramekin\": 1.0,\n      \"from_table_center\": 0.0,\n      \"on_cookie_box\": 0.4,\n      \"in_top_drawer\": 0.1,\n      \"on_ramekin\": 0.0,\n      \"next_to_cookie_box\": 0.9,\n      \"on_stove\": 0.0,\n      \"next_to_plate\": 0.2,\n      \"on_wooden_cabinet\": 0.0\n    },\n    \"overall_sr\": 0.35,\n    \"n_tasks\": 10,\n    \"complete\": true,\n    \"sources\": {\n      \"between_plate_and_ramekin\": \"eval-acr-spatial-v4-obs-only-r3\",\n      \"next_to_ramekin\": \"eval-acr-spatial-v4-obs-only-r3\",\n      \"from_table_center\": \"eval-acr-spatial-v4-obs-only-r3\",\n      \"on_cookie_box\": \"eval-acr-spatial-v4-obs-only-r3\",\n      \"in_top_drawer\": \"eval-acr-spatial-v4-obs-only-r3\",\n      \"on_ramekin\": \"eval-acr-spatial-v4-obs-only-r3\",\n      \"next_to_cookie_box\": \"eval-acr-spatial-v4-obs-only-r3\",\n      \"on_stove\": \"eval-acr-spatial-v4-obs-only-r3\",\n      \"next_to_plate\": \"eval-acr-spatial-v4-obs-only-r3\",\n      \"on_wooden_cabinet\": \"eval-acr-spatial-v4-obs-only-r3\"\n    }\n  },\n  \"ACR scalar\": {\n    \"per_task\": {\n      \"between_plate_and_ramekin\": 0.6,\n      \"next_to_ramekin\": 1.0,\n      \"from_table_center\": 0.1,\n      \"on_cookie_box\": 0.4,\n      \"in_top_drawer\": 0.0,\n      \"on_ramekin\": 0.0,\n      \"next_to_cookie_box\": 0.9,\n      \"on_stove\": 0.0,\n      \"next_to_plate\": 0.1,\n      \"on_wooden_cabinet\": 0.1\n    },\n    \"overall_sr\": 0.32,\n    \"n_tasks\": 10,\n    \"complete\": true,\n    \"sources\": {\n      \"between_plate_and_ramekin\": \"eval-acr-spatial-v4-scalar-r2\",\n      \"next_to_ramekin\": \"eval-acr-spatial-v4-scalar-r2\",\n      \"from_table_center\": \"eval-acr-spatial-v4-scalar-r2\",\n      \"on_cookie_box\": \"eval-acr-spatial-v4-scalar-r2\",\n      \"in_top_drawer\": \"eval-acr-spatial-v4-scalar-r2\",\n      \"on_ramekin\": \"eval-acr-spatial-v4-scalar-r2\",\n      \"next_to_cookie_box\": \"eval-acr-spatial-v4-scalar-r2\",\n      \"on_stove\": \"eval-acr-spatial-v4-scalar-r2\",\n      \"next_to_plate\": \"eval-acr-spatial-v4-scalar-r2\",\n      \"on_wooden_cabinet\": \"eval-acr-spatial-v4-scalar-r2\"\n    }\n  },\n  \"ACR tiny (norm=0.05)\": {\n    \"per_task\": {\n      \"between_plate_and_ramekin\": 0.7,\n      \"next_to_ramekin\": 0.9,\n      \"from_table_center\": 0.0,\n      \"on_cookie_box\": 0.3,\n      \"in_top_drawer\": 0.0,\n      \"on_ramekin\": 0.0,\n      \"next_to_cookie_box\": 0.9,\n      \"on_stove\": null,\n      \"next_to_plate\": null,\n      \"on_wooden_cabinet\": null\n    },\n    \"overall_sr\": 0.39999999999999997,\n    \"n_tasks\": 7,\n    \"complete\": false,\n    \"sources\": {\n      \"between_plate_and_ramekin\": \"eval-tiny-correction-spatial\",\n      \"next_to_ramekin\": \"eval-tiny-correction-spatial\",\n      \"from_table_center\": \"eval-tiny-correction-spatial\",\n      \"on_cookie_box\": \"eval-tiny-correction-spatial\",\n      \"in_top_drawer\": \"eval-tiny-correction-spatial\",\n      \"on_ramekin\": \"eval-tiny-correction-spatial\",\n      \"next_to_cookie_box\": \"eval-tiny-correction-spatial\"\n    }\n  }\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 113_

<details open><summary>🔧 Tool call — Bash · `toolu_013k4Twm9HuChFV4mmBnoS37`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/table1_8seed_final.md 2>/dev/null",
  "description": "Read table1 8seed final"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "uuid": "9e92c654-b2f4-4f69-b0fd-e30edd59af67",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PJhNRxexJC62G1haJeuH9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4241,
      "cache_read_input_tokens": 100094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4241
      },
      "output_tokens": 48,
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

_source line 114 · 2026-05-25T01:56:56.187Z_

<details><summary>↩ Tool result · `toolu_013k4Twm9HuChFV4mmBnoS37`</summary>

```text
# Table 1 — Multi-seed Results (Clean supp-era data)

Generated: 2026-05-24 20:10 UTC

## Main Table

| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |
|-------|---------|-------------|-------------------|--------|--------|
| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |
| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |
| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |
| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |

## Paired t-test: Δ(A-V) = Adaptive - VLA-only

| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
|-------|---------|--------|---------|-----------|-------|
| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |
| Goal | +0.43pp | 0.505 | 0.6314 | 7 | s43-s49 |
| Object | -0.50pp | -0.520 | 0.6306 | 5 | s45-s49 |
| Long | -0.70pp | -0.578 | 0.5940 | 5 | s42,s44-s47 |

## Paired t-test: Δ(A-C) = Adaptive - CRM always-on

| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |
|-------|---------|--------|---------|-----------|-------|
| Spatial | +0.60pp | 0.885 | 0.4263 | 5 | s43-s47 |
| Goal | +0.92pp | 1.309 | 0.2474 | 6 | s42-s47 |
| Object | -0.33pp | -0.249 | 0.8134 | 6 | s42-s47 |
| Long | +1.33pp | 1.315 | 0.2455 | 6 | s42-s47 |

## Trigger Rate ↔ Effect Size (D140 key evidence)

| Suite | Mean Trigger Rate | Δ(A-V) | Correlation |
|-------|------------------|--------|-------------|
| Spatial | 19.8% | +1.75pp | Highest trigger → Strongest positive Δ |
| Goal | 8.6% | +0.43pp | Medium trigger → Small positive Δ |
| Object | 3.8% | -0.50pp | Low trigger → Near zero Δ |
| Long | 4.2% | -0.70pp | Low trigger → Near zero Δ |

## Per-seed Raw Data

### Spatial (8 matched seeds)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | 80.0% | 82.0% | — | +2.0pp |
| s43 | 79.0% | 80.0% | 81.0% | +1.0pp |
| s44 | 78.5% | 80.5% | 78.5% | +2.0pp |
| s45 | 77.0% | 80.0% | 78.0% | +3.0pp |
| s46 | 80.5% | 80.0% | 81.0% | -0.5pp |
| s47 | 80.0% | 81.5% | 80.5% | +1.5pp |
| s48 | 79.5% | 81.0% | — | +1.5pp |
| s49 | 78.5% | 82.0% | — | +3.5pp |

### Goal (7 matched seeds for A-V)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | — | 84.0% | 85.5% | — |
| s43 | 82.5% | 84.5% | 82.0% | +2.0pp |
| s44 | 82.0% | 86.5% | 83.5% | +4.5pp |
| s45 | 83.5% | 81.0% | 81.0% | -2.5pp |
| s46 | 83.0% | 83.5% | 82.0% | +0.5pp |
| s47 | 82.5% | 82.0% | 82.0% | -0.5pp |
| s48 | 85.0% | 84.5% | — | -0.5pp |
| s49 | 82.0% | 81.5% | — | -0.5pp |

### Object (5 matched seeds for A-V)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | — | 81.0% | 77.0% | — |
| s43 | — | 77.5% | 78.5% | — |
| s44 | — | 75.0% | 74.0% | — |
| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |
| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |
| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |
| s48 | 79.0% | 76.0% | — | -3.0pp |
| s49 | 75.5% | 74.0% | — | -1.5pp |

### Long (5 matched seeds for A-V)
| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |
|------|---------|----------|-----|--------|
| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |
| s43 | — | 58.0% | 54.5% | — |
| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |
| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |
| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |
| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |

## Data Gaps
- Goal VLA-only s42: missing
- Object VLA-only s42/s43/s44: missing
- Spatial CRM s42/s48/s49: missing
- Goal/Object CRM s48/s49: missing
- Long VLA-only s43/s48/s49: missing
- Long Adaptive s48/s49: missing

## Note on Spatial VLA-only s42
eval-supp-spatial-vla-only-s42: command has no --model pi05 flag (should be SmolVLA default), but spec metadata shows model_name=pi05 and wall_clock=3.14h (typical for pi05, not SmolVLA ~30min). Needs verification. Current stats include this seed; excluding it would give 7-seed Spatial p-value (still likely significant).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "uuid": "54c2d227-557b-4bcc-be1f-78042b0d40ec",
  "tool_use_result": {
    "stdout": "# Table 1 — Multi-seed Results (Clean supp-era data)\n\nGenerated: 2026-05-24 20:10 UTC\n\n## Main Table\n\n| Suite | VLA-only | CRM (ε=0.05) | Adaptive (τ=0.25) | Δ(A-V) | Δ(A-C) |\n|-------|---------|-------------|-------------------|--------|--------|\n| Spatial | 79.1±1.1 (8s) | 79.8±1.4 (5s) | 80.9±0.9 (8s) | **+1.8pp** | +1.1pp |\n| Goal | 82.9±1.1 (7s) | 82.7±1.6 (6s) | 83.4±1.8 (8s) | +0.5pp | +0.8pp |\n| Object | 77.0±1.8 (5s) | 78.0±2.9 (6s) | 77.0±2.1 (8s) | +0.0pp | -1.0pp |\n| Long | 58.4±1.6 (5s) | 56.4±2.3 (6s) | 57.8±1.9 (6s) | -0.6pp | +1.3pp |\n\n## Paired t-test: Δ(A-V) = Adaptive - VLA-only\n\n| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |\n|-------|---------|--------|---------|-----------|-------|\n| **Spatial** | **+1.75pp** | **4.041** | **0.0049** | **8** | s42-s49 |\n| Goal | +0.43pp | 0.505 | 0.6314 | 7 | s43-s49 |\n| Object | -0.50pp | -0.520 | 0.6306 | 5 | s45-s49 |\n| Long | -0.70pp | -0.578 | 0.5940 | 5 | s42,s44-s47 |\n\n## Paired t-test: Δ(A-C) = Adaptive - CRM always-on\n\n| Suite | Δ(mean) | t-stat | p-value | n matched | Seeds |\n|-------|---------|--------|---------|-----------|-------|\n| Spatial | +0.60pp | 0.885 | 0.4263 | 5 | s43-s47 |\n| Goal | +0.92pp | 1.309 | 0.2474 | 6 | s42-s47 |\n| Object | -0.33pp | -0.249 | 0.8134 | 6 | s42-s47 |\n| Long | +1.33pp | 1.315 | 0.2455 | 6 | s42-s47 |\n\n## Trigger Rate ↔ Effect Size (D140 key evidence)\n\n| Suite | Mean Trigger Rate | Δ(A-V) | Correlation |\n|-------|------------------|--------|-------------|\n| Spatial | 19.8% | +1.75pp | Highest trigger → Strongest positive Δ |\n| Goal | 8.6% | +0.43pp | Medium trigger → Small positive Δ |\n| Object | 3.8% | -0.50pp | Low trigger → Near zero Δ |\n| Long | 4.2% | -0.70pp | Low trigger → Near zero Δ |\n\n## Per-seed Raw Data\n\n### Spatial (8 matched seeds)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | 80.0% | 82.0% | — | +2.0pp |\n| s43 | 79.0% | 80.0% | 81.0% | +1.0pp |\n| s44 | 78.5% | 80.5% | 78.5% | +2.0pp |\n| s45 | 77.0% | 80.0% | 78.0% | +3.0pp |\n| s46 | 80.5% | 80.0% | 81.0% | -0.5pp |\n| s47 | 80.0% | 81.5% | 80.5% | +1.5pp |\n| s48 | 79.5% | 81.0% | — | +1.5pp |\n| s49 | 78.5% | 82.0% | — | +3.5pp |\n\n### Goal (7 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | — | 84.0% | 85.5% | — |\n| s43 | 82.5% | 84.5% | 82.0% | +2.0pp |\n| s44 | 82.0% | 86.5% | 83.5% | +4.5pp |\n| s45 | 83.5% | 81.0% | 81.0% | -2.5pp |\n| s46 | 83.0% | 83.5% | 82.0% | +0.5pp |\n| s47 | 82.5% | 82.0% | 82.0% | -0.5pp |\n| s48 | 85.0% | 84.5% | — | -0.5pp |\n| s49 | 82.0% | 81.5% | — | -0.5pp |\n\n### Object (5 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | — | 81.0% | 77.0% | — |\n| s43 | — | 77.5% | 78.5% | — |\n| s44 | — | 75.0% | 74.0% | — |\n| s45 | 76.0% | 78.0% | 76.5% | +2.0pp |\n| s46 | 79.0% | 77.5% | 79.5% | -1.5pp |\n| s47 | 75.5% | 77.0% | 82.5% | +1.5pp |\n| s48 | 79.0% | 76.0% | — | -3.0pp |\n| s49 | 75.5% | 74.0% | — | -1.5pp |\n\n### Long (5 matched seeds for A-V)\n| Seed | VLA-only | Adaptive | CRM | Δ(A-V) |\n|------|---------|----------|-----|--------|\n| s42 | 58.0% | 59.0% | 56.5% | +1.0pp |\n| s43 | — | 58.0% | 54.5% | — |\n| s44 | 56.5% | 56.0% | 56.5% | -0.5pp |\n| s45 | 57.5% | 60.0% | 60.5% | +2.5pp |\n| s46 | 60.5% | 58.5% | 54.0% | -2.0pp |\n| s47 | 59.5% | 55.0% | 56.5% | -4.5pp |\n\n## Data Gaps\n- Goal VLA-only s42: missing\n- Object VLA-only s42/s43/s44: missing\n- Spatial CRM s42/s48/s49: missing\n- Goal/Object CRM s48/s49: missing\n- Long VLA-only s43/s48/s49: missing\n- Long Adaptive s48/s49: missing\n\n## Note on Spatial VLA-only s42\neval-supp-spatial-vla-only-s42: command has no --model pi05 flag (should be SmolVLA default), but spec metadata shows model_name=pi05 and wall_clock=3.14h (typical for pi05, not SmolVLA ~30min). Needs verification. Current stats include this seed; excluding it would give 7-seed Spatial p-value (still likely significant).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 115_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "uuid": "b18e931c-2e9c-4c9c-910b-bae4bf7f9bbb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KwbGwczCCx4SG5JNGBoHok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2619,
      "cache_read_input_tokens": 104335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2619
      },
      "output_tokens": 60,
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


### Assistant

_source line 116_

I have sufficient data to finalize the audit. Let me also check bjb1-18228's seed42 file mtime more carefully since it shows fresh value.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "uuid": "a8c1136b-8a2c-47dd-97b5-bd6cf5f6e42e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KwbGwczCCx4SG5JNGBoHok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2619,
      "cache_read_input_tokens": 104335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2619
      },
      "output_tokens": 60,
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

_source line 117_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_0185yryGeX74GZkAQS3BSWfA`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "python3 << 'PY'\nimport json,os,datetime\nfiles=[\n '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json',\n '/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json',\n]\nfor f in files:\n  s=os.stat(f); d=json.load(open(f))\n  print(os.path.basename(f),'|mt',datetime.datetime.fromtimestamp(s.st_mtime).isoformat(),'|nr',d.get('n_rollouts'),'|SR',d.get('overall_success_rate'),'|per_task',d.get('per_task_sr', d.get('per_task')))\nPY",
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
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "uuid": "36bd9eff-c8b9-4aef-93b0-444440fecc66",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KwbGwczCCx4SG5JNGBoHok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2619,
      "cache_read_input_tokens": 104335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2619
      },
      "output_tokens": 60,
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

_source line 118 · 2026-05-25T01:58:10.981Z_

<details><summary>↩ Tool result · `toolu_0185yryGeX74GZkAQS3BSWfA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_spatial_vla_only_seed42.json |mt 2026-05-25T02:20:18.734980 |nr 20 |SR 0.8 |per_task {'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.9, 'successes': 18, 'total': 20}, 'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}, 'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}, 'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}, 'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.7, 'successes': 14, 'total': 20}, 'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 20}, 'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 1.0, 'successes': 20, 'total': 20}, 'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate': {'success_rate': 0.8, 'successes': 16, 'total': 20}, 'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate': {'success_rate': 0.8, 'successes': 16, 'total': 20}, 'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}}\\neval_spatial_vla_only_seed43.json |mt 2026-05-19T22:38:45.244052 |nr 10 |SR 0.29 |per_task {'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.7, 'successes': 7, 'total': 10}, 'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.8, 'successes': 8, 'total': 10}, 'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate': {'success_rate': 0.1, 'successes': 1, 'total': 10}, 'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 0.3, 'successes': 3, 'total': 10}, 'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}, 'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}, 'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 0.9, 'successes': 9, 'total': 10}, 'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}, 'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate': {'success_rate': 0.1, 'successes': 1, 'total': 10}, 'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "uuid": "4dbb93c8-6f60-48ed-9657-28d71db62622",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval_spatial_vla_only_seed42.json |mt 2026-05-25T02:20:18.734980 |nr 20 |SR 0.8 |per_task {'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.9, 'successes': 18, 'total': 20}, 'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}, 'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}, 'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}, 'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.7, 'successes': 14, 'total': 20}, 'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 20}, 'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 1.0, 'successes': 20, 'total': 20}, 'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate': {'success_rate': 0.8, 'successes': 16, 'total': 20}, 'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate': {'success_rate': 0.8, 'successes': 16, 'total': 20}, 'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}}\\\\neval_spatial_vla_only_seed43.json |mt 2026-05-19T22:38:45.244052 |nr 10 |SR 0.29 |per_task {'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.7, 'successes': 7, 'total': 10}, 'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.8, 'successes': 8, 'total': 10}, 'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate': {'success_rate': 0.1, 'successes': 1, 'total': 10}, 'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 0.3, 'successes': 3, 'total': 10}, 'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}, 'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}, 'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 0.9, 'successes': 9, 'total': 10}, 'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}, 'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate': {'success_rate': 0.1, 'successes': 1, 'total': 10}, 'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval_spatial_vla_only_seed42.json |mt 2026-05-25T02:20:18.734980 |nr 20 |SR 0.8 |per_task {'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.9, 'successes': 18, 'total': 20}, 'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}, 'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}, 'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}, 'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.7, 'successes': 14, 'total': 20}, 'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 20}, 'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 1.0, 'successes': 20, 'total': 20}, 'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate': {'success_rate': 0.8, 'successes': 16, 'total': 20}, 'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate': {'success_rate': 0.8, 'successes': 16, 'total': 20}, 'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.95, 'successes': 19, 'total': 20}}\\neval_spatial_vla_only_seed43.json |mt 2026-05-19T22:38:45.244052 |nr 10 |SR 0.29 |per_task {'pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.7, 'successes': 7, 'total': 10}, 'pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.8, 'successes': 8, 'total': 10}, 'pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate': {'success_rate': 0.1, 'successes': 1, 'total': 10}, 'pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 0.3, 'successes': 3, 'total': 10}, 'pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}, 'pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}, 'pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate': {'success_rate': 0.9, 'successes': 9, 'total': 10}, 'pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}, 'pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate': {'success_rate': 0.1, 'successes': 1, 'total': 10}, 'pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate': {'success_rate': 0.0, 'successes': 0, 'total': 10}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 119_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_013XUCQQFT5HQ6ueAgL6CPPR`</summary>

```json
{
  "todos": [
    {
      "content": "Identify which seeds/exp_ids feed each Table 1 Spatial cell",
      "status": "completed",
      "activeForm": "Identifying Table 1 Spatial source experiments"
    },
    {
      "content": "Locate JSON files per experiment on each server",
      "status": "completed",
      "activeForm": "Locating JSON files per server"
    },
    {
      "content": "Verify SR / n_rollouts / baseline_mode in each JSON",
      "status": "completed",
      "activeForm": "Verifying JSON contents"
    },
    {
      "content": "Recompute means and compare to Table 1 reported values",
      "status": "in_progress",
      "activeForm": "Recomputing means and comparing"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "uuid": "80cec16f-2810-467d-a6a8-864c282f3b75",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01K9BagLE8u15fiVGUgHHLoH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7180,
      "cache_read_input_tokens": 106954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7180
      },
      "output_tokens": 49,
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

_source line 120 · 2026-05-25T01:58:15.686Z_

<details><summary>↩ Tool result · `toolu_013XUCQQFT5HQ6ueAgL6CPPR`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "uuid": "554a43d8-5b50-470d-a8ea-276a4817e409",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Identify which seeds/exp_ids feed each Table 1 Spatial cell",
        "status": "completed",
        "activeForm": "Identifying Table 1 Spatial source experiments"
      },
      {
        "content": "Locate JSON files per experiment on each server",
        "status": "completed",
        "activeForm": "Locating JSON files per server"
      },
      {
        "content": "Verify SR / n_rollouts / baseline_mode in each JSON",
        "status": "in_progress",
        "activeForm": "Verifying JSON contents"
      },
      {
        "content": "Recompute means and compare to Table 1 reported values",
        "status": "pending",
        "activeForm": "Recomputing means and comparing"
      }
    ],
    "newTodos": [
      {
        "content": "Identify which seeds/exp_ids feed each Table 1 Spatial cell",
        "status": "completed",
        "activeForm": "Identifying Table 1 Spatial source experiments"
      },
      {
        "content": "Locate JSON files per experiment on each server",
        "status": "completed",
        "activeForm": "Locating JSON files per server"
      },
      {
        "content": "Verify SR / n_rollouts / baseline_mode in each JSON",
        "status": "completed",
        "activeForm": "Verifying JSON contents"
      },
      {
        "content": "Recompute means and compare to Table 1 reported values",
        "status": "in_progress",
        "activeForm": "Recomputing means and comparing"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 121_

## Table 1 Spatial 全量溯源审计结果

### 上游数据来源
Table 1 source = `artifacts/_project/data/table1_8seed_final.md`（8-seed 池，每 cell 取 3-seed 子集）。报告数：**78.7±0.3 / 79.8±1.3 / 80.8±1.1**。

---

### [Spatial] [VLA-only] Table 1 = 78.7±0.3 (3 seeds)

**唯一能复现 78.7±0.3 的 seed 子集 = {43, 44, 49}**（值 79.0/78.5/78.5），mean=78.67, std=0.29 ✓
但 paired 标杆 CRM/Adaptive 用的是 seeds {42,43,44} — **三方法 seed 子集不一致**。

| Seed | 报告 SR | JSON 路径（on-disk 现状） | n_rollouts | baseline_mode | mtime | 校验 |
|------|--------|-----|------|----|-----|----|
| 43 | 79.0% | cqa1-32758:`eval_spatial_vla_only_seed43.json` SR=**0.790** | 20 | single | 2026-05-23 | ✓ 与报告一致 |
| 44 | 78.5% | bjb2-28827:`eval_spatial_vla_only_seed44.json` SR=**0.805** | 20 | single | 2026-05-23 07:30 | **🔴 不一致**：on-disk 80.5%，报告 78.5% |
| 49 | 78.5% | cqa1-32758:`eval_spatial_vla_only_seed49.json` SR=**0.785** | 20 | single | 2026-05-25 02:00 | ✓ 与报告一致 |

**重算（按报告值）**: mean=78.67%, std=0.29% → 78.7±0.3 ✓
**重算（按 on-disk 现状）**: mean=(79.0+80.5+78.5)/3=79.33%, std=1.04% → 79.3±1.0 🔴 **不可复现**

🔴 **问题 1**：seed 44 JSON 已被覆盖（registry 历史记录 78.5%，on-disk JSON 现为 80.5%），无法从当前 JSON 复现 Table 1 数值
🔴 **问题 2**：seed 子集 {43,44,49} 与 CRM/Adaptive 的 {42,43,44} 不匹配 → Δ(A-V) = +2.1pp 是 **非配对差值**（paired n=8 真实 Δ=+1.75pp, p=0.0049）

VLA-only s42 同名文件冗余（bjb1-32546 SR=0.30/nr=10 stale, bjb1-18228 SR=0.80/nr=20 fresh, cqa1-32758 SR=0.785/nr=20 fresh），三服务器结果不一致——同一 seed 三个版本。

---

### [Spatial] [CRM ε=0.05] Table 1 = 79.8±1.3 (3 seeds = 42,43,44)

| Seed | 报告 SR | JSON 路径 | n_rollouts | mode | baseline_mode | mtime | 校验 |
|------|--------|-----|----|----|----|----|----|
| 42 | 80.0% | bjb1-32546:`eval_spatial_crm_obs_only_norm0.05_seed42.json` SR=**0.800** | 20 | crm_obs_only | single | 2026-05-23 05:50 | ✓ |
| 43 | 81.0% | bjb1-32546:`eval_spatial_crm_obs_only_norm0.05_seed43.json` SR=**0.810** | 20 | crm_obs_only | single | 2026-05-23 11:08 | ✓ |
| 44 | 78.5% | bjb1-32546:`eval_spatial_crm_obs_only_norm0.05_seed44.json` SR=**0.785** | 20 | crm_obs_only | single | 2026-05-23 11:28 | ✓ |

**重算**: mean=(80+81+78.5)/3=79.83%, std=1.26% → **79.8±1.3 ✓ 完全匹配 Table 1**
所有 JSON 在 bjb1-32546 同服务器，n_rollouts=20，mtime 同日，未被覆盖。 ✅

---

### [Spatial] [Adaptive τ=0.25, ε=0.2] Table 1 = 80.8±1.1 (3 seeds = 42,43,44)

| Seed | 报告 SR (Table 1) | JSON 路径（on-disk 现状） | n_rollouts | mode | baseline_mode | mtime | 校验 |
|------|---|-----|----|----|----|----|----|
| 42 | 82.0% | bjb1-32546:`eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json` SR=**0.795** | 20 | adaptive_conformal_crm | single | **2026-05-24 21:23** | **🔴 不一致** |
| 43 | 80.0% | bjb1-32546:同 _seed43.json SR=**0.800** | 20 | adaptive_conformal_crm | single | 2026-05-23 11:08 | ✓ |
| 44 | 80.5% | bjb1-32546:同 _seed44.json SR=**0.805** | 20 | adaptive_conformal_crm | single | 2026-05-23 11:16 | ✓ |

**重算（按报告 82/80/80.5）**: mean=80.83%, std=1.04% → 80.8±1.0 ≈ Table 1 80.8±1.1 ✓
**重算（按 on-disk 79.5/80/80.5）**: mean=80.0%, std=0.5% → 80.0±0.5 🔴 **不可复现**

🔴 **问题 3**：seed 42 JSON 在 5/24 21:23 UTC 被覆盖（registry `eval-supp-adapt-tau025-spatial-s42-r2` 记录 82.0%，on-disk JSON 现为 79.5%）。若审稿人要求查源文件，**Adaptive 列无法复现** Table 1 数值。

---

### 关键问题总结

| # | 严重性 | 问题 |
|---|------|------|
| P0 | 🔴 高 | **Adaptive s42 JSON 已被覆盖** (mtime 5/24 21:23)：on-disk 79.5%，Table 1 用的 82.0% 仅存在于 registry 历史，无源 JSON |
| P0 | 🔴 高 | **VLA-only s44 JSON 被覆盖**：on-disk 80.5%，Table 1 用的 78.5% 仅存在于 registry 历史 |
| P0 | 🔴 高 | **三方法 seed 子集不一致**：VLA-only 用 {43,44,49}、CRM/Adaptive 用 {42,43,44} → Δ(A-V)=+2.1pp 是非配对差，实际配对 8-seed Δ=+1.75pp |
| P1 | 🟡 中 | VLA-only s42 跨三服务器三种 SR（0.30/0.80/0.785），同名文件未统一 |
| P1 | 🟡 中 | CRM 报告 (3s) 与 8seed_final.md 的 (5s, 79.8±1.4) 不一致；paper 给的 79.8±1.3 实际就是 seed 42-44 三种子，但 8seed 文档备注 "Spatial CRM s42/s48/s49: missing" 与现实不符（s42 JSON 存在） |

CRM 列 ✅ 全部可复现；VLA-only / Adaptive 列均存在 **on-disk JSON 与 Table 1 报告值的实质性不一致**（被后续重跑覆盖）。建议立刻：(1) 锁定/备份当前 bjb1-32546 上的 Adaptive seed42 JSON 旧版（若有），或在 paper 中切换到 8-seed 配对数据（80.9±0.9 Adaptive, 79.1±1.1 VLA-only, paired Δ=+1.75pp, p=0.0049）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "uuid": "efff38c6-36c7-4e61-860c-7a6eaf6a690f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LddKiQGmpnhHwQapeVnbjF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 114134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 346
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

_source line 122_

## Table 1 Spatial 全量溯源审计结果

### 上游数据来源
Table 1 source = `artifacts/_project/data/table1_8seed_final.md`（8-seed 池，每 cell 取 3-seed 子集）。报告数：**78.7±0.3 / 79.8±1.3 / 80.8±1.1**。

---

### [Spatial] [VLA-only] Table 1 = 78.7±0.3 (3 seeds)

**唯一能复现 78.7±0.3 的 seed 子集 = {43, 44, 49}**（值 79.0/78.5/78.5），mean=78.67, std=0.29 ✓
但 paired 标杆 CRM/Adaptive 用的是 seeds {42,43,44} — **三方法 seed 子集不一致**。

| Seed | 报告 SR | JSON 路径（on-disk 现状） | n_rollouts | baseline_mode | mtime | 校验 |
|------|--------|-----|------|----|-----|----|
| 43 | 79.0% | cqa1-32758:`eval_spatial_vla_only_seed43.json` SR=**0.790** | 20 | single | 2026-05-23 | ✓ 与报告一致 |
| 44 | 78.5% | bjb2-28827:`eval_spatial_vla_only_seed44.json` SR=**0.805** | 20 | single | 2026-05-23 07:30 | **🔴 不一致**：on-disk 80.5%，报告 78.5% |
| 49 | 78.5% | cqa1-32758:`eval_spatial_vla_only_seed49.json` SR=**0.785** | 20 | single | 2026-05-25 02:00 | ✓ 与报告一致 |

**重算（按报告值）**: mean=78.67%, std=0.29% → 78.7±0.3 ✓
**重算（按 on-disk 现状）**: mean=(79.0+80.5+78.5)/3=79.33%, std=1.04% → 79.3±1.0 🔴 **不可复现**

🔴 **问题 1**：seed 44 JSON 已被覆盖（registry 历史记录 78.5%，on-disk JSON 现为 80.5%），无法从当前 JSON 复现 Table 1 数值
🔴 **问题 2**：seed 子集 {43,44,49} 与 CRM/Adaptive 的 {42,43,44} 不匹配 → Δ(A-V) = +2.1pp 是 **非配对差值**（paired n=8 真实 Δ=+1.75pp, p=0.0049）

VLA-only s42 同名文件冗余（bjb1-32546 SR=0.30/nr=10 stale, bjb1-18228 SR=0.80/nr=20 fresh, cqa1-32758 SR=0.785/nr=20 fresh），三服务器结果不一致——同一 seed 三个版本。

---

### [Spatial] [CRM ε=0.05] Table 1 = 79.8±1.3 (3 seeds = 42,43,44)

| Seed | 报告 SR | JSON 路径 | n_rollouts | mode | baseline_mode | mtime | 校验 |
|------|--------|-----|----|----|----|----|----|
| 42 | 80.0% | bjb1-32546:`eval_spatial_crm_obs_only_norm0.05_seed42.json` SR=**0.800** | 20 | crm_obs_only | single | 2026-05-23 05:50 | ✓ |
| 43 | 81.0% | bjb1-32546:`eval_spatial_crm_obs_only_norm0.05_seed43.json` SR=**0.810** | 20 | crm_obs_only | single | 2026-05-23 11:08 | ✓ |
| 44 | 78.5% | bjb1-32546:`eval_spatial_crm_obs_only_norm0.05_seed44.json` SR=**0.785** | 20 | crm_obs_only | single | 2026-05-23 11:28 | ✓ |

**重算**: mean=(80+81+78.5)/3=79.83%, std=1.26% → **79.8±1.3 ✓ 完全匹配 Table 1**
所有 JSON 在 bjb1-32546 同服务器，n_rollouts=20，mtime 同日，未被覆盖。 ✅

---

### [Spatial] [Adaptive τ=0.25, ε=0.2] Table 1 = 80.8±1.1 (3 seeds = 42,43,44)

| Seed | 报告 SR (Table 1) | JSON 路径（on-disk 现状） | n_rollouts | mode | baseline_mode | mtime | 校验 |
|------|---|-----|----|----|----|----|----|
| 42 | 82.0% | bjb1-32546:`eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json` SR=**0.795** | 20 | adaptive_conformal_crm | single | **2026-05-24 21:23** | **🔴 不一致** |
| 43 | 80.0% | bjb1-32546:同 _seed43.json SR=**0.800** | 20 | adaptive_conformal_crm | single | 2026-05-23 11:08 | ✓ |
| 44 | 80.5% | bjb1-32546:同 _seed44.json SR=**0.805** | 20 | adaptive_conformal_crm | single | 2026-05-23 11:16 | ✓ |

**重算（按报告 82/80/80.5）**: mean=80.83%, std=1.04% → 80.8±1.0 ≈ Table 1 80.8±1.1 ✓
**重算（按 on-disk 79.5/80/80.5）**: mean=80.0%, std=0.5% → 80.0±0.5 🔴 **不可复现**

🔴 **问题 3**：seed 42 JSON 在 5/24 21:23 UTC 被覆盖（registry `eval-supp-adapt-tau025-spatial-s42-r2` 记录 82.0%，on-disk JSON 现为 79.5%）。若审稿人要求查源文件，**Adaptive 列无法复现** Table 1 数值。

---

### 关键问题总结

| # | 严重性 | 问题 |
|---|------|------|
| P0 | 🔴 高 | **Adaptive s42 JSON 已被覆盖** (mtime 5/24 21:23)：on-disk 79.5%，Table 1 用的 82.0% 仅存在于 registry 历史，无源 JSON |
| P0 | 🔴 高 | **VLA-only s44 JSON 被覆盖**：on-disk 80.5%，Table 1 用的 78.5% 仅存在于 registry 历史 |
| P0 | 🔴 高 | **三方法 seed 子集不一致**：VLA-only 用 {43,44,49}、CRM/Adaptive 用 {42,43,44} → Δ(A-V)=+2.1pp 是非配对差，实际配对 8-seed Δ=+1.75pp |
| P1 | 🟡 中 | VLA-only s42 跨三服务器三种 SR（0.30/0.80/0.785），同名文件未统一 |
| P1 | 🟡 中 | CRM 报告 (3s) 与 8seed_final.md 的 (5s, 79.8±1.4) 不一致；paper 给的 79.8±1.3 实际就是 seed 42-44 三种子，但 8seed 文档备注 "Spatial CRM s42/s48/s49: missing" 与现实不符（s42 JSON 存在） |

CRM 列 ✅ 全部可复现；VLA-only / Adaptive 列均存在 **on-disk JSON 与 Table 1 报告值的实质性不一致**（被后续重跑覆盖）。建议立刻：(1) 锁定/备份当前 bjb1-32546 上的 Adaptive seed42 JSON 旧版（若有），或在 paper 中切换到 8-seed 配对数据（80.9±0.9 Adaptive, 79.1±1.1 VLA-only, paired Δ=+1.75pp, p=0.0049）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 494312,
  "duration_api_ms": 484015,
  "num_turns": 50,
  "stop_reason": "end_turn",
  "session_id": "cfd3b66b-9e77-4e85-b8e3-6eefff9f260a",
  "total_cost_usd": 3.0134890000000008,
  "usage": {
    "input_tokens": 51,
    "cache_creation_input_tokens": 113446,
    "cache_read_input_tokens": 2905693,
    "output_tokens": 33980,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 113446,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2816,
        "cache_read_input_tokens": 114134,
        "cache_creation_input_tokens": 346,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 346
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1755,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00185,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 51,
      "outputTokens": 33980,
      "cacheReadInputTokens": 2905693,
      "cacheCreationInputTokens": 113446,
      "webSearchRequests": 0,
      "costUSD": 3.0116390000000006,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cdbdb4a4-e2f4-4d4c-b307-fe6169e15e76"
}
```

</details>

---
