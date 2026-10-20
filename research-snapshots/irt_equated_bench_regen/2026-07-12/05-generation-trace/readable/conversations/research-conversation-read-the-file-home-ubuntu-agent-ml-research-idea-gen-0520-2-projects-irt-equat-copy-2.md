# Research conversation: Read the file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_map.

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3a7427bd484b01d4.jsonl`
- **Structured JSON:** [`41d50ce44c64d402d622.json`](../../sessions/41/41d50ce44c64d402d622.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-21T03:15:01.202Z_

Read the file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_map.yaml and return its full contents. Also check if there's a literature.py tool at /home/ubuntu/agent-ml-research/core/tools/literature.py and show me its add_to_literature_map function signature.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2c0f4d57-045f-436c-bd98-ba48fb6b2b34",
  "agentId": "a3a7427bd484b01d4",
  "type": "user",
  "uuid": "530e6d25-fd83-4543-9f39-673df0902030",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T03:15:02.984Z_

I'll help you read the literature_map.yaml file and check for the literature.py tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "530e6d25-fd83-4543-9f39-673df0902030",
  "isSidechain": true,
  "agentId": "a3a7427bd484b01d4",
  "requestId": "req_011CbEzAuEgiwwciQWk8XWSc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7e8c4900-7b71-4905-901d-168714f94818",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XKFrFN6H6wrPKZAaqENPL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25345,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25345,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 3 · 2026-05-21T03:15:03.402Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EwHbUg1jRSh2i7BycgKXTG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e8c4900-7b71-4905-901d-168714f94818",
  "isSidechain": true,
  "agentId": "a3a7427bd484b01d4",
  "requestId": "req_011CbEzAuEgiwwciQWk8XWSc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23cf64a4-cf1e-4a62-8138-1f6c34c13492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XKFrFN6H6wrPKZAaqENPL4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25345,
      "cache_read_input_tokens": 0,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25345
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 167,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 25345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25345,
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

_source line 4 · 2026-05-21T03:15:03.463Z_

<details><summary>↩ Tool result · reported error · `toolu_01EwHbUg1jRSh2i7BycgKXTG`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23cf64a4-cf1e-4a62-8138-1f6c34c13492",
  "isSidechain": true,
  "promptId": "2c0f4d57-045f-436c-bd98-ba48fb6b2b34",
  "agentId": "a3a7427bd484b01d4",
  "type": "user",
  "uuid": "70a93bd5-8113-4644-89ae-30d62b0cefad",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen.",
  "sourceToolAssistantUUID": "23cf64a4-cf1e-4a62-8138-1f6c34c13492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T03:15:03.474Z_

<details open><summary>🔧 Tool call — Read · `toolu_013M1gvJ6TgNyYbvATtsLrYo`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/literature.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70a93bd5-8113-4644-89ae-30d62b0cefad",
  "isSidechain": true,
  "agentId": "a3a7427bd484b01d4",
  "requestId": "req_011CbEzAuEgiwwciQWk8XWSc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dfd08f5f-0037-4faa-a37d-1a01d8d5a7b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XKFrFN6H6wrPKZAaqENPL4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25345,
      "cache_read_input_tokens": 0,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25345
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 167,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 25345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25345,
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

_source line 6 · 2026-05-21T03:15:03.496Z_

<details><summary>↩ Tool result · `toolu_013M1gvJ6TgNyYbvATtsLrYo`</summary>

```text
1	"""Literature map — persistent, cross-stage knowledge base of papers.
2	
3	The literature_map.yaml is the single source of truth for papers a project
4	accumulates across the Idea → Research → Writing → Review pipeline. Each
5	entry is verified (or marked unverified) and carries enough metadata to
6	generate BibTeX entries and to drive Related Work / citation gap-fill in
7	the Paper Agent's writing pipeline.
8	
9	Two scopes:
10	
11	  - Project-level: ``projects/{project}/literature_map.yaml``
12	      Used during Research and Writing phases.
13	
14	  - Global (Idea phase): ``{WORKSPACE_ROOT}/literature_map.yaml``
15	      Used before a project exists. Each entry carries ``source_idea_id`` so
16	      multiple ideas can coexist. On project creation, matching entries are
17	      seeded into the project map.
18	
19	Design notes:
20	
21	  - Read paths support modes (summary / category:X / competitors / unverified
22	    / bib / full) so day-to-day reads stay token-cheap even when the map has
23	    grown to 40-60 papers.
24	
25	  - Writes hold an exclusive flock + use atomic temp→rename, modeled on
26	    ``core/tools/registry.py`` so the file never tears under concurrent
27	    Worker writes.
28	
29	  - Dedup happens on add: DOI exact match wins; otherwise normalized title
30	    match. Existing entries are merged (new fields fill empty existing
31	    fields) rather than overwritten.
32	"""
33	
34	from __future__ import annotations
35	
36	import fcntl
37	import logging
38	import os
39	import re
40	import tempfile
41	import unicodedata
42	from pathlib import Path
43	from typing import Any, Iterable
44	
45	import yaml
46	
47	from core import paths as _paths
48	from core.tools.result import ToolResult
49	
50	logger = logging.getLogger(__name__)
51	
52	
53	# ---------------------------------------------------------------------------
54	# Constants
55	# ---------------------------------------------------------------------------
56	
57	# Roles a paper can play relative to the project. Used by Related Work drafting
58	# (foundation papers anchor narratives; direct-competitor papers must be cited).
59	VALID_ROLES: frozenset[str] = frozenset(
60	    {"foundation", "direct-competitor", "method-component", "evaluation", "background"}
61	)
62	
63	# Modes for read_literature_map — keep token usage proportional to need.
64	VALID_READ_MODES: frozenset[str] = frozenset(
65	    {"summary", "competitors", "unverified", "bib", "full"}
66	)
67	
68	# Fields kept in summary mode (skips long fields like abstract, relevance).
69	_SUMMARY_FIELDS: tuple[str, ...] = (
70	    "title", "year", "venue", "category", "role", "verified", "bibtex_key",
71	)
72	
73	
74	# ---------------------------------------------------------------------------
75	# Path resolution
76	# ---------------------------------------------------------------------------
77	
78	def get_literature_map_path(project: str | None = None) -> Path:
79	    """Resolve the literature_map.yaml path.
80	
81	    Project name → ``projects/{project}/literature_map.yaml`` (V3 layout).
82	    No project   → ``{WORKSPACE_ROOT}/literature_map.yaml`` (global, idea phase).
83	    """
84	    if project:
85	        p = _paths.resolve_project_file(project, "literature_map.yaml")
86	        p.parent.mkdir(parents=True, exist_ok=True)
87	        return p
88	    return _paths.global_literature_map_path()
89	
90	
91	# ---------------------------------------------------------------------------
92	# Atomic file I/O — modeled on registry._read_modify_write_registry
93	# ---------------------------------------------------------------------------
94	
95	def _empty_map() -> dict:
96	    return {
97	        "meta": {"last_updated": None, "total_papers": 0},
98	        "categories": [],
99	        "papers": {},
100	    }
101	
102	
103	def _read_map(path: Path) -> dict:
104	    """Read literature_map.yaml without a lock (atomic single-syscall read).
105	
106	    Returns a fresh empty skeleton if the file doesn't exist or is unreadable.
107	    Writers use exclusive flock + atomic rename so readers always see a
108	    consistent snapshot.
109	    """
110	    if not path.exists():
111	        return _empty_map()
112	    try:
113	        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
114	    except Exception:
115	        logger.warning("Failed to parse literature_map at %s", path, exc_info=True)
116	        return _empty_map()
117	    if isinstance(data, list):
118	        data = {"papers": data, "meta": {}, "categories": []}
119	    elif not isinstance(data, dict):
120	        logger.warning("literature_map at %s is %s, expected dict — resetting", path, type(data).__name__)
121	        return _empty_map()
122	    data.setdefault("meta", {})
123	    data["meta"].setdefault("last_updated", None)
124	    data["meta"].setdefault("total_papers", 0)
125	    data.setdefault("categories", [])
126	    data.setdefault("papers", {})
127	    return data
128	
129	
130	def _read_modify_write(path: Path, modifier) -> dict:
131	    """Read, apply ``modifier(data)`` in place, atomically write back.
132	
133	    Holds LOCK_EX on a sibling .lock file (not the data file — atomic rename
134	    swaps the inode and would invalidate locks held on it).
135	    """
136	    path.parent.mkdir(parents=True, exist_ok=True)
137	    lock_path = path.with_suffix(".lock")
138	
139	    with open(lock_path, "a+") as lock_f:
140	        fcntl.flock(lock_f, fcntl.LOCK_EX)
141	        try:
142	            data = _read_map(path)
143	            modifier(data)
144	            data["meta"]["total_papers"] = len(data.get("papers", {}))
145	            data["meta"]["last_updated"] = _paths.now_iso()
146	
147	            fd, tmp_path = tempfile.mkstemp(
148	                dir=str(path.parent), prefix=".literature_", suffix=".tmp"
149	            )
150	            try:
151	                with os.fdopen(fd, "w", encoding="utf-8") as tmp_f:
152	                    yaml.dump(
153	                        data, tmp_f,
154	                        default_flow_style=False, allow_unicode=True, sort_keys=False,
155	                    )
156	                    tmp_f.flush()
157	                    os.fsync(tmp_f.fileno())
158	                os.replace(tmp_path, str(path))
159	            except Exception:
160	                if os.path.exists(tmp_path):
161	                    os.unlink(tmp_path)
162	                raise
163	        finally:
164	            fcntl.flock(lock_f, fcntl.LOCK_UN)
165	
166	    return data
167	
168	
169	# ---------------------------------------------------------------------------
170	# Normalization & dedup
171	# ---------------------------------------------------------------------------
172	
173	_PUNCT_RE = re.compile(r"[^\w\s]")
174	_WS_RE = re.compile(r"\s+")
175	
176	
177	def _normalize_title(title: str) -> str:
178	    """Lowercase, strip diacritics + punctuation, collapse whitespace.
179	
180	    Used for fuzzy dedup when two records describe the same paper with
181	    slightly different titles (smart quotes, hyphens, capitalization).
182	    """
183	    if not title:
184	        return ""
185	    s = unicodedata.normalize("NFKD", title)
186	    s = "".join(c for c in s if not unicodedata.combining(c))
187	    s = s.lower()
188	    s = _PUNCT_RE.sub(" ", s)
189	    s = _WS_RE.sub(" ", s).strip()
190	    return s
191	
192	
193	def _normalize_doi(doi: str) -> str:
194	    """Lowercase DOI, strip common prefixes."""
195	    if not doi:
196	        return ""
197	    s = doi.strip().lower()
198	    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
199	        if s.startswith(prefix):
200	            s = s[len(prefix):]
201	            break
202	    return s.strip()
203	
204	
205	def _slugify(s: str, max_len: int = 24) -> str:
206	    """First-word slug — lowercase, alnum only, truncated."""
207	    s = unicodedata.normalize("NFKD", s or "")
208	    s = "".join(c for c in s if not unicodedata.combining(c))
209	    s = re.sub(r"[^a-zA-Z0-9]+", "", s.split()[0] if s.split() else "")
210	    return s.lower()[:max_len]
211	
212	
213	def _generate_bibtex_key(paper: dict) -> str:
214	    """Generate a bibtex key like ``vaswani2017attention``.
215	
216	    Uses the first author's surname + year + the first significant word of
217	    the title. Falls back to ``paper_{hash}`` if metadata is missing.
218	    """
219	    authors = paper.get("authors") or []
220	    first_author = ""
221	    if authors:
222	        raw = authors[0]
223	        if isinstance(raw, str):
224	            # Could be "Vaswani, A." or "Ashish Vaswani"
225	            if "," in raw:
226	                first_author = raw.split(",", 1)[0].strip()
227	            else:
228	                first_author = raw.strip().split()[-1] if raw.strip() else ""
229	    surname = _slugify(first_author)
230	
231	    year = paper.get("year") or ""
232	    year_part = str(year) if year else ""
233	
234	    title = paper.get("title") or ""
235	    # Skip stop words for the title slug
236	    stop = {"a", "an", "the", "on", "in", "of", "for", "and", "or", "is", "to"}
237	    words = [w for w in re.split(r"\W+", title.lower()) if w and w not in stop]
238	    word = _slugify(words[0]) if words else ""
239	
240	    key = f"{surname}{year_part}{word}"
241	    if not key.strip():
242	        import hashlib
243	        h = hashlib.md5(title.encode("utf-8")).hexdigest()[:8]
244	        key = f"paper_{h}"
245	    return key
246	
247	
248	def _find_existing_key(papers: dict, candidate: dict) -> str | None:
249	    """Find a matching paper key in ``papers`` for the candidate dict.
250	
251	    Match order: DOI exact (normalized) → normalized title.
252	    Returns the existing key or None.
253	
254	    bibtex_key collisions are NOT treated as dedup signal — two different
255	    papers can share a naive bibtex_key (e.g. same first author + year), and
256	    we handle that with a suffix at insert time. Real dedup must be content
257	    based.
258	    """
259	    cand_doi = _normalize_doi(candidate.get("doi", ""))
260	    cand_title = _normalize_title(candidate.get("title", ""))
261	
262	    for key, entry in papers.items():
263	        if cand_doi:
264	            entry_doi = _normalize_doi(entry.get("doi", ""))
265	            if entry_doi and entry_doi == cand_doi:
266	                return key
267	        if cand_title:
268	            entry_title = _normalize_title(entry.get("title", ""))
269	            if entry_title and entry_title == cand_title:
270	                return key
271	    return None
272	
273	
274	def _merge_paper(existing: dict, new: dict) -> dict:
275	    """Merge new fields into existing — only fill empty slots, never overwrite.
276	
277	    Verified=True wins over False (a later verification cannot un-verify).
278	    """
279	    merged = dict(existing)
280	    for k, v in new.items():
281	        if v is None or v == "" or v == []:
282	            continue
283	        if k == "verified":
284	            merged["verified"] = bool(existing.get("verified")) or bool(v)
285	            continue
286	        if not merged.get(k):
287	            merged[k] = v
288	    return merged
289	
290	
291	# ---------------------------------------------------------------------------
292	# Public API
293	# ---------------------------------------------------------------------------
294	
295	def read_literature_map(
296	    project: str | None = None,
297	    mode: str = "summary",
298	) -> ToolResult:
299	    """Read the literature map with mode-controlled verbosity.
300	
301	    Args:
302	        project: Project name — None reads the global (idea-phase) map.
303	        mode:
304	          - "summary"        → categories + per-paper {title, year, venue,
305	                                category, role, verified, bibtex_key}
306	          - "category:&lt;key>" → full entries in the named category
307	          - "competitors"    → full entries with role=direct-competitor
308	          - "unverified"     → full entries with verified=False
309	          - "bib"            → list of bibtex_key strings (for citation lookups)
310	          - "full"           → everything (use sparingly — token-heavy)
311	
312	    Returns:
313	        ToolResult.data = {
314	            "categories": [...],
315	            "papers": {key: {...}, ...},
316	            "meta": {"last_updated", "total_papers"},
317	            "mode": &lt;effective mode>,
318	        }
319	    """
320	    path = get_literature_map_path(project)
321	    data = _read_map(path)
322	    papers: dict = data.get("papers", {})
323	    categories: list = data.get("categories", [])
324	
325	    # Category-scoped read: "category:&lt;key>"
326	    if mode.startswith("category:"):
327	        cat_key = mode.split(":", 1)[1].strip()
328	        filtered = {k: v for k, v in papers.items() if v.get("category") == cat_key}
329	        return ToolResult(success=True, data={
330	            "categories": [c for c in categories if c.get("key") == cat_key],
331	            "papers": filtered,
332	            "meta": data.get("meta", {}),
333	            "mode": mode,
334	        })
335	
336	    if mode not in VALID_READ_MODES:
337	        return ToolResult(
338	            success=False,
339	            error=(
340	                f"Unknown mode '{mode}'. Valid: {sorted(VALID_READ_MODES)} "
341	                "or 'category:&lt;key>'."
342	            ),
343	        )
344	
345	    if mode == "summary":
346	        compact = {
347	            k: {f: v.get(f) for f in _SUMMARY_FIELDS if f in v}
348	            for k, v in papers.items()
349	        }
350	        return ToolResult(success=True, data={
351	            "categories": categories,
352	            "papers": compact,
353	            "meta": data.get("meta", {}),
354	            "mode": mode,
355	        })
356	
357	    if mode == "competitors":
358	        filtered = {k: v for k, v in papers.items() if v.get("role") == "direct-competitor"}
359	        return ToolResult(success=True, data={
360	            "categories": categories,
361	            "papers": filtered,
362	            "meta": data.get("meta", {}),
363	            "mode": mode,
364	        })
365	
366	    if mode == "unverified":
367	        filtered = {k: v for k, v in papers.items() if not v.get("verified")}
368	        return ToolResult(success=True, data={
369	            "categories": categories,
370	            "papers": filtered,
371	            "meta": data.get("meta", {}),
372	            "mode": mode,
373	        })
374	
375	    if mode == "bib":
376	        keys = [v.get("bibtex_key") or k for k, v in papers.items()]
377	        return ToolResult(success=True, data={
378	            "bibtex_keys": keys,
379	            "meta": data.get("meta", {}),
380	            "mode": mode,
381	        })
382	
383	    # mode == "full"
384	    return ToolResult(success=True, data={
385	        "categories": categories,
386	        "papers": papers,
387	        "meta": data.get("meta", {}),
388	        "mode": mode,
389	    })
390	
391	
392	def add_to_literature_map(
393	    project: str | None = None,
394	    papers: Iterable[dict] | None = None,
395	    added_by: str = "",
396	) -> ToolResult:
397	    """Add (or merge) one or more papers into the literature map.
398	
399	    Dedup: DOI exact (normalized) → normalized title → bibtex_key collision.
400	    Existing entries are merged field-by-field, never overwritten.
401	
402	    Args:
403	        project: Project name — None writes to the global (idea-phase) map.
404	        papers: Iterable of paper dicts. Recognized fields:
405	                title, authors (list[str]), year, venue, url, doi,
406	                bibtex_key, category, role, relevance, abstract,
407	                semantic_scholar_id, source_idea_id, verified.
408	                Missing bibtex_key is auto-generated.
409	        added_by: Free-form tag for provenance ("paper-research",
410	                  "idea-generator", "user", etc.). Recorded on new entries.
411	
412	    Returns:
413	        ToolResult.data = {
414	            "added": [keys],            # newly inserted
415	            "merged": [keys],           # matched existing, fields merged
416	            "rejected": [{title, reason}],
417	            "total_papers": N,
418	        }
419	    """
420	    if not papers:
421	        return ToolResult(
422	            success=False, error="No papers provided.",
423	        )
424	
425	    paper_list = list(papers)
426	    added: list[str] = []
427	    merged: list[str] = []
428	    rejected: list[dict] = []
429	    now = _paths.now_iso()
430	
431	    def _apply(data: dict) -> None:
432	        existing = data.setdefault("papers", {})
433	        for cand in paper_list:
434	            if not isinstance(cand, dict):
435	                rejected.append({"title": str(cand), "reason": "not a dict"})
436	                continue
437	            title = (cand.get("title") or "").strip()
438	            if not title:
439	                rejected.append({"title": "", "reason": "missing title"})
440	                continue
441	            if cand.get("role") and cand["role"] not in VALID_ROLES:
442	                rejected.append({
443	                    "title": title,
444	                    "reason": f"invalid role '{cand['role']}', valid: {sorted(VALID_ROLES)}",
445	                })
446	                continue
447	
448	            existing_key = _find_existing_key(existing, cand)
449	            if existing_key:
450	                # Merge — fill empty fields, keep verified=True if either is True
451	                existing[existing_key] = _merge_paper(existing[existing_key], cand)
452	                merged.append(existing_key)
453	                continue
454	
455	            # New entry — assign a bibtex_key if missing, dedupe within file
456	            key = cand.get("bibtex_key") or _generate_bibtex_key(cand)
457	            base_key = key
458	            suffix = 1
459	            while key in existing:
460	                suffix += 1
461	                key = f"{base_key}_{suffix}"
462	
463	            entry = {
464	                "title": title,
465	                "authors": cand.get("authors") or [],
466	                "year": cand.get("year"),
467	                "venue": cand.get("venue") or "",
468	                "url": cand.get("url") or "",
469	                "doi": cand.get("doi") or "",
470	                "bibtex_key": key,
471	                "category": cand.get("category") or "",
472	                "role": cand.get("role") or "",
473	                "relevance": cand.get("relevance") or "",
474	                "abstract": cand.get("abstract") or "",
475	                "semantic_scholar_id": cand.get("semantic_scholar_id") or "",
476	                "verified": bool(cand.get("verified", False)),
477	                "added_by": cand.get("added_by") or added_by or "",
478	                "added_at": cand.get("added_at") or now,
479	            }
480	            # Optional source_idea_id (global map only) — keep if present
481	            if cand.get("source_idea_id"):
482	                entry["source_idea_id"] = cand["source_idea_id"]
483	
484	            existing[key] = entry
485	            added.append(key)
486	
487	    data = _read_modify_write(get_literature_map_path(project), _apply)
488	
489	    return ToolResult(success=True, data={
490	        "added": added,
491	        "merged": merged,
492	        "rejected": rejected,
493	        "total_papers": data["meta"]["total_papers"],
494	    })
495	
496	
497	def update_literature_category(
498	    paper_key: str,
499	    project: str | None = None,
500	    category: str | None = None,
501	    role: str | None = None,
502	    relevance: str | None = None,
503	    verified: bool | None = None,
504	) -> ToolResult:
505	    """Update a single paper's classification fields.
506	
507	    Only the fields you pass are changed — others are left intact. This is
508	    the preferred path for "re-classify this paper after reading it" or
509	    "mark verified=true after OpenAlex check" — it's smaller than rewriting
510	    the whole entry via add_to_literature_map.
511	
512	    Args:
513	        paper_key: The YAML key of the paper (e.g. "vaswani2017attention").
514	        project: Project name — None updates the global map.
515	        category: New category key (must match a categories[].key, or empty).
516	        role: New role (must be in VALID_ROLES, or empty to clear).
517	        relevance: One-line relevance description.
518	        verified: Mark verified/unverified (e.g. after OpenAlex check).
519	
520	    Returns:
521	        ToolResult.data = {"paper_key", "updated_fields": {...}}
522	        ToolResult.error if paper_key not found or role/category invalid.
523	    """
524	    if role is not None and role and role not in VALID_ROLES:
525	        return ToolResult(
526	            success=False,
527	            error=f"invalid role '{role}', valid: {sorted(VALID_ROLES)}",
528	        )
529	
530	    updated: dict[str, Any] = {}
531	    not_found = {"miss": False}
532	
533	    def _apply(data: dict) -> None:
534	        papers = data.setdefault("papers", {})
535	        if paper_key not in papers:
536	            not_found["miss"] = True
537	            return
538	        entry = papers[paper_key]
539	        if category is not None:
540	            entry["category"] = category
541	            updated["category"] = category
542	        if role is not None:
543	            entry["role"] = role
544	            updated["role"] = role
545	        if relevance is not None:
546	            entry["relevance"] = relevance
547	            updated["relevance"] = relevance
548	        if verified is not None:
549	            entry["verified"] = bool(verified)
550	            updated["verified"] = bool(verified)
551	
552	    _read_modify_write(get_literature_map_path(project), _apply)
553	
554	    if not_found["miss"]:
555	        return ToolResult(
556	            success=False,
557	            error=f"paper_key '{paper_key}' not found in literature_map",
558	        )
559	    return ToolResult(success=True, data={
560	        "paper_key": paper_key,
561	        "updated_fields": updated,
562	    })
563	
564	
565	def upsert_category(
566	    project: str | None = None,
567	    key: str = "",
568	    name: str = "",
569	    narrative: str = "",
570	) -> ToolResult:
571	    """Add or update a category entry in the categories[] list.
572	
573	    Categories define the Related Work subsection structure. A paper's
574	    ``category`` field references one of these by ``key``.
575	
576	    Args:
577	        project: Project name — None edits the global map.
578	        key: Category slug (e.g. "attention_mechanisms"). Required.
579	        name: Human-readable name (e.g. "Attention Mechanisms"). Required for new.
580	        narrative: One-line description of the category's narrative arc.
581	
582	    Returns:
583	        ToolResult.data = {"key", "action": "added"|"updated"}.
584	    """
585	    if not key:
586	        return ToolResult(success=False, error="key is required")
587	
588	    state = {"action": "added"}
589	
590	    def _apply(data: dict) -> None:
591	        cats = data.setdefault("categories", [])
592	        for c in cats:
593	            if c.get("key") == key:
594	                if name:
595	                    c["name"] = name
596	                if narrative:
597	                    c["narrative"] = narrative
598	                state["action"] = "updated"
599	                return
600	        cats.append({"key": key, "name": name or key, "narrative": narrative})
601	
602	    _read_modify_write(get_literature_map_path(project), _apply)
603	    return ToolResult(success=True, data={"key": key, "action": state["action"]})
604	
605	
606	def seed_literature_map(
607	    project: str,
608	    seed_papers: Iterable[dict],
609	    source_idea_id: str = "",
610	) -> ToolResult:
611	    """Bulk-seed a new project's literature_map from an idea's accumulated papers.
612	
613	    Called by the idea→project bootstrap hook. Each seed paper is added with
614	    ``added_by="idea_generator"`` so downstream consumers can distinguish
615	    seed papers from those discovered during research.
616	
617	    Args:
618	        project: Project name (required — seeding without a project is the
619	                 global map case, handled by add_to_literature_map directly).
620	        seed_papers: Iterable of paper dicts (same schema as add_to_literature_map).
621	        source_idea_id: Idea ID these papers came from. Stamped on entries so
622	                        a future "re-seed from idea" can find them.
623	
624	    Returns:
625	        Same shape as add_to_literature_map.
626	    """
627	    if not project:
628	        return ToolResult(success=False, error="project is required for seed_literature_map")
629	
630	    seeds = []
631	    for p in seed_papers:
632	        if not isinstance(p, dict):
633	            continue
634	        p2 = dict(p)
635	        if source_idea_id:
636	            p2.setdefault("source_idea_id", source_idea_id)
637	        seeds.append(p2)
638	
639	    return add_to_literature_map(
640	        project=project, papers=seeds, added_by="idea_generator",
641	    )
642	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfd08f5f-0037-4faa-a37d-1a01d8d5a7b4",
  "isSidechain": true,
  "promptId": "2c0f4d57-045f-436c-bd98-ba48fb6b2b34",
  "agentId": "a3a7427bd484b01d4",
  "type": "user",
  "uuid": "e3ccbea9-24f4-4659-8705-6dbfbb1a667d",
  "sourceToolAssistantUUID": "dfd08f5f-0037-4faa-a37d-1a01d8d5a7b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-21T03:15:05.231Z_

Let me search for the literature_map.yaml file in the project directory:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3ccbea9-24f4-4659-8705-6dbfbb1a667d",
  "isSidechain": true,
  "agentId": "a3a7427bd484b01d4",
  "requestId": "req_011CbEzB4trpM8yKrPjukLqp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "24a94824-6483-48af-bc19-9c42fb4377a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SYoSbc2rwd8uP4E3dSi3MJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8858,
      "cache_read_input_tokens": 25345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8858,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 8 · 2026-05-21T03:15:05.880Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012C1ZdZohVB6zUBCMvRfLp4`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -name \"literature_map.yaml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24a94824-6483-48af-bc19-9c42fb4377a8",
  "isSidechain": true,
  "agentId": "a3a7427bd484b01d4",
  "requestId": "req_011CbEzB4trpM8yKrPjukLqp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4a4660d4-9de1-4036-b569-40af661bb14b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SYoSbc2rwd8uP4E3dSi3MJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8858,
      "cache_read_input_tokens": 25345,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 116,
          "cache_read_input_tokens": 25345,
          "cache_creation_input_tokens": 8858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8858,
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

_source line 9 · 2026-05-21T03:15:06.352Z_

<details><summary>↩ Tool result · `toolu_012C1ZdZohVB6zUBCMvRfLp4`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a4660d4-9de1-4036-b569-40af661bb14b",
  "isSidechain": true,
  "promptId": "2c0f4d57-045f-436c-bd98-ba48fb6b2b34",
  "agentId": "a3a7427bd484b01d4",
  "type": "user",
  "uuid": "e3be2ceb-ac5e-4266-a070-d7a8ed7a3337",
  "sourceToolAssistantUUID": "4a4660d4-9de1-4036-b569-40af661bb14b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-21T03:15:07.537Z_

Now let me read the correct file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3be2ceb-ac5e-4266-a070-d7a8ed7a3337",
  "isSidechain": true,
  "agentId": "a3a7427bd484b01d4",
  "requestId": "req_011CbEzBH37NN7wNcNJvkLqj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f19698b6-3349-4231-a4a0-9dc282548397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tq1ozMJcz4zQ6oXApSCJeV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 34203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 166,
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

_source line 11 · 2026-05-21T03:15:07.783Z_

<details open><summary>🔧 Tool call — Read · `toolu_015wrTCjeQq4W52ZAspxNSY7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f19698b6-3349-4231-a4a0-9dc282548397",
  "isSidechain": true,
  "agentId": "a3a7427bd484b01d4",
  "requestId": "req_011CbEzBH37NN7wNcNJvkLqj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "57760936-d599-4dad-be3c-e59180a8efac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tq1ozMJcz4zQ6oXApSCJeV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 34203,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 99,
          "cache_read_input_tokens": 34203,
          "cache_creation_input_tokens": 166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 166,
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

_source line 12 · 2026-05-21T03:15:07.805Z_

<details><summary>↩ Tool result · `toolu_015wrTCjeQq4W52ZAspxNSY7`</summary>

```text
1	categories:
2	- key: contamination_detection
3	  name: Benchmark Contamination Detection
4	  narrative: Methods for detecting training data contamination in LLM benchmarks,
5	    including RL-robust approaches
6	- key: irt_equating
7	  name: IRT Methodology & Equating
8	  narrative: Item Response Theory models, calibration, equating, and their application
9	    to LLM evaluation
10	- key: benchmark_design
11	  name: Dynamic Benchmark Design
12	  narrative: Approaches for creating contamination-resistant or self-updating benchmarks
13	- key: dif_methodology
14	  name: DIF Statistical Methods
15	  narrative: Differential Item Functioning detection methods, power analysis, and
16	    small-sample strategies
17	- key: item_generation
18	  name: Automated Item Generation
19	  narrative: LLM-based test item generation with difficulty control and psychometric
20	    validation
21	meta:
22	  last_updated: '2026-05-21T02:29:19.657Z'
23	  total_papers: 21
24	papers:
25	  balloccu2024leak:
26	    abstract: ''
27	    added_at: '2026-05-21T01:40:37.987Z'
28	    added_by: literature-gap-fill
29	    authors:
30	    - Balloccu, S.
31	    - Schmidtova, P.
32	    - Lango, M.
33	    - Dusek, O.
34	    bibtex_key: balloccu2024leak
35	    category: contamination_detection
36	    doi: 10.18653/v1/2024.eacl-long.5
37	    relevance: Systematic survey of data leakage in closed-source LLMs covering 255
38	      papers and 263 benchmarks; establishes scope of contamination problem motivating
39	      our detection approach
40	    role: foundation
41	    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056
42	    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in
43	      Closed-Source LLMs'
44	    url: https://arxiv.org/abs/2402.03927
45	    venue: EACL 2024
46	    verified: true
47	    year: 2024
48	  belzak2020smallsample:
49	    abstract: ''
50	    added_at: '2026-05-20T17:30:00.000Z'
51	    added_by: director
52	    authors:
53	    - Belzak, W.
54	    bibtex_key: belzak2020smallsample
55	    category: dif_methodology
56	    doi: ''
57	    relevance: Parsimonious logistic regression with sum scores outperforms complex
58	      IRT models for DIF detection in small samples; directly applicable to our N=50-80
59	      model cohorts
60	    role: method-component
61	    semantic_scholar_id: ''
62	    title: Testing Differential Item Functioning in Small Samples
63	    url: ''
64	    venue: Multivariate Behavioral Research
65	    verified: false
66	    year: 2020
67	  dekoninck2024constat:
68	    abstract: ''
69	    added_at: '2026-05-21T01:40:37.987Z'
70	    added_by: literature-gap-fill
71	    authors:
72	    - Dekoninck, J.
73	    - Mueller, M. N.
74	    - Vechev, M.
75	    bibtex_key: dekoninck2024constat
76	    category: contamination_detection
77	    doi: ''
78	    relevance: Performance-based contamination detection via perturbation analysis;
79	      closest methodological parallel to our DIF approach in using behavioral patterns
80	      rather than memorization signals
81	    role: direct-competitor
82	    semantic_scholar_id: ''
83	    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'
84	    url: https://arxiv.org/abs/2405.16281
85	    venue: NeurIPS 2024
86	    verified: true
87	    year: 2024
88	  golchin2024timetravel:
89	    abstract: ''
90	    added_at: '2026-05-21T01:40:37.987Z'
91	    added_by: literature-gap-fill
92	    authors:
93	    - Golchin, S.
94	    - Surdeanu, M.
95	    bibtex_key: golchin2024timetravel
96	    category: contamination_detection
97	    doi: ''
98	    relevance: Instance-level contamination detection via guided completion prompts;
99	      baseline approach for individual-item detection that our group-level DIF method
100	      extends
101	    role: method-component
102	    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404
103	    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'
104	    url: https://arxiv.org/abs/2308.08493
105	    venue: ICLR 2024
106	    verified: true
107	    year: 2024
108	  hardy2026scalability:
109	    abstract: ''
110	    added_at: '2026-05-20T17:30:00.000Z'
111	    added_by: director
112	    authors:
113	    - Hardy, M.
114	    - Gilbert, J.
115	    - Domingue, B.
116	    bibtex_key: hardy2026scalability
117	    category: irt_equating
118	    doi: 10.48550/arXiv.2603.24999
119	    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform
120	      IRT item diagnostics; lightweight pre-filter for item quality before our parametric
121	      calibration
122	    role: method-component
123	    semantic_scholar_id: ''
124	    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients
125	    url: https://arxiv.org/abs/2603.24999
126	    venue: arXiv
127	    verified: true
128	    year: 2026
129	  kim2019fpc:
130	    abstract: ''
131	    added_at: '2026-05-20T17:30:00.000Z'
132	    added_by: director
133	    authors:
134	    - Kim, S.
135	    - Kolen, M.
136	    bibtex_key: kim2019fpc
137	    category: irt_equating
138	    doi: ''
139	    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full
140	      calibration; core methodology for our bifactor IRT equating with anchor items
141	    role: method-component
142	    semantic_scholar_id: ''
143	    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data
144	    url: ''
145	    venue: Applied Measurement in Education
146	    verified: false
147	    year: 2019
148	  li2024contamination:
149	    abstract: ''
150	    added_at: '2026-05-21T01:40:37.987Z'
151	    added_by: literature-gap-fill
152	    authors:
153	    - Li, Y.
154	    - Guo, Y.
155	    - Guerin, F.
156	    - Lin, C.
157	    bibtex_key: li2024contamination
158	    category: contamination_detection
159	    doi: 10.18653/v1/2024.findings-emnlp.30
160	    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks
161	      via Common Crawl matching; primary ground-truth comparison for our DIF-based
162	      contamination detection
163	    role: foundation
164	    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0
165	    title: An Open-Source Data Contamination Report for Large Language Models
166	    url: https://aclanthology.org/2024.findings-emnlp.30/
167	    venue: Findings of EMNLP 2024
168	    verified: true
169	    year: 2024
170	  liang2026dvd:
171	    abstract: ''
172	    added_at: '2026-05-20T17:30:00.000Z'
173	    added_by: director
174	    authors:
175	    - Liang, R.
176	    bibtex_key: liang2026dvd
177	    category: contamination_detection
178	    doi: ''
179	    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74
180	      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under
181	      RL training
182	    role: direct-competitor
183	    semantic_scholar_id: ''
184	    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'
185	    url: https://arxiv.org/abs/2601.04895
186	    venue: arXiv
187	    verified: true
188	    year: 2026
189	  polo2026growingpains:
190	    abstract: ''
191	    added_at: '2026-05-20T17:30:00.000Z'
192	    added_by: director
193	    authors:
194	    - Habba, E.
195	    - Itzhak, I.
196	    - Yehudai, A.
197	    - Perlitz, Y.
198	    - Bandel, E.
199	    - Shmueli-Scheuer, M.
200	    - Choshen, L.
201	    - Stanovsky, G.
202	    bibtex_key: polo2026growingpains
203	    category: irt_equating
204	    doi: 10.48550/arXiv.2604.12843
205	    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100
206	      anchor items for extensible evaluation (rho>=0.9); addresses score comparability
207	      but NOT contamination detection or item regeneration
208	    role: direct-competitor
209	    semantic_scholar_id: ''
210	    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter
211	      Calibration'
212	    url: https://arxiv.org/abs/2604.12843
213	    venue: arXiv
214	    verified: true
215	    year: 2026
216	  polo2026psnirt:
217	    abstract: ''
218	    added_at: '2026-05-20T17:30:00.000Z'
219	    added_by: director
220	    authors:
221	    - Zhou, H.
222	    - Huang, H.
223	    - Zhao, Z.
224	    - Han, L.
225	    - Wang, H.
226	    - Chen, K.
227	    - Yang, M.
228	    - Bao, W.
229	    - Dong, J.
230	    - Xu, B.
231	    - Zhu, C.
232	    - Cao, H.
233	    - Zhao, T.
234	    bibtex_key: polo2026psnirt
235	    category: irt_equating
236	    doi: ''
237	    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published
238	      IRT parameters for MMLU we can use in semi-synthetic validation
239	    role: method-component
240	    semantic_scholar_id: ''
241	    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item
242	      Response Theory
243	    url: https://arxiv.org/abs/2505.15055
244	    venue: AAAI 2026
245	    verified: true
246	    year: 2026
247	  shi2024mink:
248	    abstract: ''
249	    added_at: '2026-05-21T01:40:37.987Z'
250	    added_by: literature-gap-fill
251	    authors:
252	    - Shi, W.
253	    - Ajith, A.
254	    - Xia, M.
255	    - Huang, Y.
256	    - Liu, D.
257	    - Blevins, T.
258	    - Chen, D.
259	    - Zettlemoyer, L.
260	    bibtex_key: shi2024mink
261	    category: contamination_detection
262	    doi: ''
263	    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining
264	      data detection; key baseline whose limitations under RL training motivate our
265	      DIF-based alternative
266	    role: foundation
267	    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a
268	    title: Detecting Pretraining Data from Large Language Models
269	    url: https://arxiv.org/abs/2310.16789
270	    venue: ICLR 2024
271	    verified: true
272	    year: 2024
273	  tao2026selfcritique:
274	    abstract: ''
275	    added_at: '2026-05-20T17:30:00.000Z'
276	    added_by: director
277	    authors:
278	    - Tao, Y.
279	    bibtex_key: tao2026selfcritique
280	    category: contamination_detection
281	    doi: ''
282	    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse
283	      detection, but remains individual-model-level; our DIF is group-level and complementary
284	    role: direct-competitor
285	    semantic_scholar_id: ''
286	    title: Detecting Data Contamination from Reinforcement Learning Post-training
287	      for Large Language Models
288	    url: https://arxiv.org/abs/2510.09259
289	    venue: ICLR 2026
290	    verified: true
291	    year: 2026
292	  wang2026fragility:
293	    abstract: ''
294	    added_at: '2026-05-20T17:30:00.000Z'
295	    added_by: director
296	    authors:
297	    - Wang, H.
298	    - Li, H.
299	    - Ko, B.
300	    - Zhang, H.
301	    bibtex_key: wang2026fragility
302	    category: contamination_detection
303	    doi: ''
304	    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp
305	      AUROC degradation), motivating our DIF-based approach which operates on behavioral
306	      patterns immune to NLL smoothing
307	    role: foundation
308	    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3
309	    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models
310	    url: https://arxiv.org/abs/2510.02386
311	    venue: ICLR 2026
312	    verified: true
313	    year: 2026
314	  white2025livebench:
315	    abstract: ''
316	    added_at: '2026-05-20T17:30:00.000Z'
317	    added_by: director
318	    authors:
319	    - White, C.
320	    bibtex_key: white2025livebench
321	    category: benchmark_design
322	    doi: ''
323	    relevance: Monthly-updated contamination-free benchmark with objective scoring;
324	      no difficulty calibration or psychometric equivalence across updates
325	    role: direct-competitor
326	    semantic_scholar_id: ''
327	    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'
328	    url: ''
329	    venue: ICLR 2025
330	    verified: false
331	    year: 2025
332	  zhang2024gsm1k:
333	    abstract: ''
334	    added_at: '2026-05-20T17:30:00.000Z'
335	    added_by: director
336	    authors:
337	    - Zhang, H.
338	    bibtex_key: zhang2024gsm1k
339	    category: contamination_detection
340	    doi: ''
341	    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides
342	      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4
343	      logits) critical for our DIF power analysis
344	    role: foundation
345	    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f
346	    title: A Careful Examination of Large Language Model Performance on Grade School
347	      Arithmetic
348	    url: https://arxiv.org/abs/2405.00332
349	    venue: arXiv
350	    verified: true
351	    year: 2024
352	  zhang2024minkpp:
353	    abstract: ''
354	    added_at: '2026-05-21T01:40:37.987Z'
355	    added_by: literature-gap-fill
356	    authors:
357	    - Zhang, J.
358	    - Sun, J.
359	    - Yeats, E.
360	    - Ouyang, Y.
361	    - Kuo, M.
362	    - Zhang, J.
363	    - Yang, H.
364	    - Li, H.
365	    bibtex_key: zhang2024minkpp
366	    category: contamination_detection
367	    doi: ''
368	    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key
369	      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our
370	      DIF-based alternative
371	    role: direct-competitor
372	    semantic_scholar_id: ''
373	    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large
374	      Language Models'
375	    url: https://arxiv.org/abs/2404.02936
376	    venue: arXiv
377	    verified: true
378	    year: 2024
379	  lalor2019irt:
380	    title: 'Learning Latent Parameters without Human Response Patterns: Item Response
381	      Theory with Artificial Crowds'
382	    authors:
383	    - Lalor, J.
384	    - Wu, H.
385	    - Yu, H.
386	    year: 2019
387	    venue: EMNLP-IJCNLP 2019
388	    url: https://aclanthology.org/D19-1434/
389	    doi: 10.18653/v1/D19-1434
390	    bibtex_key: lalor2019irt
391	    category: irt_equating
392	    role: foundation
393	    relevance: Pioneering application of IRT to NLP evaluation using artificial crowds
394	      of DNN models; establishes that IRT parameters from machine response patterns
395	      correlate with human-calibrated parameters
396	    abstract: ''
397	    semantic_scholar_id: df6cd8a8d836e75690141deb732f6d19f0176a2e
398	    verified: true
399	    added_by: literature-gap-fill
400	    added_at: '2026-05-21T02:29:19.632Z'
401	  vania2021irt:
402	    title: Comparing Test Sets with Item Response Theory
403	    authors:
404	    - Vania, C.
405	    - Htut, P.M.
406	    - Huang, W.
407	    - Mungra, D.
408	    - Pang, R.Y.
409	    - Phang, J.
410	    - Liu, H.
411	    - Cho, K.
412	    - Bowman, S.R.
413	    year: 2021
414	    venue: ACL 2021
415	    url: https://aclanthology.org/2021.acl-long.92/
416	    doi: 10.18653/v1/2021.acl-long.92
417	    bibtex_key: vania2021irt
418	    category: irt_equating
419	    role: foundation
420	    relevance: IRT-based analysis of NLU benchmark discriminability; shows which test
421	      sets remain effective at differentiating strong models and which are saturated
422	    abstract: ''
423	    semantic_scholar_id: 4ca39cf99747b8962fe37e7e025e284872df3425
424	    verified: true
425	    added_by: literature-gap-fill
426	    added_at: '2026-05-21T02:29:19.632Z'
427	  li2025atlas:
428	    title: 'Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static
429	      Benchmarks'
430	    authors:
431	    - Li, P.
432	    - Tang, X.
433	    - Chen, S.
434	    - Cheng, Y.
435	    - Metoyer, R.
436	    - Hua, T.
437	    - Chawla, N.V.
438	    year: 2025
439	    venue: arXiv
440	    url: https://arxiv.org/abs/2511.04689
441	    doi: 10.48550/arXiv.2511.04689
442	    bibtex_key: li2025atlas
443	    category: irt_equating
444	    role: method-component
445	    relevance: IRT-based adaptive testing framework (ATLAS) reduces benchmark items
446	      by 90% while preserving ability estimates; demonstrates IRT enables efficient
447	      LLM evaluation
448	    abstract: ''
449	    semantic_scholar_id: 087ce2837a0d5562bc95a40e77a327a6d033366c
450	    verified: true
451	    added_by: literature-gap-fill
452	    added_at: '2026-05-21T02:29:19.632Z'
453	  chen2025irtnet:
454	    title: Learning Compact Representations of LLM Abilities via Item Response Theory
455	    authors:
456	    - Chen, J.
457	    - Wang, C.
458	    - Zhang, G.
459	    - Ye, P.
460	    - Bai, L.
461	    - Hu, W.
462	    - Qu, Y.
463	    - Hu, S.
464	    year: 2025
465	    venue: arXiv
466	    url: https://arxiv.org/abs/2510.00844
467	    doi: 10.48550/arXiv.2510.00844
468	    bibtex_key: chen2025irtnet
469	    category: irt_equating
470	    role: method-component
471	    relevance: Multidimensional IRT with MoE network for learning LLM ability vectors
472	      and query discrimination/difficulty; demonstrates IRT-based model routing and
473	      benchmark prediction
474	    abstract: ''
475	    semantic_scholar_id: ''
476	    verified: true
477	    added_by: literature-gap-fill
478	    added_at: '2026-05-21T02:29:19.632Z'
479	  choi2026llmjudgeirt:
480	    title: Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory
481	    authors:
482	    - Choi, J.
483	    - Park, S.
484	    - Cho, C.
485	    - Park, H.
486	    - Kim, B.
487	    year: 2026
488	    venue: arXiv
489	    url: https://arxiv.org/abs/2602.00521
490	    doi: 10.48550/arXiv.2602.00521
491	    bibtex_key: choi2026llmjudgeirt
492	    category: irt_equating
493	    role: method-component
494	    relevance: Applies IRT Graded Response Model to diagnose LLM judge reliability;
495	      extends IRT application beyond benchmark scoring to evaluation pipeline quality
496	      assessment
497	    abstract: ''
498	    semantic_scholar_id: 4fc931a456c8162716deadbc9db6fd770189e632
499	    verified: true
500	    added_by: literature-gap-fill
501	    added_at: '2026-05-21T02:29:19.632Z'
502	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57760936-d599-4dad-be3c-e59180a8efac",
  "isSidechain": true,
  "promptId": "2c0f4d57-045f-436c-bd98-ba48fb6b2b34",
  "agentId": "a3a7427bd484b01d4",
  "type": "user",
  "uuid": "7616c191-3546-4676-8248-6db35007d1a5",
  "sourceToolAssistantUUID": "57760936-d599-4dad-be3c-e59180a8efac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T03:15:15.626Z_

Perfect! Now I have both pieces of information. Here's my response:

## Literature Map File Contents

The file `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml` contains a comprehensive literature database with:

**Metadata:**
- Total papers: 21
- Last updated: 2026-05-21T02:29:19.657Z

**5 Categories:**
1. **contamination_detection** - Benchmark Contamination Detection
2. **irt_equating** - IRT Methodology & Equating
3. **benchmark_design** - Dynamic Benchmark Design
4. **dif_methodology** - DIF Statistical Methods
5. **item_generation** - Automated Item Generation

**21 Papers** organized by these categories, including foundational works (Balloccu 2024, Li 2024, Shi 2024, Zhang 2024, Wang 2026), method-components (Hardy 2026, Kim 2019, Lalor 2019, Li 2025, Chen 2025, Choi 2026), and direct competitors (Dekoninck 2024, Liang 2026, Polo 2026, Tao 2026, White 2025, Zhang 2024 Min-K++).

Each entry contains: title, authors, year, venue, URL, DOI, bibtex_key, category, role, relevance statement, verification status, and semantic scholar ID where available.

---

## Literature.py Function Signature

Found at `/home/ubuntu/agent-ml-research/core/tools/literature.py`

The **`add_to_literature_map`** function signature is:

```python
def add_to_literature_map(
    project: str | None = None,
    papers: Iterable[dict] | None = None,
    added_by: str = "",
) -> ToolResult:
```

**Parameters:**
- `project` (str | None): Project name — None writes to the global (idea-phase) map
- `papers` (Iterable[dict] | None): Iterable of paper dicts with recognized fields: title, authors (list[str]), year, venue, url, doi, bibtex_key, category, role, relevance, abstract, semantic_scholar_id, source_idea_id, verified. Missing bibtex_key is auto-generated
- `added_by` (str): Free-form tag for provenance ("paper-research", "idea-generator", "user", etc.)

**Returns:** 
- `ToolResult.data` with: added (list of keys), merged (list of keys), rejected (list of dicts with title/reason), total_papers (int)

The function handles deduplication by DOI exact match, then normalized title match, and merges existing entries field-by-field without overwriting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7616c191-3546-4676-8248-6db35007d1a5",
  "isSidechain": true,
  "agentId": "a3a7427bd484b01d4",
  "requestId": "req_011CbEzBPRazJZvXej4rcYWt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f788e416-d4bd-4fdf-9869-81264c05a147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "365d7717-8f52-4a32-a668-80e621d578d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W8PAKMuAJtqcK4zWdVnhuF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6746,
      "cache_read_input_tokens": 34369,
      "output_tokens": 683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6746
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 683,
          "cache_read_input_tokens": 34369,
          "cache_creation_input_tokens": 6746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6746,
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
