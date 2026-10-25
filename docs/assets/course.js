document.addEventListener("DOMContentLoaded",()=>{
 const article=document.querySelector(".md-content__inner");if(!article)return;
 const bar=document.createElement("div");bar.className="course-toolbar";
 const print=document.createElement("button");print.type="button";print.className="course-print";print.textContent="Print this page";print.addEventListener("click",()=>window.print());bar.append(print);
 const checks=[...article.querySelectorAll('input[type="checkbox"]')];
 if(checks.length){const reset=document.createElement("button");reset.type="button";reset.className="course-reset";reset.textContent="Clear checks";reset.addEventListener("click",()=>{checks.forEach(c=>c.checked=false)});bar.append(reset);
 const note=document.createElement("span");note.textContent="Practice checks only. They clear on reload and do not record an assessment or equipment permission.";bar.append(note)}
 const h=article.querySelector("h1");h?.after(bar);
});
