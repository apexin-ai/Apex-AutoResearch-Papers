# Research conversation: Transfer 5 PDF figure files to a remote server. For each figure, read the command script, then execute it on the remote.

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 2
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a93cf04f7cf220353.jsonl`
- **Structured JSON:** [`1f905241140857cc0587.json`](../../sessions/1f/1f905241140857cc0587.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-25T09:12:56.247Z_

Transfer 5 PDF figure files to a remote server. For each figure, read the command script, then execute it on the remote.

IMPORTANT: Transfer each figure INDIVIDUALLY in separate ssh_execute calls. Do NOT combine them.

Files to transfer (in order):
1. Read `/tmp/paper_transfer/cmd_fig2.sh`, execute its content via `mcp__agent-ml-research__ssh_execute(server="westd-11235", command=&lt;content>, account="root")`
2. Read `/tmp/paper_transfer/cmd_fig3.sh`, execute similarly
3. Read `/tmp/paper_transfer/cmd_fig4.sh`, execute similarly
4. Read `/tmp/paper_transfer/cmd_fig5.sh`, execute similarly
5. Read `/tmp/paper_transfer/cmd_fig6.sh`, execute similarly

After all 5 transfers, verify with:
`mcp__agent-ml-research__ssh_read_only(server="westd-11235", command="ls -la /root/trace-verdict-study/figures/paper/fig2_calibration.pdf /root/trace-verdict-study/figures/paper/fig3_cross_model_gap.pdf /root/trace-verdict-study/figures/paper/budget_curve.pdf /root/trace-verdict-study/figures/paper/training_dynamics.pdf /root/trace-verdict-study/figures/paper/error_overlap.pdf", account="root")`

Report success/failure and file sizes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "19a72555-62c9-40fa-98a2-d3fa1d927025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T09:12:56.251Z_

```json
{
  "parentUuid": "19a72555-62c9-40fa-98a2-d3fa1d927025",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "096d3aef-63cc-4fa9-bd1e-a833d8af5923",
  "timestamp": "2026-05-25T09:12:56.251Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

---

### Assistant

_source line 3 · 2026-05-25T09:12:59.982Z_



I'll start by loading the SSH tool schemas and reading all 5 command scripts in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "096d3aef-63cc-4fa9-bd1e-a833d8af5923",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2hawj8ekSzooxgmwot",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee7c03ff-ddbc-42a7-9ab9-5ca5333b057e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iUXNQY8qGSWcQynozVf6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7312,
      "cache_read_input_tokens": 6748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7312,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T09:13:00.650Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011Yup5qx8Tve2xi9sXVUru7`</summary>

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
  "parentUuid": "ee7c03ff-ddbc-42a7-9ab9-5ca5333b057e",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2hawj8ekSzooxgmwot",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c165cf91-eaa9-4456-854d-578ad807abc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iUXNQY8qGSWcQynozVf6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7312,
      "cache_read_input_tokens": 6748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7312,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T09:13:00.653Z_

<details><summary>↩ Tool result · `toolu_011Yup5qx8Tve2xi9sXVUru7`</summary>

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
  "parentUuid": "c165cf91-eaa9-4456-854d-578ad807abc5",
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "0161a151-2fbf-41cd-aba3-2839d9e42dd7",
  "sourceToolAssistantUUID": "c165cf91-eaa9-4456-854d-578ad807abc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T09:13:00.928Z_

<details open><summary>🔧 Tool call — Read · `toolu_017CbhR24sY74t3Mj6JWrUSY`</summary>

```json
{
  "file_path": "/tmp/paper_transfer/cmd_fig2.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0161a151-2fbf-41cd-aba3-2839d9e42dd7",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2hawj8ekSzooxgmwot",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e31a277a-fd63-4451-af81-a70d859de7a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iUXNQY8qGSWcQynozVf6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7312,
      "cache_read_input_tokens": 6748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7312,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T09:13:00.936Z_

<details><summary>↩ Tool result · `toolu_017CbhR24sY74t3Mj6JWrUSY`</summary>

```text
1	base64 -d > /root/trace-verdict-study/figures/paper/fig2_calibration.pdf << 'EOF_fig2_calibration_pdf'
2	JVBERi0xLjQKJazcIKu6CjEgMCBvYmoKPDwgL1R5cGUgL0NhdGFsb2cgL1BhZ2VzIDIgMCBSID4+
3	CmVuZG9iago4IDAgb2JqCjw8IC9Gb250IDMgMCBSIC9YT2JqZWN0IDcgMCBSIC9FeHRHU3RhdGUg
4	NCAwIFIgL1BhdHRlcm4gNSAwIFIKL1NoYWRpbmcgNiAwIFIgL1Byb2NTZXQgWyAvUERGIC9UZXh0
5	IC9JbWFnZUIgL0ltYWdlQyAvSW1hZ2VJIF0gPj4KZW5kb2JqCjExIDAgb2JqCjw8IC9UeXBlIC9Q
6	YWdlIC9QYXJlbnQgMiAwIFIgL1Jlc291cmNlcyA4IDAgUgovTWVkaWFCb3ggWyAwIDAgMjQ2Ljkw
7	MzU0MDIzNDUgMjc1Ljk2Mzc1IF0gL0NvbnRlbnRzIDkgMCBSIC9Bbm5vdHMgMTAgMCBSCj4+CmVu
8	ZG9iago5IDAgb2JqCjw8IC9MZW5ndGggMTIgMCBSIC9GaWx0ZXIgL0ZsYXRlRGVjb2RlID4+CnN0
9	cmVhbQp4nKVWy3IbNxDEGV+Bo3UQNDN4Hy1FVpUPSSlmOYc4h5imZbvoF53Eyd+nsSQXWD7tRKrd
10	4jYaMz0DYAZXPyz+ejtf/Hx3bW6e6av2Nf+i2bzD82DIvMPz1bC5w/OgCV/vtfhoC7ng8bXsviQF
11	W6JLAShNvt5o/VpfPYaJL5hzp7XPNhou1vtKgEnHNlGRhi0bJkms21gaJvbAxrSsTT9AJiTbDNFw
12	VBEdi82ceeKvYRC58aevEfNX/RlvMpcESx6snH0SouJNgOf5e30901dP2GQbzOz1kJHZK/2reaR+
13	VB+VUTO1Ur+ruVpcmN/M7Km+nel7PQjSzLEGxNIr6cBTUoq3MWCOSGA+K+WJ+lMt8X9aTnQ2ElGe
14	yGngKTkcxMYciZMvks/qeX5hCtvCnKJPFAqgj2p2YYKzjnIWFwQJfqQe76sUJusLk59slwaeVJmS
15	jSkHT+J8OKvyVv1dM6U+qT/UWwj8gPz9hPdS/bOva3cH+2C5372H1FhJnDGKJScZfp2SQ8riIcXH
16	nHO2ORTnRu8jcMi9SM0FC9wjaVDpA9YOa3FewzEFiAEhYSG2ChpwUEG2lIf0CHsodeR8DpzPKtjx
17	H7f+cT5doixS/ccJMPgfSDHanBK5uCU1oJFSsVJSLm5LakAj5WxLPYB5S2pAIxVYJ880khrQSEzO
18	+lBiHJV3SE+DCvElhkYbkY6GbDoYaHnokI6Gd8oRh2GkNaSjIT9SJPKYsA7paAlz2fk0pqxDOhpy
19	BCi7MR8d0tGQJcErN1pDGk1IsHZB/BhCh/Q0vD0FHxptRDoaO5twAlpCOqSj4S3EJfNIa0hHiwGF
20	PEPySGtIdxzqSbisZ4LZcqmnIVJdU4rS1wOmA9XpE6rTHNVpoV6hNt2gsi9RqV4ONb7VrFt8r/B7
21	hd8v6sQbPC8ucIj09hCJebpu7kOnnDb/vcq223L1s2/q36B9NlMiZ2exhbmU5F0xgi6COauF+cV8
22	gB5oQlnP5IpwSPX+MZz1Kah1wIUDDrGWl6VQSWjS6AE17VnqDkRT2hlZdiPi2YboPXvAzdQEflOX
23	6958t3yeBADh2HEFGyXi9K824eyQzA5J61oKMqNixL34WAq6s8ch2wuwGxL0Fy9oqnV7dtYm+H8N
24	kSxDNno/7nd1ZeLmrwaC1r5p5i3anm+O8vUQeBggigcCT5BeQr2G7QXehopYCeuom6kG/o+QURTW
25	a1TbDzoc3KGoT0YmITf0KH8dMiJB1SfZDxkLZR2uWGE/5G4o4lhKJmR82Rvr4THsIZbNFZmHC/JD
26	354DZqdQNrfdmoYYGDf7lGJfmNKhBq0SntC36f7iQ76ue9lcXkXgCPnwjMScMUyqqKDyMcOBrQvo
27	0jLcQutWd76W78CUzlomWPbHLBdUeJ9zkFRvjgnNmbGJcuH4LYZFpd7wvf4X/B+gUwplbmRzdHJl
28	YW0KZW5kb2JqCjEyIDAgb2JqCjEwNzAKZW5kb2JqCjEwIDAgb2JqClsgXQplbmRvYmoKMTcgMCBv
29	YmoKPDwgL0xlbmd0aDEgMTE1NjggL0xlbmd0aCA3OTExIC9GaWx0ZXIgL0ZsYXRlRGVjb2RlID4+
30	CnN0cmVhbQp4nM16e3gUVbbv2rWrqt9dVf1IJ51X59kkBBI7hBCNWLxf8lAQAc0QoANJh5AA4ZEg
31	BnXkHQKCgIiTjHIYB19BkckIImh0hlEGHVH0qnNUMiqemPEcMxwmJtVn7epOBGfmzHzf/ePeqm9V
32	7V21atdvr/3ba63d1UAAwIEHHnwTxo4bD07IASAoEDNhxvSZNO7LP2B9LAD3xYSZd4yGp6/sRWV2
33	v3jqqFkTE7+dew7r5ahz+/SZuYHK/6rZCSCcxPuzF1UtqKHnnZcARBfeP71oda2vKf+pbgDDBazv
34	WVyzpOrLDf/ZDmDC52HbkgUra8CAO5hQB6xLltYtfnHq56sAzFj1FpeXLQha//jqCoD0YrwwvBwv
35	OHwWxJdei/X08qratS8MUwZhcT/WDy+tXrSg0bLxfoAMFevzqhasreG3CvlYP4h137IFVWXxvysQ
36	sY54yeKa6pW1vbeVvgzgT8f7R2pWlNWsqhOvYP1t7NNPgNnKCpGNwxqFwfo1JmbIg5HAjx1/6yzw
37	LqpbsRS8S1aUVYJ36YLaZeBF++IWDkf0K8tWLANj9EmC9zj9bASOMzJNLp2bjW9yw8AW3hk+AH9n
38	C3+sH59B+dXfu/9/t2lnwtMG3rQqgqMfz49wrP9X2wxvHih9/E/e/m70LZmouyC8gB2jTy74keYB
39	hi5qi7GR47W1CD5mpX99+2fortFM/lc1tW//RUWCoy+BDAo4cEa6kAkxkAwpkA4ZeE/GGkHOUOSK
40	ACKbMT/aTBCZNICcsqCuCD6da9dvrIXI9kM7RnzWjM9YwQb26zD083wE3AiCznOfzvNsnefZOs+z
41	qxbUlkP2ANuv7RF79lP4CmZAsRUMn+gAcG7yfpxb70Vh+K8H2F8n5dHyHf+C6ezY7up/rgfzIrrs
42	PFC+po3rrs+7pr7ohzI3AuD7JiwXDzw6CK0Wo89nL4zWR4nZlvWej2pQ1EE9E5tPfiwPMjXi/Ux2
43	1bT3Or3BA3rZA3pZA3oIhfeSndg6CPnCI1hNipzpRVjMORCdKFJBFDiOtXjd6M9YPC4IKnKiTnRp
44	LnLAUEUuXadDo5IAER69hTWi13lo1Xvpw5IRj1kwFAJQAEUwCsbAeJgOs2A2lEEFLIUaWAGroE7n
45	gQ+fGYo+chgU6prjYJquuUDXXIaatbA2HA5fCn8c/iB8Mfx++L3w78Pnwm+FXw+fCZ8OHw+/ED4a
46	bg0/F342/PTf4fI/2iL+ujtac+pIIkL1fgD2IGLzoVHBeIA4AXsF+owYhlIQtUMhSlG01VFRkVDG
47	REVGGYcyHkVBYd5zevS9s6LCvPrsqMSgMF9WhuJBqYgKs/vSqCSiLEOpQUlCWRGVFBQW9xg/UlHW
48	otShpBMzrETetcGbuL+LpVshBMthE7Rg+U+wTr9+hjeyHa98KDDdd6GNZKEex3aSC8w7nMJ28vHe
49	n1B/MdZbYKF+v4ee0/cD9By3Bjg6A0sz9CdaoI3exPP0XET0p96Em+ElOMLKwjlgzL0dLuI+Gluf
50	DCfhQ/IAHCLvwXpohJU6+ROJGT1CCPeFwnv6/i3crb+ZXQsJ72E+0QIh7OdJbP1Q5DrJIrfTUrqY
51	zMEecuQInYhXH4QQX4q7X9/H6v2L9IHj1uH7o/2Fc9zdXBbvJ0fwPewd57D9I3Az4l2MSCeicAw/
52	vQwtlI19nHAGJhsmi1YiGtbjqHKwjuaTA2IilMJ6OgtbmIbXGmEauYhvQed5XBR4yhHI8cmtXMak
53	YKt62xzfb+emDMn5UdUnG3ytMKPVVudrC4dnzOHjhbmtQkIrzTC28hlpn/2jm58NyZkyY46v9ey4
54	sdFWx5WOxWsz52CR1fAyXh83dgjoI4Ujj/OSzerHtTNcI1rUBgmqzWADcbldBLNCObvc3dseuAHk
55	3reKivJIJqfIjkK3yE4ervG7q1e/O7Bx4wHtTBX5kCwiQfJh1cKQ1qA9oR3SGkLMm+zCltfrLcer
56	VgPmN8vtFsUAvF2+0B7o7G/YWTDcocicvyCGnXYd2LTpQPfVq9qZhSFyH7mblJD7QgurNL92UHtM
57	82OrZ8KXyJvQhTFqxDEbTlarfKG3fUqr87Y5x8zYL764WC4unnsDHKMLTKVWubszck8g1GKI3Msr
58	HDY8PxDjdolpqZlnbi0qnDatsOjW8hHTpo0onDaVWWdT+BLfhKyz4KxMU51QZhXLHBXW0lgqul0m
59	UbLEYrvdrAsd3Z1yV15GgGFPS9VtkwqKDPkBduS2PbJ//yNMvtP+TJTvuomsfTuezCAzySwyQ2vV
60	ntae0VoXkf1kGakm+7VybZf2kFaOvexBB9WNCMywVk3gg+jHaVAUplKRJ4JYYSQrwWRQMHG0oC3b
61	e9tvgNzOQHe7UqQU5eGYG/hvDDL/zdxUMqXVPGvOy9gRFRu1gCV8eoRSOGKuavKBj+Sacs18CepY
62	dJ3w6YgOqLpOSkGKIhRk5CspbpJGeO1dsnQr4UP8/3ntgc6een2Et6HrnIYoE2CqmmJ1gWSDWi7o
63	LRMqbGsUl83qATPxiEa7WSYOS6Lc3X6h8wLaSykqKkLEXVe6tC4ZQRflqZbx5vGW8dbxrvFuAcc8
64	TRlJ8gO824UTjKQUIIYCMpIUDMtMSxWJWFP5YfllYtd+H2vVNnHVq3pvJq/v3fDY1qaD/HJiLir+
65	/NWPtPMevNemHaoi7Xu/37rvyA42rrcg3lbEy6F3blYzuKDJbCJBs9k0lZitsNJukIWV5grKGXkR
66	FBuVLEbOIXdfKEYTFyNOxNzRW3yhuDMQNbPM7CygnZ/PNRFSctxn8tl8dhox6ZRW66y7prTa2EGa
67	dRda2KFb2IF7xMJqrIV4yQgyifAiF8MNMg/nRpgncBPNhhIoIYqpv+dsCFKUfO5NjaPH++Z821fL
68	7XiDJGqXviU91Nv7hSaGSEYV7e41V2ofsXF5Fvlbhz40GZ5RM6iYuNZbJsq1UpmrDF3WGlhoLfUl
69	Kpw5CTyiKUkxS5wP+YyD087GJsrqN9jgaB0OnPpTWk2zWI8GOuLTO4IUinYENRyo4Yzc1LnmY0qR
70	XmZKVOIlQRIlg2SU4iSvFC8lSIlSklUCiSRDMsabXCKyPmM32cCD2wUpqZl+JT8Ja8Mj425IU3ix
71	b9awbbP/i8RqfwrDkg+WLzc9sftnR37ZPG9LwWzhvUParPR0rfurb7T/DuST1B17337t1fPqGK6L
72	2eRpHPsH0CZGWKEmUub5OEoITEXHsMawkKB3xnzaDCJnQp52Kh422t2d/QMtRAdatwV20qRbwIT7
73	NRZg1/XOm9h9/foxD4mlXIkJZ1CKO01J4R/oa3uYG9I3bRW9KFT37BJuaCN3ox/egiPWGPU4uTBS
74	TU2PpWVuU1mSVJZdkVSalx5rdQh+qzAExHi3KPpTLHkMZnf/fOp3Re93MV+t28vtikHb0WvKhiTi
75	dvFpqekFw4YXDsXpFHWD9KXmnTubmWRtvWfdtm3r7tm69Mgp7crV/9b+cuqpfT+/+uGHV39O9rcc
76	Pdry86NH6erN+/dv3rJ//1nPueY/XLr0h+ZznvjnNh87f/7Y5ufYLLsv2pc4XK2UqOng9ZVR51JH
77	nadMot4yU4VUmukyO0BME6zuRNERI1oy5e4O7Avij/QDeYjkw37lqfHJJJlLpsl8spCclJyc7EtO
78	SU4d5RzlGuW2lRA7SUuFgmFRd8soU6BTxkH6+4zcoafGPFv1Ry1MPJf7iKSd0j6e/uxdNbb7q149
79	pZ3asW/fjh379nOPTZlMrF9dIoq2SXtcW6vdnpR0tWwpyeBTz7/66ttnX/7N+xgxMY8UPkIOcTiF
80	n1FvA+aXuSDBTFtwKJyMHlrSL6HnNxgNRDYa7CgWK2eTjUbDVE60V4NsNVK+Wlxopoos2W0WowEf
81	IGBzmqhTvvBWhHjFHZ2ewIVOxwD7PAEDUpCx0Kgz0aBfilbQ/wxyoP9RY9iEkuySxA8SBomDbIPs
82	Ocpghz6zUkykIJ/g7kanQlNovpsc4NK1rr6JD3CuJzn37r7PDq/v277+EJfIvfF9Ykio7Hk4FCIT
83	tTbd068MXxIO4Zgmwgg13rsMqNwgBV3LrBW0NEmRpMxEP3jspowkmTGyPzL2Mi+Sd0xOrk7m0KmL
84	SL1MfyZXgCMV4D1K2lASCZk4TIXCodHa2a6HehbUVJGHyKR64mpenvHvZ/985cqff/FBHtn2zsXg
85	ghqSeAxTgqfUUdqTJ5/H0PkrrU17pvlniG+5vgp6D2fP7Wq22yndp2yw3WcxmDbQamEhqXZusNyL
86	lpfsRkl0STE8pDvMCpfCwnigI8Ci0oXOAAuinQi+t13u0Drk9rxjeXHT4xB5PrrhNIyGTFKiZXZe
87	fuoU//y6vtvJ5XXrNA93al1IgErt2Dua9YQmn+hrekc7BlFshYjNDeNV//XInKQ6CsxlNkp2sR9Y
88	TBRYe6eMc4Eh6+oKYLjUkeX9PTz5bobmjXV9I4mGaLg/X4/lXn0Ug+FL4mFE4oQadYgsiwbRIEuy
89	NFU2EGRltVlYqJBqO5jSDY502ZJukGwISJa4FBfiYXbqkHFHNG8gmuKuQIDF7oFAyBKO531uRkS7
90	YCB57unuGvcGd7NbQAJGMRN2QEeYRhBx8OxZ0kAbfstZz9b1jj3LEH+/mM+trOyp47/+/jGWnSPv
91	xETdL/ogR3XAMqu4LBYzsRRqjzfZHRkpOuEGErHj81OrU1tSKSm5PiXTaTfMUYjBxQeKizPYCZ34
92	l56ev1zp6bmyP4ykq6pZ2HuAjCM7l2FhGrmNTCZTyG3ac9qL2nHtuUpGvoQXXySJNQsXabO1J17Q
93	PqteuIjZ1IWjOxptKsE6Nd4kWGi1YaGNVINZMvKSaE83WhVIFzkZE7WO3vYOuYs5udyuQLdW3B7I
94	648nsh43ZJCjceP5ZIVck0YwDT3iyEwzElYtuUqp0qS0KK8oQomeKbAAEyUD2fSKNmmdMHSdNumV
95	EN99mZRqLZe/tzIWhDsR8Z8QsR0eUotwWcIFmbMKAjEyn8URTIpsdg5kPS8ymkWOQrWVX2i0mU1G
96	A1vFmCTBIg34qu5i9FXKtZ5Kd0sR1+QJICcMGGdL1FQjMXI85XmjKZbEcrGmBFuCfRCXbcu22wwk
97	hvgJJk4lJk4nCMZLdiaLya9J25Pk+K6+/3i6r+thzieEvt/I1yNF9gqhykq2LsNosw3XdmZczd+r
98	5sanWOJwQpH6uN3GJmfKjrTGpKbM7c5Sa72dixMgZUiqLccrgd8ieFNjsrNYEMWpH8BxURyRrLRD
99	67ryhYzJKZJbKUIXrKbL2dXZawedzubrB50mp7nTtJ1vF9rFdnd7TLvndOzpuNNeDEYlpGAg1DoV
100	5mhZeMpkYTalP4UpYOlNDM39ZsvGzbUrG9sOaYdubqk8+nbXh4Tb/eCy++X5pS/O/uRLMu2z1fXV
101	9+8gJ/v+EFo5efzJln87PqnuweDCi1lZH7EYexP2ug3XVpgnwQQ1I0VQ3BSS9hhj99hJPV0O9fZS
102	43ZHvNdS4ORy3Arvh7xU5lPQqTDvnNvZwbwzi7EenMLPN6ThrC3UucMAOtwujvlq7ALpj6Ksa51H
103	ScXwX6xrv3q1fd0vhmv7SMXu7Y27djVu3x0S1FBfVXC+9rueHu3s/ODhEFl1+uznH3/y6e9eYbOE
104	jVIijpIXClQvPOJporZ91oeVJtN2WhpvH2L1gssrZsez2fxWZD73MoDo7J6vTkBs0UjPFlYx0cgR
105	tXQhn+j/Y+tX2hfE+1XZb8sq3Y0PPLx/3941O7zkliPPk3wNwuSG3Dzt2+0bvvzii6/uWR/lzKWo
106	9aarmTG8jNaL22NL3mNQ6p1oPUOpbTvnyHHL1E9yoCDBa85m5uvG9L+442/Mp5ogTU5rSGtN49Hx
107	9A88czgRtAUptOCaNIzPb9X2MzP+9erraMZnyeK23dt37Nq1A80YOhycTwp7esjw+UEuK/T9mxWv
108	/O7TTz7+/GwU9Wy0oQviYZqaxBnd9WB8RGiyxjbBo47t1tIEo8nthXjilbIT2GBjVHsrYkpmSbmL
109	cdnhS1QTGxLpeThPznPn3efjBcbclKgx86/JqAy6lQ387N4vH/9Z3aPJe3K+OXNZ+xOJ+fw/CXdB
110	3LW54SEZV9wXP2pY/1wrGrqXDNMuHn3p5VO/ZgydjIdS4RJ6bjdMUj3U5Kh3HZRxGgIVbTlWv1PK
111	UfIwznUEejsu6JQM9CLevOebPER3fW7mF2N0rxeDe8TrOa9Zujv1XIaZ9zdjcoeOGZ2bO+Y/nu37
112	urWVlAvLh44dOzR39OjvB4VC9PZKbOMmxHM7jjlm6KpDrDcu56Gew8H1G2iOkGeOAInCQBCWa0CY
113	dRBm3CMgMgZeTA4923f5KM6KUIjNAMZ07DffhaOUiDF2qMHm8vKUeB4003rhYLzDTkm9ebsMys3O
114	hBxRynH6bTfyOV7RDzlcXhLLggMYyPqjbHFXlyfQy1jm8BTlHc9NbkhuTaY/4ErScSXhHsEVjbFu
115	3ce4lQjKCPGwMuswGib/iaWthw9pfHNp3YaNLcw0Ly9d9rv3+94IhTh4bdeJFzRvCKJcC2Ev2Hpk
116	sOqEJqvYxCgWS73usSYk2A+/gLCJkHfMF1fNUqWMAV/hivH0EwlXc1z5nn379uzZt383m6lxly+T
117	OO3L8V93dFy+3NHx9SJkj0YC2u81TTvHvJs2m2/Dt1shDe5QcwgoidTG7/Ha6qXUpHqfeY9ru7fU
118	d790MD05BwxeT0GKPSdRBr8tL33AyTELyp2dOrzAwFQ91pDRmsGSUfc1fs3fb7R+vxcxHTnU793a
119	rvN7bMi5iRVR9/Zi5eEf3J4WX1kZ4QB9F/HHwsMY9kxOgYBUr4AQs91mqlcOWsxGbgjIOQ6j35pj
120	z4uLjDuu5NojiZ72xhsI+A391xx1BIZ8jMoylXlZkN1yjOyRY3O9KqhE5VSq8qow1q3GqB411s0W
121	tUzZR3ycWPIDUeJ0osThHl2t9ntQZYDJEdLQd0PCtCmbd73Xd46xZfiR+iGL+CztyvRpJ1uRGSE6
122	q+Ll6ko74zlGIOoXliM/ytVEjxlkW5OLN0K9yB10lcYaZIXkmAQ/hVxkSjHr3lv6IrUXy+2ypv/q
123	Q9ivIwgvVk9+YiG2/xcDt2AQjG6D25hpyDTmxjXENcU1x5lLnGmINfJjyDXeKrPgk8cf/zWZpx0e
124	Nn7iaG6bcceu5p/Sk5Vksna8sq9k0613zN+1sfGXDHMhsvojjIVxsEpN9Sii1ebiHjTFIq3goKmU
125	hxwPIs4hN9pzZL8118uSXubyOyI//HQijVjGG0Gu/2bm1ZF7wdu/3G+Ib43nBuzu1e3uZWoRu6dc
126	kxbo0TbCQiWNe4/MeVY7kP945dFfHCbz59fj7OT9vWNCJ0PVZy9yRZV9D7+68+QL5JI+joBz04+O
127	vlVdgkmu1Oxyu+zNNrsbTyMluyGy5BxpZNkaR5oxzYfmeDDgaSQBd4w7zsvFj4yJcU912w3AG70x
128	ArqlWHrQKVmpsV4xx8e59aWpAXM9q4M3OTwJmL1+3B5dm2K616vnfJ5/mPT9/USQsFyWmYblswm6
129	bRJwj+azn/Jgtrsh3p4B2fYJMMl+J9xpmGuf414Miw3l9nJ3nb3O/SBsw6USMXEmarKJkhAneMV4
130	L/FyXhpnibN6bW4pLi7O644fBFkkh8uhGZYM6yCb354pZcqZSlZcltcfX8TdwhXRW+hEmEQm2MdL
131	E+LnkbncXDpXxBfa7rTfIc2OmR032zs7PkRCXIguMZRbyq3ltiX2Mmlx/Fq4h9zD3UPvEetsa+y1
132	Uq1cq9S61rpXx6yKW+VdFb8Rthi2W7Zbt9i22DdJm1wb3RvjNno3xt/FluFOPbs1RZbhlsjJpKe6
133	adysf28ijzRql8it2zT3pi+/2qotbSQZ2ssPkI8auC0kv7JSW6MV4qJ8pPYqHveQU+hsMJ/v0Yr4
134	BuRDAqHqXNLMEcken8B5oVmS7BYzZ2q247q32WDEqnGkyUg4IoicYSRSY6oxkZO8wMW4vU0Om0mk
135	XL2FP+h4LJFz21myj37LKFk9Q9xWmogMuNCpFHmK9F8IO3UGyF3v615KcfwvTLB/g0QxGNniEJdd
136	uDic55HnkgqylvAGyS1nCVlitjnb4rf7cYjmkJncHcIM4Q5xhjjTMNs821JOgphHlIpBw2pYQ9Zy
137	99J7+VqhVqwzrbWutdXZV0mr5NXKau/q+NUJg9DEQiGJ2jiykNAnW/RnoeHkpfHayjpy+QgZTAY3
138	k6Y1Wlygvjp3UeAnYlFx4ZjXjtLfV1b2ZXAfVVZ+P+ueu2TpzbE33cw8R2tfL51heAjjIWC7stPh
139	zAfKKWTlay0vHW7Reuc19PV+TfeRz7k8Qvu+0zb2dfV+E3mOrDRsYV8bnehnW197zbDlykq9Rc2F
140	LW7RW3SzBtM4bLCArGzY/WbL2ztbDFu+7v037U7NpZXhsrSLy6SBr3+MpEDG5Vi+w+lQ3Fxjwzyt
141	t+XwSy0MiJNzkDrOrvX1va0l9VZ8DYRr1J/bwr51ovtX8ugMHYr+VflaLPmY9HI0jTXKNb7WsvPt
142	ljd3NzAw5/o+0hzaCfIo6SS/pHdFvhdzcx+5//VHd86Xiv8CyUb9I+s799o/6z//9YO+G+UPjJ8C
143	gHHgmyw+Z6jSEgGj+l8/6K2RP/ib77l+nn15Y80fQdmG0TQZHkfZheUzggc2ofSgbEO5BeVZlKdR
144	tqDcJ/wm3C0mw0rhIiwXGmG5ASAoNmF9NrjwXif/OiwWkuEmfp1+XsyfhMVcE0xGuUnww2T+nch9
145	+i5MpoX6tUL+AYjjHwz3oPFaIzvXqH8J/2EbAnNgK7xJkshq8jVXy71Gs+he3skv4o/yV4TpQovw
146	V7FU/MiQb6g3vGfMMdYanzRZTJNNR8wJ5tXmDy2fWXdbn7OetH5g7bZxtqSInTAtNMFg2M++1+HK
147	/xH2RZq3kO9A/58Q1uaxb3g8+7/HKf2bNiuzUHoqWmZf+t6Pluk11/lrygKW/xgti5hpX4ExUA01
148	UAcroAKWQDnU6t/vF0EWngOQh3s+lhaihg9Go04trERZAWWwAKogB69OgmWoPxRLo2Ap7j64faCt
149	lXqtDM9l+MxqPAZR0wxjsRTCFmbDKtRYhLoLsJUluqYPy6x9H7ayDI81qLMQ261APR8+X43vXaDf
150	+3E7M/W3VCCfRqNWNVTq/09YgW1WYG2Z3qOh2J+C65774SnQ/82BW/he/X8ff7vl6GPF/k3D/jej
151	RP+x40Gr4mIM41u6/u+OLLgB31QIRfiecTAeJsBEuBWmw21oi5lwB9yJ/LkL7kbvTAlPBCISg2HV
152	sopAftHo6HlM9Dw2eh4XPY+PnEflAbRxG9RPf6PRN5z09fZ04fUgfV3l29Ppazb66hm/8GqQnvHT
153	0yX0lfX0pIWesNCXfu0SXgrQX7toW4D+SqPHNfqiRl/Q6PMaPdo6QTjaQ1sn0Oc0+ux6+oxGn7bT
154	p45Yhadc9IiV/jJAnwzSXyTRQwH6xONB4QmNPh6kP99rF36eQVvWmoWWDNo8hf5Mpo8NpQc3JwkH
155	NfroAVl4NJEekOkj++3CIxl0P+rtt9P9Kr8PH9znovs28HvtdK/KP5xB9/w0T9ij0d0POYXdGfSh
156	XTbhISd9qI2oqonftdMs7LLRXW0E1En8TjPdeZpvql4vNJ2gO+6zCDsUukPlG7HUeCPdvu2EsF2j
157	27aWCNtO0G0b+K1bMoStJXSrym9BXFsy6OZNirA5iW5uC59Ww/wmhT6Ir34wSH+aRx+IoffvpfdZ
158	6IZgUNig0YalstAQR+9dbxfuDdD1dnrPOkm4x0nXSbR+L61T6FozXbPaJ6zpoatXJQirfXRVAq3F
159	h2qT6EqNrtDo8hqbsFyjNTZao/LV6+myqpHCskpaNZIurbQKS2W6dANfaaWVKh/CV4Z6aEX5CaFC
160	o+VLSoTyE7R8A79kcYawpIQuUfnFGbQMlcp6aDBIF7npQo0u0Gjp/KFCqUbnD6U/0WiJRu+eQu9a
161	T+dpdO5YOkejd2p09gl6h0ZnBuntLnpbgM6YLgkz1tPpEp02Sh1Nb7XQyUE6KdUoTNpLJwboBCoL
162	E5x0vIOO48zCuDg6doxTGFtJx4yWhTFOOnqURRgt01GqSRhloaqJqsyOM/lb9tKR/BBh5FR6c7FL
163	uHkKLb7JLBS7aLHK32SmNxY5hBtLaNEIRShy0BEKLbTR4RotGOYSCjQ6LN8pDHPR/IBZyHfSwA0m
164	IWCmgcj43GCiebmxQt5YmjvULeTG0tzT/NAkszDUTYdu4IeYgsKQvTRnsEvImUIHYycGu+hglc9G
165	6NlBmjUoT8gaRQchsEF51I8nv0Yzb6QZtlgho4SmpzmE9Jk0DR9Lc9A0lU810hRfrJBSQn3JiuCL
166	pb7TfDK+LFmhyRv4JDNNUvnENJog0fh06o3LE7wzaRy2GpdHYzXqwZd6NBojU7fLJbgrqcvpFFwu
167	6lJ5p5M6UM9xgipoXkWjuMYT5NFUQvzSXmrHe3aN2rABWyy1qbxVoxasWNQRldSMOub11BSkRoMi
168	GF3UoFBRCAjieirgc0KA8tgYP4Rio5yZkpkUNEraSPDBRjL4/9sN/l8D+F83zFj+B8BX0PAKZW5k
169	c3RyZWFtCmVuZG9iagoxNiAwIG9iago8PCAvTGVuZ3RoIDkzIC9GaWx0ZXIgL0ZsYXRlRGVjb2Rl
170	ID4+CnN0cmVhbQp4nKWO2QqDUAxED9hWrfvSui91+f9fdLiIDxffGjiZmYRA4M9yrPzgefmXcPHw
171	pW8C9ZCI2LpIRCoycmtTUF7+I763H1TUNLR0Z+5NH8TIxCz9iYXVzDf2A5d8Ar0KZW5kc3RyZWFt
172	CmVuZG9iagoxOSAwIG9iago8PCAvTGVuZ3RoIDM3OSAvRmlsdGVyIC9GbGF0ZURlY29kZSA+Pgpz
173	dHJlYW0KeJxdk8tugzAQRfd8hZfpIiI83UgIqUo3LPpQaVdRFsQMEVIxyJAFf1/sOxCpSDC6587Y
174	Yxj8U/Fa6HYS/qfpVUmTaFpdGxr7u1EkrnRrtReEom7VxMo9VVcNnr8Ul/M4UVfopveyTPhfizlO
175	Zha7l7q/0pMnhPA/TE2m1Tex+zmVQOV9GH6pIz2Jg5fnoqZmWe6tGt6rjoTvivdFvfjtNO+XskfG
176	9zyQCJ0O0JLqaxqHSpGp9I287LBcucia5co90vU/Pzii7Nps+aHNRzgjXhx+Bj4y3iRcgiR2CTjC
177	WlEIvMpgpUiKIRNO2iRcCcn7rvJ5pS4pxoo2nBGBI+CIccQ4AU4ZbxIujhI37G7SuQm6s+GMCJwC
178	85IJr5Wir5SPtsoQAd2l8ZqDkiMknzflE6YKWDFWjNGd5I/FMm1W6pIk9pP8FSS/d4mNJTf3kHDx
179	hiX38ZAXO0brvNiJsuO/jau6G7NMqvtH3Ija4Ww1bb/R0A+2yt5/dkDihQplbmRzdHJlYW0KZW5k
180	b2JqCjE0IDAgb2JqCjw8IC9UeXBlIC9Gb250IC9TdWJ0eXBlIC9DSURGb250VHlwZTIgL0Jhc2VG
181	b250IC9CWEdFVkwrRGVqYVZ1U2VyaWYKL0NJRFN5c3RlbUluZm8gPDwgL1JlZ2lzdHJ5IChBZG9i
182	ZSkgL09yZGVyaW5nIChJZGVudGl0eSkgL1N1cHBsZW1lbnQgMCA+PgovRm9udERlc2NyaXB0b3Ig
183	MTMgMCBSIC9XIDE4IDAgUiAvQ0lEVG9HSURNYXAgMTYgMCBSID4+CmVuZG9iagoxNSAwIG9iago8
184	PCAvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTAgL0Jhc2VGb250IC9CWEdFVkwrRGVqYVZ1U2Vy
185	aWYKL0VuY29kaW5nIC9JZGVudGl0eS1IIC9EZXNjZW5kYW50Rm9udHMgWyAxNCAwIFIgXSAvVG9V
186	bmljb2RlIDE5IDAgUiA+PgplbmRvYmoKMTMgMCBvYmoKPDwgL1R5cGUgL0ZvbnREZXNjcmlwdG9y
187	IC9Gb250TmFtZSAvQlhHRVZMK0RlamFWdVNlcmlmIC9GbGFncyAzMgovRm9udEJCb3ggWyAtNzcw
188	IC0zNDcgMjEwNiAxMTEwIF0gL0FzY2VudCA5MjkgL0Rlc2NlbnQgLTIzNiAvQ2FwSGVpZ2h0IDAK
189	L1hIZWlnaHQgMCAvSXRhbGljQW5nbGUgMCAvU3RlbVYgMCAvRm9udEZpbGUyIDE3IDAgUiAvTWF4
190	V2lkdGggODc1ID4+CmVuZG9iagoxOCAwIG9iagpbIDMyIFsgMzE4IF0gNDAgWyAzOTAgMzkwIF0g
191	NDYgWyAzMTggXSA0OCBbIDYzNiA2MzYgNjM2IF0gNTIgWyA2MzYgNjM2IF0KNTUgWyA2MzYgNjM2
192	IDYzNiBdIDY1IFsgNzIyIF0gNjcgWyA3NjUgXSA2OSBbIDczMCA2OTQgXSA3OCBbIDg3NSA4MjAg
193	XSA4NApbIDY2NyBdIDg2IFsgNzIyIF0gOTcgWyA1OTYgNjQwIDU2MCA2NDAgNTkyIF0gMTA1IFsg
194	MzIwIF0gMTA4IFsgMzIwIF0gMTEwClsgNjQ0IDYwMiA2NDAgXSAxMTQgWyA0NzggXSAxMTYgWyA0
195	MDIgNjQ0IF0gMTIwIFsgNTY0IDU2NSBdIF0KZW5kb2JqCjMgMCBvYmoKPDwgL0YxIDE1IDAgUiA+
196	PgplbmRvYmoKNCAwIG9iago8PCAvQTEgPDwgL1R5cGUgL0V4dEdTdGF0ZSAvQ0EgMCAvY2EgMSA+
197	PgovQTIgPDwgL1R5cGUgL0V4dEdTdGF0ZSAvQ0EgMSAvY2EgMSA+PiA+PgplbmRvYmoKNSAwIG9i
198	ago8PCA+PgplbmRvYmoKNiAwIG9iago8PCA+PgplbmRvYmoKNyAwIG9iago8PCA+PgplbmRvYmoK
199	MiAwIG9iago8PCAvVHlwZSAvUGFnZXMgL0tpZHMgWyAxMSAwIFIgXSAvQ291bnQgMSA+PgplbmRv
200	YmoKMjAgMCBvYmoKPDwgL0NyZWF0b3IgKE1hdHBsb3RsaWIgdjMuMTAuNSwgaHR0cHM6Ly9tYXRw
201	bG90bGliLm9yZykKL1Byb2R1Y2VyIChNYXRwbG90bGliIHBkZiBiYWNrZW5kIHYzLjEwLjUpCi9D
202	cmVhdGlvbkRhdGUgKEQ6MjAyNjA1MjUwMzA2MTArMDgnMDAnKSA+PgplbmRvYmoKeHJlZgowIDIx
203	CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxNiAwMDAwMCBuIAowMDAwMDExMjI5IDAwMDAw
204	IG4gCjAwMDAwMTEwMzUgMDAwMDAgbiAKMDAwMDAxMTA2NyAwMDAwMCBuIAowMDAwMDExMTY2IDAw
205	MDAwIG4gCjAwMDAwMTExODcgMDAwMDAgbiAKMDAwMDAxMTIwOCAwMDAwMCBuIAowMDAwMDAwMDY1
206	IDAwMDAwIG4gCjAwMDAwMDAzNDcgMDAwMDAgbiAKMDAwMDAwMTUxMyAwMDAwMCBuIAowMDAwMDAw
207	MjA4IDAwMDAwIG4gCjAwMDAwMDE0OTIgMDAwMDAgbiAKMDAwMDAxMDUxMiAwMDAwMCBuIAowMDAw
208	MDEwMTUwIDAwMDAwIG4gCjAwMDAwMTAzNjQgMDAwMDAgbiAKMDAwMDAwOTUzMyAwMDAwMCBuIAow
209	MDAwMDAxNTMzIDAwMDAwIG4gCjAwMDAwMTA3MzYgMDAwMDAgbiAKMDAwMDAwOTY5OCAwMDAwMCBu
210	IAowMDAwMDExMjg5IDAwMDAwIG4gCnRyYWlsZXIKPDwgL1NpemUgMjEgL1Jvb3QgMSAwIFIgL0lu
211	Zm8gMjAgMCBSID4+CnN0YXJ0eHJlZgoxMTQ0OAolJUVPRgo=
212	EOF_fig2_calibration_pdf
213	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e31a277a-fd63-4451-af81-a70d859de7a1",
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "3771e373-e962-431e-a7a9-d1405b08f391",
  "sourceToolAssistantUUID": "e31a277a-fd63-4451-af81-a70d859de7a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T09:13:01.412Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NHCSHb7GtvYYw2HYbrRrGz`</summary>

```json
{
  "file_path": "/tmp/paper_transfer/cmd_fig3.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3771e373-e962-431e-a7a9-d1405b08f391",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2hawj8ekSzooxgmwot",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc226cac-d678-4fd5-8496-b3c8957e52a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iUXNQY8qGSWcQynozVf6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7312,
      "cache_read_input_tokens": 6748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7312,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T09:13:01.728Z_

<details><summary>↩ Tool result · reported error · `toolu_01NHCSHb7GtvYYw2HYbrRrGz`</summary>

```text
File content (31760 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc226cac-d678-4fd5-8496-b3c8957e52a6",
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "f047c4be-76a2-48d1-9fe0-a0cb1588275a",
  "toolUseResult": "Error: File content (31760 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "fc226cac-d678-4fd5-8496-b3c8957e52a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T09:13:01.880Z_

<details open><summary>🔧 Tool call — Read · `toolu_0197RfsC3fwBSraFYiucsUqG`</summary>

```json
{
  "file_path": "/tmp/paper_transfer/cmd_fig4.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f047c4be-76a2-48d1-9fe0-a0cb1588275a",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2hawj8ekSzooxgmwot",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "383d3019-9476-453b-aca7-e15299d12b43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iUXNQY8qGSWcQynozVf6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7312,
      "cache_read_input_tokens": 6748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7312,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T09:13:01.883Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JKRBDBogYAT5kJF8a2HLpD`</summary>

```json
{
  "file_path": "/tmp/paper_transfer/cmd_fig5.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "383d3019-9476-453b-aca7-e15299d12b43",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2hawj8ekSzooxgmwot",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5fd0242-ba0c-4187-a044-c48dbe164b6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iUXNQY8qGSWcQynozVf6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7312,
      "cache_read_input_tokens": 6748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7312,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T09:13:02.145Z_

<details><summary>↩ Tool result · reported error · `toolu_0197RfsC3fwBSraFYiucsUqG`</summary>

```text
File content (25289 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "383d3019-9476-453b-aca7-e15299d12b43",
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "cd825998-3f5b-46e5-94cb-2109ecc2740c",
  "toolUseResult": "Error: File content (25289 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "383d3019-9476-453b-aca7-e15299d12b43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T09:13:01.888Z_

<details><summary>↩ Tool result · `toolu_01JKRBDBogYAT5kJF8a2HLpD`</summary>

```text
1	base64 -d > /root/trace-verdict-study/figures/paper/training_dynamics.pdf << 'EOF_training_dynamics_pdf'
2	JVBERi0xLjQKJazcIKu6CjEgMCBvYmoKPDwgL1R5cGUgL0NhdGFsb2cgL1BhZ2VzIDIgMCBSID4+
3	CmVuZG9iago4IDAgb2JqCjw8IC9Gb250IDMgMCBSIC9YT2JqZWN0IDcgMCBSIC9FeHRHU3RhdGUg
4	NCAwIFIgL1BhdHRlcm4gNSAwIFIKL1NoYWRpbmcgNiAwIFIgL1Byb2NTZXQgWyAvUERGIC9UZXh0
5	IC9JbWFnZUIgL0ltYWdlQyAvSW1hZ2VJIF0gPj4KZW5kb2JqCjExIDAgb2JqCjw8IC9UeXBlIC9Q
6	YWdlIC9QYXJlbnQgMiAwIFIgL1Jlc291cmNlcyA4IDAgUgovTWVkaWFCb3ggWyAwIDAgNDkxLjMw
7	ODk5NzkzMzkgMjA0LjA5MTM5NzA3ODUgXSAvQ29udGVudHMgOSAwIFIKL0Fubm90cyAxMCAwIFIg
8	Pj4KZW5kb2JqCjkgMCBvYmoKPDwgL0xlbmd0aCAxMiAwIFIgL0ZpbHRlciAvRmxhdGVEZWNvZGUg
9	Pj4Kc3RyZWFtCnicxVpLbxzHEZ7z/Iq5GJAObFZVV7+OUmwLMBwEsgjkEOcQMLQsg5ItKYnif5+v
10	Z5fT3bOzM0tnpZVEQvuxH9VfPbqqmtdf3/3nze3dDy+eD3961V+XT7cfex5+wdfrgYZf8PVp4OEF
11	vl73hE9ve01sLMWUIj7e1x+F1FBimwJwaj/+3Pc/9dfPsMxHTHvR90rGWxY3WDEpkcf/3vaibJIN
12	QWMF39cwp2RsTEE07/2wRoPut5LdVq8hOo5hIg6CjTPSe2+Uo6pvNi+oJKMPe/fPwcWn/j2+03BF
13	WM2zIRZOnthbbG1YfQxuuH3bP7/pr7/lIRo33Pw08nXzz/5vw5POdfR0+Ptw813/zU3/sh/F6SG0
14	TyIaGjEKui4GeHdRYhArIZwoBne0JAjn/b0nTY0kFbwuCoua6LwP1tvEJ8uySApDDWJTbA2joBuS
15	uGjYkgZNjtyJksgRVqAJx9Y7bkUp8IYs0JCSSvDiOZ0syyIrULIJMaizrb8UeF0W2JPxIVIILthT
16	jdbOeakPR944q5oiLCQNzkRul2OarXbTfej+0b3p3o1fr7uhe9X9q7vrfmt2GBbiglAOMV5TSNaC
17	SNiCxY9SDNHH4cPd8Nfh3XD9zGaHl+E7OLvD6bFOouylISr8vg1xj4k+/av+5fB+F0KWJ9oAo2vB
18	ZSXsWYKu3Cb7vnM1M1mE83DTIxCexI1zRoNPqaVmQo8xU02biKknHefFiSHnmDUQpVVyQmuYFyAn
19	BMRGa5227BT4GD31xImfZtpxgoIap6AnKXHcIOjS1sNEBvEh8Mx+KvwYRc3UiaN24nGSUjAkEE2Z
20	ZJ2keHErYkidrKc4M6MKP0pSPbWQ1Ew8ThJzvsVUKEayYYOli5uSInzgCtO5KRX8KEv11MJSM3GF
21	JUVEIsKd6Qh54RpL6fK25BFEoE+2M5YKfpSlemphqZm4wpJXo9EnGwXhe4Oli9tSIizmOMQZSwU/
22	ylI9tbDUTDzMAgOqijwsepOQe5HgjI/M0t/3eaWrvCazYUiMqwDBkBh/YrK6mnc9HQJytczrE6Rb
23	H5F0Dd2z7hZ//z2mZLfd70B+fNJ91f349FzayWrhkT4yHMTpqJqsI0G6isGkQ/OTH+YaQ2WJ3Jad
24	5qCGeUhzURPVZRr7aCJF8Zn5aHPuYDGEIzZ2ZF127lJNZQUEaMADrSob8IcT4jiS8anMaOGS8jd4
25	lX43OMyHRrM86eQfcon6qcH6tdF768omMVGEiO8rmqy1OVoN13+m4etfp+HsISOcBAbowqAolRD/
26	ZRfZ1scy2MVlkdjJaLwbK5uUUzgSCzoOB1trJNhI8B/WAVHEWomcnNjNwXTmEWcy8oGhMdRCZJMw
27	CCDY4k5fFFct26NwEgo8M2x4uajloK1hize42Dm41rBZIRtnxbSWjRBlcW4XWssuztRaNmKhRd1M
28	dmbZkis9m6iybBB79Lgfdo0jHhtHa8OO2vFEiiIl3imLV4xtd5U7lKEubY4GV2AQthlI/OboKygC
29	LEPvXtUtDJ+Z8i73SmBVl0RpR1+Ne+2NKmwvvlObc040nrD4kYPuLH68Nae+2Am18XKrDebwyEo6
30	N+N2LnPyvdAr7Djuq0i/a1u87R3ONwPvey8HIz97NK4ksZV4sEpm73yFAkuItpyh6EL2AgevTE69
31	DlgFTuc9D7c9UB8IKUVGkc8EdnnkdF4srLnp4g8oGOfuQQ9BAwLrUC2H/0WPq7HeGOWSZ4opT54k
32	RNZiPdLfoTpImA4ynThUGyMKOYQnrQfioPnaqNezRiGN9e3GNreKU7S1iHJ4Elk6sRwyU5YrBJaN
33	a6onCYtOykHs4Ylt2fjnnO7R2Cjf9ZXrJnF8sESIIrPeWDhI+b7p/os87K77DdnZm+7X7l13NX6/
34	736vM7LqwlkJrQcXzuRAqoZs6z4PUOU8BTpruC+KylXVXgw/g+4ryE+QHEAT92N3f4V/RKIx/15j
35	/1tkwvf4ewX2dxnx3S4j/r77yywn3j9h1M8jtH8e6QUZptI8cMZgwu59pA6FFdxE1GmNRz5pIAQb
36	5KA+tW8aFbzeIEaugyvYIvv4f181bL6QvUXm1EpS4A1JctrioLMzPGzYEE2wQVKa9WsneEOWMIb+
37	JGd42MCJTC7YWut4ANflULKoxHHvnOFZA4mMkZgds5WkwBuy5Mo3IAs5w7OGQhHORUTlVpYCb8gS
38	xpYgDOVMzxoWocaSQ+Jy1meNMeU6jA6foc9RdkFK7XHx8SwGTfCsy7E4USJkbcHFTlDO2ONIvMUR
39	1EX4i7r1tiJ15rBl9oVJgtwpwmJajib0GEXVtImhetIaQbhlnRckksjUZZMgvjBBSQyW9zpjqMDH
40	KKonThw109ZIiojPIYVgxfltK5ILk8Qcc+Xuxyq+vtgLfoymZurEUztxjahc+6fkg3Jg4U2m7KWZ
41	QmrpLUL7LDOq8KNM1VMLU83EVaaQCArbwDDAsN7Kz0zppZnCzRaduPGZsGaq4EeZqqcWppqJq0z5
42	XKyRxynEbtvUQUP/SzOV3/t8ciIzpgp+lKl6amGqmbjKVMrVYMA/iLiedGSm/JGevrhkvB+rlcjG
43	IS/F8ltd/YO043sUjB+7j+fSxhka+JIc0jikz9n6ULkll8YOflWU4LyBFZEOVFuJJoJdVAi56ZBC
44	TFkDVeGA8s8KJ5c7lFUOr7lwTUr5WpkS6tzNVMLPM1hyW4UJoMAZ0ZJlAoVjyBft3Rd2ds37iSGL
45	ULVr2MlKZzJpLnApes2/YLc5XDyiHxiPuYF4wuo5xU9gFQItjJ71GlGc4KZWlATRbo9mg+QH0QWQ
46	bI+GZkRhphBuiZWD0ShLduf01egzucIj2/y1/SfOts0SW/tnJNZ5sTRzAGabNYAauPUAXPJgj2Ai
47	rQsgZMHIaXx9mlyAOZs1Shrf+kBMCDIpOW6dgEmMj1HHF7LP1OifG/1Ei41hb2h2xSxRnT3YAqXt
48	4QtGvzI8mOjhtQTR/MLgmaWJNQ53RGBPaUmUdnhWJ0WNiDEhnLA45bdilKG4W5ZoOW3x7Vb/Ysdq
49	uQUFg3hMf+uPtvrJ5no/v3DkF1XkwG78RTKFKacDPNt6XBj/+Xv+jTyhlhMXuMCetMZHj5Txhsqo
50	zb8HwCOqpOp5REMQm5OI0X9R/TjOr9DRsAaE+HH0tGM03nlkHy06nX+3RoUHZH/khnrlhFApDkG+
51	kQOoJ4q5Mu1rqVM2SBfhGPUJ4b3TCQsfBb0deVKHwlia0ZQMpKDYrkw5LnmyOpMDuBAUwY3UFJdO
52	2KJFjhov7FUrV0xXcjR6qaSutVhOWGt8yT7WnwxUdGfL+7so5t/aYLe/iy74elD5ZMDmIER05pMF
53	b32yxs/7mFBrNLhaKlnA71s8VXi9ToVvPTDMtRVQiOO+FruprUe8Nrzs/wc0IAJhCmVuZHN0cmVh
54	bQplbmRvYmoKMTIgMCBvYmoKMjU0NgplbmRvYmoKMTAgMCBvYmoKWyBdCmVuZG9iagoyMSAwIG9i
55	ago8PCAvTGVuZ3RoMSAxMjUyNCAvTGVuZ3RoIDg2NjYgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4K
56	c3RyZWFtCniczXp5QBRXtve9dauq967qjaVZuput2QTSiIiiaTfcojEuREgYQRahQcCAC6DBJOMu
57	otEgOkZI4piJk0Q06hg1biFmEuOYmZgYx2SySBbzEV7eC+NzCFS/c6sbxdm+vL++r4rbde+tU/ee
58	c+7vLLcohBFCRvhhkX3yxElZyISSEcKJ0BswedaDcxRrvtkF7YkIEWbynHnj0cu3WoB4CtzPnDFu
59	7pSwgZwr0P4l0Mx+cE6yq/y/qrcixH0M97MLFxdUkz7zdoT4FLh/tnBZrb059be9CCl+gPaOkupF
60	i79Z/Z+dCKngebRpUUFNNVLAidQitLWLKupKCha+dhvaoQiFXSgtLijS/uX8Ywg5u+D+iFLoMNo1
61	HyIUC/dRVOni2hWnt5oOQNsN7cMVVYUF7f0v8dCGOVH+4oIV1WwTl4pQ3Fxo2ysLFheHvJsG9+Nq
62	gZ+S6qqa2vykAQtC8Z/A/Y7qx4qrl9bxtxBK2Awy/QJRXWmR72CgRVCS3EeLGqWgsYidmPXAXGQt
63	rHusAlkXPVZcjqwVBbWVyAr6hcPr9dGXFz9WiZT+JzHcY+SrEjGMnVIymUwlzBSAhhze36GffXi3
64	/ov+T+TfV+An5n8x2j7pnHemv7506Pj/ah75Xs6/HZNyMt27/mczMd0nv0+Cf39It6UP/JzFeAu8
65	BfBUgX9W+eot/zs+fvbxv6H22n4+rfTDzyTEgAoF2KgZWQAdgSgIBSMHikROFAv3TNCHAUsEMMQh
66	nlrSPYcKUZz6DiXSAK0CRchP/LOD+K+DYynhWRU8pUU6pEcCEpEBGf28DNrASDQKcbIN2GUbiJdt
67	IF62gfjFBbWlKP6OJQyVij77OfoWzUKZIOCntJN5EqZ2gt196GfDeS97g21c6q/P+xnq08O4y/7v
68	dCjXR0uvd+pDxrinP3dIu/BunRmJ0E/NUM+882gs6C1A1rYVjZf1TjVLpWf9FAQlUDoVtbJ4oI9V
69	NcH9OKghVcs9dEl36IbdoUu8QwessFa8FcZHXCpHPXi470quohLGCNzxPOF4jmHoiHio6LNKJhUh
70	N7KjOt4smfFuxWJ84x4a4i/U51I0vQctLLdZ1CFLSX2YEn6jgfMklIHGoSz0AHoQzUUFqBAVo0Wo
71	DFWgarQU1ck4oJSxIEcKUE6SKefcQ1mJHkMrvF7vDe9n3k+9f/Ze8/7Je9n7rvf33re8r3uPe3/n
72	PeY96n3Ne9h7yHvwXmn+7eHz5b3+lknmxFeofNH+wsoyQZCAwsn6RrL2qXVBXAP5fJY1zl/oOJOg
73	ZEExQ3nAX6g3f9BfAqHMgULjUBCUAn+xQin0lxAoxf5Cdb3IX8KglPlLOJQKf6H+phJKtV8GiJOI
74	4iMSygoodVCcWI1qAHfH0UU4P4DaA8iDlqB1qB3qX6EGuf8cq6Qn9FzjKO0H6DiOAzqGnhjyA7ie
75	hnFS4d5XQF8C7Xa0UL7fRy7J525yiVmOGDILarPkJ9rRcTKaZcklX5GfuojGoBPoAK1zlxBF7mx0
76	Fc7xMPo0dApdw0+hffhDtAo1oRoZ/GFYDR7BA+dC7kP5/AE9Ks9M+zzch7wZZvKAnKdg9H2+fhyH
77	Z5N8UoLng4QMPkCmQO8a5GHz4XTK50RZPp8MDNMA8/vlRZeYR5k41okPwDx0jksw/gE0BvgtAU6n
78	QGEo/+QmaicUUcHcOTRNMY3XYl6xClaYQQ0kFe/mw1A+WkXmwggzoa8JzcRXYRaAyDGeYwkD5msX
79	O5joqUUd7ofm23+f4xiW+HdNu6iwd6BZHbo6+3Gvd9Z8NoTL6eBCO0i0soONjvziX938Ylji9Fnz
80	7R3vTJroH3VS/kTomzMfqrQF3dA/aSKFNvAGKw92SQDtS7w3FHGgYQ0glkaZVLTQnRpDnFHOKBId
81	Ez1D6wniPUnIE2X0BMWE58dGlQ2PtghOFRG0Dos2RKVNCCHa+zTDxd7uzivdYs9HPQZjBvzdh8Qu
82	V29mp9wl9qQAKwqR+56WnAgcwVvMAamuEWnDY4bWna4Ai5mPjIhJGz7ClIojTUPa+OL8wuLseYWF
83	5NDDhUXZ2QsL5+09cfLZ9hMnI1r7c1tD9p462db2+glu+/5ntv/mxR07XhyI/M0z2198cfuOl3I/
84	OXny+vWTp64zn//tR153/eQbf75+6sQn4Eeel84xTYAnHQp16xQ6xC/R80htIIxe7O3vdIEQ/e9l
85	ZKTgGMYgGtMtPL0EMk0/3r794+61a3dL5xbja7gQF+Frixd6pEbpBWmf1OihvnQbjLxKHjnErVVA
86	5rdErzEoEKsXr3S6ugcHNqWNMBpExpkWQC/bdq9bt7v39m3p3EIPfgI/ivPwE56FiyWntEd6VnLC
87	qLn4KpPL1MDKiUcZxEJiKV55Dwa78l6KyWFx5DJIQkzNHqA8572BL6IeWNeRR3SQAGvFK/2d0ztM
88	D80/oob1ZzMzxczMnPvQEVKgytfC6vnucZhoFL57KenDR6QOLsC5BzLSZ85Mz3igdOTMmSPTZ86g
89	KFrnvcE2D2LHbULFWr7YWKbNDyKwpCpe0ATBuL1U2K5ewEFKtItKGRkhazECGUSU6qK/zKZdra27
90	aPlR+g9s+LEXi9IPWXgWnoPn4llSh/Sy9IrUUYhbcSWuwq1SqbRNeloqBSn7wJH3AgdqtMIdyhZB
91	vCNFPDeD8Czm+DIlrkEqhQGSbw1ovbO/8z6U3O3q7TRkGDJkQLKAR5bicXqHeu78N0AQNwyqQRrv
92	2ZGG9JE5bpUd2XGyKlnN5gGNRqbxnvXRILdM40hzGLi06FSDw4IjMSt9gCs2YtbD/vnNp7r76mUs
93	bIIQMxO4DEUz3A6tGQk6VMsUWYu5Mt1yg1mnDURqHMgr9WoRGzVhYi8YEjUlQ0YGmFFyz60eqUcE
94	pjNS3JosdZYmS5tlzrJwgI5Iw1ic6mItZnBE2JEGPKThsRgMKTKCx3x1+bXSm1gv/SFIK61jqpb2
95	j8Fvtax+dmPzHnYJVmdkfnn+unQ5EO4dl/Ytxp0tP23ceWAL5XcPrGsj8BsP/CaowoptplpjcWCx
96	TYBdVHFMMSkT8hPs4aqwyDg1iuR5K681q5GRSQDOu++ynuFb9/5u8QIVoAfQTrmlgFKEY4uZdUTE
97	OA2p4dhn+wk4zVcB3hWRby+9+ovrtw7sOX5R+ka6vfSzymr1q3t3HTrWscB18ODWdeue0VVzLYlJ
98	b/xm3VG79epv//iZKxVHbN1xaHfH0ZJtTz+1afXjgM/7Qe8dIAcDeWybO5opUqlVuEitVs3Aai2q
99	0YMzqlGXEUbJ8sigI4JGyRjF3iuZAJVM0Dfovqs/80pmt8sPF5H1+6/DySqM847ZVXadXU980Jje
100	oZ37yPQOHf0R5j4CSDHKSDHC6UOKO0iDrXgknopZnglgYtUjmJHqycwUtSIP5WGDanAFKZQchlTm
101	osSQYwPzfxioZbZcwGHSjR9wH7H2fy3xHhy9mPT2q8ul63S9XoX1qoOYaUOvuKMJH7bCWsyLtUKx
102	uRhC1HK0UJtvDzMw6nAUyKvCDWqBsfu8dSddKL91ymskdRnB2U3vUM2lEt0RxC4LAqbgFwQojEBh
103	8t2UbcZOiXxSxghEYAVO4AWFoBSCBasQIoQKYUK4VkACtiEb5BfJmKcyg5gUEshiRveCQcaAgeUH
104	5g7flP1fOEj6yosWfbxkieqF7XsPvNSWuyEtm/twnzQ3Kkrq/fZ76b/p6m9pef/N85fdE5ge6ps2
105	gE5aZN8UjQrdEVrEFwuo2GKrCK+LLA4ps+TH2NXhAYQ3WrS8igvSxIBKuu96q35fKAOTi1ZpVToD
106	K3IiLyoMSpPWpBP1oiCKBkOcNk430zbTPtNhzIse5BuCGRkUKlJ2cg5XQKAlMgmD42P2NrW2NjW3
107	tL4+8eWKzzCRbt4ckH7A43H0g68+skT7ZOX501mXz5+//Ps33v6I+WH6NJDuBrjEOvwLvB6/Gh5+
108	q9gj/RnU/TIg+ylYcSV6zB1GaHbOEIzRDHDfyxULMeQasENUI55RUZs0BFIs93YPwvhOGKYrDUuo
109	ktdXBeeQ9aX98tKq6H25/0ggDiJMngr8nMMSaXCwTw0cf4YZNjBzKbnKVfVt4+47jh+F2ER13+SP
110	C8lorDsiKogUW1TF4UJxfFl4fkpUkNbIObXcMMSHWHje6dCkUDZ7B13HYMD4qIfG3kGtAjLIkLrP
111	h0RGREFukJ4ETs8frMiJtq1b22iJ27iyYdOmhpUbKw6clm7d/m/pr6d/u/O529eu3X4Ot7YfOtT+
112	3KFDZNn61tb1G1pb3wm81PanGzf+1HYpMOTg+iOXLx9Zf5Di6Am/LMGAozx3FLLai4mpwlgXWCwQ
113	a7EKXGGMWW1EfCSntYTxxgCeIqkLZAH+fXKAlVH3R7EUYsM2xkZsrI2zhdtsNrvNYYsYZxpnHmfR
114	5WE9IASlDfcHRWoQabJBGIemSOT0hFcX/0Xy4sCbA1iQTkufAHKqdU8uPn9aOr1l584tW3a2Ms9O
115	n4a1397ABmmd9Ly0QpodHn67uAJHsxEArvffAXBB/ge7Iu46YIgBB/WK+yFEoydThGHfyBkNjAhx
116	VJC7ID4rlAosKhV6KBotoxOVSsUMhtdXIVGrJGwVv1BNDKKg12mUCngAI51JRUyQlPiAl9nVHei6
117	0m28g75AlwIgSFGolJGokLv8DfCusUbwru4A6i4EvSCwsVwsH6uL1ScaEoyy33CoIFhgOC3gMomD
118	pFrwbiZK6hmY8hRj/g1j2T7wxf5VA5tX7WPCmAs/hXm48r5nPB48RToux+Ml8p75Q0DnbHe8xSQ8
119	YVite0KjUK0mVdxCXGVarXkcJBP0SoE3CwEsijKqDYyDJjOuLtcVOcS5aCpBHUZ/p9gldYmdKUdS
120	gh8MZnBeKjjxSMgJaHH46/S65PRp9nDDwGx8s6FBCmRON3g4VC4d+aOkPSmJJwea/ygdGeQtHXiz
121	oCy3817OTLjKz5hZrRT0/CBjAX7GINcGrFHOenpckDTInKX8M35SLZSbCw0DY7EE3DD/cS8vj9/R
122	kg040aEUt1WjUlAWVKtxFeKjlGpBC7MrYXJIlLupUsQued5bPS7QhX9O6iN8kjOTTzMHZInLfzL0
123	SZuoZdV4b/Bhspewo0S3EVVq+cogyB4dRB+i0hujHSJ1CHeSx2MLIqoi2iMIzrs3jYxxxjBpw43p
124	4HPtyGBmFHpMpvy1r++vt/r6brV6C6oXL65e2L8bT8JbK6EyEz+Ep+Hp+CHpoHRUOiYdLC8qqMah
125	R4/isOqFhVK29MJr0hdVCwupBl4G2/8KOIzDTvd4mC/KIWq0mnAbE2YXtVrNDI3W7mADcCOYTqUz
126	oNFSZK00ljnz4+0arSNMGShYGAEp4yyKqLA4JDDxcnrUBbKIdI80NEECBwGm4jMP/fdQ9V/AFsQE
127	agsae0JKwqyE6oTVCVze3fA7vcMsx+B42VHHo/jBGFwbq47T0PAUZ4uzxzniIkaqMtSjNKO0o3QZ
128	+ozwUbZR9lGOjIiRkVPVUzXTtFN1U2xT7VMdUyNy1DmaHG2OLsee48iJ8Kgq1BWaCm25rtxWYa9w
129	VESURTaoGzQN2gZdnb7B1mBvcDRE1EWmtyd0JDBgmemGwMEQnoypU44CpxxokIMf9WE2PJj5na7h
130	Tp45fHLJsbc+Ooj1vaW3Ny8xHDq699cr33n94ivSd9L3Dd4pkP0feKFpXUVt+uhx5186/adhCdL5
131	vU1PNJTXZ6aPeaPt2icuukpmwOl4wKmAGtwhKk5DqhQLdQBTtaBkBV4fpdQaUBTPiLAF6Orv7KLq
132	p1B19UqZna6UwRgoyioUkehX4WGbAQ9J7CiFHCVFSulTsibZkG9oNrQbzhi4PDl3o4D3Gxhed0aa
133	2sAlNUhTz3jY3ps4X2q/+ZPWQ5FfArjaxE6EXUssetydHOLQBINZ4/rg7cpmk2NLZFN4c8xmU762
134	Xs8Ec8gxLEKXaBWQU8NZIwLi43xZtsvV5YMRlaVL6rn1tQjGB8HTkAGO1h0lxlfFr4g9G8/Wx57F
135	Z5mzpJPt5Dr5TktnQGfg2aCzwWetEHLycNqdgGoyUHdKgxDdbqc6BtOwNDlrJ8nfb1i7vram6fg+
136	ad+Y9vJD7/dcw8z2NZVPigvyj2Z/+g2e+cWy+qont+BTA3/y1EzLOtX+62NT69YULbwaFydnqVTq
137	MJDaitLcVrQrsJnodmqfMTSrNpP8EP0wrRWZrXx8CLX693x2309tA1zY4apQMAJ/fKSbxqGQAs7T
138	2TDnXzq+lb7G1m+Lf19cbml66pnWnS3Lt1jx/QcO41QJefF9ySnSD5tXf/P119+uXOVfg2zgxoxC
139	0Ex3OKO01CPlLq5ZG9SMfmXcrM0PVaosVhSCrUJ8KHWw4PXf8zFFeRJ7qJaN9jB3WGMYuYwu48vM
140	ZcvlEI7q1OFnK3VIRFfI/CrY7P5vnt9b9yvbjsTvz92UvsIBX/4nZq7w29Y3Pi3Cvvzq9cZVBzuA
141	5X48XLp66MQbp1+XESNlsDeAWxtKRCXu1ESIjCYx1E7iUH1Y3A6Tcq9C28xG7ggG1LDPhu0Zphqm
142	CE+0hwpOlBZjVaQHxA/zJSUyakCK7u4u6nb+8rXsjAIBMjJqVChJTGpM6khiQQqDvPH35yAjxsjq
143	p56Wqh98+9C8LI1N7b9ZdnZ+vnHtqud3jnixofNvt99qeHEELpVat2/esm3bls3byan+R776W0zM
144	Z6X5v+tsLlqA0/v68IgFRfvLpc1n3v3800++fOcsSDoNxM3nbkBUsKCp7kCiMtab94hgCojwukSt
145	0yQkGlIg4nW5+rsoSmBD3w8rk3K4ORDLBmuh1hwg22oAnD5bNQ15lWGSswZqpm9PSE6aMD45ecL/
146	eXXgu44OXMotSZo4MSl5/PifYj0eMrscxhgN/MzmzTQXdhv5euUSFtUzOBE5FSSRS1H7GPGzAUxo
147	hjChlplQw+ljIvrOxHjfqwM3Dx3CZR6Ph3PL0RbkZntghcNQtTtJoTNbWYID16hJPbcnxKgnuF69
148	WUSGMabQRF5INDl1o9hEK+9EiUxKOF1aFwSSLrFLjsKZPT2Brn45ykBQOZZsa7R12MhdvsJlvsLh
149	9PE1GK19u3ODj0vf6kJj7n5QTOoLFR3790lsW37d6rXtVDVvVFS++9HABY+HQW9uO/maZL3j2Twg
150	Bc38E9wm1Kzlm6kxBRGrZaIKTOnuGyGKv5Qj9uAqmjQN3T0FDpoMbKCY0h07d+7YsbN1O7Xu4Js3
151	cbD0TdZ3XV03b3Z1fVcIdiJhl/QHSZIuweyjpWz2OMyuRZFonjsRI0MY0bE7rLp6ISK83q7eYd5s
152	zbc/KeyJsiUihRVQrE8ME5FTlxIlyrbh6pXzmEHzcPmtIyPlSGN0RzTwie/k4cCrc1BpRouZiZT3
153	r1R1eN/2zU3btjVt3n4cVpgaw+3bnWAMdMmZKWVn3/nyk08/f/do+f6iBdK7fX3SOwuKpJDych8G
154	yAfAfxB6xh2hVJk4jIR6A+ICNutU9YY9GrWSGYbERKPSqU3UpwT71h1Sr05fyidduAAMX5DfbrlH
155	QqDCIiMSkW5dLWKAGCgGJVvdyI3djJu4WTc30eIOcAe6gyx0+0iJ7djO8Hl3gRIsAyUYTv++cNDr
156	Gu4g2Qca8oGHmzl9/bYPBy5RtIw4UD+skI2Tbj0481QHIMND5pa9UVWupziHrI8cBhnj0DX3ODmn
157	GutPqcZq7qZUz6F2rtkZ8Jyl3Qr4uZtSDbOEjRWUTktWFDNMQJP+eUrV300Txlt/n1INZlR2OaOa
158	77Q57U6HM8IZmavO1eRqc3W5tlx7riM3Yn7kWtta+1rH2oi1kS22FnuLoyWiJXK/bb99v2N/xP7I
159	MHdCY8JB80HLwYCDgQeDDgafMZ+xnAk4E3gm6EywnmZBaan3ZkHU+fhfAdzNgqgvqvGwTRtXPrlg
160	15oNDR+9MfdEoYddv7R2ee66p3eu+ebios7Rt5cvy8vJyr5vWOIvS57enxj/7aLa2bMnPBQ/LLmp
161	aucriVSjo0GjTm4JWFypOyxQjURds5lVonqe2WPOD1KIBpyo4pwEJYPtZVLAvOfTEtQ7RUl+r4jp
162	eytY8CA5CQpCQYN5pIVTcEqLwqKMUcQok4Mbg5uD24LVeaZIWH3fa6ohkS4m7dPnn38d50r7h2dN
163	Gc9sUm7Z1vZLcqocT5OOlQ/krXtg3oJta5teojyng5+4zjoBWUvdEYEGXqszM2tUQWCoaI8qn0WJ
164	gcBxIh6lTxSd2mQr3WP0Asddvldy3WCYLvkVY8rgW1mrzLkVWQdfVTSGdIQwd5BslZFspWQ+JDuG
165	JDtyxuaza0Mk8yGe/6q0O/X58kMv7scLFtSDv2Od/RM8pzxV71xlMsoHnjm/9dRr+IZsGQi8nROS
166	hA73ItiSCG1mi1nfptNb4DJW0Ct82+WxsF0mDIPbeAWP2kKQAi5jMbIEWIKtTMjYgADLDItegVil
167	NYADRx9E9pgELVHWG9QhwRZ5W62APbXWyKqMgaGQxX7S6d9Xw7a6n/7cAfrdfbRvL01b/9gnv/jR
168	zqWqoXltqKybUDj9ee3nLFLrLShEH43i9ZPRVP3D6GFFjn6+pQSVKEr1pZY6fZ1lDdoE21CsYlRE
169	peMFLpiz8iFWbGWsJFgTrLXqLEJwcLDVEhIL26dEJpFEa6K1sTqnPkaIEWMMccFxVmdIBnM/k0Hu
170	J1PQVDxZnyVMDsnFOUwOyeFhQt3D+nlCdkB2cLY1O8SDPYyHLFKUakq1pbpF+mKhJGQFWolXMivJ
171	Sr5Ot1xfK9SKtYZa8wrLsoClwUutS0PWog2KzZrN2g26Dfp1wjrzWsva4LXWtSGP0FcIJnl/qvK9
172	QtD4LiosdzJzP2vGu5qkG/iBTZJl3TffbpQqmnC09MZT+HojswGnlpdLy6V0jwePlc7D7w58Gtw3
173	wt4+yNIaAQ+hmLhzcBuDBX1IKGNFbYKg16gZVZte0CvbFEpoKseqlJjBHM8oxgI0ZijDGMGKmAAL
174	+DudiidMvYbdY3w2jLHo1SqlAiKBUtCC+9OSMEDAlW5DRmCG/O62W0aA2POR7PcNxn+DBJ8bVNI3
175	LLBJBh+YGyjm4DK8ArMKwSLGcXF8vDpe49Q7YYnm4znMPG4WN4+fxc9RZKuzNaW4CDKzfL5IsQwt
176	xyuYx8njbC1Xy9epVmhXwHZwqbBUXGZYZl0Wsiw0FlTMpWO/juWLnD/eSSfxiSyppg7fPIATcEIb
177	bl4uBbvqq5ILXb/gMzLTJ7x5iPyhvHwgmrleXv7T3JWPiMLFiaPHUM/RMdBPZimehgwDwbiiyWhK
178	RYQx4Jo320/sb5f6cxsH+r8jO/GXTAomAz9Kawd6+r/3PYdrFBvo//1NELk63nxTseFWjTyiZIYR
179	N8gjWuiAkQwMmIZrGrdfbH9/a7tiw3f9v5YelsxSMZ6Ee5gY4vru7zlJEwmDU40mo8HCNDXmSv3t
180	+0+0U0ZMjBHXMXppYOB9Kby/7DuEmSb5uQ30qwMIqIYUMktmRf6+YygvqRYYlETSQZmmN9u3vt9+
181	cXsjZebSwHXJKJ3Ev8Ld+CXyCP2PLv0igsnZZb09u3WBkPlXZFPKHzz88XH9F4PXv308MEr8WPk5
182	Qkh55/sIeE6xWApDkCn97eP+avHjf/i2Ip6l/wWnwx+Asgnod6MlxIaeh7KNOYJyoe8cF4jWQemD
183	sgnKHij3Q3kVygYoL/uvT3Bve3u5q2gJ1wRlFlrCN6MargHuZyMz+xYqYRugnEIlnA2VMM1oGpTR
184	nBNNY/8o940mH0A9BNWQdLk/nX0KBbNrvH2gyg7fyTTJX6jcPRrRy+gq6oaIuwAfZtRMJfMlqSDX
185	2Xh2KzvA1XO/53X8GH6LokBxQpmmXKn8QDVFtVXVqXaqS9QXNCM1X2hHa/fq9uvn62v1T+if1b+u
186	f1t/Q9ZSMqNCCaiV/i8diWgX/VqE1eAfoc3K347k0q9mWPrdyGn5exNap8H1tL9O/wv/kb9OhvSz
187	Q+oc1P/ir/Owm7mFJqAqVI3q0GOoDC1CpagW2VEsKoR8yo5cKAXOVKgtBAo7Gg80tagGymOoGBWg
188	xbB7tKOpqBLok6A2DlXAaUez74xVI7eK4VoMzyyD3yKgVKOJUPPACNloKVAUAm0BjLJIprRDnY5v
189	h1Eq4Zd+9bMQxi0DOjs8XwXzFsj3/n6cOfIsZYCv8UBVhcqhn/bUQF+VPJYLZk9Fafc8d/cpNPhd
190	m/dx+ZusfzySZYzT7+WU8ndt9Iu2e7+tgy0+RL4o0GEcULvQCJQOs2WhKZCN0++UHgJ9zEHzYOaH
191	0Xz0CHoUvDbBLOYwjxWKpZVlrtSM8f7rBP91ov86yX/N8l3HpRxnVrs/f1siF0zkrc4o7q0i8pab
192	7Ywib+rI+XNO7nwROeckZ/PImVXklIac1JATr5u5Ey7yupkcd5HfSeSYRI5K5DWJHJbIoY7J3KE+
193	0jGZHJTIq6vIKxJ5WU9+e0DL/dZMDmjJSy7ymyLyYjjZ5yIvPF/EvSCR54vIcy167rlo0r5CzbVH
194	k7bpZK9Ink0ie9aHc3sk8qvdIverMLJbJLta9dyuaNIKdK160upmd8KDO81k52q2RU9a3Owz0WTH
195	L1O4HRLZ/rSJ2x5Nnt6m4542kaePY7dbxW7bqua26ci24xi5p7Jb1WTrWba5ahXXfJJseULDbTGQ
196	LW62CWpNo8jmTSe5zRLZtDGP23SSbFrNbtwQzW3MIxvd7Abga0M0Wb/OwK0PJ+uPe8+6vew6A1kD
197	U68pIr9MIU8FkCdbyBMasrqoiFstkcYKkWsMJo+v0nOPu8gqPVnZIHArTaRBIPUtpM5AVqjJ8mV2
198	bnkfWbY0lFtmJ0tDSS08VBtOaiTymESWVOu4JRKp1pFqN1u1ilQuHstVlpPFY0lFuZarEEnFarZc
199	S8rdrAem9PSRstKTXJlEShflcaUnSelqdlFJNLcojyxysyXRpBiIivtIUREptJCFEimQSP6CJC5f
200	IguSyC8kkieRR6eTR1aRXInkTCTzJfKwRLJPknkSmVNEZpvJQy4y60GBm7WKPCiQmePc48kDGjKt
201	iEyNUHJTW8gUF5lMRG6yiWQZySRGzU0KJhMnmLiJ5WTCeJGbYCLjx2m48SIZ51Zx4zTErSJuqsc5
202	7P0tZCw7jBs7g4zJNHNjppPM0Wou00wy3exoNRmVYeRG5ZGMkQYuw0hGGki6joyQSNpwM5cmkeGp
203	Jm64maS61FyqibjuU3EuNXH51uc+FUlJDuJSJpLkJAuXHESSz7JJ4WouyUKSVrPDVEXcsBaSmGDm
204	EqeTBBAiwUwS3Gw8sB5fROJiU7i4cSQWGItNIU64OCUSM4pE64K46DwSFWnkouaQSHgs0kgi3WyE
205	kjjsQZwjj9htBs4eROxnWRtMZjMQ22o2XE3C3WxYJAkVSEgUsQancNY5JBhGDU4hQRIJhEkDJRIg
206	EovZzFnKidlk4sxmYnazJhMxAp3xJDGAeg0Sgb00J44nAvAvtBA93NNLRAcD6IKIzs1qJaKBhsY9
207	spyogUa9iqiKiFJh4JRmojAQnnNx/CrCwXOci7AwGDuMwKCMmuA5BEkEH8dFa5pwwv+3B/p/zcC/
208	PSCL+R+uDPkVCmVuZHN0cmVhbQplbmRvYmoKMjAgMCBvYmoKPDwgL0xlbmd0aCA5OCAvRmlsdGVy
209	IC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJyljtkKg1AMRA/U3Wrdt2pdatX//8KGy0VE8MnAmcnM
210	QwjcnMe+GUpNLJ1tHFEXD58nASEvImKS04VUe0Z+aAulpU4V9eUHjfAWWqETPqrthYGRSfzLzI9F
211	9SvbH73HAzIKZW5kc3RyZWFtCmVuZG9iagoyMyAwIG9iago8PCAvTGVuZ3RoIDM4OSAvRmlsdGVy
212	IC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJxdU8tugzAQvPMVPqaHiBDANBKKVKWXHPpQaU9RDsRe
213	R0jFIIcc+Ptiz0KkIsFoZnbNYNbx4fh6tM0g4k/XqYoGYRqrHd26u1MkLnRtbJRshW7UwCw8VVv3
214	UTw1V+NtoPZoTReVpYi/JvM2uFGsXnR3oadICBF/OE2usVex+jlUkKp73/9SS3YQm2i/F5rMtNxb
215	3b/XLYk4NK+PevKbYVxPbY+K77EnsQ08QSTVabr1tSJX2ytF5Wa69qI007WPyOp/frJD28Us9Vtf
216	DzgBz0HOIecs5yw/Q96xvFC4GpTYXWhwU7wp5d6ZJoAtIAVkAIRIJaAAPM/LhFUz9Hs4ASGjNZMs
217	LxSuAlXsKpYNZMOygZwjVJ5BftDgSgSQHEByAIkqDycgZASRvK+S91Xi2zycgJB3kHnLJH+zRHzJ
218	8SXHlxTkgn8lU2lmNRQV2OiCA8wUaYtsNlGLrS749Q969rM1D5EfM38mlhlWd+em8Q0HJ8ytn9jG
219	0nK2+q73Xf7+A6SH5zsKZW5kc3RyZWFtCmVuZG9iagoxOCAwIG9iago8PCAvVHlwZSAvRm9udCAv
220	U3VidHlwZSAvQ0lERm9udFR5cGUyIC9CYXNlRm9udCAvQlhHRVZMK0RlamFWdVNlcmlmCi9DSURT
221	eXN0ZW1JbmZvIDw8IC9SZWdpc3RyeSAoQWRvYmUpIC9PcmRlcmluZyAoSWRlbnRpdHkpIC9TdXBw
222	bGVtZW50IDAgPj4KL0ZvbnREZXNjcmlwdG9yIDE3IDAgUiAvVyAyMiAwIFIgL0NJRFRvR0lETWFw
223	IDIwIDAgUiA+PgplbmRvYmoKMTkgMCBvYmoKPDwgL1R5cGUgL0ZvbnQgL1N1YnR5cGUgL1R5cGUw
224	IC9CYXNlRm9udCAvQlhHRVZMK0RlamFWdVNlcmlmCi9FbmNvZGluZyAvSWRlbnRpdHktSCAvRGVz
225	Y2VuZGFudEZvbnRzIFsgMTggMCBSIF0gL1RvVW5pY29kZSAyMyAwIFIgPj4KZW5kb2JqCjE3IDAg
226	b2JqCjw8IC9UeXBlIC9Gb250RGVzY3JpcHRvciAvRm9udE5hbWUgL0JYR0VWTCtEZWphVnVTZXJp
227	ZiAvRmxhZ3MgMzIKL0ZvbnRCQm94IFsgLTc3MCAtMzQ3IDIxMDYgMTExMCBdIC9Bc2NlbnQgOTI5
228	IC9EZXNjZW50IC0yMzYgL0NhcEhlaWdodCAwCi9YSGVpZ2h0IDAgL0l0YWxpY0FuZ2xlIDAgL1N0
229	ZW1WIDAgL0ZvbnRGaWxlMiAyMSAwIFIgL01heFdpZHRoIDk1MCA+PgplbmRvYmoKMjIgMCBvYmoK
230	WyAzMiBbIDMxOCBdIDM3IFsgOTUwIF0gNDAgWyAzOTAgMzkwIF0gNDUgWyAzMzggMzE4IF0gNDgK
231	WyA2MzYgNjM2IDYzNiA2MzYgNjM2IDYzNiA2MzYgNjM2IDYzNiA2MzYgXSA2NSBbIDcyMiBdIDY5
232	IFsgNzMwIDY5NCBdIDc2ClsgNjY0IF0gNzkgWyA4MjAgXSA4MyBbIDY4NSA2NjcgXSA5NyBbIDU5
233	NiBdIDk5IFsgNTYwIF0gMTAxIFsgNTkyIF0gMTAzClsgNjQwIF0gMTA1IFsgMzIwIF0gMTA4IFsg
234	MzIwIF0gMTEwIFsgNjQ0IDYwMiA2NDAgXSAxMTQgWyA0NzggNTEzIDQwMiA2NDQgXQoxMjAgWyA1
235	NjQgNTY1IF0gXQplbmRvYmoKMyAwIG9iago8PCAvRjEgMTkgMCBSID4+CmVuZG9iago0IDAgb2Jq
236	Cjw8IC9BMSA8PCAvVHlwZSAvRXh0R1N0YXRlIC9DQSAwIC9jYSAxID4+Ci9BMiA8PCAvVHlwZSAv
237	RXh0R1N0YXRlIC9DQSAxIC9jYSAxID4+Ci9BMyA8PCAvVHlwZSAvRXh0R1N0YXRlIC9DQSAwLjIg
238	L2NhIDEgPj4gPj4KZW5kb2JqCjUgMCBvYmoKPDwgPj4KZW5kb2JqCjYgMCBvYmoKPDwgPj4KZW5k
239	b2JqCjcgMCBvYmoKPDwgL00wIDEzIDAgUiAvTTEgMTQgMCBSIC9NMiAxNSAwIFIgL00zIDE2IDAg
240	UiA+PgplbmRvYmoKMTMgMCBvYmoKPDwgL1R5cGUgL1hPYmplY3QgL1N1YnR5cGUgL0Zvcm0gL0JC
241	b3ggWyAtNyAtNyA3IDcgXSAvTGVuZ3RoIDEzMQovRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJl
242	YW0KeJxtkD0OgDAIhXdOwQVeA1j/Vkev4WJMvP8qjbZpUxdC4fXjgfJFwjt5gPFNEsZBokzppUGG
243	VT3VMC+rTbNXokbTmEpfdlDpIn8wRuEYi2s85kIFe9UF1TBz7xM3PHNFPQGdHH9QdKNR+cLrFLV5
244	9Lvh9wbob4WWjGT6JNroAUAcRRgKZW5kc3RyZWFtCmVuZG9iagoxNCAwIG9iago8PCAvVHlwZSAv
245	WE9iamVjdCAvU3VidHlwZSAvRm9ybSAvQkJveCBbIC03IC03IDcgNyBdIC9MZW5ndGggMzYKL0Zp
246	bHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCnicM1DI4jJQ8OLSNVIAolwuMJUDpECkLoTK4OJy
247	4gIAm6IHTgplbmRzdHJlYW0KZW5kb2JqCjE1IDAgb2JqCjw8IC9UeXBlIC9YT2JqZWN0IC9TdWJ0
248	eXBlIC9Gb3JtIC9CQm94IFsgLTcgLTcgNyA3IF0gL0xlbmd0aCAxMzEKL0ZpbHRlciAvRmxhdGVE
249	ZWNvZGUgPj4Kc3RyZWFtCnicbZA9DoAwCIV3TsEFXgNY/1ZHr+FiTLz/Ko22aVMXQuH144HyRcI7
250	eYDxTRLGQaJM6aVBhlU91TAvq02zV6JG05hKX3ZQ6SJ/MEbhGItrPOZCBXvVBdUwc+8TNzxzRT0B
251	nRx/UHSjUfnC6xS1efS74fcG6G+Floxk+iTa6AFAHEUYCmVuZHN0cmVhbQplbmRvYmoKMTYgMCBv
252	YmoKPDwgL1R5cGUgL1hPYmplY3QgL1N1YnR5cGUgL0Zvcm0gL0JCb3ggWyAtNyAtNyA3IDcgXSAv
253	TGVuZ3RoIDM2Ci9GaWx0ZXIgL0ZsYXRlRGVjb2RlID4+CnN0cmVhbQp4nDNQyOIyUPDi0jVSAKJc
254	LjCVA6RApC6EyuDicuICAJuiB04KZW5kc3RyZWFtCmVuZG9iagoyIDAgb2JqCjw8IC9UeXBlIC9Q
255	YWdlcyAvS2lkcyBbIDExIDAgUiBdIC9Db3VudCAxID4+CmVuZG9iagoyNCAwIG9iago8PCAvQ3Jl
256	YXRvciAoTWF0cGxvdGxpYiB2My4xMC41LCBodHRwczovL21hdHBsb3RsaWIub3JnKQovUHJvZHVj
257	ZXIgKE1hdHBsb3RsaWIgcGRmIGJhY2tlbmQgdjMuMTAuNSkKL0NyZWF0aW9uRGF0ZSAoRDoyMDI2
258	MDUyNTAzMDYxNyswOCcwMCcpID4+CmVuZG9iagp4cmVmCjAgMjUKMDAwMDAwMDAwMCA2NTUzNSBm
259	IAowMDAwMDAwMDE2IDAwMDAwIG4gCjAwMDAwMTQ0MDIgMDAwMDAgbiAKMDAwMDAxMzI5OSAwMDAw
260	MCBuIAowMDAwMDEzMzMxIDAwMDAwIG4gCjAwMDAwMTM0NzEgMDAwMDAgbiAKMDAwMDAxMzQ5MiAw
261	MDAwMCBuIAowMDAwMDEzNTEzIDAwMDAwIG4gCjAwMDAwMDAwNjUgMDAwMDAgbiAKMDAwMDAwMDM1
262	MiAwMDAwMCBuIAowMDAwMDAyOTk0IDAwMDAwIG4gCjAwMDAwMDAyMDggMDAwMDAgbiAKMDAwMDAw
263	Mjk3MyAwMDAwMCBuIAowMDAwMDEzNTc4IDAwMDAwIG4gCjAwMDAwMTM4MzIgMDAwMDAgbiAKMDAw
264	MDAxMzk5MCAwMDAwMCBuIAowMDAwMDE0MjQ0IDAwMDAwIG4gCjAwMDAwMTI3NjMgMDAwMDAgbiAK
265	MDAwMDAxMjQwMSAwMDAwMCBuIAowMDAwMDEyNjE1IDAwMDAwIG4gCjAwMDAwMTE3NjkgMDAwMDAg
266	biAKMDAwMDAwMzAxNCAwMDAwMCBuIAowMDAwMDEyOTg3IDAwMDAwIG4gCjAwMDAwMTE5MzkgMDAw
267	MDAgbiAKMDAwMDAxNDQ2MiAwMDAwMCBuIAp0cmFpbGVyCjw8IC9TaXplIDI1IC9Sb290IDEgMCBS
268	IC9JbmZvIDI0IDAgUiA+PgpzdGFydHhyZWYKMTQ2MjEKJSVFT0YK
269	EOF_training_dynamics_pdf
270	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5fd0242-ba0c-4187-a044-c48dbe164b6e",
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "47d8e2fb-d22c-40e7-9f86-12fe11b7c1c1",
  "sourceToolAssistantUUID": "b5fd0242-ba0c-4187-a044-c48dbe164b6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T09:13:02.559Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JZZYACZNvmhzy9XFKad3yQ`</summary>

```json
{
  "file_path": "/tmp/paper_transfer/cmd_fig6.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d8e2fb-d22c-40e7-9f86-12fe11b7c1c1",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2hawj8ekSzooxgmwot",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9ca8ef4-b1fb-47cf-9dc8-d0f73a845ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iUXNQY8qGSWcQynozVf6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7312,
      "cache_read_input_tokens": 6748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7312,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T09:13:02.852Z_

<details><summary>↩ Tool result · `toolu_01JZZYACZNvmhzy9XFKad3yQ`</summary>

```text
1	base64 -d > /root/trace-verdict-study/figures/paper/error_overlap.pdf << 'EOF_error_overlap_pdf'
2	JVBERi0xLjQKJazcIKu6CjEgMCBvYmoKPDwgL1R5cGUgL0NhdGFsb2cgL1BhZ2VzIDIgMCBSID4+
3	CmVuZG9iago4IDAgb2JqCjw8IC9Gb250IDMgMCBSIC9YT2JqZWN0IDcgMCBSIC9FeHRHU3RhdGUg
4	NCAwIFIgL1BhdHRlcm4gNSAwIFIKL1NoYWRpbmcgNiAwIFIgL1Byb2NTZXQgWyAvUERGIC9UZXh0
5	IC9JbWFnZUIgL0ltYWdlQyAvSW1hZ2VJIF0gPj4KZW5kb2JqCjExIDAgb2JqCjw8IC9UeXBlIC9Q
6	YWdlIC9QYXJlbnQgMiAwIFIgL1Jlc291cmNlcyA4IDAgUgovTWVkaWFCb3ggWyAwIDAgMzI1LjQ1
7	MTQwMDUwNDggMjgwLjMwNjM1OTA4MjIgXSAvQ29udGVudHMgOSAwIFIKL0Fubm90cyAxMCAwIFIg
8	Pj4KZW5kb2JqCjkgMCBvYmoKPDwgL0xlbmd0aCAxMiAwIFIgL0ZpbHRlciAvRmxhdGVEZWNvZGUg
9	Pj4Kc3RyZWFtCnicrVhNbxs3EL3zV/BoH0Jxhl/DY9KkRnIpUhvtoSgCQ5ZdB7JdO2nT/vs+SrJ3
10	udpVKFU2BHtHu28fZ94MhzN7u/j7dr74+eyN/uFczbqr+RdF+jM+N9rqz/h806TP8LlRFld3ynEw
11	PpC3hMtl/5LFGmejCxl2W1/+odS1mr0GzBc8dqZUiCYHHaxJycaUAczRmszR2b552Tdz8Cb5mMXD
12	vgaoTKuXPOoaWsSV+6wzORUU9pyGl08L/au+17PXXPhh/fh8wxLOdO2ZRzzodfFD+Tv2nvmdnr0n
13	/fZBf1Qf9eMzpIU7C6w1AocWYFhUAgkvlms/dFafDD+7Qb1RhdOjwp02UXkhsa4uXk1/5b0RSzmm
14	lHNWRIYl5Ug2SQJl9eZCzX4knfXF9SrKF1fqN32yONWUjIu0+dEn/2xZ5p8e7pf/nurf9cUH9e5C
15	fVSrJSpAYxXeplitrWc+3uKETM5kfUqOvSJv4L2cLbkUphd3uZhi7gEHOUMWFfPOfDzmxM5ExzHj
16	Ooni8oosNgRyMk39l60o/HRxqlM0TjY/WZ+8HllZCibjsST1yjrzEVcGxSFHUiQOHJTgOyQyZZpe
17	1vLh4c+JmLDNoMjMua4YnfmIzFM21iYXQsoSVTbBZvIhCLtp7td/LZefvj5dzhcj5D0SmoVrr3fW
18	41FnaF8ywFK0zpU0DykwO7YSp7nfP0wx35RYl1BiJYdCOzhU+76px7lsCK8s6hzh8RC53OeNAx9x
19	0Ycd7vs/lWZDEgUda81WOpKdaZRkMC6RpHIjNipHFkwTHVIy1hQoZrwvSkgvFHqmMQpcEs+XMkUR
20	2euQ+yQ57SjJh6b+hqELBtIQGzuGnWmMIaSJWxjcJMND7PJB+bt5vSW8y6cQutd3prHXi3HeFiHl
21	8h8L9rBg+bA0XHOIEG6UhN37mUJnGVUJGdR83IVdBWphZFf0++US6w/rVmq199cNxXYXNNLWqPPx
22	3uhusjfCE8391cu9PYSdyBbroU0/Q732sOe1yNiDkfYJ+0pGFQgm+CBuWAWkdh5cbW0VuFUTuu6V
23	eug5At1hixS0E83odojej7KzCG9G8kXx/jiQK8WgvbRl6zgOJLIAImRsR+44iNgajI8JqYVAy1Eg
24	B6FHfgefkwxL6/cQ1wLbEtYg9I3orcIayqCZPALSKIM9/BHbZLAHYmiUwR6QU+uuZUAosiG45Ibb
25	2x7CqkPfjjiIzYSwBqFvhW9WVi2DPfzhpoJWy2APRJY2GewD2VYNyDkgYrcddhKHy2APxMl8GoS+
26	HbKOzZSyBqFvhN9S1nTomwnH0KLVoQya4X1uk0HGmSoSeotBM3ewCvYAnMymWgTtiHU2tWmgGX0Q
27	sEkJNALu0tQg6u0UuUVTtQAi2oxYzteDZvpgAewBOLlR1wJoR5ysfYOgNyMO0mhKUpUAmsHjJN2B
28	ABoRWzdACQbn8ZRSZHKa4/ORwgr35YUTbQdf8N89rU681of1b9AnsDCVyTIOy+VXnzw86fPFV/3h
29	cj6/HN6vTq70+e3d7fLy6fZrOZqqZ6abaXR/0m03flac4AxOQQZHKGF4MJZhdzWi7szVYamHsj2n
30	rofNemzYTNYgtutxs8MpVa8AdSBDq7n6xnl69p7XE+fetPl50nwzTrqsJRraXsvIlELy+nkbrBft
31	cVhMTqzbzLtfQme3UmNkFtZxyVQEln1N5cXawETKyT3b6EVkJxHeSWQ134iErrem0rM3kCEWMEcu
32	BpS4uJOO300nOUNAijyg09lb6MRsoJAgkFygnXTiTjpIV5MDJXY1nZ69gQ5DyhS8eOjG7faO7KZT
33	DSl6dKohxXfpQPE5WLJ5WH/sVnmry2UBe1VgHUXjUi/8yMyEVCcf7Y7Zfa9G9ad4V/r9/dXoFLRt
34	jjRZsBJ6eI45u6mC1VbHXlCa6tsomVXZO8c6/gPL7cwbCmVuZHN0cmVhbQplbmRvYmoKMTIgMCBv
35	YmoKMTQ0OAplbmRvYmoKMTAgMCBvYmoKWyBdCmVuZG9iagoxOSAwIG9iago8PCAvTGVuZ3RoIDkx
36	IC9GaWx0ZXIgL0ZsYXRlRGVjb2RlID4+CnN0cmVhbQp4nDWMuw3AMAhEe6a4Efg4gPeJohT2/m2I
37	LRfcPemJ82xgZJ2HI7TjFrKmcFNMUk6odwxqpTcdO+glzf00yXouGvQPcfUVtpsDklEkkYdEl8uV
38	Z+VffD4MbxxiCmVuZHN0cmVhbQplbmRvYmoKMjAgMCBvYmoKPDwgL0xlbmd0aCA4MSAvRmlsdGVy
39	IC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJxNzbsNwCAMBNCeKTwC4P8+UZQi2b+NDRGhsZ90J51g
40	hwpucVgMtDscrfjUU5h96B4SklBz3URYMyXahKRf+ssww5hYyLavN1eucr4W3ByLCmVuZHN0cmVh
41	bQplbmRvYmoKMjEgMCBvYmoKPDwgL0xlbmd0aCA1MSAvRmlsdGVyIC9GbGF0ZURlY29kZSA+Pgpz
42	dHJlYW0KeJwzsjRVMFCwtAAShpbmCuZGlgophlxAPoiVywUTywGzDIA0WGkOTEUOVwZXGgC/jA1W
43	CmVuZHN0cmVhbQplbmRvYmoKMjIgMCBvYmoKPDwgL0xlbmd0aCAxMTUgL0ZpbHRlciAvRmxhdGVE
44	ZWNvZGUgPj4Kc3RyZWFtCnicPY5LEgMhCAX3nOJdwCrBIHKeSaWyMPffDuiYFc2nAXFFRVFGYXew
45	G0wcbyYfi350anNRTG4orYNHuKm9IufmuIi5BZqj172yrIJn739mPsg9UepBkU2aSm2wGLI0R+xR
46	RfwU/QyhX+fFSV/63OYPJeEKZW5kc3RyZWFtCmVuZG9iagoyMyAwIG9iago8PCAvTGVuZ3RoIDIx
47	NSAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJw1UEuuAzEI2+cUvkClQBII55mqepve
48	f/swqIsR1uAf8euYOIaXLPgS+Fa8ZazYMFN8x1ItpHZg60B14VzFM+QKjl6ITey04Fy2uUmkriBD
49	Ikoj23JDl1C0KTolf2+aW7optydNmm7TysDUy5CzI4gYSgZLUNO1aMKi7an4nfKMvzqLF37HDit0
50	3OHTUxH1PcNnPohLvcb2qNmZRLovyJDTmksJTTTZ0e/IFM48N6SQziBBUlyCa2WQ/emXowMSMDG3
51	LEB2V6KcJWnH0r8zeNLnH2FcVI0KZW5kc3RyZWFtCmVuZG9iagoyNCAwIG9iago8PCAvTGVuZ3Ro
52	IDM0MSAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJw1UjvSm0EI679T6AKeWd7LeZzJ
53	pPhz/zYCOxUssEIC0gIHmXiJIapRrvglTzBeJ/B3vTyNn8e7kFrwVKQfuDZt4/1YsyYKlkYshdnH
54	vh8l5Hhq/BsCPRdpwoxMRg4kA3G/1ufPepMph9+ANG1OHyVJD6IFu1vDji8LMkh6UsOSnfywrgVW
55	F6EJc2NNJCOnVqbm+dgzXMYTYySomgUk6RP3qYIRacZj56wlDzIcT/Xixa+38VrmMfWyqkDGNsEc
56	bCcz4RRFBOIXlCQ3cRdNHcXRzFhzu9BQUuS+u4eTk173l5OowCshnMVawjFDT1nmZKdBCVStnAAz
57	rNe+ME7TRgl3arq9K/b188wkjNscdlZKpsE5Du5lkzmCZK87JmzC4xDz3j2CkZg3v4stgiuXOddk
58	+rEfRRvpg+L6nKspsxUl/EOVPLHiGv+f3/v58/z+B4wofiMKZW5kc3RyZWFtCmVuZG9iagoyNSAw
59	IG9iago8PCAvTGVuZ3RoIDY2IC9GaWx0ZXIgL0ZsYXRlRGVjb2RlID4+CnN0cmVhbQp4nDMzNFQw
60	UNA1AhJmhiYK5kaWCimGXEA+iJXLBRPLAbPMTMyALGNTUySWAZA2MjWD0xAZoAFwBkR/BlcaAFJr
61	FMAKZW5kc3RyZWFtCmVuZG9iagoyNiAwIG9iago8PCAvTGVuZ3RoIDcyIC9GaWx0ZXIgL0ZsYXRl
62	RGVjb2RlID4+CnN0cmVhbQp4nDOzMFEwULAAYjNzMwVzI0uFFEMuIwszoEAulwVYIIfL0NAQyjI2
63	MVIwNDQFskzNjaFiMI1AWUuQQTlQ/TlcGVxpAHQyEqEKZW5kc3RyZWFtCmVuZG9iagoyNyAwIG9i
64	ago8PCAvTGVuZ3RoIDMwNyAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJw9kktuAzEM
65	Q/c+hS4QwPrZnvOkKLqY3n/bJyXpihzZFkVqlrpMWVMekDSThH/p8HCxnfI7bM9mZuBaopeJ5ZTn
66	0BVi7qJ82cxGXVknxeqEZjq36FE5Fwc2Taqfqyyl3S54Dtcmnlv2ET+80KAe1DUuCTd0V6NlKTRj
67	qvt/0nv8jDLgakxdbFKrex88XkRV6OgHR4kiY5cX5+NBCelKwmhaiJV3RQNB7vK0ynsJ7tveasiy
68	B6mYzjspZrDrdFIubheHIR7I8qjw5aPYa0LP+LArJfRI2IYzcifuaMbm1MjikP7ejQRLj65oIfPg
69	r27WLmC8UzpFYmROcqxpi1VO91AU07nDvQwQ9WxFQylzkdXqX8POC2uWbBZ4SvoFHqPdJksOVtnb
70	qE7vrTzZ0PcfWtd0HwplbmRzdHJlYW0KZW5kb2JqCjI4IDAgb2JqCjw8IC9MZW5ndGggMjMyIC9G
71	aWx0ZXIgL0ZsYXRlRGVjb2RlID4+CnN0cmVhbQp4nDVRSW7EMAy7+xX8wADW7rwnxaCH9v/XUsoU
72	CEAltrglYmMjAi8x+DmI3PiSNaMmfmdyV/wsT4VHwq3gSRSBl+FedoLLG8ZlPw4zH7yXVs6kxpMM
73	yEU2PTwRMtglEDowuwZ12Gbaib4h4bMjUs1GltPXEvTSKgTKU7bf6YISbav6c/usC2372hNOdnvq
74	SeUTiOeWrMBl4xWTxVgGPVG5SzF9kOpsoSehvCifg2w+aohElyhn4InBwSjQDuy57WfiVSFoXd2n
75	bWOoRkrH078NTU2SCPlECWe2NO4W/n/Pvb7X+w9OIVQRCmVuZHN0cmVhbQplbmRvYmoKMjkgMCBv
76	YmoKPDwgL0xlbmd0aCAyMzEgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCnicNU85kgQh
77	DMt5hT4wVRjbQL+np7Y22Pl/upKZTpDwIcnTEx2ZeJkjI7Bmx9taZCBm4FNMxb/2tA8TqvfgHiKU
78	iwthhpFw1qzjbp6OF/92lc9YB+82+IpZXhDYwkzWVxZnLtsFY2mcxDnJboxdE7GNda2nU1hHMKEM
79	hHS2w5Qgc1Sk9MmOMuboOJEnnovv9tssdjl+DusLNo0hFef4KnqCNoOi7HnvAhpyQf9d3fgeRbvo
80	JSAbCRbWUWLunOWEX712dB61KBJzQppBLhMhzekqphCaUKyzo6BSUXCpPqforJ9/5V9cLQplbmRz
81	dHJlYW0KZW5kb2JqCjMwIDAgb2JqCjw8IC9MZW5ndGggMjQ5IC9GaWx0ZXIgL0ZsYXRlRGVjb2Rl
82	ID4+CnN0cmVhbQp4nD1QO45EIQzrOYUv8CTyI3AeRqstZu/frgOaKVBMfrYzJNARgUcMMZSv4yWt
83	oK6Bv4tC8W7i64PCIKtDUiDOeg+IdOymNpETOh2cMz9hN2OOwEUxBpzpdKY9ByY5+8IKhHMbZexW
84	SCeJqiKO6jOOKZ4qe594FiztyDZbJ5I95CDhUlKJyaWflMo/bcqUCjpm0QQsErngZBNNOMu7SVKM
85	GZQy6h6mdiJ9rDzIozroZE3OrCOZ2dNP25n4HHC3X9pkTpXHdB7M+Jy0zoM5Fbr344k2B02N2ujs
86	9xNpKi9Sux1anX51EpXdGOcYEpdnfxnfZP/5B/6HWiIKZW5kc3RyZWFtCmVuZG9iagozMSAwIG9i
87	ago8PCAvTGVuZ3RoIDM5NSAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJw9UktuxUAI
88	2+cUXKDS8JvPeVJV3bz7b2tDUqkqvIkxxjB9ypC55UtdEnGFybderls8pnwuW1qZeYi7i40lPrbc
89	l+4htl10LrE4HUfyCzKdKkSozarRofhCloUHkE7woQvCfTn+4y+AwdewDbjhPTJBsCTmKULGblEZ
90	mhJBEWHnkRWopFCfWcLfUe7r9zIFam+MpQtjHPQJtAVCbUjEAupAAETslFStkI5nJBO/Fd1nYhxg
91	59GyAa4ZVESWe+zHiKnOqIy8RMQ+T036KJZMLVbGblMZX/yUjNR8dAUqqTTylPLQVbPQC1iJeRL2
92	OfxI+OfWbCGGOm7W8onlHzPFMhLOYEs5YKGX40fg21l1Ea4dubjOdIEfldZwTLTrfsj1T/5021rN
93	dbxyCKJA5U1B8LsOrkaxxMQyPp2NKXqiLLAamrxGM8FhEBHW98PIAxr9crwQNKdrIrRYIpu1YkSN
94	imxzPb0E1kzvxTnWwxPCbO+d1qGyMzMqIYLauoZq60B2s77zcLafPzPoom0KZW5kc3RyZWFtCmVu
95	ZG9iagozMiAwIG9iago8PCAvTGVuZ3RoIDEzNiAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJl
96	YW0KeJxNj0EOAzEIA+95hZ9AIEB4z1ZVD9v/X0vYdtMLHsmAbFEGgSWHeIcb4dHbD99FNhVn45xf
97	UiliIZhPcJ8wUxyNKXfyY4+AcZRqLKdoeF5Lzk3DFy13Ey2lrZeTGW+47pf3R5VtkQ1Fzy0LQtds
98	kvkygQd8GJhHdeNppcfd9myv9vwAzmw0SQplbmRzdHJlYW0KZW5kb2JqCjMzIDAgb2JqCjw8IC9M
99	ZW5ndGggMjQ5IC9GaWx0ZXIgL0ZsYXRlRGVjb2RlID4+CnN0cmVhbQp4nE1RSYoDMAy75xX6QCFe
100	k7ynQ5lD5//Xyg6FOQQJr5KTlphYCw8xhB8sPfiRIXM3/Rt+otm7WXqSydn/mOciU1H4UqguYkJd
101	iBvPoRHwPaFrElmxvfE5LKOZc74HH4W4BDOhAWN9STK5qOaVIRNODHUcDlqkwrhrYsPiWtE8jdxu
102	+0ZmZSaEDY9kQtwYgIgg6wKyGCyUNjYTMlnOA+0NyQ1aYNepG1GLgiuU1gl0olbEqszgs+bWdjdD
103	LfLgqH3x+mhWl2CF0Uv1WHhfhT6YqZl27pJCeuFNOyLMHgqkMjstK7V7xOpugfo/y1Lw/cn3+B2v
104	D838XJwKZW5kc3RyZWFtCmVuZG9iagozNCAwIG9iago8PCAvTGVuZ3RoIDk0IC9GaWx0ZXIgL0Zs
105	YXRlRGVjb2RlID4+CnN0cmVhbQp4nEWNwRHAIAgE/1RBCQoK2k8mk4f2/40QMnxg5w7uhAULtnlG
106	HwWVJl4VWAdKY9xQj0C94XItydwFD3Anf9rQVJyW03dpkUlVKdykEnn/DmcmkKh50WOd9wtj+yM8
107	CmVuZHN0cmVhbQplbmRvYmoKMzUgMCBvYmoKPDwgL0xlbmd0aCA3MiAvRmlsdGVyIC9GbGF0ZURl
108	Y29kZSA+PgpzdHJlYW0KeJwzMrdQMFCwNAEShhYmCuZmBgophlxAvqmJuUIuF0gMxMoBswyAtCWc
109	gohngJggbRDFIBZEsZmJGUQdnAGRy+BKAwAl2xbJCmVuZHN0cmVhbQplbmRvYmoKMzYgMCBvYmoK
110	PDwgL0xlbmd0aCA0NyAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJwzMrdQMFCwNAES
111	hhYmCuZmBgophlyWEFYuF0wsB8wC0ZZwCiKewZUGALlnDScKZW5kc3RyZWFtCmVuZG9iagozNyAw
112	IG9iago8PCAvTGVuZ3RoIDI1OCAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJxFkUty
113	BCAIRPeegiOA/OQ8k0plMbn/Ng3OZDZ2l6j9hEojphIs5xR5MH3J8s1ktul3OVY7GwUURSiYyVXo
114	sQKrO1PEmWuJautjZeS40zsGxRvOXTmpZHGjjHVUdSpwTM+V9VHd+XZZlH1HDmUK2KxzHGzgym3D
115	GCdGm63uDveJIE8nU0fF7SDZ8AcnjX2VqytwnWz20UswDgT9QhOY5ItA6wyBxs1T9OQS7OPjdueB
116	YG95EUjZEMiRIRgdgnadXP/i1vm9/3GGO8+1Ga4c7+J3mNZ2x19ikhVzAYvcKajnay5a1xk63pMz
117	x+Sm+4bOuWCXu4NM7/k/1s/6/gMeKWb6CmVuZHN0cmVhbQplbmRvYmoKMzggMCBvYmoKPDwgL0xl
118	bmd0aCAxNjMgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCnicRZA7EgMhDEN7TqEj+CMD
119	Ps9mMik2929j2GxSwNNYIIO7E4LU2oKJ6IKHtiXdBe+tBGdj/Ok2bjUS5AR1gFak42iUUn25xWmV
120	dPFoNnMrC60THWYOepSjGaAQOhXe7aLkcqbuzvlDcPVf9b9i3TmbiYHJyh0IzepT3Pk2O6K6usn+
121	pMfcrNd+K+xVYWlZS8sJt527ZkAJ3FM52qs9Px8KOvYKZW5kc3RyZWFtCmVuZG9iagozOSAwIG9i
122	ago8PCAvTGVuZ3RoIDMyMiAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJw1UbttxTAM
123	7DUFFzAgfiXN4yBIkbd/mzvaqUjTvB9VXjKlXC51ySpZYfKlQ3WKpnyeZqb8DvWQ45ge2SG6U9aW
124	exgWlol5Sh2xmiz3cAs2vgCaEnML8fcI8CuAUcBEoG7x9w+6WRJAGhT8FOiaq5ZYYgINi4Wt2RXi
125	Vt0pWLir+HYkuQcJcjFZ6FMORYopt8B8GSzZkVqc63JZCv9ufQIaYYU47LOLROB5wANMJP5kgGzP
126	Plvs6upFNnaGOOnQgIuAm80kAUFTOKs+uGH7arvm55koJzg51q+iMb4NTuZLUt5XucfPoEHe+DM8
127	Z3eOUA6aUAj03QIgh93ARoQ+tc/ALgO2Sbt3Y0r5nGQpvgQ2CvaoUx3K8GLszFZv2PzH6MpmUWyQ
128	lfXR6Q7K3KATYh5vZKFbsrb7Nw+zff8BXxl7ZAplbmRzdHJlYW0KZW5kb2JqCjQwIDAgb2JqCjw8
129	IC9MZW5ndGggMjE4IC9GaWx0ZXIgL0ZsYXRlRGVjb2RlID4+CnN0cmVhbQp4nD1QuY0EMQzLXYUa
130	WMB67alnFotLpv/0SPn2ItEWRVIqNZmSKS91lCVZU946fJbEDnmG5W5kNiUqRS+TsCX30ArxfYnm
131	FPfd1ZazQzSXaDl+CzMqqhsd00s2mnAqE7qg3MMz+g1tdANWhx6xWyDQpGDXtiByxw8YDMGZE4si
132	DEpNBv+uco+fXosbPsPxQxSRkg7mNf9Y/fJzDa9TjyeRbm++4l6cqQ4DERySmrwjXVixLhIRaTVB
133	Tc/AWi2Au7de/hu0I7oMQPaJxHGaUo6hv2twpc8v5SdT2AplbmRzdHJlYW0KZW5kb2JqCjQxIDAg
134	b2JqCjw8IC9MZW5ndGggODMgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCnicRYy7DcAw
135	CER7pmAEfib2PlGUwt6/DRAlbrgn3T1cHQmZKW4zw0MGngwshl1xgfSWMAtcR1COneyjYdW+6gSN
136	9aZS8+8PlJ7srOKG6wECQhpmCmVuZHN0cmVhbQplbmRvYmoKNDIgMCBvYmoKPDwgL0xlbmd0aCAy
137	MzkgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCnicTVDJbQQxDPu7CjUwwOgcux4Hizyy
138	/X9DygmSl2hL4qHylFuWymX3IzlvybrlQ4dOlWnybtDNr7H+owwCdv9QVBCtJbFKzFzSbrE0SS/Z
139	wziNl2u1juepe4RZo3jw49jTKYHpPTLBZrO9OTCrPc4OkE64xq/q0zuVJAOJupDzQqUK6x7UJaKP
140	K9uYUp1OLeUYl5/oe3yOAD3F3o3c0cfLF4xGtS2o0WqVOA8wE1PRlXGrkYGUEwZDZ0dXNAulyMp6
141	QjXCjTmhmb3DcGADy7OEpKWtUrwPZQHoAl3aOuM0SoKOAMLfKIz1+gaq/F43CmVuZHN0cmVhbQpl
142	bmRvYmoKNDMgMCBvYmoKPDwgL0xlbmd0aCA1MSAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJl
143	YW0KeJwzNrRQMFAwNDAHkkaGQJaRiUKKIRdIAMTM5YIJ5oBZBkAaojgHriaHK4MrDQDhtA2YCmVu
144	ZHN0cmVhbQplbmRvYmoKNDQgMCBvYmoKPDwgL0xlbmd0aCAxNjAgL0ZpbHRlciAvRmxhdGVEZWNv
145	ZGUgPj4Kc3RyZWFtCnicRZA5EgMxCARzvYInSFyC96zLtcH6/6kH1kei6QI0HLoWTcp6FGg+6bFG
146	obrQa+gsSpJEwRaSHVCnY4g7KEhMSGOSSLYegyOaWLNdmJlUKrNS4bRpxcK/2VrVyESNcI38iekG
147	VPxP6lyU8E2Dr5Ix+hhUvDuDjEn4XkXcWjHt/kQwsRn2CW9FJgWEibGp2b7PYIbM9wrXOMfzDUyC
148	N+sKZW5kc3RyZWFtCmVuZG9iago0NSAwIG9iago8PCAvTGVuZ3RoIDMyMCAvRmlsdGVyIC9GbGF0
149	ZURlY29kZSA+PgpzdHJlYW0KeJw1UktuBTEI288puECl8E/O86qqi777b2sTvRVMMGDjKS9Z0ku+
150	1CXbpcPkWx/3JbFC3o/tmsxSxfcWsxTPLa9HzxG3LQoEURM9WJkvFSLUz/ToOqhwSp+BVwi3FBu8
151	g0kAg2r4Bx6lMyBQ50DGu2IyUgOCJNhzaXEIiXImiX+kvJ7fJ62kofQ9WZnL35NLpdAdTU7oAcXK
152	xUmgXUn5oJmYSkSSl+t9sUL0hsCSPD5HMcmA7DaJbaIFJucepSXMxBQ6sMcCvGaa1VXoYMIehymM
153	VwuzqB5s8lsTlaQdreMZ2TDeyzBTYqHhsAXU5mJlgu7l4zWvwojtUZNdw3Duls13CNFo/hsWyuBj
154	FZKAR6exEg1pOMCIwJ5eOMVe8xM5DsCIY52aLAxjaCaneo6JwNCes6VhxsceWvXzD1TpfIcKZW5k
155	c3RyZWFtCmVuZG9iago0NiAwIG9iago8PCAvTGVuZ3RoIDE4IC9GaWx0ZXIgL0ZsYXRlRGVjb2Rl
156	ID4+CnN0cmVhbQp4nDM2tFAwgMMUQ640AB3mA1IKZW5kc3RyZWFtCmVuZG9iago0NyAwIG9iago8
157	PCAvTGVuZ3RoIDEzMyAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeJxFj0sOBCEIRPec
158	oo7Axx/ncTLphXP/7YCdbhNjPYVUgbmCoT0uawOdFR8hGbbxt6mWjkVZPlR6UlYPyeCHrMbLIdyg
159	LPCCSSqGIVCLmBqRLWVut4DbNg2yspVTpY6wi6Mwj/a0bBUeX6JbInWSP4PEKi/c47odyKXWu96i
160	i75/pAExCQplbmRzdHJlYW0KZW5kb2JqCjQ4IDAgb2JqCjw8IC9MZW5ndGggMzQwIC9GaWx0ZXIg
161	L0ZsYXRlRGVjb2RlID4+CnN0cmVhbQp4nDVSOW4EMQzr/Qp9IIBu2+/ZIEiR/L8NqdkUA3F0UpQ7
162	WlR2y4eFVLXsdPm0ldoSN+R3ZYXECcmrEu1ShkiovFYh1e+ZMq+3NWcEyFKlwuSk5HHJgj/DpacL
163	x/m2sa/lyB2PHlgVI6FEwDLFxOgals7usGZbfpZpwI94hJwr1i3HWAVSG9047Yr3oXktsgaIvZmW
164	igodVokWfkHxoEeNffYYVFgg0e0cSXCMiVCRgHaB2kgMOXssdlEf9DMoMRPo2htF3EGBJZKYOcW6
165	dPTf+NCxoP7YjDe/OirpW1pZY9I+G+2Uxiwy6XpY9HTz1seDCzTvovzn1QwSNGWNksYHrdo5hqKZ
166	UVZ4t0OTDc0xxyHzDp7DGQlK+jwUv48lEx2UyN8ODaF/Xx6jjJw23gLmoj9tFQcO4rPDXrmBFUoX
167	a5L3AalM6IHp/6/xtb7X1x8d7YDGCmVuZHN0cmVhbQplbmRvYmoKNDkgMCBvYmoKPDwgL0xlbmd0
168	aCAyNTEgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCnicLVFJcgNBCLvPK/SEZqffY5cr
169	h+T/1wjKBwYNi0B0WuKgjJ8gLFe85ZGraMPfMzGC3wWHfivXbVjkQFQgSWNQNaF28Xr0HthxmAnM
170	k9awDGasD/yMKdzoxeExGWe312XUEOxdrz2ZQcmsXMQlExdM1WEjZw4/mTIutHM9NyDnRliXYZBu
171	VhozEo40hUghhaqbpM4EQRKMrkaNNnIU+6Uvj3SGVY2oMexzLW1fz004a9DsWKzy5JQeXXEuJxcv
172	rBz09TYDF1FprPJASMD9bg/1c7KT33hL584W0+N7zcnywlRgxZvXbkA21eLfvIjj+4yv5+f5/ANf
173	YFuICmVuZHN0cmVhbQplbmRvYmoKNTAgMCBvYmoKPDwgL0xlbmd0aCAxNzQgL0ZpbHRlciAvRmxh
174	dGVEZWNvZGUgPj4Kc3RyZWFtCnicTZBJDkMhDEP3nMIXqIQzwOc8v6q6aO+/rUMHdYH85CBwPDzQ
175	cSQudGTojI4rmxzjwLMgY+LROP/JuD7EMUHdoi1Yl3bH2cwSc8IyMQK2RsnZPKLAD8dcCBJklx++
176	wCAiXY/5VvNZk/TPtzvdj7q0Zl89osCJ7AjFsAFXgP26x4FLwvle0+SXKiVjE4fygeoiUjY7oRC1
177	VOxyqoqz3ZsrcBX0/NFD7u0FtSM83wplbmRzdHJlYW0KZW5kb2JqCjUxIDAgb2JqCjw8IC9MZW5n
178	dGggNTQgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCnicMzUwUDBQ0LVU0DUyNlUwNQSy
179	Dc1MFVIMueDsXAgTJJ/DBVMJYYGkcxAqc7gyuNIAc1EPjwplbmRzdHJlYW0KZW5kb2JqCjUyIDAg
180	b2JqCjw8IC9MZW5ndGggODkgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCnicNU25EYAw
181	DOs9hUfAj0i8D8dRhP1b7IQ0lk6fEcoHa+QBguGNLyH4oi8ZhLULDyr7SHTYRA1nFSQTw68s8Kqc
182	FW1zJRPZWUyjs0HL9K3tb4Meuj/djhwKCmVuZHN0cmVhbQplbmRvYmoKNTMgMCBvYmoKPDwgL0xl
183	bmd0aCAxNDEgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCnicPY/BDsMwCEPv+Qr/QKTY
184	KaF8T6dqh+7/ryNLuwt6AmOMhdDQG6qaw4Zgm+PF0iVUa/gUxUAlN8iZYA6lpNIdR5F6YjgYXB60
185	G47isej6EbuSZn3QxkK6JWiAe6xTadymcRPEHTUF6inqnKO8ELmfqWfYNJLdNLOSc7gNv3vPU9f/
186	p6u8y/kFvXcu/gplbmRzdHJlYW0KZW5kb2JqCjU0IDAgb2JqCjw8IC9MZW5ndGggMjE1IC9GaWx0
187	ZXIgL0ZsYXRlRGVjb2RlID4+CnN0cmVhbQp4nDVROQ4DIQzs9xX+QCSML3hPoijN/r/NjNFWHsFc
188	hrSUIZnyUpOoIeVTPnqZLpy63NfMajTnlrQtc4C4trwvrZLAiWaIg8FpmLgBmjwBQ9fRqFFDFx7Q
189	1KVTKLDcBD6Kt24P3WO1gZe2IeeJIGIoGSxBzalFExZtzyekNb9eixvel+3dyFOlxpYYgQYBVjgc
190	1+jX8JU9TybRdBUy1Ks1yxgJE0UiPPmOptUT61o00jIS1MYRrGoDvDv9ME4AABNxywJkn0qUs+TE
191	b7H0swZX+v4Bn0dUlgplbmRzdHJlYW0KZW5kb2JqCjE3IDAgb2JqCjw8IC9UeXBlIC9Gb250IC9C
192	YXNlRm9udCAvQk1RUURWK0RlamFWdVNhbnMgL0ZpcnN0Q2hhciAwIC9MYXN0Q2hhciAyNTUKL0Zv
193	bnREZXNjcmlwdG9yIDE2IDAgUiAvU3VidHlwZSAvVHlwZTMgL05hbWUgL0JNUVFEVitEZWphVnVT
194	YW5zCi9Gb250QkJveCBbIC0xMDIxIC00NjMgMTc5NCAxMjMzIF0gL0ZvbnRNYXRyaXggWyAwLjAw
195	MSAwIDAgMC4wMDEgMCAwIF0KL0NoYXJQcm9jcyAxOCAwIFIKL0VuY29kaW5nIDw8IC9UeXBlIC9F
196	bmNvZGluZwovRGlmZmVyZW5jZXMgWyAzMiAvc3BhY2UgNDYgL3BlcmlvZCA0OCAvemVybyAvb25l
197	IC90d28gL3RocmVlIC9mb3VyIC9maXZlIC9zaXggNTYKL2VpZ2h0IC9uaW5lIDY1IC9BIDY5IC9F
198	IDczIC9JIC9KIDc5IC9PIDgzIC9TIC9UIDg2IC9WIDk1IC91bmRlcnNjb3JlIDk3IC9hCjk5IC9j
199	IC9kIC9lIC9mIDEwNSAvaSAxMDggL2wgL20gL24gL28gL3AgMTE0IC9yIDExNiAvdCAvdSAxMjAg
200	L3ggL3kgXQo+PgovV2lkdGhzIDE1IDAgUiA+PgplbmRvYmoKMTYgMCBvYmoKPDwgL1R5cGUgL0Zv
201	bnREZXNjcmlwdG9yIC9Gb250TmFtZSAvQk1RUURWK0RlamFWdVNhbnMgL0ZsYWdzIDMyCi9Gb250
202	QkJveCBbIC0xMDIxIC00NjMgMTc5NCAxMjMzIF0gL0FzY2VudCA5MjkgL0Rlc2NlbnQgLTIzNiAv
203	Q2FwSGVpZ2h0IDAKL1hIZWlnaHQgMCAvSXRhbGljQW5nbGUgMCAvU3RlbVYgMCAvTWF4V2lkdGgg
204	MTM0MiA+PgplbmRvYmoKMTUgMCBvYmoKWyA2MDAgNjAwIDYwMCA2MDAgNjAwIDYwMCA2MDAgNjAw
205	IDYwMCA2MDAgNjAwIDYwMCA2MDAgNjAwIDYwMCA2MDAgNjAwIDYwMAo2MDAgNjAwIDYwMCA2MDAg
206	NjAwIDYwMCA2MDAgNjAwIDYwMCA2MDAgNjAwIDYwMCA2MDAgNjAwIDMxOCA0MDEgNDYwIDgzOCA2
207	MzYKOTUwIDc4MCAyNzUgMzkwIDM5MCA1MDAgODM4IDMxOCAzNjEgMzE4IDMzNyA2MzYgNjM2IDYz
208	NiA2MzYgNjM2IDYzNiA2MzYgNjM2CjYzNiA2MzYgMzM3IDMzNyA4MzggODM4IDgzOCA1MzEgMTAw
209	MCA2ODQgNjg2IDY5OCA3NzAgNjMyIDU3NSA3NzUgNzUyIDI5NQoyOTUgNjU2IDU1NyA4NjMgNzQ4
210	IDc4NyA2MDMgNzg3IDY5NSA2MzUgNjExIDczMiA2ODQgOTg5IDY4NSA2MTEgNjg1IDM5MCAzMzcK
211	MzkwIDgzOCA1MDAgNTAwIDYxMyA2MzUgNTUwIDYzNSA2MTUgMzUyIDYzNSA2MzQgMjc4IDI3OCA1
212	NzkgMjc4IDk3NCA2MzQgNjEyCjYzNSA2MzUgNDExIDUyMSAzOTIgNjM0IDU5MiA4MTggNTkyIDU5
213	MiA1MjUgNjM2IDMzNyA2MzYgODM4IDYwMCA2MzYgNjAwIDMxOAozNTIgNTE4IDEwMDAgNTAwIDUw
214	MCA1MDAgMTM0MiA2MzUgNDAwIDEwNzAgNjAwIDY4NSA2MDAgNjAwIDMxOCAzMTggNTE4IDUxOAo1
215	OTAgNTAwIDEwMDAgNTAwIDEwMDAgNTIxIDQwMCAxMDIzIDYwMCA1MjUgNjExIDMxOCA0MDEgNjM2
216	IDYzNiA2MzYgNjM2IDMzNwo1MDAgNTAwIDEwMDAgNDcxIDYxMiA4MzggMzYxIDEwMDAgNTAwIDUw
217	MCA4MzggNDAxIDQwMSA1MDAgNjM2IDYzNiAzMTggNTAwCjQwMSA0NzEgNjEyIDk2OSA5NjkgOTY5
218	IDUzMSA2ODQgNjg0IDY4NCA2ODQgNjg0IDY4NCA5NzQgNjk4IDYzMiA2MzIgNjMyIDYzMgoyOTUg
219	Mjk1IDI5NSAyOTUgNzc1IDc0OCA3ODcgNzg3IDc4NyA3ODcgNzg3IDgzOCA3ODcgNzMyIDczMiA3
220	MzIgNzMyIDYxMSA2MDUKNjMwIDYxMyA2MTMgNjEzIDYxMyA2MTMgNjEzIDk4MiA1NTAgNjE1IDYx
221	NSA2MTUgNjE1IDI3OCAyNzggMjc4IDI3OCA2MTIgNjM0CjYxMiA2MTIgNjEyIDYxMiA2MTIgODM4
222	IDYxMiA2MzQgNjM0IDYzNCA2MzQgNTkyIDYzNSA1OTIgXQplbmRvYmoKMTggMCBvYmoKPDwgL0Eg
223	MTkgMCBSIC9FIDIwIDAgUiAvSSAyMSAwIFIgL0ogMjIgMCBSIC9PIDIzIDAgUiAvUyAyNCAwIFIg
224	L1QgMjUgMCBSCi9WIDI2IDAgUiAvYSAyNyAwIFIgL2MgMjggMCBSIC9kIDI5IDAgUiAvZSAzMCAw
225	IFIgL2VpZ2h0IDMxIDAgUiAvZiAzMiAwIFIKL2ZpdmUgMzMgMCBSIC9mb3VyIDM0IDAgUiAvaSAz
226	NSAwIFIgL2wgMzYgMCBSIC9tIDM3IDAgUiAvbiAzOCAwIFIKL25pbmUgMzkgMCBSIC9vIDQwIDAg
227	UiAvb25lIDQxIDAgUiAvcCA0MiAwIFIgL3BlcmlvZCA0MyAwIFIgL3IgNDQgMCBSCi9zaXggNDUg
228	MCBSIC9zcGFjZSA0NiAwIFIgL3QgNDcgMCBSIC90aHJlZSA0OCAwIFIgL3R3byA0OSAwIFIgL3Ug
229	NTAgMCBSCi91bmRlcnNjb3JlIDUxIDAgUiAveCA1MiAwIFIgL3kgNTMgMCBSIC96ZXJvIDU0IDAg
230	UiA+PgplbmRvYmoKMyAwIG9iago8PCAvRjEgMTcgMCBSID4+CmVuZG9iago0IDAgb2JqCjw8IC9B
231	MSA8PCAvVHlwZSAvRXh0R1N0YXRlIC9DQSAwIC9jYSAxID4+Ci9BMiA8PCAvVHlwZSAvRXh0R1N0
232	YXRlIC9DQSAxIC9jYSAxID4+ID4+CmVuZG9iago1IDAgb2JqCjw8ID4+CmVuZG9iago2IDAgb2Jq
233	Cjw8ID4+CmVuZG9iago3IDAgb2JqCjw8IC9JMSAxMyAwIFIgL0kyIDE0IDAgUiA+PgplbmRvYmoK
234	MTMgMCBvYmoKPDwgL1R5cGUgL1hPYmplY3QgL1N1YnR5cGUgL0ltYWdlIC9XaWR0aCA4NTAgL0hl
235	aWdodCA4NTAKL0NvbG9yU3BhY2UgWyAvSW5kZXhlZCAvRGV2aWNlUkdCIDkgKP//zP2PPfZDJ//8
236	xf/7wv/6wP/+yv7qmvxQKoAAJikgXQovQml0c1BlckNvbXBvbmVudCA0IC9GaWx0ZXIgL0ZsYXRl
237	RGVjb2RlCi9EZWNvZGVQYXJtcyA8PCAvUHJlZGljdG9yIDEwIC9Db2xvcnMgMSAvQ29sdW1ucyA4
238	NTAgL0JpdHNQZXJDb21wb25lbnQgNCA+PgovTGVuZ3RoIDU1IDAgUiA+PgpzdHJlYW0KeJzt07FJ
239	BGEURtFZncTQFqxAsAULMrOGzUzd2kTtYM0EkVljA8HgwXLhnAI+/pnL2z0vEz4fRmb428W5H8A/
240	KVWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWh
241	VIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVS
242	FUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpV
243	KFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWh
244	VIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVS
245	FUpVKFWhVIVSFUpVKFWhVIVSFUpVKFWhVIVSFbuZmaunkZntfWTm9DEyM+QwM+OmKpSqUKpCqQql
246	KpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSq
247	UKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpC
248	qQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQql
249	KpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSq
250	UKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpCqQqlKpSqUKpC
251	qQqlKpSqUKpCqQqlKpSqUKpCqQqlKtaZme11ZObiZmTm+21k5jiystzNzLipCqUqlKpQqkKpCqUq
252	lKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQ
253	qkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKp
254	CqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUq
255	lKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQ
256	qkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKpCqUqlKpQqkKp
257	CqUqlKpQqkKpCqUqlKpQqkKpinVm5nScmXkZmVnvR2b2IyvLzK9xUxlKVShVoVSFUhVKVShVoVSF
258	UhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVK
259	VShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShV
260	oVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSF
261	UhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVK
262	VShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShV
263	oVSFUhVKVShVoVTFeu4H/HI6jsxs+5GZx5GVZeab3FSGUhVKVShVoVSFUhVKVShVoVSFUhVKVShV
264	oVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSF
265	UhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVK
266	VShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShV
267	oVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSF
268	UhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVKVShVoVSFUhVK
269	VShVoVTFOjPzdRiZubwdmdmOIzMzK8v1zIybqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCq
270	QqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkK
271	pSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqU
272	qlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCq
273	QqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkK
274	pSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqUqlCqQqkKpSqU
275	qvgBI7ghwAplbmRzdHJlYW0KZW5kb2JqCjU1IDAgb2JqCjIwNjUKZW5kb2JqCjE0IDAgb2JqCjw8
276	IC9UeXBlIC9YT2JqZWN0IC9TdWJ0eXBlIC9JbWFnZSAvV2lkdGggNDMgL0hlaWdodCA4NDkKL0Nv
277	bG9yU3BhY2UgWyAvSW5kZXhlZCAvRGV2aWNlUkdCIDI1NQoo/q9L/qFF7TAi/E0q+0tcKfxPKvhF
278	XCj3Qyf0PSXzOyXyOSTwNSPvMyPuMSLrKyHqXCkg6Scg5yMe5h8d//rA4hkc4Rkd3xcd/q5K3BUe
279	/X442RMf/XQ11hEf0w8g0FxyIfxfL80LIsoJI8gHI8cHI/7ji8QFJMIDJcEDJf2PPb4BJv6tSv2d
280	Q/xdLv/5vv/0sv7ghf/0sP7df//snf6sSf18N/xsM//1s/7IY//uo/2YQf6+Wf/3uf2OPP7Vcv/t
281	of2fRP6rSf/xqfxbLv7Zd/7Rbv/zrv7DXv/4u/2WQPxhL/xjMP/qmf66Vf16N/xqMv7be/7Wc/7e
282	gP7aeP/kjf2aQv64Uv7QbP2IO//3t/6/Wv/pl/6kRv6pSP2ZQfxZLf/9yP7bev7Tb//1tf/6wf7Z
283	dv7AW//olf6oSP14NvxoMv2COf/5vf7cfP62Uf7GYv2cQv7iiP/pmP/xq/E4JP2GOv6gRP1uM/xk
284	MP2XQPpKXCn5SFwo+EZcKPZCJ/VAJvQ+Jv61T/E2JP/nk+0uIewsIf6nR+kmH+gkH//8xOUeHeQc
285	HeMaHPxXLOAYHf/mkd0WHdsUHtoUHvxmMdcSH9UQINQQIP7OatEOIc8MIc4MIstcbiL+zGjJCCP/
286	/cb9jDzFBiT+tE7DBCTAAiX/5Y/9kD29ACa7ACa5ACb+4IS3ACa2ACa0ACb+13SyACawACauACas
287	ACaqACaoACb//sumACb/7J+kACaiACahACafACadACabACaZACaXACb+xF+VACaTACaRACaPACb/
288	8qyNACaLACaKACaIACaGACb9nkOEACaCACaAACb/65z9kj7+s039kz/8Uyv+4on//sn+xWH/+8L+
289	uVP+u1b+3oL/9rb/5Iz+okX9cjT9gDj+34P9hDn//MX+z2v/55T//8z/7aD+wV39kT78USv+1HD+
290	vVf+4Yf/5ZD+y2f+pUb9lT//8Kj/+Lr8VSz/8Kf+3X7+sEv9cDT+pkf/76X9djb/6pvmIR7+ymb/
291	86/9ijv+skz+yWX/76QpCl0KL0JpdHNQZXJDb21wb25lbnQgOCAvRmlsdGVyIC9GbGF0ZURlY29k
292	ZQovRGVjb2RlUGFybXMgPDwgL1ByZWRpY3RvciAxMCAvQ29sb3JzIDEgL0NvbHVtbnMgNDMgL0Jp
293	dHNQZXJDb21wb25lbnQgOCA+PgovTGVuZ3RoIDU2IDAgUiA+PgpzdHJlYW0KeJzNymfbCAQAhtFX
294	NGiorIaiIbK1lAYpDSoqJCsjoakpbVSiVEZKKqNBsiJ7VUbJKNIwioiipdCW/sL95b6u53w+BUu5
295	Aut+xGl3CRdxP+C0u5jT7iJOuwu5iLuA0+57nHbf5SLufE678zjtzuEi7mxOu7M47c7kIu4MTrvT
296	Oe1O4yLuVE67Uzjtvs1F3Emcdidy2p3ARdzxnHbHcdody0XcNzntjuG0+wan3de5iPsap92TOe2O
297	5CJuRU67J3HaHcFF3Aqcdl/htHsCF3GP57Q7jNPucVzEHcpptzyn3Re4iPs8p91jOe0O4SLuMZx2
298	B3PaHcRF3LKcdgdy2j2K0+6zXMR9htPuEZx2n+YibmlOu09x2i3FRdySnHb7cdrty0XcJzjtHs5p
299	9y8u4h7GafdxTruPcRH3UE67xTntHsJF3N6cdntx2t2Hi7gHc9o9iNPugZx2H+Ei7p2cdotx2i3K
300	RdwDOO0+xGn3QS7iPsBpd39Ou/txEfd+Trv3cdrtwUXcIpx2C3Pa3ZeLuFs57X7CaXcHF3Gf5LTb
301	ltNufS7iVuW0W47T7qWcdhtyEbc7p90BnHa7chH3Ck67p3PavYeLuLs47a7jtHs0F3H/4LTbhdPu
302	5VzEPY3T7pGcdtdzEfdGTrtfc9q9i4u413Da/ZfT7stcxD2H024lTruvctrdwkXc5Zx2P+a0+xMX
303	cS/htHsvp92zuIjbhtNuU067t3ERtwqn3Q857dblIu7dnHYLcdpdy0XcVpx2f+S0u5uLuI9y2u3M
304	abc1F3Hrcdo9ldNuZU67ZbiIm2Anp909XMRdwWl3OKfdh7mIewun3Wacdj/jIu5lnHY/57T7PRdx
305	63DavZbTbicu4n7LafciTrtzuYj7KafdWznt1uYi7n+cdv/mtPsDp90XuYj7HKfdjZx2m3MR90JO
306	u+057X7HRdxzOe024bT7Fhdxr+e0ewGn3au4iNuO025jTrs3cxH3N067tTjtXslF3C847X7FaXc0
307	p90aXMTdxmm3G6fdlVzEPZHT7hpOu1dzEXcUp93tnHb7cxG3J6fdbzjt3sBF3Jacdm/ntNuIi7h/
308	ctpdxmn3FC7ivsNpdzOn3fO4iHsmp929nHZ/57T7Kxdxf+a0ez6n3Tu4iPs+p90GnHb/4SJuTU67
309	1TntnsFF3A6cdr/ktNuCi7hnc9r9hdPuxVzEvYnTbjVOuyW4iNuR0+5qTrt9uIi7gdPuS5x2r+O0
310	u4qLuJM57W7irPs/IWAY5AplbmRzdHJlYW0KZW5kb2JqCjU2IDAgb2JqCjk0MAplbmRvYmoKMiAw
311	IG9iago8PCAvVHlwZSAvUGFnZXMgL0tpZHMgWyAxMSAwIFIgXSAvQ291bnQgMSA+PgplbmRvYmoK
312	NTcgMCBvYmoKPDwgL0NyZWF0b3IgKE1hdHBsb3RsaWIgdjMuMTAuOSwgaHR0cHM6Ly9tYXRwbG90
313	bGliLm9yZykKL1Byb2R1Y2VyIChNYXRwbG90bGliIHBkZiBiYWNrZW5kIHYzLjEwLjkpCi9DcmVh
314	dGlvbkRhdGUgKEQ6MjAyNjA1MTcwMDU3MTRaKSA+PgplbmRvYmoKeHJlZgowIDU4CjAwMDAwMDAw
315	MDAgNjU1MzUgZiAKMDAwMDAwMDAxNiAwMDAwMCBuIAowMDAwMDE3NjEwIDAwMDAwIG4gCjAwMDAw
316	MTMwMDggMDAwMDAgbiAKMDAwMDAxMzA0MCAwMDAwMCBuIAowMDAwMDEzMTM5IDAwMDAwIG4gCjAw
317	MDAwMTMxNjAgMDAwMDAgbiAKMDAwMDAxMzE4MSAwMDAwMCBuIAowMDAwMDAwMDY1IDAwMDAwIG4g
318	CjAwMDAwMDAzNTIgMDAwMDAgbiAKMDAwMDAwMTg5NiAwMDAwMCBuIAowMDAwMDAwMjA4IDAwMDAw
319	IG4gCjAwMDAwMDE4NzUgMDAwMDAgbiAKMDAwMDAxMzIyNCAwMDAwMCBuIAowMDAwMDE1NjA3IDAw
320	MDAwIG4gCjAwMDAwMTE1MjkgMDAwMDAgbiAKMDAwMDAxMTMyMiAwMDAwMCBuIAowMDAwMDEwODA0
321	IDAwMDAwIG4gCjAwMDAwMTI1ODIgMDAwMDAgbiAKMDAwMDAwMTkxNiAwMDAwMCBuIAowMDAwMDAy
322	MDc5IDAwMDAwIG4gCjAwMDAwMDIyMzIgMDAwMDAgbiAKMDAwMDAwMjM1NSAwMDAwMCBuIAowMDAw
323	MDAyNTQzIDAwMDAwIG4gCjAwMDAwMDI4MzEgMDAwMDAgbiAKMDAwMDAwMzI0NSAwMDAwMCBuIAow
324	MDAwMDAzMzgzIDAwMDAwIG4gCjAwMDAwMDM1MjcgMDAwMDAgbiAKMDAwMDAwMzkwNyAwMDAwMCBu
325	IAowMDAwMDA0MjEyIDAwMDAwIG4gCjAwMDAwMDQ1MTYgMDAwMDAgbiAKMDAwMDAwNDgzOCAwMDAw
326	MCBuIAowMDAwMDA1MzA2IDAwMDAwIG4gCjAwMDAwMDU1MTUgMDAwMDAgbiAKMDAwMDAwNTgzNyAw
327	MDAwMCBuIAowMDAwMDA2MDAzIDAwMDAwIG4gCjAwMDAwMDYxNDcgMDAwMDAgbiAKMDAwMDAwNjI2
328	NiAwMDAwMCBuIAowMDAwMDA2NTk3IDAwMDAwIG4gCjAwMDAwMDY4MzMgMDAwMDAgbiAKMDAwMDAw
329	NzIyOCAwMDAwMCBuIAowMDAwMDA3NTE5IDAwMDAwIG4gCjAwMDAwMDc2NzQgMDAwMDAgbiAKMDAw
330	MDAwNzk4NiAwMDAwMCBuIAowMDAwMDA4MTA5IDAwMDAwIG4gCjAwMDAwMDgzNDIgMDAwMDAgbiAK
331	MDAwMDAwODczNSAwMDAwMCBuIAowMDAwMDA4ODI1IDAwMDAwIG4gCjAwMDAwMDkwMzEgMDAwMDAg
332	biAKMDAwMDAwOTQ0NCAwMDAwMCBuIAowMDAwMDA5NzY4IDAwMDAwIG4gCjAwMDAwMTAwMTUgMDAw
333	MDAgbiAKMDAwMDAxMDE0MSAwMDAwMCBuIAowMDAwMDEwMzAyIDAwMDAwIG4gCjAwMDAwMTA1MTYg
334	MDAwMDAgbiAKMDAwMDAxNTU4NiAwMDAwMCBuIAowMDAwMDE3NTkwIDAwMDAwIG4gCjAwMDAwMTc2
335	NzAgMDAwMDAgbiAKdHJhaWxlcgo8PCAvU2l6ZSA1OCAvUm9vdCAxIDAgUiAvSW5mbyA1NyAwIFIg
336	Pj4Kc3RhcnR4cmVmCjE3ODIzCiUlRU9GCg==
337	EOF_error_overlap_pdf
338	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9ca8ef4-b1fb-47cf-9dc8-d0f73a845ead",
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "6c22f233-8cad-431a-856b-0a1d22fe1c7d",
  "sourceToolAssistantUUID": "a9ca8ef4-b1fb-47cf-9dc8-d0f73a845ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-25T09:13:13.826Z_



Now let me read the two large files in chunks, and start executing the first transfer.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c22f233-8cad-431a-856b-0a1d22fe1c7d",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2i5Epwk1uxZDtZuvFE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f15517b-46c5-4218-a79b-48289fc84899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XBHPsXEZZMVqupXaT5Eav",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 57683,
      "cache_read_input_tokens": 14060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 57683,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T09:13:14.774Z_

<details open><summary>🔧 Tool call — Read · `toolu_014C7brJozygUGAMAzgsZuo8`</summary>

```json
{
  "file_path": "/tmp/paper_transfer/cmd_fig3.sh",
  "offset": 0,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f15517b-46c5-4218-a79b-48289fc84899",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2i5Epwk1uxZDtZuvFE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddb976da-37ac-4ac2-bf0e-7d582e5ec5db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XBHPsXEZZMVqupXaT5Eav",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 57683,
      "cache_read_input_tokens": 14060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 57683,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T09:13:15.019Z_

<details><summary>↩ Tool result · reported error · `toolu_014C7brJozygUGAMAzgsZuo8`</summary>

```text
File content (31760 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddb976da-37ac-4ac2-bf0e-7d582e5ec5db",
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "493b54d4-b271-49bf-b742-dae8771fed33",
  "toolUseResult": "Error: File content (31760 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "ddb976da-37ac-4ac2-bf0e-7d582e5ec5db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T09:13:15.394Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B9EkybkNRy99nTQaa7f9K4`</summary>

```json
{
  "file_path": "/tmp/paper_transfer/cmd_fig4.sh",
  "offset": 0,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "493b54d4-b271-49bf-b742-dae8771fed33",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2i5Epwk1uxZDtZuvFE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa9c4288-e528-40d4-bdf8-fcbd59c25539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XBHPsXEZZMVqupXaT5Eav",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 57683,
      "cache_read_input_tokens": 14060,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 57683
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 14060,
          "cache_creation_input_tokens": 57683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 57683,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T09:13:15.659Z_

<details><summary>↩ Tool result · reported error · `toolu_01B9EkybkNRy99nTQaa7f9K4`</summary>

```text
File content (25289 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa9c4288-e528-40d4-bdf8-fcbd59c25539",
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "12a12487-d727-4ad2-ab53-a994b2b4482d",
  "toolUseResult": "Error: File content (25289 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "fa9c4288-e528-40d4-bdf8-fcbd59c25539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-25T09:13:20.344Z_

The files are too large to read through the Read tool. I'll use bash to get their contents and execute them directly via SSH.

Let me start by transferring figure 2 (which I already have the content for), while getting the content of the large files via bash.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12a12487-d727-4ad2-ab53-a994b2b4482d",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2j1LTJTra7Wvu2n7xV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d94ddc9f-4118-472b-bb9f-b15e215ff1f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZ2cJrxcPAyRbxCWnaBWm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 345,
      "cache_read_input_tokens": 71743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 345,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T09:13:21.682Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017mHvSYCuTqTptb5bAqiVM4`</summary>

```json
{
  "command": "wc -c /tmp/paper_transfer/cmd_fig2.sh /tmp/paper_transfer/cmd_fig3.sh /tmp/paper_transfer/cmd_fig4.sh /tmp/paper_transfer/cmd_fig5.sh /tmp/paper_transfer/cmd_fig6.sh",
  "description": "Check file sizes of all command scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d94ddc9f-4118-472b-bb9f-b15e215ff1f1",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2j1LTJTra7Wvu2n7xV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07239662-d1e9-42db-abc5-29638653c6e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZ2cJrxcPAyRbxCWnaBWm4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 345,
      "cache_read_input_tokens": 71743,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 345
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 71743,
          "cache_creation_input_tokens": 345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 345,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T09:13:21.730Z_

<details><summary>↩ Tool result · `toolu_017mHvSYCuTqTptb5bAqiVM4`</summary>

```text
 16270 /tmp/paper_transfer/cmd_fig2.sh
 36776 /tmp/paper_transfer/cmd_fig3.sh
 29275 /tmp/paper_transfer/cmd_fig4.sh
 20666 /tmp/paper_transfer/cmd_fig5.sh
 25874 /tmp/paper_transfer/cmd_fig6.sh
128861 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07239662-d1e9-42db-abc5-29638653c6e3",
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "92f6b8f4-a2de-4e90-93dc-af2424786701",
  "sourceToolAssistantUUID": "07239662-d1e9-42db-abc5-29638653c6e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-25T09:13:26.885Z_

The files are large base64-encoded PDFs. I'll transfer them one by one using ssh_execute. Since I can't read the large files through the Read tool, I'll use bash to pipe them into the ssh_execute calls. Let me start with figure 2 which I already read.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92f6b8f4-a2de-4e90-93dc-af2424786701",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2jTRbeCL3n3fBNTEZc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07d8340c-a8ab-4085-a5e4-8fcd64599cd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Moki6w7wig8usHCRCo32Lh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 72088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 308,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T09:13:27.478Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TVsF6nS9dV9ke32AMd77Vt`</summary>

```json
{
  "command": "cat /tmp/paper_transfer/cmd_fig2.sh",
  "description": "Read fig2 command script content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07d8340c-a8ab-4085-a5e4-8fcd64599cd2",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2jTRbeCL3n3fBNTEZc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3975bb27-85ab-4379-94bf-2f07c61ff2c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Moki6w7wig8usHCRCo32Lh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 72088,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 308
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 72088,
          "cache_creation_input_tokens": 308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 308,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T09:13:27.533Z_

<details><summary>↩ Tool result · `toolu_01TVsF6nS9dV9ke32AMd77Vt`</summary>

```text
base64 -d > /root/trace-verdict-study/figures/paper/fig2_calibration.pdf << 'EOF_fig2_calibration_pdf'
JVBERi0xLjQKJazcIKu6CjEgMCBvYmoKPDwgL1R5cGUgL0NhdGFsb2cgL1BhZ2VzIDIgMCBSID4+
CmVuZG9iago4IDAgb2JqCjw8IC9Gb250IDMgMCBSIC9YT2JqZWN0IDcgMCBSIC9FeHRHU3RhdGUg
NCAwIFIgL1BhdHRlcm4gNSAwIFIKL1NoYWRpbmcgNiAwIFIgL1Byb2NTZXQgWyAvUERGIC9UZXh0
IC9JbWFnZUIgL0ltYWdlQyAvSW1hZ2VJIF0gPj4KZW5kb2JqCjExIDAgb2JqCjw8IC9UeXBlIC9Q
YWdlIC9QYXJlbnQgMiAwIFIgL1Jlc291cmNlcyA4IDAgUgovTWVkaWFCb3ggWyAwIDAgMjQ2Ljkw
MzU0MDIzNDUgMjc1Ljk2Mzc1IF0gL0NvbnRlbnRzIDkgMCBSIC9Bbm5vdHMgMTAgMCBSCj4+CmVu
ZG9iago5IDAgb2JqCjw8IC9MZW5ndGggMTIgMCBSIC9GaWx0ZXIgL0ZsYXRlRGVjb2RlID4+CnN0
cmVhbQp4nKVWy3IbNxDEGV+Bo3UQNDN4Hy1FVpUPSSlmOYc4h5imZbvoF53Eyd+nsSQXWD7tRKrd
4jYaMz0DYAZXPyz+ejtf/Hx3bW6e6av2Nf+i2bzD82DIvMPz1bC5w/OgCV/vtfhoC7ng8bXsviQF
W6JLAShNvt5o/VpfPYaJL5hzp7XPNhou1vtKgEnHNlGRhi0bJkms21gaJvbAxrSsTT9AJiTbDNFw
VBEdi82ceeKvYRC58aevEfNX/RlvMpcESx6snH0SouJNgOf5e30901dP2GQbzOz1kJHZK/2reaR+
VB+VUTO1Ur+ruVpcmN/M7Km+nel7PQjSzLEGxNIr6cBTUoq3MWCOSGA+K+WJ+lMt8X9aTnQ2ElGe
yGngKTkcxMYciZMvks/qeX5hCtvCnKJPFAqgj2p2YYKzjnIWFwQJfqQe76sUJusLk59slwaeVJmS
jSkHT+J8OKvyVv1dM6U+qT/UWwj8gPz9hPdS/bOva3cH+2C5372H1FhJnDGKJScZfp2SQ8riIcXH
nHO2ORTnRu8jcMi9SM0FC9wjaVDpA9YOa3FewzEFiAEhYSG2ChpwUEG2lIf0CHsodeR8DpzPKtjx
H7f+cT5doixS/ccJMPgfSDHanBK5uCU1oJFSsVJSLm5LakAj5WxLPYB5S2pAIxVYJ880khrQSEzO
+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
85IJr5Wir5SPtsoQAd2l8ZqDkiMknzflE6YKWDFWjNGd5I/FMm1W6pIk9pP8FSS/d4mNJTf3kHDx
hiX38ZAXO0brvNiJsuO/jau6G7NMqvtH3Ija4Ww1bb/R0A+2yt5/dkDihQplbmRzdHJlYW0KZW5k
b2JqCjE0IDAgb2JqCjw8IC9UeXBlIC9Gb250IC9TdWJ0eXBlIC9DSURGb250VHlwZTIgL0Jhc2VG
b250IC9CWEdFVkwrRGVqYVZ1U2VyaWYKL0NJRFN5c3RlbUluZm8gPDwgL1JlZ2lzdHJ5IChBZG9i
ZSkgL09yZGVyaW5nIChJZGVudGl0eSkgL1N1cHBsZW1lbnQgMCA+PgovRm9udERlc2NyaXB0b3Ig
MTMgMCBSIC9XIDE4IDAgUiAvQ0lEVG9HSURNYXAgMTYgMCBSID4+CmVuZG9iagoxNSAwIG9iago8
PCAvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTAgL0Jhc2VGb250IC9CWEdFVkwrRGVqYVZ1U2Vy
aWYKL0VuY29kaW5nIC9JZGVudGl0eS1IIC9EZXNjZW5kYW50Rm9udHMgWyAxNCAwIFIgXSAvVG9V
bmljb2RlIDE5IDAgUiA+PgplbmRvYmoKMTMgMCBvYmoKPDwgL1R5cGUgL0ZvbnREZXNjcmlwdG9y
IC9Gb250TmFtZSAvQlhHRVZMK0RlamFWdVNlcmlmIC9GbGFncyAzMgovRm9udEJCb3ggWyAtNzcw
IC0zNDcgMjEwNiAxMTEwIF0gL0FzY2VudCA5MjkgL0Rlc2NlbnQgLTIzNiAvQ2FwSGVpZ2h0IDAK
L1hIZWlnaHQgMCAvSXRhbGljQW5nbGUgMCAvU3RlbVYgMCAvRm9udEZpbGUyIDE3IDAgUiAvTWF4
V2lkdGggODc1ID4+CmVuZG9iagoxOCAwIG9iagpbIDMyIFsgMzE4IF0gNDAgWyAzOTAgMzkwIF0g
NDYgWyAzMTggXSA0OCBbIDYzNiA2MzYgNjM2IF0gNTIgWyA2MzYgNjM2IF0KNTUgWyA2MzYgNjM2
IDYzNiBdIDY1IFsgNzIyIF0gNjcgWyA3NjUgXSA2OSBbIDczMCA2OTQgXSA3OCBbIDg3NSA4MjAg
XSA4NApbIDY2NyBdIDg2IFsgNzIyIF0gOTcgWyA1OTYgNjQwIDU2MCA2NDAgNTkyIF0gMTA1IFsg
MzIwIF0gMTA4IFsgMzIwIF0gMTEwClsgNjQ0IDYwMiA2NDAgXSAxMTQgWyA0NzggXSAxMTYgWyA0
MDIgNjQ0IF0gMTIwIFsgNTY0IDU2NSBdIF0KZW5kb2JqCjMgMCBvYmoKPDwgL0YxIDE1IDAgUiA+
PgplbmRvYmoKNCAwIG9iago8PCAvQTEgPDwgL1R5cGUgL0V4dEdTdGF0ZSAvQ0EgMCAvY2EgMSA+
PgovQTIgPDwgL1R5cGUgL0V4dEdTdGF0ZSAvQ0EgMSAvY2EgMSA+PiA+PgplbmRvYmoKNSAwIG9i
ago8PCA+PgplbmRvYmoKNiAwIG9iago8PCA+PgplbmRvYmoKNyAwIG9iago8PCA+PgplbmRvYmoK
MiAwIG9iago8PCAvVHlwZSAvUGFnZXMgL0tpZHMgWyAxMSAwIFIgXSAvQ291bnQgMSA+PgplbmRv
YmoKMjAgMCBvYmoKPDwgL0NyZWF0b3IgKE1hdHBsb3RsaWIgdjMuMTAuNSwgaHR0cHM6Ly9tYXRw
bG90bGliLm9yZykKL1Byb2R1Y2VyIChNYXRwbG90bGliIHBkZiBiYWNrZW5kIHYzLjEwLjUpCi9D
cmVhdGlvbkRhdGUgKEQ6MjAyNjA1MjUwMzA2MTArMDgnMDAnKSA+PgplbmRvYmoKeHJlZgowIDIx
CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxNiAwMDAwMCBuIAowMDAwMDExMjI5IDAwMDAw
IG4gCjAwMDAwMTEwMzUgMDAwMDAgbiAKMDAwMDAxMTA2NyAwMDAwMCBuIAowMDAwMDExMTY2IDAw
MDAwIG4gCjAwMDAwMTExODcgMDAwMDAgbiAKMDAwMDAxMTIwOCAwMDAwMCBuIAowMDAwMDAwMDY1
IDAwMDAwIG4gCjAwMDAwMDAzNDcgMDAwMDAgbiAKMDAwMDAwMTUxMyAwMDAwMCBuIAowMDAwMDAw
MjA4IDAwMDAwIG4gCjAwMDAwMDE0OTIgMDAwMDAgbiAKMDAwMDAxMDUxMiAwMDAwMCBuIAowMDAw
MDEwMTUwIDAwMDAwIG4gCjAwMDAwMTAzNjQgMDAwMDAgbiAKMDAwMDAwOTUzMyAwMDAwMCBuIAow
MDAwMDAxNTMzIDAwMDAwIG4gCjAwMDAwMTA3MzYgMDAwMDAgbiAKMDAwMDAwOTY5OCAwMDAwMCBu
IAowMDAwMDExMjg5IDAwMDAwIG4gCnRyYWlsZXIKPDwgL1NpemUgMjEgL1Jvb3QgMSAwIFIgL0lu
Zm8gMjAgMCBSID4+CnN0YXJ0eHJlZgoxMTQ0OAolJUVPRgo=
EOF_fig2_calibration_pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3975bb27-85ab-4379-94bf-2f07c61ff2c0",
  "isSidechain": true,
  "promptId": "e6b5258b-f1bb-42d3-80a8-e9c77d65827b",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "b8735de4-50e0-45bf-8262-f4e5daae00f5",
  "sourceToolAssistantUUID": "3975bb27-85ab-4379-94bf-2f07c61ff2c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-25T09:13:32.768Z_

Good, I have the content. Now let me execute the transfers one by one. I'll start with fig2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8735de4-50e0-45bf-8262-f4e5daae00f5",
  "isSidechain": true,
  "agentId": "a93cf04f7cf220353",
  "requestId": "req_011CbP2jt7A4Z8f2yVDBqTfP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "795da05f-6fb6-4390-b67b-fef0da9889ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiB4ZXuTk8iB317oiqGtcT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14151,
      "cache_read_input_tokens": 72396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14151,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

## Round 2

1 recorded events

### User

_source line 28 · 2026-05-25T09:23:32.774Z_

[Request interrupted by user]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "795da05f-6fb6-4390-b67b-fef0da9889ea",
  "isSidechain": true,
  "promptId": "1977c993-f261-406f-99af-1cea79027019",
  "agentId": "a93cf04f7cf220353",
  "type": "user",
  "uuid": "aa36311b-b071-4903-958b-dcb45106c82b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "995a981a-a963-42bc-ab1d-d207ba4580d9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "bright-crafting-parrot"
}
```

</details>

---
