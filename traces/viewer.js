'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const fmt = n => Number(n || 0).toLocaleString('en-US');
  const kindLabel = {conversation:'Conversation',worker:'Worker execution',result:'Task result',history:'Context / loop note',other:'Other record'};
  const roleLabel = {user:'User-role message',assistant:'Assistant',tool_call:'Tool call',tool_result:'Tool result',system:'System',record:'Runtime record',log:'Log line',note:'Context note',result:'Task result'};
  const state = {projects:[], catalog:null, catalogURL:null, session:null, sessionURL:null, currentRound:null, messages:[], filtered:[], limit:30, listLimit:50, generation:0, roundGeneration:0};
  const offline = document.body.dataset.offline === 'true';
  const embedded = offline ? JSON.parse($('embedded-sessions').textContent) : [];
  const repository = 'https://github.com/Zxy-MLlab/Release_examples/blob/main/';
  if(offline){
    for(const a of document.querySelectorAll('a[href]'))a.href=new URL(a.getAttribute('href'),repository+'traces/demo.html').href;
    $('offline-banner').querySelector('a').href=repository+'traces/README.md';
  }

  function el(tag, text, cls) { const n=document.createElement(tag); if(text!==undefined)n.textContent=text; if(cls)n.className=cls; return n; }
  function status(text, error=false) { $('status').hidden=!text; $('status').textContent=text; $('status').classList.toggle('error',error); }
  async function json(url) { const r=await fetch(url); if(!r.ok)throw new Error(`Could not load ${url.pathname} (${r.status}).`); return r.json(); }
  function setQuery(values) { const q=new URLSearchParams(location.search); for(const [k,v] of Object.entries(values)){ if(v===null)q.delete(k);else q.set(k,v); } history.replaceState(null,'',`${location.pathname}?${q}`); }
  function download(value,name) { const a=el('a');const u=URL.createObjectURL(new Blob([JSON.stringify(value,null,2)+'\n'],{type:'application/json'}));a.href=u;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(u),1000); }
  function timestamp(value){ if(!value)return 'Time not recorded';const d=new Date(value);return Number.isNaN(d.valueOf())?value:d.toISOString().replace('T',' ').replace(/\.\d+Z$/,' UTC'); }

  function metrics(stats) {
    $('metrics').replaceChildren();
    for(const [label,key] of [['Source records','files'],['Messages / events','messages'],['User turns','user_turns'],['Tool calls','tool_calls']]) {
      const b=el('div',undefined,'metric');b.append(el('b',fmt(stats[key])),el('span',label));$('metrics').append(b);
    }
  }
  function renderList() {
    if(!state.catalog)return;
    const query=$('session-search').value.toLowerCase().trim(),kind=$('source-kind').value;
    const entries=state.catalog.sessions.filter(e=>(kind==='all'||e.kind===kind)&&`${e.title} ${e.source_path} ${e.preview}`.toLowerCase().includes(query));
    $('list-count').textContent=`${fmt(entries.length)} ${entries.length===1?'record':'records'}${offline?' in this preview':''}`;
    $('session-list').replaceChildren();
    for(const e of entries.slice(0,state.listLimit)) {
      const b=el('button',undefined,'session-item'+(state.session?.id===e.id?' active':''));
      b.type='button';b.dataset.session=e.id;b.title=e.source_path;
      b.append(el('strong',e.title),el('small',`${fmt(e.messages)} events · ${fmt(e.user_turns)} user turns`));
      b.addEventListener('click',()=>openSession(e));$('session-list').append(b);
    }
    if(!entries.length)$('session-list').append(el('p','No matching source records.','muted'));
    $('more-sessions').hidden=entries.length<=state.listLimit;
  }
  async function selectProject(project, desiredSession=null, desiredRound=null) {
    const generation=++state.generation;
    ++state.roundGeneration;
    state.session=null;state.catalog=null;state.messages=[];state.listLimit=50;
    $('session-list').replaceChildren();$('more-sessions').hidden=true;
    $('reader').hidden=true;$('empty').hidden=true;status('Loading source catalogue…');
    setQuery({project:project.project,session:desiredSession,round:desiredRound});
    $('project-title').textContent=project.title;
    $('paper-link').href=offline?`${repository}paper-assets/${encodeURIComponent(project.project)}/01-manuscript/paper.pdf`:`../paper-assets/${encodeURIComponent(project.project)}/01-manuscript/paper.pdf`;
    try {
      if(offline) {
        const sample=embedded.find(s=>s.project===project.project);
        state.catalog={sessions:[{...sample,source_path:sample.source.member,preview:'',messages:sample.statistics.messages,user_turns:sample.statistics.user_turns,tool_calls:sample.statistics.tool_calls}],statistics:{files:1,...sample.statistics}};
        state.catalogURL=new URL(`../paper-assets/${project.project}/05-generation-trace/catalog.json`,location.href);
      } else {
        const url=new URL(project.catalog,location.href),catalog=await json(url);
        if(generation!==state.generation)return;
        state.catalog=catalog;state.catalogURL=url;
      }
      if(generation!==state.generation)return;
      metrics(state.catalog.statistics);
      $('catalog-link').href=state.catalogURL.href;
      renderList();status('');$('empty').hidden=false;
      const chosen=state.catalog.sessions.find(s=>s.id===desiredSession);
      if(chosen) {$('source-kind').value=chosen.kind;await openSession(chosen,desiredRound);} else if(offline)await openSession(state.catalog.sessions[0]);
    } catch(error){if(generation===state.generation)status(`${error.message}\nRun python3 scripts/serve_traces.py --open from the repository root, or use the offline preview in traces/demo.html.`,true);}
  }
  async function openSession(entry,desiredRound=null) {
    const generation=++state.generation;
    ++state.roundGeneration;
    state.session=null;state.messages=[];state.currentRound=null;
    $('messages').replaceChildren();$('reader').hidden=true;$('empty').hidden=true;status('Loading recorded session…');
    try {
      const url=entry.path?new URL(entry.path,state.catalogURL):new URL(`../paper-assets/${entry.project}/05-generation-trace/example-session.json`,location.href);
      const session=offline?embedded.find(s=>s.id===entry.id):await json(url);
      if(generation!==state.generation)return;
      state.session=session;state.sessionURL=url;
      $('record-kind').textContent=kindLabel[session.kind]||session.kind;
      $('session-title').textContent=session.title;
      $('source-path').textContent=session.source.member;
      if(offline){
        if(state.previewURL)URL.revokeObjectURL(state.previewURL);
        state.previewURL=URL.createObjectURL(new Blob([JSON.stringify(session,null,2)],{type:'application/json'}));
        $('json-link').href=state.previewURL;$('json-link').textContent='Preview JSON ↗';
      }else $('json-link').href=url.href;
      $('source-index-link').href=offline?`${repository}paper-assets/${session.project}/05-generation-trace/trace-index.csv`:new URL('trace-index.csv',state.catalogURL).href;
      $('provenance').textContent=`Archive: ${session.source.archive}\nMember: ${session.source.member}\nOccurrence: ${session.source.occurrence}\nSHA-256: ${session.source.sha256}\nSanitized source size: ${fmt(session.source.bytes)} bytes`;
      $('provenance').style.whiteSpace='pre-wrap';$('related').replaceChildren();
      for(const e of state.catalog.sessions.filter(e=>e.task_key===session.task_key&&e.id!==session.id).slice(0,10)) {
        const b=el('button',`${kindLabel[e.kind]} · occurrence ${e.occurrence}`);b.addEventListener('click',()=>{$('source-kind').value=e.kind;openSession(e);});$('related').append(b);
      }
      $('round').replaceChildren();
      for(const r of session.rounds) {
        const option=el('option',`${r.number===0?'Unbounded sequence':`Round ${r.number}`} · ${fmt(r.message_count)} events`);option.value=r.number;$('round').append(option);
      }
      $('role-filter').value='all';$('message-search').value='';
      $('reader').hidden=false;status('');renderList();
      setQuery({session:session.id,round:desiredRound});
      const requested=desiredRound;
      const initial=session.rounds.find(r=>String(r.number)===requested)||session.rounds.find(r=>r.number>0)||session.rounds[0];
      if(initial) {$('round').value=initial.number;await openRound(initial.number);} else status('This source contains no non-empty recorded messages.');
    }catch(error){if(generation===state.generation)status(error.message,true);}
  }
  async function openRound(number) {
    const r=state.session.rounds.find(r=>r.number===Number(number));if(!r)return;
    const generation=++state.roundGeneration,sessionID=state.session.id;
    state.currentRound=r;state.messages=[];state.limit=30;$('messages').replaceChildren();
    $('download-round').disabled=true;
    const i=state.session.rounds.indexOf(r);
    $('prev-round').disabled=i===0;$('next-round').disabled=i===state.session.rounds.length-1;
    $('round-description').textContent=r.number===0?'No preceding user message is recorded for this sequence. Order follows the source file.':`Round ${r.number} starts with a recorded user-role message and continues to the next user-message boundary. This does not imply a human author.`;
    setQuery({round:r.number});
    if(r.messages)state.messages=r.messages;
    else {
      status(`Loading ${fmt(r.message_count)} recorded events…`);
      try {
        // Sequential pages bound peak memory and do not prefetch other rounds.
        const all=[];
        for(const chunk of r.chunks||[]) {
          const page=await json(new URL(chunk.path,state.sessionURL));
          if(generation!==state.roundGeneration||state.session?.id!==sessionID)return;
          const segment=(page.rounds||[]).find(turn=>turn.number===r.number);
          if(segment)all.push(...segment.messages);
        }
        state.messages=all;
      }catch(error){if(generation===state.roundGeneration)status(error.message,true);return;}
    }
    if(generation!==state.roundGeneration)return;
    $('download-round').disabled=false;status('');renderMessages();
  }
  function longText(parent,text,cls='') {
    const node=el(cls==='text-block'?'div':'pre',text.length>16000?text.slice(0,16000)+'\n…':text,cls);parent.append(node);
    if(text.length>16000){const b=el('button',`Show complete text (${fmt(text.length)} characters)`,'expand-text');b.addEventListener('click',()=>{node.textContent=text;b.remove();});parent.append(b);}
  }
  function blockView(block) {
    const out=el('div',undefined,'block');
    if(typeof block!=='object'||block===null){longText(out,String(block));return out;}
    const type=block.type;
    if(type==='text')longText(out,String(block.text||''),'text-block');
    else if(type==='thinking') {
      const d=el('details',undefined,'thinking');d.append(el('summary','Logged reasoning block'));longText(d,String(block.thinking||''));out.append(d);
    } else if(type==='tool_use'||type==='server_tool_use') {
      out.classList.add('tool-block');out.append(el('div','TOOL CALL','block-label'),el('strong',block.name||'Unnamed tool'));
      if(block.id)out.append(el('div',`Call ID: ${block.id}`,'source-line'));
      longText(out,block.input===undefined?'Arguments not recorded in this source.':JSON.stringify(block.input,null,2));
    } else if(type==='tool_result') {
      out.classList.add('tool-block');out.append(el('div',`TOOL RESULT${block.is_error?' · REPORTED ERROR':''}`,'block-label'));
      if(block.tool_use_id)out.append(el('div',`Call ID: ${block.tool_use_id}`,'source-line'));
      if(Array.isArray(block.content)){for(const child of block.content)out.append(blockView(child));}
      else longText(out,typeof block.content==='string'?block.content:JSON.stringify(block.content??null,null,2));
    } else {out.append(el('div',type||'Recorded value','block-label'));longText(out,JSON.stringify(type==='json'?block.value:block,null,2));}
    return out;
  }
  function messageView(event) {
    const item=el('article',undefined,`message ${event.role}`);item.id=event.id;
    const h=el('div',undefined,'message-head');h.append(el('span',roleLabel[event.role]||event.role,'role'),el('span',event.id));
    h.append(el('span',`source line ${event.source_line}`),el('time',timestamp(event.timestamp)));item.append(h);
    if(event.metadata?.source)h.insertBefore(el('span',`from ${event.metadata.source}`),h.lastChild);
    const content=el('div',undefined,'message-content');for(const block of event.content||[])content.append(blockView(block));
    const meta=event.metadata||{};
    if(event.role==='tool_call'&&meta.tool){const b=el('div',undefined,'block tool-block');b.append(el('strong',meta.tool));longText(b,meta.tool_args===undefined?'Arguments not recorded in this source.':JSON.stringify(meta.tool_args,null,2));content.append(b);}
    if(event.role==='tool_result'&&!event.content?.some(b=>b.text||b.content))content.append(el('p','The source records a tool-result event without a text payload.','muted'));
    item.append(content);
    if(event.metadata||event.recorded_role){const d=el('details',undefined,'metadata');d.append(el('summary','Recorded metadata'));longText(d,JSON.stringify({recorded_role:event.recorded_role,...event.metadata},null,2));item.append(d);}
    return item;
  }
  function renderMessages() {
    const role=$('role-filter').value,q=$('message-search').value.toLowerCase().trim();
    const isTool=e=>['tool_call','tool_result'].includes(e.role)||(e.content||[]).some(b=>['tool_use','server_tool_use','tool_result'].includes(b.type));
    state.filtered=state.messages.filter(e=>{
      const roleMatch=role==='all'||(role==='tool'?isTool(e):role==='other'?!['user','assistant','tool_call','tool_result'].includes(e.role):e.role===role);
      return roleMatch&&(!q||JSON.stringify(e).toLowerCase().includes(q));
    });
    $('messages').replaceChildren();
    for(const event of state.filtered.slice(0,state.limit))$('messages').append(messageView(event));
    if(!state.filtered.length)$('messages').append(el('div','No messages match these filters.','load-note'));
    $('more-messages').hidden=state.filtered.length<=state.limit;
    $('more-messages').textContent=`Load more messages (${fmt(state.filtered.length-state.limit)} remaining)`;
  }
  $('project').addEventListener('change',()=>selectProject(state.projects.find(p=>p.project===$('project').value)));
  for(const id of ['session-search','source-kind'])$(id).addEventListener(id==='session-search'?'input':'change',()=>{state.listLimit=50;renderList();});
  $('more-sessions').addEventListener('click',()=>{state.listLimit+=50;renderList();});
  $('more-messages').addEventListener('click',()=>{state.limit+=30;renderMessages();});
  $('round').addEventListener('change',()=>openRound($('round').value));
  for(const id of ['role-filter','message-search'])$(id).addEventListener(id==='message-search'?'input':'change',()=>{state.limit=30;renderMessages();});
  for(const [id,step] of [['prev-round',-1],['next-round',1]])$(id).addEventListener('click',()=>{const i=state.session.rounds.indexOf(state.currentRound);const r=state.session.rounds[i+step];if(r){$('round').value=r.number;openRound(r.number);}});
  $('download-round').addEventListener('click',()=>{if(state.session&&state.currentRound)download({schema_version:state.session.schema_version,session_id:state.session.id,project:state.session.project,source:state.session.source,round:{number:state.currentRound.number,boundary:state.currentRound.boundary,messages:state.messages}},`${state.session.id}-round-${state.currentRound.number}.json`);});
  (async()=>{
    try {
      const requested=new URLSearchParams(location.search);
      if(offline){$('offline-banner').hidden=false;state.projects=embedded.map(s=>({project:s.project,title:s.paper_title||s.project}));}
      else state.projects=(await json(new URL('projects.json',location.href))).projects;
      for(const p of state.projects){const o=el('option',p.project);o.value=p.project;$('project').append(o);}
      const p=state.projects.find(p=>p.project===requested.get('project'))||state.projects[0];
      if(!p)throw new Error('No source records are available.');
      $('project').value=p.project;
      await selectProject(p,requested.get('session'),requested.get('round'));
    }catch(error){status(`${error.message}\nTo browse the full dataset, run python3 scripts/serve_traces.py --open from the repository root. For a preview without a server, open traces/demo.html.`,true);}
  })();
})();
