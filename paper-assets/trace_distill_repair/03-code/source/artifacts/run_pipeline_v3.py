"""Pipeline v3: skip bare repos, setup directly, collect traces, segment."""
import json
import logging
import os
import signal
import subprocess
import sys
import time

sys.path.insert(0, "/root/trace_distill_repair")

from bugsinpy_setup import BugsInPySetup
from trace_collector import TraceCollector
from structural_segmenter import StructuralSegmenter
from line_segmenter import LineSegmenter
from dtd_types import serialize_segment

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)
sys.stdout.reconfigure(line_buffering=True)

WORKSPACE = "/root/trace_distill_repair/bugsinpy_workspace"
OUTPUT_DIR = "/root/trace_distill_repair/pipeline_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

setup = BugsInPySetup(workspace_dir=WORKSPACE)
setup._ensure_repo()

# Build project -> url mapping
project_urls = {}
for project, bug_id, _ in setup.CANDIDATE_BUGS:
    if project in project_urls:
        continue
    bug_dir = os.path.join(setup.repo_dir, "projects", project, "bugs", str(bug_id))
    bug_info = setup._read_bug_info(bug_dir)
    repo_url = bug_info.get("github_url", "")
    if not repo_url:
        pinfo = os.path.join(setup.repo_dir, "projects", project, "project.info")
        if os.path.isfile(pinfo):
            with open(pinfo) as f:
                for line in f:
                    if "github_url" in line.lower():
                        _, _, url = line.partition("=")
                        repo_url = url.strip().strip('"')
                        break
    if repo_url:
        project_urls[project] = repo_url

# Phase 1: Setup instances
instances = []
setup_results = {"success": [], "failed": []}
REPO_POOL = os.path.join(WORKSPACE, "repo_pool")

logger.info("=== PHASE 1: Setting up %d BugsInPy instances ===", len(setup.CANDIDATE_BUGS))
for project, bug_id, desc in setup.CANDIDATE_BUGS:
    key = f"{project}_{bug_id}"
    work_dir = os.path.join(WORKSPACE, "instances", key)
    buggy_dir = os.path.join(work_dir, "buggy")
    bug_dir = os.path.join(setup.repo_dir, "projects", project, "bugs", str(bug_id))

    if os.path.isdir(buggy_dir) and os.path.isdir(os.path.join(buggy_dir, ".git")):
        bug_info = setup._read_bug_info(bug_dir)
        test_cmd = bug_info.get("test_command", "python -m pytest")
        instances.append({
            "project": project, "bug_id": bug_id,
            "buggy_dir": buggy_dir, "test_command": test_cmd, "bug_info": bug_info,
        })
        setup_results["success"].append(key)
        logger.info("SKIP %s (exists)", key)
        continue

    os.makedirs(work_dir, exist_ok=True)
    try:
        bug_info = setup._read_bug_info(bug_dir)
        commit_id = bug_info.get("buggy_commit_id", "")
        test_cmd = bug_info.get("test_command", "python -m pytest")
        if not commit_id:
            raise ValueError(f"No buggy commit ID for {key}")

        repo_url = project_urls.get(project, "")
        if not repo_url:
            raise ValueError(f"No URL for {project}")

        # Try local bare clone first, then remote
        pool_dir = os.path.join(REPO_POOL, project)
        if os.path.isfile(os.path.join(pool_dir, "HEAD")):
            clone_src = pool_dir
            clone_timeout = 60
        else:
            clone_src = repo_url
            clone_timeout = 300

        # Use process group so timeout kills all children
        if os.path.isdir(buggy_dir):
            subprocess.run(["rm", "-rf", buggy_dir])

        proc = subprocess.Popen(
            ["git", "clone", clone_src, buggy_dir],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            preexec_fn=os.setsid
        )
        try:
            proc.communicate(timeout=clone_timeout)
            if proc.returncode != 0:
                raise subprocess.CalledProcessError(proc.returncode, "git clone")
        except subprocess.TimeoutExpired:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
            proc.wait()
            raise TimeoutError(f"Clone timed out after {clone_timeout}s")

        subprocess.run(["git", "checkout", commit_id],
                       check=True, capture_output=True, cwd=buggy_dir)

        instances.append({
            "project": project, "bug_id": bug_id,
            "buggy_dir": buggy_dir, "test_command": test_cmd, "bug_info": bug_info,
        })
        setup_results["success"].append(key)
        logger.info("OK setup %s", key)
    except Exception as e:
        setup_results["failed"].append({"key": key, "error": str(e)[:200]})
        logger.error("FAIL setup %s: %s", key, str(e)[:200])

logger.info("Phase 1 done: %d/%d success", len(setup_results["success"]), len(setup.CANDIDATE_BUGS))

# Phase 2: Trace collection
collector = TraceCollector()
trace_results = {"success": [], "failed": [], "traces": {}}

logger.info("=== PHASE 2: Collecting traces for %d instances ===", len(instances))
for inst in instances:
    key = f"{inst['project']}_{inst['bug_id']}"
    buggy_dir = inst["buggy_dir"]
    test_cmd = inst["test_command"]
    try:
        main_py = None
        for root, dirs, files in os.walk(buggy_dir):
            if ".git" in dirs:
                dirs.remove(".git")
            for f in sorted(files):
                if f.endswith(".py") and not f.startswith("test_") and f != "setup.py":
                    main_py = os.path.join(root, f)
                    break
            if main_py:
                break

        if not main_py:
            trace_results["failed"].append({"key": key, "error": "No Python file found"})
            logger.error("FAIL trace %s: no Python file", key)
            continue

        events = collector.collect(main_py, test_cmd, timeout=120)

        if events:
            trace_results["success"].append(key)
            trace_results["traces"][key] = events
            trace_file = os.path.join(OUTPUT_DIR, f"{key}_trace.json")
            with open(trace_file, "w") as f:
                json.dump([{
                    "event_type": e.event_type,
                    "function_name": e.function_name,
                    "filename": e.filename,
                    "lineno": e.lineno,
                    "call_depth": e.call_depth,
                } for e in events], f)
            logger.info("OK trace %s: %d events", key, len(events))
        else:
            trace_results["failed"].append({"key": key, "error": "No events collected"})
            logger.warning("FAIL trace %s: 0 events", key)
    except Exception as e:
        trace_results["failed"].append({"key": key, "error": str(e)[:200]})
        logger.error("FAIL trace %s: %s", key, str(e)[:200])

logger.info("Phase 2 done: %d/%d success", len(trace_results["success"]), len(instances))

# Phase 3: Segmentation
struct_seg = StructuralSegmenter()
line_seg = LineSegmenter(window_size=5, stride=5)
seg_results = {"structural": {}, "line": {}}

logger.info("=== PHASE 3: Segmenting traces ===")
for key, events in trace_results["traces"].items():
    try:
        s_segs = struct_seg.segment(events)
        l_segs = line_seg.segment(events)

        seg_results["structural"][key] = {
            "num_segments": len(s_segs),
            "types": {},
        }
        for s in s_segs:
            t = s.segment_type
            seg_results["structural"][key]["types"][t] = seg_results["structural"][key]["types"].get(t, 0) + 1

        seg_results["line"][key] = {"num_segments": len(l_segs)}

        s_file = os.path.join(OUTPUT_DIR, f"{key}_structural_segments.json")
        l_file = os.path.join(OUTPUT_DIR, f"{key}_line_segments.json")
        with open(s_file, "w") as f:
            json.dump([serialize_segment(s) for s in s_segs], f)
        with open(l_file, "w") as f:
            json.dump([serialize_segment(s) for s in l_segs], f)

        logger.info("OK seg %s: structural=%d, line=%d", key, len(s_segs), len(l_segs))
    except Exception as e:
        logger.error("FAIL seg %s: %s", key, e)

# Summary
summary = {
    "phase1_setup": {
        "total": len(setup.CANDIDATE_BUGS),
        "success": len(setup_results["success"]),
        "failed": len(setup_results["failed"]),
        "failed_list": setup_results["failed"],
    },
    "phase2_traces": {
        "total": len(instances),
        "success": len(trace_results["success"]),
        "failed": len(trace_results["failed"]),
        "failed_list": trace_results["failed"],
        "event_counts": {k: len(v) for k, v in trace_results["traces"].items()},
    },
    "phase3_segmentation": seg_results,
    "output_dir": OUTPUT_DIR,
}

with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
    json.dump(summary, f, indent=2)

logger.info("=== FINAL SUMMARY ===")
logger.info("Phase 1: %d/%d", summary["phase1_setup"]["success"], summary["phase1_setup"]["total"])
logger.info("Phase 2: %d/%d", summary["phase2_traces"]["success"], summary["phase2_traces"]["total"])
if trace_results["traces"]:
    avg_events = sum(len(v) for v in trace_results["traces"].values()) / len(trace_results["traces"])
    logger.info("Avg trace events: %.0f", avg_events)
logger.info("Phase 3: %d structural, %d line", len(seg_results["structural"]), len(seg_results["line"]))
logger.info("Output: %s", OUTPUT_DIR)
