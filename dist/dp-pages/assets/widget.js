/* Digi chat widget (moved from homepage) */
// ── DIGI CHAT WIDGET ──
(function(){
  var WEBHOOK='https://engine.digipromise.com/webhook/b3118165-b837-4458-b22b-e174e0555a32/chat/dp-web-digipromise';
  var sessionId='digi_'+Math.random().toString(36).substr(2,12)+'_'+Date.now();
  var launcher=document.getElementById('digiLauncher');
  var panel=document.getElementById('digiPanel');
  var closeBtn=document.getElementById('digiClose');
  var msgs=document.getElementById('digiMsgs');
  var inp=document.getElementById('digiInp');
  var snd=document.getElementById('digiSnd');
  var typing=document.getElementById('digiTyping');
  var busy=false;
  var avatarUrl='https://digipromise.com/wp-content/uploads/2026/06/Gemini_Generated_Image_kby6c5kby6c5kby6.png';
var waLauncher=document.getElementById('waLauncher');
var tgLauncher=document.getElementById('tgLauncher');
launcher.addEventListener('click',function(){ panel.classList.toggle('open'); var isOpen=panel.classList.contains('open'); if(waLauncher) waLauncher.style.display=isOpen?'none':''; if(tgLauncher) tgLauncher.style.display=isOpen?'none':''; if(isOpen) setTimeout(function(){inp.focus();},200); });
closeBtn.addEventListener('click',function(){ panel.classList.remove('open'); if(waLauncher) waLauncher.style.display=''; if(tgLauncher) tgLauncher.style.display=''; });
  function addMsg(text,who){
    var wrap=document.createElement('div'); wrap.className='digi-msg '+who;
    if(who==='bot'){ var av=document.createElement('img'); av.className='digi-msg-av'; av.src=avatarUrl; av.alt='Digi'; wrap.appendChild(av); }
    var b=document.createElement('div'); b.className='digi-bbl'; b.textContent=text; wrap.appendChild(b);
    msgs.insertBefore(wrap,typing); msgs.scrollTop=msgs.scrollHeight;
  }
  function parseReply(raw){
    try{ var j=JSON.parse(raw); return j.output||j.message||j.text||j.response||raw; }
    catch(e){ var lines=raw.split('\n').filter(function(l){return l.trim();}); var out='';
      for(var i=0;i<lines.length;i++){ try{ var o=JSON.parse(lines[i]); if(o.type==='item'&&o.content&&o.metadata&&o.metadata.nodeName==='Respond to Webhook'){out+=o.content;} }catch(e2){} }
      return out.trim()||'Sorry, I could not process that. Please try again.'; }
  }
  async function send(){
    if(busy)return; var text=inp.value.trim(); if(!text)return;
    addMsg(text,'user'); inp.value=''; busy=true; snd.disabled=true;
    typing.classList.add('show'); msgs.scrollTop=msgs.scrollHeight;
    try{
      var res=await fetch(WEBHOOK,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({chatInput:text,sessionId:sessionId,ref:window.DP_REF||'',page:location.pathname})});
      var raw=await res.text(); typing.classList.remove('show'); addMsg(parseReply(raw),'bot');
    }catch(err){ typing.classList.remove('show'); addMsg('Oops! Something went wrong. Please try again.','bot'); }
    busy=false; snd.disabled=false; inp.focus();
  }
  snd.addEventListener('click',send);
  inp.addEventListener('keydown',function(e){if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();send();}});
  addMsg(document.body.getAttribute('data-greet')||'Hi! I am Digi, the DigiPromise AI agent. Ask me anything, I reply in seconds.','bot');
})();

/* Greeting bubble: once per visit, after 8s or half-page scroll */
(function(){
  var g=document.getElementById('digiGreet'),x=document.getElementById('digiGreetX'),t=document.getElementById('digiGreetTxt'),
      l=document.getElementById('digiLauncher'),p=document.getElementById('digiPanel');if(!g||!l)return;
  var seen=false;try{seen=sessionStorage.getItem('dp_greet')==='1'}catch(e){}
  if(seen)return;
  t.textContent=document.body.getAttribute('data-greet')||'Hi! I am Digi, the DigiPromise AI agent. Ask me anything, I reply in seconds.';
  var shown=false;
  function show(){if(shown||(p&&p.classList.contains('open')))return;shown=true;g.hidden=false;try{sessionStorage.setItem('dp_greet','1')}catch(e){}
    removeEventListener('scroll',onS)}
  function onS(){if(scrollY>(document.documentElement.scrollHeight-innerHeight)*.5)show()}
  setTimeout(show,8000);addEventListener('scroll',onS,{passive:true});
  x.addEventListener('click',function(e){e.stopPropagation();g.hidden=true});
  g.addEventListener('click',function(){g.hidden=true;if(p&&!p.classList.contains('open'))l.click()});
  l.addEventListener('click',function(){g.hidden=true});
})();
/* Arabic labels for the widget on /ar/ pages */
(function(){if(document.documentElement.lang!=='ar')return;
  var q=function(s){return document.querySelector(s)};
  var l=q('.digi-lbl');if(l)l.textContent='اسأل ديجي';
  var i=q('#digiInp');if(i){i.placeholder='اكتب سؤالك...';i.setAttribute('aria-label','اكتب رسالتك');i.dir='auto'}
  var tg=document.querySelector('.digi-alt a[href*="t.me"]');if(tg)tg.lastChild.textContent='تيليجرام';
  var s=q('.digi-ph-status');if(s)s.lastChild.textContent='متصل · ذكاء ديجي برومس';
  var pw=q('.digi-pwrd');if(pw)pw.firstChild.textContent='بواسطة ';
  var x=q('#digiGreetX');if(x)x.setAttribute('aria-label','إغلاق الرسالة');
  var p=q('#digiPanel');if(p)p.setAttribute('dir','rtl');
})();

/* Voice call with Digi (ElevenLabs, 17 Oct 2026). Loads the client only when Talk is tapped. */
(function(){
  var btn=document.getElementById('digiTalk'),bar=document.getElementById('digiVoice'),st=document.getElementById('digiVst'),
      end=document.getElementById('digiVend'),panel=document.getElementById('digiPanel'),closeBtn=document.getElementById('digiClose'),
      launcher=document.getElementById('digiLauncher');
  if(!btn||!bar)return;
  var AR=document.documentElement.lang==='ar',conv=null,starting=false;
  var T=AR?{talk:'🎙 تحدث',conn:'جارٍ الاتصال…',listen:'أستمع إليك…',speak:'ديجي يتحدث',busy:'الخدمة الصوتية مشغولة، يرجى استخدام الدردشة.',soon:'المكالمات الصوتية قريباً. استخدم الدردشة الآن.',mic:'نحتاج إذن الميكروفون للتحدث مع ديجي.',endc:'إنهاء المكالمة',ended:'انتهت المكالمة.'}
         :{talk:'🎙 Talk',conn:'Connecting…',listen:'Listening…',speak:'Digi is speaking',busy:'Voice is busy, please use chat.',soon:'Voice calls are coming soon. Please use chat for now.',mic:'Please allow the microphone to talk to Digi.',endc:'End call',ended:'Call ended.'};
  btn.textContent=T.talk;end.textContent=T.endc;
  var URL='https://engine.digipromise.com/webhook/voice-session',LIB='https://cdn.jsdelivr.net/npm/@elevenlabs/client@1.26.0/+esm';
  function show(t,idle){bar.hidden=false;bar.classList.toggle('idle',!!idle);st.textContent=t}
  function note(t){show(t,true);end.style.display='none';setTimeout(function(){if(!conv&&!starting){bar.hidden=true;end.style.display=''}},5000)}
  function reset(){conv=null;starting=false;btn.disabled=false}
  function stop(){var c=conv;conv=null;if(c){try{c.endSession()}catch(e){}}starting=false;btn.disabled=false;bar.hidden=true;end.style.display=''}
  btn.addEventListener('click',async function(){
    if(conv||starting)return;starting=true;btn.disabled=true;end.style.display='';show(T.conn);
    try{var ms=await navigator.mediaDevices.getUserMedia({audio:true});ms.getTracks().forEach(function(t){t.stop()})}
    catch(e){reset();note(T.mic);return}
    var signedUrl='';
    try{var r=await fetch(URL,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({agent:'digi',page:location.pathname})});
      if(r.status===404){reset();note(T.soon);return}
      var j=await r.json().catch(function(){return {}});
      if(!r.ok||j.error||!j.signed_url){reset();note(T.busy);return}
      signedUrl=j.signed_url}
    catch(e){reset();note(T.soon);return}
    if(!starting)return; /* closed meanwhile */
    try{var m=await import(LIB);
      conv=await m.Conversation.startSession({signedUrl:signedUrl,connectionType:'websocket',
        onConnect:function(){show(T.listen)},
        onModeChange:function(x){show(x&&x.mode==='speaking'?T.speak:T.listen)},
        onDisconnect:function(){if(conv||starting){conv=null;starting=false;btn.disabled=false;note(T.ended)}},
        onError:function(){}});
      starting=false;if(!panel.classList.contains('open'))stop();}
    catch(e){reset();note(T.busy)}
  });
  end.addEventListener('click',stop);
  closeBtn&&closeBtn.addEventListener('click',stop);
  launcher&&launcher.addEventListener('click',function(){if(!panel.classList.contains('open'))stop()});
  addEventListener('pagehide',stop);
})();
