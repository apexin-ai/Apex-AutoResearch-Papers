#!/usr/bin/env python3
"""Build a self-contained HTML annotation tool from CSV data."""

import csv
import json
import html
import sys
from pathlib import Path

def main():
    base = Path(__file__).parent

    # Read annotation samples
    with open(base / "annotation_sample_650.csv", "r") as f:
        reader = csv.DictReader(f)
        samples = list(reader)

    # Read mapping data
    with open(base / "annotation_mapping.csv", "r") as f:
        reader = csv.DictReader(f)
        mapping = {r["id"]: r for r in reader}

    # Merge
    data = []
    for s in samples:
        m = mapping.get(s["id"], {})
        data.append({
            "id": int(s["id"]),
            "trajectory_id": s["trajectory_id"],
            "window_idx": int(s["window_idx"]),
            "confidence": int(s["confidence"]),
            "agent_actions": s["agent_actions"],
            "source": s["source"],
            "majority_label": int(m.get("majority_label", -1)),
            "trajectory_outcome": m.get("trajectory_outcome", ""),
            "is_calibration": m.get("is_calibration", "False") == "True",
            "lf_file_diff_delta": int(m.get("lf_file_diff_delta", -1)),
            "lf_command_repetition": int(m.get("lf_command_repetition", -1)),
            "lf_outcome_backpropagation": int(m.get("lf_outcome_backpropagation", -1)),
        })

    data_json = json.dumps(data, ensure_ascii=False)

    # Read annotation guide
    guide_md = (base / "annotation_guide.md").read_text()
    guide_html_content = guide_md.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")

    html_content = HTML_TEMPLATE.replace("__DATA_JSON__", data_json)

    out_path = base / "annotation_tool.html"
    out_path.write_text(html_content, encoding="utf-8")
    print(f"Generated: {out_path}")
    print(f"Samples: {len(data)}, Calibration: {sum(1 for d in data if d['is_calibration'])}")

HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Agent Progress Probe — Annotation Tool</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f5f5f5; color: #333; }

.header { background: #1a1a2e; color: #fff; padding: 12px 24px; display: flex; align-items: center; justify-content: space-between; position: sticky; top: 0; z-index: 100; }
.header h1 { font-size: 18px; font-weight: 600; }
.header-right { display: flex; align-items: center; gap: 16px; }

.annotator-input { background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); color: #fff; padding: 6px 12px; border-radius: 6px; font-size: 14px; width: 140px; }
.annotator-input::placeholder { color: rgba(255,255,255,0.5); }

.progress-bar-container { width: 200px; height: 8px; background: rgba(255,255,255,0.2); border-radius: 4px; overflow: hidden; }
.progress-bar { height: 100%; background: #4ade80; border-radius: 4px; transition: width 0.3s; }
.progress-text { font-size: 13px; color: rgba(255,255,255,0.8); min-width: 80px; text-align: right; }

.toolbar { background: #fff; border-bottom: 1px solid #e0e0e0; padding: 10px 24px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.toolbar select, .toolbar input[type="text"] { padding: 6px 10px; border: 1px solid #d0d0d0; border-radius: 6px; font-size: 13px; background: #fff; }
.toolbar label { font-size: 13px; color: #666; }
.toolbar .spacer { flex: 1; }

.btn { padding: 6px 14px; border: none; border-radius: 6px; font-size: 13px; cursor: pointer; font-weight: 500; transition: all 0.15s; }
.btn-sm { padding: 4px 10px; font-size: 12px; }
.btn-outline { background: transparent; border: 1px solid #d0d0d0; color: #555; }
.btn-outline:hover { background: #f0f0f0; }
.btn-primary { background: #3b82f6; color: #fff; }
.btn-primary:hover { background: #2563eb; }
.btn-success { background: #22c55e; color: #fff; }
.btn-success:hover { background: #16a34a; }
.btn-danger { background: #ef4444; color: #fff; }
.btn-danger:hover { background: #dc2626; }
.btn-export { background: #8b5cf6; color: #fff; }
.btn-export:hover { background: #7c3aed; }

.main { max-width: 1100px; margin: 20px auto; padding: 0 20px; }

.sample-card { background: #fff; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); overflow: hidden; margin-bottom: 20px; }

.sample-header { padding: 16px 20px; border-bottom: 1px solid #f0f0f0; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; }
.sample-id { font-size: 20px; font-weight: 700; color: #1a1a2e; }
.sample-meta { display: flex; gap: 8px; flex-wrap: wrap; }
.badge { display: inline-flex; align-items: center; padding: 3px 10px; border-radius: 12px; font-size: 12px; font-weight: 500; }
.badge-source { background: #e0e7ff; color: #3730a3; }
.badge-confidence { background: #fef3c7; color: #92400e; }
.badge-calibration { background: #fce7f3; color: #9d174d; }
.badge-outcome { background: #ecfdf5; color: #065f46; }

.actions-container { padding: 20px; max-height: 500px; overflow-y: auto; border-bottom: 1px solid #f0f0f0; }
.action-step { margin-bottom: 12px; padding: 10px 14px; border-radius: 8px; font-size: 13px; line-height: 1.6; font-family: "SF Mono", "Fira Code", "Consolas", monospace; white-space: pre-wrap; word-break: break-word; }
.action-step:last-child { margin-bottom: 0; }

.step-thought { background: #f0f9ff; border-left: 3px solid #3b82f6; }
.step-thought .step-label { color: #1d4ed8; font-weight: 600; }

.step-command { background: #1a1a2e; color: #e2e8f0; border-left: 3px solid #a78bfa; }
.step-command .step-label { color: #a78bfa; font-weight: 600; }

.step-output { background: #f8f8f8; border-left: 3px solid #94a3b8; color: #555; }
.step-output .step-label { color: #64748b; font-weight: 600; }

.step-separator { text-align: center; color: #ccc; font-size: 12px; margin: 8px 0; }

.label-section { padding: 20px; display: flex; align-items: center; gap: 16px; justify-content: center; flex-wrap: wrap; }
.label-btn { padding: 14px 40px; border: 3px solid transparent; border-radius: 12px; font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.2s; min-width: 180px; }
.label-btn-progress { background: #dcfce7; color: #166534; border-color: #bbf7d0; }
.label-btn-progress:hover, .label-btn-progress.active { background: #22c55e; color: #fff; border-color: #22c55e; transform: scale(1.05); }
.label-btn-stagnation { background: #fee2e2; color: #991b1b; border-color: #fecaca; }
.label-btn-stagnation:hover, .label-btn-stagnation.active { background: #ef4444; color: #fff; border-color: #ef4444; transform: scale(1.05); }
.label-btn-skip { background: #f3f4f6; color: #6b7280; border-color: #e5e7eb; padding: 10px 24px; font-size: 13px; min-width: auto; }
.label-btn-skip:hover, .label-btn-skip.active { background: #9ca3af; color: #fff; border-color: #9ca3af; }

.nav-section { padding: 16px 20px; border-top: 1px solid #f0f0f0; display: flex; align-items: center; justify-content: space-between; }
.nav-buttons { display: flex; gap: 8px; }
.jump-input { width: 70px; padding: 6px 10px; border: 1px solid #d0d0d0; border-radius: 6px; font-size: 13px; text-align: center; }

.ref-info { padding: 12px 20px; background: #fffbeb; border-top: 1px solid #fde68a; font-size: 12px; color: #92400e; display: none; }
.ref-info.visible { display: block; }
.ref-info table { border-collapse: collapse; width: 100%; }
.ref-info td { padding: 4px 12px; border-bottom: 1px solid #fde68a; }
.ref-info td:first-child { font-weight: 600; width: 180px; }

.lf-vote { display: inline-block; padding: 1px 6px; border-radius: 4px; font-weight: 600; font-size: 11px; }
.lf-progress { background: #dcfce7; color: #166534; }
.lf-stagnation { background: #fee2e2; color: #991b1b; }
.lf-abstain { background: #f3f4f6; color: #9ca3af; }

.shortcuts-help { position: fixed; bottom: 20px; right: 20px; background: #1a1a2e; color: #fff; padding: 12px 16px; border-radius: 10px; font-size: 12px; line-height: 1.8; box-shadow: 0 4px 12px rgba(0,0,0,0.3); z-index: 50; }
.shortcuts-help kbd { background: rgba(255,255,255,0.2); padding: 2px 6px; border-radius: 4px; font-family: monospace; }

.guide-modal { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 200; align-items: center; justify-content: center; }
.guide-modal.active { display: flex; }
.guide-content { background: #fff; border-radius: 12px; max-width: 800px; max-height: 80vh; overflow-y: auto; padding: 32px; margin: 20px; line-height: 1.8; font-size: 14px; }
.guide-content h1 { font-size: 22px; margin-bottom: 16px; }
.guide-content h2 { font-size: 16px; margin: 20px 0 8px; color: #1a1a2e; }
.guide-content h3 { font-size: 14px; margin: 16px 0 6px; }
.guide-content table { border-collapse: collapse; width: 100%; margin: 8px 0; }
.guide-content th, .guide-content td { border: 1px solid #e0e0e0; padding: 8px 12px; text-align: left; font-size: 13px; }
.guide-content th { background: #f5f5f5; }

.stats-panel { background: #fff; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); padding: 20px; margin-bottom: 20px; }
.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 16px; }
.stat-item { text-align: center; }
.stat-value { font-size: 28px; font-weight: 700; color: #1a1a2e; }
.stat-label { font-size: 12px; color: #888; margin-top: 4px; }

.list-view { display: none; }
.list-view.active { display: block; }
.card-view { display: block; }
.card-view.hidden { display: none; }

.list-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.list-table th { background: #f8f8f8; padding: 10px 14px; text-align: left; font-size: 13px; font-weight: 600; border-bottom: 2px solid #e0e0e0; }
.list-table td { padding: 8px 14px; font-size: 13px; border-bottom: 1px solid #f0f0f0; }
.list-table tr:hover { background: #f8faff; cursor: pointer; }
.list-table .label-cell { font-weight: 600; }
.list-table .label-progress { color: #16a34a; }
.list-table .label-stagnation { color: #dc2626; }
.list-table .label-skip { color: #9ca3af; }
.list-table .label-unlabeled { color: #d4d4d4; }

.toast { position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%); background: #1a1a2e; color: #fff; padding: 10px 24px; border-radius: 8px; font-size: 14px; z-index: 300; opacity: 0; transition: opacity 0.3s; pointer-events: none; }
.toast.show { opacity: 1; }

@media (max-width: 768px) {
  .header { flex-direction: column; gap: 8px; }
  .toolbar { flex-direction: column; align-items: stretch; }
  .label-btn { min-width: 140px; padding: 12px 24px; font-size: 14px; }
  .shortcuts-help { display: none; }
}
</style>
</head>
<body>

<div class="header">
  <h1>Agent Progress Probe — Annotation Tool</h1>
  <div class="header-right">
    <input type="text" class="annotator-input" id="annotatorName" placeholder="标注者姓名">
    <div class="progress-bar-container"><div class="progress-bar" id="progressBar"></div></div>
    <span class="progress-text" id="progressText">0/650</span>
  </div>
</div>

<div class="toolbar">
  <label>筛选:</label>
  <select id="filterStatus">
    <option value="all">全部</option>
    <option value="unlabeled">未标注</option>
    <option value="labeled">已标注</option>
    <option value="progress">Progress</option>
    <option value="stagnation">Stagnation</option>
    <option value="skip">跳过</option>
  </select>
  <select id="filterSource">
    <option value="all">全部来源</option>
    <option value="openhands">OpenHands</option>
    <option value="swe-agent">SWE-Agent</option>
  </select>
  <select id="filterConfidence">
    <option value="all">全部置信度</option>
    <option value="0">Conf 0</option>
    <option value="1">Conf 1</option>
    <option value="2">Conf 2</option>
    <option value="3">Conf 3</option>
  </select>
  <label><input type="checkbox" id="filterCalibration"> 仅校准样本</label>
  <div class="spacer"></div>
  <button class="btn btn-outline btn-sm" onclick="toggleView()">📋 列表/卡片切换</button>
  <button class="btn btn-outline btn-sm" onclick="toggleRef()">📎 参考信息</button>
  <button class="btn btn-outline btn-sm" onclick="showGuide()">📖 标注指南</button>
  <button class="btn btn-export btn-sm" onclick="exportCSV()">⬇ 导出 CSV</button>
  <button class="btn btn-outline btn-sm" onclick="importCSV()">⬆ 导入</button>
  <input type="file" id="importFile" accept=".csv,.json" style="display:none" onchange="handleImport(event)">
</div>

<div class="main">
  <div class="stats-panel">
    <div class="stats-grid">
      <div class="stat-item"><div class="stat-value" id="statTotal">650</div><div class="stat-label">总计</div></div>
      <div class="stat-item"><div class="stat-value" id="statLabeled">0</div><div class="stat-label">已标注</div></div>
      <div class="stat-item"><div class="stat-value" id="statProgress">0</div><div class="stat-label">Progress</div></div>
      <div class="stat-item"><div class="stat-value" id="statStagnation">0</div><div class="stat-label">Stagnation</div></div>
      <div class="stat-item"><div class="stat-value" id="statSkip">0</div><div class="stat-label">跳过</div></div>
      <div class="stat-item"><div class="stat-value" id="statRemaining">650</div><div class="stat-label">剩余</div></div>
    </div>
  </div>

  <!-- Card View -->
  <div class="card-view" id="cardView">
    <div class="sample-card" id="sampleCard">
      <div class="sample-header">
        <div>
          <span class="sample-id" id="sampleId">#1</span>
          <span class="sample-meta" id="sampleMeta"></span>
        </div>
        <div id="sampleFilterPos" style="font-size:13px;color:#888;"></div>
      </div>
      <div class="ref-info" id="refInfo"></div>
      <div class="actions-container" id="actionsContainer"></div>
      <div class="label-section">
        <button class="label-btn label-btn-progress" onclick="setLabel('progress')">✓ Progress <kbd style="font-size:11px;opacity:0.7">1</kbd></button>
        <button class="label-btn label-btn-stagnation" onclick="setLabel('stagnation')">✗ Stagnation <kbd style="font-size:11px;opacity:0.7">2</kbd></button>
        <button class="label-btn label-btn-skip" onclick="setLabel('skip')">跳过 <kbd style="font-size:11px;opacity:0.7">3</kbd></button>
      </div>
      <div class="nav-section">
        <div class="nav-buttons">
          <button class="btn btn-outline" onclick="navPrev()">← 上一个 <kbd style="font-size:10px">A</kbd></button>
          <button class="btn btn-outline" onclick="navNext()">下一个 → <kbd style="font-size:10px">D</kbd></button>
          <button class="btn btn-outline" onclick="navNextUnlabeled()">下一个未标注 <kbd style="font-size:10px">S</kbd></button>
        </div>
        <div style="display:flex;align-items:center;gap:8px;">
          <span style="font-size:13px;color:#888;">跳转到 ID:</span>
          <input type="number" class="jump-input" id="jumpInput" min="1" max="650" onkeydown="if(event.key==='Enter')jumpTo()">
          <button class="btn btn-outline btn-sm" onclick="jumpTo()">Go</button>
        </div>
      </div>
    </div>
  </div>

  <!-- List View -->
  <div class="list-view" id="listView">
    <table class="list-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>来源</th>
          <th>置信度</th>
          <th>校准</th>
          <th>Agent Actions (摘要)</th>
          <th>标注</th>
        </tr>
      </thead>
      <tbody id="listBody"></tbody>
    </table>
  </div>
</div>

<div class="shortcuts-help">
  <div><kbd>1</kbd> Progress &nbsp; <kbd>2</kbd> Stagnation &nbsp; <kbd>3</kbd> 跳过</div>
  <div><kbd>A</kbd> 上一个 &nbsp; <kbd>D</kbd> 下一个 &nbsp; <kbd>S</kbd> 下一个未标注</div>
  <div><kbd>R</kbd> 切换参考信息</div>
</div>

<div class="guide-modal" id="guideModal" onclick="if(event.target===this)closeGuide()">
  <div class="guide-content" id="guideContent"></div>
</div>

<div class="toast" id="toast"></div>

<script>
const ALL_DATA = __DATA_JSON__;

let labels = {};        // id -> "progress" | "stagnation" | "skip"
let filteredIds = [];   // current filtered list of data indices
let currentFilterIdx = 0;
let showRef = false;
let isListView = false;

// --- LocalStorage ---
const STORAGE_KEY = "agent_progress_annotation";
const ANNOTATOR_KEY = "agent_progress_annotator";

function saveToStorage() {
  const payload = { labels, annotator: document.getElementById("annotatorName").value, savedAt: new Date().toISOString() };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
}

function loadFromStorage() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (raw) {
    try {
      const payload = JSON.parse(raw);
      labels = payload.labels || {};
      if (payload.annotator) document.getElementById("annotatorName").value = payload.annotator;
    } catch(e) { console.error("Failed to load storage", e); }
  }
  const name = localStorage.getItem(ANNOTATOR_KEY);
  if (name) document.getElementById("annotatorName").value = name;
}

document.getElementById("annotatorName").addEventListener("input", function() {
  localStorage.setItem(ANNOTATOR_KEY, this.value);
  saveToStorage();
});

// --- Filtering ---
function applyFilters() {
  const status = document.getElementById("filterStatus").value;
  const source = document.getElementById("filterSource").value;
  const conf = document.getElementById("filterConfidence").value;
  const calOnly = document.getElementById("filterCalibration").checked;

  filteredIds = [];
  for (let i = 0; i < ALL_DATA.length; i++) {
    const d = ALL_DATA[i];
    const lbl = labels[d.id] || null;

    if (status === "unlabeled" && lbl) continue;
    if (status === "labeled" && !lbl) continue;
    if (status === "progress" && lbl !== "progress") continue;
    if (status === "stagnation" && lbl !== "stagnation") continue;
    if (status === "skip" && lbl !== "skip") continue;
    if (source !== "all" && d.source !== source) continue;
    if (conf !== "all" && d.confidence !== parseInt(conf)) continue;
    if (calOnly && !d.is_calibration) continue;

    filteredIds.push(i);
  }

  if (currentFilterIdx >= filteredIds.length) currentFilterIdx = Math.max(0, filteredIds.length - 1);
  renderCurrent();
  renderList();
  updateStats();
}

// --- Rendering ---
function renderCurrent() {
  if (filteredIds.length === 0) {
    document.getElementById("sampleId").textContent = "无匹配样本";
    document.getElementById("sampleMeta").innerHTML = "";
    document.getElementById("actionsContainer").innerHTML = '<p style="padding:40px;text-align:center;color:#999;">当前筛选条件下无样本</p>';
    document.getElementById("refInfo").innerHTML = "";
    document.getElementById("sampleFilterPos").textContent = "";
    updateLabelButtons(null);
    return;
  }

  const dataIdx = filteredIds[currentFilterIdx];
  const d = ALL_DATA[dataIdx];
  const lbl = labels[d.id] || null;

  document.getElementById("sampleId").textContent = `#${d.id}`;
  document.getElementById("sampleFilterPos").textContent = `${currentFilterIdx + 1} / ${filteredIds.length}`;

  // Meta badges
  let meta = `<span class="badge badge-source">${d.source}</span>`;
  meta += `<span class="badge badge-confidence">置信度 ${d.confidence}</span>`;
  if (d.is_calibration) meta += `<span class="badge badge-calibration">校准样本</span>`;
  meta += `<span class="badge badge-outcome">${d.trajectory_outcome}</span>`;
  document.getElementById("sampleMeta").innerHTML = meta;

  // Reference info
  const lfLabel = v => v === 1 ? '<span class="lf-vote lf-progress">Progress</span>' :
                         v === 0 ? '<span class="lf-vote lf-stagnation">Stagnation</span>' :
                         '<span class="lf-vote lf-abstain">Abstain</span>';
  const mjLabel = d.majority_label === 1 ? '<span class="lf-vote lf-progress">Progress</span>' :
                  d.majority_label === 0 ? '<span class="lf-vote lf-stagnation">Stagnation</span>' :
                  '<span class="lf-vote lf-abstain">Abstain</span>';
  document.getElementById("refInfo").innerHTML = `
    <table>
      <tr><td>多数投票标签</td><td>${mjLabel}</td></tr>
      <tr><td>LF: file_diff_delta</td><td>${lfLabel(d.lf_file_diff_delta)}</td></tr>
      <tr><td>LF: command_repetition</td><td>${lfLabel(d.lf_command_repetition)}</td></tr>
      <tr><td>LF: outcome_backpropagation</td><td>${lfLabel(d.lf_outcome_backpropagation)}</td></tr>
      <tr><td>Trajectory ID</td><td style="font-family:monospace;font-size:11px;">${d.trajectory_id}</td></tr>
      <tr><td>Window Index</td><td>${d.window_idx}</td></tr>
    </table>`;
  document.getElementById("refInfo").className = showRef ? "ref-info visible" : "ref-info";

  // Agent actions
  renderActions(d.agent_actions);

  // Label buttons
  updateLabelButtons(lbl);
}

function renderActions(text) {
  const container = document.getElementById("actionsContainer");
  const parts = text.split(/^---$/m);
  let html = "";

  for (const part of parts) {
    const trimmed = part.trim();
    if (!trimmed) continue;

    // Split into segments by [Thought], [Command], [Output]
    const segments = trimmed.split(/(?=\[(?:Thought|Command|Output)\])/);
    for (const seg of segments) {
      const s = seg.trim();
      if (!s) continue;

      let cls = "action-step ";
      let label = "";
      if (s.startsWith("[Thought]")) { cls += "step-thought"; label = "Thought"; }
      else if (s.startsWith("[Command]")) { cls += "step-command"; label = "Command"; }
      else if (s.startsWith("[Output]")) { cls += "step-output"; label = "Output"; }
      else { cls += "step-output"; }

      const escaped = escapeHtml(s);
      html += `<div class="${cls}">${escaped}</div>`;
    }
    html += '<div class="step-separator">───</div>';
  }
  // Remove trailing separator
  html = html.replace(/<div class="step-separator">───<\/div>$/, "");
  container.innerHTML = html;
  container.scrollTop = 0;
}

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function updateLabelButtons(lbl) {
  document.querySelectorAll(".label-btn-progress").forEach(b => b.classList.toggle("active", lbl === "progress"));
  document.querySelectorAll(".label-btn-stagnation").forEach(b => b.classList.toggle("active", lbl === "stagnation"));
  document.querySelectorAll(".label-btn-skip").forEach(b => b.classList.toggle("active", lbl === "skip"));
}

function updateStats() {
  let nProgress = 0, nStagnation = 0, nSkip = 0;
  for (const [id, lbl] of Object.entries(labels)) {
    if (lbl === "progress") nProgress++;
    else if (lbl === "stagnation") nStagnation++;
    else if (lbl === "skip") nSkip++;
  }
  const nLabeled = nProgress + nStagnation + nSkip;
  const total = ALL_DATA.length;

  document.getElementById("statTotal").textContent = total;
  document.getElementById("statLabeled").textContent = nLabeled;
  document.getElementById("statProgress").textContent = nProgress;
  document.getElementById("statStagnation").textContent = nStagnation;
  document.getElementById("statSkip").textContent = nSkip;
  document.getElementById("statRemaining").textContent = total - nLabeled;

  document.getElementById("progressBar").style.width = `${(nLabeled / total) * 100}%`;
  document.getElementById("progressText").textContent = `${nLabeled}/${total}`;
}

// --- Actions ---
function setLabel(lbl) {
  if (filteredIds.length === 0) return;
  const d = ALL_DATA[filteredIds[currentFilterIdx]];
  if (labels[d.id] === lbl) {
    delete labels[d.id]; // toggle off
  } else {
    labels[d.id] = lbl;
  }
  saveToStorage();
  renderCurrent();
  updateStats();
  renderList();

  // Auto-advance after labeling
  if (labels[d.id]) {
    setTimeout(() => navNext(), 150);
  }
}

function navPrev() {
  if (currentFilterIdx > 0) { currentFilterIdx--; renderCurrent(); }
}
function navNext() {
  if (currentFilterIdx < filteredIds.length - 1) { currentFilterIdx++; renderCurrent(); }
}
function navNextUnlabeled() {
  for (let i = currentFilterIdx + 1; i < filteredIds.length; i++) {
    const d = ALL_DATA[filteredIds[i]];
    if (!labels[d.id]) { currentFilterIdx = i; renderCurrent(); return; }
  }
  // Wrap around
  for (let i = 0; i < currentFilterIdx; i++) {
    const d = ALL_DATA[filteredIds[i]];
    if (!labels[d.id]) { currentFilterIdx = i; renderCurrent(); return; }
  }
  showToast("所有样本已标注完成！");
}

function jumpTo() {
  const id = parseInt(document.getElementById("jumpInput").value);
  if (isNaN(id)) return;
  // Find in filtered list
  for (let i = 0; i < filteredIds.length; i++) {
    if (ALL_DATA[filteredIds[i]].id === id) {
      currentFilterIdx = i;
      renderCurrent();
      if (isListView) switchToCard();
      return;
    }
  }
  // Find in all data
  for (let i = 0; i < ALL_DATA.length; i++) {
    if (ALL_DATA[i].id === id) {
      // Reset filters and go
      document.getElementById("filterStatus").value = "all";
      document.getElementById("filterSource").value = "all";
      document.getElementById("filterConfidence").value = "all";
      document.getElementById("filterCalibration").checked = false;
      applyFilters();
      for (let j = 0; j < filteredIds.length; j++) {
        if (ALL_DATA[filteredIds[j]].id === id) {
          currentFilterIdx = j;
          renderCurrent();
          if (isListView) switchToCard();
          return;
        }
      }
    }
  }
  showToast("未找到该 ID");
}

// --- Views ---
function toggleView() {
  isListView = !isListView;
  document.getElementById("listView").classList.toggle("active", isListView);
  document.getElementById("cardView").classList.toggle("hidden", isListView);
  if (isListView) renderList();
}

function switchToCard() {
  isListView = false;
  document.getElementById("listView").classList.remove("active");
  document.getElementById("cardView").classList.remove("hidden");
  renderCurrent();
}

function renderList() {
  const tbody = document.getElementById("listBody");
  let html = "";
  for (let i = 0; i < filteredIds.length; i++) {
    const d = ALL_DATA[filteredIds[i]];
    const lbl = labels[d.id] || "";
    const lblClass = lbl === "progress" ? "label-progress" : lbl === "stagnation" ? "label-stagnation" : lbl === "skip" ? "label-skip" : "label-unlabeled";
    const lblText = lbl || "—";
    const summary = d.agent_actions.substring(0, 100).replace(/</g, "&lt;") + "...";
    const cal = d.is_calibration ? "✦" : "";
    html += `<tr onclick="currentFilterIdx=${i};switchToCard();renderCurrent();">
      <td><strong>${d.id}</strong></td>
      <td>${d.source}</td>
      <td>${d.confidence}</td>
      <td>${cal}</td>
      <td style="max-width:400px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-family:monospace;font-size:12px;">${summary}</td>
      <td class="label-cell ${lblClass}">${lblText}</td>
    </tr>`;
  }
  tbody.innerHTML = html;
}

function toggleRef() {
  showRef = !showRef;
  document.getElementById("refInfo").className = showRef ? "ref-info visible" : "ref-info";
}

// --- Export/Import ---
function exportCSV() {
  const annotator = document.getElementById("annotatorName").value || "unknown";
  let csv = "id,trajectory_id,window_idx,confidence,annotator_label,annotator,source\n";
  for (const d of ALL_DATA) {
    const lbl = labels[d.id] || "";
    if (lbl && lbl !== "skip") {
      csv += `${d.id},"${d.trajectory_id}",${d.window_idx},${d.confidence},${lbl},"${annotator}",${d.source}\n`;
    }
  }

  const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `annotation_${annotator}_${new Date().toISOString().slice(0,10)}.csv`;
  a.click();
  URL.revokeObjectURL(url);

  const nExported = Object.values(labels).filter(v => v && v !== "skip").length;
  showToast(`已导出 ${nExported} 条标注`);
}

function importCSV() {
  document.getElementById("importFile").click();
}

function handleImport(event) {
  const file = event.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = function(e) {
    const text = e.target.result;
    if (file.name.endsWith(".json")) {
      try {
        const data = JSON.parse(text);
        if (data.labels) { labels = { ...labels, ...data.labels }; }
        else { for (const [k,v] of Object.entries(data)) { labels[k] = v; } }
      } catch(err) { showToast("JSON 解析失败"); return; }
    } else {
      // CSV
      const lines = text.trim().split("\n");
      for (let i = 1; i < lines.length; i++) {
        const cols = lines[i].split(",");
        if (cols.length >= 5) {
          const id = cols[0].trim();
          const lbl = cols[4].trim().replace(/"/g, "");
          if (lbl === "progress" || lbl === "stagnation") {
            labels[parseInt(id)] = lbl;
          }
        }
      }
    }
    saveToStorage();
    applyFilters();
    showToast("导入成功");
    event.target.value = "";
  };
  reader.readAsText(file);
}

// --- Guide ---
function showGuide() { document.getElementById("guideModal").classList.add("active"); }
function closeGuide() { document.getElementById("guideModal").classList.remove("active"); }

// --- Toast ---
function showToast(msg) {
  const t = document.getElementById("toast");
  t.textContent = msg;
  t.classList.add("show");
  setTimeout(() => t.classList.remove("show"), 2000);
}

// --- Keyboard ---
document.addEventListener("keydown", function(e) {
  if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA" || e.target.tagName === "SELECT") return;
  if (document.getElementById("guideModal").classList.contains("active")) {
    if (e.key === "Escape") closeGuide();
    return;
  }

  switch(e.key) {
    case "1": setLabel("progress"); break;
    case "2": setLabel("stagnation"); break;
    case "3": setLabel("skip"); break;
    case "a": case "A": case "ArrowLeft": navPrev(); break;
    case "d": case "D": case "ArrowRight": navNext(); break;
    case "s": case "S": navNextUnlabeled(); break;
    case "r": case "R": toggleRef(); break;
    case "Escape": closeGuide(); break;
  }
});

// --- Filter listeners ---
["filterStatus", "filterSource", "filterConfidence"].forEach(id => {
  document.getElementById(id).addEventListener("change", () => { currentFilterIdx = 0; applyFilters(); });
});
document.getElementById("filterCalibration").addEventListener("change", () => { currentFilterIdx = 0; applyFilters(); });

// --- Guide content ---
document.getElementById("guideContent").innerHTML = `
<h1>Agent 行为窗口标注指南</h1>

<h2>任务定义</h2>
<p>判断给定的 agent 行为窗口中，agent 是否在<strong>取得有效进展（progress）</strong>还是<strong>陷入停滞（stagnation）</strong>。</p>

<h2>标注选项</h2>
<ul>
<li><strong>Progress</strong> — agent 在此窗口内取得了有效进展</li>
<li><strong>Stagnation</strong> — agent 在此窗口内未取得有效进展</li>
</ul>

<h2>Progress（进展）</h2>
<ul>
<li>修改了相关代码文件</li>
<li>定位到新的错误位置或相关代码</li>
<li>采用了新的解决策略</li>
<li>产生了有意义的文件变更</li>
<li>运行测试获取了新的信息</li>
<li>首次阅读和理解代码结构</li>
</ul>

<h2>Stagnation（停滞）</h2>
<ul>
<li>重复执行相同或近似的命令</li>
<li>反复浏览同一文件的同一区域</li>
<li>修改后又撤销/回退到之前状态</li>
<li>陷入无关操作（与任务目标无关）</li>
<li>反复尝试同一种失败方案</li>
<li>原地循环（做了很多操作但没有实际推进）</li>
</ul>

<h2>边界案例</h2>
<table>
<tr><th>场景</th><th>判定</th><th>理由</th></tr>
<tr><td>agent 尝试了多种不同方法但都失败了</td><td><strong>progress</strong></td><td>每次尝试是新策略</td></tr>
<tr><td>agent 重复同一失败操作</td><td><strong>stagnation</strong></td><td>没有新信息产生</td></tr>
<tr><td>agent 首次阅读代码结构</td><td><strong>progress</strong></td><td>在建立问题理解</td></tr>
<tr><td>agent 反复浏览同一文件同一区域</td><td><strong>stagnation</strong></td><td>未产生新理解</td></tr>
<tr><td>agent 修改代码但引入了新 bug</td><td><strong>progress</strong></td><td>尝试了解决方案</td></tr>
<tr><td>agent 运行测试但测试失败</td><td><strong>progress</strong></td><td>获取了新的诊断信息</td></tr>
<tr><td>agent 反复运行同一测试</td><td><strong>stagnation</strong></td><td>重复行为无新信息</td></tr>
</table>

<h2>常见易混淆</h2>
<ul>
<li><strong>忙碌 ≠ 进展</strong>：反复 scroll_up/scroll_down 同一文件 = 停滞</li>
<li><strong>失败 ≠ 停滞</strong>：尝试新方法并失败 = 进展</li>
<li><strong>慢 ≠ 停滞</strong>：仔细阅读分析 = 进展</li>
<li><strong>多步 ≠ 进展</strong>：步数多但无新信息 = 停滞</li>
</ul>

<h2>键盘快捷键</h2>
<table>
<tr><th>按键</th><th>功能</th></tr>
<tr><td><kbd>1</kbd></td><td>标记为 Progress</td></tr>
<tr><td><kbd>2</kbd></td><td>标记为 Stagnation</td></tr>
<tr><td><kbd>3</kbd></td><td>跳过</td></tr>
<tr><td><kbd>A</kbd> / <kbd>←</kbd></td><td>上一个</td></tr>
<tr><td><kbd>D</kbd> / <kbd>→</kbd></td><td>下一个</td></tr>
<tr><td><kbd>S</kbd></td><td>跳到下一个未标注</td></tr>
<tr><td><kbd>R</kbd></td><td>切换参考信息</td></tr>
</table>

<p style="margin-top:20px;"><button class="btn btn-primary" onclick="closeGuide()">关闭</button></p>
`;

// --- Init ---
loadFromStorage();
applyFilters();
</script>
</body>
</html>
'''

if __name__ == "__main__":
    main()
