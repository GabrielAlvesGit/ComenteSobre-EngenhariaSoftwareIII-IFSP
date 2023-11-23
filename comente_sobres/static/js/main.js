function Ver(event) {
    document.getElementById("lista_topicos").style.display = "inherit";
}

function like(l) {
    document.getElementById("like " + l)
    let num = document.getElementById("nlikes " + l).innerHTML;
    num++;
    document.getElementById("nlikes " + l).innerHTML = num;

    document.getElementById("ilike " + l).style = `
    font-variation-settings: 'FILL'1, 'wght'600, 'GRAD'0, 'opsz'24;
`;
    document.getElementById("like " + l).style = "color: #BDB3FF;";
}