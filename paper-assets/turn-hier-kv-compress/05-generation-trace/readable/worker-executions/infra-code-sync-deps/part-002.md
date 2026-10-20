# infra code sync deps — Part 2 of 2

**turn hier kv compress** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../infra-code-sync-deps.md) · [Structured JSON](../../../sessions/e5/e5ecb4fd6d7eccae3407.json)

## Round 1

### Tool call

_source line 181_

<details open><summary>🔧 Tool call — Bash · `toolu_01E35cEw72JrwzaseqE3Bzgc`</summary>

```json
{
  "command": "cat /tmp/gt_transfer_cmd.txt",
  "description": "Read the transfer command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "3ab35129-4d91-4c4e-aba9-e1a8b70cf90e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqX9JNe2jB1PaQ3saEUvQs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 370,
      "cache_read_input_tokens": 94285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 370,
        "ephemeral_1h_input_tokens": 0
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

_source line 182 · 2026-05-13T09:49:50.400Z_

<details><summary>↩ Tool result · `toolu_01E35cEw72JrwzaseqE3Bzgc`</summary>

```text
&lt;persisted-output>
Output too large (97.7KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-hier-kv-compress/82c8fd16-0814-4367-94aa-9dec50b3c1e7/tool-results/b11rovsw7.txt

Preview (first 2KB):
python3 -c "import base64; data=base64.b64decode('IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiJHZW5lcmF0ZSBzeW50aGV0aWMgbXVsdGktdHVybiBhZ2VudCB0cmFjZXMgZm9yIFR1cm5LViBldmFsdWF0aW9uLiIiIgoKaW1wb3J0IGFyZ3BhcnNlCmltcG9ydCBqc29uCmltcG9ydCByYW5kb20KaW1wb3J0IHN0cmluZwppbXBvcnQgdXVpZApmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgSGVscGVycwojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVmIHJhbmRfaGV4KG46IGludCkgLT4gc3RyOgogICAgcmV0dXJuICIiLmpvaW4ocmFuZG9tLmNob2ljZXMoc3RyaW5nLmhleGRpZ2l0c1s6MTZdLCBrPW4pKQoKCmRlZiByYW5kX2FscGhhbnVtKG46IGludCkgLT4gc3RyOgogICAgcmV0dXJuICIiLmpvaW4ocmFuZG9tLmNob2ljZXMoc3RyaW5nLmFzY2lpX2xldHRlcnMgKyBzdHJpbmcuZGlnaXRzLCBrPW4pKQoKCmRlZiByYW5kX2RhdGUoeWVhcj0yMDI2KSAtPiBzdHI6CiAgICBtID0gcmFuZG9tLnJhbmRpbnQoMSwgMTIpCiAgICBkID0gcmFuZG9tLnJhbmRpbnQoMSwgMjgpCiAgICByZXR1cm4gZiJ7eWVhcn0te206MDJkfS17ZDowMmR9IgoKCmRlZiByYW5kX2RhdGV0aW1lKHllYXI9MjAyNikgLT4gc3RyOgogICAgcmV0dXJuIGYie3JhbmRfZGF0ZSh5ZWFyKX1Ue3JhbmRvbS5yYW5kaW50KDAsMjMpOjAyZH06e3JhbmRvbS5yYW5kaW50KDAsNTkpOjAyZH06e3JhbmRvbS5yYW5kaW50KDAsNTkpOjAyZH1aIgoKCmRlZiByYW5kX21vbmV5KGxvPTEwLCBoaT01MDAwMCkgLT4gc3RyOgogICAgdiA9IHJhbmRvbS51bmlmb3JtKGxvLCBoaSkKICAgIHJldHVybiBmIiR7djosLjJmfSIKCgpkZWYgcmFuZF9pcCgpIC0+IHN0cjoKICAgIHJldHVybiAiLiIuam9pbihzdHIocmFuZG9tLnJhbmRpbnQoMSwgMjU0KSkgZm9yIF8gaW4gcmFuZ2UoNCkpCgoKZGVmIHJhbmRfZW1haWwoZG9tYWluPSJjb3JwLmNvbSIpIC0+IHN0cjoKICAgIG5hbWUgPSByYW5kb20uY2hvaWNlKFsiYWRtaW4iLCAib3BzIiwgImRlcGxveSIsICJhbmFseXN0IiwgInN1cHBvcnQiLCAiZGV2IiwgImRhdGEiXSkKICAgIHJldHVybiBmIntuYW1lfV97cmFuZF9oZXgoNCl9QHtkb21haW59IgoKCmRlZiByYW5kX3VzZXJfaWQoKSAtPiBzdHI6CiAgICByZXR1cm4gZiJVU1Ite3JhbmRvbS5yYW5kaW50KDEwMDAwMCwgOTk5OTk5KX0iCgoKZGVmIHJhbmRfYWNjb3VudF9pZCgpIC0+IHN0cjoKICAgIHJldHVybiBmIkFDQ1Qte3JhbmRvbS5yYW5kaW50KDEwMDAwMCwgOTk5OTk5KX0iCgoKZGVmIHJhbmRfb3JkZXJfaWQoKSAtPiBzdHI6CiAgICByZXR1cm4gZiJPUkQte3JhbmRvbS5yYW5kaW50KDEwMDAwMCwgOTk5OTk5KX0iCgoKZG
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "a3dc88a6-b2a9-480d-b262-209ff58e41ec"
}
```

</details>

---


### System

_source line 183_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Split into 5 chunks for transfer",
  "usage": {
    "total_tokens": 96727,
    "tool_uses": 24,
    "duration_ms": 132040
  },
  "last_tool_name": "Bash",
  "uuid": "3f1a08f5-c4ba-428e-b2f8-f8bff2c5b87d",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 184_

<details open><summary>🔧 Tool call — Bash · `toolu_01GBAhWcc6MndmxewM7NuTtr`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport base64\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn-hier-kv-compress/eval/generate_traces.py', 'rb') as f:\n    data = f.read()\nb64 = base64.b64encode(data).decode('ascii')\n\n# Split into 5 chunks\nchunk_size = len(b64) // 5 + 1\nchunks = [b64[i:i+chunk_size] for i in range(0, len(b64), chunk_size)]\n\nfor i, c in enumerate(chunks):\n    with open(f'/tmp/gt_chunk_{i}.txt', 'w') as f:\n        f.write(c)\n    print(f\"Chunk {i}: {len(c)} chars\")\n\nprint(f\"Total chunks: {len(chunks)}\")\nPYEOF",
  "description": "Split into 5 chunks for transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "2d33db50-54fa-465e-a684-d45812bf411a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UneiRvuwp2jJSBrm7xsvJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 94655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1903,
        "ephemeral_1h_input_tokens": 0
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

_source line 185 · 2026-05-13T09:49:56.791Z_

<details><summary>↩ Tool result · `toolu_01GBAhWcc6MndmxewM7NuTtr`</summary>

```text
Chunk 0: 19981 chars
Chunk 1: 19981 chars
Chunk 2: 19981 chars
Chunk 3: 19981 chars
Chunk 4: 19976 chars
Total chunks: 5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "c4fecb2f-3319-407e-9bcf-c9ae5261f8f0"
}
```

</details>

---


### System

_source line 186_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Read gt chunk 0",
  "usage": {
    "total_tokens": 97141,
    "tool_uses": 25,
    "duration_ms": 136498
  },
  "last_tool_name": "Bash",
  "uuid": "8009c7b8-1f67-4af5-be33-8d4d6e3c6449",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 187_

<details open><summary>🔧 Tool call — Bash · `toolu_01RXoJ5CXcAu9JQKRjSJwa2c`</summary>

```json
{
  "command": "python3 -c \"\nwith open('/tmp/gt_chunk_0.txt') as f:\n    print(f.read(), end='')\n\"",
  "description": "Read gt chunk 0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "5020ad48-b6b9-4916-9c9a-3c9ecd97cb6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NReK2rGai5wMYsfaktozj8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 412,
      "cache_read_input_tokens": 96558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 412,
        "ephemeral_1h_input_tokens": 0
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

_source line 188 · 2026-05-13T09:50:01.256Z_

<details><summary>↩ Tool result · `toolu_01RXoJ5CXcAu9JQKRjSJwa2c`</summary>

```text
[ATTACHMENT_DATA_REDACTED]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "fc804fdd-8732-49ed-bed4-db32a4021179"
}
```

</details>

---


### System

_source line 189_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Compress both files and check sizes",
  "usage": {
    "total_tokens": 114008,
    "tool_uses": 26,
    "duration_ms": 148644
  },
  "last_tool_name": "Bash",
  "uuid": "0a044e3f-f7bc-4e25-804f-879b136a1599",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 190_

<details open><summary>🔧 Tool call — Bash · `toolu_01ANzhDAEKi8UsMxCKRZcTTw`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport base64, gzip\n\n# Read and compress generate_traces.py\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn-hier-kv-compress/eval/generate_traces.py', 'rb') as f:\n    data = f.read()\n\ncompressed = gzip.compress(data, compresslevel=9)\nb64 = base64.b64encode(compressed).decode('ascii')\nprint(f\"Original: {len(data)} bytes\")\nprint(f\"Compressed: {len(compressed)} bytes\")\nprint(f\"Base64: {len(b64)} chars\")\n\n# Write to file\nwith open('/tmp/gt_compressed_b64.txt', 'w') as f:\n    f.write(b64)\n\n# Now do the same for traces.json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn-hier-kv-compress/data/synthetic_traces/traces.json', 'rb') as f:\n    data2 = f.read()\n\ncompressed2 = gzip.compress(data2, compresslevel=9)\nb64_2 = base64.b64encode(compressed2).decode('ascii')\nprint(f\"\\ntraces.json:\")\nprint(f\"Original: {len(data2)} bytes\")\nprint(f\"Compressed: {len(compressed2)} bytes\")\nprint(f\"Base64: {len(b64_2)} chars\")\n\nwith open('/tmp/tj_compressed_b64.txt', 'w') as f:\n    f.write(b64_2)\nPYEOF",
  "description": "Compress both files and check sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "e110e980-bf74-43ca-a879-b64b26fd1795",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EffzhsRSPySgXMe79eZLV5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16865,
      "cache_read_input_tokens": 96970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16865,
        "ephemeral_1h_input_tokens": 0
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

_source line 191 · 2026-05-13T09:50:13.424Z_

<details><summary>↩ Tool result · `toolu_01ANzhDAEKi8UsMxCKRZcTTw`</summary>

```text
Original: 74925 bytes
Compressed: 20387 bytes
Base64: 27184 chars

traces.json:
Original: 653538 bytes
Compressed: 87681 bytes
Base64: 116908 chars
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "6112cd2c-7e89-4d81-8453-1551098e84a4"
}
```

</details>

---


### System

_source line 192_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Read compressed base64 of generate_traces.py",
  "usage": {
    "total_tokens": 114639,
    "tool_uses": 27,
    "duration_ms": 155193
  },
  "last_tool_name": "Bash",
  "uuid": "b87c028e-8c09-4b07-8284-3ba1180ffa70",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 193_

<details open><summary>🔧 Tool call — Bash · `toolu_01B7ktEMbRg9TNZybgZ37qgt`</summary>

```json
{
  "command": "cat /tmp/gt_compressed_b64.txt",
  "description": "Read compressed base64 of generate_traces.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "737a707d-1e08-4950-a146-245d368ceeda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mjjaseXhkk9p1hhvcZsb1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 113835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 627,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 194 · 2026-05-13T09:50:19.936Z_

<details><summary>↩ Tool result · `toolu_01B7ktEMbRg9TNZybgZ37qgt`</summary>

```text
[ATTACHMENT_DATA_REDACTED]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "7e5ca3a6-e90c-4508-9fee-f512025d7071"
}
```

</details>

---


### System

_source line 195_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Build SSH command for generate_traces.py transfer",
  "usage": {
    "total_tokens": 138352,
    "tool_uses": 28,
    "duration_ms": 163845
  },
  "last_tool_name": "Bash",
  "uuid": "d4afc0fb-516f-4382-aa2c-2e6949e6ec22",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 196_

<details open><summary>🔧 Tool call — Bash · `toolu_017N47punT2s1yEz7MR6s5qA`</summary>

```json
{
  "command": "python3 -c \"\nwith open('/tmp/gt_compressed_b64.txt') as f:\n    b64 = f.read().strip()\n# Build the ssh command\ncmd = f\\\"\\\"\\\"cat << 'B64EOF' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); open(\\\"/root/turn-hier-kv-compress/eval/generate_traces.py\\\",\\\"wb\\\").write(data); print(f\\\"Wrote {len(data)} bytes\\\")'\n{b64}\nB64EOF\\\"\\\"\\\"\nwith open('/tmp/gt_ssh_cmd.txt', 'w') as f:\n    f.write(cmd)\nprint(f'Command length: {len(cmd)}')\" ",
  "description": "Build SSH command for generate_traces.py transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "59ba913e-5068-4e28-857c-03d2bdb3ec73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADnxg3DQZc8cDdaxqwYqAY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23711,
      "cache_read_input_tokens": 114462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23711,
        "ephemeral_1h_input_tokens": 0
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

_source line 197 · 2026-05-13T09:50:28.931Z_

<details><summary>↩ Tool result · reported error · `toolu_017N47punT2s1yEz7MR6s5qA`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 5, in &lt;module>
    cmd = f"""cat << 'B64EOF' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); open("/root/turn-hier-kv-compress/eval/generate_traces.py","wb").write(data); print(f"Wrote {len(data)} bytes")'
                                                                                                                                                                                                                                       ^^^^
NameError: name 'data' is not defined
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "df94a305-1617-4843-9b57-904c635807b6",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 5, in &lt;module>\n    cmd = f\"\"\"cat << 'B64EOF' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); open(\"/root/turn-hier-kv-compress/eval/generate_traces.py\",\"wb\").write(data); print(f\"Wrote {len(data)} bytes\")'\n                                                                                                                                                                                                                                       ^^^^\nNameError: name 'data' is not defined"
}
```

</details>

---


### System

_source line 198_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Build SSH command for generate_traces.py transfer",
  "usage": {
    "total_tokens": 138883,
    "tool_uses": 29,
    "duration_ms": 170197
  },
  "last_tool_name": "Bash",
  "uuid": "f41d0ffa-1082-4f69-af68-666db4122358",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 199_

<details open><summary>🔧 Tool call — Bash · `toolu_01DCPs4mV29SQNgKSgGdAJRf`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nwith open('/tmp/gt_compressed_b64.txt') as f:\n    b64 = f.read().strip()\n\ncmd = \"cat << 'B64EOF' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); f=open(\\\"/root/turn-hier-kv-compress/eval/generate_traces.py\\\",\\\"wb\\\"); f.write(data); f.close(); print(\\\"Wrote \\\" + str(len(data)) + \\\" bytes\\\")'\\n\" + b64 + \"\\nB64EOF\"\n\nwith open('/tmp/gt_ssh_cmd.txt', 'w') as f:\n    f.write(cmd)\nprint(f'Command length: {len(cmd)}')\nPYEOF",
  "description": "Build SSH command for generate_traces.py transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "741feffa-01f4-4cd1-bfed-6817f41c9ca7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWPeespRH3jWah7m9zNnks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 138173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 466,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 200 · 2026-05-13T09:50:34.968Z_

<details><summary>↩ Tool result · `toolu_01DCPs4mV29SQNgKSgGdAJRf`</summary>

```text
Command length: 27450
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "7ae42d78-640d-4274-ae98-c5f0906e26f9"
}
```

</details>

---


### System

_source line 201_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Verify command structure",
  "usage": {
    "total_tokens": 139242,
    "tool_uses": 30,
    "duration_ms": 175057
  },
  "last_tool_name": "Bash",
  "uuid": "241b1e5c-164e-43e3-9bd2-e2ffedf91c19",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 202_

<details open><summary>🔧 Tool call — Bash · `toolu_01L8hEFAhXnZuLEdhgLL2VYN`</summary>

```json
{
  "command": "cat /tmp/gt_ssh_cmd.txt | head -3 && echo \"...\" && cat /tmp/gt_ssh_cmd.txt | tail -3",
  "description": "Verify command structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "c8718396-832e-4ae0-b3f3-f0dbdc080bae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QP1YB8NLFuo3aJcQp9UJHy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 138639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 308,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
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

_source line 203 · 2026-05-13T09:50:39.806Z_

<details><summary>↩ Tool result · `toolu_01L8hEFAhXnZuLEdhgLL2VYN`</summary>

```text
&lt;persisted-output>
Output too large (53.6KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-hier-kv-compress/82c8fd16-0814-4367-94aa-9dec50b3c1e7/tool-results/bofgf0xfc.txt

Preview (first 2KB):
cat << 'B64EOF' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); f=open("/root/turn-hier-kv-compress/eval/generate_traces.py","wb"); f.write(data); f.close(); print("Wrote " + str(len(data)) + " bytes")'
H4sIAAAAAAAC/81963rbxpLg/zxFHyYZkT4UJVGWj8M5Go9syY4mvh1JTibraGmIBEkcgQADgJIZLffbh9gn3CfZuvUNAHXP7viHRYKN7urq6rp1VfW3f9mY59nGWZRshMmFmi2KSZpsf9NoNN6ESZgFRajyRVJMwiIaqOk8LqL1Yp4lKhiHSaGKLBiEuRqlmTqBpz/9rMKLIJ4HRZQmHejjm2+i6SzNChVk41mQ5aH+/s88TfTnLEiG6VR/y4ssSsb623weDb8ZZelUzYJiEkdnSn74CF+/+eZbtf54/6C3H8N4Fmb5I/f7zTAc0Sz7k/BrM+mpKClaav3fcK69bxT8y0JCaqPR+WcaJU3GSGcwSSNAb5NR0oGXh9E4KvLPva1np211vpu0Wt84vQfxbBIk8+n9hwjyQRT147AoAAvqr7IYHR62ZsQh0EdzEQbZbnez+8wfcKp2ZWk7+AcAam611Va3Rb8Oa3/tPm+5wI4aV9j5cv1q2tvsDuHvkP42yjAU0XQlHLYvH+TW8uSqBMFmu7vdohF61Z92frjxp//mATZNk3DRjNPdrc22mkS7O5vwz4ftwmJhnkSwjabQHhuX0PDd1UWv3emO/JlHs2b9GndkkeGHZg2Sd562WrRn+0Am2NU4bD71FzacBlHchBeDKNltDNJs1hmk04Y/XBJMQzsBJqXm50YwnEZJo60a6SzHP8NwFqcL/BQkQbzIC/yYz2e4j/n3C/oTFEHjtLz+OMayf2V2z9PW8t+vGC4fGfM8zPrRsLli8T8dH62XF24LFwTW5gf61/L7CwaDdJ4U13S59+rVyd36TLPhtUB+ONq/W4fAlM/D62A8+WkFiNJhedKzqH8OROv3NpoWNcucn68XYV6sXy1x9V7CjgozxV/2Ph7+dPCr/FKk533+BD3js9IaT4sOEn5QNH0m1i2R5DyLS3DlF4M68ptFhpyQ5ubFBP+eRXEMvAw/JmkRjYggc4B6MNEQXcAEqv1dbGHLiy79v22hz2vaIhESzdNK0yehI/oM4jLJgwFKR/qehbgH6GN4EWKjMv1PimKW9zY2rmCuy074NZjO4hC34sYVQLvcuAI4/CWcBXl+CcOXcTULB1EQV2Bu/OXfv/3u+//+L08apZFPprOPV/LW8spfmuetZZWo2kJNjy2TP8ZBUoTD9SgZpQq1i1CNWTVJH19SH75//aH/5uD9wdHeyYejY0DXFaGlITuj0VNxMD0bBr3Shmlzs0GajKJxn8AstXXohNrSzmpMg699wHkWhfluGafd9tYmoLTtNEdBl86L3Rr0b3XLjVF768fRNLLtNQTAA9ogj9rIC/ADf9o8LfVwFhSDST+P/girPTxrb3fbz57CuM/b3Z1n5VcBE4N5loXJYFE3sWem+anGnea4tHNvgzv9wlkAJDIIe+rKkbtbLo9zARNBoVsbueG3suxfN3QFQmmqWTiMCsZ0BQiAggW//w5IxCAuFv0ZyOkil7ccFO1UXzSIAk7YD5MhvVomSOKSmhgBLuAqsIFvhU7EBIpbPQXWAUpwa/aiG1l247cbnvWBApKQmF1PzdK8GAOv+j0GZjY8w6F6JaYCmuHy34dnHZgUwhH3dp5udzdmWToszx9VuP4wDIbA0G+3y3RjDTUpgdVVhKcAUOG2Is2yvK+A/VwGMf1+XY9J+BWIk+VOfTszJUBAmEUD6BSQBFbWbel/DgbYwlKPViI3O8+BfDY7QPy9ztNRiYekB
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "d7296aa5-2845-457e-9cfa-7a1159ecae67"
}
```

</details>

---


### System

_source line 204_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Verify command is ready",
  "usage": {
    "total_tokens": 141081,
    "tool_uses": 31,
    "duration_ms": 182517
  },
  "last_tool_name": "Bash",
  "uuid": "d4de9652-2148-4eca-b0a2-a59a10a2b05a",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 205_

<details open><summary>🔧 Tool call — Bash · `toolu_016BeFEpRrzRqondapgXMAyX`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nwith open('/tmp/gt_ssh_cmd.txt') as f:\n    cmd = f.read()\n# Write a JSON-safe version\nimport json\nprint(json.dumps(cmd)[:100])\nprint(\"...\")\nprint(f\"Total length: {len(cmd)}\")\nPYEOF",
  "description": "Verify command is ready"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "a9043ce2-7dd2-4462-ad20-5fa0b3850fe6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012H5HRh2bTcbenoqoUEHK44",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1837,
      "cache_read_input_tokens": 138947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1837,
        "ephemeral_1h_input_tokens": 0
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

_source line 206 · 2026-05-13T09:50:47.273Z_

<details><summary>↩ Tool result · `toolu_016BeFEpRrzRqondapgXMAyX`</summary>

```text
"cat << 'B64EOF' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.std
...
Total length: 27450
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "41616956-34ca-4ffc-8f09-4a7190ceecd8"
}
```

</details>

---


### System

_source line 207_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Get clean b64 content",
  "usage": {
    "total_tokens": 141386,
    "tool_uses": 32,
    "duration_ms": 186879
  },
  "last_tool_name": "Bash",
  "uuid": "be8cc5cb-22d8-4397-b275-bef05d64746e",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 208_

<details open><summary>🔧 Tool call — Bash · `toolu_012vhhAGrc4htzW8zBbMReij`</summary>

```json
{
  "command": "python3 -c \"\nwith open('/tmp/gt_compressed_b64.txt') as f:\n    b64 = f.read().strip()\nprint(b64)\n\" > /tmp/gt_b64_only.txt && wc -c /tmp/gt_b64_only.txt",
  "description": "Get clean b64 content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "e23a393c-3331-4ad8-8740-56b5f9011e00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BydSq9Bop6dkxjKC1AdRAk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 245,
      "cache_read_input_tokens": 140784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 245,
        "ephemeral_1h_input_tokens": 0
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

_source line 209 · 2026-05-13T09:50:51.633Z_

<details><summary>↩ Tool result · `toolu_012vhhAGrc4htzW8zBbMReij`</summary>

```text
27185 /tmp/gt_b64_only.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "4e627ac0-567e-42c4-9161-3ea46acc6d03"
}
```

</details>

---


### System

_source line 210_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Build echo-based transfer command",
  "usage": {
    "total_tokens": 141559,
    "tool_uses": 33,
    "duration_ms": 193224
  },
  "last_tool_name": "Bash",
  "uuid": "df8b2346-00a4-400c-8cf8-29455f01b25f",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 211_

<details open><summary>🔧 Tool call — Bash · `toolu_01HAfu5atftnLTobtdqktG6q`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nwith open('/tmp/gt_compressed_b64.txt') as f:\n    b64 = f.read().strip()\nwith open('/tmp/gt_ssh_cmd.txt', 'w') as f:\n    f.write(f\"echo '{b64}' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); f=open(\\\"/root/turn-hier-kv-compress/eval/generate_traces.py\\\",\\\"wb\\\"); f.write(data); f.close(); print(\\\"Wrote \\\" + str(len(data)) + \\\" bytes\\\")'\")\nwith open('/tmp/gt_ssh_cmd.txt') as f:\n    content = f.read()\nprint(f\"Length: {len(content)}\")\nPYEOF",
  "description": "Build echo-based transfer command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "e219dc7b-22f5-4c09-a347-fcb657e9ddd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DdDH4Go4Hdf7TDEiNUFUM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 171,
      "cache_read_input_tokens": 141029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 171,
        "ephemeral_1h_input_tokens": 0
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

_source line 212 · 2026-05-13T09:50:57.986Z_

<details><summary>↩ Tool result · `toolu_01HAfu5atftnLTobtdqktG6q`</summary>

```text
Length: 27434
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "dfcf64a8-179f-4336-90dc-6e7bf0b92728"
}
```

</details>

---


### System

_source line 213_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Reading /tmp/gt_ssh_cmd.txt",
  "usage": {
    "total_tokens": 141901,
    "tool_uses": 34,
    "duration_ms": 197284
  },
  "last_tool_name": "Read",
  "uuid": "ff75e18e-78d1-4063-b1d6-582a831bc212",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 214_

<details open><summary>🔧 Tool call — Read · `toolu_016jdhe3Tg8a4fTwAVFNLPL6`</summary>

```json
{
  "file_path": "/tmp/gt_ssh_cmd.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "d436c003-d0c4-4d59-a132-321b62e52654",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RBQC7GHjKSffMc33sSMgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 141200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 340,
        "ephemeral_1h_input_tokens": 0
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

_source line 215 · 2026-05-13T09:51:02.343Z_

<details><summary>↩ Tool result · `toolu_016jdhe3Tg8a4fTwAVFNLPL6`</summary>

```text
1	echo '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' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); f=open("/root/turn-hier-kv-compress/eval/generate_traces.py","wb"); f.write(data); f.close(); print("Wrote " + str(len(data)) + " bytes")'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "fadc32b0-c6b4-46d8-88cc-7f0d8bff3e22"
}
```

</details>

---


### System

_source line 216_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Get command for clipboard",
  "usage": {
    "total_tokens": 165646,
    "tool_uses": 35,
    "duration_ms": 205050
  },
  "last_tool_name": "Bash",
  "uuid": "aee4400c-96f8-45f1-aefd-59599e172dcf",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 217_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vjqhnpozr1bTqhNXSmCtKB`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nwith open('/tmp/gt_ssh_cmd.txt') as f:\n    cmd = f.read()\nprint(cmd)\nPYEOF",
  "description": "Get command for clipboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "2575b620-450e-43df-9513-8e213130ff0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Vc3NVFgS3NTjvhYebgwbK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23743,
      "cache_read_input_tokens": 141540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23743,
        "ephemeral_1h_input_tokens": 0
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

_source line 218 · 2026-05-13T09:51:09.797Z_

<details><summary>↩ Tool result · `toolu_01Vjqhnpozr1bTqhNXSmCtKB`</summary>

```text
echo 'H4sIAAAAAAAC/81963rbxpLg/zxFHyYZkT4UJVGWj8M5Go9syY4mvh1JTibraGmIBEkcgQADgJIZLffbh9gn3CfZuvUNAHXP7viHRYKN7urq6rp1VfW3f9mY59nGWZRshMmFmi2KSZpsf9NoNN6ESZgFRajyRVJMwiIaqOk8LqL1Yp4lKhiHSaGKLBiEuRqlmTqBpz/9rMKLIJ4HRZQmHejjm2+i6SzNChVk41mQ5aH+/s88TfTnLEiG6VR/y4ssSsb623weDb8ZZelUzYJiEkdnSn74CF+/+eZbtf54/6C3H8N4Fmb5I/f7zTAc0Sz7k/BrM+mpKClaav3fcK69bxT8y0JCaqPR+WcaJU3GSGcwSSNAb5NR0oGXh9E4KvLPva1np211vpu0Wt84vQfxbBIk8+n9hwjyQRT147AoAAvqr7IYHR62ZsQh0EdzEQbZbnez+8wfcKp2ZWk7+AcAam611Va3Rb8Oa3/tPm+5wI4aV9j5cv1q2tvsDuHvkP42yjAU0XQlHLYvH+TW8uSqBMFmu7vdohF61Z92frjxp//mATZNk3DRjNPdrc22mkS7O5vwz4ftwmJhnkSwjabQHhuX0PDd1UWv3emO/JlHs2b9GndkkeGHZg2Sd562WrRn+0Am2NU4bD71FzacBlHchBeDKNltDNJs1hmk04Y/XBJMQzsBJqXm50YwnEZJo60a6SzHP8NwFqcL/BQkQbzIC/yYz2e4j/n3C/oTFEHjtLz+OMayf2V2z9PW8t+vGC4fGfM8zPrRsLli8T8dH62XF24LFwTW5gf61/L7CwaDdJ4U13S59+rVyd36TLPhtUB+ONq/W4fAlM/D62A8+WkFiNJhedKzqH8OROv3NpoWNcucn68XYV6sXy1x9V7CjgozxV/2Ph7+dPCr/FKk533+BD3js9IaT4sOEn5QNH0m1i2R5DyLS3DlF4M68ptFhpyQ5ubFBP+eRXEMvAw/JmkRjYggc4B6MNEQXcAEqv1dbGHLiy79v22hz2vaIhESzdNK0yehI/oM4jLJgwFKR/qehbgH6GN4EWKjMv1PimKW9zY2rmCuy074NZjO4hC34sYVQLvcuAI4/CWcBXl+CcOXcTULB1EQV2Bu/OXfv/3u+//+L08apZFPprOPV/LW8spfmuetZZWo2kJNjy2TP8ZBUoTD9SgZpQq1i1CNWTVJH19SH75//aH/5uD9wdHeyYejY0DXFaGlITuj0VNxMD0bBr3Shmlzs0GajKJxn8AstXXohNrSzmpMg699wHkWhfluGafd9tYmoLTtNEdBl86L3Rr0b3XLjVF768fRNLLtNQTAA9ogj9rIC/ADf9o8LfVwFhSDST+P/girPTxrb3fbz57CuM/b3Z1n5VcBE4N5loXJYFE3sWem+anGnea4tHNvgzv9wlkAJDIIe+rKkbtbLo9zARNBoVsbueG3suxfN3QFQmmqWTiMCsZ0BQiAggW//w5IxCAuFv0ZyOkil7ccFO1UXzSIAk7YD5MhvVomSOKSmhgBLuAqsIFvhU7EBIpbPQXWAUpwa/aiG1l247cbnvWBApKQmF1PzdK8GAOv+j0GZjY8w6F6JaYCmuHy34dnHZgUwhH3dp5udzdmWToszx9VuP4wDIbA0G+3y3RjDTUpgdVVhKcAUOG2Is2yvK+A/VwGMf1+XY9J+BWIk+VOfTszJUBAmEUD6BSQBFbWbel/DgbYwlKPViI3O8+BfDY7QPy9ztNRiYekBYwzgBXxiXUHXtmqI1UAGXZxf/bDD9WRtphMYZit0XKaey+GWZZm/cxiyYNwc3MLQdzcqQNxkqXz8WQ2L6o7gza2wAni6veNvIzMHHTMcNqPEpB+cyLAW6Cz8T5E+Z/B/yAmweBVoMUo4O2qSBXsNiWy3b6wF18Gixy1BtAmVERbrViosxAmCFbzJEDbSQnbUMOwgO3kdXCQw4KjhQ0jTObTIFGiFatoRBDgkDjFOehZuQrg42gOkKQI6HeAdbez/VSBXqOGUT6I0zxUehupGdAVAoJon8eBB8HbFACMY4Us9yyAty6zCOBJZyheUUtB0BCSYA4cDs39KHbfPwLo14nvoUI0gxdCeiUo1BToS+0o6EmBOTCHXtHiGGVhuF5E8NBFJ67cUpSYaXAeikQEKdr/PWii4O8XixlQESxom3UA+ZwPwgTwnNJX0niKOWhIn/nHIjtl7afRaByxYtMkZMLU2ir8CtoN7fgkvwwzNokCNWN9Q+Gw5MPADoCeZrhUudEISlqBJST64ZcJoCDKfTrCZ5dBjlMfImO7AJoZvnDwSa++AjpYpHMYEhYGDCxGP/wP5DWgVcHeKq/RiHooGJk1kTmIAJoXsCImB0D7BVA+0mWY5243p87ClvSYa2Z3tTRDMXB5WBRAb/UAsv6GSIBmBNjVchUMJX3gGhgG87xIgYGu5aXuPITGaXqu5jOBetWoJeF6zai6lfp09Jamgg8FvTWzjwYTWh/zGmIBGEDs04C3Cq4Ar4MEbC4aNU7HYMnb5nk99u2SXQOuC0BZ0l6DDd1KpciyYti8yPTg/RpQwsQBJR9MwuH8GizUyMY6OBCd2KVprri5YiurZqeVcEK0uQqIWplyDTq4/TrgIYyV8xZAMw6yITLkYoJt01k0qIcsA6TwVkErbBQRT3I6B86eTmdFDcTAS/EPcALQzzI03mlunXwWR0Wzsdtofd481d968g04LvqTQPRAAxyJ9yosJzSx38OYhIuw5A4gNw7QjuyjFavEivy97zJM87kzDgvLztvqc2kJXmj79/eKner02NL+Aj0/z3L9XQTE4xuixy7WHYnQ7G5uroM0hrU8D0FkhsFg0npsw/T41+OTg3f9j0cf3n08cexSzfr6ojr0yTEPtNm0tPsrMD/kFIFhlEbRYDc++e/DweR9ehGow2TQaUPb4yA4RmFYILYViyskW1Av5sN11BaG+PSfIENBaCfQ05SOBNI0zjuq4Q2fafUgAnU4AvmfAwkN4vkQ5Dj8ksYX1LOGLkp+n0doEqvgDKxdo0PlRVDM87YSnRqgBG0on5/lA6Bd2l0WkH91QShAnTyLw3ySpgVtPZhsQjwiynNQCJBjofKv1R097X/FGaKcxJdY+8ppUFQS1GCCrtOcdJwBEEWQLMDQiaPBwhsc24es6tEsU/ThfNUjawVrBiOBqobqoFHdijCYdn5Lfkuc3r79Vn3EMQA73vN19TMrohaLqzRSALOklaozeJSfi5qIAEW4ZOMIKB41CDIFkRXo9w73O6XRjwQ78B9qp6Cgg3BLYGyNQmRf0ylYyjDFeNExL5yFxWUIEgFfWUetljTeCADmxcwYN7CpAXXD0L5o1GA1hSnjSILlcFgG7kqUun6VjS8r82A9VqHlp47f7vXUKMpyq+Cqywg4d6K6otcCPRIJz4kA9Y9P1QTIPi8D8gk7xh2C664VEo1U5IzI2Eg7dXyFCgRFkWaLGnqX9ashkr0L+CEAolcnOF4Jji849nymnRpNWuB+ip6Q1peeYmU5r5AJb1okE0Ro22xIhEu8MOUZfwGe33cdn03rSGmDgrDId7c33TGzcCBHi+aVSp/zGWkmLiq8bsE+7yOE2O8r2aUkOF3cYYNKz0Ksfd7sXqfBFD/iagd5Sl1/FMq2tlmlP/YqiKPe6w50+XBMqzoMDVAEML2CfMZyAs2vuZ/ycr+yur7WLnuW5kGj9Yn8WEwAsRacpmLPmObWrTkM+wGwQVjw5AYZk4dJBJwiT0fFJT4JE9BNw5BZj+6C9onYIGQwAhJAU0pnJEPC5CLK0gQ/lyUJMZXwazhAixLBovUYEgWy8TqKYtqTc9CV0G5m6hyGZ/Ox8NxKn5dpdq6AIgL1kc6/N05APTmmNQE7NklRgxSI1esgLxBxZwGsRMIDH4HIBykKIBch0UB5M/4CA+Qz0JNK5PFR5GcGcqmnvmxc6nYbwPO+lBq/5BEr7TYElI0vqsnwq+3O1lZbg9pWx/94uxeDmj1dtEp9vhaYq53q2WCvFh1tmevW87b6GbBd7m9fHAmwN9jjB0OrrR10CHwxVGbtlOWXKq7ezEFwoSWR35+Ji2vG0IAKRgU6IgIScSK3Yc6zBf6s13KD2m6U8f46jeP0kk2+r0C+LMSHwE2KRQzyiHg6YAjYdFIgjxQqIgdEBMiy6Cuzh1eu5ezsQ7aol3fm6rIx+gheE/oaz2GrtglaYrFzDRvK8nyCHgZQR0DODqs8FrdVHzdTE0MvmEPDRsMnaPEXeF5VeYm2oH2rrVvi67/Q9qTNjg0q7/JhHMGOJISemmyBLx6DdELnh+IWwDayNBfLXxpXoZ8nfVpOA/2BMA1a8XwOsHTKbA49DX0+pI7y67kcNlW66XV8TRTDtZxfQZYImgFAXMfYkGBxx+DUI+RioFqS+o2CFkkPVVY9KjO2sQ7TkcNEr98TNMy9YWlBggg9e0hGHLuTB8QyteaI42bpELaWjHEZnvGoAECdroG7Xh2DvjOobNov1HeHz0NhFT7gB5Tx8CRnbA1Ad5oCQE19PG4hoS8CiyeDrbNeKyGt+oHNnFCwas0YeiQpoZreQHj40WZdF3oNxyh/2iqORnQKwM6wFcNofLFSgB9RvgdxOlZNF34ewop+dM7SBs2LSs8W4zMgxYsovMTuf4G1AN1oNIL90MzRNEkTRhNtdYQUEDKdgVohfAUl5CjMsjBrVdmPnNBIpI/LgiyT/lN5NGA1QmWOaH4hPptc2ywz+I5QJOMOKHLh4Jzo9f2nt2/ZymdrDGzEOAqr2vYRbQkU4aC/QufyCnDoT8f7THxd0AwG0RT95OjHqHSxH+STszTIhohEAGai5DzjoawaGRRNuZn/Hrv8KTAcYEGTE7+GIKaqYAJ/QZaPuyBv4mZvqym6zwc5KZP8s8dA8jmwfOQvq7TViyifw7L8QeQjfYLQzArx26Skq1L/JkqQfq/2GH4lrwQzpybbN55UOPjKjohcfdx/vfHq+OeNg6+DMK7wZlRNrXV/LXNOSLN1fBKWPSP1vEIHxhuAua2bjuELEKMx+yu8GSTlTGuoGBnHeKLl4WG0Lp23reOdKEXR6Qg5K9DjDdYeMNMJGF/QsuQjADKNwMyjruY5dFpn+mt/zD5bZOU9haFXwAmSML7OAFhX7wK07G9hAWhOQUf5BdlMsGZolgDrAnHSRId6qrY235mDqg2YCIjcVZxh5YY5BvrP0F+xwr9xF94iq2E8A1lakH8Hz/gW6odNMjzLxPoLr4yxoeR1lJo/npx8PK6wF7O+oEu+zkL0GQBSt9iFsQFL0UZpQIeV9omDPDrF1L/c3YaX3apjUFi2AH1OI5IKOR1xRaxDmX0aoHGsEVTZrjHsE90hRoWSZIXX38JzOinUmK3R3oq+DTgh3yxKJfrGjKh2W9TwM2nXl43SBPJtK46Pwk0Esy5YK3S3U63bgXaRcEYNEOAnSoeMkoL3mWWOeYXtAK1RPOMNNi9RJAgjbAo9yVGY5TvEJcgCVqM4hIHTEZ29IDOJ0PCcLM6yaMjO1Wvt30lwEarj4x8dJVMUDBoRHUQFDyX9swqH2qWwKo7HnDI+NdORI4VJGMSotpdYE6kif9A5U53+d5iMsoA3Iyxc1cbV0A3iObKdntrqqgQ095yVo3VYw/XNLT0V/vqMFb91IEb3N/r6VH4b4mvO526Z6RwzKnrqqR5PkCNDtjWyZBj7fej/jLZxmMGj8ghv08C4vrIbeC6jmuB5AxocIBXtYh3iN+ZHJv5lY7gRIV7LCgmt3kqufUtf8R14qbN+DuUYJ+0ZqFTrYOiHpEOiYrtgzSoDsxkNayC9WUBu/wq7eRfgZBPEHbyTDNNLYKQnIESQO6vu+lO19059OnnVqaiOIfrCJqiPpfEQmMvHT+rf1PPN70nA7yhitO/CKejY8PyHze/baj/Kz7HNzvd3Z7R5PumLad2cgKre1lazNqoD/YC9SBmMXISyAascDvXYvpy89pnHSrfyUHMnfVbPu7LSES9HU1q1MRIl58gGyz+wKyGZwPQnDWt5Jm5xHxpk4gnah3mUMGyvwwLMcDRuYIRaRTJDIwT0PumiOr0jbmCBqnBe1PzJIXA7vyNocodKv+NwXglhjf5AlhghExxM8Jg6hoYJH4cM1fu3H+t1Pt0h8ulRhAc/wYx4qujQf4T0GPohzQ9MfTy3CItJOhTGiyky5xRrkkWkjFpFvkyFRxr6V6gefy1W6WDsNAQ1DI3AiBTcAtVpOgAL0bsV5VO27OMUmNeAu1Nv374rk/bb4EzbCCSywDo4TDDyJAJUA6XA723kongyMVSfkohIp1jU+LHCjN6AVQUy6qn34Tw7/HisMCFDNZ0APM150OhbltnpL//y0s7vS6gnuG4muH7RrfpFc7JFQZaBUapoe9X7wP9EM3aAvi0mDmZ/ozloSxi3g6tA2hMQA+adVLRODIdg0kFyNMSTifHKthx3iiQ9RGMUbJEoqD0bOSF6Q1XNoTkvQoc0DkD0Pfggb0ieJvvnQIOgCGaiaVbLxEcXDMNpNBCc1LIa+qkvZ0tN/hYZ1YwQSA8RB4E43EAXOUM5M6j4Ur+MkCv1L6HNWV+w1kQr23bpYESjlXLLGBlVuxo2c1/Wo8l/obO8Yl/TKYfp2gSe1OjImmnw1EtTNgq60aSGwmYWFeYITAel5vVaKTeKbNBXXrKEyeIKXwbJuaIUL2h5Bl/kfO8aU9h41bROqbMc2hS/x4d3I1E+WXUEPkx8krmiRL8BJV6AIKAVGcNmlAPEqmXIcqve6H0pIINpcr0Cpruxrq2bDd9jPniDpZBo9ggPDj4d74Mh9+mord68/NhW//Hx17Z6tbdf3YqEBWMj7qfonINN8d3OZhtMvw3Qc9rEcEHhE/b73Zb5qYoIpLY4Qizdn2GdOAercobOQxqV7tXJEXroa6wzH1SzylYZBCJGlk3ONgxHkIjFCpO6TNdHAANGFPihjdITBy3aAQROBLOiDFJoKiojYBiykOipvxGrvce5OPIlc0oLUs85spVDagxMDSsn4/c+AWc9aUjuqFACxHGkk+r5f6VjsDWLiI6XBVFNZGca/jYYTfaz8ZxLUgbxalHB9Ov1XBrIfwRWRBkVh3brmiYVfmU4n+x+c7ri4cDa5K/YMw4scmg4hjrLwuAcjIOkwgYB8IswpqP+hHq/jh1yY6Ubl3jhLwEGrvwS5egWRL/zNJpP9TtnaXoLrkghzfqQagQq1AQZIr6rJmAPxHiugnFD6PgAXs8nPI4PEZXN7MKI9ZW+PzC30zIPFABv5IEfYcWTu3j+LAMMoox0JbCmdzb/ar7i6Xk8vARuXnrzR5yzmvGA8Na7IINlLoAGf4ziAu2Uwx/ftNUeEELWBkkA5gwsuGi4QBIFma2Pb9CSp26AOzWOg7qgHXTOyIp3KsYwCpAppkWBwAoyHBOU2mgENBOnl3S2hC0iVL8xVl+6fvqcu27rGH4KmY1GojVXh2Hym4bTM6Qp2Idqa+d7iu4ntoNMgdArcFZ0jbecX6R0ftEWf6JYte+2aG8VnEYhTdQuygEA7xL0y3urhkL1TdjCY7TBhyjvEjmGYiaHGUNhMiblYBCcRUl/EMMjV3c0Q0l3q46KeVc143QgI5DuH+kP6RymOJ5zEEhG0Xf9aZQ4I3EHle4RqTKVJv+REzYNOXaBW47cefh7fRfUfZP+52PNVeA5/VHrWkas2caiKYtelkmaS9mgsJJKSzTfl2ZOL25M0ytqRE4Mw41cvrv85pvjVwfv944OP/Tf7707wFhUtG+afoRqhxzImMH72GG4YGuiEco710bhImHrbJA/o35DH8P2+hiv38fiFc1R0udkOUo1AaMXNtkwGtRXXcA3OsP5dJY3rxr4Gsgo6aCtGsAi4QOWXIDH2NNSJz6fzaN42K/E+FLZjWaGjkSJkj6iP22dvNKjJfmM8JwSQPYrwwW6toRY2wRI+gHEsk729jIe6UcOA911SwQ0KJQ2vQg6USrB36IG6XY2uQzTGbkJiUH4HRisyZ0mZSTMMIz8Y5aO+GQ7iPG7PTLRAeIcB6eHcNLgBevIY/us8vhwYL7aNoJh4MBw0WCGoqfZp+Qjedj0E1DaXuoo4I9S2iMumIIfVySkUA7X4f4LaAIvtVr3Gbea6CqfroNBa6jSFAGQj7cCwsk9afvJobTwNDI+NMMycQyjoYcBOj0rUglGHmEWVDjNwxh0R4SIXmrJakzzMYqhz6fmm4btqpGlMW4aM6ScIOM+avwYgSqhkhB0FNLDyFUyNUHOHfVuIdABagT8TmPZumYYoxuWx3obou/AhO4uMLZdj4NC86rMJ9b8SNu1trpac6Jt13oM2rK1vB4iZ5UtPC5fqSZORUPkJ7ChZan4wRz5fYMGbcjgTp4Lrj885vDeBjunCSGgSl2EVEiBiQgeyic/YUnCchq9UnWW7mb3qajtMNd74f5QdCoX6ap5hTNctjoK9PA1UPRTzpEhhXDJnCbQLw3EhapZFNKD3kodUFgv6ZzskMjoBa4HgUlRo2V25dSTGMGk51nIFR2Q82guBWqhvLtrC1D0DLpuS+EwccoVm6BrFbbXJWqYoDNRZEsx6Sid4UZqxQtNR8Qnv6L/q78F0I8aJ//5fv0KJ1GqLWJLi5Re697xtSHSeQ3T7QLT7WrefzPrqSR8IQOCvmN0EoSCB2BEdjifD3q5VCv/+VljAnbKibflwZBV2dFarRuWcAUFl1lDo+wYgOZXtbsXz8Pg27NNs3Xuzyj8pLWrBq81tNG0gkVLaJ7wzE6aS6qE7r5utqh6jwlex9HfIUXGCy/SvuFxEs5/gYVuLNs3gNL9LwDKLejfhdJVeVDjad0S2L3hcB0dVwdfgSAUunuCcXgLaE9vJohr+ClyuxzjVi61hMb4MKZ5MoPdPdZRJ5ixiPIM/o/OKQxWb5SOOlxDfz1nRNhcdZ1oGtK8uOdOY/lYO8hP11i5f+qJiI0eHK683xuPsM+uXOlJGUzh0IoITVxHB69riKtdR1oe7GhXT0nWsomBo2yv74DFkKNTJqcAp9tMYyV17AMR/0XtmaIDPjGoSYBBmpjJK07IIZBAofJJOo+HmLIFFjYeNHnCWrwhFUANRYSxJzNlWe8uMoG414aaSJ0ZeJYBUbTJgSZRgF5GotltcQWRmL0Mw3OPaO8hv7yRe2VIrDZ9S+GFusp0PpjoyVX0bonGQ8nlDdW6N0H8Hdfu/N8QZTKoCE3UosqIFT2ZNBIuZwGtIi89cMTe/3Rd5/d1/r7BQ/yWyOuanVDpBIejAFH9f2Qi3lw9PqJJKZ0X6NBFjh0m7Kr4L8lS/FV7ALOQHN8V+8wyCw01pxWARuwniAL3yIp44bCDPLSbX/Tssib+BuApJP6Yqqxh4iaFXYh+zntCjaIwHuZSn07C57Smfjfesp+CdAQD07UxJJ9ZXQmUyxeN5WNstZoxAJdBHg00PvKOHRS3mHWfginkulLk+Bzw7+w079WrNRliuIablgb9y65aE9/MGmf/r2GhGdNwabi8AyqAtGaiFW2kYlSoJL3sXNv5LyRAqGAHsm94az4bZ8EwfLG2dFGqu0A5oX1HPY973tq++hUPYmQUKrmSenjzWM3D2U1N8upKnqMTWbF/zyvmbdbH4Sj5nLfEdcOi5jEaheQM6Ff12ltCtQJTpHKo//O//jeTE62u4RyyPMPK4qDdj1RVpjUMgfGo32wXY9jfmkBOJkFynhtlFt0Df7mXA6khTorLMAbhgFozmZ8UwLbALTnmXcCqufFmGV4i/mQc03cR+wm6D3cQn83HlMZXcXtIqmQwizayFNPfN+jYszNbsHOIf9YBJxt4vF/6jcK08g3K9sKftEsXtBU9pB7dlhfRL7sdcbomvddo2abUBsuRbIkQoTJkFCHGkzFlCLGQ2M6m24ryOEtTxvTNA/yVREdRZNEZzNs8+SlcmM8/czIT0Bs/OnX7hkUrde1UPFu7cn9Yew87Acdda6u1vMjwD0C8BtbemkrPKGcYd0aCpbYEIFXqIhriW+iz5U5wm1MHXqW1AymCxRmsa0gB0HwMDL7UHRIIdlSGrNLju0iXy9CRHCh3e+X+yPGInYhnEj+yuuB2KQgcRV/7F0FG7ii/GDCQydfGbZz5XkWrdqXypksWUnZTF/0pO9adFyWwDpVsxIvvWP+8vnX6uVGqMtY4hUl4DRii04e5wA/XpnhIXHCKwZUlZpLOX670hlp+wZBz2gtXdl8srQuRA7KiMRVuepCLnNLyEV+0pykHgYwB8gbg0Cv85SbvmFzlmL27Br2uldLT7YzWxHVOoBIfzJMIgEUfZF9nx/ZZDuqfkDW2HcbQdrb/nZ3w7pjXS5bb6HsECKlxteuETdg+jtgJE2Ng91T2XIIxk4xmSaBkecjlpkLLLDr6wAQF5RC0QopmwPyTAHOTrXr4W3LIHiIzLspnEllref3I9YALVcB2BS3wfqcvFU3KTXcnFUqnvGMn7lIN6cC18a16DcPDcHHEU7dU9Fvyrdobon5Rg0PDYsVouOEAo5ZKGu7QomphiOvCqiMkydhlQHVVS+LqOTrRW5WWZO5ASzwaQbp2SmzutNV2B12Q3duc+NW6Lbh8AkU+4LlnGcS7Ot7Zb4EViNyOpTwDM4uvyE2xcn15rFbrfpvrPQwZC0+a8+EQDb6K/+jKAdfzH6OuGAZ0R4IYNXZX/ZMaBay5coQgEMOqf78lgzSOWYpXFwh2WzilOKqrNTC8nlSojOLiV4NS06MsGgiWqzIhLq+B857iZA+2Yw0Qln6YKSJjAU6GPKm6gz3ep22EWj51k6Ltl4h4uJ7NxXix6mwyD8uhCpu2fLQ+PQsuxnyNQG14hXCHdNbXJQbKyuwBEkqWJtGADL1XcUpWB37+EQwS9S/qDciBkGj12FSnx9gk4ysx4SgDfdJX8jXpwtXUepyll8WEUkNJfbtyWdT6Dl5HwcWDv7+VGlfPpFwkIpdyv9+ZRXnngtSVkq6QM3l9t+7NV8FWxRMeuRJCStpemdW9H9A68oP7VkwnuqylJZ37Q+0sJkDrfGO3ot3Cd4RY0z/3SBnCCLEzwMNiREwN2HF0QR6eQP0+J5cRng9iBQ+dboMm/j+2KGvpvvovHYRx/QaqOUbdI9+4RuBQcxI4+e8xyJu144O3B69O1PGnd03x22OJBI/42urVh0/vT5pP6CcmJAn23vv5jfuaZRqvjz68U25JFvXLjwdHB049FfXy4OSXg4P3hIL1zS1Mvt17vy9ft9e3t9YeM1bFmxGe/PozbDjTQleTw2l2HE7jVg3WczXFi80TPGNJIkC1iahDv5fPzpwIlQfYPkGcpxy2ji5POlQ6W5iyL/egg1nH1oxBmkg7zvKupoe8ZsFT9R8fDt8rv26NmqkP71XasbVq0Ex1vzKdpJ27UIp6c/Th00f18lcHfvXhaP/gCJ/pTb9/cPzq4TRlnSlXDT0W0ZOVhXRSognNE56OnG3Z21t6NZJNCs+360fzRO3rNB3K1TjzgjxgJ+kCpegqOLoMR/d6OMzNELeD4gPmUFIkwd4c6DzVYVwfw+IaUOSOoK3rQelqcDUop/fbN03HfaRNYVfu0tGEL9Q5yO/K37xLxfvb5qe5iRojwP/MbELp01KHc2gZxIM5FeYXeXSRq388Rbre8Sxjt+tvv9ViQx0Tw+faQ+Vm6+rJE57aEU/kyZOKvlJ9Y08EOhfP+hn5Gr1n1YXqO58YE7rmVU4v+OjqtZd10M10Fs5CgHNwVG3/j/Qf6g2hiVq7OoGJGr+zv90EtEmdHeVVJNJRWlMJ8Cky6PDF47gU6iogkWtBqtA3ZFAjsrA7UxoJG1CpdLr9jGO6ehhNFBUMhqYRHZt0ZHtZ9IOvER3EyEPV/HS832os7+Nt8I54GL55FpOI0vUmpGCTKTdh3arPW8vOjG0CJ/qI+X7jfsGbjR/ZYeQum97ctHyu4sUGHcGHJ8KXOeXEhsFwgaeOeNoe6hqAeMiDdSCk1/xG+61URurhBhweleGVC7ulC6FMBXZ9S57LlG3FlnU5zBBkU7ERXXoTn03TsygOMUSiwZkCmEy1jos25mxubZVJHRxcZrKz9DJTramO73vPYxgUHe5YMy4bgnTCL+ksH4dJFKL/na4YM4c4ljTo3iZGsKn1g4pWaYJbIqNYgrC4Eji5Js8q09GK4VsF6Mv1G229Cl40/MgzMZyqR1rb5fsn9BrhjRC6n1tZSN5NEW13Acqh8fITXRRBkbymXu8L/8XbReaXTzL8e77cZbmvWWZLNHl3dWg88v0jN4z80Kh+66A2UsBdQ4SHgg7M+tlALio/A/xinSsCOyWxOo8qJSz9maweDQ1uVjss3hWBYUK0pQmoxikepVN5Lhz4h81h46F83tpAXOuKsIgfne3blQAgc2+N3jjOdRt3nsit4v9ber5hXvq5+cC0gFeym6v08cUSx5feb8m6+gkzXr9cyaSx+vC6+mhn1yOqaXMhafztgAFGV6fUjEOF7h2WOMgxEgmIE0N1Qw5vw2FzKqkA0g2PSXD7pMkaVaBDQYbXJgdRcvcAhFEDq52Rp8TuTDy/KG06XUuOI33QCOXDHc2AYGtfOexmeU8Ph+jo72V/Inu4hhPw2Z8p/6ZhQfBdWCSCmOpHnKVYFxb2W+4fRa1RwWLdE7Z6pA3tV6+jDX3jJuKmvZIkfLC2ZlUuDhTiCD8LW4+vMq5d93tqZ1X+Vi7CRxhhDdKXc3JvKbIFrCfI0j38OgDSYMjxKe978xUUv/Qcvp7SDaxYz0+zA0Tvdrf1YBxqGGX9Lid9T7ttrEhtqkzwviwJA5mI4dgSkbRLrtmy2FoXoHTu7qLC6S5EX4izIavBwsSDxSAOpTjiTaqvKWX4cKUXy3nV6bRSVo9UVVOtr2u+0q/mCt3BbM4VGmtPL5/h9Z07LRPFMw2n17R+iq27tvUwys+vaY7HJc+f2+bzGVV4prJzZaXUSV3SNdukfhrp2Rel2JEdUJ69R5vtH6qP6K5WhpSKsz1ql3yeVa9iO8dE0UwbLXjx070PX8wyon9Bf15+f8cDDF9Zx3p+vHqAkiuktiUrnN4I9z/HcDDU0+d/g/skko3sgTb1kgP3yELJU5TburCinj8PPN12Bm09VFV+ZQJruFIghWDTaKSGXIYYcmjCg7B4or5ZaRKNJ4jtx9KLa0obkuhAYOAFLgOow+Sp5zh+RMXXHyaawedohoyd9jeLTmevLzlLxlVgZ3NuVaLkKdWS5J8MJ+KfkNXwD5bp4C/O3XFiR5MrCG9D+YrTyuZUhobV8VnpCd4onLvPli6QnMWqeQY0KzGmB+rTsPk4/sjFgqXgjq6s6WKiTSxXeTjoKDy7t7XHMgrASKiYu5cfYnYJirZL4ANreDPi3IQtPTKV6jKXN1Amu1yoxg18J5dGg0pg4q9bk3uR7ajxmY9Hdta3tqHPXne7t7Vzqg6Ojj4c9dyC/DMAWoVfJwGWzB2qJmspPRRGGyiQfktqenp2qn7ZO3qPNUEo+wePIedU8beY9NTzp3+rfetvZvwTvl4cjH4qzkzrYe6Gtfc5q+b2Jl640Ol0VNNjn3JeLrwQGCDlT2EqVUuv3R2dG3bUPqKELyPv4t239z8gH5TQjH3a61kN0pFVN3CoVuuBQX3lASNnFNxoXbwtzbTBhA4PqRadtFM0SiUhM7KbJXOWXdc21ZuHSx3ms4irX2E5ZgsVLjgM+4F91kDtLetqNSjCODIllV3JL4M1VDE8KXZnmLfVdstN/NKhgnwkjgV7+QYdO13Xxjtx9rueGiAJj0/rNwfWpyGHMawMBUVPQNmG2ZSQylp426Dqlhg+pLtKptOQbmKgqZtgShhPu5yuw0ZB952auFr9Ot75xLO7ga3VnI+8AcN+oq+9ErBkINYnZRoUR6ar/T4O8yxV9r2Zhz6iQSxjsyU5I+OuxoH8TJ9ZGqnf2MwfyzJm9NKsq7LCCmRfq0c72ZZkpuBUcwDwmPjhURk918DiL5eu071anTAQ3pF1a3B0P7tXPijL+9kI2lSifF0Zgixro1/7w9yPe+tioYbmaK+VZ1ADQEcd6crnGlI8ai7jFHljQl6SG8+saiphP9yE59qzdDBJ5UFq81Iar4EVTvZM8eXtHl0qR6g4+IoXwZnf2Ot++GF9D++aSiiRzLkonooTFqY+58s4HZxf4h0YXCQVjHIqsY2X+8Bc1w+BlBL03UspbLcvW/b6uAAJNcWu30rgt3pHyUUMjIXtGKRL7qeUuPPvrpz/2zQZH6UfD6gwg5SjfPv2nQZL/UJV69XLcJECSrrqHRZ5gQFP6CpgF+o3/9ijop4RSV+u9htTnct3YJVG6/8g6ehgQ6bi9vEO+6AFcNvtg4AiwGjSbm8GAf7UgwFYEMFgIWVhrvyg8ec7bbXZ+eFZq9d5OhKPgnmjW/vGJr3x1H0DkIu33OJ1LpU3tjvofulsQvuubs+FmqktfvTddff2TWi4MVbCTPp+sZX6fZNpf+aXHcey8uEFB1qaoe7vobD4wxKd5svDglmdRZEQCqy0maJ+xeWtEXrb6IExl68jUk7oNlepjA47w9R0Vz/9vD4ArHGafCbB7pWi9YXDHx7N2e+UMSdRTqopdlELE8Kj6uChkCAKWSAfgS2EDl3tPFCuu/Fsuk44CaYg+xpd9HwXIR61d3d+qHgFWSPaspn/OhDF4/4YfAIoafRoPghQxLcBVEPg2BnqBZ79ucB1PeCeXQPcDgUb/NmwNY6TYPbTzz2SAj8lGJxCW0yXGX4rNTiRjl9y8oFUdpfqQ7fDtE5NdePq7qHEvCY/ZI63XlE0XRxeBGY3stU0Telua/kFptD7LdnqqCdPrjwaWT55ghfdd3fA7O9Wfu7qn5/Bz9v4M6PJeem35HiC0TqHVMyWS5SaAveYSplm5gINvn9cKu+/uLN19Mp2M2WhiIECYg3V3MTxOFyl5voB4i0s2XB96cPjOTtLHVOwEEgi7AX1yPOL9Yuuqz1ooHpca4BEFFJJnAZ0M7WWWXziLzLANHDEwgq50ygmWTofT2ZzfUhZmxfSQicRakcb+SoJ1ji/6BMbBn6qzaReWYvAI5+/mdwRzz9Khgh7W/txsODA1W1kJUkfzWbzVZh6Pw6TcTFBL9/21ubfusuHOVDF8fMBiM7TDXKrRLjqCF+IYEWzK+47+oIJMjDK2rjVQUzHAR12Of13oQ+E5KefFUs2g1I0S7AIBU4hwkIKxpuEZWtgY2OuhA770de56ItcPJ8N9n8CJAfS86JrrvDUu3kUXKRZcBYv6ET0yZM9AY1DWB08NPV0eup/uhNo8XsfDVroTQdLFNpRP79onNAtBFh8aoKJyFO8c0q08N8xxrNY3GiA6ds2Hm51YVmPvq29W6mwW1s7d8uNxeYMLynYv6LErVdr114CsHJUU7+fjfeaNDQblkfnoAVYb1J4rCapi2vssnZ/u6yu+1a8vavfl+tvjx9aG7deY/eRiBTqP3kQ6OxXtxctmKyu0iD3h99dVADe/fogyH892WeCke3FB6C284cefh5P8AQ2dAr+ml0UWAPELbPJcZ+yFZePeKjkXhxSX9LnURWAut5RVZVAdE3tNxbtlRtB8J1Px/v1wTG2OTrH3aqlNZF+D5KeVEqsslObZr1a5OQPzCLjWbep4XuPyDpzS89Viasuyadn2aellPukqPp996qj3aUEoC3/R6a99CTxxKWOH3Z4pZGDWK7gh0tB+IX96CYhczUjXy+fYhhp7Jz4dlT39R6I4gVGRooX1CoUFOany0ryuZwemsqHPc6GrVyeQzvWvUDH31Wp89i9WMdW0yvhp13dWmZPYHnZDPSL29dXfvjpgK0fyyUD+eoRqbYL36+fyiikAb/b7GxuNm55IlAR6w7b6BsIcC8wBA+TkJpETMcKduJZmNGe4AHutxeu3wQlJqEMmjvqqGaK96g+toeBvLkVc1HNzUuPKMVMn/8PRBhnvulM3ZIug96Swilw62oNbTfoh06UKQi1VMU5X0zPUrKI9/Y+viXJNgGTpM6vtcVnhhqUivq9U078LI/w5sOHN6uHMMWgVw7w9KYBfj45XN29eObqB9hxDQi3ePQjSGqrksI+pLEpoqGi/LIjJiB1UCwH3E6emnmjIVa+7+vhBhlfVFS5i+T1B5zsf7z+Cf+83ftP/PPhiHSj44M9HcGKtxuVX31/dELv/HhE9TX23+Cf16+ov+Nf9021O57JkMtiOLkQzvxX/SpXEvFNU56ttr3J15uIncY3D9W00yaiGJ1yEZAWSC9/WnfPXzrzGV5WqQURd1qX1fYGX1I/LoKCSIVv+ZJ6IuowIYagLwFTr4B4igX8hk+PouKP9VdBhi8QvpCyjqmsrik7IrMGnm5NTpPR9mkPM9j26P/9t/j/S/r8/kfMZitL17bI1fsqc+4CAGt3vy4fFPfKSyVnM9wth+1cMZ2ytEGy43hYZ+BbGX5UeFS7cPQZfZBhWUwiMFZLNWHeTSV152F6pTu/RCnV3d7vDhyHSI1MdZ49SHXQF2fVaQ7OGI+X0XbGd32xr67IotmqVW4LKiliyV2atvAI+sFhF8uOeqkrq9O9am28+k1fXPa4B2hyOxupCQw5NNY3vzWcq98oCCV37m1wZkJZrfpeNfTA4tD2WjgES5eKbzzikZq51o3PSd46HO+Z5Mjx/YbkANec53Ovi0kr9sEZFh12GjiUZ7cW+67d1TvxONIzjN3vbXaHy97mZo9DG5FNguC8+6sOAMQXLHj0VWPXwysujFwOXfXcP2tj0u9EldINdoCDThveadtdcOoJjk97VJ+C/t9/y2UpKjhexfFX8/dHWowajDqi9KnW3Vp/DmofdvSnL1Cko74zVFe4LAGFJFkUL0ll8+RYR+nzOmJWUXH3czgqq01vkw0vNyUqMmdGGBwgtx0CWwz4lGGA5x/or3s0VuVc5cj2/Y006nGjzyaxt/Ef6SRR+2mo26CCS518rDHejflOhLg8fXCQn72sEX14ViaVbohJRlE2ZQtfJu1xJzG4SjzhkUIjvUs5uRynXMxp+b/49SoiQF+ISXcSGGEGP/D9mCIX7B2e8ODpI0oDfUUnXyd3UkMVQgVW+TXgIMjVfDQMcXra+YFSzCocpI8n54ksj6OkY7qBRVnjFe6GV7Qb+NaGEF1WIWdb/hK9jqiOD6wC/n2zmHLNvqBxWmYd91BxHagstD0McTTPH6bqUodYBYRS+wvds6nE4Ax0P6/Na1afca9g/gTslZLG2Oqo12lmrmZ2AfCvUbDQ8bw3CHY2aDHVNY4pmoCoAVjtL3jYyLcIPALrdIrlMgx3s9YegXvSsBLnfdM2ecD+flwWWcHVakbJ8yvtbc0nfS+KjmC4p0z+0VzZLE4Sl+SEQiuAy9WGGdsJEde8ycPiL6udJdeVva54Smz1056K0NVrS2HT5bb+hbZ85bcxfjgXZBdroje33L7UutoRux3LWWNmBYw7DpuSq+C0/Kt61uq513pEeKeHA5bHWggAjXPQp6Le0+FS/Q/FmED+BeDgjsLidXSHQM6Jj3lnDBjAu0soIIBOAtdaSn3rl0vHdJWGvcSCL6TyAYK5bd0eKLoAdlcNzzoUZdj8BN9bHYAM2Hr/bNGMhrtSAh+fZnnRbN08fvd24yMxoEuXBtB4aJprbPXqoj+s5w2a3wHrWCQ5z9d45b5X2wjsplzmEqdjNDvxQLQ5+g3vEtHlyAktVwLK8rdGy+9gSzr4Fn2KcqcC5ghGg7Vlw6P7xm9Jo/PPNEqaBCRenWwuqH756fDt/sER3lHNTudG5S7lYMy787qrltvyrn/JRunNmhs45D2/ZrD/Wk09YXmrVKnKf62ujJW8Z9L8/Tf87H9pW5NZ4L+1KvVA3teBMf5LXriMtCx7bv03av26dNf4Y98e/pG1HoUUSferhNlj3xauNSvOLaPNvyl82VO8EATLZttKwkboc4G3EBZ9lCj8pEa9olQ/yqagV/RFE/QVtiZeSAFD070UZpNzSeY4PQtiVYaTfqsA/1fYi+52cw5vaAKiDdDnq/Lbvc2nQ9cOb5g5Y2a2/uz8rg8v+PzHOSey+EDdwn5z2vCdHPBmX2MGmuqPTrvyjRw9gzrkQPYzXq9SMBqJFzkwAWF+c/Th7UF///D45Ojw5aeTww/v+yd7R28OThxmI/eH9NRmp7sjG0HrMfhwWz8kDRCfbOknVofwHtMRORsd8HTzT9ki7wJMg8QdyLvz8XcI7gWc4DgxBKPtnrw5BQEB3CF3j25uf57TaDT2qGcl/fSjZBh+pVAg0jv5K+jmYTCY6G6ZHWD44RBzFC7pRibMIeV4OL7NMu9A53IdTUIl70QJ4n6HX2mja5VnRjqPBttQH9fKm0X23hdz57IlamrRmaWzpkf4csmMLcBJLp5d9ToA8nSeZmoatVEfRAhCMu/w8EgjtuWLdlFQUYnLx6QjGZ0V1NeGf5+XQActP7O6e+r9DPsHJxglutdehW/Z68OkL/xTaQUd8c+77lagVdShKQ1nGPlho/pLr9YuRSYxS1GPlWYd9Ec14XGrtj3129fKrveOAee6N0Nap9J7G9e+yHdmmlH/vmuA/rvttLfS6q6g2bKOa5HNnKh+KkLmfdoduxi639xickOEa/L63JtGp9jnVJOI7biFqnOVJCrq5p8+ZLljtF/AuvMeV9cFt61x0JwaPl85W/JYD7DqaQRGDphHYGv8dYuu3JGoNoqOIiGBmVjTWYFWIXOozfquRQL6y1vvfGlYfocy051a9YVl5YnmLifZvLo/qba5a7OhqKQ3/IW8BcYq2FrfqoLXqEp+TBhpzJPzJL2scz/5sy/3aadLvFxbNrPIMy3ot3INLVisPi9WMx+ESZBFqWhgVeuaRFQxn8XhZ2phpZUVVy+x4xIVkGvJlU0YS4Qg5arJTfqYt2DEIkWc9rH3lhFS0N0s5gCC41+PTw7e9T8efXj38eT4swb71HUOsjjjIHWuDllf0pbry9IP8FEeDrKQczdxy6E7Ay84xiZ0y5txRnFihrwOSNKHObe5jG1E97qm82K35G5vb2Hlq7xaj7RUjxbdN1tUh9aWy5PQgiiB1ZGkAS+mATHaBLvZTQl+j9lUVLw4iMmTqStOok4BO4auQ3R13r34EuuKwVvRaCHXrBcLfTUNhvO4ga6cGeV1cJAPAlpJGGEyn+Kd7WydSn0NtqWl9odz93qKgH63451hNfZT2qvDKB/EKWi1uv4zxR5I5tp0HgceBG/TMbmdTC0YLqyaziSxjS7cpJoY82FE0ZpRbHKOxX1bE8wie43ubUQ7NvcYRONKU7dQ4BIj0Phju6YVFbTsIYHW/YokGlKiCzbCb7WtiEKpBX2qayM8wCGaJVkz5mvdSxxP0SMsGBuCt+lX1Cn0brX6IyIFQ9tCbRqSD81BVodudmr6vjPnNapmAr37HNmM97UwV2ZWx2qV1TpTMla0Wt2+KrdvW7JZr6S9ZvF2V5/7ERx680VuVWVdx8Vjqi/smC1/euRjo+KPD5xcqSI0V8h8yOx0eRndqT/NFzxG7WwsuT90Uk5Pbd43D5uT7Q9n46+UnhsxlRcyXv38OMfvoXPzS5bInn/g/Nw5qFmQgThER0rEdbRXkSa/VjtXh7U8dMJV3gVDu6zrYXOXsz1TCBnk3MYsjaPBwpOxq3DgtKlFBEUPPRAD5RA4OYd6hFnrTlnSTTlJ8xpmNHSutRKF01PqRPE0Zzkc7Er/oyIvpzUlHZSjz7luxAqltHaOA5Dq1hmJ9iKa3EOMzyx5D0G/lIx2LMmOvvw4ZHeRUT1XORj5yIhJkKeq9Wmjg16nZtNkzEWvyUW/xilkvTLiu0L1t3wcUNKAqS9tS2oYwowviXUHkrGBFC2aydKUr/2MQlbJP2cPU74CcvqsvO+qfjAc2mb8mAeys/SHdPw0FspOSOVomk7nctV0XIVuGIazfhJisbnr4eI29hT40SAzaNNUxo6dIRZDgp7xpNX0Bk99qJxmfe3EeDDizCg6ptMu/2d7kmsvgLbHuA79Lk/Brve6FwMqjh2SLtH4Xz0wa9rf6Bltuy8I/Ml86qzbaldJ1UuiHdISYxDkBskIS7Joeg63aY2H8DajWCeevuwWawD00Tk/ZcMAAY7DpFk3QiefxVHRbLXUE7XV2a4O6GJBaOfWCGA30TcrDjk0v6VTDv5yZXnw5rZ/vmEAwKsV9GevBgNDgU4hvZr2V9eaR1vHrrJfxiGQy4h8Z0pDbwQkUr0n/BaWMZCFo7+UW+ldio3051IbTtzhQg5mFckMKpr+0pbKRTR8StV4Mg9KrV16xBgN56ttubSnMnTMtoLHVkIfSrLzLmcMw6HGnzIjKSY9ct6YPUS0Yo8OzFGvzrQfsRI6lJB2v7LW37iy1g9upaw7B3P5Q7YdT/Ct4+QtiCoOL8KYb7HR16SRIeKPIhsWeWjr89bpI93eSWP8EZbKZ5LzX1/suaDs4RK497sbrOZWOqlaTF+UlDvhDFhg8TMsUop/O/4taVscfTvLYDvQvXN4izqKhJyj/nE2YZDFEWYYnqHJx/y+1E23o17hnVfrOkvBlHwj5RM4QlsdAkYSuq89AMujQM9OqZftjnq3QBED3AdVVCzB4a1c6Yq3p06VILlu3sF8hJdP5oDyQahPN1C/51zgOA2GpdFX3Z73Up+8YRK/gNMuL3P9YP4Nf4fAIS6kgKxDBaSCY+iUmXfHXk23IoZqpUL0yGwEtTPAKg+lcCi6+QTvP4sSyzjYL6hr5O17wXfPtYNV4LW8Rd7i0DLTxa04SSkDx+36Aak2DIOTaWO2wCiN4/RyfT7jQsFcx1MA1vwDjMoUjZJF34R6jSSsjwJwhIFqt6/cT7mF/z09bd2XgZZHvc/0GUiFQBLzZILjwsZkHeoxrFP1Rc3QK/jqKCmX8KRMXuNLxrji9Hw+62MxY06543JVRpnQSXZJuRam3ELjvAmMBd4UBwyZzslA1/o/fRijlwypKTrGBXjkCpQ+QEWZBQtKS4RhFqFbOr1M7ntbs7B0QodDoXn9Jb2AaLycNxqu9Sx1PuZ9yHbDNpwRXA2T96HWABsk4PpbzucuffbSgIN4NgkSVIjxjhQ6SQFkTGfV2h3L5dILqSH5DhBQ0PmocXRQDvolDbtv4zu3W6ePUj3rTVq4DAPny3VbLNpJNAGlYJGpbSWwKibUvHTFAGj9eEkHkRdRNEpPE/BBuSd8qwLtVL+8FafSuLRh+vYEcmjFcRmYR0lmgc1JBeVKtMFFWjhlAPfiY1aUxv7CoS0JQ1xW1PybeFPb3GBVex/c/a9783DOdZkZTtZVrsqALfFIHUN+Q5ZBhsPaWg1gLQ4wMnU0j+NV9cAeO85qz/o1HHMBBxSXX5rlf0bkledQoYNjLKePmk3LKCaYVYJ5yF58lAWLdmJQB38ejvlwiuXAYTKI58MwJ41snfUStCZz1TTnP/ZAQHvBpZQVGMBpMs5Bh9PGvSeZ6cwRU9ouJyHeMqAO9o6PSQGG3wd4C3QWFdieoUdFg0PYQct4iakcVNquArdgwD0J1zecVk/DEfY+hj9fwjbXTfR3tw0dhOsGciru0pg9YKYV1yP32E1HAYmsKeHCwPxmYCAAP5pnnLesLVBcZN2Re9g2agTzYsL2Oqr8dl5+miSXOp7jTQKFBMmzp0ZuxtCwyMB05Cv6+ouGY+n7Y+va5zSh/Hw9vxiIFDGCiW6vqkCiz7/0KR8CwQfoo8h61s30rwEB+AWWJNIYyIoKAE/rAJDXHByAZQOm5s0Y4GW0tI0cezgf6HXU5YRvWEHv8A3U+TNDXHjblkt8NcCb03pDoPX4W7GCpbE5epxIV49NX+oICJsqJnnGWYGXbCY+2lYtW2ncHFYNaXUUYVImbFs0Wo9/3OvuPOuV1nC7W7eGx8c/8o2gtoMSIuoWzmFE7CqbI91j9uw0oPwbyqUoL1flal59eQiulLm+xjNSdrg0C9X7pSIu8N8OZxqd1k2n9vIaNinMWDetbBlMJ5zMRNCUbCkuUtM1tXCknowbTVMB1XRbvlB4BeprIBOE98/I6Khi7znA8axN1VyfPYXP3eeIvme1mKM+LL4cqsRUvVAv7k0guWuKERTAJ0tBS9sISAkCc0+cfoVvinM6uy0qMGJIztR8XMD8PXTUIoHeVhxrVKKamm1Qlrk9w/+094+if/xdUJtQqqHHW3LILZtxvREvqX8rXH+Kaf3b8ndH/sLzbfzbxb+109IbU3fPFLea+azYGfW1+8jXHUfBWRRzQf5KbaWu1FaqAsaFO83LFc/pzcPPsvSfnLCQBxfIdCoAmOpUG/ComFSBoMfxQkkHTHqm3xu4RT1QP/zQxxkkdLlC5W7NzU0uzDzNq8CY2wh++EFJF3fEyGCCsZ0A/5mzJJ7jfJMusXiK5aG3R3VMFHtQTg9yLzuz+dvAkKWROeIoDb/V6eL9FlKb+mt19KMPh8qcfK0giFPthxSly9PaOXOlaTOG/CRNjJUAEwrXlZsYAETbLPvoMUsdTDbz8u5t3931XnVbaPAlX63mDJdPb1E317keFCl7WnKo+lMzAbO6gnxbJWCYZq4NopMCuOKYY6Voa4YAtK5VPRwQ9FmISrp+YALkGn20QpU+JQQDMqF9tOvo7caVNAgw/hLsSO+8gh0Y7Oyk+4C8QZcch8mGfMehGLdqEBi50BPJL3QQY6+IvWzKevo4oLvWqClQ9gUIWRVAq5SPKVzft9u/3FLANgUW0jOlOkFldE85dFWk0mGH15l1yOhLB2jeFLxGQaJljwm2N+6UMx0lAxMalLGQT9I5rPvvcyxXPlqYQCMpa6/jaccRsjg8SDCSLXCReqoPevXx4CiKY5yUu5aN15iIizWWLqLwUssMmsogheaOPUa1mcVnn5MvgqJxowQ4Sd7xg2i5ylTAji05n8n1qY3oRAuDOXdy5AElOgh0+Xevb/eAaQRUhDZ6wKvKBybzAtjcHwHHeA3wNEdfxDJYtHUFeqKlBAN5nK4t/cG+QmM84+vZifwAv0Oq0hpNZ3gdFHaERnuYraPUxcexTrb2eq0eZfFFnzmATjY7IZt2sHbMuWdjEn+dU21ZVcDvQ7//Y0Gi1LLHuGZBi6nBFeoSwkN7PiQSsIJbgkbKxSv0pSMEKNTx9u2EN0iqhllwKQSK13pc0DnVIJ7n7vSFAP+JVxeaRHSf+qgQP5+HOGeE7k4ye10fHIoIx9ASZHcVAtkXtQ12bTAeZ6FzEaHe1T496yr+wVl64RPEKyOsSg7UFMP3AoKPK2//Po8yCezGePM5cKBhCbUwUaZxCm3VDht968AwHESIvPVpQFtnxvnjfPlhDT1JrjhukzGengFXweuwQKow9ngzsPuK1y/iCwDKMHGcLXogjSBx96zQouOCgIXHEbyefsaI/8gBxrs2ioUQYx0PrfVKkr+6TC2lsgteOr6jQWvBJNGTXjOdygdN8zBx2B6+nwfoCG1WuCJe+el0JcFTfhfXjOU//Clc+GYDUgkmw5FSq4Ur1Ytoq2ZEUSeSdat+b/nJjKQ2oO5h9ZNSjQKlriK5P4NM9yspwt9a/QIWM3Cw6W/R1lJDWI/WOM05ZsrbyGEemikC+aDvIZCrQmfRAAuSdRTVu5aLcP6gcjMBn2BzrIXeDFTUosyYNMfS93agNxtvLRVpOUph14m3RXyGsFtZzSDmBXRJFcLQXkIfKgiahKhZuII34HuwYeWEPZAbsiYhdADfUU4aOY43Z1HR/YnHAelzlGMMAe4ovGgYU1QuJ2E81cyodpIeSzUzliSY3CC0JPAZr+ch6CoeAggnzLYSdMGhFuPst+v2lyxyKWq3pgKFzfa/CMbzsM/MfD7Tmjs62z29Vud/lCSBGxihGYQfIKG5N+cHYG6hzRYhPkPMCy/VBnwMJb2dwmUqXLtDLex9t/oCbiTInHgUaoT0jNLwVhPjodYmHAk1wLVG0Qv98UENpzGQ+mMkygizrhFkYawmHZ9OF2UvYCwBBpGmI4KIAk18WNDmZbGC5hWW/sPGgERz8ZQR9QQKo+xQkh7z+XhMqVSX4VoWavmWUdUnNMbOEfUk9C9DvdPAxI4KZF2A3FTyqC6DbFjSpYwnUaNVw0ayIYOZOCvMsMlpB4i2sY4uA4YCvCnDJLJkMAG+cc4yLY+mURxkfg5CVZtxmLBaRGGMHsNAVGLiCrwyTA+CDKGGiIAOnJuHsI7fkFgl6raIM9FO5BjfkYqelehsK0P8LTf45rZxv/cLu5FYPbJX/IMioC5tKH54//ZXYpFgSsm5NND+2JqO5IHdve5IzcSlksQqBVd022r71BPLyHo9kYwdtW0HOpZaOhN9gGSmLy+l7gWlwpuunShr4kMI+k3+BSsvaVDNFZv147WlZzfirxqf/40ujCQh/iWuV473Q11+gegf444EGWC0SS/2L3B2tzF2ecM4ttQLdzcY/qoNao6jI3aJ9hOFE5pefQGTv1BiG+XAo1BRqBWa0sa1xDWblG2fR8VcRNYvQXzOEYbclMa3h0M42xqTwkPaMCVEgNQbIl6EeWkxQXUwQpgs2vcSmAS2E3D3wkMM+qnWch7fF78WswJ+SpZWbKfhY5jN8suQlXd02CBXwVhCApd8AvNkMKmAaZfVVzXKRtrdYoyc7ecSYEvfymA4ja2LcZ0Py3rHkCV9bhawI0hbJUnFX2BP4Dak7eN4tzgAkUdlLUGrKKXtsDfC/DFxK5XEv0G6WKVcFIqYOBE+2ccBUhCRIfsfakInSS64HodD3GeOYNZigEUi2l8kDlzROARrT7LIzuak/YkvyBnGbBVy2ItHIkcxjhnv8yyfQ7eowFo1hEgnSpFHiy8NlWOAZV2cDhHH0qLLBmmiXnsyu499Oki8/p6nCTuHo9oNA4MAcFjTUevxFbzpHQCMFD3qKUX5gmzI6Q49oywMwgxvnjMo1lEpGOQ6ZR4+RccdmczeIK4cJvUVcS87mxfXmKhg2/NFl7O0kDRL6RlQ5aPnnQ22Nf4Ucu3k6FAZFxPehzxABbyqYm45gwO6df0RKbKmbvVu9j1VcK+pxFwklDuqlmif7ihieGAxCLznb4DuTlQciYNpdoMeGgQUmSO5TIrURwjTvIkJWsl4lHEJIStFLLH7NmQlKCcKwMuR+MpBmnijchEnbQ3Rk1m0xSDpU9w24qVy9wgP6mxI8R9ostBGkLvXCjSVxwtOgkkvarTS0wdE6P2WXJWZ5fK3xA2cc43pEofjkMkblBetTBjuafWXa4N4/d6cfIeVagrbZ30w0MxNiW6RibaCFWp20TOesOtBVzWwL7r6nehu4qQodX6naZf6d09jZpOM+NuuedGeV9AxE9cD5p0E7Gkhek2jZdvhqXS1GV41hK1yLDnabLxotNRfVQNsMWAh8eKFJbFbC10N7LJ1w7urQiFvsKWXvkX+J0Xs7UeIEZBtphjlnxGfN4sG532bnNW0ub50liyfVxSbcQ/Ktje/R4sQ+sFLYb7XCUt4Wv09eeklz5YfOFmittAZWAZAX1jbbINH10eE9MvfsYbdZuWEsMGDNmxCqmn9rKZ1NXm25sXnNS86U9Cv5NXzSi/9tZxTjbG1nKHVpDQ0+qgzq0O0JuFjrRl5pyKKVAFStERb/oaXrYnjSCwgP8cH8lTfFTTwiu6KApn3B4sBFfcyGc7v994dHKsnqulMR21sEN/yG7VwT2+1NFSdfDIfjYBnlTpvrRix9ORzz453anMxdQ45lXnDGukOVE+QHFxeaGPIbSvHvatHrBk8OnWSfW3qc3UnsSHNXUs2eSUB3st955q0f/cnQ9UgvexlW8SPyibulpP2pf6Xm6lsci/ZcjDD75pPLb9XwyzpW6luADX4EzjeMep2IFsGf0okMsXiUepI3tRbr+S9wYqHTANYmgnJWAhDkogpC9XJ+C0+Ozm4p2yFKV3P0nvLSdCWzGN418vAPW1d976TMe50YBJ8r3+ZE2ctzDYP5/OK1NrT67srZX6Xuizl3K7qy2pzrAPZFGqnLRWd8rv3knR1CpAJcKDeYGVxUbkMGqw61YJbfuNv2Zub6r1xY0vUJ25sZCrQ3q7ljX0aXuagy2VgWHfJx5xJ2T6t8DkZ6XM+OHVYnjylHPl80FabxMYtF/taHcNJ+q7jk3qcwddTqlFZek4jDb5WRyrKI0nevkkeb7s1RKp81oxL2Cs/5mGLyrAmn9/ba34RGJS309r6pM4Kfs5OpfioO2JWOyDXcq2wB3/UqJDCrrbGcak4aonaPkc08/JjgiOqzpy6yGQMW1Oxvg5riVw/R5kZqjzlyM6ZXdrIlJujBphva7trT55t6iNT/YNSxxSIBFJBnZC8k3owqBUfhXQvjv/Gyo5OKDhSs35762WyqqktDqyb+sx45RBcOxEtk1bPeY+eV1/au5Bk/g2CrecPxr8kFN23Yjw3b8YdT57Xjyg/umP6r10/psiUJogMf470vNdeMU361Zun9x6M2e5sXjOojn0qv6ylTc2bLEe8Ogk9fNOTP8sNJoMSUQL1aUVw6Jhj+voCOgUDvjhIiAfnQIyoTJe4p1TOc7RLC53C2Lze9ma+VFfQS297uFRN/LSRPNna3OwhMr5v1QH2yuqeq0BDRuqDVmW4NwA3+Ho/4DARhPTblbAVFdjKTPkm0Ip7gfaONy8XIV4FXVYGzuVjN8CV9bZ2NFg7BiyfczCMW6tg9O4NuBaNUQWNFQ5/A7hR0esaeJ+W4BVWcBdwr8VrlNWCewfsRi56bwVunWz4DSsQPb4B8+rt4Z9huUyDKNGVN2dBxle8BNmYPnf2svEc/eAf6ZfmMMwHWUT37u3a2mm5EaIUo7ZOhhxdiyECUSOKOunQibj022ysr1tDFm9XRcORnBYAXADd7T7fbNP1FruN93SkRod1zHcLk8kZXj9EOi9m80J3T7qu7p7uNNkwUxBINsRQxWTihh7/A/Wi8CoejJ+bXD8muj1qJ/S0qztktwm5ZySQb5alw/kg4mA+6R86RWNIhqE/OFDeLO0WrbvgPar4e8cidqkxxidpMN4uN8GPS9XpdBot30FT51cqddpWpgsdTT4v+ogYeP8j/OEXGPctrwHOAo9epufDKGvyl3wX63Pj7R+wv/vpOX3l1whqjAhs6g5AI79stDBIY2T3ssn8bmoAR22qQZ4Uu4BzUAHwduAgH0TRLt00UELgcYBxkFeOab50KO1Kj+2pAZ7Nj9sebMo+3YPV71NNrn4fd1i/L3XheLt9838BYfK8q60kAQA=' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); f=open("/root/turn-hier-kv-compress/eval/generate_traces.py","wb"); f.write(data); f.close(); print("Wrote " + str(len(data)) + " bytes")'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "98cb6473-0a7c-4d52-9c13-ff7a24bdb6ec"
}
```

</details>

---


### System

_source line 219_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Reading /tmp/gt_ssh_cmd.txt",
  "usage": {
    "total_tokens": 16873,
    "tool_uses": 36,
    "duration_ms": 268108
  },
  "last_tool_name": "Read",
  "uuid": "3474599e-7c96-40ac-a686-3cd7c9ad2396",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 220_

<details open><summary>🔧 Tool call — Read · `toolu_01QdiA5xFs3iGdUDzP6mpqTC`</summary>

```json
{
  "file_path": "/tmp/gt_ssh_cmd.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "92b0a636-806b-4118-98dc-840d25860976",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTuCAL8VDUbHNzUNcKURZy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8252,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8252,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 221 · 2026-05-13T09:52:13.064Z_

<details><summary>↩ Tool result · `toolu_01QdiA5xFs3iGdUDzP6mpqTC`</summary>

```text
1	echo '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' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); f=open("/root/turn-hier-kv-compress/eval/generate_traces.py","wb"); f.write(data); f.close(); print("Wrote " + str(len(data)) + " bytes")'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "31df09b6-4301-4e8f-a2c1-1d072c0bb3c7"
}
```

</details>

---


### System

_source line 222_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Transfer large files to server",
  "usage": {
    "total_tokens": 40597,
    "tool_uses": 37,
    "duration_ms": 272815
  },
  "last_tool_name": "ToolSearch",
  "uuid": "450a62f9-d642-4991-96c8-501f320670d7",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 223_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MZWkeizoBMiemyG2NRTnVn`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "cca03223-ca7c-424d-b2cf-a1b31fb5f708",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VDzirPGH7FUL9rwreC9Xhd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23724,
      "cache_read_input_tokens": 16504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23724,
        "ephemeral_1h_input_tokens": 0
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

_source line 224 · 2026-05-13T09:52:17.498Z_

<details><summary>↩ Tool result · `toolu_01MZWkeizoBMiemyG2NRTnVn`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "eefeaeed-e0e5-4648-b9e8-ed45495e4b3c"
}
```

</details>

---


### System

_source line 225_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Reading /tmp/gt_ssh_cmd.txt",
  "usage": {
    "total_tokens": 41289,
    "tool_uses": 38,
    "duration_ms": 276158
  },
  "last_tool_name": "Read",
  "uuid": "6e509aa8-a937-44c2-992e-81ca878c4217",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 226_

<details open><summary>🔧 Tool call — Read · `toolu_01S175yJrnCPFqT6zRySkFgX`</summary>

```json
{
  "file_path": "/tmp/gt_ssh_cmd.txt",
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "39f92ba7-2440-4e2c-a936-5e3a55449275",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmK5EbHR2V41Wb2cxEdXdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 40228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 686,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 227 · 2026-05-13T09:52:21.207Z_

<details><summary>↩ Tool result · `toolu_01S175yJrnCPFqT6zRySkFgX`</summary>

```text
1	echo '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' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); f=open("/root/turn-hier-kv-compress/eval/generate_traces.py","wb"); f.write(data); f.close(); print("Wrote " + str(len(data)) + " bytes")'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "8f2bd07b-437b-4d58-8f16-308a660fdfd8"
}
```

</details>

---


### System

_source line 228_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Running Check the size of the transfer command",
  "usage": {
    "total_tokens": 65048,
    "tool_uses": 39,
    "duration_ms": 280155
  },
  "last_tool_name": "Bash",
  "uuid": "49aa9300-8c7c-4107-88c3-c716957126c3",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 229_

<details open><summary>🔧 Tool call — Bash · `toolu_01Kc3CTfXH6GJJKt9Hgey8wG`</summary>

```json
{
  "command": "cat /tmp/gt_ssh_cmd.txt | wc -c",
  "description": "Check the size of the transfer command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "ebddee79-c445-43c8-8b05-41fd5e29628d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0121AvmNBrp1yarXNbXxLsSh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23759,
      "cache_read_input_tokens": 40914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23759,
        "ephemeral_1h_input_tokens": 0
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

_source line 230 · 2026-05-13T09:52:24.890Z_

<details><summary>↩ Tool result · `toolu_01Kc3CTfXH6GJJKt9Hgey8wG`</summary>

```text
27434
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "28ea3cee-0412-498e-938c-ed5c9d5861e2"
}
```

</details>

---


### System

_source line 231_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Transfer large files to server",
  "usage": {
    "total_tokens": 65171,
    "tool_uses": 40,
    "duration_ms": 1627817
  },
  "last_tool_name": "mcp__agent-ml-research__ssh_execute",
  "uuid": "fd71462a-e42f-4d9a-aec9-48398bbb4da1",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 232_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Xizyrt6twYvuRrRYWULP5D`</summary>

```json
{
  "server": "westd-16980",
  "account": "root",
  "command": "echo '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' | python3 -c 'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); f=open(\"/root/turn-hier-kv-compress/eval/generate_traces.py\",\"wb\"); f.write(data); f.close(); print(\"Wrote \" + str(len(data)) + \" bytes\")'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "5d2ad3bb-dcbd-4ec3-8dd9-c0e2f37cd78e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NgqBj8HWphWnfueLPpUsCc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 64673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 121,
        "ephemeral_1h_input_tokens": 0
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

_source line 233 · 2026-05-13T10:14:53.013Z_

<details><summary>↩ Tool result · `toolu_01Xizyrt6twYvuRrRYWULP5D`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'echo \\\\'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\\\\' | python3 -c \\\\'import sys,base64,gzip; data=gzip.decompress(base64.b64decode(sys.stdin.read().strip())); f=open(\\\"/root/turn-hier-kv-compress/eval/generate_traces.py\\\",\\\"wb\\\"); f.write(data); f.close(); print(\\\"Wrote \\\" + str(len(data)) + \\\" bytes\\\")\\\\''\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "6945a33b-cdec-4c5f-b65d-2183e6af0280"
}
```

</details>

---


### System

_source line 234_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Transfer large files to server",
  "usage": {
    "total_tokens": 112691,
    "tool_uses": 41,
    "duration_ms": 1633978
  },
  "last_tool_name": "mcp__agent-ml-research__ssh_read_only",
  "uuid": "24b3d2c7-cb2b-4c2b-846b-f980fc4eb844",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 235_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011kdHqAGdTmzxjiJKn4tp4x`</summary>

```json
{
  "server": "westd-16980",
  "account": "root",
  "command": "which python3 2>/dev/null; which python 2>/dev/null; ls /root/miniconda3/bin/python3 2>/dev/null; ls /usr/bin/python3 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "8c8e4ebc-afaa-4462-8df6-5655018daf20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VmPBmK9Nkm6DfDWaLF2PpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 112312,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 112312,
        "ephemeral_1h_input_tokens": 0
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

_source line 236 · 2026-05-13T10:14:58.667Z_

<details><summary>↩ Tool result · `toolu_011kdHqAGdTmzxjiJKn4tp4x`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "26be5703-2642-4a7f-b019-758b2bc8826b"
}
```

</details>

---


### System

_source line 237_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac46f49b80b0b7760",
  "tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "description": "Transfer large files to server",
  "usage": {
    "total_tokens": 113038,
    "tool_uses": 42,
    "duration_ms": 1636459
  },
  "last_tool_name": "mcp__agent-ml-research__ssh_read_only",
  "uuid": "f64b93bd-5750-4c04-9b80-df6ba0f87c26",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7"
}
```

---


### Tool call

_source line 238_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Jeeq7zKED8xeorC7zdtZVg`</summary>

```json
{
  "server": "westd-16980",
  "account": "root",
  "command": "ls /root/miniconda3/bin/python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "c7d287f8-b877-4860-beb0-762cfef73317",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcmPYfxWv699r9Wo8gkUxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 112312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 278,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 239 · 2026-05-13T10:15:02.237Z_

<details><summary>↩ Tool result · `toolu_01Jeeq7zKED8xeorC7zdtZVg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MKo7S2NQT8FTu8YxUfsgBB",
  "session_id": "82c8fd16-0814-4367-94aa-9dec50b3c1e7",
  "uuid": "ae12a6a3-0a79-4706-8af2-9f6d9b4c6098"
}
```

</details>

---
