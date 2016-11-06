function setTitle() {
var tit=document.domain.split(".").slice(-2).join(".");
document.title=tit;
alert(tit);
}
