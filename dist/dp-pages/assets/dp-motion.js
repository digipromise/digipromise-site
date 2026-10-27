/* DigiPromise motion layer v1 — ~3 KB, no libraries */
(function(){
  var d=document,root=d.documentElement,reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Scroll reveal
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.18});
  d.querySelectorAll('.rv,.demo').forEach(function(el){io.observe(el)});

  // Header pill on scroll + timeline fill
  var tl=d.querySelector('.tl'),items=tl?tl.querySelectorAll('.tl-i'):[];
  function onScroll(){
    root.classList.toggle('scrolled',scrollY>40);
    if(tl){var r=tl.getBoundingClientRect(),p=Math.min(1,Math.max(0,(innerHeight*.75-r.top)/(r.height+innerHeight*.25)));
      tl.style.setProperty('--p',p);items.forEach(function(it,i){it.classList.toggle('on',p>=i/items.length)})}
  }
  addEventListener('scroll',onScroll,{passive:true});onScroll();

  // Rotating hero verb
  d.querySelectorAll('.rot').forEach(function(r){
    var s=r.querySelectorAll('span'),i=0;if(reduce||s.length<2)return;
    setInterval(function(){var a=s[i];a.classList.remove('on');a.classList.add('out');
      setTimeout(function(){a.classList.remove('out')},450);i=(i+1)%s.length;s[i].classList.add('on')},2200);
  });

  // Sparkles
  var sp=d.querySelector('.sparkles');
  if(sp&&!reduce){for(var k=0;k<14;k++){var e=d.createElement('i');e.style.left=Math.random()*100+'%';
    e.style.animationDuration=(14+Math.random()*16)+'s';e.style.animationDelay=(-Math.random()*20)+'s';
    var z=6+Math.random()*8;e.style.width=e.style.height=z+'px';sp.appendChild(e)}}

  // Count-up numbers
  var cio=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;cio.unobserve(e.target);
    var el=e.target,to=+el.dataset.to,suf=el.dataset.suf||'',t0=null;
    if(reduce){el.textContent=to+suf;return}
    function f(t){t0=t0||t;var p=Math.min(1,(t-t0)/1400),v=Math.round(to*(1-Math.pow(1-p,3)));el.textContent=v+suf;if(p<1)requestAnimationFrame(f)}
    requestAnimationFrame(f)})},{threshold:.5});
  d.querySelectorAll('[data-to]').forEach(function(el){cio.observe(el)});

  // Agent carousel (coverflow)
  d.querySelectorAll('.cf').forEach(function(cf){
    var it=[].slice.call(cf.querySelectorAll('.cf-item')),n=it.length,c=0,dots=cf.parentNode.querySelector('.cf-dots'),timer;
    it.forEach(function(_,i){var b=d.createElement('button');b.setAttribute('aria-label','Show agent '+(i+1));b.onclick=function(){go(i)};dots.appendChild(b)});
    function go(k){c=(k+n)%n;it.forEach(function(el,i){var o=((i-c+n+Math.floor(n/2))%n)-Math.floor(n/2),a=Math.abs(o);
      el.classList.toggle('c',o===0);el.style.zIndex=10-a;el.style.opacity=a>2?0:1-a*.28;el.style.filter=a?'blur('+a*2+'px)':'none';
      el.style.transform='translateX('+o*260+'px) scale('+(1-a*.22)+')';el.setAttribute('aria-hidden',o!==0)});
      [].forEach.call(dots.children,function(b,i){b.classList.toggle('on',i===c)})}
    it.forEach(function(el,i){el.addEventListener('click',function(ev){if(i!==c){ev.preventDefault();go(i)}})});
    cf.querySelector('.cf-prev').onclick=function(){go(c-1);pause()};cf.querySelector('.cf-next').onclick=function(){go(c+1);pause()};
    var resume;
    function stop(){clearInterval(timer);clearTimeout(resume)}
    function start(){stop();if(!reduce)timer=setInterval(function(){go(c+1)},3500)}
    function pause(){stop();resume=setTimeout(start,5000)}
    go(0);start();cf.addEventListener('mouseenter',stop);cf.addEventListener('mouseleave',pause);
    cf.addEventListener('touchstart',pause,{passive:true});
  });

  // Hero chat replay
  var ph=d.querySelector('.phone .msgs[data-script]'),feed=d.querySelectorAll('.feed li');
  if(ph){var script=JSON.parse(ph.dataset.script),step=0;
    function next(){
      if(step>=script.length){setTimeout(function(){ph.innerHTML='';step=0;feed.forEach(function(f){f.classList.remove('on')});next()},3500);return}
      var m=script[step],delay=m[0]==='b'?1100:700;
      if(m[0]==='b'){var t=d.createElement('div');t.className='msg b t';t.innerHTML='<i></i><i></i><i></i>';ph.appendChild(t);
        setTimeout(function(){t.remove();add(m)},reduce?0:900)}else add(m);
      function add(m){var e=d.createElement('div');e.className='msg '+m[0];e.textContent=m[1];ph.appendChild(e);
        if(m[2]!=null&&feed[m[2]])feed[m[2]].classList.add('on');step++;setTimeout(next,delay)}
    }
    next();
  }

  // Hero capture form -> engine lead webhook (window.DP_SEND in dp.js)
  d.querySelectorAll('.capture').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();
    var ar=d.documentElement.lang==='ar',n=f.parentNode.querySelector('.capture-note'),b=f.querySelector('button'),i=f.querySelector('input[name=contact]'),v=i?i.value.trim():'';
    var say=function(t,bad){if(n){n.textContent=t;n.style.color=bad?'#B91C1C':''}};
    if(!v){say(ar?'أدخل بريدك الإلكتروني أو رقم واتساب.':'Please enter your email or WhatsApp number.',1);return}
    if(!window.DP_SEND){say(ar?'حدث خطأ، يرجى المحاولة مرة أخرى.':'Something went wrong. Please try again.',1);return}
    var hp=f.querySelector('input[name=website]');b&&(b.disabled=true);
    window.DP_SEND({email:v,website:hp?hp.value:'',message:'Homepage form'}).then(function(r){b&&(b.disabled=false);
      if(r&&r.ok){location.href=ar?'/ar/thanks/':'/thanks/'}
      else say((ar?'لم يتم الإرسال: ':'Not sent: ')+((r&&r.error&&r.error!=='network')?r.error:(ar?'تحقق من الاتصال وحاول مرة أخرى.':'check your connection and try again.')),1)})})});
})();
/* Product page helpers */
(function(){
  var d=document;
  // "Try it live" buttons open the Digi chat widget
  d.addEventListener('click',function(e){var b=e.target.closest('[data-open-chat]');if(!b)return;e.preventDefault();
    var l=d.getElementById('digiLauncher'),p=d.getElementById('digiPanel');if(l&&p&&!p.classList.contains('open'))l.click();
    var i=d.getElementById('digiInp');if(i){i.value=b.getAttribute('data-open-chat')||'';i.focus()}});
  // Auto-advancing tabs (manual click stops auto)
  d.querySelectorAll('.ptabs').forEach(function(list){
    var tabs=[].slice.call(list.querySelectorAll('[role="tab"]')),i=0,timer;
    function show(k){i=k;tabs.forEach(function(t,j){var on=j===k;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1;
      var p=d.getElementById(t.getAttribute('aria-controls'));if(p)p.hidden=!on});}
    tabs.forEach(function(t,j){t.addEventListener('click',function(){clearInterval(timer);show(j)})});
    var h=location.hash.slice(1),st=0;tabs.forEach(function(t,k){if(t.getAttribute('aria-controls')===h)st=k});show(st);if(!list.hasAttribute('data-noauto')&&!matchMedia('(prefers-reduced-motion: reduce)').matches)timer=setInterval(function(){show((i+1)%tabs.length)},7000);
  });
})();

/* Fluffy mascots: fur + eyes that follow the cursor (all pages with mascots) */
(function(){
  var d=document,ms=[].slice.call(d.querySelectorAll('.mascot'));if(!ms.length)return;
  var NS='http://www.w3.org/2000/svg',svg=d.createElementNS(NS,'svg');svg.setAttribute('width','0');svg.setAttribute('height','0');svg.setAttribute('aria-hidden','true');svg.style.position='absolute';
  function f(id,bf,sc){return '<filter id="'+id+'" x="-30%" y="-30%" width="160%" height="160%" color-interpolation-filters="sRGB"><feTurbulence type="fractalNoise" baseFrequency="'+bf+'" numOctaves="3" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="'+sc+'" xChannelSelector="R" yChannelSelector="G" result="d"/><feTurbulence type="turbulence" baseFrequency="1.3" numOctaves="2" seed="4" result="s"/><feColorMatrix in="s" type="saturate" values="0" result="g"/><feComponentTransfer in="g" result="t"><feFuncA type="linear" slope="0.8"/></feComponentTransfer><feBlend in="d" in2="t" mode="overlay" result="b"/><feComposite in="b" in2="d" operator="in"/></filter>'}
  svg.innerHTML='<defs>'+f('dpfurL','0.55',34)+f('dpfurM','0.7',18)+f('dpfurS','0.9',7)+'</defs>';d.body.appendChild(svg);
  var sc=d.querySelector('script[src*="dp-motion.js"]'),base=sc?sc.src.replace(/dp-motion\.js.*$/,''):'';
  ms.forEach(function(m){if(m.querySelector('.eyes'))return;var w=m.getBoundingClientRect().width||m.offsetWidth||100,
    id=(m.className.match(/\bm-([a-z]+)/)||[])[1],img=id?'<img class="mimg" src="'+base+'mascot-'+id+'.webp" alt="" loading="lazy" decoding="async">':'<span class="fur"></span>';
    m.classList.add('fluffy',w>=150?'fz-l':w>=70?'fz-m':'fz-s');
    m.insertAdjacentHTML('afterbegin',img+'<span class="eyes"><i></i><i></i></span>')});
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var mx=null,my=null,raf=0,idle;
  function upd(){raf=0;ms.forEach(function(m){var e=m.querySelector('.eyes');if(!e)return;var r=m.getBoundingClientRect();
    if(r.bottom<0||r.top>innerHeight)return;var dx=0,dy=0;
    if(mx!==null){var cx=r.left+r.width/2,cy=r.top+r.height/2,ax=mx-cx,ay=my-cy,dist=Math.hypot(ax,ay)||1,k=Math.min(1,dist/300);dx=ax/dist*k;dy=ay/dist*k}
    e.style.transform='translate('+(dx*r.width*.13).toFixed(1)+'px,'+(dy*r.height*.11).toFixed(1)+'px)'})}
  function q(){if(!raf)raf=requestAnimationFrame(upd)}
  d.addEventListener('mousemove',function(ev){mx=ev.clientX;my=ev.clientY;q();clearTimeout(idle);idle=setTimeout(function(){mx=null;q()},4000)},{passive:true});
  addEventListener('scroll',q,{passive:true});
  // touch devices: eyes glance around on their own
  if(!matchMedia('(hover: hover)').matches){var a=0;setInterval(function(){a+=1.7;mx=innerWidth/2+Math.cos(a)*240;my=innerHeight/2+Math.sin(a*1.3)*160;q()},1600)}
})();
/* Live product demo (Lilia): chips + free text, scripted on sample data; uses data-webhook when set */
(function(){
  var d=document;[].forEach.call(d.querySelectorAll('.ld'),function(ld){
    var cfg=JSON.parse(ld.getAttribute('data-ld')),box=ld.querySelector('.ld-msgs'),form=ld.querySelector('.ld-form'),inp=form.querySelector('input'),hook=ld.getAttribute('data-webhook'),
        sid='lilia-'+Math.random().toString(36).slice(2),busy=false;
    function norm(t){return (t||'').toLowerCase().replace(/[ً-ْـ]/g,'').replace(/[أإآ]/g,'ا')}
    function add(cls,html){var m=d.createElement('div');m.className='msg '+cls;m.innerHTML=html;box.appendChild(m);box.scrollTop=box.scrollHeight;return m}
    function esc(t){return t.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
    function local(q){var n=norm(q);for(var i=0;i<cfg.r.length;i++){var ks=cfg.r[i][0];for(var j=0;j<ks.length;j++){if(n.indexOf(norm(ks[j]))>-1)return cfg.r[i][1]}}return cfg.f}
    function reply(html){var t=add('b t','<i></i><i></i><i></i>');setTimeout(function(){t.remove();add('b',html);busy=false},900)}
    function ask(q){if(busy||!q.trim())return;busy=true;add('u',esc(q));
      if(hook){fetch(hook,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action:'sendMessage',sessionId:sid,chatInput:q,agent:'lilia'})})
        .then(function(r){return r.json()}).then(function(j){reply(esc(j.output||j.reply||'').replace(/\n/g,'<br>')||local(q))}).catch(function(){reply(local(q))})}
      else reply(local(q))}
    [].forEach.call(ld.querySelectorAll('[data-q]'),function(b){b.addEventListener('click',function(){ask(b.getAttribute('data-q'))})});
    form.addEventListener('submit',function(ev){ev.preventDefault();var q=inp.value;inp.value='';ask(q)});
    // greet once visible
    var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){io.disconnect();busy=true;reply(cfg.r[cfg.r.length-1][1])}},{threshold:.4});io.observe(ld);
  });
})();
/* Hero voice demo (Lilia "Jarvis"): tap orb -> browser speech recognition -> scripted answer -> spoken reply */
(function(){
  var d=document,vs=d.querySelector('.vstage'),ld=d.querySelector('.ld');if(!vs||!ld)return;
  var cfg=JSON.parse(ld.getAttribute('data-ld')),ar=vs.getAttribute('data-vlang')==='ar',orb=vs.querySelector('.vs-orb'),st=vs.querySelector('.vs-state'),log=vs.querySelector('.vs-log'),
      L={tap:vs.getAttribute('data-l-tap'),listen:vs.getAttribute('data-l-listen'),speak:vs.getAttribute('data-l-speak')},
      SR=window.SpeechRecognition||window.webkitSpeechRecognition,syn=window.speechSynthesis,rec=null,on=false,voice=null;
  function norm(t){return (t||'').toLowerCase().replace(/[ً-ْـ]/g,'').replace(/[أإآ]/g,'ا')}
  function local(q){var n=norm(q);for(var i=0;i<cfg.r.length;i++){var ks=cfg.r[i][0];for(var j=0;j<ks.length;j++){if(n.indexOf(norm(ks[j]))>-1)return cfg.r[i][1]}}return cfg.f}
  function plain(h){var x=d.createElement('div');x.innerHTML=h.replace(/<br\s*\/?>/g,'. ');var t=x.textContent;
    try{t=t.replace(/[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{FE0F}]/gu,'')}catch(e){}return t.replace(/•/g,'').replace(/\s*\.\s*\./g,'.').replace(/\s+/g,' ').trim()}
  function esc(t){return t.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function state(c,txt){vs.classList.remove('listening','speaking');if(c)vs.classList.add(c);st.textContent=txt}
  function pick(){if(!syn)return;var vv=syn.getVoices();if(!vv.length)return;
    var pref=ar?[/ar/i]:[/Samantha|Aria|Jenny|Libby|Sonia|Google UK English Female|Google US English|Karen|Moira|Serena/i,/en-GB|en-US|en/i];
    for(var p=0;p<pref.length&&!voice;p++)for(var i=0;i<vv.length;i++){var v=vv[i];if(ar?/^ar/i.test(v.lang):(pref[p].test(v.name)||(p>0&&pref[p].test(v.lang)))){voice=v;break}}}
  if(syn){pick();syn.onvoiceschanged=pick}
  function line(cls,html){var m=d.createElement('div');m.className='vs-l '+cls;m.innerHTML=html;log.appendChild(m);while(log.children.length>4)log.removeChild(log.firstChild);return m}
  function say(html){line('b',html);if(!syn){state('','🎙️ '+L.tap);return}
    syn.cancel();var u=new SpeechSynthesisUtterance(plain(html));u.lang=ar?'ar-AE':'en-GB';if(voice)u.voice=voice;u.rate=1.03;u.pitch=1.05;
    u.onstart=function(){state('speaking','🔊 '+L.speak)};u.onend=u.onerror=function(){state('','🎙️ '+L.tap)};syn.speak(u)}
  function ask(q){if(!q.trim())return;line('u',esc(q));var t=line('b t','<i></i><i></i><i></i>');setTimeout(function(){t.remove();say(local(q))},700)}
  orb.addEventListener('click',function(){
    if(syn)syn.cancel();
    if(on&&rec){rec.stop();return}
    if(!SR){vs.classList.add('nosr');line('b',ar?'التحدث الصوتي غير مدعوم في هذا المتصفح. اختر سؤالاً بالأسفل 👇':'Voice input isn\'t supported in this browser. Tap a question below 👇');return}
    rec=new SR();rec.lang=ar?'ar-AE':'en-US';rec.interimResults=true;rec.maxAlternatives=1;var interim=null,final='';
    rec.onstart=function(){on=true;state('listening','👂 '+L.listen)};
    rec.onresult=function(ev){var s='';final='';for(var i=0;i<ev.results.length;i++){if(ev.results[i].isFinal)final+=ev.results[i][0].transcript;else s+=ev.results[i][0].transcript}
      if(!interim)interim=line('u p','');interim.textContent=final||s};
    rec.onerror=function(){on=false;state('','🎙️ '+L.tap)};
    rec.onend=function(){on=false;var q=interim?interim.textContent:'';if(interim)interim.remove();interim=null;if(q)ask(q);else state('','🎙️ '+L.tap)};
    try{rec.start()}catch(e){}
  });
  [].forEach.call(vs.querySelectorAll('[data-vq]'),function(b){b.addEventListener('click',function(){if(syn)syn.cancel();ask(b.getAttribute('data-vq'))})});
  line('b',ar?'أهلاً، أنا Lilia 👋 اضغط على الدائرة واسألني عن يومك.':'Hi, I\'m Lilia 👋 Tap the orb and ask me about your day.');
})();
/* Inbound / outbound pricing groups (Stella) */
(function(){[].forEach.call(document.querySelectorAll('.grp-sw'),function(sw){var bs=sw.querySelectorAll('button');
  [].forEach.call(bs,function(b){b.addEventListener('click',function(){[].forEach.call(bs,function(x){x.classList.toggle('on',x===b);var g=document.getElementById(x.getAttribute('data-grp'));if(g)g.hidden=x!==b})})})})})();
