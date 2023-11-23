function handleSelectionChange() {
    let selectElement = document.getElementById('orderSelect');
    let selectedOption = selectElement.options[selectElement.selectedIndex].value;

    if (selectedOption === '') {
        // Ignora a opção vazia
        return;
    }

    if (selectedOption === 'usuario') {
        showInputUsuario();
    }else{
        hideInputUsuario();
        document.getElementById('buttonSubmit').click();
    }
}

function showInputUsuario(){
    document.getElementById('buttonSubmit').style.display = 'block';
    document.getElementById('nameUser').style.display = 'block';
    document.getElementById('nameUser').style.display.focus();
}

function hideInputUsuario(){
    document.getElementById('buttonSubmit').style.display = 'none';
    document.getElementById('nameUser').style.display = 'none';
}