/* DigiPromise site JS v1 — loaded with defer, ~1 KB.
   Currency is set before paint by the inline head snippet (see README). */
(function(){
  var d=document.documentElement;d.classList.add('js');
  // Checkout links follow the billing + currency switches (same tab)
  var CK='https://engine.digipromise.com/webhook/checkout';
  window.DP_CK=function(){var bl=d.getAttribute('data-bill')==='annual'?'annual':'monthly',cu=d.getAttribute('data-cur')==='USD'?'usd':'aed',r=window.DP_REF;
    document.querySelectorAll('a[data-ck]').forEach(function(a){a.href=CK+'?plan='+a.getAttribute('data-ck')+'&billing='+bl+'&currency='+cu+(r?'&ref='+encodeURIComponent(r):'')})};
  // Currency switch
  document.addEventListener('click',function(e){
    var y=e.target.closest('[data-bill-set]');if(y){d.setAttribute('data-bill',y.getAttribute('data-bill-set'));DP_CK();return;}
    var b=e.target.closest('[data-set]');if(!b)return;
    var c=b.getAttribute('data-set');d.setAttribute('data-cur',c);
    try{localStorage.setItem('dp_cur',c)}catch(_){}
    DP_CK();
  });
  DP_CK();
  // Mobile nav
  var t=document.querySelector('.nav-toggle'),n=document.querySelector('.nav');
  if(t&&n)t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)});
  // Pricing tabs (panels stay in HTML for SEO; JS only hides the inactive ones)
  document.querySelectorAll('[role="tablist"]').forEach(function(list){
    var tabs=list.querySelectorAll('[role="tab"]');
    function show(tab){tabs.forEach(function(x){var on=x===tab;x.setAttribute('aria-selected',on);
      var p=document.getElementById(x.getAttribute('aria-controls'));if(p)p.hidden=!on;});}
    tabs.forEach(function(x){x.addEventListener('click',function(){show(x);history.replaceState(null,'','#'+x.getAttribute('aria-controls'))})});
    var h=location.hash.slice(1),start=h&&list.querySelector('[aria-controls="'+h+'"]');
    show(start||tabs[0]);
  });
})();
/* Affiliate referral: ?ref=CODE is kept 90 days (last click wins) and attached to every form, plan link and chat */
(function(){
  var K='dp_ref',DAYS=90,ok=/^[A-Za-z0-9_-]{2,24}$/;
  function get(){var m=document.cookie.match(/(?:^|; )dp_ref=([^;]+)/);if(m)return m[1];try{var s=JSON.parse(localStorage.getItem(K)||'null');if(s&&Date.now()-s.t<DAYS*864e5)return s.c}catch(_){}return ''}
  var q='';try{q=new URLSearchParams(location.search).get('ref')||''}catch(_){}
  if(q&&ok.test(q)){q=q.toUpperCase();
    document.cookie=K+'='+q+';max-age='+DAYS*86400+';path=/;SameSite=Lax'+(location.protocol==='https:'?';Secure':'');
    try{localStorage.setItem(K,JSON.stringify({c:q,t:Date.now()}))}catch(_){}
    var hook=document.body&&document.body.getAttribute('data-aff-hook');
    if(hook&&navigator.sendBeacon)try{navigator.sendBeacon(hook,new Blob([JSON.stringify({code:q,url:location.href,referrer:document.referrer})],{type:'application/json'}))}catch(_){}}
  var ref=get();window.DP_REF=ref;if(window.DP_CK)DP_CK();if(!ref)return;
  document.querySelectorAll('form').forEach(function(f){if(f.querySelector('input[name="ref"]'))return;var i=document.createElement('input');i.type='hidden';i.name='ref';i.value=ref;f.appendChild(i)});
  document.querySelectorAll('a[href*="?plan="]:not([data-ck])').forEach(function(a){if(a.href.indexOf('ref=')<0)a.href+='&ref='+encodeURIComponent(ref)});
})();

/* Site forms -> engine lead webhook (13 Oct 2026). DP_SEND(fields) resolves to {ok:true} or {ok:false,error}. */
(function(){
  var URL='https://engine.digipromise.com/webhook/site-form';
  window.DP_SEND=function(o){
    o=o||{};o.page=o.page||location.pathname;
    if(!o.ref){var r=window.DP_REF;if(!r){try{r=new URLSearchParams(location.search).get('ref')||''}catch(_){r=''}}if(r)o.ref=r}
    return fetch(URL,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(o)})
      .then(function(res){return res.json().catch(function(){return {ok:false,error:'Unexpected reply ('+res.status+')'}})})
      .catch(function(){return {ok:false,error:'network'}});
  };
})();
