function drumhit(keyid) {
    var drum = document.getElementById(keyid);
    drum.play();
  }

function drumclick(audioid) {
    drumhit(audioid)
}

window.addEventListener("keydown", (event) => {
if (event.defaultPrevented) {
    return;
}

switch (event.key) {
    case "w":
    drumhit("wkey");
    break;
    case "a":
    drumhit("akey");
    break;
    case "s":
    drumhit("skey");
    break;
    case "d":
    drumhit("dkey");
    break;
    case "j":
    drumhit("jkey");
    break;
    case "k":
    drumhit("kkey");
    break;
    case "l":
    drumhit("lkey");
    break;
    default:
    return;
}

event.preventDefault();
}, true);
